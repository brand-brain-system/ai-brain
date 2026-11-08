#!/usr/bin/env python3
"""Transcribe audio longer than the model's limit by cutting it into overlapping chunks.

fal's Scribe v2 rejects audio over 1,200 s, and only says so when you fetch the result (422,
`audio_duration_too_long`). Raw creator files of 20-30 minutes are normal, so cut first:

  python transcript-chunks.py split  <audio> <outdir> [--max 1100] [--overlap 5]
      Writes chunk-1.mp3, chunk-2.mp3 ... (mono, 64 kbps) and chunks.json (the offsets). Audio at or
      under --max seconds is not cut: it prints "single" and you transcribe the file as it is.

  (upload each chunk with the fal MCP's upload_file, run the model on each, save each result as JSON)

  python transcript-chunks.py merge  <chunks.json> <result-1.json> <result-2.json> ... -o transcript.json [--md transcript.md]
      Joins the results into one word list on the original timeline. In each overlap the first chunk
      keeps the words that start before the middle of it, the next chunk the rest, so no word is
      doubled or cut off at the seam. Result files may be the raw model output or the MCP's saved
      wrapper ({"result": {...}}).

Speaker labels are not consistent between chunks (each chunk numbers its speakers again). Fine for one
speaker; for several, treat the labels as per chunk.

The cut re-encodes audio only, at below-normal priority: light on the PC.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


def ffmpeg_bin(name):
    path = shutil.which(name)
    if not path:
        sys.exit(f"{name} not found on PATH (open a new terminal after installing ffmpeg)")
    return path


def duration(audio):
    out = subprocess.run([ffmpeg_bin("ffprobe"), "-v", "error", "-show_entries", "format=duration",
                          "-of", "default=nw=1:nk=1", str(audio)], capture_output=True, text=True)
    try:
        return float(out.stdout.strip())
    except ValueError:
        sys.exit(f"could not read the length of {audio}: {out.stderr.strip()}")


def low_priority():
    if os.name == "nt":
        return {"creationflags": 0x00004000}  # BELOW_NORMAL_PRIORITY_CLASS
    return {"preexec_fn": lambda: os.nice(10)}


def split(args):
    audio, outdir = Path(args.audio), Path(args.outdir)
    total = duration(audio)
    if total <= args.max:
        print(f"single: {total:.0f} s is within {args.max:.0f} s, transcribe the file as it is")
        return
    if args.overlap * 4 >= args.max:
        sys.exit("--overlap is too large for --max")
    outdir.mkdir(parents=True, exist_ok=True)
    step = args.max - args.overlap
    chunks, start, n = [], 0.0, 0
    while start < total - args.overlap:  # no chunk made only of the overlap
        n += 1
        length = min(args.max, total - start)
        name = f"chunk-{n}.mp3"
        cmd = [ffmpeg_bin("ffmpeg"), "-v", "error", "-y", "-ss", f"{start:.3f}", "-i", str(audio),
               "-t", f"{length:.3f}", "-ac", "1", "-b:a", "64k", str(outdir / name)]
        if subprocess.run(cmd, **low_priority()).returncode:
            sys.exit(f"ffmpeg failed on {name}")
        chunks.append({"file": name, "offset": round(start, 3), "length": round(length, 3)})
        start += step
    meta = {"source": str(audio), "total": round(total, 3), "overlap": args.overlap, "chunks": chunks}
    (outdir / "chunks.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(f"{len(chunks)} chunks in {outdir}:")
    for c in chunks:
        print(f"  {c['file']}  starts at {c['offset']:.0f} s, {c['length']:.0f} s long")


def norm(text):
    return re.sub(r"\W", "", text.lower())


def load_result(path):
    raw = Path(path).read_text(encoding="utf-8-sig")
    data = json.loads(raw[raw.index("{"):])  # the MCP may put a line of text before the JSON
    data = data.get("result", data)
    if "words" not in data:
        sys.exit(f"{path} has no word list (a failed job, or the wrong file)")
    return data


def merge(args):
    meta = json.loads(Path(args.chunks).read_text(encoding="utf-8-sig"))
    chunks, overlap = meta["chunks"], meta["overlap"]
    if len(chunks) != len(args.results):
        sys.exit(f"chunks.json lists {len(chunks)} chunks but {len(args.results)} result files were given")
    words = []
    for i, (chunk, path) in enumerate(zip(chunks, args.results)):
        lo = chunk["offset"] + overlap / 2 if i > 0 else float("-inf")
        hi = chunks[i + 1]["offset"] + overlap / 2 if i + 1 < len(chunks) else float("inf")
        first = True
        for w in load_result(path)["words"]:
            if w.get("type") != "word" or w.get("start") is None:
                continue
            start = round(w["start"] + chunk["offset"], 2)
            if not lo <= start < hi:
                continue
            # A word sitting on the seam can be heard by both chunks a few hundredths apart,
            # on either side of the cut. Only at the seam: drop it if it repeats the last word.
            if first and i > 0 and words and norm(words[-1]["text"]) == norm(w["text"]) \
                    and start - words[-1]["start"] < 0.5:
                first = False
                continue
            first = False
            words.append({"text": w["text"], "start": start,
                          "end": round(w["end"] + chunk["offset"], 2),
                          "speaker_id": w.get("speaker_id")})
    words.sort(key=lambda w: w["start"])
    Path(args.output).write_text(json.dumps(words, ensure_ascii=False), encoding="utf-8")
    print(f"{len(words)} words, last ends at {words[-1]['end']:.1f} s (source {meta['total']:.1f} s) -> {args.output}")
    if args.md:
        write_paragraphs(words, args.md)


def write_paragraphs(words, path):
    paras, cur = [], []
    for w in words:
        if cur and (w["speaker_id"] != cur[-1]["speaker_id"]
                    or (len(cur) >= 70 and re.search(r"[.?!]$", cur[-1]["text"]))
                    or w["start"] - cur[-1]["end"] > 2.5):
            paras.append(cur)
            cur = []
        cur.append(w)
    if cur:
        paras.append(cur)
    lines = [f"[{int(p[0]['start'] // 60):02d}:{int(p[0]['start'] % 60):02d}] {p[0]['speaker_id'] or '?'}: "
             + " ".join(w["text"] for w in p) for p in paras]
    Path(path).write_text("\n\n".join(lines), encoding="utf-8")
    print(f"{len(paras)} paragraphs -> {path}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("split")
    s.add_argument("audio")
    s.add_argument("outdir")
    s.add_argument("--max", type=float, default=1100, help="longest chunk in seconds (model limit 1200)")
    s.add_argument("--overlap", type=float, default=5, help="seconds shared by neighbouring chunks")
    s.set_defaults(fn=split)
    m = sub.add_parser("merge")
    m.add_argument("chunks")
    m.add_argument("results", nargs="+")
    m.add_argument("-o", "--output", required=True)
    m.add_argument("--md", help="also write a readable transcript with timestamps")
    m.set_defaults(fn=merge)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()

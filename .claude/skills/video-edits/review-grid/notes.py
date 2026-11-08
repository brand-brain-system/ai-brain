#!/usr/bin/env python3
"""Read and answer review notes from the command line (the same review-notes.json the page uses).

  python notes.py list   <run folder> [--ad B014] [--hook H1] [--all]    open notes (all with --all)
  python notes.py reply  <run folder> <note id> "what changed, in which version, at what time" [--keep-open]
  python notes.py add    <run folder> <video file> <seconds> "text" [--author QA]
  python notes.py next   <run folder> <ad> [<hook>]                        the next version's file name
  python notes.py status <run folder>                                       one line per ad and hook

reply marks the note done unless --keep-open (use it for a question back to the human). add stores the
words spoken at that moment when the video has a .words.json, so a QA finding reads like a human note.
"""
import argparse
import importlib.util
import json
import sys
from pathlib import Path

_spec = importlib.util.spec_from_file_location("review_serve", Path(__file__).resolve().parent / "serve.py")
serve = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(serve)


def words_at(folder, video, t, span=1.2):
    f = Path(folder) / (Path(video).stem + ".words.json")
    if not f.exists():
        return ""
    ws = json.loads(f.read_text(encoding="utf-8-sig"))
    return " ".join(w["w"] for w in ws if w["e"] >= t - span and w["s"] <= t + span)


def fmt(t):
    m = int(t // 60)
    return f"{m}:{t - m * 60:04.1f}"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("list"); p.add_argument("folder"); p.add_argument("--ad"); p.add_argument("--hook"); p.add_argument("--all", action="store_true")
    p = sub.add_parser("reply"); p.add_argument("folder"); p.add_argument("id"); p.add_argument("text"); p.add_argument("--keep-open", action="store_true")
    p = sub.add_parser("add"); p.add_argument("folder"); p.add_argument("video"); p.add_argument("seconds", type=float); p.add_argument("text"); p.add_argument("--author", default="QA")
    p = sub.add_parser("next"); p.add_argument("folder"); p.add_argument("ad"); p.add_argument("hook", nargs="?", default="Main")
    p = sub.add_parser("status"); p.add_argument("folder")
    a = ap.parse_args()
    review = serve.Review(a.folder)

    if a.cmd == "list":
        notes = [n for n in review.load()["notes"] if (a.all or n["status"] == "open")
                 and (not a.ad or n["ad"] == a.ad) and (not a.hook or n["hook"] == a.hook)]
        for n in sorted(notes, key=lambda n: (n["ad"], n["hook"], n["version"], n["t"])):
            print(f'{n["id"]:4} {n["ad"]}/{n["hook"]} v{n["version"]} {fmt(n["t"])} [{n["status"]}] {n["author"]}'
                  f'{" GENERAL" if n.get("general") else ""}\n     words: "{n.get("words", "")}"\n     note:  {n["text"]}'
                  + (f'\n     reply: {n["reply"]}' if n.get("reply") else ""))
        if not notes:
            print("no open notes" if not a.all else "no notes")
    elif a.cmd == "reply":
        with serve.LOCK:
            data = review.load()
            note = next((n for n in data["notes"] if n["id"] == a.id), None)
            if not note:
                sys.exit(f"no note {a.id}")
            note["reply"] = a.text
            note["status"] = "open" if a.keep_open else "done"
            review.save(data)
        print(f'{a.id}: {note["status"]}')
    elif a.cmd == "add":
        ad, hook, v = serve.parse_name(a.video)
        note = review.add_note({"ad": ad, "hook": hook, "version": v, "t": a.seconds,
                                "words": words_at(a.folder, a.video, a.seconds), "text": a.text}, author=a.author)
        print(f'{note["id"]}: {ad}/{hook} v{v} {fmt(a.seconds)} by {note["author"]}')
    elif a.cmd == "next":
        hook = next((h for ad in review.ads() if ad["id"] == a.ad for h in ad["hooks"] if h["id"] == a.hook), None)
        if not hook:
            sys.exit(f"no {a.ad}/{a.hook} in {a.folder}")
        print(serve.next_name(a.ad, a.hook, hook["latest"] + 1))
    elif a.cmd == "status":
        for ad in review.ads():
            for h in ad["hooks"]:
                print(f'{ad["id"]}/{h["id"]}: v{h["latest"]} {h["status"]}' + (f', {h["open"]} open' if h["open"] else ""))


if __name__ == "__main__":
    main()

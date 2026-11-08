#!/usr/bin/env python3
"""The edit review: watch each ad and hook, leave timestamped notes, read Claude's answers, approve.

  python serve.py <run folder> [--glob "*preview*.mp4"] [--checks checks.json] [--port 8766] [--no-open]

Starting it also writes "Open review.cmd" (Windows) or "Open review.command" (macOS) into the run folder:
double-click it to start the page again after a restart. If the server is already running, it only opens
the page. Start it as its own process (Windows: Start-Process), not a background job of a Claude session.

Why a server: a page opened as a bare file or in an app's HTML viewer can't load the videos next to it.
Nothing leaves the machine: it listens on 127.0.0.1 only, serves only video, caption, image and word files
at the top of the run folder (not its subfolders), and accepts changes only from its own page.

Names (parsed from the file name, "_preview" ignored):
  <ad>_<hook>_v<N>        e.g. B014_H3_v2, C07_B014_H3_15s_v3      hook = H<n> with an optional _<len>s
  <ad>_<hook>             version 1                                 (<ad>_<hook>v2 is read the same way)
  <ad>_v<N> or <ad>       hook "Main"
A word file next to a video, <video stem>.words.json = [{"w": "word", "s": 1.23, "e": 1.5}, ...] on the
video's own timeline, gives the transcript line and the words stored with each note. The render writes it.

review-notes.json in the run folder is the shared record, read fresh on every request:
  {"notes": [{"id": "n1", "ad": "B014", "hook": "H1", "version": 2, "t": 6.6, "words": "...",
              "text": "...", "general": false, "author": "you" | "QA" | ..., "status": "open" | "done" |
              "dismissed", "reply": "", "created": "..."}],
   "approved": {"B014/H1": 2}}
A hook is approved only while its approved version is its latest one. notes.py reads and answers notes.
"""
import argparse
import datetime
import functools
import json
import os
import re
import socket
import sys
import threading
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
ALLOWED = {".mp4", ".mov", ".webm", ".srt", ".png", ".jpg", ".jpeg"}
LOCK = threading.Lock()


def parse_name(filename):
    """(ad, hook, version) from a video file name."""
    stem = re.sub(r"[_-]?preview$", "", Path(filename).stem)
    m = re.match(r"^(.*?)(?:[_-]?v(\d+))?$", stem)
    base, version = m.group(1), int(m.group(2) or 1)
    h = re.match(r"^(.+?)[_-](H\d+(?:[_-]\d+s)?)$", base)
    return (h.group(1), h.group(2), version) if h else (base, "Main", version)


def next_name(ad, hook, version):
    return f"{ad}_v{version}_preview.mp4" if hook == "Main" else f"{ad}_{hook}_v{version}_preview.mp4"


class Review:
    def __init__(self, folder, glob="*preview*.mp4", checks=None):
        self.folder, self.glob, self.checks = Path(folder), glob, checks or {}
        self.notes_file = self.folder / "review-notes.json"

    def videos(self):
        return sorted(p.name for p in self.folder.glob(self.glob)) or sorted(p.name for p in self.folder.glob("*.mp4"))

    def ads(self, data=None):
        data = data or self.load()
        tree = {}
        for f in self.videos():
            ad, hook, v = parse_name(f)
            words = Path(f).stem + ".words.json"
            tree.setdefault(ad, {}).setdefault(hook, []).append(
                {"v": v, "file": f, "check": self.checks.get(f, ""),
                 "words": words if (self.folder / words).exists() else None})
        out = []
        for ad, hooks in tree.items():
            hs = []
            for hook, versions in sorted(hooks.items(), key=lambda kv: (kv[0] != "Main", kv[0])):
                versions.sort(key=lambda x: x["v"])
                latest = versions[-1]["v"]
                open_notes = sum(1 for n in data["notes"] if n["ad"] == ad and n.get("hook", "Main") == hook
                                 and n["status"] == "open")
                status = ("approved" if data["approved"].get(f"{ad}/{hook}") == latest
                          else "notes" if open_notes else "review")
                hs.append({"id": hook, "versions": versions, "latest": latest, "status": status, "open": open_notes})
            out.append({"id": ad, "hooks": hs})
        return out

    def load(self):
        try:
            data = json.loads(self.notes_file.read_text(encoding="utf-8-sig"))
        except (FileNotFoundError, ValueError):
            data = {}
        data.setdefault("notes", [])
        data.setdefault("approved", {})
        for n in data["notes"]:
            n.setdefault("hook", "Main")
        return data

    def save(self, data):
        tmp = self.notes_file.with_suffix(".tmp")
        tmp.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
        os.replace(tmp, self.notes_file)

    def state(self):
        data = self.load()
        return {"title": self.folder.name, "ads": self.ads(data), **data}

    def add_note(self, body, author="you"):
        text = str(body.get("text", "")).strip()
        if not text:
            raise ValueError("empty note")
        with LOCK:
            data = self.load()
            n = max([int(x["id"][1:]) for x in data["notes"] if re.fullmatch(r"n\d+", x.get("id", ""))] or [0]) + 1
            note = {"id": f"n{n}", "ad": str(body["ad"]), "hook": str(body.get("hook") or "Main"),
                    "version": int(body["version"]), "t": round(float(body["t"]), 1),
                    "words": str(body.get("words", ""))[:300], "text": text, "general": bool(body.get("general")),
                    "author": str(body.get("author") or author)[:20], "status": "open", "reply": "",
                    "created": datetime.datetime.now().isoformat(timespec="seconds")}
            data["notes"].append(note)
            self.save(data)
            return note

    def change(self, body):
        with LOCK:
            data = self.load()
            nid = body.get("id")
            if body.get("delete"):
                data["notes"] = [n for n in data["notes"] if n["id"] != nid]
            else:
                if body.get("status") not in ("open", "done", "dismissed"):
                    raise ValueError("bad status")
                for n in data["notes"]:
                    if n["id"] == nid:
                        n["status"] = body["status"]
            self.save(data)

    def approve(self, body):
        with LOCK:
            data = self.load()
            key = f'{body["ad"]}/{body.get("hook") or "Main"}'
            v = body.get("version")
            if v is None or data["approved"].get(key) == v:
                data["approved"].pop(key, None)        # pressing it again takes the approval back
            else:
                data["approved"][key] = int(v)
            self.save(data)


class Handler(SimpleHTTPRequestHandler):
    review = None

    def log_message(self, *args):
        pass

    def send_bytes(self, data, ctype, code=200):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def send_json(self, obj, code=200):
        self.send_bytes(json.dumps(obj, ensure_ascii=False).encode("utf-8"), "application/json", code)

    def do_GET(self):
        path = self.path.split("?")[0]
        if path in ("/", "/index.html"):
            return self.send_bytes((HERE / "grid.html").read_bytes(), "text/html; charset=utf-8")
        if path == "/state":
            return self.send_json(self.review.state())
        parts = [p for p in path.split("/") if p]
        ok = len(parts) == 1 and (Path(path).suffix.lower() in ALLOWED or path.endswith(".words.json"))
        if not ok:
            return self.send_error(404)  # top of the run folder only: raw footage in subfolders stays unserved
        return super().do_GET()

    def do_POST(self):
        # Only our own page may change anything: a custom header can't be sent cross-site without a
        # preflight this server never answers, and the Origin, when sent, must be this server.
        origin = self.headers.get("Origin")
        if self.headers.get("X-Review-Page") != "1" or (origin and origin != f"http://{self.headers.get('Host')}"):
            return self.send_error(403)
        length = int(self.headers.get("Content-Length") or 0)
        if length > 100_000:
            return self.send_error(413)
        try:
            body = json.loads(self.rfile.read(length) or b"{}")
            action = {"/notes": self.review.add_note, "/notes/change": self.review.change,
                      "/approve": self.review.approve}.get(self.path.split("?")[0])
            if not action:
                return self.send_error(404)
            action(body)
        except (ValueError, KeyError, TypeError) as e:
            return self.send_json({"error": str(e)}, 400)
        return self.send_json(self.review.state())

    def send_head(self):
        rng = self.headers.get("Range")
        path = self.translate_path(self.path)
        m = re.match(r"bytes=(\d*)-(\d*)$", rng or "")
        if not m or not os.path.isfile(path):
            return super().send_head()
        size = os.path.getsize(path)
        start = int(m.group(1)) if m.group(1) else 0
        end = min(int(m.group(2)) if m.group(2) else size - 1, size - 1)
        f = open(path, "rb")
        f.seek(start)
        self.send_response(206)
        self.send_header("Content-Type", self.guess_type(path))
        self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        self.send_header("Content-Length", str(end - start + 1))
        self.end_headers()
        self._left = end - start + 1
        return f

    def copyfile(self, source, outputfile):
        left = getattr(self, "_left", None)
        if left is None:
            return super().copyfile(source, outputfile)
        while left > 0:
            chunk = source.read(min(65536, left))
            if not chunk:
                break
            outputfile.write(chunk)
            left -= len(chunk)
        self._left = None

    def end_headers(self):
        self.send_header("Accept-Ranges", "bytes")
        super().end_headers()


def write_launcher(folder, argv):
    """A double-clickable file in the run folder that starts this page again."""
    cmd = [sys.executable, str(Path(__file__).resolve()), str(folder)] + [a for a in argv if a != "--no-open"]
    if os.name == "nt":
        path = folder / "Open review.cmd"
        path.write_text("@echo off\r\n" + " ".join(f'"{c}"' for c in cmd) + "\r\n", encoding="utf-8", newline="")
    else:
        path = folder / "Open review.command"
        path.write_text("#!/bin/sh\n" + " ".join("'" + c.replace("'", "'\\''") + "'" for c in cmd) + "\n", encoding="utf-8")
        path.chmod(0o755)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folder")
    ap.add_argument("--glob", default="*preview*.mp4")
    ap.add_argument("--checks")
    ap.add_argument("--port", type=int, default=8766)
    ap.add_argument("--no-open", action="store_true")
    args = ap.parse_args()

    folder = Path(args.folder).resolve()
    if not folder.is_dir():
        sys.exit(f"{folder} is not a folder")
    url = f"http://127.0.0.1:{args.port}/"
    with socket.socket() as s:
        if s.connect_ex(("127.0.0.1", args.port)) == 0:     # already running: just open the page
            print(f"The review is already running: {url}")
            if not args.no_open:
                webbrowser.open(url)
            return
    checks = json.loads(Path(args.checks).read_text(encoding="utf-8-sig")) if args.checks else {}
    Handler.review = Review(folder, args.glob, checks)
    if not Handler.review.videos():
        sys.exit(f"no videos in {folder}")
    extra = ["--glob", args.glob, "--port", str(args.port)] + (["--checks", str(Path(args.checks).resolve())] if args.checks else [])
    write_launcher(folder, extra)

    server = ThreadingHTTPServer(("127.0.0.1", args.port), functools.partial(Handler, directory=str(folder)))
    print(f"Edit review for {folder.name}: {url}  (notes in review-notes.json; Ctrl+C or close this window to stop)")
    if not args.no_open:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("stopped")


if __name__ == "__main__":
    main()

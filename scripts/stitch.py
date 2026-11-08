"""Stitch screenshot pieces top to bottom into one PNG, and make before/after side-by-sides.

Usage:
  python stitch.py <out.png> <piece0.png> <piece1.png> ...
  python stitch.py --side <before.png> <after.png> <out.png> [--top Y --height H]
      (--top/--height crop the same band from both, for a change in one section)

Part of the site-watch routine (schedules/site-watch.md). Needs Pillow.
"""
import sys
from PIL import Image

Image.MAX_IMAGE_PIXELS = None


def stitch(out, parts):
    ims = [Image.open(p).convert("RGB") for p in parts]
    w = max(i.width for i in ims)
    canvas = Image.new("RGB", (w, sum(i.height for i in ims)), "white")
    y = 0
    for i in ims:
        canvas.paste(i, (0, y))
        y += i.height
    canvas.save(out, optimize=True)


def side(before, after, out, top=None, height=None):
    a, b = Image.open(before).convert("RGB"), Image.open(after).convert("RGB")
    if top is not None:
        h = height or 1200
        a, b = a.crop((0, top, a.width, min(a.height, top + h))), b.crop((0, top, b.width, min(b.height, top + h)))
    gap = 24
    canvas = Image.new("RGB", (a.width + b.width + gap, max(a.height, b.height)), (220, 220, 220))
    canvas.paste(a, (0, 0))
    canvas.paste(b, (a.width + gap, 0))
    canvas.save(out, optimize=True)


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--side":
        opts = dict(zip(args[4::2], args[5::2]))
        side(args[1], args[2], args[3],
             int(opts["--top"]) if "--top" in opts else None,
             int(opts["--height"]) if "--height" in opts else None)
    elif len(args) >= 2:
        stitch(args[0], args[1:])
    else:
        print(__doc__)
        sys.exit(2)

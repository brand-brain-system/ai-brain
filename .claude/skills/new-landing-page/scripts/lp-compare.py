#!/usr/bin/env python3
"""Put a reference capture and a draft capture side by side, in strips, for the look check (step 6).

Usage: python3 lp-compare.py <reference.png> <draft.png> <out-prefix> [--strip 1400] [--width 1440]

Both images are scaled to the same width, cut into strips of the same height, and written as
<out-prefix>-01.jpg, -02.jpg ... with the reference on the left and the draft on the right.
Read every strip: the draft should pass for the reference with the words blurred.
"""
import sys, os
from PIL import Image, ImageDraw


def main():
    argv = sys.argv[1:]
    # positional args only: skip each --flag and the value after it (fixed 2026-10-01: '--width 390' was read as a path)
    args = [a for i, a in enumerate(argv) if not a.startswith('--') and not (i and argv[i - 1] in ('--strip', '--width'))]
    if len(args) != 3:
        sys.exit(__doc__)
    ref_p, draft_p, out = args
    opt = lambda k, d: int(sys.argv[sys.argv.index(k) + 1]) if k in sys.argv else d
    strip, width = opt('--strip', 1400), opt('--width', 0)
    ref, draft = Image.open(ref_p).convert('RGB'), Image.open(draft_p).convert('RGB')
    w = width or min(ref.width, draft.width)
    scale = lambda im: im.resize((w, round(im.height * w / im.width)))
    ref, draft = scale(ref), scale(draft)
    sh = round(strip * w / 1440) if w != 1440 else strip
    n = max(-(-ref.height // sh), -(-draft.height // sh))
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    gap, label = 24, 36
    for i in range(n):
        y = i * sh
        canvas = Image.new('RGB', (w * 2 + gap, sh + label), (255, 255, 255))
        d = ImageDraw.Draw(canvas)
        d.text((10, 10), f'REFERENCE  {i + 1}/{n}', fill=(200, 0, 0))
        d.text((w + gap + 10, 10), f'DRAFT  {i + 1}/{n}', fill=(0, 120, 0))
        for k, im in enumerate((ref, draft)):
            if y < im.height:
                canvas.paste(im.crop((0, y, w, min(im.height, y + sh))), (k * (w + gap), label))
        if w > 800:  # halve desktop strips only; phone strips stay at full size so they can be read
            canvas = canvas.resize((canvas.width // 2, canvas.height // 2))
        p = f'{out}-{i + 1:02d}.jpg'
        canvas.save(p, quality=78)
        print('wrote', p)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Prepare draft-4 images from the brand-assets pull: cut packshots out of their light backgrounds,
trim transparent cutouts, size and compress everything into assets/v4/ (webp keeps alpha)."""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageChops
RUN = os.path.dirname(os.path.abspath(__file__))
BA = os.path.join(RUN, '../../../other/brand-assets')
SITE, PROD = BA + '/other-assets/site/', BA + '/other-assets/products/'
OUT = os.path.join(RUN, 'assets/v4'); os.makedirs(OUT, exist_ok=True)

def trim(im, pad=8):
    a = im.split()[3].point(lambda v: 255 if v > 12 else 0); bb = a.getbbox()
    x0, y0, x1, y1 = bb; return im.crop((max(0, x0 - pad), max(0, y0 - pad), min(im.width, x1 + pad), min(im.height, y1 + pad)))

def knockout(path, tol=48):
    im = Image.open(path).convert('RGB'); w, h = im.size
    bg = im.getpixel((6, 6))
    diff = ImageChops.difference(im, Image.new('RGB', im.size, bg)).convert('L')
    m = diff.point(lambda v: 255 if v > tol else 0)            # foreground candidates
    # flood the background from the corners so dark-on-light text inside the pack is kept
    mask = m.copy(); ImageDraw.floodfill(mask, (0, 0), 128); ImageDraw.floodfill(mask, (w - 1, 0), 128)
    mask = mask.point(lambda v: 0 if v == 128 else 255).filter(ImageFilter.GaussianBlur(1.2))
    rgba = im.convert('RGBA'); rgba.putalpha(mask); return trim(rgba)

def save(im, name, size, q=82):
    im = im.copy(); im.thumbnail((size, size), Image.LANCZOS)
    p = os.path.join(OUT, name)
    if name.endswith('.webp'): im.save(p, 'WEBP', quality=q, method=6)
    else: im.convert('RGB').save(p, 'JPEG', quality=q, optimize=True, progressive=True)
    print(name, im.size, os.path.getsize(p) // 1024, 'KB')

def sq(path, box=None):
    im = Image.open(path).convert('RGB')
    if box: im = im.crop(box)
    return im

save(knockout(BA + '/the-good-stuff-pouch--01.png'), 'pouch-cinnamon.webp', 900)
save(knockout(PROD + 'the-good-stuff-pouch--02.png'), 'pouch-mocha.webp', 900)
save(knockout(PROD + 'the-good-stuff-pouch--03.png'), 'pouch-vanilla.webp', 900)
save(trim(Image.open(SITE + 'showcase_the-good-stuff-pouch.png').convert('RGBA')), 'pour.webp', 1200)
save(trim(Image.open(SITE + 'showcase_the-good-stuff-travel-sticks.png').convert('RGBA')), 'sticks-pack.webp', 900)
save(knockout(BA + '/the-good-stuff-travel-sticks--01.png'), 'sticks.webp', 700)
save(trim(Image.open(PROD + 'ceramic-canister--01.png').convert('RGBA')), 'canister.webp', 600)
save(sq(SITE + 'tgs-hero-desktop.png'), 'kit.jpg', 1600, 84)
save(sq(SITE + 'feature-4.jpg'), 'life-stir.jpg', 1100)
save(sq(SITE + 'feature-1.jpg'), 'life-sip.jpg', 1100)
save(sq(SITE + 'Dave_Hero.png'), 'life-dave.jpg', 1500)
save(sq(SITE + 'Focus.png'), 'life-desk.jpg', 1000)
save(sq(SITE + 'fw-video-gym-desktop-poster.jpg'), 'life-kitchen.jpg', 1400)
for f, n in (('2_-_Collagen.jpg', 'ing-collagen'), ('3_-_MCT.jpg', 'ing-mct'), ('1_-_L-Theanine.jpg', 'ing-theanine'), ('13_-_Organic_Cinnamon.jpg', 'ing-cinnamon')):
    im = Image.open(SITE + f).convert('RGB'); w, h = im.size; s = min(w, h)
    save(im.crop((0, (h - s) // 2 - int(h * .08), s, (h - s) // 2 - int(h * .08) + s)), n + '.jpg', 420)

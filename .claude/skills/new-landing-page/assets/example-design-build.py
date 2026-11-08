#!/usr/bin/env python3
"""Draft 4: the For Wellness Welcome Kit page, built to the reference's level (gruns-2) in For Wellness's own look.

Every word comes from page.json (the approved copy); this file holds only layout, styling and a little behaviour.
Structure follows the reference's page (see design-spec.md); the look is For Wellness's: Messina Sans (the brand
font, assets/fonts), the pouch's matte black and wide-tracked caps, the three flavour colours, coffee-surface waves
instead of the reference's candy scallops, real site photography (assets/v4, made by prep-assets.py).
Writes one self-contained HTML file with fonts and photos embedded. Built on draft 2 (no 21st.dev components),
per Alex Cooper 2026-09-30; the 21st.dev version is kept as build-design.v3-21st.py.

Usage: python3 build-design.py [--labels]
"""
import json, os, sys, base64, html, re

RUN = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(os.path.join(RUN, 'page.json')))
B = json.load(open(os.path.join(RUN, 'brief.json')))
S = {s['id']: s['fields'] for s in P['sections']}
LABELS = '--labels' in sys.argv
CTA_URL = (P.get('meta') or {}).get('cta_url') or B.get('cta_url') or '#'
PH = re.compile(r'(\[(?:OFFER|STAT NEEDED|PHOTO|CODE|DATE|PRICE|CREATOR VIDEO)[^\]]*\])')
MIME = {'png': 'image/png', 'jpg': 'image/jpeg', 'jpeg': 'image/jpeg', 'webp': 'image/webp', 'woff2': 'font/woff2'}


def T(s):
    return PH.sub(r'<mark class="ph">\1</mark>', html.escape(str(s or ''), quote=True)).replace('\n', '<br>')


def A(s):
    return html.escape(str(s or ''), quote=True)


def data(path):
    return f'data:{MIME[path.rsplit(".", 1)[1].lower()]};base64,' + base64.b64encode(open(os.path.join(RUN, path), 'rb').read()).decode()


def tag(sid):
    return f'<span class="sid">{sid.upper()}</span>' if LABELS else ''


def btn(label, cls='pill'):
    return f'<a class="{cls}" href="{A(CTA_URL)}">{T(label)}</a>'


def wave(cls):
    # a soft coffee-surface curve; colour comes from CSS `color`
    return (f'<svg class="wave {cls}" viewBox="0 0 1440 60" preserveAspectRatio="none" aria-hidden="true">'
            '<path d="M0 34 C 180 6 360 6 540 30 S 900 58 1080 34 S 1350 8 1440 26 V60 H0Z" fill="currentColor"/></svg>')


def stars(score=4.6):
    out = []
    for i in range(5):
        fill = max(0.0, min(1.0, score - i))
        out.append(f'<span class="st"><span style="width:{fill * 100:.0f}%"></span></span>')
    return f'<span class="stars" role="img" aria-label="{score} out of 5 stars">{"".join(out)}</span>'


V = 'assets/v4/'
IMG = {k: data(V + f) for k, f in {
    'cin': 'pouch-cinnamon.webp', 'moc': 'pouch-mocha.webp', 'van': 'pouch-vanilla.webp', 'pour': 'pour.webp',
    'sticks': 'sticks.webp', 'stickspack': 'sticks-pack.webp', 'can': 'canister.webp', 'stir': 'life-stir.jpg',
    'sip': 'life-sip.jpg', 'dave': 'life-dave.jpg', 'i_col': 'ing-collagen.jpg', 'i_mct': 'ing-mct.jpg',
    'i_the': 'ing-theanine.jpg', 'i_cin': 'ing-cinnamon.jpg'}.items()}
IMG['kit'] = data('assets/kit-hero.jpg')
LOGO, LOGO_W = data('assets/ForWellness-Logo.png'), data('assets/ForWellness-Logo-white.png')
FONT_BOOK, FONT_BOLD = data('assets/fonts/MessinaSansWeb-Book.woff2'), data('assets/fonts/MessinaSansWeb-Bold.woff2')

CHECK = '<svg class="ck" viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="10"/><path d="M5.6 10.3l2.9 2.9 5.9-6.4" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ICON = {
    'mug': '<svg viewBox="0 0 40 40"><path d="M8 15h19v9a8 8 0 0 1-8 8h-3a8 8 0 0 1-8-8z" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M27 18h3a4 4 0 0 1 0 8h-3" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M14 6c-2 2 2 3 0 6M20 6c-2 2 2 3 0 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
    'jug': '<svg viewBox="0 0 40 40"><path d="M15 7h9l3 7v18a2 2 0 0 1-2 2H13a2 2 0 0 1-2-2V14z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/><path d="M11 21h16" stroke="currentColor" stroke-width="2.2"/></svg>',
    'loop': '<svg viewBox="0 0 40 40"><path d="M30 15a11 11 0 1 0 1 9" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/><path d="M31 8v7h-7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'nocup': '<svg viewBox="0 0 40 40"><path d="M11 16h16v8a7 7 0 0 1-7 7h-2a7 7 0 0 1-7-7z" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M8 32L32 8" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>',
    'truck': '<svg viewBox="0 0 40 40"><path d="M5 11h19v16H5zM24 17h6l5 5v5H24z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/><circle cx="12" cy="29" r="3" fill="#fff" stroke="currentColor" stroke-width="2.2"/><circle cx="29" cy="29" r="3" fill="#fff" stroke="currentColor" stroke-width="2.2"/></svg>',
    'pause': '<svg viewBox="0 0 40 40"><circle cx="20" cy="20" r="14" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M17 14v12M23 14v12" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/></svg>',
    'box': '<svg viewBox="0 0 40 40"><path d="M6 13l14-6 14 6v15l-14 6-14-6z M6 13l14 6 14-6 M20 19v15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>',
    'frother': '<svg viewBox="0 0 40 40"><path d="M20 3v21" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/><rect x="16.5" y="3" width="7" height="12" rx="3" fill="currentColor"/><circle cx="20" cy="29" r="6" fill="none" stroke="currentColor" stroke-width="2"/><path d="M15.5 26.5c3 2 6 2 9 0M15.5 31.5c3-2 6-2 9 0" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>',
    'scoop': '<svg viewBox="0 0 40 40"><path d="M5 22a9 7 0 0 0 18 0z" fill="currentColor"/><path d="M22 21l14-9" stroke="currentColor" stroke-width="3.2" stroke-linecap="round"/></svg>',
    'play': '<svg viewBox="0 0 40 40"><circle cx="20" cy="20" r="19" fill="rgba(0,0,0,.45)" stroke="#fff" stroke-width="2"/><path d="M16 12l12 8-12 8z" fill="#fff"/></svg>',
}

s01, s02, s03, s04, s05 = (S[k] for k in ('s01', 's02', 's03', 's04', 's05'))
s08, s09, s10, s11, s12, s13, s14, s15 = (S[k] for k in ('s08', 's09', 's10', 's11', 's12', 's13', 's14', 's15'))
FLAV = {'Cinnamon': ('cin', '#C9681C'), 'Vanilla': ('van', '#A8822A'), 'Mocha': ('moc', '#6E4630')}


def split_note(note):
    return [x.strip() + '.' for x in note.rstrip('.').split('. ') if x.strip()]


o90, o30 = s05['options']
kit_banner = next((x for x in split_note(o90['note']) if 'Welcome Kit' in x), '').rstrip('.')

# ---------------- hero ----------------
ring_txt = A(s03['items'][0].upper())
sticker = ('<div class="sticker" aria-hidden="true"><svg viewBox="0 0 200 200"><defs><path id="ring" d="M100 100 m-76 0 a76 76 0 1 1 152 0 a76 76 0 1 1 -152 0"/></defs>'
           '<circle cx="100" cy="100" r="99" fill="#161412"/><circle cx="100" cy="100" r="62" fill="none" stroke="#E0842A" stroke-width="1.5"/>'
           f'<text class="ring"><textPath href="#ring" textLength="470">{ring_txt} · {ring_txt} ·</textPath></text></svg>'
           '<b>FREE</b></div>')
hero = f'''
<section class="hero" id="s02">{tag('s02')}<div class="wrap hero-grid">
  <div class="hero-copy">
    <p class="proof">{stars()}<span>{T(s02['rating_line'])}</span></p>
    <h1 class="h1">{T(s02['headline'])}</h1>
    <ul class="checks">{''.join(f'<li>{CHECK}<span>{T(x)}</span></li>' for x in s02['bullets'])}</ul>
    <p class="stockup">{T(s02['subhead'])}</p>
    <div class="cta-wrap"><span class="badge">{T(s03['items'][0])}</span>{btn(s02['cta'], 'pill pill-xl')}</div>
    <p class="riskfree">{CHECK}<span>{T(s02['trust'][1])}</span></p>
  </div>
  <div class="hero-media"><div class="hero-card"><img src="{IMG['kit']}" alt="{A(s02['image']['alt'])}"></div>{sticker}
    <img class="float f-cin" src="{IMG['i_cin']}" alt=""></div>
</div></section>'''

# ---------------- statement band + who it's for ----------------
band = f'''
<section class="band" id="s04">{tag('s04')}{wave('w-top')}
  <img class="float f-sticks" src="{IMG['sticks']}" alt="">
  <div class="wrap band-inner"><p class="eyebrow light">{T(s02['eyebrow'])}</p>
  <h2 class="h2 band-title">{T(s04['heading'])}</h2></div>
  <img class="float f-pour" src="{IMG['pour']}" alt="">
  {wave('w-bot')}
</section>
<section class="benefits"><div class="wrap grid4">
  <div class="col">{''.join(f'<div class="tile"><div class="ic">{ICON[k]}</div><p>{T(x)}</p></div>' for k, x in zip(('mug', 'jug'), s04['for'][:2]))}</div>
  <div class="ben-center"><img src="{IMG['cin']}" alt="{A(s05['image']['alt'])}"></div>
  <div class="col"><div class="tile"><div class="ic">{ICON['loop']}</div><p>{T(s04['for'][2])}</p></div>
  <div class="tile not"><div class="ic">{ICON['nocup']}</div><p><small>NOT FOR YOU IF</small>{T(s04['not_for'][0])}</p></div></div>
</div></section>
<div class="ticker" aria-hidden="true"><div>{''.join(f'<span>{A(f["name"].upper())}</span><i>{A(f["note"].upper())}</i>' for f in s11['items'] * 6)}</div></div>'''

# ---------------- buy box ----------------
gallery = [('kit', s02['image']['alt']), ('cin', 'The Good Stuff Cinnamon pouch'), ('can', 'The ceramic canister'),
           ('stickspack', 'The Good Stuff travel sticks'), ('stir', 'Stirring The Good Stuff into a mug of coffee'), ('pour', 'A scoop of The Good Stuff going into coffee')]
thumbs = ''.join(f'<button class="thumb{" on" if i == 0 else ""}" data-src="{k}" aria-label="{A(a)}"><img src="{IMG[k]}" alt=""></button>' for i, (k, a) in enumerate(gallery))
GIFT_IMG = {'Canister': f'<img src="{IMG["can"]}" alt="">', 'Frother': ICON['frother'], 'Scoop': ICON['scoop'], '3 Travel Sticks': f'<img src="{IMG["sticks"]}" alt="">'}
gifts = ''.join(f'<div class="gift"><span class="val">{T(g["value"])}</span><div class="gbox">{GIFT_IMG.get(g["name"], ICON["box"])}</div><b>{T(g["name"])}</b></div>' for g in s05['gifts'])
n90 = [x for x in split_note(o90['note']) if 'Welcome Kit' not in x]
n30 = split_note(o30['note'])
flav = ''.join(f'<button class="flav{" on" if i == 0 else ""}" data-src="{FLAV[f["name"]][0]}" data-name="{A(f["name"])}" style="--fc:{FLAV[f["name"]][1]}">'
               f'<img src="{IMG[FLAV[f["name"]][0]]}" alt=""><b>{T(f["name"])}</b><small>{T(f["note"])}</small></button>' for i, f in enumerate(s05['flavors']))
ING = {'Collagen': 'i_col', 'MCT': 'i_mct', 'L-Theanine': 'i_the', 'Cinnamon': 'i_cin'}
trust = [(ICON['truck'], s03['items'][1]), (ICON['pause'], s03['items'][2]), (ICON['box'], s03['items'][3])]
buy = f'''
<section class="buy" id="s05">{tag('s05')}<div class="wrap buy-grid">
  <div class="buy-media"><div class="thumbs">{thumbs}</div>
    <div class="stage"><img id="stage" src="{IMG['kit']}" alt="{A(s02['image']['alt'])}"></div></div>
  <div class="buy-info">
    <p class="proof sm">{stars()}<span>{T(s05['rating_line'])}</span></p>
    <h2 class="ptitle">{T(s05['product_name'])}</h2>
    <ul class="checks sm">{''.join(f'<li>{CHECK}<span>{T(x)}</span></li>' for x in (s05['includes'][0], s05['includes'][2]))}</ul>
    <div class="field"><p class="flabel">Flavor: <span id="flavname">{T(s05['flavors'][0]['name'])}</span></p><div class="flavs">{flav}</div></div>
    <p class="flabel">{T(s05['heading'])}</p>
    <label class="plan on"><input type="radio" name="plan" checked><div class="plan-banner">{T(kit_banner.upper())}</div>
      <div class="plan-head"><span class="radio"></span><div class="pl"><b>{T(o90['label'])}</b></div>
        <div class="pp"><b>{T(o90['price'])}</b> <s>{T(o90['anchor'])}</s></div></div>
      <ul class="checks xs">{''.join(f'<li>{CHECK}<span>{T(x)}</span></li>' for x in n90)}</ul>
      <div class="giftbox"><div class="gb-head"><b>Welcome Kit</b><span>{T(s03['items'][0])}</span></div><div class="gifts">{gifts}</div></div>
    </label>
    <label class="plan"><input type="radio" name="plan"><div class="plan-head"><span class="radio"></span><div class="pl"><b>{T(o30['label'])}</b></div>
        <div class="pp"><b>{T(o30['price'])}</b> <s>{T(o30['anchor'])}</s></div></div>
      <ul class="checks xs">{''.join(f'<li>{CHECK}<span>{T(x)}</span></li>' for x in n30)}</ul></label>
    {btn(s05['cta'], 'pill pill-xl pill-block')}
    <div class="trust3">{''.join(f'<div><span>{ic}</span><p>{T(t)}</p></div>' for ic, t in trust)}</div>
    <p class="fine">{T(s05['fine_print'])}</p>
    <details class="acc" open><summary>{T(s05['ingredients_heading'])}</summary>
      <ul class="ings">{''.join(f'<li><img src="{IMG[ING[n]]}" alt=""><span>{T(n)}</span></li>' for n in s05['ingredients'])}</ul></details>
  </div>
</div></section>'''

# ---------------- flavour feature card ----------------
fl_words = ' '.join(f'<span style="color:{FLAV[f["name"]][1]}">{T(f["name"])}.</span>' for f in s11['items'])
flavor = f'''
<section class="flavor" id="s11">{tag('s11')}<div class="wrap"><div class="fcard"><div class="fcard-in">
  <div class="fc-copy"><p class="eyebrow">{T(s11['eyebrow'])}</p><h2 class="h2 fc-title">{fl_words}</h2><p>{T(s11['body'])}</p></div>
  <div class="fc-packs">{''.join(f'<figure style="--fc:{FLAV[f["name"]][1]}"><img src="{IMG[FLAV[f["name"]][0]]}" alt="The Good Stuff {A(f["name"])} pouch"><figcaption><b>{T(f["name"])}</b>{T(f["note"])}</figcaption></figure>' for f in s11['items'])}</div>
</div></div></div></section>'''

# ---------------- how it works ----------------
packs3 = f'<div class="packs3"><img src="{IMG["van"]}" alt=""><img src="{IMG["cin"]}" alt=""><img src="{IMG["moc"]}" alt=""></div>'
step_media = [packs3, f'<img src="{IMG["kit"]}" alt="">', f'<img src="{IMG["stir"]}" alt="">', f'<img src="{IMG["dave"]}" alt="">']
how = f'''
<section class="how" id="s12">{tag('s12')}<div class="wrap">
  <h2 class="h2 center">{T(s12['heading'])}</h2>
  <div class="steps">{''.join(f'<div class="step"><div class="sm">{m}<span class="num">{i + 1}</span></div><h3>{T(st["title"])}</h3><p>{T(st["body"])}</p></div>' for i, (st, m) in enumerate(zip(s12['steps'], step_media)))}</div>
  <div class="center">{btn(s12['cta'], 'pill pill-lg')}</div>
</div></section>'''

# ---------------- what's in one scoop ----------------
scoop = f'''
<section class="scoop" id="s13">{tag('s13')}{wave('w-top')}<div class="wrap scoop-grid">
  <div><h2 class="h2">{T(s13['heading'])}</h2>
    <div class="nums">{''.join(f'<div><b>{T(x["number"])}</b><span>{T(x["label"])}</span></div>' for x in s13['items'])}</div>
    {btn(s13['cta'], 'pill pill-lg')}</div>
  <div class="scoop-img"><img src="{IMG['sip']}" alt="A woman drinking a mug of coffee"></div>
</div></section>'''

# ---------------- study card ----------------
pct = re.search(r'(\d+)%', s14['heading'])
pv = int(pct.group(1)) if pct else 0
study = f'''
<section class="study" id="s14">{tag('s14')}<div class="wrap"><div class="scard">
  <div class="ring" aria-hidden="true"><svg viewBox="0 0 120 120"><circle cx="60" cy="60" r="52" fill="none" stroke="rgba(255,255,255,.12)" stroke-width="10"/>
    <circle cx="60" cy="60" r="52" fill="none" stroke="#E0842A" stroke-width="10" stroke-linecap="round" stroke-dasharray="{326.7 * pv / 100:.1f} 400" transform="rotate(-90 60 60)"/></svg><b>{pv}%</b></div>
  <div class="sc-copy"><p class="eyebrow light">{T(s14['eyebrow'])}</p><h2 class="h2">{T(s14['heading'])}</h2><p>{T(s14['body'])}</p>
    <ul class="checks">{''.join(f'<li>{CHECK}<span>{T(x)}</span></li>' for x in s14['lines'])}</ul></div>
  <p class="sc-fine">{T(s14['fine_print'])}</p>
</div></div></section>'''

# ---------------- reviews + creator videos ----------------
tabs = ''.join(f'<button class="tab{" on" if i == 0 else ""}" data-tab="{i}">{T(t["label"])}</button>' for i, t in enumerate(s08['tabs']))
panes = ''.join(f'<div class="pane{" on" if i == 0 else ""}" data-pane="{i}">' + ''.join(
    f'<figure class="rev">{("<h3>" + T(s08["items"][j]["title"]) + "</h3>") if s08["items"][j].get("title") else ""}<blockquote>{T(s08["items"][j]["quote"])}</blockquote><figcaption>{T(s08["items"][j]["name"])}</figcaption></figure>'
    for j in t['items']) + '</div>' for i, t in enumerate(s08['tabs']))
videos = ''.join(f'<div class="vid"><span class="vtag">{T(t)}</span><span class="vplay">{ICON["play"]}</span><span class="vph">{T(s15["placeholder"])}</span></div>' for t in s15['tags'])
reviews = f'''
<section class="reviews" id="s08">{tag('s08')}{wave('w-top')}<div class="wrap">
  <p class="proof center">{stars()}<span>{T(s08['rating_line'])}</span></p>
  <h2 class="h2 center">{T(s08['heading'])}</h2>
  <div class="tabs" role="tablist">{tabs}</div>{panes}
  <div class="vids" id="s15">{tag('s15')}{videos}</div>
</div></section>'''

faq = f'''
<section class="faq" id="s09">{tag('s09')}{wave('w-top')}<div class="wrap faq-grid"><h2 class="h2">{T(s09['heading'])}</h2>
  <div>{''.join(f'<details><summary>{T(q["q"])}</summary><p>{T(q["a"])}</p></details>' for q in s09['items'])}</div></div></section>'''

final = f'''
<section class="final" id="s10">{tag('s10')}{wave('w-top')}<div class="wrap final-grid">
  <div class="final-copy"><h2 class="h1">{T(s10['heading'])}</h2><p>{T(s10['body'])}</p>{btn(s10['cta'], 'pill pill-xl pill-cin')}</div>
  <div class="final-img"><img src="{IMG['pour']}" alt="A scoop of The Good Stuff going into coffee"><img class="float f-petri" src="{IMG['i_cin']}" alt=""></div>
</div></section>'''

CSS = '''
@font-face{font-family:"Messina Sans";src:url(FONT_BOOK) format("woff2");font-weight:400;font-display:swap}
@font-face{font-family:"Messina Sans";src:url(FONT_BOLD) format("woff2");font-weight:700;font-display:swap}
:root{--cream:#F5F0E8;--paper:#FBF8F3;--ink:#161412;--esp:#2B201A;--tan:#DCC9AE;--tan2:#ECE0CD;--cin:#E0842A;--cin-d:#C9681C;
--soft:#6A6158;--line:#E2D6C4;--green:#3E7B50;--f:"Messina Sans",Helvetica,Arial,sans-serif;color-scheme:light;
--star:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3E%3Cpath d='M10 1.5l2.6 5.6 6.1.7-4.5 4.2 1.2 6L10 15l-5.4 3 1.2-6L1.3 7.8l6.1-.7z'/%3E%3C/svg%3E")}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;background:var(--cream);color:var(--ink);font-family:var(--f);font-size:16px;line-height:1.55;-webkit-font-smoothing:antialiased}
img{max-width:100%}button{font:inherit;color:inherit}
.page{overflow:hidden}.wrap{max-width:1200px;margin:0 auto;padding:0 18px}
section{position:relative}
.h1,.h2{font-weight:700;letter-spacing:-.03em;line-height:1.02;margin:0;text-wrap:balance}
.h1{font-size:44px}.h2{font-size:34px}.center{text-align:center}
.eyebrow{margin:0 0 12px;font-size:12px;font-weight:700;letter-spacing:.24em;text-transform:uppercase;color:var(--soft)}.eyebrow.light{color:#E9C9A4}
.ann{background:var(--ink);color:#fff;text-align:center;font-size:13px;font-weight:700;letter-spacing:.04em;padding:9px 14px}
.nav{display:flex;align-items:center;justify-content:space-between;padding-block:14px;gap:12px}
.nav .logo img{height:15px;display:block}
.pill{display:inline-block;background:var(--ink);color:#fff;text-decoration:none;border-radius:999px;font-weight:700;text-align:center;transition:transform .15s,box-shadow .15s}
.pill:hover{transform:translateY(-2px);box-shadow:0 8px 20px rgba(22,20,18,.22)}
.nav .pill{font-size:14px;padding:10px 20px}.pill-lg{font-size:17px;padding:15px 36px}.pill-xl{display:block;font-size:19px;padding:18px 24px}
.pill-block{width:100%}.pill-cin{background:var(--cin);color:var(--ink)}
.checks{list-style:none;margin:0 0 14px;padding:0;display:grid;gap:9px}
.checks li{display:flex;gap:10px;align-items:flex-start}.ck{flex:none;width:19px;height:19px;margin-top:2px;fill:var(--cin)}
.checks.sm li{font-size:15px}.checks.xs{gap:5px;margin:8px 14px 0 46px}.checks.xs li{font-size:14px}.checks.xs .ck{width:15px;height:15px;fill:var(--ink)}
.stars{display:inline-flex;gap:2px}.st{position:relative;width:17px;height:17px;background:#D8CBB8;-webkit-mask:var(--star) center/contain no-repeat;mask:var(--star) center/contain no-repeat}
.st span{position:absolute;inset:0 auto 0 0;background:var(--cin)}
.proof{display:flex;align-items:center;gap:10px;margin:0 0 16px;font-size:14px;font-weight:700}.proof.center{justify-content:center}.proof.sm{font-size:13px;margin-bottom:8px}
.wave{position:absolute;left:0;width:100%;height:46px;display:block;pointer-events:none;z-index:1}
.w-top{top:-45px}.w-bot{bottom:-45px;transform:scaleY(-1)}
.float{position:absolute;pointer-events:none;z-index:2;filter:drop-shadow(0 18px 24px rgba(0,0,0,.25))}
/* hero */
.hero{padding:14px 0 76px}
.hero-grid{display:flex;flex-direction:column-reverse;gap:30px}
.hero-media{position:relative}
.hero-card{border-radius:26px;overflow:hidden;background:#D9C6B5;box-shadow:0 30px 60px -30px rgba(61,44,34,.45)}
.hero-card img{display:block;width:100%}
.sticker{position:absolute;left:-6px;top:-16px;width:112px;height:112px;display:grid;place-items:center;z-index:3}
.sticker svg{position:absolute;inset:0;width:100%;height:100%;animation:spin 30s linear infinite}
.sticker .ring{font:700 14px var(--f);letter-spacing:.12em;fill:#F5F0E8}
.sticker b{position:relative;color:var(--cin);font-size:24px;letter-spacing:.06em;transform:rotate(-10deg)}
@keyframes spin{to{transform:rotate(360deg)}}
.f-cin{width:96px;right:-8px;bottom:-34px;border-radius:50%;clip-path:circle(41% at 50% 50%)}
.h1{margin-bottom:18px}.hero .checks li{font-size:16px}
.stockup{font-weight:700;font-size:17px;margin:6px 0 24px;max-width:520px}
.cta-wrap{position:relative;padding-top:13px;max-width:470px}
.badge{position:absolute;left:50%;top:0;transform:translateX(-50%);z-index:1;background:var(--cin);color:var(--ink);font-size:11.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;
 border-radius:999px;padding:5px 14px;white-space:nowrap;border:2px solid var(--cream)}
.riskfree{display:flex;gap:8px;align-items:center;justify-content:center;max-width:470px;margin:14px 0 0;font-size:14px;font-weight:700}.riskfree .ck{fill:var(--green)}
/* band */
.band{background:radial-gradient(70% 120% at 50% 0%,#4A3427 0%,var(--esp) 55%,#1E1612 100%);color:var(--cream);padding:70px 0 130px;text-align:center}
.band .w-top{color:#3E2D23}.band .w-bot{color:#1F1713}
.band-inner{position:relative;z-index:3}.band-title{font-size:40px;color:#FBF3E6;max-width:820px;margin:0 auto}
.f-sticks{display:none;width:110px;left:-22px;top:20px;transform:rotate(-14deg)}
.f-pour{width:250px;right:-24px;bottom:-60px;transform:rotate(4deg)}
/* benefits */
.benefits{padding:80px 0 60px;background:var(--cream)}
.grid4{display:grid;grid-template-columns:1fr 1fr;gap:28px 16px;text-align:center}.grid4 .col{display:contents}
.ben-center{grid-column:1/-1;order:-1;display:grid;place-items:center}.ben-center img{width:56%;filter:drop-shadow(0 26px 28px rgba(22,20,18,.28))}
.tile .ic{width:60px;height:60px;border-radius:50%;background:var(--tan2);color:var(--cin-d);display:grid;place-items:center;margin:0 auto 12px}
.tile .ic svg{width:32px;height:32px}.tile p{margin:0;font-weight:700;font-size:16px;line-height:1.3}
.tile.not .ic{background:#E9E4DC;color:var(--soft)}.tile.not p{color:var(--soft)}.tile small{display:block;font-size:10.5px;letter-spacing:.2em;margin-bottom:4px}
.ticker{background:var(--ink);color:var(--cream);overflow:hidden;white-space:nowrap;padding:15px 0}
.ticker div{display:inline-block;animation:tick 50s linear infinite}
.ticker span{font-weight:700;letter-spacing:.26em;font-size:13px;margin:0 12px}.ticker i{font-style:normal;color:var(--cin);letter-spacing:.26em;font-size:13px;margin-right:40px}
@keyframes tick{to{transform:translateX(-50%)}}
/* buy */
.buy{background:var(--paper);padding:34px 0 50px}
.buy-media{display:flex;flex-direction:column-reverse;gap:10px}
.thumbs{display:flex;gap:8px;overflow-x:auto}
.thumb{flex:none;width:62px;height:62px;border-radius:12px;border:2px solid transparent;background:var(--tan2);padding:0;overflow:hidden;cursor:pointer}
.thumb img{width:100%;height:100%;object-fit:cover}.thumb.on{border-color:var(--ink)}
.stage{border-radius:22px;overflow:hidden;background:#D9C6B5;aspect-ratio:1/1;display:grid;place-items:center}
.stage img{width:100%;height:100%;object-fit:contain}.stage img.photo{object-fit:cover}.stage img.cut{width:68%;height:68%;object-fit:contain;filter:drop-shadow(0 24px 26px rgba(22,20,18,.28))}
.ptitle{font-weight:700;font-size:32px;letter-spacing:-.03em;line-height:1.02;margin:6px 0 14px}
.field{border-top:1px solid var(--line);margin-top:16px;padding-top:14px}
.flabel{font-weight:700;font-size:15px;margin:18px 0 9px}.field .flabel{margin-top:0}.flabel span{font-weight:400}
.flavs{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.flav{border:1.5px solid var(--line);border-radius:14px;background:#fff;padding:8px 6px 10px;cursor:pointer;display:grid;justify-items:center;gap:2px;transition:border-color .15s,box-shadow .15s}
.flav img{width:58px;height:66px;object-fit:contain}.flav b{font-size:14px}.flav small{font-size:12px;font-weight:700;color:var(--fc)}
.flav.on{border:2px solid var(--fc);box-shadow:0 0 0 3px color-mix(in srgb,var(--fc) 18%,transparent)}
.plan{display:block;border:1.5px solid var(--line);border-radius:16px;background:#fff;margin:0 0 12px;overflow:hidden;padding-bottom:14px;cursor:pointer;transition:border-color .15s;position:relative}
.plan input{position:absolute;opacity:0;pointer-events:none}
.plan.on{border:2px solid var(--ink);background:#FFFCF7}
.plan-banner{background:var(--ink);color:var(--cream);text-align:center;font-size:11.5px;font-weight:700;letter-spacing:.18em;padding:8px}
.plan-head{display:flex;align-items:center;gap:12px;padding:14px 16px 0}
.radio{width:20px;height:20px;border-radius:50%;border:2px solid #B9AE9F;flex:none}.plan.on .radio{border-color:var(--ink);box-shadow:inset 0 0 0 4px #fff;background:var(--ink)}
.pl{flex:1;font-size:17px}.pp{text-align:right;font-size:21px;white-space:nowrap}.pp s{font-size:14px;color:var(--soft)}
.giftbox{margin:14px 14px 0;border-radius:12px;overflow:hidden;background:var(--tan2)}
.gb-head{display:flex;justify-content:space-between;align-items:center;gap:8px;padding:10px 12px 14px;font-size:13px}.gb-head span{background:var(--cin);border-radius:999px;padding:2px 10px;font-weight:700;font-size:11px}
.gifts{display:grid;grid-template-columns:repeat(4,1fr);gap:7px;padding:0 10px 12px}
.gift{text-align:center;font-size:11.5px;line-height:1.2;position:relative}
.gift .val{position:absolute;top:-8px;left:50%;transform:translateX(-50%);background:var(--green);color:#fff;font-weight:700;font-size:10px;border-radius:999px;padding:1px 8px;z-index:1}
.gbox{height:64px;border-radius:10px;background:#fff;display:grid;place-items:center;color:var(--ink);margin-bottom:5px}.gbox svg{width:30px;height:30px}.gbox img{height:52px;width:auto}
.trust3{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:18px 0 4px;text-align:center}
.trust3 span{display:grid;place-items:center;width:44px;height:44px;margin:0 auto 6px;border-radius:50%;background:var(--tan2);color:var(--cin-d)}.trust3 svg{width:24px;height:24px}
.trust3 p{margin:0;font-size:12.5px;font-weight:700;line-height:1.25}
.fine{font-size:12px;color:var(--soft);text-align:center;margin:12px 0 4px}
.acc{border-top:1px solid var(--line);border-bottom:1px solid var(--line);margin-top:16px;padding:14px 0}
.acc summary,.faq summary{list-style:none;font-weight:700;font-size:16px;display:flex;justify-content:space-between;gap:12px;cursor:pointer}
.acc summary::-webkit-details-marker,.faq summary::-webkit-details-marker{display:none}
.acc summary::after,.faq summary::after{content:"+";font-size:22px;line-height:1;font-weight:400}.acc[open] summary::after,.faq details[open] summary::after{content:"\\2212"}
.ings{list-style:none;padding:0;margin:12px 0 0;display:grid;grid-template-columns:1fr 1fr;gap:10px}
.ings li{display:flex;align-items:center;gap:10px;font-size:14px;font-weight:700}.ings img{width:46px;height:46px;border-radius:50%;object-fit:cover}
/* flavour card */
.flavor{padding:50px 0 30px;background:var(--paper)}
.fcard{border-radius:28px;background:var(--esp);padding:10px}
.fcard-in{border-radius:20px;background:radial-gradient(90% 130% at 75% 50%,#F6ECDD 0%,#EADBC5 60%,#DFCBAE 100%);padding:30px 22px;display:grid;gap:26px;align-items:center;overflow:hidden}
.fc-title{font-size:38px}.fc-copy p{margin:14px 0 0;font-size:17px;max-width:420px}
.fc-packs{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;align-items:end}
.fc-packs figure{margin:0;text-align:center}.fc-packs img{width:100%;filter:drop-shadow(0 18px 18px rgba(22,20,18,.25))}
.fc-packs figure:nth-child(2) img{transform:translateY(-14px) scale(1.08)}
.fc-packs figcaption{font-size:13px;margin-top:8px;color:var(--soft)}.fc-packs figcaption b{display:block;color:var(--fc);font-size:16px}
/* how */
.how{padding:60px 0 80px;background:var(--paper)}
.how .h2{margin-bottom:36px}
.steps{display:grid;gap:34px;margin-bottom:36px}
.step{text-align:center}.step .sm{position:relative;border-radius:20px;aspect-ratio:4/3;background:var(--tan2);margin-bottom:32px}
.step .sm>img{width:100%;height:100%;object-fit:cover;border-radius:20px;display:block}
.packs3{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;border-radius:20px;background:radial-gradient(90% 90% at 50% 40%,#F1E6D5,#DCC9AE)}
.packs3 img{width:34%;margin:0 -5%;filter:drop-shadow(0 12px 14px rgba(0,0,0,.25))}.packs3 img:nth-child(2){width:40%;z-index:1;transform:translateY(-6px)}
.num{position:absolute;left:50%;bottom:-21px;transform:translateX(-50%);width:42px;height:42px;border-radius:50%;background:var(--ink);color:var(--cream);display:grid;place-items:center;font-weight:700;font-size:18px;border:3px solid var(--paper)}
.step h3{font-size:19px;letter-spacing:-.02em;margin:0 0 6px;line-height:1.2}.step p{margin:0 auto;font-size:15px;color:var(--soft);max-width:300px}
/* scoop */
.scoop{background:var(--tan2);padding:50px 0 60px}.scoop .wave{color:var(--tan2)}
.scoop-grid{display:grid;gap:30px;align-items:center}
.nums{display:grid;grid-template-columns:1fr 1fr;gap:24px 18px;margin:28px 0 32px}
.nums div{border-top:2px solid var(--ink);padding-top:12px}
.nums b{display:block;font-size:36px;letter-spacing:-.04em;line-height:1;margin-bottom:6px}.nums span{font-size:14px;color:var(--soft);font-weight:700}
.scoop-img img{display:block;width:100%;border-radius:26px;box-shadow:0 30px 60px -30px rgba(61,44,34,.55)}
/* study */
.study{padding:10px 0 70px;background:var(--tan2)}
.scard{border-radius:28px;background:radial-gradient(80% 120% at 20% 20%,#4A3427 0%,var(--esp) 60%,#1E1612 100%);color:var(--cream);padding:34px 24px;display:grid;gap:22px}
.ring{position:relative;width:170px;height:170px;margin:0 auto}.ring svg{width:100%;height:100%}
.ring b{position:absolute;inset:0;display:grid;place-items:center;font-size:44px;letter-spacing:-.04em;color:#FBF3E6}
.scard .h2{font-size:32px;color:#FBF3E6}.sc-copy p{margin:14px 0 18px;color:#E7DCCB}.scard .checks li{font-weight:700}
.sc-fine{grid-column:1/-1;margin:0;font-size:11.5px;line-height:1.5;color:#B9AA95;border-top:1px solid rgba(255,255,255,.12);padding-top:16px}
/* reviews */
.reviews{background:linear-gradient(180deg,var(--cream) 0%,#EEDFC9 100%);padding:44px 0 60px}.reviews .wave{color:var(--cream)}
.reviews .h2{margin-bottom:24px}
.tabs{display:flex;justify-content:center;gap:8px;margin-bottom:28px}
.tab{border:1.5px solid var(--ink);border-radius:999px;background:transparent;padding:9px 24px;font-weight:700;font-size:14px;cursor:pointer}.tab.on{background:var(--ink);color:var(--cream)}
.pane{display:none}.pane.on{display:grid;gap:28px}
.rev{margin:0;text-align:center}.rev h3{font-size:18px;letter-spacing:-.02em;margin:0 0 8px;line-height:1.25}
.rev blockquote{margin:0 0 10px;font-size:15.5px;line-height:1.6}.rev figcaption{font-weight:700;font-size:14px}
.vids{display:flex;gap:12px;overflow-x:auto;margin-top:44px;padding-bottom:6px;scroll-snap-type:x mandatory}
.vid{flex:none;width:58%;aspect-ratio:9/16;border-radius:20px;position:relative;scroll-snap-align:start;overflow:hidden;
 background:linear-gradient(160deg,#4A3427 0%,var(--esp) 55%,#161412 100%);border:2px dashed rgba(224,132,42,.6)}
.vtag{position:absolute;top:14px;left:50%;transform:translateX(-50%);background:var(--cin);color:var(--ink);font-weight:700;font-size:11.5px;letter-spacing:.16em;text-transform:uppercase;border-radius:6px;padding:4px 10px;white-space:nowrap}
.vplay{position:absolute;inset:0;display:grid;place-items:center}.vplay svg{width:54px;height:54px}
.vph{position:absolute;bottom:16px;left:0;right:0;text-align:center;font-size:12px}
/* faq + final */
.faq{background:var(--paper);padding:54px 0 90px}.faq .wave{color:var(--paper)}.faq .h2{margin-bottom:12px}
.faq details{border-bottom:1.5px solid var(--ink);padding:16px 0}.faq details p{margin:10px 0 0;color:var(--soft)}
.final{background:radial-gradient(70% 120% at 70% 30%,#4A3427 0%,var(--esp) 55%,#1E1612 100%);color:var(--cream);padding:40px 0 0}
.final .wave{color:#3B2B21}
.final-grid{display:grid;gap:10px;align-items:end}
.final .h1{color:#FBF3E6;margin-bottom:14px}.final p{color:#E7DCCB;max-width:440px;margin:0 0 26px}
.final .pill-xl{display:inline-block;padding:18px 44px}
.final-img{position:relative}.final-img>img:first-child{display:block;width:100%;margin-top:10px}
.f-petri{width:96px;right:-8px;bottom:-20px;border-radius:50%;clip-path:circle(41% at 50% 50%)}
.foot{background:#100E0C;color:#8E8577;padding:30px 0 36px;font-size:11.5px;line-height:1.6}
.foot img{height:14px;display:block;margin-bottom:16px}.foot p{margin:0;max-width:900px}
mark.ph{background:#FFE86B;color:#1a1a1a;padding:0 4px;border-radius:4px}
.vph mark.ph{font-weight:700}
.sid{position:absolute;top:6px;right:8px;z-index:9;font:700 11px/1 ui-monospace,Menlo,monospace;background:#1a1a1a;color:#fff;padding:4px 7px;border-radius:6px;opacity:.85}
@media (prefers-reduced-motion:reduce){.sticker svg,.ticker div{animation:none}}
@media (min-width:700px){.vid{width:31%}.steps{grid-template-columns:1fr 1fr}.pane.on{grid-template-columns:repeat(3,1fr);gap:36px}}
@media (min-width:960px){
 body{font-size:17px}.wrap{padding:0 40px}
 .ann{font-size:14px}.nav .logo img{height:17px}.nav .pill{font-size:15px;padding:12px 26px}
 .h1{font-size:72px}.h2{font-size:52px}
 .hero{padding:30px 0 130px}
 .hero-grid{display:grid;grid-template-columns:1fr 1.08fr;gap:64px;align-items:center}
 .sticker{width:156px;height:156px;left:-34px;top:-34px}.sticker .ring{font-size:14px}.sticker b{font-size:34px}
 .f-cin{width:150px;right:-44px;bottom:-64px}
 .hero .checks li{font-size:17px}.stockup{font-size:19px}.pill-xl{font-size:20px;padding:20px 26px}
 .band{padding:120px 0 170px}.band-title{font-size:68px}
 .wave{height:70px}.w-top{top:-69px}.w-bot{bottom:-69px}
 .f-sticks{display:block;width:220px;left:3%;top:70px}.f-pour{width:440px;right:1%;bottom:-110px}
 .benefits{padding:140px 0 110px}
 .grid4{grid-template-columns:1fr 290px 1fr;gap:56px;align-items:center}
 .grid4 .col{display:grid;gap:70px}.ben-center{grid-column:auto;order:0}.ben-center img{width:100%}
 .tile p{font-size:19px}.tile .ic{width:74px;height:74px}.tile .ic svg{width:38px;height:38px}
 .buy{padding:80px 0 90px}
 .buy-grid{display:grid;grid-template-columns:1.12fr 1fr;gap:60px;align-items:start}
 .buy-media{position:sticky;top:24px;flex-direction:row;gap:14px}.thumbs{flex-direction:column;overflow:visible}.thumb{width:76px;height:76px}
 .stage{flex:1}.ptitle{font-size:46px}
 .flavor{padding:60px 0 40px}.fcard{padding:14px}.fcard-in{grid-template-columns:1fr 1.15fr;padding:56px 64px}.fc-title{font-size:60px}
 .how{padding:90px 0 120px}.steps{grid-template-columns:repeat(4,1fr);gap:26px}
 .scoop{padding:90px 0 110px}.scoop-grid{grid-template-columns:1fr 1fr;gap:70px}.nums b{font-size:54px}
 .study{padding:0 0 130px}.scard{grid-template-columns:260px 1fr;gap:24px 64px;padding:60px 68px;align-items:center}
 .ring{width:250px;height:250px}.ring b{font-size:66px}.scard .h2{font-size:46px}
 .reviews{padding:80px 0 110px}.vid{width:auto;flex:1}.vids{overflow:visible}
 .faq{padding:100px 0 140px}.faq-grid{display:grid;grid-template-columns:.8fr 1.2fr;gap:60px;align-items:start}.faq .h2{font-size:64px}
 .final{padding:80px 0 0}.final-grid{grid-template-columns:1fr 1.05fr;gap:40px}.final-copy{padding-bottom:120px}.final .h1{font-size:76px}
 .final p{font-size:19px}.f-petri{width:160px;right:auto;left:-80px;bottom:40px}
}
'''.replace('FONT_BOOK', FONT_BOOK).replace('FONT_BOLD', FONT_BOLD)

JS = '''
(function(){
 var IMG={}, stage=document.getElementById('stage'), CUT={cin:1,moc:1,van:1,can:1,stickspack:1};
 document.querySelectorAll('[data-src]').forEach(function(el){var i=el.querySelector('img');if(i)IMG[el.dataset.src]=i.src});
 function show(k,alt){stage.src=IMG[k];stage.className=CUT[k]?'cut':(k==='stir'?'photo':'');if(alt)stage.alt=alt;
  document.querySelectorAll('.thumb').forEach(function(t){t.classList.toggle('on',t.dataset.src===k)});}
 document.querySelectorAll('.thumb').forEach(function(t){t.addEventListener('click',function(){show(t.dataset.src,t.getAttribute('aria-label'))})});
 document.querySelectorAll('.flav').forEach(function(f){f.addEventListener('click',function(){
  document.querySelectorAll('.flav').forEach(function(x){x.classList.toggle('on',x===f)});
  document.getElementById('flavname').textContent=f.dataset.name;show(f.dataset.src,'The Good Stuff '+f.dataset.name+' pouch');})});
 document.querySelectorAll('.plan input').forEach(function(r){r.addEventListener('change',function(){
  document.querySelectorAll('.plan').forEach(function(p){p.classList.toggle('on',p.querySelector('input').checked)})})});
 document.querySelectorAll('.tab').forEach(function(t){t.addEventListener('click',function(){
  document.querySelectorAll('.tab').forEach(function(x){x.classList.toggle('on',x===t)});
  document.querySelectorAll('.pane').forEach(function(p){p.classList.toggle('on',p.dataset.pane===t.dataset.tab)})})});
})();'''

title = (P.get('meta') or {}).get('title') or 'For Wellness'
doc = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{A(title)}</title>
<style>{CSS}</style></head>
<body><div class="page">
<div class="ann" id="s01">{tag('s01')}{T(s01['text'])}</div>
<nav class="nav wrap"><span class="logo"><img src="{LOGO}" alt="For Wellness"></span>{btn(s02['cta'])}</nav>
{hero}{band}{buy}{flavor}{how}{scoop}{study}{reviews}{faq}{final}
<footer class="foot"><div class="wrap"><img src="{LOGO_W}" alt="For Wellness"><p>{T(s14['fine_print'])}</p></div></footer>
</div><script>{JS}</script></body></html>'''

out = os.path.join(RUN, 'for-wellness-welcome-kit' + ('-labelled' if LABELS else '') + '.html')
open(out, 'w').write(doc)
print(f'wrote {out} ({len(doc) // 1024} KB)')

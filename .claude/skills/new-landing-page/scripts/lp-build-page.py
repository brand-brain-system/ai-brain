#!/usr/bin/env python3
"""Build a landing page from a run's approved copy.

Usage: python3 lp-build-page.py <run_dir> [--labels] [--artifact] [--out <file>]

--artifact writes the page in the shape the Artifact tool publishes (no doctype, head or body tags; it adds
them), for sending the reviewer a link to the page itself.

Reads <run>/page.json (the approved copy, one entry per section, in template order) and
<run>/brief.json (brand tokens: palette, fonts, logo, cta_url) and writes <run>/page.html
(or --out; --labels writes <run>/page-labelled.html). --labels adds a small section tag (S01, S02 ...) to every section so reviewers can
leave feedback by section on the draft board; the final build has no labels.

Never fill the page by hand: change page.json (copy) or brief.json (tokens) and rebuild.
Every button on the page goes to one link, brief.json cta_url (page.json meta.cta_url overrides),
because a single discounted link beat per-section links in the swipe file (The Perfect Jean).

Section types (fields in page.json "fields"):
  offer_bar     text
  hero          eyebrow, headline, subhead, bullets[], cta, image, trust[]
  byline        name, title, updated
  disclosure    text
  press_bar     label, names[]
  trust_row     items[]
  text          heading, paragraphs[]
  founder_note  heading, paragraphs[], signoff, image
  numbered_reasons  heading, items[{title, body, cta, image}]
  benefits      heading, items[{title, body}], cta
  comparison_table  heading, columns[], rows[[...]], note, highlight_col
  reviews       heading, items[{quote, name, detail, stars}]
  timeline      heading, items[{when, what}]
  buy_box       heading, product_name, image, rating_line, options[{label, price, anchor, note, default}],
                includes[], gifts[{name, value}], cta, guarantee, fine_print
  value_stack   heading, items[{name, price, value}], total_line, cta
  faq           heading, items[{q, a}]
  quiz          intro, steps[{question, options[]}], skip_label, loading_lines[], result{headline, body, bullets[], cta}, reward
  game          headline, subhead, cards, prizes[], cta
  rounds        heading, items[{title, body, winner, cta}]
  verdict       heading, points[], cta
  guarantee     heading, body
  who_for       heading, for[], not_for[]
  cta_block     heading, body, cta
  sticky_cta    text, cta
  steps         heading, items[{title, body}]
  stat_strip    items[{number, label}]
  product_grid  heading, items[{name, price, anchor, tag, image}]
  image         image, caption
An image is {"src": "assets/<file>", "alt": "..."} (a real brand photo saved in <run>/assets/, placed as is;
a published board cannot show images from other sites, so photos are always local files) or
{"placeholder": "what the photo should show"} (drawn as a labelled box until a real photo exists).
"""
import sys, os, json, html, re

def arg(name, default=None):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default

E = lambda s: html.escape(str(s or ''), quote=True)
PH = re.compile(r'(\[(?:OFFER|STAT NEEDED|PHOTO|CODE|DATE|PRICE)[^\]]*\])')

def T(s):
    """Escape text and highlight placeholders so nothing unfinished can hide."""
    return PH.sub(r'<mark class="ph">\1</mark>', E(s))


class Page:
    def __init__(self, page, brief, labels, artifact=False):
        self.page, self.brief, self.labels, self.artifact = page, brief, labels, artifact
        meta = page.get('meta') or {}
        self.cta_url = meta.get('cta_url') or brief.get('cta_url') or brief.get('landing_url') or '#'

    def btn(self, label, cls='btn'):
        if not label:
            return ''
        return f'<a class="{cls}" href="{E(self.cta_url)}">{T(label)}</a>'

    def img(self, im, cls='img'):
        if not im:
            return ''
        if isinstance(im, str):
            im = {'src': im}
        if im.get('src'):
            return f'<img class="{cls}" src="{E(im["src"])}" alt="{E(im.get("alt", ""))}" loading="lazy">'
        if im.get('placeholder'):
            return f'<div class="{cls} ph-img"><span>PHOTO NEEDED</span><small>{E(im["placeholder"])}</small></div>'
        return ''

    def ul(self, items, cls='checks'):
        items = [i for i in (items or []) if i]
        if not items:
            return ''
        return f'<ul class="{cls}">' + ''.join(f'<li>{T(i)}</li>' for i in items) + '</ul>'

    def h2(self, s):
        return f'<h2>{T(s)}</h2>' if s else ''

    # ---- components ----
    def offer_bar(self, f):
        return f'<div class="offer-bar">{T(f.get("text"))}</div>'

    def hero(self, f):
        trust = ''.join(f'<span>{T(t)}</span>' for t in (f.get('trust') or []))
        return (f'<div class="hero">' + (f'<p class="eyebrow">{T(f.get("eyebrow"))}</p>' if f.get('eyebrow') else '') +
                f'<h1>{T(f.get("headline"))}</h1>' + (f'<p class="sub">{T(f.get("subhead"))}</p>' if f.get('subhead') else '') +
                self.img(f.get('image'), 'img hero-img') + self.ul(f.get('bullets')) + self.btn(f.get('cta')) +
                (f'<div class="trust-mini">{trust}</div>' if trust else '') + '</div>')

    def byline(self, f):
        return (f'<div class="byline"><div class="avatar">{E((f.get("name") or "?")[:1])}</div><div>'
                f'<b>{T(f.get("name"))}</b><span>{T(f.get("title"))}</span>' +
                (f'<span class="muted">Updated {T(f.get("updated"))}</span>' if f.get('updated') else '') + '</div></div>')

    def disclosure(self, f):
        return f'<p class="disclosure">{T(f.get("text"))}</p>'

    def press_bar(self, f):
        names = ''.join(f'<span>{T(n)}</span>' for n in (f.get('names') or []))
        return (f'<p class="label">{T(f.get("label") or "As seen in")}</p>' if names else '') + f'<div class="press">{names}</div>'

    def trust_row(self, f):
        return '<div class="trust-row">' + ''.join(f'<div>{T(i)}</div>' for i in (f.get('items') or [])) + '</div>'

    def text(self, f):
        return self.h2(f.get('heading')) + ''.join(f'<p>{T(p)}</p>' for p in (f.get('paragraphs') or []))

    def founder_note(self, f):
        return ('<div class="note">' + self.h2(f.get('heading')) + self.img(f.get('image')) +
                ''.join(f'<p>{T(p)}</p>' for p in (f.get('paragraphs') or [])) +
                (f'<p class="sign">{T(f.get("signoff"))}</p>' if f.get('signoff') else '') + '</div>')

    def numbered_reasons(self, f):
        out = self.h2(f.get('heading'))
        for i, it in enumerate(f.get('items') or [], 1):
            out += (f'<div class="reason"><div class="num">{i}</div><h3>{T(it.get("title"))}</h3>' + self.img(it.get('image')) +
                    f'<p>{T(it.get("body"))}</p>' + self.btn(it.get('cta'), 'btn btn-sm') + '</div>')
        return out

    def benefits(self, f):
        cards = ''.join(f'<div class="card"><h3>{T(it.get("title"))}</h3><p>{T(it.get("body"))}</p></div>' for it in (f.get('items') or []))
        return self.h2(f.get('heading')) + f'<div class="cards">{cards}</div>' + self.btn(f.get('cta'))

    def comparison_table(self, f):
        cols = f.get('columns') or []
        hi = f.get('highlight_col', 1)
        head = ''.join(f'<th class="{"hi" if j == hi else ""}">{T(c)}</th>' for j, c in enumerate(cols))
        body = ''
        for r in f.get('rows') or []:
            body += '<tr>' + ''.join(f'<td class="{"hi" if j == hi else ""}">{T(c)}</td>' for j, c in enumerate(r)) + '</tr>'
        return (self.h2(f.get('heading')) + f'<div class="table-wrap"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>' +
                (f'<p class="muted small">{T(f.get("note"))}</p>' if f.get('note') else ''))

    def reviews(self, f):
        out = ''
        for it in f.get('items') or []:
            stars = '★' * int(it.get('stars') or 0)
            out += (f'<figure class="review">' + (f'<div class="stars">{stars}</div>' if stars else '') +
                    f'<blockquote>{T(it.get("quote"))}</blockquote><figcaption>{T(it.get("name"))}' +
                    (f' <span class="muted">{T(it.get("detail"))}</span>' if it.get('detail') else '') + '</figcaption></figure>')
        return self.h2(f.get('heading')) + f'<div class="reviews">{out}</div>'

    def timeline(self, f):
        out = ''.join(f'<li><b>{T(it.get("when"))}</b><span>{T(it.get("what"))}</span></li>' for it in (f.get('items') or []))
        return self.h2(f.get('heading')) + f'<ol class="timeline">{out}</ol>'

    def buy_box(self, f):
        opts = ''
        for i, o in enumerate(f.get('options') or []):
            checked = 'checked' if o.get('default') or (i == 0 and not any(x.get('default') for x in f.get('options'))) else ''
            anchor = f'<s>{T(o.get("anchor"))}</s> ' if o.get('anchor') else ''
            opts += (f'<label class="opt"><input type="radio" name="opt-{id(f)}" {checked}><span class="opt-l">{T(o.get("label"))}'
                     + (f'<small>{T(o.get("note"))}</small>' if o.get('note') else '') + f'</span><span class="opt-p">{anchor}{T(o.get("price"))}</span></label>')
        gifts = ''.join(f'<li><span>{T(g.get("name"))}</span><b>{T(g.get("value"))}</b></li>' for g in (f.get('gifts') or []))
        return ('<div class="buybox">' + self.img(f.get('image'), 'img') + self.h2(f.get('heading')) +
                (f'<p class="pname">{T(f.get("product_name"))}</p>' if f.get('product_name') else '') +
                (f'<p class="rating">{T(f.get("rating_line"))}</p>' if f.get('rating_line') else '') +
                (f'<div class="opts">{opts}</div>' if opts else '') + self.ul(f.get('includes')) +
                (f'<p class="label">Free with your order</p><ul class="gifts">{gifts}</ul>' if gifts else '') +
                self.btn(f.get('cta'), 'btn btn-block') +
                (f'<p class="guar">{T(f.get("guarantee"))}</p>' if f.get('guarantee') else '') +
                (f'<p class="muted small">{T(f.get("fine_print"))}</p>' if f.get('fine_print') else '') + '</div>')

    def value_stack(self, f):
        rows = ''.join(f'<li><span>{T(it.get("name"))}</span><span><b>{T(it.get("price"))}</b> <s>{T(it.get("value"))}</s></span></li>' for it in (f.get('items') or []))
        return ('<div class="buybox">' + self.h2(f.get('heading')) + f'<ul class="stack">{rows}</ul>' +
                (f'<p class="total">{T(f.get("total_line"))}</p>' if f.get('total_line') else '') + self.btn(f.get('cta'), 'btn btn-block') + '</div>')

    def faq(self, f):
        return self.h2(f.get('heading') or 'Questions') + ''.join(
            f'<details><summary>{T(it.get("q"))}</summary><p>{T(it.get("a"))}</p></details>' for it in (f.get('items') or []))

    def quiz(self, f):
        steps = f.get('steps') or []
        n = len(steps)
        html_steps = ''
        for i, s in enumerate(steps):
            opts = ''.join(f'<button type="button" class="qopt">{T(o)}</button>' for o in (s.get('options') or []))
            html_steps += (f'<div class="qstep" data-i="{i}" {"hidden" if i else ""}><p class="muted small">{i + 1} of {n}</p>'
                           f'<h3>{T(s.get("question"))}</h3><div class="qopts">{opts}</div>'
                           f'<a class="skip" href="{E(self.cta_url)}">{T(f.get("skip_label") or "Skip and start now")}</a></div>')
        loading = ''.join(f'<li>{T(l)}</li>' for l in (f.get('loading_lines') or []))
        r = f.get('result') or {}
        return ('<div class="quiz">' + (f'<p class="sub">{T(f.get("intro"))}</p>' if f.get('intro') else '') + html_steps +
                f'<div class="qload" hidden><ul>{loading}</ul></div>'
                f'<div class="qresult" hidden><h3>{T(r.get("headline"))}</h3>' + (f'<p>{T(r.get("body"))}</p>' if r.get('body') else '') +
                self.ul(r.get('bullets')) + (f'<p class="reward">{T(f.get("reward"))}</p>' if f.get('reward') else '') +
                self.btn(r.get('cta'), 'btn btn-block') + '</div></div>')

    def game(self, f):
        n = int(f.get('cards') or 6)
        prizes = [T(p) for p in (f.get('prizes') or [])]
        cards = ''.join('<button type="button" class="gcard"><span class="back">?</span></button>' for _ in range(n))
        return ('<div class="game">' + f'<h1>{T(f.get("headline"))}</h1>' + (f'<p class="sub">{T(f.get("subhead"))}</p>' if f.get('subhead') else '') +
                f'<div class="gcards" data-prizes=\'{E(json.dumps(prizes))}\'>{cards}</div><p class="gcount muted small">0 of {len(prizes)} found</p>'
                f'<div class="gwin" hidden><p class="label">You unlocked</p><ul class="gifts">' + ''.join(f'<li><span>{p}</span></li>' for p in prizes) + '</ul>' +
                self.btn(f.get('cta') or 'Continue', 'btn btn-block') + '</div></div>')

    def rounds(self, f):
        out = self.h2(f.get('heading'))
        for i, it in enumerate(f.get('items') or [], 1):
            out += (f'<div class="round"><p class="label">Round {i}</p><h3>{T(it.get("title"))}</h3><p>{T(it.get("body"))}</p>' +
                    (f'<p class="winner">{T(it.get("winner"))}</p>' if it.get('winner') else '') + self.btn(it.get('cta'), 'btn btn-sm') + '</div>')
        return out

    def verdict(self, f):
        return '<div class="verdict">' + self.h2(f.get('heading')) + self.ul(f.get('points')) + self.btn(f.get('cta'), 'btn btn-block') + '</div>'

    def guarantee(self, f):
        return '<div class="guarantee">' + self.h2(f.get('heading')) + f'<p>{T(f.get("body"))}</p></div>'

    def who_for(self, f):
        return (self.h2(f.get('heading')) + '<div class="whofor"><div><p class="label">For you if</p>' + self.ul(f.get('for')) + '</div>' +
                ('<div><p class="label">Not for you if</p>' + self.ul(f.get('not_for'), 'crosses') + '</div>' if f.get('not_for') else '') + '</div>')

    def cta_block(self, f):
        return '<div class="cta-block">' + self.h2(f.get('heading')) + (f'<p>{T(f.get("body"))}</p>' if f.get('body') else '') + self.btn(f.get('cta'), 'btn btn-block') + '</div>'

    def sticky_cta(self, f):
        return f'<div class="sticky"><span>{T(f.get("text"))}</span>{self.btn(f.get("cta"), "btn btn-sm")}</div>'

    def steps(self, f):
        out = ''.join(f'<li><b>{T(it.get("title"))}</b><span>{T(it.get("body"))}</span></li>' for it in (f.get('items') or []))
        return self.h2(f.get('heading')) + f'<ol class="steps">{out}</ol>'

    def stat_strip(self, f):
        return '<div class="stats">' + ''.join(f'<div><b>{T(it.get("number"))}</b><span>{T(it.get("label"))}</span></div>' for it in (f.get('items') or [])) + '</div>'

    def product_grid(self, f):
        out = ''
        for it in f.get('items') or []:
            out += ('<div class="tile">' + self.img(it.get('image')) + (f'<span class="tag">{T(it.get("tag"))}</span>' if it.get('tag') else '') +
                    f'<p class="pname">{T(it.get("name"))}</p><p>' + (f'<s>{T(it.get("anchor"))}</s> ' if it.get('anchor') else '') +
                    f'<b>{T(it.get("price"))}</b></p>' + self.btn('Shop', 'btn btn-sm') + '</div>')
        return self.h2(f.get('heading')) + f'<div class="grid">{out}</div>'

    def image(self, f):
        return self.img(f.get('image')) + (f'<p class="muted small">{T(f.get("caption"))}</p>' if f.get('caption') else '')

    # ---- page ----
    def section(self, s, i):
        kind = s.get('type')
        fn = getattr(self, kind, None)
        if not fn:
            raise SystemExit(f'unknown section type {kind!r} in {s.get("id")}')
        sid = s.get('id') or f's{i:02d}'
        tag = f'<span class="sid">{E(sid.upper())} · {E(kind.replace("_", " "))}</span>' if self.labels else ''
        full = kind in ('offer_bar', 'sticky_cta')
        return f'<section class="s s-{kind}{" full" if full else ""}" id="{E(sid)}" data-sid="{E(sid)}">{tag}{fn(s.get("fields") or {})}</section>'

    def render(self):
        b = self.brief
        pal = {'bg': '#ffffff', 'ink': '#1a1a1a', 'muted': '#6b6b6b', 'accent': '#1a1a1a', 'accent_ink': '#ffffff', 'soft': '#f4f2ee', 'line': '#e6e3dd'}
        pal.update((b.get('tokens') or {}).get('palette') or {})
        fonts = (b.get('tokens') or {}).get('fonts') or {}
        hf, bf = fonts.get('heading') or 'Inter', fonts.get('body') or 'Inter'
        gf = 'https://fonts.googleapis.com/css2?' + '&'.join('family=' + f.replace(' ', '+') + ':wght@400;600;700;800' for f in sorted({hf, bf})) + '&display=swap'
        logo = (b.get('tokens') or {}).get('logo') or {}
        logo_html = (f'<img src="{E(logo["src"])}" alt="{E(b.get("brand_name", ""))}">' if logo.get('src') else f'<b>{E(logo.get("text") or b.get("brand_name", ""))}</b>')
        meta = self.page.get('meta') or {}
        body = ''.join(self.section(s, i) for i, s in enumerate(self.page.get('sections') or [], 1))
        title = meta.get('title') or f'{b.get("brand_name", "")}'
        css = CSS
        root = ':root{' + ''.join(f'--{k.replace("_", "-")}:{v};' for k, v in pal.items()) + f'--hf:"{hf}",system-ui,sans-serif;--bf:"{bf}",system-ui,sans-serif;}}'
        if self.artifact:
            # Published as a claude.ai page: the Artifact tool adds the doctype, head and body itself.
            return (f'<title>{E(title)}</title><link rel="preconnect" href="https://fonts.googleapis.com"><link href="{E(gf)}" rel="stylesheet">'
                    f'<style>{root}{css}</style><header class="top">{logo_html}</header><main>{body}</main>'
                    f'<footer class="foot">{E(b.get("brand_name", ""))}</footer><script>{JS}</script>')
        return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
                f'<title>{E(title)}</title><link rel="preconnect" href="https://fonts.googleapis.com"><link href="{E(gf)}" rel="stylesheet">'
                f'<style>{root}{css}</style></head><body{" class=labels" if self.labels else ""}>'
                f'<header class="top">{logo_html}</header><main>{body}</main>'
                f'<footer class="foot">{E(b.get("brand_name", ""))}</footer><script>{JS}</script></body></html>')


CSS = """
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--bf);font-size:17px;line-height:1.55}
main{max-width:640px;margin:0 auto;padding:0 18px 90px}
h1,h2,h3{font-family:var(--hf);line-height:1.15;letter-spacing:-.01em;margin:0 0 12px}
h1{font-size:32px;font-weight:800}h2{font-size:25px;font-weight:800;margin-top:6px}h3{font-size:19px;font-weight:700}
p{margin:0 0 14px}a{color:inherit}
.top{display:flex;justify-content:center;align-items:center;padding:12px 18px;border-bottom:1px solid var(--line)}
.top img{max-height:28px}.top b{font-family:var(--hf);font-size:20px;letter-spacing:.02em}
.s{position:relative;padding:28px 0;border-bottom:1px solid var(--line)}.s:last-child{border-bottom:0}
.s.full{padding:0;border:0}
.s-offer_bar{margin:0 -18px}.offer-bar{background:var(--accent);color:var(--accent-ink);text-align:center;font-weight:700;font-size:14px;padding:9px 14px;letter-spacing:.01em}
.hero{text-align:center}.eyebrow{font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);margin-bottom:10px}
.sub{font-size:18px;color:var(--muted)}
.img{display:block;width:100%;border-radius:14px;margin:14px 0;background:var(--soft)}
.ph-img{aspect-ratio:4/3;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;padding:16px;text-align:center;
 background:repeating-linear-gradient(45deg,var(--soft),var(--soft) 10px,var(--bg) 10px,var(--bg) 20px);border:2px dashed var(--line);color:var(--muted)}
.ph-img span{font-weight:800;font-size:12px;letter-spacing:.1em}.ph-img small{font-size:13px}
mark.ph{background:#ffe86b;color:#1a1a1a;padding:0 3px;border-radius:3px}
.checks,.crosses{list-style:none;padding:0;margin:0 0 16px;text-align:left}
.checks li,.crosses li{padding:6px 0 6px 28px;position:relative}
.checks li:before{content:"✓";position:absolute;left:4px;color:var(--accent);font-weight:800}
.crosses li:before{content:"✕";position:absolute;left:4px;color:var(--muted);font-weight:800}
.btn{display:inline-block;background:var(--accent);color:var(--accent-ink);text-decoration:none;font-weight:800;font-size:17px;padding:15px 26px;border-radius:999px;text-align:center;margin:6px 0}
.btn-block{display:block;width:100%}.btn-sm{font-size:15px;padding:11px 20px}
.trust-mini{display:flex;flex-wrap:wrap;justify-content:center;gap:6px 14px;margin-top:12px;font-size:13px;color:var(--muted)}
.byline{display:flex;gap:12px;align-items:center;font-size:14px}.byline div{display:flex;flex-direction:column}
.avatar{width:44px;height:44px;border-radius:50%;background:var(--soft);display:flex!important;align-items:center;justify-content:center;font-weight:800}
.muted{color:var(--muted)}.small{font-size:13px}.label{font-size:12px;font-weight:800;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);margin:0 0 8px}
.disclosure{font-size:12px;color:var(--muted);text-transform:uppercase;letter-spacing:.06em;margin:0}
.press{display:flex;flex-wrap:wrap;justify-content:center;gap:10px 22px;font-family:var(--hf);font-weight:700;color:var(--muted);font-size:15px}
.trust-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;text-align:center;font-size:14px;font-weight:600}
.trust-row div{background:var(--soft);border-radius:12px;padding:12px 8px}
.note{background:var(--soft);border-radius:16px;padding:20px}.sign{font-style:italic}
.reason{position:relative;padding:18px 0 6px}.num{width:38px;height:38px;border-radius:50%;background:var(--accent);color:var(--accent-ink);display:flex;align-items:center;justify-content:center;font-weight:800;margin-bottom:10px}
.cards{display:grid;gap:12px}.card{background:var(--soft);border-radius:14px;padding:16px}.card p{margin:0}
.table-wrap{overflow-x:auto}table{width:100%;border-collapse:collapse;font-size:14px}th,td{padding:10px 8px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}
th.hi,td.hi{background:var(--soft);font-weight:700}
.reviews{display:grid;gap:12px}.review{margin:0;background:var(--soft);border-radius:14px;padding:16px}.review blockquote{margin:0 0 8px}.review figcaption{font-size:14px;font-weight:700}
.stars{color:#f5a623;letter-spacing:2px;margin-bottom:6px}
.timeline,.steps{list-style:none;padding:0;margin:0;counter-reset:t}.timeline li,.steps li{display:flex;flex-direction:column;padding:10px 0 10px 18px;border-left:3px solid var(--accent);margin-left:6px}
.buybox{border:2px solid var(--ink);border-radius:18px;padding:18px}.pname{font-weight:800;font-size:19px;margin-bottom:4px}.rating{font-size:14px;color:var(--muted)}
.opts{display:grid;gap:10px;margin:12px 0}.opt{display:flex;align-items:center;gap:10px;border:1.5px solid var(--line);border-radius:12px;padding:12px;cursor:pointer}
.opt input{accent-color:var(--accent)}.opt-l{flex:1;display:flex;flex-direction:column;font-weight:700}.opt-l small{font-weight:400;color:var(--muted)}.opt-p{font-weight:800}.opt-p s{color:var(--muted);font-weight:400}
.gifts,.stack{list-style:none;padding:0;margin:0 0 14px}.gifts li,.stack li{display:flex;justify-content:space-between;gap:10px;padding:8px 0;border-bottom:1px dashed var(--line)}
.stack s{color:var(--muted)}.total{font-weight:800;font-size:20px;text-align:center}
.guar{text-align:center;font-size:14px;margin-top:10px}
details{border-bottom:1px solid var(--line);padding:12px 0}summary{font-weight:700;cursor:pointer}details p{margin:10px 0 0}
.quiz{background:var(--soft);border-radius:18px;padding:20px;text-align:center}.qopts{display:grid;gap:10px;margin:14px 0}
.qopt{font:inherit;font-weight:700;background:var(--bg);border:1.5px solid var(--line);border-radius:12px;padding:14px;cursor:pointer}.qopt:hover{border-color:var(--accent)}
.skip{font-size:14px;color:var(--muted)}.qload ul{list-style:none;padding:0}.reward{font-weight:800}
.game{text-align:center;padding-top:8px}.gcards{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:16px 0}
.gcard{aspect-ratio:3/4;border:0;border-radius:14px;background:var(--accent);color:var(--accent-ink);font:inherit;font-size:28px;font-weight:800;cursor:pointer}
.gcard.open{background:var(--soft);color:var(--ink);font-size:14px;padding:8px}
.round{border-left:3px solid var(--accent);padding:4px 0 4px 16px;margin:18px 0}.winner{font-weight:800}
.verdict,.guarantee,.cta-block{background:var(--soft);border-radius:18px;padding:20px;text-align:center}
.whofor{display:grid;gap:10px}
.sticky{position:fixed;left:0;right:0;bottom:0;display:flex;gap:12px;align-items:center;justify-content:space-between;background:var(--bg);border-top:1px solid var(--line);padding:10px 16px;z-index:5;font-weight:700;font-size:14px}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:12px;text-align:center}.stats b{display:block;font-family:var(--hf);font-size:30px}.stats span{font-size:14px;color:var(--muted)}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}.tile{background:var(--soft);border-radius:14px;padding:10px;display:flex;flex-direction:column;gap:4px}.tile .img{margin:0 0 6px}.tag{font-size:11px;font-weight:800;text-transform:uppercase;color:var(--accent)}
.foot{text-align:center;color:var(--muted);font-size:13px;padding:24px}
.sid{position:absolute;top:6px;right:0;z-index:3;font:700 11px/1 ui-monospace,Menlo,monospace;background:#1a1a1a;color:#fff;padding:4px 7px;border-radius:6px;opacity:.85}
.labels .s-offer_bar .sid{top:auto;bottom:-20px;right:18px}.labels .s-sticky_cta .sid{top:-22px;right:8px}
"""

JS = r"""
document.querySelectorAll('.quiz').forEach(q=>{const steps=[...q.querySelectorAll('.qstep')];let i=0;
 q.addEventListener('click',e=>{const b=e.target.closest('.qopt');if(!b)return;steps[i].hidden=true;i++;
  if(i<steps.length){steps[i].hidden=false}else{const l=q.querySelector('.qload');l.hidden=false;setTimeout(()=>{l.hidden=true;q.querySelector('.qresult').hidden=false},1400)}});});
document.querySelectorAll('.game').forEach(g=>{const box=g.querySelector('.gcards');const prizes=JSON.parse(box.dataset.prizes||'[]');let found=0;
 box.addEventListener('click',e=>{const c=e.target.closest('.gcard');if(!c||c.classList.contains('open')||found>=prizes.length)return;
  c.classList.add('open');c.innerHTML=prizes[found];found++;g.querySelector('.gcount').textContent=found+' of '+prizes.length+' found';
  if(found>=prizes.length){setTimeout(()=>{g.querySelector('.gwin').hidden=false},500)}});});
"""


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    run = sys.argv[1]
    page = json.load(open(os.path.join(run, 'page.json')))
    brief = json.load(open(os.path.join(run, 'brief.json')))
    labels = '--labels' in sys.argv
    out = arg('--out') or os.path.join(run, 'page-labelled.html' if labels else 'page.html')
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    doc = Page(page, brief, labels, '--artifact' in sys.argv).render()
    open(out, 'w').write(doc)
    ph = len(PH.findall(json.dumps(page)))
    print(f'wrote {out} ({len(page.get("sections") or [])} sections, {ph} placeholders still open)')


if __name__ == '__main__':
    main()

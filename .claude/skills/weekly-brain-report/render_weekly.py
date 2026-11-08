#!/usr/bin/env python3
"""Render the weekly brain report: one clean page from a JSON data file.

  python3 render_weekly.py report.json [out.html] [--pdf]

Standard library only. Every section is optional: a section that is missing from the data file is
left out; a section marked "data_limited" shows what it needs. Text may use **bold** and *italic*.
The data file's shape is in schema.md. --pdf prints the page with headless Chrome or Edge if found
(CHROME=<path> overrides), one render, no loop.
"""
import html, json, os, re, shutil, subprocess, sys

LABEL_CLASS = {"verified": "v", "stated": "s", "inferred": "i", "data-limited": "d"}


def esc(s):
    return html.escape(str(s if s is not None else ""), quote=True)


def md(s):
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return re.sub(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"<i>\1</i>", s)


def chip(label):
    if not label:
        return ""
    key = str(label).lower()
    return f'<span class="chip {LABEL_CLASS.get(key, "d")}">{esc(label)}</span>'


def cards(items, cols=3):
    out = []
    for c in items or []:
        out.append(f'<div class="card"><h3>{md(c.get("title"))}</h3><p>{md(c.get("body"))}</p>{chip(c.get("label"))}</div>')
    return f'<div class="grid g{cols}">{"".join(out)}</div>'


def section(kicker, title, intro, body, state=""):
    intro_html = f'<p class="intro">{md(intro)}</p>' if intro else ""
    return (f'<section class="sec {state}"><div class="pill">{esc(kicker)}</div><h2>{md(title)}</h2>{intro_html}{body}</section>')


def limited(box):
    need = box.get("needs") or "the data for this section"
    return f'<div class="callout lim"><b>Data-limited.</b> {md(need)}</div>'


def lines(items, kind):
    rows = "".join(
        f'<li><b>{md(i.get("title"))}</b>{(" · " + md(i.get("detail"))) if i.get("detail") else ""} {chip(i.get("label"))}</li>'
        for i in items or [])
    return f'<div class="col {kind}"><h3>{"Working" if kind == "good" else "Dying but still spending"}</h3><ul>{rows or "<li>None this week</li>"}</ul></div>'


def render(d):
    m = d.get("meta", {})
    parts = []
    if m.get("example"):
        parts.append('<div class="example">Example data: placeholder brand and made-up numbers. Replace everything before use.</div>')
    parts.append(f'<header><div class="pill">{esc(m.get("kicker", "Weekly report"))}</div><h1>{md(m.get("brand", "[BRAND]"))}: {md(d.get("headline", "Weekly report"))}</h1>'
                 f'<p class="meta">{esc(m.get("week_label", ""))} {("· " + esc(m.get("date_range"))) if m.get("date_range") else ""}</p>'
                 f'{("<p class=intro>" + md(d.get("intro")) + "</p>") if d.get("intro") else ""}</header>')
    if d.get("key_points"):
        parts.append(section("The short version", "The things that matter this week", None, cards(d["key_points"])))
    a = d.get("account")
    if a:
        body = limited(a) if a.get("data_limited") else (
            f'<div class="two">{lines(a.get("working"), "good")}{lines(a.get("dying"), "bad")}</div>'
            + (f'<div class="callout warn">{md(a.get("note"))}</div>' if a.get("note") else ""))
        parts.append(section("Account", "What's working, what's dying", a.get("summary"), body))
    c = d.get("competitors")
    if c:
        parts.append(section("Competitive intelligence", "Competitors: the moves and the gaps", c.get("summary"),
                             limited(c) if c.get("data_limited") else cards(c.get("cards"))))
    v = d.get("voice")
    if v:
        if v.get("data_limited"):
            body = limited(v)
        else:
            rows = []
            for n, it in enumerate(v.get("items") or [], 1):
                quote = f'<q>{esc(it.get("quote"))}</q> <span class="src">{esc(it.get("source"))}</span>' if it.get("quote") else ""
                rows.append(f'<div class="vrow"><span class="num">{n}</span><div><b>{md(it.get("theme"))}</b><p>{quote} {md(it.get("note"))} {chip(it.get("label"))}</p></div></div>')
            body = "".join(rows)
        parts.append(section("Voice of customer", "What the customer is telling us, in their words", v.get("summary"), body))
    o = d.get("openings")
    if o:
        def col(box):
            if not box:
                return ""
            li = "".join(f'<li>{md(i.get("text"))} {chip(i.get("label"))}</li>' for i in box.get("items") or [])
            call = f'<div class="callout warn">{md(box.get("callout"))}</div>' if box.get("callout") else ""
            return f'<div class="col"><h3>{md(box.get("title"))}</h3>{("<p>" + md(box.get("intro")) + "</p>") if box.get("intro") else ""}<ul>{li}</ul>{call}</div>'
        parts.append(section("Organic and affinity", "Where the openings are", o.get("summary"),
                             f'<div class="two">{col(o.get("organic"))}{col(o.get("affinity"))}</div>'))
    n = d.get("next")
    if n:
        rows = "".join(
            f'<div class="card"><h3>{md(c.get("name"))}</h3><p><b>Who:</b> {md(c.get("persona"))}<br><b>Angle:</b> {md(c.get("angle"))}<br>{md(c.get("why"))}</p>'
            f'{chip(c.get("label"))}{("<span class=verdict>" + esc(c.get("verdict")) + "</span>") if c.get("verdict") else ""}</div>'
            for c in n.get("concepts") or [])
        parts.append(section("Next", "What to make next", n.get("summary"), f'<div class="grid g3">{rows}</div>'))
    j = d.get("judging")
    if j:
        js = "".join(f'<div class="card judge"><h3>{md(x.get("name"))}</h3><p>{md(x.get("text"))}</p></div>' for x in j.get("judges") or [])
        died = f'<h4>What died and why</h4><p>{md(j.get("died"))}</p>' if j.get("died") else ""
        parts.append(section("Judging method", j.get("title", "How the concepts were judged"), j.get("summary"), f'<div class="grid g3">{js}</div>{died}'))
    if d.get("limits"):
        parts.append(section("Honest limits", "What we couldn't see", None, "<ul class=lim>" + "".join(f"<li>{md(x)}</li>" for x in d["limits"]) + "</ul>"))
    if d.get("sources"):
        parts.append(section("Sources", "Where this came from", None,
                             "<ul class=src2>" + "".join(f'<li><b>{esc(s.get("name"))}</b>: {md(s.get("what"))} <span>{esc(s.get("date"))}</span></li>' for s in d["sources"]) + "</ul>"))
    foot = f'<footer>{esc(m.get("concept_label", ""))} {("· " + esc(m.get("prepared_by"))) if m.get("prepared_by") else ""}</footer>'
    return parts, foot, m.get("accent", "#5b4fd6")


CSS = """
:root{--a:%(a)s;--ink:#1d1d1b;--mut:#6b6a63;--line:#dcdad2;--bg:#f7f6f2}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 -apple-system,Segoe UI,Inter,Helvetica,Arial,sans-serif}
.wrap{max-width:1040px;margin:0 auto;padding:36px 28px 60px}
header,.sec{background:#fff;border:1px solid var(--line);border-radius:16px;padding:28px 32px;margin:0 0 18px}
.pill{display:inline-block;background:color-mix(in srgb,var(--a) 14%%,#fff);color:color-mix(in srgb,var(--a) 80%%,#000);font-size:11px;letter-spacing:.06em;text-transform:uppercase;font-weight:700;border-radius:6px;padding:4px 9px;margin-bottom:10px}
h1{font-size:34px;line-height:1.15;margin:0 0 8px;letter-spacing:-.02em}h2{font-size:26px;line-height:1.2;margin:0 0 8px;letter-spacing:-.015em}h3{font-size:16px;margin:0 0 6px}h4{margin:14px 0 4px}
.meta{color:var(--mut);margin:0 0 6px}.intro{color:#3c3c38;margin:0 0 16px;max-width:820px}
.grid{display:grid;gap:14px}.sec h2+.grid{margin-top:16px}.g3{grid-template-columns:repeat(3,1fr)}.g2{grid-template-columns:repeat(2,1fr)}
.card{border:1px solid var(--line);border-left:4px solid var(--a);border-radius:10px;padding:14px 16px;background:#fff}.card p{margin:0 0 8px;font-size:14px}
.card.judge{background:color-mix(in srgb,var(--a) 8%%,#fff);border-left-color:var(--a)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:18px}.col{border:1px solid var(--line);border-radius:10px;padding:14px 18px}.col.good h3{color:#1f7a3d}.col.bad h3{color:#b3261e}
ul{margin:0;padding-left:18px}li{margin:0 0 7px;font-size:14px}
.callout{border-radius:8px;padding:12px 16px;margin-top:14px;font-size:14px}.callout.warn{background:#fff6cc;border:1px solid #ecd36a}.callout.lim{background:#f1f0ea;border:1px dashed #b9b6a8}
.vrow{display:flex;gap:14px;border:1px solid var(--line);border-radius:10px;padding:12px 16px;margin-bottom:10px}.num{background:color-mix(in srgb,var(--a) 14%%,#fff);border-radius:6px;width:26px;height:26px;display:grid;place-items:center;font-weight:700;flex:none}
.vrow p{margin:2px 0 0;font-size:14px}q{font-style:italic}.src{color:var(--mut);font-size:12px}
.chip{display:inline-block;font-size:10.5px;font-weight:700;border-radius:99px;padding:1px 8px;border:1px solid}.chip.v{color:#1f7a3d;border-color:#1f7a3d}.chip.s{color:#2d5fa6;border-color:#2d5fa6}.chip.i{color:#9a6200;border-color:#9a6200}.chip.d{color:#6b6a63;border-color:#6b6a63}
.verdict{float:right;font-size:11px;font-weight:700;color:var(--a)}.example{background:#ffe9e7;border:1px solid #e9a29b;color:#8a1f16;padding:10px 16px;border-radius:8px;margin-bottom:16px;font-weight:600}
ul.lim li,ul.src2 li{font-size:13.5px}ul.src2 span{color:var(--mut);font-size:12px}footer{color:var(--mut);font-size:12px;text-align:center;margin-top:24px}
@media(max-width:760px){.g3,.two{grid-template-columns:1fr}.wrap{padding:16px}header,.sec{padding:20px}}
@media print{body{background:#fff}.wrap{padding:0}.sec,header{break-inside:avoid;margin-bottom:10px}}
"""


def find_chrome():
    for p in (os.environ.get("CHROME"), r"C:\Program Files\Google\Chrome\Application\chrome.exe", r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
              r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"):
        if p and os.path.exists(p):
            return p
    return shutil.which("google-chrome") or shutil.which("chromium") or shutil.which("chrome")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit(__doc__)
    data = json.load(open(args[0], encoding="utf-8"))
    out = args[1] if len(args) > 1 else os.path.splitext(args[0])[0] + ".html"
    parts, foot, accent = render(data)
    title = esc(data.get("meta", {}).get("brand", "Weekly report"))
    doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
           f'<title>{title} weekly report</title><style>{CSS % {"a": accent}}</style></head><body><div class="wrap">{"".join(parts)}{foot}</div></body></html>')
    open(out, "w", encoding="utf-8", newline="\n").write(doc)
    print("wrote", out)
    if "--pdf" in sys.argv:
        chrome = find_chrome()
        if not chrome:
            print("no Chrome or Edge found: open the HTML and print it to PDF")
            return
        pdf = os.path.splitext(out)[0] + ".pdf"
        subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={os.path.abspath(pdf)}",
                        "file:///" + os.path.abspath(out).replace("\\", "/")], check=False, capture_output=True, timeout=120)
        print("wrote", pdf if os.path.exists(pdf) else "(PDF failed: print the HTML to PDF)")


if __name__ == "__main__":
    main()

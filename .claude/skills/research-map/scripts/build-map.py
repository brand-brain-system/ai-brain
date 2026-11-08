#!/usr/bin/env python3
"""Build the research map: one self-contained HTML page from quotes and groups.

    python3 build-map.py <research-map folder>

Reads  <folder>/evidence.jsonl  one quote per line
       <folder>/groups.json     layers, groups, which desires each group links to
Writes <folder>/map.html and prints the checks (the page is written even if they warn).

Evidence row: id, group, quote, source, url, date, author, pull
  author  a pseudonymous id (hash), never a handle or a name
  pull    "unweighted" (counts) or "searched" (shown in the drawer, never counted)
Groups are ranked by the number of DIFFERENT authors in the unweighted pull. The same
person saying it three times counts once.
"""
import html
import json
import sys
from collections import defaultdict
from pathlib import Path


def load(folder: Path):
    groups = json.loads((folder / "groups.json").read_text(encoding="utf-8"))
    rows = []
    for n, line in enumerate((folder / "evidence.jsonl").read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as err:
                sys.exit(f"evidence.jsonl line {n}: {err}")
    return groups, rows


def analyse(groups, rows):
    warn = []
    gids = {g["id"] for g in groups["groups"]}
    lids = {l["id"] for l in groups["layers"]}
    per = defaultdict(list)
    for r in rows:
        if r.get("group") not in gids:
            warn.append(f"quote {r.get('id')}: unknown group {r.get('group')!r}")
            continue
        for k in ("quote", "source", "url", "author", "pull"):
            if not r.get(k):
                warn.append(f"quote {r.get('id')}: missing {k}")
        if r.get("pull") not in ("unweighted", "searched"):
            warn.append(f"quote {r.get('id')}: pull must be unweighted or searched")
        per[r["group"]].append(r)
    base = {r["author"] for r in rows if r.get("pull") == "unweighted" and r.get("author")}
    out = []
    for g in groups["groups"]:
        if g["layer"] not in lids:
            warn.append(f"group {g['id']}: unknown layer {g['layer']!r}")
        rs = per.get(g["id"], [])
        people = {r["author"] for r in rs if r.get("pull") == "unweighted" and r.get("author")}
        sources = {r["source"] for r in rs if r.get("pull") == "unweighted" and r.get("source")}
        if not rs:
            warn.append(f"group {g['id']}: no quotes")
        elif len(people) < 2:
            warn.append(f"group {g['id']}: {len(people)} person in the unweighted pull, a lead for hypotheses/, not a finding")
        for d in g.get("desires", []):
            if d not in gids:
                warn.append(f"group {g['id']}: unknown desire {d!r}")
        out.append({**g, "people": len(people), "sources": len(sources), "quotes": rs})
    return out, len(base), warn


PAGE = """<!doctype html><html lang="__LANG__"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title><style>
:root{--bg:#f3f5f4;--card:#fff;--ink:#16302f;--mute:#6b7b7a;--line:#dfe5e3}
@media(prefers-color-scheme:dark){:root{--bg:#121918;--card:#1b2625;--ink:#e6efed;--mute:#93a5a3;--line:#2c3a38}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.4 system-ui,sans-serif}
main{max-width:1000px;margin:0 auto;padding:16px}h1{font-size:22px;margin:8px 0}
.lim{color:var(--mute);font-size:13px;margin:0 0 12px}
#chips{position:sticky;top:0;z-index:2;background:var(--bg);padding:8px 0;display:flex;flex-wrap:wrap;gap:6px;align-items:center}
.chip{border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:99px;padding:5px 11px;cursor:pointer;font:inherit}
.chip i,.tag i{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:6px}
.chip.on{outline:2px solid var(--ink)}
section{background:var(--card);border-radius:14px;padding:14px;margin:14px 0}
h2{font-size:12px;letter-spacing:.08em;text-transform:uppercase;margin:0;color:var(--mute)}
h3{margin:2px 0 10px;font-size:18px}
.g{position:relative;border:1px solid var(--line);border-radius:10px;margin:6px 0;padding:9px 80px 9px 12px;cursor:pointer;overflow:hidden}
.g .bar{position:absolute;inset:0 auto 0 0;opacity:.14}
.g>*{position:relative}.g .bar{position:absolute}.g .n{position:absolute;right:12px;top:6px;text-align:right;font-weight:700;font-size:20px}
.g .n small{display:block;font-size:10px;font-weight:400;color:var(--mute);letter-spacing:.06em;text-transform:uppercase}
.g .sub{color:var(--mute);font-size:13px}.tag{display:inline-block;font-size:11px;border:1px solid var(--line);border-radius:99px;padding:1px 8px;margin:4px 4px 0 0;text-transform:uppercase;letter-spacing:.04em}
.g.dim{opacity:.25}.g.hit{outline:2px solid var(--ink)}
#drawer{position:fixed;inset:0 0 0 auto;width:min(460px,100%);background:var(--card);box-shadow:-6px 0 24px #0003;padding:16px;overflow:auto;transform:translateX(105%);transition:.2s;z-index:5}
#drawer.open{transform:none}#drawer button{float:right}
blockquote{margin:8px 0;padding:8px 12px;border-left:3px solid var(--ink);background:var(--bg);border-radius:6px}
blockquote small{display:block;color:var(--mute);margin-top:4px}blockquote a{color:inherit}
</style><main><h1>__TITLE__</h1><p class="lim">__LIMIT__</p><div id="chips"></div><div id="root"></div></main>
<aside id="drawer"></aside><script>
const D=__DATA__;const U=D.unit;
const col=id=>(D.layers.find(l=>l.id===id)||{}).color||'#567';
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const byId=Object.fromEntries(D.groups.map(g=>[g.id,g]));
const desires=D.groups.filter(g=>g.layer===D.desireLayer);
let sel=null;
function chips(){document.getElementById('chips').innerHTML='<b style="font-size:12px;color:var(--mute)">LIGHT UP A DESIRE</b>'+
 desires.map(d=>`<button class="chip ${sel===d.id?'on':''}" data-d="${d.id}"><i style="background:${col(d.layer)}"></i>${esc(d.short||d.title)} ${D.groups.filter(g=>(g.desires||[]).includes(d.id)).length}</button>`).join('');
 document.querySelectorAll('.chip').forEach(b=>b.onclick=()=>{sel=sel===b.dataset.d?null:b.dataset.d;render()})}
function render(){chips();document.getElementById('root').innerHTML=D.layers.map(l=>{
 const gs=D.groups.filter(g=>g.layer===l.id).sort((a,b)=>b.people-a.people);if(!gs.length)return'';const max=gs[0].people||1;
 return `<section><h2 style="color:${l.color}">${esc(l.label)}</h2><h3>${esc(l.title)} <small style="color:var(--mute);font-weight:400">${gs.length} groups</small></h3>`+gs.map(g=>{
  const hit=sel&&(g.id===sel||(g.desires||[]).includes(sel));
  const tags=(g.desires||[]).map(d=>`<span class="tag"><i style="background:${col(byId[d].layer)}"></i>${esc(byId[d].short||byId[d].title)}</span>`).join('');
  return `<div class="g ${sel?(hit?'hit':'dim'):''}" data-g="${g.id}"><div class="bar" style="width:${100*g.people/max}%;background:${l.color}"></div>
  <div>${esc(g.title)}</div>${g.note?`<div class="sub">${esc(g.note)}</div>`:''}${tags}
  <div class="n">${g.people}<small>${esc(U)}${g.base?' · '+Math.round(100*g.people/g.base)+'%':''}</small></div></div>`}).join('')+'</section>'}).join('');
 document.querySelectorAll('.g').forEach(e=>e.onclick=()=>openG(e.dataset.g))}
function openG(id){const g=byId[id];const d=document.getElementById('drawer');
 d.innerHTML=`<button onclick="this.parentNode.classList.remove('open')">Close</button><h2>${esc(g.layer)}</h2><h3>${esc(g.title)}</h3><p class="lim">${g.people} ${esc(U)} · ${g.sources} sources · ${g.quotes.length} quotes</p>`+
 g.quotes.map(q=>`<blockquote>“${esc(q.quote)}”<small>${esc(q.source)}${q.date?' · '+esc(q.date):''}${q.pull==='searched'?' · searched pull, not counted':''} · <a href="${esc(q.url)}" target="_blank" rel="noopener">Open original ↗</a></small></blockquote>`).join('');
 d.classList.add('open')}
render();
</script></html>"""


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    folder = Path(sys.argv[1])
    groups, rows = load(folder)
    out, base, warn = analyse(groups, rows)
    for g in out:
        g["base"] = base
    meta = groups.get("meta", {})
    data = {
        "unit": meta.get("unit", "people"),
        "desireLayer": meta.get("desire_layer", "desire"),
        "layers": groups["layers"],
        "groups": out,
    }
    blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    limit = meta.get("limit") or (
        f"Counts are different {data['unit']} in the unweighted pull ({base} in all); "
        "quotes from searched pulls are shown but not counted. Posts are not customers."
    )
    page = (PAGE.replace("__LANG__", meta.get("lang", "en"))
            .replace("__TITLE__", html.escape(meta.get("title", "Research map")))
            .replace("__LIMIT__", html.escape(limit))
            .replace("__DATA__", blob))
    (folder / "map.html").write_text(page, encoding="utf-8")
    print(f"{len(out)} groups, {len(rows)} quotes, {base} {data['unit']} in the unweighted pull -> {folder / 'map.html'}")
    for g in sorted(out, key=lambda g: -g["people"])[:5]:
        print(f"  {g['people']:>3}  {g['layer']:<10} {g['title']}")
    for w in warn:
        print("WARN", w)


if __name__ == "__main__":
    main()

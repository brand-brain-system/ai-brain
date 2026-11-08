#!/usr/bin/env python3
"""Build the template picker artifact from the swipe file's index.html.

The swipe page (`<swipe>/index.html`) stays the one source of the cards. This
script turns it into `<swipe>/picker.html`, the page that is published as the
"Landing Page Picker" artifact: same cards, but "Build this one" saves the pick
to the artifact's database (collection `picks`) so Claude reads it back, instead
of copying a line to paste.

Usage: python3 lp-picker.py            (writes <swipe>/picker.html and prints the publish files map)
Then publish or republish it with the Artifact tool (see processes/pick-template.md).
"""
import json, pathlib, re, sys

SKILL = pathlib.Path(__file__).resolve().parent.parent
SWIPE = next((p for p in [SKILL.parent / "landing-page-swipe-file", SKILL / "swipe-file",
                          SKILL.parents[2] / "brain-system/.claude/skills/new-landing-page/swipe-file"] if p.exists()), None)
if not SWIPE:
    sys.exit("swipe file not found next to the skill or inside it")

src = (SWIPE / "index.html").read_text()
style = re.search(r"<style>(.*?)</style>", src, re.S).group(1)
body = re.search(r"<body>(.*)</body>", src, re.S).group(1)

# Header copy: how to pick here.
body = re.sub(
    r"To make one for a brand, press <b>Build this one</b>.*?</p>",
    "To make one, press <b>Build this one</b> on a card, "
    "then go back to Claude and say <b>picked</b>.</p>",
    body, flags=re.S)
body = body.replace("</header>", '  <div class="lastpick" id="lastpick" hidden></div>\n</header>', 1)

OLD_HANDLER = re.search(r"grid\.addEventListener\('click', async e=>\{.*?\n\}\);\n", body, re.S)
if not OLD_HANDLER:
    sys.exit("could not find the Build this one handler in index.html; update lp-picker.py")

NEW_HANDLER = r"""
// Picking: "Build this one" saves the pick for Claude in one click. No ad field:
// the reviewer names an ad in chat when there is one (Alex, 2026-10-01).
const dbP = (async()=>{ try{ return window.claude ? await claude.use("db") : null }catch(e){ return null } })();
const userP = (async()=>{ try{ return window.claude ? await claude.use("user") : null }catch(e){ return null } })();
grid.addEventListener('click', async e=>{
  const b = e.target.closest('.pick'); if(!b) return;
  const card = b.closest('.card');
  let msg = card.querySelector('.pfmsg');
  if(!msg){ msg = document.createElement('div'); msg.className='pfmsg'; msg.setAttribute('role','status'); card.querySelector('.body').appendChild(msg); }
  grid.querySelectorAll('.pfmsg').forEach(x=>{ if(x!==msg){ x.textContent=''; x.classList.remove('ok'); } });
  const line = b.dataset.line;
  const m = line.match(/^LANDING PAGE TEMPLATE: (lp-\d+) (.*) \(reference: ([^,]+), (.*)\)$/);
  b.disabled = true;
  const db = await dbP, user = await userP;
  if(db && m){
    try{
      const at = new Date().toISOString();
      const by = user && user.id ? await user.id() : null;
      const pick = {template_id:m[1], template_name:m[2], ref:m[3], ref_brand:m[4], line, at, by};
      await db.collection("picks").doc(at.replace(/[^0-9A-Za-z]/g,'')).set(pick);
      msg.textContent = 'Picked. Go back to Claude and say "picked".';
      msg.classList.add('ok'); showLast(pick); b.disabled = false; return;
    }catch(err){ /* fall through to copy */ }
  }
  try{ await navigator.clipboard.writeText(line); msg.textContent = 'Could not save it here, so I copied it. Paste it to Claude.'; }
  catch(err){ msg.innerHTML = 'Copy this line and paste it to Claude:<br><code></code>'; msg.querySelector('code').textContent = line; }
  b.disabled = false;
});
function showLast(p){
  const el = document.getElementById('lastpick'); if(!p) return;
  el.textContent = `Last pick: ${p.template_id} ${p.template_name}, reference ${p.ref_brand} (${p.ref})`;
  el.hidden = false;
}
(async()=>{
  const db = await dbP; if(!db) return;
  try{ db.collection("picks").orderBy("at","desc").limit(1).onSnapshot(snap=>{ const d = snap.docs && snap.docs[0]; if(d) showLast(d.data ? d.data() : d); }); }catch(e){}
})();
"""
body = body.replace(OLD_HANDLER.group(0), NEW_HANDLER.lstrip("\n"))

EXTRA_CSS = """
.lastpick{margin-top:14px;display:inline-block;background:var(--accent-soft);color:var(--accent);border-radius:8px;padding:6px 10px;font-size:13px;font-weight:500}
.pick:focus-visible,.chip:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.pick:disabled{opacity:.6;cursor:wait}
.pfmsg{min-height:1em;color:var(--muted);font-size:13px;margin-top:4px}
.pfmsg.ok{color:var(--accent);font-weight:600}
.pfmsg code{display:block;margin-top:4px;user-select:all;word-break:break-all;font-size:12px}
"""

fonts = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'
out = f"<title>Landing Page Picker</title>\n{fonts}\n<style>{style}{EXTRA_CSS}</style>\n{body.strip()}\n"
(SWIPE / "picker.html").write_text(out)

files = {f"screenshots/{p.name}": str(p) for p in sorted((SWIPE / "screenshots").glob("*.jpg"))}
files.update({f"screenshots/desktop/{p.name}": str(p) for p in sorted((SWIPE / "screenshots" / "desktop").glob("*.jpg"))})
files.update({f"brands/{p.name}": str(p) for p in sorted((SWIPE / "brands").glob("*.md"))})
files.update({f"pages/{p.name}": str(p) for p in sorted((SWIPE / "pages").glob("*.html"))})
files["README.md"] = str(SWIPE / "README.md")
print(f"wrote {SWIPE / 'picker.html'}")
print(json.dumps(files, indent=1))

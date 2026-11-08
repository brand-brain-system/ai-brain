// Full-page phone captures plus page facts, for the site-watch routine.
//
// Usage: node site-capture.mjs <pages.json> <out-dir>
//   pages.json: [{"name": "home", "url": "https://..."}, ...]
//
// For each page: a 390x844 iPhone viewport (the width must never change, or every page looks
// "changed"), slow scroll to the bottom and back so lazy images and reviews load, cookie walls and
// pop-ups removed (the promo bar stays), then the full page captured in pieces of at most 4000 px
// and stitched into <name>.png by stitch.py. Pages taller than Chrome's ~8,192 px limit therefore
// still reach the footer. Also writes <name>.html (the raw page, for spotting A/B promo variants)
// and <name>.json (the facts compared text-to-text: promo bar, headings, buttons, prices, reviews).
// Never clicks a buy button, fills a form or goes to checkout: the cart is done by hand in the
// routine, with the browser tools.
//
// Based on Alex Cooper's lp-screenshot.mjs (new-landing-page skill, Parker course), 2026-10-06.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { spawn, execFileSync } from 'child_process';
import { fileURLToPath } from 'url';

const [pagesFile, outDir] = process.argv.slice(2);
if (!pagesFile || !outDir) { console.error('usage: node site-capture.mjs <pages.json> <out-dir>'); process.exit(2); }
const pages = JSON.parse(fs.readFileSync(pagesFile, 'utf8'));
fs.mkdirSync(outDir, { recursive: true });
const here = path.dirname(fileURLToPath(import.meta.url));
const W = 390, VH = 844, PIECE = 4000;

const chrome = process.env.CHROME || (process.platform === 'win32'
  ? [path.join(process.env.PROGRAMFILES || '', 'Google', 'Chrome', 'Application', 'chrome.exe'),
     path.join(process.env['PROGRAMFILES(X86)'] || '', 'Microsoft', 'Edge', 'Application', 'msedge.exe')].find(p => fs.existsSync(p))
  : '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome');
const port = 9300 + Math.floor(Math.random() * 600);
const prof = fs.mkdtempSync(path.join(os.tmpdir(), 'site-watch-'));
const proc = spawn(chrome, ['--headless', '--no-sandbox', '--disable-gpu', `--remote-debugging-port=${port}`, `--user-data-dir=${prof}`,
  '--no-first-run', '--no-default-browser-check', '--disable-extensions', '--hide-scrollbars', 'about:blank'], { stdio: 'ignore' });
const sleep = ms => new Promise(r => setTimeout(r, ms));
const done = code => { try { proc.kill(); } catch {} try { fs.rmSync(prof, { recursive: true, force: true }); } catch {} process.exit(code); };
setTimeout(() => { console.error('timed out'); done(1); }, 120000 * Math.max(1, pages.length));

let t;
for (let i = 0; i < 40; i++) {
  try { t = await (await fetch(`http://127.0.0.1:${port}/json/new?about:blank`, { method: 'PUT' })).json(); break; } catch { await sleep(250); }
}
if (!t) { console.error('chrome did not start'); done(1); }
const ws = new WebSocket(t.webSocketDebuggerUrl);
await new Promise(r => ws.onopen = r);
let id = 0; const pend = {};
let status = null;
ws.onmessage = m => {
  const d = JSON.parse(m.data);
  if (d.id && pend[d.id]) { pend[d.id](d); delete pend[d.id]; }
  if (d.method === 'Network.responseReceived' && d.params.type === 'Document' && status === null) status = d.params.response.status;
};
const send = (method, params = {}) => new Promise(r => { const i = ++id; pend[i] = r; ws.send(JSON.stringify({ id: i, method, params })); });
const evalv = async expr => { const r = await send('Runtime.evaluate', { expression: expr, returnByValue: true, awaitPromise: true }); return r.result && r.result.result && r.result.result.value; };

await send('Network.enable');
await send('Network.setUserAgentOverride', { userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1' });
await send('Emulation.setDeviceMetricsOverride', { width: W, height: VH, deviceScaleFactor: 1, mobile: true });
await send('Page.enable');

// Remove cookie walls, email pop-ups and dialogs: fixed elements covering over a quarter of the screen.
const clean = `(() => { const vw = innerWidth, vh = innerHeight; let n = 0;
  for (const el of Array.from(document.querySelectorAll('body *'))) { const cs = getComputedStyle(el);
    if (cs.position === 'fixed') { const r = el.getBoundingClientRect(); if (r.width * r.height > vw * vh * 0.25) { el.remove(); n++; continue; } }
    if (el.tagName === 'DIALOG' || el.getAttribute('aria-modal') === 'true') { el.remove(); n++; } }
  for (const s of [document.documentElement, document.body]) { s.style.overflow = 'visible'; }
  return n; })()`;

// The facts compared day to day. Text, not pixels.
const facts = `(() => {
  const vis = el => { const r = el.getBoundingClientRect(), cs = getComputedStyle(el); return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none'; };
  const txt = el => (el.innerText || '').replace(/\\s+/g, ' ').trim();
  const uniq = a => [...new Set(a.filter(Boolean))];
  const bars = uniq(Array.from(document.querySelectorAll('[class*=announcement],[class*=Announcement],[class*=promo],[class*=Promo],[id*=announcement],[class*=marquee],[class*=top-bar],[class*=topbar]')).filter(vis).map(txt).filter(s => s.length < 300));
  const body = document.body.innerText;
  const lines = body.split('\\n').map(s => s.trim()).filter(Boolean);
  const grab = re => uniq(lines.filter(l => re.test(l) && l.length < 200));
  return {
    title: document.title,
    promo_bar: bars.slice(0, 6),
    h1: uniq(Array.from(document.querySelectorAll('h1')).filter(vis).map(txt)).slice(0, 4),
    h2: uniq(Array.from(document.querySelectorAll('h2')).filter(vis).map(txt)).slice(0, 15),
    buttons: uniq(Array.from(document.querySelectorAll('button, a[class*=btn], a[class*=button], input[type=submit]')).filter(vis).map(txt).filter(s => s.length < 60)).slice(0, 25),
    prices: grab(/(\\$|€|£|kr\\.?|DKK)\\s?\\d|\\d[\\d.,]*\\s?(kr|DKK|€)/i).slice(0, 40),
    strikethrough: uniq(Array.from(document.querySelectorAll('s, del, strike, [class*=compare], [class*=Compare], body *')).filter(el => el.tagName.match(/^(S|DEL|STRIKE)$/) || /compare/i.test(el.className) || (el.children.length === 0 && getComputedStyle(el).textDecorationLine.includes('line-through'))).filter(vis).map(txt).filter(s => s && s.length < 40)).slice(0, 20),
    review_widgets: Array.from(document.querySelectorAll('iframe')).map(f => f.src).filter(u => /loox|judge\.me|okendo|yotpo|stamped|trustpilot|reviews\.io/i.test(u)).slice(0, 3),
    reviews: grab(/review|anmeldelse|rating|stars|stjerne|★/i).slice(0, 20),
    offers_and_trust: grab(/free shipping|fri fragt|gratis|guarantee|garanti|gift|gave|bundle|save|spar|off\\b|rabat|% /i).slice(0, 30),
    broken_images: Array.from(document.images).filter(i => i.complete && i.naturalWidth === 0 && vis(i)).map(i => i.currentSrc || i.src).slice(0, 20),
    text_length: body.length
  };
})()`;

const results = [];
for (const pg of pages) {
  status = null;
  const name = pg.name.replace(/[^a-z0-9_-]/gi, '-');
  await send('Emulation.setDeviceMetricsOverride', { width: W, height: VH, deviceScaleFactor: 1, mobile: true });
  await send('Page.navigate', { url: pg.url });
  await sleep(8000);
  await evalv(clean);
  // Slow scroll to the bottom and back, twice if the page grew (lazy sections).
  for (let pass = 0; pass < 2; pass++) {
    await evalv(`(async()=>{const h=()=>document.documentElement.scrollHeight;for(let y=0;y<h();y+=300){scrollTo(0,y);await new Promise(r=>setTimeout(r,180));}await new Promise(r=>setTimeout(r,1200));scrollTo(0,0);})()`);
  }
  await sleep(1000);
  await evalv(clean);
  const full = await evalv('document.documentElement.scrollHeight') || VH;
  const f = await evalv(facts) || {};
  const html = await evalv('document.documentElement.outerHTML') || '';
  fs.writeFileSync(path.join(outDir, `${name}.html`), html);
  const parts = [];
  for (let y = 0, k = 0; y < full; y += PIECE, k++) {
    const h = Math.min(PIECE, full - y);
    const shot = await send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: true, clip: { x: 0, y, width: W, height: h, scale: 1 } });
    const p = path.join(outDir, `${name}.part${k}.png`);
    fs.writeFileSync(p, Buffer.from(shot.result.data, 'base64'));
    parts.push(p);
  }
  const outPng = path.join(outDir, `${name}.png`);
  try {
    execFileSync(process.platform === 'win32' ? 'python' : 'python3', [path.join(here, 'stitch.py'), outPng, ...parts], { stdio: 'inherit' });
    for (const p of parts) fs.rmSync(p);
  } catch (e) { console.error(`stitch failed for ${name}; pieces kept`); }
  // Review widgets live in cross-origin iframes that don't paint in a full-page capture: read their
  // page instead, for the count and rating (e.g. Loox: "629 Reviews 4.7 (536) (36) ...").
  f.review_widget_text = [];
  for (const u of (f.review_widgets || [])) {
    try {
      const html = await (await fetch(u, { headers: { 'User-Agent': 'Mozilla/5.0' } })).text();
      const plain = html.replace(/<(script|style)[\s\S]*?<\/>/g, ' ').replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ');
      const m = plain.match(/(\d[\d,.]*)\s+Reviews?\s+(\d(?:\.\d)?)((?:\s*\(\d[\d,]*\)){0,5})/i);
      f.review_widget_text.push(m ? m[0].trim() : 'no count found in widget');
    } catch (e) { f.review_widget_text.push('widget not readable'); }
  }
  const rec = { name, url: pg.url, http_status: status, captured_at: new Date().toISOString(), viewport: `${W}x${VH}`, page_height: full, pieces: parts.length, ...f };
  fs.writeFileSync(path.join(outDir, `${name}.json`), JSON.stringify(rec, null, 1));
  results.push({ name, status, height: full, promo: (f.promo_bar || [])[0] || '' });
  console.log(`${name}: HTTP ${status}, ${W}x${full} in ${parts.length} piece(s)${(f.broken_images || []).length ? `, ${f.broken_images.length} broken image(s)` : ''}`);
}
ws.close();
await sleep(500); // let the socket close first: exiting mid-close trips a libuv assert on Windows
done(0);

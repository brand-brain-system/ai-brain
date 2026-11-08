// Phone-width screenshot of a landing page (a built draft or a live URL), with pop-ups cleared.
//
// Usage: node lp-screenshot.mjs <file-or-url> <out.png> [--height 4000] [--width 390] [--desktop] [--keep-popups]
// --desktop captures at 1440px wide with a desktop browser (the web version); default is a 390px phone.
//
// Launches its own headless Chrome (macOS path by default, CHROME=/path to override) with a throwaway
// profile, emulates an iPhone at 390px wide, waits for the page, removes large fixed overlays and dialogs
// (cookie walls, email pop-ups, country pickers) unless --keep-popups, scrolls once to load lazy images,
// and captures the top <height> pixels. Plain `chrome --screenshot` hangs on some pages and cannot clear
// pop-ups, which is why this drives Chrome over its debugging protocol instead (swipe-file build, 2026-09-29).
import fs from 'fs';
import os from 'os';
import path from 'path';
import { spawn } from 'child_process';
import { pathToFileURL } from 'url';

const args = process.argv.slice(2);
const opt = (n, d) => { const i = args.indexOf(n); return i >= 0 ? args[i + 1] : d; };
const [target, out] = args;
if (!target || !out) { console.error('usage: node lp-screenshot.mjs <file-or-url> <out.png> [--height 4000] [--width 390] [--keep-popups]'); process.exit(2); }
const desk = args.includes('--desktop');
const W = +opt('--width', desk ? 1440 : 390), H = +opt('--height', 4000), keep = args.includes('--keep-popups');
const url = /^https?:|^file:/.test(target) ? target : pathToFileURL(path.resolve(target)).href;
// Windows default added 2026-10-06 (the original assumed macOS). CHROME=/path still overrides.
const chrome = process.env.CHROME || (process.platform === 'win32'
  ? [path.join(process.env.PROGRAMFILES || "", "Google", "Chrome", "Application", "chrome.exe"), path.join(process.env["PROGRAMFILES(X86)"] || "", "Microsoft", "Edge", "Application", "msedge.exe")].find(p => fs.existsSync(p))
  : '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome');
const port = 9300 + Math.floor(Math.random() * 600);
const prof = fs.mkdtempSync(path.join(os.tmpdir(), 'lp-shot-'));
const proc = spawn(chrome, ['--headless', '--no-sandbox', '--disable-gpu', `--remote-debugging-port=${port}`, `--user-data-dir=${prof}`,
  '--no-first-run', '--no-default-browser-check', '--disable-extensions', '--hide-scrollbars', '--allow-file-access-from-files', 'about:blank'], { stdio: 'ignore' });
const sleep = ms => new Promise(r => setTimeout(r, ms));
const done = code => { try { proc.kill(); } catch {} try { fs.rmSync(prof, { recursive: true, force: true }); } catch {} process.exit(code); };
setTimeout(() => { console.error('timed out'); done(1); }, 90000);

let t;
for (let i = 0; i < 40; i++) {
  try { t = await (await fetch(`http://127.0.0.1:${port}/json/new?about:blank`, { method: 'PUT' })).json(); break; } catch { await sleep(250); }
}
if (!t) { console.error('chrome did not start'); done(1); }
const ws = new WebSocket(t.webSocketDebuggerUrl);
await new Promise(r => ws.onopen = r);
let id = 0; const pend = {};
ws.onmessage = m => { const d = JSON.parse(m.data); if (d.id && pend[d.id]) { pend[d.id](d); delete pend[d.id]; } };
const send = (method, params = {}) => new Promise(r => { const i = ++id; pend[i] = r; ws.send(JSON.stringify({ id: i, method, params })); });
await send('Network.enable');
await send('Network.setUserAgentOverride', { userAgent: desk ? 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0 Safari/537.36' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1' });
await send('Emulation.setDeviceMetricsOverride', { width: W, height: desk ? 900 : 844, deviceScaleFactor: 1, mobile: !desk });
await send('Page.enable');
await send('Page.navigate', { url });
await sleep(/^file:/.test(url) ? 2500 : 8000);
const clean = `(() => { const vw = innerWidth, vh = innerHeight; let n = 0;
  for (const el of Array.from(document.querySelectorAll('body *'))) { const cs = getComputedStyle(el);
    if (cs.position === 'fixed' && !el.classList.contains('sticky') && !el.closest('.s-offer_bar')) { const r = el.getBoundingClientRect(); if (r.width * r.height > vw * vh * 0.25) { el.remove(); n++; continue; } }
    if (el.tagName === 'DIALOG' || el.getAttribute('aria-modal') === 'true') { el.remove(); n++; } }
  for (const s of [document.documentElement, document.body]) { s.style.overflow = 'visible'; s.style.height = 'auto'; }
  return n; })()`;
if (!keep) await send('Runtime.evaluate', { expression: clean });
await send('Runtime.evaluate', { expression: `(async()=>{for(let y=0;y<${H};y+=400){scrollTo(0,y);await new Promise(r=>setTimeout(r,150));}scrollTo(0,0);})()`, awaitPromise: true });
await sleep(800);
if (!keep) await send('Runtime.evaluate', { expression: clean });
const m = await send('Runtime.evaluate', { expression: 'document.documentElement.scrollHeight', returnByValue: true });
const full = Math.min(H, (m.result && m.result.result && m.result.result.value) || H);
// Phone: keep the real phone viewport and capture beyond it. Stretching a mobile viewport to the full page height
// makes some sites re-lay out wider than the screen, which cropped the right side of the swipe screenshots (2026-10-01).
if (desk) await send('Emulation.setDeviceMetricsOverride', { width: W, height: full, deviceScaleFactor: 1, mobile: false });
await sleep(800);
const shot = await send('Page.captureScreenshot', desk ? { format: 'png' } : { format: 'png', captureBeyondViewport: true, clip: { x: 0, y: 0, width: W, height: full, scale: 1 } });
fs.mkdirSync(path.dirname(path.resolve(out)), { recursive: true });
fs.writeFileSync(out, Buffer.from(shot.result.data, 'base64'));
console.log(`wrote ${out} (${W}x${full})`);
ws.close();
done(0);

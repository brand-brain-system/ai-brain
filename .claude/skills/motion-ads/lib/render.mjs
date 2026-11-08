// render.mjs: render a seek(t) page to video, frame by frame, with headless Chrome + ffmpeg. No npm packages.
//
// Usage: node render.mjs <page.html> [options]
//   --format 9x16|4x5|1x1   frame size, read by the page (default 9x16)
//   --scale 0.5             output scale: 0.5 = preview (540 wide), 1 = final (default 0.5)
//   --fps 30                frames per second (default 30)
//   --dur 8                 seconds (default: the page's window.DUR)
//   --sub 1                 subframes blended per frame for motion blur; 2 doubles the work (default 1)
//   --audio track.wav       mux an audio track, normalised to about -14 LUFS (default: silent)
//   --alpha                 transparent background, ProRes 4444 .mov, for overlays in video-edits
//   --stills 0,1.5,4        write PNG stills at these times instead of a video (cheapest check)
//   --out out/preview.mp4   output file, or the folder for --stills (default out/<format>_<scale>.mp4)
//
// Light on the PC: the process drops itself to below-normal priority before starting Chrome and ffmpeg (both
// inherit it on Windows) and gives ffmpeg half the cores. Preview at --scale 0.5; render --scale 1 once.
// Adapted from the motion-design course's route A (movez Substack, Oct 2026), rewritten for Windows: file URLs
// via pathToFileURL, the Chrome DevTools protocol instead of Playwright, fonts loaded explicitly by the page.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { spawn } from 'child_process';
import { pathToFileURL } from 'url';

const args = process.argv.slice(2);
const opt = (n, d) => { const i = args.indexOf(n); return i >= 0 ? args[i + 1] : d; };
const page = args[0];
if (!page || page.startsWith('--')) { console.error('usage: node render.mjs <page.html> [--format 9x16] [--scale 0.5] [--fps 30] [--dur 8] [--sub 1] [--audio f] [--alpha] [--stills 0,1.5] [--out f]'); process.exit(2); }
const FORMAT = opt('--format', '9x16'), SCALE = +opt('--scale', 0.5), FPS = +opt('--fps', 30), SUB = Math.max(1, +opt('--sub', 1));
const AUDIO = opt('--audio', null), ALPHA = args.includes('--alpha');
const STILLS = opt('--stills', null)?.split(',').map(Number);
const OUT = opt('--out', STILLS ? 'out/stills' : `out/${FORMAT}_${SCALE === 1 ? 'final' : 'preview'}${ALPHA ? '.mov' : '.mp4'}`);

try { os.setPriority(0, os.constants.priority.PRIORITY_BELOW_NORMAL); } catch { console.warn('could not lower priority'); }
const threads = String(Math.max(1, Math.floor(os.cpus().length / 2)));

const chrome = process.env.CHROME || (process.platform === 'win32'
  ? [path.join(process.env.PROGRAMFILES || '', 'Google', 'Chrome', 'Application', 'chrome.exe'), path.join(process.env['PROGRAMFILES(X86)'] || '', 'Microsoft', 'Edge', 'Application', 'msedge.exe')].find((p) => fs.existsSync(p))
  : '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome');
const port = 9300 + Math.floor(Math.random() * 600);
const prof = fs.mkdtempSync(path.join(os.tmpdir(), 'motion-'));
const proc = spawn(chrome, ['--headless', '--no-sandbox', `--remote-debugging-port=${port}`, `--user-data-dir=${prof}`,
  '--no-first-run', '--no-default-browser-check', '--disable-extensions', '--hide-scrollbars', '--allow-file-access-from-files',
  '--force-color-profile=srgb', '--font-render-hinting=none', 'about:blank'], { stdio: 'ignore' });
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const cleanup = () => { try { proc.kill(); } catch {} try { fs.rmSync(prof, { recursive: true, force: true }); } catch {} };
const fail = (msg) => { console.error('FAILED: ' + msg); cleanup(); process.exit(1); };

let target;
for (let i = 0; i < 40; i++) {
  try { target = await (await fetch(`http://127.0.0.1:${port}/json/new?about:blank`, { method: 'PUT' })).json(); break; } catch { await sleep(250); }
}
if (!target) fail('chrome did not start');
const ws = new WebSocket(target.webSocketDebuggerUrl);
await new Promise((r) => (ws.onopen = r));
let id = 0; const pend = {}; let loaded = null;
ws.onmessage = (m) => {
  const d = JSON.parse(m.data);
  if (d.id && pend[d.id]) { pend[d.id](d); delete pend[d.id]; }
  if (d.method === 'Page.loadEventFired' && loaded) loaded();
};
const send = (method, params = {}) => new Promise((r) => { const i = ++id; pend[i] = r; ws.send(JSON.stringify({ id: i, method, params })); });
const evaluate = async (expression) => {
  const r = await send('Runtime.evaluate', { expression, awaitPromise: true, returnByValue: true });
  if (r.result?.exceptionDetails) fail(`page error in "${expression.slice(0, 40)}": ${r.result.exceptionDetails.exception?.description || r.result.exceptionDetails.text}`);
  return r.result?.result?.value;
};

await send('Page.enable');
const url = pathToFileURL(path.resolve(page)).href + `?render=1&format=${FORMAT}`;
await new Promise(async (r) => { loaded = r; await send('Page.navigate', { url }); });
const size = await evaluate('window.SIZE');
if (!size) fail('the page has no window.SIZE: is it built from template.html?');
const [W, H] = size;
await send('Emulation.setDeviceMetricsOverride', { width: W, height: H, deviceScaleFactor: 1, mobile: false });
if (ALPHA) await send('Emulation.setDefaultBackgroundColorOverride', { color: { r: 0, g: 0, b: 0, a: 0 } });
const ok = await Promise.race([evaluate('window.ready'), sleep(30000).then(() => 'timeout')]);
if (ok !== true) fail('window.ready did not resolve in 30 s (fonts or images not loading?)');
const errs = await evaluate('window.__errors');
if (errs?.length) fail('page reported: ' + errs.join(' | '));
const DUR = +opt('--dur', await evaluate('window.DUR'));
const outW = Math.round(W * SCALE / 2) * 2, outH = Math.round(H * SCALE / 2) * 2; // even sizes for H.264

const shot = async (t) => {
  await evaluate(`window.seek(${t})`);
  const r = await send('Page.captureScreenshot', { format: 'png', fromSurface: true, clip: { x: 0, y: 0, width: W, height: H, scale: outW / W } });
  if (!r.result?.data) fail('screenshot failed at t=' + t);
  return Buffer.from(r.result.data, 'base64');
};

if (STILLS) {
  fs.mkdirSync(OUT, { recursive: true });
  for (const t of STILLS) fs.writeFileSync(path.join(OUT, `${FORMAT}_t${t.toFixed(2)}.png`), await shot(t));
  console.log(`wrote ${STILLS.length} stills to ${OUT} (${outW}x${outH})`);
  ws.close(); cleanup(); process.exit(0);
}

fs.mkdirSync(path.dirname(path.resolve(OUT)), { recursive: true });
const final = SCALE >= 1;
const vf = [`scale=${outW}:${outH}:flags=lanczos`];
if (SUB > 1) vf.unshift(`tmix=frames=${SUB}`, `select='eq(mod(n\\,${SUB})\\,${SUB - 1})'`, `setpts=N/${FPS}/TB`);
const ffArgs = ['-hide_banner', '-loglevel', 'error', '-y', '-f', 'image2pipe', '-framerate', String(FPS * SUB), '-i', '-'];
if (AUDIO) ffArgs.push('-i', AUDIO);
ffArgs.push('-vf', vf.join(','), '-r', String(FPS), '-t', String(DUR), '-threads', threads);
if (ALPHA) ffArgs.push('-c:v', 'prores_ks', '-profile:v', '4444', '-pix_fmt', 'yuva444p10le');
else ffArgs.push('-c:v', 'libx264', '-preset', final ? 'medium' : 'veryfast', '-crf', final ? '17' : '23', '-pix_fmt', 'yuv420p', '-movflags', '+faststart');
if (AUDIO) ffArgs.push('-map', '0:v', '-map', '1:a', '-af', 'apad,loudnorm=I=-14:TP=-1.5:LRA=11', '-c:a', ALPHA ? 'pcm_s16le' : 'aac', '-b:a', '192k', '-ar', '48000');
ffArgs.push(OUT);
const ff = spawn('ffmpeg', ffArgs, { stdio: ['pipe', 'inherit', 'inherit'] });
let ffDone = false; const ffClosed = new Promise((r) => ff.on('close', (c) => { ffDone = true; r(c); }));

const total = Math.round(DUR * FPS * SUB);
const t0 = Date.now();
for (let i = 0; i < total; i++) {
  if (ffDone) fail('ffmpeg stopped early');
  const png = await shot(i / (FPS * SUB));
  if (!ff.stdin.write(png)) await new Promise((r) => ff.stdin.once('drain', r));
  if (i % (FPS * SUB) === 0) console.log(`rendered ${(i / (FPS * SUB)).toFixed(0)} s / ${DUR} s`);
}
ff.stdin.end();
const code = await ffClosed;
const late = await evaluate('window.__errors');
ws.close(); cleanup();
if (code !== 0) fail('ffmpeg exited with ' + code);
if (late?.length) fail('page reported during render: ' + late.join(' | '));
console.log(`wrote ${OUT} (${outW}x${outH}, ${FPS} fps, ${DUR} s, ${total} frames) in ${((Date.now() - t0) / 1000).toFixed(0)} s`);

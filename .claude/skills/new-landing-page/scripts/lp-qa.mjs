// Functional browser QA for a built landing page.
//
// Usage:
//   node lp-qa.mjs <file-or-url> --out <qa.json> [--cta-url <url>]
//
// This is intentionally a non-submitting check. It opens the page at desktop and
// phone widths, exercises safe local interactions, and reports wiring that still
// needs a human check. It never submits a form or follows a CTA.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { spawn } from 'child_process';
import { pathToFileURL } from 'url';

const args = process.argv.slice(2);
const target = args[0];
const opt = (name, fallback = '') => {
  const i = args.indexOf(name);
  return i >= 0 ? args[i + 1] : fallback;
};
if (!target) {
  console.error('usage: node lp-qa.mjs <file-or-url> --out <qa.json> [--cta-url <url>]');
  process.exit(2);
}

const out = path.resolve(opt('--out', 'lp-qa.json'));
const expectedCta = opt('--cta-url');
const url = /^https?:|^file:/.test(target) ? target : pathToFileURL(path.resolve(target)).href;
// Windows default added 2026-10-06 (the original assumed macOS). CHROME=/path still overrides.
const chrome = process.env.CHROME || (process.platform === 'win32'
  ? [path.join(process.env.PROGRAMFILES || "", "Google", "Chrome", "Application", "chrome.exe"), path.join(process.env["PROGRAMFILES(X86)"] || "", "Microsoft", "Edge", "Application", "msedge.exe")].find(p => fs.existsSync(p))
  : '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome');
const port = 9900 + Math.floor(Math.random() * 500);
const profile = fs.mkdtempSync(path.join(os.tmpdir(), 'lp-qa-'));
const proc = spawn(chrome, [
  '--headless', '--no-sandbox', '--disable-gpu', `--remote-debugging-port=${port}`,
  `--user-data-dir=${profile}`, '--no-first-run', '--no-default-browser-check',
  '--disable-extensions', '--allow-file-access-from-files', 'about:blank'
], { stdio: 'ignore' });

const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
const cleanup = () => {
  try { proc.kill(); } catch {}
  try { fs.rmSync(profile, { recursive: true, force: true }); } catch {}
};
const timeout = setTimeout(() => {
  console.error('timed out');
  cleanup();
  process.exit(1);
}, 90000);

let tab;
for (let i = 0; i < 40; i++) {
  try {
    tab = await (await fetch(`http://127.0.0.1:${port}/json/new?about:blank`, { method: 'PUT' })).json();
    break;
  } catch {
    await sleep(250);
  }
}
if (!tab) {
  clearTimeout(timeout);
  cleanup();
  console.error('chrome did not start');
  process.exit(1);
}

const ws = new WebSocket(tab.webSocketDebuggerUrl);
await new Promise(resolve => { ws.onopen = resolve; });
let id = 0;
const pending = new Map();
const consoleErrors = [];
const exceptions = [];
const networkFailures = [];
ws.onmessage = message => {
  const data = JSON.parse(message.data);
  if (data.id && pending.has(data.id)) {
    pending.get(data.id)(data);
    pending.delete(data.id);
    return;
  }
  if (data.method === 'Runtime.consoleAPICalled' && data.params.type === 'error') {
    consoleErrors.push((data.params.args || []).map(x => x.value ?? x.description ?? '').join(' '));
  }
  if (data.method === 'Runtime.exceptionThrown') {
    exceptions.push(data.params.exceptionDetails?.text || 'uncaught browser exception');
  }
  if (data.method === 'Network.loadingFailed' && !data.params.canceled) {
    networkFailures.push(data.params.errorText || 'network request failed');
  }
};
const send = (method, params = {}) => new Promise(resolve => {
  const callId = ++id;
  pending.set(callId, resolve);
  ws.send(JSON.stringify({ id: callId, method, params }));
});
const evaluate = async expression => {
  const response = await send('Runtime.evaluate', { expression, awaitPromise: true, returnByValue: true });
  if (response.error || response.result?.exceptionDetails) {
    const detail = response.result?.exceptionDetails;
    throw new Error(response.error?.message || detail?.exception?.description || detail?.text || 'browser evaluation failed');
  }
  return response.result.result.value;
};

await send('Runtime.enable');
await send('Network.enable');
await send('Page.enable');
await send('Page.addScriptToEvaluateOnNewDocument', { source: `(() => {
  const original = EventTarget.prototype.addEventListener;
  EventTarget.prototype.addEventListener = function(type, listener, options) {
    if (this instanceof Element) {
      if (type === 'submit') this.dataset.lpSubmitListener = '1';
      if (type === 'click') this.dataset.lpClickListener = '1';
    }
    return original.call(this, type, listener, options);
  };
})()` });
await send('Emulation.setDeviceMetricsOverride', { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false });
await send('Page.navigate', { url });
await sleep(/^file:/.test(url) ? 2500 : 7000);

const scrollForLazyAssets = async () => {
  await evaluate(`(async () => {
    const height = Math.min(document.documentElement.scrollHeight, 14000);
    for (let y = 0; y < height; y += 500) {
      scrollTo(0, y);
      await new Promise(resolve => setTimeout(resolve, 80));
    }
    scrollTo(0, 0);
    await new Promise(resolve => setTimeout(resolve, 300));
    return true;
  })()`);
};

const collect = async label => evaluate(String.raw`(() => {
  const normal = value => {
    try { return new URL(value, location.href).href.replace(/\/$/, ''); }
    catch { return value || ''; }
  };
  const expected = ${JSON.stringify(expectedCta)};
  const links = [...document.querySelectorAll('a')].map(a => ({
    text: (a.innerText || a.getAttribute('aria-label') || '').trim().slice(0, 100),
    raw: a.getAttribute('href') || '',
    href: a.href || ''
  }));
  const ctas = [...document.querySelectorAll('a.pill, a[class*="cta" i], a[data-cta], a[role="button"]')]
    .map(a => ({ text: (a.innerText || a.getAttribute('aria-label') || '').trim().slice(0, 100), href: a.href || '' }));
  const assets = [...document.querySelectorAll('img[src], script[src], video[src], audio[src], source[src], link[rel="stylesheet"][href]')]
    .map(el => ({ tag: el.tagName.toLowerCase(), src: el.src || el.href || '' }));
  const images = [...document.images].map(img => ({
    alt: img.getAttribute('alt'), src: img.currentSrc || img.src || '',
    complete: img.complete, width: img.naturalWidth, height: img.naturalHeight
  }));
  const forms = [...document.forms].map(form => {
    const submitters = [...form.querySelectorAll('button[type="submit"], input[type="submit"]')];
    const action = form.getAttribute('action') || '';
    const wired = Boolean(action || form.getAttribute('onsubmit') || form.dataset.lpSubmitListener === '1' || submitters.some(x => x.dataset.lpClickListener === '1'));
    return { action, method: (form.getAttribute('method') || 'get').toLowerCase(), submitters: submitters.length, wired };
  });
  return {
    label: ${JSON.stringify(label)}, title: document.title,
    viewport: { width: innerWidth, height: innerHeight },
    layout: { scrollWidth: document.documentElement.scrollWidth, clientWidth: document.documentElement.clientWidth },
    placeholderLinks: links.filter(x => !x.raw || x.raw === '#' || /^javascript:/i.test(x.raw)),
    missingHashTargets: links.filter(x => x.raw.startsWith('#') && x.raw.length > 1 && !document.getElementById(x.raw.slice(1))),
    ctas,
    ctaMismatches: expected ? ctas.filter(x => normal(x.href) !== normal(expected)) : [],
    assetsOutsideFile: assets.filter(x => x.src && !x.src.startsWith('data:') && !x.src.startsWith('blob:')),
    brokenImages: images.filter(x => !x.complete || x.width === 0),
    missingAlt: images.filter(x => x.alt === null),
    forms,
    details: document.querySelectorAll('details').length,
    visiblePlaceholders: (document.body.innerText.match(/\[(?:OFFER|STAT NEEDED|PHOTO|CODE|DATE|PRICE|CREATOR VIDEO)[^\]]*\]/g) || [])
  };
})()`);

await scrollForLazyAssets();
const desktop = await collect('desktop');
const interactions = await evaluate(`(() => {
  const tested = [];
  for (const details of document.querySelectorAll('details')) {
    const before = details.open;
    details.querySelector('summary')?.click();
    tested.push({ type: 'details', changed: details.open !== before });
  }
  for (const control of document.querySelectorAll('[data-tab], [role="tab"], button[data-src]')) {
    control.click();
    tested.push({ type: 'safe-control', text: (control.innerText || control.getAttribute('aria-label') || '').trim().slice(0, 80), clicked: true });
  }
  return tested;
})()`);

await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 1, mobile: true });
await sleep(500);
await scrollForLazyAssets();
const mobile = await collect('mobile');

const failures = [];
const warnings = [];
for (const view of [desktop, mobile]) {
  if (view.layout.scrollWidth > view.layout.clientWidth + 2) failures.push(`${view.label}: horizontal overflow (${view.layout.scrollWidth}px > ${view.layout.clientWidth}px)`);
  if (view.brokenImages.length) failures.push(`${view.label}: ${view.brokenImages.length} broken image(s)`);
  if (view.placeholderLinks.length) failures.push(`${view.label}: ${view.placeholderLinks.length} empty, #, or javascript link(s)`);
  if (view.missingHashTargets.length) failures.push(`${view.label}: ${view.missingHashTargets.length} missing internal link target(s)`);
  if (view.assetsOutsideFile.length) failures.push(`${view.label}: ${view.assetsOutsideFile.length} non-embedded asset(s) in a self-contained deliverable`);
  if (expectedCta && !view.ctas.length) failures.push(`${view.label}: no CTA-like links found`);
  if (view.ctaMismatches.length) failures.push(`${view.label}: ${view.ctaMismatches.length} CTA link(s) do not match --cta-url`);
  for (const form of view.forms) {
    if (!form.submitters) failures.push(`${view.label}: form has no submit control`);
    else if (!form.wired) warnings.push(`${view.label}: form submission could not be verified automatically`);
  }
  if (view.missingAlt.length) warnings.push(`${view.label}: ${view.missingAlt.length} image(s) have no alt attribute`);
}
if (interactions.some(x => x.type === 'details' && !x.changed)) failures.push('one or more details/FAQ controls did not toggle');
if (consoleErrors.length) failures.push(`${consoleErrors.length} console error(s)`);
if (exceptions.length) failures.push(`${exceptions.length} uncaught browser exception(s)`);
if (networkFailures.length) failures.push(`${networkFailures.length} failed network request(s)`);

const report = {
  target: url,
  checkedAt: new Date().toISOString(),
  expectedCta: expectedCta || null,
  result: failures.length ? 'fail' : 'pass',
  failures,
  warnings,
  consoleErrors,
  exceptions,
  networkFailures,
  interactions,
  desktop,
  mobile,
  note: 'Forms were inspected but not submitted. Test any live submission only with explicit approval.'
};
fs.mkdirSync(path.dirname(out), { recursive: true });
fs.writeFileSync(out, JSON.stringify(report, null, 2) + '\n');
console.log(`${report.result.toUpperCase()}: ${out}`);
for (const item of failures) console.error(`FAIL: ${item}`);
for (const item of warnings) console.warn(`WARN: ${item}`);

clearTimeout(timeout);
ws.close();
cleanup();
process.exit(failures.length ? 1 : 0);

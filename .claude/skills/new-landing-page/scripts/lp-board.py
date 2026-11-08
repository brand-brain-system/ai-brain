#!/usr/bin/env python3
"""Build the draft board (or the final board) for a landing-page run.

Usage: python3 lp-board.py <run_dir> <out_dir> [--final]

Draft mode (default): rebuilds the page with section labels, and writes into <out_dir>:
  <slug>-draft-v<N>.html   the board page (assets/board-template.html filled; never fill it by hand)
  page.html                the labelled draft the board draws inside its phone
  page-final.html          the clean build (what Download the page saves)
  ref/<slug>.jpg           the reference screenshots for the picked template, from the swipe file
  assets/*                 the run's photos (<run>/assets/), so the draft shows real images
  files.json               the map to pass as the Artifact tool's `files`, with `root` = <out_dir>
--final builds the same board around the clean page (no section labels), titled as final.

Publish the board page with capabilities {"db": {}, "downloads": true}. Section feedback is written by
the board to the artifact's db collection "feedback"; the Approve / Needs changes decision to
"decisions/v<N>". Register the URL in references/feedback-boards.md the moment it is published.
The version N is page.json "version" (the revise step bumps it), so every draft gets its own decision.
"""
import sys, os, re, json, shutil, subprocess

SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(SKILL, 'assets', 'board-template.html')


def swipe_shots():
    for p in (os.path.join(SKILL, 'swipe-file', 'screenshots'), os.path.join(os.path.dirname(SKILL), 'landing-page-swipe-file', 'screenshots'),
              os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(SKILL))), 'brain-system', '.claude', 'skills', 'new-landing-page', 'swipe-file', 'screenshots')):
        if os.path.isdir(p):
            return p
    return None


def walk(obj):
    if isinstance(obj, str):
        if obj.strip():
            yield obj
    elif isinstance(obj, list):
        for v in obj:
            yield from walk(v)
    elif isinstance(obj, dict):
        for k, v in obj.items():
            if k in ('src', 'alt', 'default', 'stars', 'cards', 'highlight_col'):
                continue
            if k == 'placeholder':
                if str(v).strip():
                    yield f'[photo: {v}]'
                continue
            yield from walk(v)


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    run, out = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
    final = '--final' in sys.argv
    page = json.load(open(os.path.join(run, 'page.json')))
    brief = json.load(open(os.path.join(run, 'brief.json')))
    tpl = json.load(open(os.path.join(run, 'template.json')))
    os.makedirs(os.path.join(out, 'ref'), exist_ok=True)
    build = os.path.join(SKILL, 'scripts', 'lp-build-page.py')
    subprocess.run([sys.executable, build, run, '--out', os.path.join(out, 'page-final.html')], check=True)
    if final:
        shutil.copy(os.path.join(out, 'page-final.html'), os.path.join(out, 'page.html'))
    else:
        subprocess.run([sys.executable, build, run, '--labels', '--out', os.path.join(out, 'page.html')], check=True)
    shots, refs = swipe_shots(), []
    order = sorted(tpl['refs'], key=lambda r: r['slug'] != tpl.get('primary_ref'))
    for r in order:
        src = shots and os.path.join(shots, r['slug'] + '.jpg')
        if src and os.path.exists(src):
            shutil.copy(src, os.path.join(out, 'ref', r['slug'] + '.jpg'))
            refs.append({'slug': r['slug'], 'brand': r['brand'], 'url': r['url'], 'img': 'ref/' + r['slug'] + '.jpg'})
        else:
            print(f'note: no swipe screenshot for {r["slug"]} (looked in {shots})')
    version = page.get('version', 0)
    brand = brief.get('brand_name') or page.get('brand', '')
    slug = re.sub(r'[^a-z0-9]+', '-', f'{brand}-{tpl["slug"]}'.lower()).strip('-')
    data = {
        'run': os.path.basename(run), 'brand': brand, 'template': tpl['id'], 'templateName': tpl['name'], 'version': version,
        'mode': 'final' if final else 'draft', 'page': 'page.html', 'finalPage': 'page-final.html', 'slug': slug, 'refs': refs,
        'sections': [{'id': s['id'], 'type': s['type'], 'job': s.get('job', ''), 'summary': ' / '.join(walk(s.get('fields') or {}))}
                     for s in page.get('sections') or [] if any(True for _ in walk(s.get('fields') or {}))],
    }
    title = f'{brand} Landing Page' + (' Final' if final else ' Draft')
    html = open(TEMPLATE).read().replace('__TITLE__', title.replace('<', ''))
    html = html.replace('__DATA__', json.dumps(data, ensure_ascii=False).replace('</', '<\\/'))
    name = f'{slug}-{"final" if final else "draft"}-v{version}.html'
    open(os.path.join(out, name), 'w').write(html)
    files = {'page.html': 'page.html', 'page-final.html': 'page-final.html'}
    assets = os.path.join(run, 'assets')
    if os.path.isdir(assets):
        os.makedirs(os.path.join(out, 'assets'), exist_ok=True)
        for f in sorted(os.listdir(assets)):
            if f.startswith('.'):
                continue
            shutil.copy(os.path.join(assets, f), os.path.join(out, 'assets', f))
            files['assets/' + f] = 'assets/' + f
    remote = re.findall(r'"src":\s*"(https?://[^"]+)"', json.dumps(page))
    if remote:
        print(f'note: {len(remote)} image(s) point at another site and will not show on a published board; save them into <run>/assets/ and use "assets/<file>"')
    files.update({r['img']: r['img'] for r in refs})
    json.dump(files, open(os.path.join(out, 'files.json'), 'w'), indent=2)
    print(f'board: {os.path.join(out, name)}\nfiles: {os.path.join(out, "files.json")} ({len(files)} supporting files)\n'
          f'publish with capabilities {{"db": {{}}, "downloads": true}}, root = {out}; then register the URL in references/feedback-boards.md')


if __name__ == '__main__':
    main()

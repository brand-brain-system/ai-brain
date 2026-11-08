#!/usr/bin/env python3
"""Validate the template library and (re)write the readable template cards.

Usage: python3 lp-validate-templates.py [--write-cards]

templates/INDEX.json is the source of truth: one entry per template with its section contract (what the
run scripts read). This checks every entry and, with --write-cards, writes templates/<id>-<slug>.md for
people to read. Fix INDEX.json, never the card.

Checks: unique ids; at least 4 sections; every section has id, type (one the page builder knows), job,
guide, required; section ids unique and in order; at least one reference per template; every reference
screenshot exists in the swipe file; no client performance numbers ($ spend, CPA, ROAS) in story or
notes (the library must stay safe to show).
"""
import sys, os, re, json

SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TYPES = {'offer_bar', 'hero', 'byline', 'disclosure', 'press_bar', 'trust_row', 'text', 'founder_note', 'numbered_reasons', 'benefits',
         'comparison_table', 'reviews', 'timeline', 'buy_box', 'value_stack', 'faq', 'quiz', 'game', 'rounds', 'verdict', 'guarantee',
         'who_for', 'cta_block', 'sticky_cta', 'steps', 'stat_strip', 'product_grid', 'image'}
PRIVATE = re.compile(r'\bCPA\b|\bROAS\b|\$\d[\d,]{4,}', re.I)


def shots_dir():
    for p in (os.path.join(SKILL, 'swipe-file', 'screenshots'), os.path.join(os.path.dirname(SKILL), 'landing-page-swipe-file', 'screenshots'),
              os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(SKILL))), 'brain-system', '.claude', 'skills', 'new-landing-page', 'swipe-file', 'screenshots')):
        if os.path.isdir(p):
            return p


def card(t):
    L = [f'# {t["id"]} {t["name"]}', '', f'**Use when:** {t["use_when"]}', '', f'**Buying phase it serves:** {t["teep"]}', '',
         f'**The brand needs:** {", ".join(t["requires"])}. **Helps to have:** {", ".join(t.get("nice_to_have") or []) or "nothing extra"}.', '',
         '## Why it works', '', t['story'], '', '## Reference pages (in the swipe file)', '']
    for r in t['refs']:
        L.append(f'- {r["brand"]}: {r["url"]} (screenshot `{r["slug"]}.jpg`, breakdown `brands/{r["file"]}`)')
    L += ['', '## Section contract', '', '| # | Section | Required | Its job | What to write |', '|---|---|---|---|---|']
    for s in t['sections']:
        L.append(f'| {s["id"].upper()} | {s["type"].replace("_", " ")} | {"yes" if s["required"] else "optional"} | {s["job"]} | {s["guide"]} |')
    L += ['', '## Adaptation notes', '', t['adaptation'], '', '## Watch-outs', '', t['watch_outs'], '',
          '_Generated from `templates/INDEX.json` by `scripts/lp-validate-templates.py --write-cards`. Edit the JSON, not this file._', '']
    return '\n'.join(L)


def main():
    lib = json.load(open(os.path.join(SKILL, 'templates', 'INDEX.json')))
    shots, fails, seen = shots_dir(), [], set()
    for t in lib['templates']:
        tid = t.get('id', '?')
        if tid in seen:
            fails.append(f'{tid}: duplicate id')
        seen.add(tid)
        for k in ('name', 'slug', 'use_when', 'teep', 'requires', 'story', 'refs', 'sections', 'adaptation', 'watch_outs'):
            if not t.get(k):
                fails.append(f'{tid}: missing {k}')
        secs = t.get('sections') or []
        if len(secs) < 4:
            fails.append(f'{tid}: fewer than 4 sections')
        ids = [s.get('id') for s in secs]
        if len(set(ids)) != len(ids) or ids != sorted(ids):
            fails.append(f'{tid}: section ids must be unique and in order')
        for s in secs:
            for k in ('id', 'type', 'job', 'guide'):
                if not s.get(k):
                    fails.append(f'{tid} {s.get("id")}: missing {k}')
            if 'required' not in s:
                fails.append(f'{tid} {s.get("id")}: missing required')
            if s.get('type') not in TYPES:
                fails.append(f'{tid} {s.get("id")}: unknown section type {s.get("type")!r}')
        for r in t.get('refs') or []:
            if not shots or not os.path.exists(os.path.join(shots, r['slug'] + '.jpg')):
                fails.append(f'{tid}: reference screenshot {r["slug"]}.jpg not found in the swipe file')
        for k in ('story', 'adaptation', 'watch_outs', 'use_when'):
            if PRIVATE.search(t.get(k, '')):
                fails.append(f'{tid}: {k} carries a client performance number; keep those in the swipe file\'s private tables')
    if fails:
        print('\n'.join(fails))
        sys.exit(f'{len(fails)} failures')
    if '--write-cards' in sys.argv:
        for t in lib['templates']:
            open(os.path.join(SKILL, 'templates', f'{t["id"]}-{t["slug"]}.md'), 'w').write(card(t))
        print(f'wrote {len(lib["templates"])} cards')
    print(f'library ok: {len(lib["templates"])} templates, {sum(len(t["sections"]) for t in lib["templates"])} sections')


if __name__ == '__main__':
    main()

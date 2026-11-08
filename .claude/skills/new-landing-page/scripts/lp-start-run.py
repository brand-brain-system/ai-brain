#!/usr/bin/env python3
"""Start a landing-page run from the template the reviewer picked.

Usage: python3 lp-start-run.py <runs_root> --brand "Brand Name" --template lp-01 [--ref tpj-2] [--focus "magnesium sleep"]

Creates <runs_root>/<YYYY-MM-DD>-<brand-slug>-<template-slug>/ with:
  template.json   the picked template's contract, copied from templates/INDEX.json (the run reads this, so a later
                  library edit never changes a run in flight)
  page.json       a skeleton: one entry per template section, in order, with its job and guide and empty fields
  brief.json      an empty brief to fill (brief-schema.md), unless one exists
  copy/ assets/ shots/
The reviewer picks the template (from the swipe file page's "Build this one" line, or by id or name);
this script never picks one. --ref names the reference page the run follows most closely (a swipe
screenshot slug from the template's refs; default the first).
"""
import sys, os, json, re, datetime

SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def arg(name, default=None):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


BLANK = {
    'offer_bar': {'text': ''},
    'hero': {'eyebrow': '', 'headline': '', 'subhead': '', 'bullets': [], 'cta': '', 'image': {'placeholder': ''}, 'trust': []},
    'byline': {'name': '', 'title': '', 'updated': ''},
    'disclosure': {'text': ''},
    'press_bar': {'label': 'As seen in', 'names': []},
    'trust_row': {'items': []},
    'text': {'heading': '', 'paragraphs': []},
    'founder_note': {'heading': '', 'paragraphs': [], 'signoff': ''},
    'numbered_reasons': {'heading': '', 'items': [{'title': '', 'body': '', 'cta': ''}]},
    'benefits': {'heading': '', 'items': [{'title': '', 'body': ''}]},
    'comparison_table': {'heading': '', 'columns': [], 'rows': [], 'note': '', 'highlight_col': 1},
    'reviews': {'heading': '', 'items': [{'quote': '', 'name': '', 'detail': '', 'stars': 5}]},
    'timeline': {'heading': '', 'items': [{'when': '', 'what': ''}]},
    'buy_box': {'heading': '', 'product_name': '', 'image': {'placeholder': ''}, 'rating_line': '', 'options': [{'label': '', 'price': '', 'anchor': '', 'note': '', 'default': True}], 'includes': [], 'gifts': [], 'cta': '', 'guarantee': '', 'fine_print': ''},
    'value_stack': {'heading': '', 'items': [{'name': '', 'price': '', 'value': ''}], 'total_line': '', 'cta': ''},
    'faq': {'heading': 'Questions', 'items': [{'q': '', 'a': ''}]},
    'quiz': {'intro': '', 'steps': [{'question': '', 'options': []}], 'skip_label': '', 'loading_lines': [], 'result': {'headline': '', 'body': '', 'bullets': [], 'cta': ''}, 'reward': ''},
    'game': {'headline': '', 'subhead': '', 'cards': 6, 'prizes': [], 'cta': ''},
    'rounds': {'heading': '', 'items': [{'title': '', 'body': '', 'winner': '', 'cta': ''}]},
    'verdict': {'heading': '', 'points': [], 'cta': ''},
    'guarantee': {'heading': '', 'body': ''},
    'who_for': {'heading': '', 'for': [], 'not_for': []},
    'cta_block': {'heading': '', 'body': '', 'cta': ''},
    'sticky_cta': {'text': '', 'cta': ''},
    'steps': {'heading': '', 'items': [{'title': '', 'body': ''}]},
    'stat_strip': {'items': [{'number': '', 'label': ''}]},
    'product_grid': {'heading': '', 'items': [{'name': '', 'price': '', 'anchor': '', 'tag': '', 'image': {'placeholder': ''}}]},
    'image': {'image': {'placeholder': ''}, 'caption': ''},
}


def find_template(key):
    lib = json.load(open(os.path.join(SKILL, 'templates', 'INDEX.json')))
    k = key.lower().strip()
    for t in lib['templates']:
        if k in (t['id'], t['slug'], t['name'].lower()) or k.startswith(t['id'] + ' '):
            return lib, t
    sys.exit(f'no template matches {key!r}. Pick one of: ' + ', '.join(f"{t['id']} {t['name']}" for t in lib['templates']))


def main():
    if len(sys.argv) < 2 or not arg('--brand') or not arg('--template'):
        sys.exit(__doc__)
    root, brand = sys.argv[1], arg('--brand')
    lib, t = find_template(arg('--template'))
    ref = arg('--ref') or t['refs'][0]['slug']
    if ref not in [r['slug'] for r in t['refs']]:
        sys.exit(f'--ref {ref} is not one of this template\'s references: ' + ', '.join(r['slug'] for r in t['refs']))
    date = datetime.date.today().isoformat()
    name = '-'.join(x for x in [date, slug(brand), slug(arg('--focus') or ''), t['slug']] if x)
    run = os.path.join(root, name)
    for d in ('copy', 'assets', 'shots'):
        os.makedirs(os.path.join(run, d), exist_ok=True)
    tpl = dict(t, primary_ref=ref, library=lib['library'])
    json.dump(tpl, open(os.path.join(run, 'template.json'), 'w'), indent=2, ensure_ascii=False)
    page = {
        'template': t['id'], 'template_name': t['name'], 'primary_ref': ref, 'brand': brand, 'version': 0,
        'meta': {'title': '', 'cta_url': '', 'site_nav': False},
        'sections': [{'id': s['id'], 'type': s['type'], 'required': s['required'], 'job': s['job'], 'guide': s['guide'],
                      'fields': json.loads(json.dumps(BLANK[s['type']]))} for s in t['sections']],
    }
    pj = os.path.join(run, 'page.json')
    if os.path.exists(pj):
        sys.exit(f'{pj} exists; not overwriting')
    json.dump(page, open(pj, 'w'), indent=2, ensure_ascii=False)
    bj = os.path.join(run, 'brief.json')
    if not os.path.exists(bj):
        json.dump({'brand_name': brand, 'template': t['id']}, open(bj, 'w'), indent=2)
    print(f'run: {run}\ntemplate: {t["id"]} {t["name"]} (reference {ref})\nsections: ' + ', '.join(f"{s['id']} {s['type']}{'' if s['required'] else ' (optional)'}" for s in t['sections']))


if __name__ == '__main__':
    main()

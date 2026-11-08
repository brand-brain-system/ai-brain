#!/usr/bin/env python3
"""Copy tools for a landing-page run: collect, check, table.

Usage:
  python3 lp-copy.py collect <run>   write <run>/copy/all-copy.md, one line per piece of copy: "#S03 headline: line"
                                     (what the claims check, both review gates and the reviewer read)
  python3 lp-copy.py check <run>     the claims and structure check. Fails (exit 1) on:
                                       - a number ($, %, counts, day windows) not in brief.json claims.allowlist
                                       - a review quote that is not verbatim in brief.json claims.reviews
                                       - a kill-list pattern (em dash, "that's not X, it's Y", "no X, no Y, just Z")
                                       - a required template section that is missing or empty, or sections out of template order
                                     Reports open placeholders ([OFFER], [STAT NEEDED], [PHOTO ...]) and fields left empty,
                                     and customer-voice coverage: the share of key lines traced to a voc.bank phrase.
  python3 lp-copy.py table <run>     write <run>/copy/approval-table.md: the one-row-per-section table posted in chat
                                     (Section | What this section does on the reference page | Proposed copy)

Run collect, then check, until check passes; then the gates; then table.
"""
import sys, os, re, json

NUM = re.compile(r"(\$\s?\d[\d,]*(?:\.\d+)?|\d[\d,]*(?:\.\d+)?\s?%|\b\d[\d,]*(?:\.\d+)?\+?\s?(?:k\+?\s)?(?:reviews?|customers?|members?|people|women|men|nights?|days?|weeks?|months?|years?|ingredients?|stars?|servings?|calories|mg|g|countries|studies|doctors)\b|\b\d+[\s-]?(?:day|night|week|month|year)s?\b|\b\d(?:\.\d)?\s?(?:/|out of)\s?5\b)", re.I)
PH = re.compile(r"\[(?:OFFER|STAT NEEDED|PHOTO|CODE|DATE|PRICE)[^\]]*\]")
KILL = {
    'em dash': re.compile(r'—'),
    'negate then restate': re.compile(r"(?:that'?s|it'?s|this is|this isn'?t) not [^.]{1,40}[.,;] (?:that'?s|it'?s|this is)", re.I),
    'no X no Y just Z': re.compile(r"\bno [^,.]{1,20}, no [^,.]{1,20}[,.]? just\b", re.I),
}
KEY_TYPES = ('hero', 'numbered_reasons', 'faq', 'benefits', 'who_for', 'quiz', 'rounds', 'angle_benefits')
KEY_FIELD = re.compile(r'(^|\.)(headline|subhead|bullets\[\d+\]|title|lead|q)$|items\[\d+\]\.(title|lead|q)$|^bullets\[\d+\]$')
TEXT_KEYS = ('text', 'eyebrow', 'headline', 'subhead', 'cta', 'name', 'title', 'updated', 'label', 'heading', 'signoff', 'body',
             'note', 'quote', 'detail', 'when', 'what', 'product_name', 'rating_line', 'price', 'anchor', 'guarantee', 'fine_print',
             'value', 'total_line', 'q', 'a', 'intro', 'question', 'skip_label', 'reward', 'winner', 'number', 'tag', 'caption', 'placeholder')


def load(run):
    page = json.load(open(os.path.join(run, 'page.json')))
    brief = json.load(open(os.path.join(run, 'brief.json')))
    tpl_p = os.path.join(run, 'template.json')
    tpl = json.load(open(tpl_p)) if os.path.exists(tpl_p) else None
    return page, brief, tpl


def walk(obj, path=''):
    """Yield (field_path, text) for every string in a section's fields."""
    if isinstance(obj, str):
        if obj.strip():
            yield path, obj
    elif isinstance(obj, list):
        for i, v in enumerate(obj, 1):
            yield from walk(v, f'{path}[{i}]' if path else f'[{i}]')
    elif isinstance(obj, dict):
        for k, v in obj.items():
            if k in ('src', 'alt', 'default', 'stars', 'highlight_col'):  # 'cards' removed 2026-10-01: walk() only yields strings, so the game's card count is skipped by type, and copy in a 'cards' list was going unchecked
                continue
            yield from walk(v, f'{path}.{k}' if path else k)


def lines(page):
    for s in page.get('sections') or []:
        for p, t in walk(s.get('fields') or {}):
            yield s, p, t


def collect(run):
    page, _, _ = load(run)
    out = [f"# All copy: {page.get('brand', '')} {page.get('template', '')} {page.get('template_name', '')} (version {page.get('version', 0)})", '']
    for s, p, t in lines(page):
        if p.endswith('placeholder'):
            continue
        out.append(f"#{s['id'].upper()} {p}: {t}")
    os.makedirs(os.path.join(run, 'copy'), exist_ok=True)
    open(os.path.join(run, 'copy', 'all-copy.md'), 'w').write('\n'.join(out) + '\n')
    print(f"wrote {os.path.join(run, 'copy', 'all-copy.md')} ({len(out) - 2} lines)")


def norm(s):
    return re.sub(r'\s+', ' ', str(s).replace(',', '')).strip().lower()


def check(run):
    page, brief, tpl = load(run)
    claims = brief.get('claims') or {}
    allow = [norm(a) for a in (claims.get('allowlist') or [])]
    quotes = [norm(r.get('quote', '')) for r in (claims.get('reviews') or []) if isinstance(r, dict)]
    fails, notes = [], []
    for s, p, t in lines(page):
        where = f"#{s['id'].upper()} {p}"
        bare = PH.sub('', t)
        if not p.endswith('placeholder'):
            for m in NUM.finditer(bare):
                tok = norm(m.group(0))
                if not any(tok in a or a in tok for a in allow):
                    fails.append(f'{where}: number not in allowlist: {m.group(0)!r}')
            for name, rx in KILL.items():
                if rx.search(bare):
                    fails.append(f'{where}: kill list: {name}')
        if s['type'] == 'reviews' and p.endswith('.quote'):
            if norm(t) not in quotes:
                fails.append(f'{where}: review quote is not verbatim in brief.json claims.reviews')
        for m in PH.finditer(t):
            notes.append(f'{where}: open placeholder {m.group(0)}')
    # structure against the template
    if tpl:
        order = [x['id'] for x in tpl['sections']]
        ids = [s['id'] for s in page.get('sections') or []]
        known = [i for i in ids if i in order]
        if known != sorted(known, key=order.index):
            fails.append('sections are out of template order: ' + ', '.join(ids))
        for x in tpl['sections']:
            sec = next((s for s in page.get('sections') or [] if s['id'] == x['id']), None)
            has = sec and any(True for _, t in walk(sec.get('fields') or {}) if t.strip())
            if x['required'] and not has:
                fails.append(f"#{x['id'].upper()} {x['type']}: required section is missing or empty")
            if sec and sec['type'] != x['type']:
                fails.append(f"#{x['id'].upper()}: type {sec['type']} does not match the template's {x['type']}")
    for s in page.get('sections') or []:
        for k, v in (s.get('fields') or {}).items():
            if isinstance(v, str) and not v.strip() and k in ('headline', 'heading', 'text', 'cta') and s.get('required', True):
                notes.append(f"#{s['id'].upper()} {k}: empty")
    # customer-voice coverage (Alex, 2026-10-01): key lines should be built from voc.bank phrases, traced in section 'voc'
    bank = [norm(b.get('phrase', '')) for b in ((brief.get('voc') or {}).get('bank') or []) if isinstance(b, dict)]
    if not bank:
        notes.append('customer voice: brief.json voc.bank is empty; pull reviews, ad comments, survey, Reddit and TikTok first (intake-brief.md step 3)')
    key, traced = 0, 0
    for s in page.get('sections') or []:
        if s['type'] not in KEY_TYPES:
            continue
        tr = {v.get('line'): v for v in (s.get('voc') or []) if isinstance(v, dict)}
        for p, t in walk(s.get('fields') or {}):
            if p.endswith('placeholder') or not KEY_FIELD.search(p):
                continue
            key += 1
            v = tr.get(p)
            if v and v.get('from'):
                traced += 1
                if bank and norm(v['from']) not in bank:
                    notes.append(f"#{s['id'].upper()} {p}: voc trace phrase is not in brief.json voc.bank")
    if key:
        notes.append(f'customer voice: {traced} of {key} key lines traced to a customer phrase ({round(100 * traced / key)}%)')
    if not ((page.get('meta') or {}).get('cta_url') or brief.get('cta_url') or brief.get('landing_url')):
        notes.append('no cta_url: every button will point to "#"')
    for n in notes:
        print('note:', n)
    if fails:
        for f in fails:
            print('FAIL:', f)
        print(f'{len(fails)} failures')
        sys.exit(1)
    print(f'check passed: numbers on the allowlist, quotes verbatim, no kill-list pattern, template structure intact ({len(notes)} notes)')


def summary(fields):
    parts = []
    for p, t in walk(fields):
        if p.endswith('placeholder'):
            parts.append(f'[photo: {t}]')
        else:
            parts.append(t)
    return ' / '.join(parts).replace('|', '\\|')


def table(run):
    page, brief, tpl = load(run)
    ref = None
    if tpl:
        ref = next((r for r in tpl['refs'] if r['slug'] == tpl.get('primary_ref')), tpl['refs'][0])
    head = [f"**{brief.get('brand_name', page.get('brand', ''))}: {page.get('template')} {page.get('template_name', '')}**" +
            (f" (reference: {ref['brand']}, {ref['url']})" if ref else ''), '',
            '| # | Section | What this section does on the reference page | Proposed copy | Customer words behind it |', '|---|---|---|---|---|']
    rows = []
    for s in page.get('sections') or []:
        body = summary(s.get('fields') or {})
        if not body:
            continue
        vo = ' / '.join(f'"{v["from"]}" ({v.get("source", "")})' for v in (s.get('voc') or []) if isinstance(v, dict) and v.get('from')).replace('|', '/') or '-'
        rows.append(f"| {s['id'].upper()} | {s['type'].replace('_', ' ')} | {s.get('job', '').replace('|', '/')} | {body} | {vo} |")
    out = '\n'.join(head + rows) + '\n'
    open(os.path.join(run, 'copy', 'approval-table.md'), 'w').write(out)
    print(out)


if __name__ == '__main__':
    if len(sys.argv) < 3 or sys.argv[1] not in ('collect', 'check', 'table'):
        sys.exit(__doc__)
    {'collect': collect, 'check': check, 'table': table}[sys.argv[1]](sys.argv[2])

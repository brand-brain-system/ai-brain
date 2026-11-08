#!/usr/bin/env python3
"""Build the angle gap matrix: which angles, personas and awareness levels the account has tried.

    python3 gap_matrix.py [--angles angle-bank/angles.csv] [--tags angle-bank/ad-tags.csv]
                          [--out-dir angle-bank] [--date YYYY-MM-DD] [--min-spend 0]

Reads the two angle-bank files (columns in brain-system/.claude/skills/angle-bank/SKILL.md) and writes
  gap-matrix-YYYY-MM-DD.md    the tables, the gaps ranked by evidence, the warnings
  gap-matrix-YYYY-MM-DD.html  the same as a self-contained heatmap (no external files, light and dark)

Three tables:
  1. angles x awareness (UN PA SA PR MA): ads, winners and spend per cell
  2. personas x awareness
  3. share of winner spend by angle, flagged when the top 3 angles hold 80 % or more
Cell states: won (a winner in the cell), live (ads, no winner yet, one launched in the last
--young-days days), lost (ads, no winner, all older), never tried (no ads). An empty cell on an
angle with --high-evidence or more different people behind it is marked as a gap worth a look.

Several values in one field are joined by "+" (awareness "PA+SA"). An ad with two values counts in
both cells; in the share table its spend is split evenly so the shares add up to 100 %.
Ad ids in ad-tags.csv whose angle is not in angles.csv are reported, never dropped silently.
Standard library only.
"""
import argparse
import csv
import datetime as dt
import html
import re
import sys
from collections import defaultdict
from pathlib import Path

LEVELS = ["UN", "PA", "SA", "PR", "MA"]
LEVEL_NAMES = {"UN": "unaware", "PA": "problem aware", "SA": "solution aware",
               "PR": "product aware", "MA": "most aware"}
ANGLE_COLUMNS = ["angle_id", "angle", "persona_ids", "awareness", "evidence_people", "status"]
TAG_COLUMNS = ["ad_id", "spend", "is_winner", "angle_id", "persona_id", "awareness"]
OPTIONAL_TAG_COLUMNS = ["ad_name", "launch_date", "format", "voice", "shape"]
YES = {"yes", "y", "true", "1", "ja", "won", "winner"}
UNKNOWN = {"", "x", "-", "none", "n/a"}
CONCENTRATION = 0.80


class InputError(Exception):
    pass


def split_values(value):
    return [v.strip() for v in (value or "").split("+") if v.strip() and v.strip().lower() not in UNKNOWN]


def natural_key(value):
    match = re.match(r"([A-Za-z]*)(\d*)(.*)", value)
    prefix, number, rest = match.groups()
    return (prefix.upper(), int(number) if number else -1, rest)


def parse_number(raw):
    """Read 1234.5, 1,234.50, 1.234,50 and 1234,5 as numbers. Returns None when it can't."""
    text = re.sub(r"[^0-9,.\-]", "", raw or "")
    if not text or text in {"-", ".", ","}:
        return None
    if "," in text and "." in text:
        if text.rfind(",") > text.rfind("."):
            text = text.replace(".", "").replace(",", ".")
        else:
            text = text.replace(",", "")
    elif "," in text:
        tail = text.rpartition(",")[2]
        text = text.replace(",", ".") if text.count(",") == 1 and len(tail) <= 2 else text.replace(",", "")
    elif text.count(".") > 1:
        text = text.replace(".", "")
    try:
        return float(text)
    except ValueError:
        return None


def parse_date(raw):
    try:
        return dt.date.fromisoformat((raw or "").strip()[:10])
    except ValueError:
        return None


def read_csv(path, required, what):
    if not path.is_file():
        raise InputError(f"{what}: file not found: {path}")
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fields = [c.strip() for c in (reader.fieldnames or [])]
        if not fields:
            raise InputError(f"{what}: {path} is empty. It needs at least the header row: {','.join(required)}")
        missing = [c for c in required if c not in fields]
        if missing:
            raise InputError(f"{what}: {path} is missing columns: {', '.join(missing)}")
        rows = []
        for row in reader:
            clean = {(k or "").strip(): (v or "").strip() for k, v in row.items() if k is not None}
            if any(clean.values()):
                rows.append(clean)
        return rows


def fmt_money(value):
    return f"{value:,.0f}"


def n_ads(n):
    return f"{n} ad" if n == 1 else f"{n} ads"


def new_cell():
    return {"ads": 0, "winners": 0, "spend": 0.0, "young": False}


def build(angles_rows, tag_rows, today, min_spend, young_days, high_evidence):
    warnings = []
    angles = {}
    for row in angles_rows:
        aid = row["angle_id"]
        if not aid or aid.lower() in UNKNOWN:
            warnings.append(f"angles.csv: a row has no angle_id ({row.get('angle', '')[:60]!r}); skipped")
            continue
        if aid in angles:
            warnings.append(f"angles.csv: {aid} appears twice; the first row is used. Merge them (build-bank)")
            continue
        people = parse_number(row.get("evidence_people", ""))
        levels = [v.upper() for v in split_values(row.get("awareness", ""))]
        bad = [v for v in levels if v not in LEVELS]
        if bad:
            warnings.append(f"angles.csv: {aid} has unknown awareness {'+'.join(bad)}; use {' '.join(LEVELS)}")
        angles[aid] = {"id": aid, "angle": row.get("angle", ""), "personas": split_values(row.get("persona_ids", "")),
                       "levels": [v for v in levels if v in LEVELS], "people": int(people or 0),
                       "status": (row.get("status", "") or "").lower()}

    angle_cells = defaultdict(new_cell)
    persona_cells = defaultdict(new_cell)
    winner_spend = {"angle": defaultdict(float), "persona": defaultdict(float), "awareness": defaultdict(float),
                    "format": defaultdict(float), "voice": defaultdict(float), "shape": defaultdict(float)}
    unknown_angles = defaultdict(lambda: {"ads": 0, "spend": 0.0, "winners": 0})
    counts = {"rows": len(tag_rows), "below_floor": 0, "used": 0, "winners": 0, "no_angle": 0,
              "no_persona": 0, "no_awareness": 0, "spend": 0.0, "winner_spend": 0.0}
    personas_seen = set()
    for a in angles.values():
        personas_seen.update(a["personas"])

    for row in tag_rows:
        ad = row.get("ad_id") or row.get("ad_name") or "?"
        spend = parse_number(row.get("spend", ""))
        if spend is None:
            if row.get("spend", ""):
                warnings.append(f"ad-tags.csv: ad {ad} has a spend that isn't a number ({row['spend']!r}); read as 0")
            spend = 0.0
        if spend < min_spend:
            counts["below_floor"] += 1
            continue
        counts["used"] += 1
        counts["spend"] += spend
        winner = row.get("is_winner", "").lower() in YES
        launched = parse_date(row.get("launch_date", ""))
        young = bool(launched and 0 <= (today - launched).days <= young_days)
        ad_angles = split_values(row.get("angle_id", ""))
        ad_personas = split_values(row.get("persona_id", ""))
        raw_levels = [v.upper() for v in split_values(row.get("awareness", ""))]
        bad = [v for v in raw_levels if v not in LEVELS]
        if bad:
            warnings.append(f"ad-tags.csv: ad {ad} has unknown awareness {'+'.join(bad)}; left out of the matrix")
        ad_levels = [v for v in raw_levels if v in LEVELS]
        if not ad_angles:
            counts["no_angle"] += 1
        if not ad_personas:
            counts["no_persona"] += 1
        if not ad_levels:
            counts["no_awareness"] += 1
        personas_seen.update(ad_personas)
        if winner:
            counts["winners"] += 1
            counts["winner_spend"] += spend

        for aid in ad_angles:
            if aid not in angles:
                u = unknown_angles[aid]
                u["ads"] += 1
                u["spend"] += spend
                u["winners"] += int(winner)
        for keys, cells in ((ad_angles, angle_cells), (ad_personas, persona_cells)):
            for key in keys:
                for level in ad_levels:
                    cell = cells[(key, level)]
                    cell["ads"] += 1
                    cell["winners"] += int(winner)
                    cell["spend"] += spend
                    cell["young"] = cell["young"] or young

        if winner:
            for field, values in (("angle", ad_angles), ("persona", ad_personas), ("awareness", ad_levels)):
                values = values or ["x"]
                for v in values:
                    winner_spend[field][v] += spend / len(values)
            for field in ("format", "voice", "shape"):
                values = split_values(row.get(field, "")) or ["x"]
                for v in values:
                    winner_spend[field][v] += spend / len(values)

    for aid, u in sorted(unknown_angles.items(), key=lambda kv: natural_key(kv[0])):
        warnings.append(f"ad-tags.csv: angle {aid} is not in angles.csv ({n_ads(u['ads'])}, {u['winners']} winners, "
                        f"spend {fmt_money(u['spend'])}). Add it to the bank or fix the tag")

    angle_rows = sorted(angles, key=natural_key) + sorted(unknown_angles, key=natural_key)
    personas = sorted(personas_seen, key=natural_key)

    def state(cell):
        if not cell or not cell["ads"]:
            return "never"
        if cell["winners"]:
            return "won"
        return "live" if cell["young"] else "lost"

    gaps = []
    for aid in sorted(angles, key=natural_key):
        a = angles[aid]
        if a["status"] == "retired":
            continue
        fits = a["levels"] or LEVELS
        won_at = [lv for lv in LEVELS if state(angle_cells.get((aid, lv))) == "won"]
        for level in fits:
            if state(angle_cells.get((aid, level))) == "never":
                gaps.append({"angle": aid, "level": level, "people": a["people"], "won_at": won_at,
                             "personas": a["personas"], "high": a["people"] >= high_evidence})
    gaps.sort(key=lambda g: (-g["people"], -len(g["won_at"]), natural_key(g["angle"]), LEVELS.index(g["level"])))

    high_persona = set()
    for g in gaps:
        if g["high"]:
            for p in g["personas"]:
                if state(persona_cells.get((p, g["level"]))) == "never":
                    high_persona.add((p, g["level"]))

    def shares(field):
        total = sum(winner_spend[field].values())
        items = sorted(winner_spend[field].items(), key=lambda kv: (-kv[1], natural_key(kv[0])))
        return [(k, v, v / total if total else 0.0) for k, v in items], total

    angle_share, total = shares("angle")
    named = [s for s in angle_share if s[0] != "x"]
    top3 = sum(s[2] for s in named[:3])
    concentrated = bool(named) and top3 >= CONCENTRATION

    return {"angles": angles, "angle_rows": angle_rows, "unknown": dict(unknown_angles), "personas": personas,
            "angle_cells": angle_cells, "persona_cells": persona_cells, "state": state, "gaps": gaps,
            "high_persona": high_persona, "shares": {f: shares(f) for f in winner_spend},
            "top3": top3, "concentrated": concentrated, "counts": counts, "warnings": warnings,
            "high_evidence": high_evidence}


def cell_text(cell, st):
    if st == "never":
        return ""
    return f"{n_ads(cell['ads'])}, {cell['winners']} won, {fmt_money(cell['spend'])}"


STATE_WORD = {"won": "WON", "live": "live", "lost": "lost", "never": "-"}


def render_md(r, day, args):
    c = r["counts"]
    out = [f"# Gap matrix {day}", "",
           f"Inputs: `{args.angles.as_posix()}` ({len(r['angles'])} angles), `{args.tags.as_posix()}` "
           f"({c['rows']} ads, {c['used']} at or above the spend floor of {fmt_money(args.min_spend)}). "
           f"{c['winners']} winners by the brand's winner definition, winner spend {fmt_money(c['winner_spend'])} "
           f"of {fmt_money(c['spend'])}.", "",
           "**Limit:** counts and spend come from the ad-tags file, so the matrix is only as good as the tags "
           "(see the `tag_source` and `label` columns). An ad with two awareness levels or personas counts in "
           "each cell. Empty means never tried in this window, not never tried at all.", ""]
    if r["warnings"]:
        out += ["## Warnings", ""] + [f"- {w}" for w in r["warnings"]] + [""]
    if c["no_angle"] or c["no_persona"] or c["no_awareness"]:
        out += [f"Untagged above the floor: {c['no_angle']} ads with no angle, {c['no_persona']} with no persona, "
                f"{c['no_awareness']} with no awareness level. They are left out of the tables below.", ""]

    out += ["## 1. Angles x awareness", "",
            "Cell: state, then ads, winners and spend. `GAP` = never tried at a level the angle fits, "
            f"with {r['high_evidence']} or more different people behind the angle.", "",
            "| Angle | People | Status | " + " | ".join(LEVELS) + " |",
            "|---|---|---|" + "---|" * len(LEVELS)]
    gap_cells = {(g["angle"], g["level"]) for g in r["gaps"] if g["high"]}
    for aid in r["angle_rows"]:
        a = r["angles"].get(aid)
        label = f"{aid} {a['angle']}" if a else f"{aid} (not in angles.csv)"
        cells = []
        for lv in LEVELS:
            cell = r["angle_cells"].get((aid, lv))
            st = r["state"](cell)
            if st == "never":
                cells.append("GAP" if (aid, lv) in gap_cells else "-")
            else:
                cells.append(f"{STATE_WORD[st]} {cell_text(cell, st)}")
        out.append(f"| {md(label)} | {a['people'] if a else ''} | {a['status'] if a else ''} | "
                   + " | ".join(cells) + " |")
    out.append("")

    out += ["## 2. Personas x awareness", "",
            "`GAP` = never tried, and a high-evidence angle for this persona fits this level.", "",
            "| Persona | " + " | ".join(LEVELS) + " |", "|---|" + "---|" * len(LEVELS)]
    for p in r["personas"]:
        cells = []
        for lv in LEVELS:
            cell = r["persona_cells"].get((p, lv))
            st = r["state"](cell)
            if st == "never":
                cells.append("GAP" if (p, lv) in r["high_persona"] else "-")
            else:
                cells.append(f"{STATE_WORD[st]} {cell_text(cell, st)}")
        out.append(f"| {md(p)} | " + " | ".join(cells) + " |")
    if not r["personas"]:
        out.append("| (no personas in either file) |" + " |" * len(LEVELS))
    out.append("")

    out += ["## 3. Share of winner spend", ""]
    rows, total = r["shares"]["angle"]
    if not total:
        out += ["No winner spend in the file. Check `is_winner` against the brand's winner definition "
                "(`running-notes/success-definition.md`).", ""]
    else:
        if r["concentrated"]:
            out += [f"**Concentrated:** the top 3 angles hold {r['top3']:.0%} of winner spend (flag at "
                    f"{CONCENTRATION:.0%}). The account scales on a few angles; the gaps below are where the next "
                    "level of spend can come from.", ""]
        else:
            out += [f"The top 3 angles hold {r['top3']:.0%} of winner spend (flag at {CONCENTRATION:.0%}).", ""]
        out += share_md("Angle", rows, r["angles"])
    for field, title in (("persona", "Persona"), ("awareness", "Awareness"), ("format", "Format"),
                         ("voice", "Voice"), ("shape", "Shape")):
        rows, total = r["shares"][field]
        if total:
            out += [f"### By {field}", ""] + share_md(title, rows, None)

    out += ["## Empty cells, ranked by evidence", "",
            "Mechanical rank only: different people behind the angle, then whether the angle already won at "
            "another level. The gap-matrix process adds persona size, roadmap fit and whether a cell is empty "
            "for a reason.", ""]
    if r["gaps"]:
        out += ["| # | Angle | Level | People | Personas | Won elsewhere |", "|---|---|---|---|---|---|"]
        for i, g in enumerate(r["gaps"][:15], 1):
            a = r["angles"][g["angle"]]
            out.append(f"| {i} | {md(g['angle'] + ' ' + a['angle'])} | {g['level']} | {g['people']} | "
                       f"{'+'.join(g['personas']) or 'x'} | {'+'.join(g['won_at']) or 'no'} |")
    else:
        out.append("No empty cells on the angles' own awareness levels.")
    out.append("")
    return "\n".join(out)


def md(text):
    return str(text).replace("|", "/").replace("\n", " ")


def share_md(title, rows, angles):
    out = [f"| {title} | Winner spend | Share |", "|---|---|---|"]
    for key, spend, share in rows:
        label = key
        if angles is not None:
            label = f"{key} {angles[key]['angle']}" if key in angles else (
                "x (no angle)" if key == "x" else f"{key} (not in angles.csv)")
        out.append(f"| {md(label)} | {fmt_money(spend)} | {share:.0%} |")
    return out + [""]


CSS = """
:root{--bg:#fbfaf7;--fg:#1d1f21;--muted:#5f6368;--line:#d9d6cf;--won:#cfe8d5;--won-fg:#14532d;
--live:#d6e4f5;--live-fg:#1e3a5f;--lost:#f3d9d3;--lost-fg:#7a2617;--never:#f1efea;--gap:#f6c945;--card:#ffffff}
@media (prefers-color-scheme: dark){:root{--bg:#161719;--fg:#e8e6e3;--muted:#a3a7ad;--line:#34363a;
--won:#1f4a2c;--won-fg:#c9f0d3;--live:#1d3550;--live-fg:#cfe0f5;--lost:#57261c;--lost-fg:#f7d4cb;
--never:#222326;--gap:#b8901c;--card:#1d1e21}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.45 system-ui,-apple-system,"Segoe UI",sans-serif}
main{max-width:1100px;margin:0 auto;padding:24px 16px 48px}
h1{font-size:24px;margin:0 0 4px}h2{font-size:18px;margin:32px 0 8px}
p{margin:6px 0;color:var(--fg)}.muted{color:var(--muted)}
.wrap{overflow-x:auto;border:1px solid var(--line);border-radius:8px;background:var(--card)}
table{border-collapse:collapse;width:100%;min-width:640px}
th,td{border-bottom:1px solid var(--line);padding:8px;text-align:left;vertical-align:top;font-size:13px}
th{font-weight:600;color:var(--muted)}
td.c{text-align:center;width:13%}
td.won{background:var(--won);color:var(--won-fg)}td.live{background:var(--live);color:var(--live-fg)}
td.lost{background:var(--lost);color:var(--lost-fg)}td.never{background:var(--never);color:var(--muted)}
td.gap{background:var(--never);box-shadow:inset 0 0 0 3px var(--gap);color:var(--fg);font-weight:600}
.s{display:block;font-weight:600}.n{display:block;font-size:12px}
.legend span{display:inline-block;margin:4px 12px 4px 0;font-size:13px}
.legend i{display:inline-block;width:14px;height:14px;border-radius:3px;vertical-align:-2px;margin-right:4px}
.flag{border-left:4px solid var(--gap);padding:8px 12px;background:var(--card);margin:8px 0}
.bar{height:10px;background:var(--won-fg);border-radius:2px;opacity:.7}
ul{padding-left:20px}
"""


def render_html(r, day, args):
    e = html.escape
    c = r["counts"]
    gap_cells = {(g["angle"], g["level"]) for g in r["gaps"] if g["high"]}

    def td(cell, st, is_gap, title):
        if st == "never":
            cls = "gap" if is_gap else "never"
            text = "gap" if is_gap else "never tried"
            return f'<td class="c {cls}" title="{e(title)}"><span class="s">{text}</span></td>'
        return (f'<td class="c {st}" title="{e(title)}"><span class="s">{st}</span>'
                f'<span class="n">{n_ads(cell["ads"])}, {cell["winners"]} won</span>'
                f'<span class="n">{fmt_money(cell["spend"])}</span></td>')

    head = "".join(f'<th title="{LEVEL_NAMES[lv]}">{lv}</th>' for lv in LEVELS)
    rows = []
    for aid in r["angle_rows"]:
        a = r["angles"].get(aid)
        label = (f"<b>{e(aid)}</b> {e(a['angle'])}<br><span class='muted'>{a['people']} people, "
                 f"{e(a['status'] or 'no status')}</span>") if a else f"<b>{e(aid)}</b> <span class='muted'>not in angles.csv</span>"
        cells = "".join(td(r["angle_cells"].get((aid, lv)), r["state"](r["angle_cells"].get((aid, lv))),
                           (aid, lv) in gap_cells, f"{aid} at {LEVEL_NAMES[lv]}") for lv in LEVELS)
        rows.append(f"<tr><td>{label}</td>{cells}</tr>")
    angle_table = f"<table><tr><th>Angle</th>{head}</tr>{''.join(rows)}</table>"

    rows = []
    for p in r["personas"]:
        cells = "".join(td(r["persona_cells"].get((p, lv)), r["state"](r["persona_cells"].get((p, lv))),
                           (p, lv) in r["high_persona"], f"{p} at {LEVEL_NAMES[lv]}") for lv in LEVELS)
        rows.append(f"<tr><td><b>{e(p)}</b></td>{cells}</tr>")
    persona_table = (f"<table><tr><th>Persona</th>{head}</tr>{''.join(rows)}</table>" if rows
                     else "<p class='muted'>No personas in either file.</p>")

    share_rows, total = r["shares"]["angle"]
    if total:
        body = []
        for key, spend, share in share_rows:
            a = r["angles"].get(key)
            label = (f"<b>{e(key)}</b> {e(a['angle'])}" if a else
                     ("x (no angle)" if key == "x" else f"<b>{e(key)}</b> not in angles.csv"))
            body.append(f"<tr><td>{label}</td><td>{fmt_money(spend)}</td><td>{share:.0%}</td>"
                        f"<td style='width:30%'><div class='bar' style='width:{share * 100:.1f}%'></div></td></tr>")
        flag = (f"<div class='flag'><b>Concentrated:</b> the top 3 angles hold {r['top3']:.0%} of winner spend "
                f"(flag at {CONCENTRATION:.0%}). The gaps are where the next level of spend can come from.</div>"
                if r["concentrated"] else
                f"<p>The top 3 angles hold {r['top3']:.0%} of winner spend (flag at {CONCENTRATION:.0%}).</p>")
        share_table = (flag + "<div class='wrap'><table><tr><th>Angle</th><th>Winner spend</th><th>Share</th><th></th></tr>"
                       + "".join(body) + "</table></div>")
    else:
        share_table = ("<p>No winner spend in the file. Check <code>is_winner</code> against the brand's winner "
                       "definition.</p>")

    gap_items = []
    for g in r["gaps"][:10]:
        a = r["angles"][g["angle"]]
        won = f", already won at {'+'.join(g['won_at'])}" if g["won_at"] else ""
        gap_items.append(f"<li><b>{e(g['angle'])} at {g['level']}</b> {e(a['angle'])} "
                         f"<span class='muted'>({g['people']} people{won})</span></li>")
    gaps = f"<ul>{''.join(gap_items)}</ul>" if gap_items else "<p class='muted'>No empty cells on the angles' own levels.</p>"
    warn = ("<h2>Warnings</h2><ul>" + "".join(f"<li>{e(w)}</li>" for w in r["warnings"]) + "</ul>") if r["warnings"] else ""

    legend = ("<p class='legend'><span><i style='background:var(--won)'></i>won</span>"
              "<span><i style='background:var(--live)'></i>live, no winner yet</span>"
              "<span><i style='background:var(--lost)'></i>tried and lost</span>"
              "<span><i style='background:var(--never)'></i>never tried</span>"
              f"<span><i style='background:var(--never);box-shadow:inset 0 0 0 3px var(--gap)'></i>gap: never tried, "
              f"{r['high_evidence']}+ people behind the angle</span></p>")
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Gap matrix {day}</title><style>{CSS}</style></head>
<body><main>
<h1>Gap matrix {day}</h1>
<p class="muted">{len(r['angles'])} angles. {c['used']} of {c['rows']} ads at or above the spend floor of
{fmt_money(args.min_spend)}. {c['winners']} winners, winner spend {fmt_money(c['winner_spend'])} of {fmt_money(c['spend'])}.</p>
<p class="muted">Limit: the matrix is only as good as the tags. An ad with two levels or personas counts in each cell.
Empty means never tried in this window.</p>
{legend}
<h2>Angles x awareness</h2><div class="wrap">{angle_table}</div>
<h2>Personas x awareness</h2><div class="wrap">{persona_table}</div>
<h2>Share of winner spend by angle</h2>{share_table}
<h2>Empty cells with the most evidence</h2>{gaps}
{warn}
</main></body></html>
"""


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--angles", type=Path, default=Path("angle-bank/angles.csv"))
    parser.add_argument("--tags", type=Path, default=Path("angle-bank/ad-tags.csv"))
    parser.add_argument("--out-dir", type=Path, help="where to write (default: the folder of --angles)")
    parser.add_argument("--date", help="date in the file names, YYYY-MM-DD (default: today)")
    parser.add_argument("--min-spend", type=float, default=0.0, help="leave out ads that spent less (default 0)")
    parser.add_argument("--young-days", type=int, default=14,
                        help="an ad launched this many days before --date or fewer is still live, not lost (default 14)")
    parser.add_argument("--high-evidence", type=int, default=5,
                        help="evidence_people at or above this marks an empty cell as a gap (default 5)")
    args = parser.parse_args(argv)
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

    day = dt.date.today() if not args.date else parse_date(args.date)
    if day is None or (args.date and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.date)):
        print(f"error: --date must be YYYY-MM-DD, got {args.date!r}", file=sys.stderr)
        return 2
    try:
        angles_rows = read_csv(args.angles, ANGLE_COLUMNS, "angles")
        tag_rows = read_csv(args.tags, TAG_COLUMNS, "ad tags")
    except InputError as err:
        print(f"error: {err}", file=sys.stderr)
        return 2

    result = build(angles_rows, tag_rows, day, args.min_spend, args.young_days, args.high_evidence)
    out_dir = args.out_dir or args.angles.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = f"gap-matrix-{day.isoformat()}"
    md_path, html_path = out_dir / f"{stem}.md", out_dir / f"{stem}.html"
    md_path.write_text(render_md(result, day.isoformat(), args), encoding="utf-8", newline="\n")
    html_path.write_text(render_html(result, day.isoformat(), args), encoding="utf-8", newline="\n")

    for w in result["warnings"]:
        print(f"! {w}")
    c = result["counts"]
    print(f"{len(result['angles'])} angles, {c['used']} ads used ({c['below_floor']} below the spend floor), "
          f"{c['winners']} winners")
    print(f"top 3 angles hold {result['top3']:.0%} of winner spend"
          + (" (concentrated)" if result["concentrated"] else ""))
    high = [g for g in result["gaps"] if g["high"]]
    print(f"{len(result['gaps'])} empty cells on the angles' own levels, {len(high)} with high evidence")
    print(f"wrote {md_path}")
    print(f"wrote {html_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

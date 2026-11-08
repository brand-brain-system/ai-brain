#!/usr/bin/env python3
"""Rank a brand's ads by the creative tags in their names: the weekly creative leaderboard.

    python3 leaderboard.py source-pulls/ad-account-2026-11-07-7d.csv \
        --long source-pulls/ad-account-2026-11-07-28d.csv \
        --min-spend 300 --winner-cpa-max 250 --winner-min-spend 1000 \
        --angles angle-bank/angles.csv --write-tags angle-bank/ad-tags.csv

Input: an ad-level export (Ads Manager CSV in English or Danish, or the read-only Meta Ads MCP
pull saved as CSV with snake_case columns). Column names are matched loosely, a currency suffix
like "(DKK)" is fine, and --colmap fixes anything the matcher misses. Rows for the same ad (one
per day or per ad set) are added up.

Each ad name is parsed with the convention (brain-system/system/ad-naming-convention.md) or with
the brand's own field map (--naming-map running-notes/ad-naming.md). Names that don't parse are
listed in their own section, never dropped.

Output: audits/leaderboard/YYYY-Www.md and .html (self-contained, light and dark). The main
export is the ranking window (usually the last 7 days); --long adds a second window (usually 28
days), which is where hit rate means most.

Rules the numbers follow:
  tested   = spend >= --min-spend
  winner   = spend >= --winner-min-spend (default: --min-spend) and CPA <= --winner-cpa-max
             and/or ROAS >= --winner-roas-min (every bar given must hold). No bar, no winners.
  hit rate = winners / tested ads launched inside the window (launch date from the name, else a
             created-time column). Always printed as k/n with the percent.
The winner bar comes from the brand (running-notes/success-definition.md, brand-rules.md); the
script never makes one up. Standard library only.
"""
import argparse
import csv
import html
import json
import re
import sys
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ad_name  # noqa: E402

DIMENSIONS = [("angle_id", "Angle"), ("persona_id", "Persona"), ("awareness", "Awareness"),
              ("format", "Format"), ("voice", "Voice"), ("shape", "Shape"),
              ("concept_id", "Concept")]

# Our column -> names seen in exports, normalised (lower case, no currency suffix, no punctuation).
SYNONYMS = {
    "ad_id": ["ad id", "ad_id", "id", "annonce id", "annonce-id"],
    "ad_name": ["ad name", "ad_name", "name", "annoncenavn", "annonce navn"],
    "spend": ["amount spent", "spend", "amount_spent", "brugt beløb", "beløb brugt", "forbrug"],
    "results": ["purchases", "website purchases", "purchase", "køb", "webstedskøb", "results",
                "resultater", "conversions"],
    "value": ["purchases conversion value", "website purchases conversion value",
              "purchase conversion value", "purchase value", "purchases value", "conversion value",
              "action values purchase", "revenue", "konverteringsværdi for køb",
              "konverteringsværdi for webstedskøb", "købsværdi"],
    "date_start": ["reporting starts", "date start", "rapportering starter", "start date"],
    "date_end": ["reporting ends", "date stop", "date end", "rapportering slutter", "end date"],
    "created": ["created time", "ad created", "date created", "ad creation date", "oprettet",
                "oprettelsesdato"],
}
TAG_COLUMNS = ["ad_id", "ad_name", "launch_date", "spend", "results", "cpa", "roas", "is_winner",
               "concept_id", "angle_id", "persona_id", "awareness", "format", "voice", "shape",
               "hook_family", "enemy", "mechanism", "proof", "close", "product_at", "tag_source",
               "label"]
CURRENCY = re.compile(r"\s*[\(\[]\s*([A-Za-z]{3})\s*[\)\]]\s*$")


def norm_header(h: str) -> str:
    h = CURRENCY.sub("", (h or "").replace("﻿", "")).strip().lower()
    h = re.sub(r"[_\-:.]+", " ", h)
    return re.sub(r"\s+", " ", h).strip()


def map_columns(headers, colmap=None):
    """Return ({our column: their header}, currency or '')."""
    found, currency = {}, ""
    colmap = colmap or {}
    for ours, theirs in colmap.items():
        if theirs in headers:
            found[ours] = theirs
        else:
            sys.exit(f"--colmap: column '{theirs}' is not in the export")
    normed = {h: norm_header(h) for h in headers}
    for ours, names in SYNONYMS.items():
        if ours in found:
            continue
        wanted = [norm_header(n) for n in names]
        for name in wanted:  # synonym order is preference order
            hit = next((h for h, n in normed.items() if n == name), None)
            if hit:
                found[ours] = hit
                break
    spend_col = found.get("spend", "")
    m = CURRENCY.search(spend_col) or next((CURRENCY.search(h) for h in headers if CURRENCY.search(h)), None)
    if m:
        currency = m.group(1).upper()
    return found, currency


def to_number(raw) -> float:
    s = str(raw or "").strip().replace(" ", "").replace(" ", "")
    s = re.sub(r"[^\d,.\-]", "", s)
    if s in ("", "-", ".", ","):
        return 0.0
    if "," in s and "." in s:
        dec = "," if s.rfind(",") > s.rfind(".") else "."
        s = s.replace("." if dec == "," else ",", "").replace(",", ".")
    elif "," in s:
        parts = s.split(",")
        s = s.replace(",", "") if len(parts) > 2 or len(parts[-1]) == 3 else s.replace(",", ".")
    elif s.count(".") > 1:
        s = s.replace(".", "")
    try:
        return float(s)
    except ValueError:
        return 0.0


def to_date(raw):
    s = str(raw or "").strip()[:10]
    for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%d.%m.%Y", "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d"):
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    return None


def load_export(path: Path, colmap=None) -> dict:
    with path.open(encoding="utf-8-sig", newline="") as f:
        sample = f.read(4096)
        f.seek(0)
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")
        except csv.Error:
            dialect = csv.excel
        reader = csv.DictReader(f, dialect=dialect)
        headers = reader.fieldnames or []
        cols, currency = map_columns(headers, colmap)
        if "ad_name" not in cols:
            sys.exit(f"{path}: no ad name column found (columns: {', '.join(headers)}). Use --colmap.")
        if "spend" not in cols:
            sys.exit(f"{path}: no spend column found (columns: {', '.join(headers)}). Use --colmap.")
        ads, starts, ends, rows = {}, [], [], 0
        for row in reader:
            name = (row.get(cols["ad_name"]) or "").strip()
            ad_id = (row.get(cols["ad_id"]) or "").strip() if "ad_id" in cols else ""
            if not name and not ad_id:
                continue
            if name.lower().startswith(("total", "i alt", "results from")):
                continue  # Ads Manager summary lines
            rows += 1
            key = ad_id or name
            ad = ads.setdefault(key, {"ad_id": ad_id, "ad_name": name, "spend": 0.0, "results": 0.0,
                                      "value": 0.0, "has_value": False, "created": None})
            ad["spend"] += to_number(row.get(cols["spend"]))
            if "results" in cols:
                ad["results"] += to_number(row.get(cols["results"]))
            if "value" in cols and str(row.get(cols["value"]) or "").strip():
                ad["value"] += to_number(row.get(cols["value"]))
                ad["has_value"] = True
            if "created" in cols:
                c = to_date(row.get(cols["created"]))
                if c and (ad["created"] is None or c < ad["created"]):
                    ad["created"] = c
            for col, bucket in (("date_start", starts), ("date_end", ends)):
                if col in cols:
                    d = to_date(row.get(cols[col]))
                    if d:
                        bucket.append(d)
    return {"path": str(path), "ads": list(ads.values()), "rows": rows, "currency": currency,
            "columns": cols, "start": min(starts) if starts else None,
            "end": max(ends) if ends else (max(starts) if starts else None)}


def enrich(window: dict, fmap, rules: dict) -> dict:
    start, end = window["start"], window["end"]
    for ad in window["ads"]:
        p = ad_name.parse(ad["ad_name"], fmap)
        ad["parse"] = p
        launch = p["fields"]["launch_date"] if p["fields"]["launch_date"] != "x" else None
        launch = to_date(launch) if launch else ad["created"]
        ad["launch"] = launch
        ad["cpa"] = ad["spend"] / ad["results"] if ad["results"] else None
        ad["roas"] = ad["value"] / ad["spend"] if ad["has_value"] and ad["spend"] else None
        ad["tested"] = ad["spend"] >= rules["min_spend"] and ad["spend"] > 0
        ad["is_winner"] = winner(ad, rules)
        ad["new"] = bool(launch and start and end and start <= launch <= end) or \
            (not (start and end) and launch is not None)
    window["parsed"] = [a for a in window["ads"] if a["parse"]["ok"]]
    window["unparsed"] = [a for a in window["ads"] if not a["parse"]["ok"]]
    return window


def winner(ad, rules):
    if rules["cpa_max"] is None and rules["roas_min"] is None:
        return None
    if ad["spend"] < rules["winner_min_spend"] or ad["spend"] <= 0:
        return False
    if rules["cpa_max"] is not None and (ad["cpa"] is None or ad["cpa"] > rules["cpa_max"]):
        return False
    if rules["roas_min"] is not None and (ad["roas"] is None or ad["roas"] < rules["roas_min"]):
        return False
    return True


def summarise(ads, total_spend):
    spend = sum(a["spend"] for a in ads)
    results = sum(a["results"] for a in ads)
    has_value = any(a["has_value"] for a in ads)
    value = sum(a["value"] for a in ads)
    new_tested = [a for a in ads if a["new"] and a["tested"]]
    return {"ads": len(ads), "tested": sum(1 for a in ads if a["tested"]), "spend": spend,
            "share": spend / total_spend if total_spend else 0.0, "results": results,
            "cpa": spend / results if results else None,
            "roas": value / spend if has_value and spend else None,
            "winners": sum(1 for a in ads if a["is_winner"]),
            "new_tested": len(new_tested), "new_winners": sum(1 for a in new_tested if a["is_winner"])}


def aggregate(window):
    total = sum(a["spend"] for a in window["ads"])
    out = {}
    for field, _ in DIMENSIONS:
        groups = defaultdict(list)
        for a in window["parsed"]:
            groups[a["parse"]["fields"][field]].append(a)
        rows = [(k, summarise(v, total)) for k, v in groups.items()]
        rows.sort(key=lambda kv: (-kv[1]["spend"], kv[0]))
        out[field] = rows
    window["total"] = summarise(window["ads"], total)
    window["parsed_total"] = summarise(window["parsed"], total)
    window["dims"] = out
    return window


# ---------- formatting ----------

def money(x, cur=""):
    return "" if x is None else f"{x:,.2f}" + (f" {cur}" if cur else "")


def ratio(x):
    return "" if x is None else f"{x:,.2f}"


def pct(x):
    return f"{x * 100:.2f}%"


def num(x):
    return f"{x:,.0f}" if float(x).is_integer() else f"{x:,.2f}"


def hit(k, n):
    return "no bar" if k is None else (f"{k}/{n}" + (f" ({k / n * 100:.2f}%)" if n else ""))


def label_for(field, value, angles):
    if value == "x":
        return "x (not tagged)"
    if field == "angle_id" and value in angles:
        return f"{value}: {angles[value]}"
    return value


def load_angles(path):
    if not path or not Path(path).exists():
        return {}
    with Path(path).open(encoding="utf-8-sig", newline="") as f:
        return {(r.get("angle_id") or "").strip(): (r.get("angle") or "").strip()
                for r in csv.DictReader(f) if (r.get("angle_id") or "").strip()}


def window_label(w, default):
    if w["start"] and w["end"]:
        days = (w["end"] - w["start"]).days + 1
        return f"{w['start'].isoformat()} to {w['end'].isoformat()} ({days} days)"
    return default + " (dates not in the export)"


def dim_rows(w, field, angles, rules):
    cur = w["currency"]
    rows = []
    for value, s in w["dims"][field]:
        rows.append({"label": label_for(field, value, angles), "ads": s["ads"], "tested": s["tested"],
                     "spend": money(s["spend"], cur), "share": s["share"],
                     "results": num(s["results"]), "cpa": money(s["cpa"], cur), "roas": ratio(s["roas"]),
                     "winners": "" if not rules["has_bar"] else str(s["winners"]),
                     "hit": hit(s["new_winners"] if rules["has_bar"] else None, s["new_tested"])})
    return rows


DIM_HEAD = ["Value", "Ads", "Tested", "Spend", "Share", "Results", "CPA", "ROAS", "Winners", "Hit rate (new)"]


def top_ads(w, n):
    ads = sorted([a for a in w["ads"] if a["tested"]], key=lambda a: -a["spend"])
    return ads[:n]


def write_markdown(meta, windows, angles, rules, takeaways, n_top) -> str:
    L = [f"# Creative leaderboard, {meta['week']}", ""]
    L.append(f"Made {meta['today']} by `creative-leaderboard/scripts/leaderboard.py`. "
             f"Naming: {meta['naming']}.")
    L.append(f"- Tested floor: spend at least {money(rules['min_spend'], meta['currency'])}"
             + ("" if rules["min_spend"] else " (no floor set: every ad with spend counts as tested)"))
    L.append(f"- Winner bar: {rules['bar_text']}")
    L.append("- Hit rate (new) = winners among tested ads launched inside the window / those ads. "
             "Launch date from the name, else the export's created date")
    L.append("")
    L.append("## Takeaways")
    L.append("")
    L.append(takeaways.strip() if takeaways else
             "_Not written yet. Read the tables, then write what won by angle, persona, awareness, "
             "format, voice and shape, and what the next batch starts from._")
    L.append("")
    for key, w in windows:
        cur = w["currency"]
        t, pt = w["total"], w["parsed_total"]
        L.append(f"## {key}: {window_label(w, key)}")
        L.append("")
        L.append(f"Source: `{w['path']}`, {w['rows']} rows, {t['ads']} ads, spend {money(t['spend'], cur)}, "
                 f"results {num(t['results'])}, CPA {money(t['cpa'], cur) or 'n/a'}, ROAS {ratio(t['roas']) or 'n/a'}.")
        L.append(f"Names parsed: {pt['ads']}/{t['ads']} ads, {pct(pt['spend'] / t['spend']) if t['spend'] else '0.00%'} of spend. "
                 f"Tested: {t['tested']}. Winners: {t['winners'] if rules['has_bar'] else 'no bar'}. "
                 f"Hit rate (new): {hit(t['new_winners'] if rules['has_bar'] else None, t['new_tested'])}.")
        if w["unparsed"]:
            L.append(f"The dimension tables leave out the {len(w['unparsed'])} ads whose names don't parse "
                     "(listed at the end of this window).")
        L.append("")
        for field, title in DIMENSIONS:
            L.append(f"### By {title.lower()}")
            L.append("")
            L.append("| " + " | ".join(DIM_HEAD) + " |")
            L.append("|" + "---|" * len(DIM_HEAD))
            for r in dim_rows(w, field, angles, rules):
                L.append(f"| {r['label']} | {r['ads']} | {r['tested']} | {r['spend']} | {pct(r['share'])} | "
                         f"{r['results']} | {r['cpa']} | {r['roas']} | {r['winners']} | {r['hit']} |")
            L.append("")
        L.append(f"### Top {n_top} tested ads by spend")
        L.append("")
        L.append("| # | Ad | Spend | Results | CPA | ROAS | Winner | Angle | Persona | Awareness | Format |")
        L.append("|---|---|---|---|---|---|---|---|---|---|---|")
        for i, a in enumerate(top_ads(w, n_top), 1):
            f = a["parse"]["fields"]
            win = {True: "yes", False: "no", None: ""}[a["is_winner"]]
            L.append(f"| {i} | `{a['ad_name']}` | {money(a['spend'], cur)} | {num(a['results'])} | "
                     f"{money(a['cpa'], cur)} | {ratio(a['roas'])} | {win} | "
                     + " | ".join(f[k] if a["parse"]["ok"] else "?" for k in ("angle_id", "persona_id", "awareness", "format"))
                     + " |")
        L.append("")
        L.append(f"### Names that don't parse ({len(w['unparsed'])})")
        L.append("")
        if not w["unparsed"]:
            L.append("None.")
        else:
            L.append("| Ad | Ad ID | Spend | Why |")
            L.append("|---|---|---|---|")
            for a in sorted(w["unparsed"], key=lambda a: -a["spend"]):
                L.append(f"| `{a['ad_name']}` | {a['ad_id']} | {money(a['spend'], cur)} | "
                         f"{'; '.join(a['parse']['errors'])} |")
        L.append("")
    return "\n".join(L) + "\n"


CSS = """
:root{--bg:#fbfaf7;--fg:#1d1d1b;--muted:#6b6a65;--line:#e4e1d9;--card:#ffffff;--bar:#3f6f8f;--win:#2f7d4f;--warn:#a5552a}
@media (prefers-color-scheme: dark){:root{--bg:#161615;--fg:#ecebe6;--muted:#a3a29b;--line:#34332f;--card:#1f1f1d;--bar:#7fb1d1;--win:#7cc79a;--warn:#e19a6f}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif}
main{max-width:1100px;margin:0 auto;padding:24px 16px 64px}h1{font-size:26px;margin:0 0 4px}h2{font-size:20px;margin:36px 0 8px}
h3{font-size:16px;margin:24px 0 6px}.muted{color:var(--muted)}.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px;margin:12px 0}
.scroll{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:13px}th,td{text-align:left;padding:6px 8px;border-bottom:1px solid var(--line);vertical-align:top}
th{color:var(--muted);font-weight:600}td.n{text-align:right;white-space:nowrap}.bar{height:8px;border-radius:4px;background:var(--bar);min-width:2px}
.barcell{width:120px}.yes{color:var(--win);font-weight:600}.warn{color:var(--warn)}code{font-size:12px;word-break:break-all}
.tiles{display:flex;flex-wrap:wrap;gap:10px}.tile{flex:1 1 150px;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 12px}
.tile b{display:block;font-size:20px}
"""


def e(x):
    return html.escape(str(x if x is not None else ""))


def md_to_html(text):
    out, in_list = [], False
    for line in text.strip().splitlines():
        s = line.strip()
        if s.startswith(("- ", "* ")):
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{e(s[2:])}</li>")
            continue
        if in_list:
            out.append("</ul>")
            in_list = False
        if s.startswith("#"):
            out.append(f"<h3>{e(s.lstrip('#').strip())}</h3>")
        elif s:
            out.append(f"<p>{e(s)}</p>")
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


def write_html(meta, windows, angles, rules, takeaways, n_top) -> str:
    H = ["<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">",
         "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">",
         f"<title>Creative leaderboard {e(meta['week'])}</title><style>{CSS}</style></head><body><main>",
         f"<h1>Creative leaderboard, {e(meta['week'])}</h1>",
         f"<p class=\"muted\">Made {e(meta['today'])}. Naming: {e(meta['naming'])}. Tested floor: "
         f"{e(money(rules['min_spend'], meta['currency']))}. Winner bar: {e(rules['bar_text'])}.</p>",
         "<h2>Takeaways</h2><div class=\"card\">",
         md_to_html(takeaways) if takeaways else "<p class=\"muted\">Not written yet.</p>", "</div>"]
    for key, w in windows:
        cur = w["currency"]
        t, pt = w["total"], w["parsed_total"]
        H.append(f"<h2>{e(key)}: {e(window_label(w, key))}</h2>")
        H.append("<div class=\"tiles\">")
        tiles = [("Spend", money(t["spend"], cur)), ("Results", num(t["results"])),
                 ("CPA", money(t["cpa"], cur) or "n/a"), ("ROAS", ratio(t["roas"]) or "n/a"),
                 ("Ads tested", f"{t['tested']}/{t['ads']}"),
                 ("Hit rate (new)", hit(t["new_winners"] if rules["has_bar"] else None, t["new_tested"])),
                 ("Names parsed", f"{pt['ads']}/{t['ads']}")]
        H += [f"<div class=\"tile\"><span class=\"muted\">{e(k)}</span><b>{e(v)}</b></div>" for k, v in tiles]
        H.append("</div>")
        H.append(f"<p class=\"muted\">Source: <code>{e(w['path'])}</code>, {w['rows']} rows.</p>")
        for field, title in DIMENSIONS:
            rows = dim_rows(w, field, angles, rules)
            top = max((r["share"] for r in rows), default=0) or 1
            H.append(f"<h3>By {e(title.lower())}</h3><div class=\"scroll\"><table><tr>")
            H += [f"<th>{e(h)}</th>" for h in DIM_HEAD[:4]] + ["<th>Share</th><th></th>"]
            H += [f"<th>{e(h)}</th>" for h in DIM_HEAD[5:]] + ["</tr>"]
            for r in rows:
                H.append(f"<tr><td>{e(r['label'])}</td><td class=\"n\">{r['ads']}</td><td class=\"n\">{r['tested']}</td>"
                         f"<td class=\"n\">{e(r['spend'])}</td><td class=\"n\">{pct(r['share'])}</td>"
                         f"<td class=\"barcell\"><div class=\"bar\" style=\"width:{r['share'] / top * 100:.1f}%\"></div></td>"
                         f"<td class=\"n\">{e(r['results'])}</td><td class=\"n\">{e(r['cpa'])}</td><td class=\"n\">{e(r['roas'])}</td>"
                         f"<td class=\"n\">{e(r['winners'])}</td><td class=\"n\">{e(r['hit'])}</td></tr>")
            H.append("</table></div>")
        H.append(f"<h3>Top {n_top} tested ads by spend</h3><div class=\"scroll\"><table>"
                 "<tr><th>#</th><th>Ad</th><th>Spend</th><th>Results</th><th>CPA</th><th>ROAS</th><th>Winner</th>"
                 "<th>Angle</th><th>Persona</th><th>Awareness</th><th>Format</th></tr>")
        for i, a in enumerate(top_ads(w, n_top), 1):
            f = a["parse"]["fields"]
            win = {True: "<span class=\"yes\">yes</span>", False: "no", None: ""}[a["is_winner"]]
            tags = "".join(f"<td>{e(f[k] if a['parse']['ok'] else '?')}</td>"
                           for k in ("angle_id", "persona_id", "awareness", "format"))
            H.append(f"<tr><td>{i}</td><td><code>{e(a['ad_name'])}</code></td><td class=\"n\">{e(money(a['spend'], cur))}</td>"
                     f"<td class=\"n\">{e(num(a['results']))}</td><td class=\"n\">{e(money(a['cpa'], cur))}</td>"
                     f"<td class=\"n\">{e(ratio(a['roas']))}</td><td>{win}</td>{tags}</tr>")
        H.append("</table></div>")
        H.append(f"<h3 class=\"warn\">Names that don't parse ({len(w['unparsed'])})</h3>")
        if w["unparsed"]:
            H.append("<div class=\"scroll\"><table><tr><th>Ad</th><th>Ad ID</th><th>Spend</th><th>Why</th></tr>")
            for a in sorted(w["unparsed"], key=lambda a: -a["spend"]):
                H.append(f"<tr><td><code>{e(a['ad_name'])}</code></td><td>{e(a['ad_id'])}</td>"
                         f"<td class=\"n\">{e(money(a['spend'], cur))}</td><td>{e('; '.join(a['parse']['errors']))}</td></tr>")
            H.append("</table></div>")
        else:
            H.append("<p>None.</p>")
    H.append("</main></body></html>")
    return "\n".join(H) + "\n"


def write_tags(path: Path, window, rules) -> tuple:
    existing, header = [], list(TAG_COLUMNS)
    if path.exists():
        with path.open(encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            header = list(reader.fieldnames or TAG_COLUMNS)
            existing = list(reader)
        header += [c for c in TAG_COLUMNS if c not in header]
    by_id = {r.get("ad_id", "").strip(): i for i, r in enumerate(existing) if r.get("ad_id", "").strip()}
    by_name = {r.get("ad_name", "").strip(): i for i, r in enumerate(existing) if r.get("ad_name", "").strip()}
    added = updated = kept = 0
    for a in window["parsed"]:
        f = a["parse"]["fields"]
        new = {"ad_id": a["ad_id"], "ad_name": a["ad_name"],
               "launch_date": a["launch"].isoformat() if a["launch"] else "",
               "spend": f"{a['spend']:.2f}", "results": num(a["results"]).replace(",", ""),
               "cpa": "" if a["cpa"] is None else f"{a['cpa']:.2f}",
               "roas": "" if a["roas"] is None else f"{a['roas']:.2f}",
               "is_winner": {True: "yes", False: "no", None: ""}[a["is_winner"]],
               "tag_source": "name", "label": "Verified"}
        for k in ("concept_id", "angle_id", "persona_id", "awareness", "format", "voice", "shape"):
            new[k] = f[k]
        idx = by_id.get(a["ad_id"]) if a["ad_id"] else None
        if idx is None:
            idx = by_name.get(a["ad_name"])
        if idx is None:
            row = {c: "" for c in header}
            row.update(new)
            existing.append(row)
            added += 1
        elif (existing[idx].get("tag_source") or "").strip().lower() == "breakdown":
            kept += 1
        else:
            existing[idx].update(new)  # fields the name doesn't carry (hook_family, enemy...) stay
            updated += 1
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header, extrasaction="ignore")
        writer.writeheader()
        for r in existing:
            writer.writerow({c: r.get(c, "") for c in header})
    return added, updated, kept


def parse_colmap(value):
    if not value:
        return {}
    p = Path(value)
    text = p.read_text(encoding="utf-8-sig") if p.exists() else value
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        sys.exit(f"--colmap is not valid JSON: {exc}")
    bad = [k for k in data if k not in SYNONYMS]
    if bad:
        sys.exit(f"--colmap: unknown keys {', '.join(bad)} (use {', '.join(SYNONYMS)})")
    return data


def main(argv=None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Weekly creative leaderboard from an ad-level export.")
    ap.add_argument("export", help="ad-level CSV for the ranking window (usually the last 7 days)")
    ap.add_argument("--long", help="ad-level CSV for a second, longer window (usually the last 28 days)")
    ap.add_argument("--naming-map", help="the brand's field map, e.g. running-notes/ad-naming.md")
    ap.add_argument("--colmap", help="JSON (inline or a file) {our column: their header}; our columns: "
                    + ", ".join(SYNONYMS))
    ap.add_argument("--min-spend", type=float, default=0.0, help="spend an ad needs to count as tested")
    ap.add_argument("--winner-cpa-max", type=float, help="a winner's CPA is at most this")
    ap.add_argument("--winner-roas-min", type=float, help="a winner's ROAS is at least this")
    ap.add_argument("--winner-min-spend", type=float, help="spend a winner needs (default: --min-spend)")
    ap.add_argument("--angles", help="angle-bank/angles.csv, to show each angle's one-liner")
    ap.add_argument("--write-tags", help="upsert one row per parsed ad into this ad-tags.csv")
    ap.add_argument("--takeaways", help="a text or markdown file with the written takeaways to include")
    ap.add_argument("--out-dir", default="audits/leaderboard", help="where the .md and .html go")
    ap.add_argument("--week", help="ISO week for the file name, e.g. 2026-W45 (default: the window's end)")
    ap.add_argument("--top", type=int, default=10, help="how many ads in the top table (default 10)")
    ap.add_argument("--audit", action="store_true", help="only list the names that don't parse; write nothing")
    args = ap.parse_args(argv)

    fmap = ad_name.load_field_map(args.naming_map) if args.naming_map else None
    colmap = parse_colmap(args.colmap)
    bars = []
    if args.winner_cpa_max is not None:
        bars.append(f"CPA at most {args.winner_cpa_max:,.2f}")
    if args.winner_roas_min is not None:
        bars.append(f"ROAS at least {args.winner_roas_min:,.2f}")
    wms = args.winner_min_spend if args.winner_min_spend is not None else args.min_spend
    rules = {"min_spend": args.min_spend, "cpa_max": args.winner_cpa_max, "roas_min": args.winner_roas_min,
             "winner_min_spend": wms, "has_bar": bool(bars)}

    windows = [("Ranking window", enrich(load_export(Path(args.export), colmap), fmap, rules))]
    if args.long:
        windows.append(("Long window", enrich(load_export(Path(args.long), colmap), fmap, rules)))
    currency = windows[0][1]["currency"]
    rules["bar_text"] = (" and ".join(bars) + f", spend at least {money(wms, currency)}") if bars else \
        "none given, so no winners and no hit rate (read it from running-notes/success-definition.md)"

    if args.audit:
        w = windows[-1][1] if args.long else windows[0][1]
        print(f"{len(w['unparsed'])} of {len(w['ads'])} ads have names that don't parse "
              f"({money(sum(a['spend'] for a in w['unparsed']), w['currency'])} of "
              f"{money(sum(a['spend'] for a in w['ads']), w['currency'])} spend):")
        for a in sorted(w["unparsed"], key=lambda a: -a["spend"]):
            print(f"  {a['ad_name']}\t{a['ad_id']}\t{money(a['spend'], w['currency'])}\t{'; '.join(a['parse']['errors'])}")
        return 0

    for _, w in windows:
        aggregate(w)
    main_w = windows[0][1]
    end = main_w["end"] or date.today()
    iso = end.isocalendar()
    week = args.week or f"{iso[0]}-W{iso[1]:02d}"
    meta = {"week": week, "today": date.today().isoformat(), "currency": currency,
            "naming": f"field map {args.naming_map}" if args.naming_map else "the factory convention"}
    angles = load_angles(args.angles)
    takeaways = Path(args.takeaways).read_text(encoding="utf-8-sig") if args.takeaways else ""

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    md_path, html_path = out / f"{week}.md", out / f"{week}.html"
    md_path.write_text(write_markdown(meta, windows, angles, rules, takeaways, args.top), encoding="utf-8")
    html_path.write_text(write_html(meta, windows, angles, rules, takeaways, args.top), encoding="utf-8")

    t = main_w["total"]
    print(f"Wrote {md_path} and {html_path}")
    print(f"Ranking window: {t['ads']} ads, {len(main_w['unparsed'])} names don't parse, "
          f"hit rate (new) {hit(t['new_winners'] if rules['has_bar'] else None, t['new_tested'])}")
    if not args.min_spend:
        print("WARNING: no --min-spend floor; every ad with spend counts as tested")
    if not rules["has_bar"]:
        print("WARNING: no winner bar; read it from running-notes/success-definition.md and brand-rules.md")
    for key, w in windows:
        missing = [c for c in ("results", "value", "date_start") if c not in w["columns"]]
        if missing:
            print(f"NOTE ({key}): no column found for {', '.join(missing)}")
    if args.write_tags:
        src = windows[-1][1]
        added, updated, kept = write_tags(Path(args.write_tags), src, rules)
        print(f"Tags: {added} added, {updated} updated, {kept} breakdown rows kept as they were "
              f"({args.write_tags}, numbers from the {'long' if args.long else 'ranking'} window)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

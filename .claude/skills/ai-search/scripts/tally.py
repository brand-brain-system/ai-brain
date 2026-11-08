#!/usr/bin/env python3
"""Tally the AI-search run log: how often the brand and its rivals are mentioned and recommended.

    python3 tally.py <runs.csv> [--version N] [--cohort core|exploratory|control|all]

Reads the run log described in ai-search/prompt-portfolio.md, one row per run:
  date, portfolio_version, prompt_id, topic, cohort, assistant, run, mentioned,
  recommended, position, competitors, cited_urls, wrong_facts, screenshot
Prints, for one portfolio version (the newest in the file unless --version is given):
  - the brand's mention and recommendation rate per topic and per assistant, as "k/n"
  - each rival's mention rate per topic, from the `competitors` column
  - the cited domains, by the number of runs that cited them
  - every wrong fact, with prompt and assistant
Rates are counts of runs, never percentages without the n. Rows from other portfolio
versions are skipped and counted, so two different portfolios are never mixed.
"""
import argparse
import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse

COLUMNS = ["date", "portfolio_version", "prompt_id", "topic", "cohort", "assistant", "run",
           "mentioned", "recommended", "position", "competitors", "cited_urls", "wrong_facts",
           "screenshot"]
YES = {"yes", "ja", "y", "true", "1"}


def split_list(value: str) -> list[str]:
    return [v.strip() for v in (value or "").split(";") if v.strip()]


def domain(url: str) -> str:
    host = urlparse(url if "://" in url else "https://" + url).netloc.lower()
    return host[4:] if host.startswith("www.") else host


def load(path: Path) -> list[dict]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        missing = [c for c in COLUMNS if c not in (reader.fieldnames or [])]
        if missing:
            sys.exit(f"{path}: missing columns: {', '.join(missing)}")
        return list(reader)


def rate(rows: list[dict], field: str) -> str:
    k = sum(1 for r in rows if r[field].strip().lower() in YES)
    return f"{k}/{len(rows)}"


def table(title: str, groups: dict[str, list[dict]]) -> list[str]:
    out = [title, f"  {'':28} {'mentioned':>10} {'recommended':>12}"]
    for key in sorted(groups):
        rows = groups[key]
        out.append(f"  {key[:28]:28} {rate(rows, 'mentioned'):>10} {rate(rows, 'recommended'):>12}")
    return out


def tally(rows: list[dict], version: str | None, cohort: str) -> tuple[list[str], list[str]]:
    versions = sorted({r["portfolio_version"].strip() for r in rows if r["portfolio_version"].strip()},
                      key=lambda v: (len(v), v))
    if not versions:
        return [], ["no rows with a portfolio_version"]
    version = version or versions[-1]
    picked = [r for r in rows if r["portfolio_version"].strip() == version]
    warn = []
    skipped = len(rows) - len(picked)
    if skipped:
        warn.append(f"{skipped} rows from other portfolio versions skipped (reporting version {version})")
    if cohort != "all":
        picked = [r for r in picked if r["cohort"].strip().lower() == cohort]
    if not picked:
        return [], warn + [f"no {cohort} rows in version {version}"]

    runs_per_prompt = Counter((r["prompt_id"], r["assistant"]) for r in picked)
    thin = sorted(k for k, n in runs_per_prompt.items() if n < 3)
    if thin:
        warn.append(f"{len(thin)} prompt x assistant pairs have fewer than 3 runs: read them as anecdotes")

    dates = sorted({r["date"] for r in picked})
    lines = [f"Portfolio version {version}, cohort {cohort}, {len(picked)} runs, "
             f"{dates[0]} to {dates[-1]}", ""]

    by_topic, by_assistant = defaultdict(list), defaultdict(list)
    for r in picked:
        by_topic[r["topic"].strip() or "(no topic)"].append(r)
        by_assistant[r["assistant"].strip() or "(no assistant)"].append(r)
    lines += table("The brand, by topic", by_topic) + [""]
    lines += table("The brand, by assistant", by_assistant) + [""]

    rivals = sorted({c for r in picked for c in split_list(r["competitors"])})
    if rivals:
        lines.append("Rivals named, by topic (runs naming them / runs)")
        for topic in sorted(by_topic):
            topic_rows = by_topic[topic]
            counts = Counter(c for r in topic_rows for c in set(split_list(r["competitors"])))
            named = ", ".join(f"{c} {counts[c]}/{len(topic_rows)}" for c in rivals if counts[c])
            lines.append(f"  {topic[:28]:28} {named or '-'}")
        lines.append("")

    cited = Counter()
    for r in picked:
        for d in {domain(u) for u in split_list(r["cited_urls"])}:
            cited[d] += 1
    if cited:
        lines.append("Cited domains (runs citing them)")
        for d, n in cited.most_common(15):
            lines.append(f"  {n:>4}  {d}")
        lines.append("")

    wrong = [r for r in picked if r["wrong_facts"].strip()]
    if wrong:
        lines.append("Wrong facts")
        for r in wrong:
            lines.append(f"  {r['date']} {r['prompt_id']} {r['assistant']} run {r['run']}: {r['wrong_facts'].strip()}")
        lines.append("")
    return lines, warn


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("runs", type=Path)
    parser.add_argument("--version", help="portfolio version to report (default: newest)")
    parser.add_argument("--cohort", default="core", help="core, exploratory, control or all (default: core)")
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")  # Danish letters survive a Windows pipe
    lines, warn = tally(load(args.runs), args.version, args.cohort.lower())
    for w in warn:
        print(f"! {w}")
    print("\n".join(lines))
    return 0 if lines else 1


if __name__ == "__main__":
    sys.exit(main())

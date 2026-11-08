"""The scripts behind ai-search and competitor-teardown (v11).

ai-search/scripts/tally.py turns the run log into rates that always carry their n
and never mixes two portfolio versions. competitor-teardown/scripts/teardown.py
reads public pages; only its offline parts are tested here (tool detection, the
headline reader, the ad-library links), so the suite never touches the network.
"""
import csv
import importlib.util
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from test_runtime_hooks import FACTORY

SKILLS = Path(FACTORY) / ".claude" / "skills"
TALLY = SKILLS / "ai-search" / "scripts" / "tally.py"
TEARDOWN = SKILLS / "competitor-teardown" / "scripts" / "teardown.py"

COLUMNS = ["date", "portfolio_version", "prompt_id", "topic", "cohort", "assistant", "run",
           "mentioned", "recommended", "position", "competitors", "cited_urls", "wrong_facts",
           "screenshot"]


def load(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_tally(rows, *args):
    with tempfile.TemporaryDirectory() as tmp:
        log = Path(tmp) / "runs.csv"
        with log.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=COLUMNS)
            writer.writeheader()
            for row in rows:
                writer.writerow({c: row.get(c, "") for c in COLUMNS})
        r = subprocess.run([sys.executable, str(TALLY), str(log), *args], capture_output=True,
                           text=True, encoding="utf-8", env={**os.environ, "PYTHONIOENCODING": "utf-8"})
    return r.returncode, r.stdout


def row(**kw):
    base = {"date": "2026-10-31", "portfolio_version": "1", "prompt_id": "p1", "topic": "gaveidé til far",
            "cohort": "core", "assistant": "chatgpt", "run": "1", "mentioned": "no", "recommended": "no"}
    return {**base, **kw}


class TallyTest(unittest.TestCase):
    def test_rates_carry_their_n_and_danish_survives(self):
        code, out = run_tally([row(run="1", mentioned="yes", recommended="yes"),
                               row(run="2", mentioned="yes"), row(run="3")])
        self.assertEqual(code, 0, out)
        self.assertIn("gaveidé til far", out)
        self.assertRegex(out, r"gaveidé til far\s+2/3\s+1/3")

    def test_versions_never_mix(self):
        code, out = run_tally([row(portfolio_version="1", mentioned="no"),
                               row(portfolio_version="2", mentioned="yes")])
        self.assertIn("1 rows from other portfolio versions skipped (reporting version 2)", out)
        self.assertRegex(out, r"gaveidé til far\s+1/1")

    def test_thin_samples_are_flagged(self):
        code, out = run_tally([row()])
        self.assertIn("fewer than 3 runs", out)

    def test_cited_domains_drop_www_and_count_once_per_run(self):
        code, out = run_tally([row(cited_urls="https://www.example.dk/a;https://example.dk/b"),
                               row(run="2", cited_urls="example.dk/c")])
        self.assertRegex(out, r"\s2\s+example\.dk")

    def test_missing_columns_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            log = Path(tmp) / "runs.csv"
            log.write_text("date,topic\n2026-10-31,x\n", encoding="utf-8")
            r = subprocess.run([sys.executable, str(TALLY), str(log)], capture_output=True, text=True)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("missing columns", r.stderr)


class TeardownOfflineTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.t = load(TEARDOWN)

    def test_detects_tools_from_page_source(self):
        page = ('<script src="https://cdn.shopify.com/x.js"></script>'
                '<script src="https://static.klaviyo.com/onsite/js/klaviyo.js"></script>'
                '<script>fbq("init","1")</script><script src="https://widget.trustpilot.com/b.js"></script>')
        found = self.t.detect(page)
        for tool in ("Shopify", "Klaviyo", "Meta pixel", "Trustpilot widget"):
            self.assertIn(tool, found)
        self.assertNotIn("Recharge", found)

    def test_reads_title_headline_and_description(self):
        hero = self.t.hero_of('<title>Sko &amp; mere</title><meta name="description" content="Fri fragt">'
                              '<h1 class="x">Gå <em>længere</em></h1>')
        self.assertEqual(hero, {"title": "Sko & mere", "h1": "Gå længere", "description": "Fri fragt"})

    def test_ad_links_are_set_to_denmark(self):
        links = self.t.cmd_ads("Some Rival", "rival.dk")
        self.assertIn("country=DK", links["meta_ad_library"])
        self.assertIn("q=Some%20Rival", links["meta_ad_library"])
        self.assertIn("region=DK", links["google_ads_transparency"])


if __name__ == "__main__":
    unittest.main()

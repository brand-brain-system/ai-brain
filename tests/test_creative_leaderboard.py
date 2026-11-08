"""The creative-leaderboard scripts (v20).

ad_name.py parses an ad name into the shared tags (the convention in
system/ad-naming-convention.md, or a brand's own field map). leaderboard.py ranks an
ad-level export by those tags, counts winners and hit rate, writes the weekly .md and
.html and can upsert angle-bank/ad-tags.csv. All data here is synthetic and fictional.
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

SCRIPTS = Path(FACTORY) / ".claude" / "skills" / "creative-leaderboard" / "scripts"
LEADERBOARD = SCRIPTS / "leaderboard.py"


def load(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ad_name = load(SCRIPTS / "ad_name.py")

MCP_COLUMNS = ["ad_id", "ad_name", "spend", "purchases", "purchase_value", "date_start", "date_stop"]


def write_csv(path: Path, columns, rows):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(columns)
        w.writerows(rows)


def run(*args, cwd=None):
    r = subprocess.run([sys.executable, str(LEADERBOARD), *map(str, args)], capture_output=True,
                       text=True, encoding="utf-8", cwd=cwd,
                       env={**os.environ, "PYTHONIOENCODING": "utf-8"})
    return r.returncode, r.stdout + r.stderr


# A fictional week, 2026-11-02 to 2026-11-08 (ISO week 45).
WEEK = [
    # ad_id, name, spend, purchases, value
    ["101", "261103_C07_A01_P1_PA_ugc-talk_creator_enemy_H1_v1", "2000", "20", "9000"],   # winner, new
    ["102", "261103_C07_A01_P2_PA_static-benefit_none_symptom_H2_v1", "1500", "5", "2000"],  # not a winner, new
    ["103", "261020_C08_A02_P1_SA_podcast_expert_authority_H1_v2", "3000", "25", "11000"],  # winner, old
    ["104", "261104_C09_A02_P1_UN_song_song_story_x_v1", "100", "1", "400"],              # under the floor
    ["105", "Summer sale ad - final FINAL", "800", "4", "1500"],                         # doesn't parse
]


def week_rows():
    return [r + ["2026-11-02", "2026-11-08"] for r in WEEK]


class ParserTest(unittest.TestCase):
    def test_full_name(self):
        p = ad_name.parse("261107_C07_A03_P2_PA_ugc-talk_creator_enemy_H2_v1")
        self.assertTrue(p["ok"], p["errors"])
        self.assertEqual(p["fields"], {"launch_date": "2026-11-07", "concept_id": "C07", "angle_id": "A03",
                                       "persona_id": "P2", "awareness": "PA", "format": "ugc-talk",
                                       "voice": "creator", "shape": "enemy", "hook": "H2", "version": "v1"})

    def test_x_fields_and_a_copy_suffix(self):
        p = ad_name.parse("261107_C07-2_x_x_x_static-offer_none_offer_x_v3 - Copy")
        self.assertTrue(p["ok"], p["errors"])
        self.assertTrue(p["copy"])
        self.assertEqual(p["fields"]["concept_id"], "C07-2")
        self.assertEqual(p["fields"]["angle_id"], "x")
        self.assertEqual(p["fields"]["awareness"], "x")

    def test_extra_tail_is_kept(self):
        p = ad_name.parse("261107_C07_A03_P2_PA_ugc-talk_creator_enemy_H2_v1_15s_9x16")
        self.assertTrue(p["ok"], p["errors"])
        self.assertEqual(p["extra"], ["15s", "9x16"])

    def test_malformed_names_say_why(self):
        p = ad_name.parse("261107_C07_A03_P2_XX_ugc talk_creator")
        self.assertFalse(p["ok"])
        joined = " ".join(p["errors"])
        self.assertIn("expected at least 10", joined)
        self.assertIn("awareness 'XX'", joined)
        self.assertIn("has a space", joined)
        self.assertFalse(ad_name.parse("261399_C07_A03_P2_PA_ugc-talk_creator_enemy_H2_v1")["ok"])
        self.assertFalse(ad_name.parse("261107__A03_P2_PA_ugc-talk_creator_enemy_H2_v1")["ok"])

    def test_custom_field_map(self):
        with tempfile.TemporaryDirectory() as tmp:
            m = Path(tmp) / "ad-naming.md"
            m.write_text(
                "# Ad naming field map\n\n"
                "separator: `-`\n"
                "date_format: DDMMYY\n\n"
                "| Position | Their field | Our field | Value map |\n"
                "|---|---|---|---|\n"
                "| 1 | Product | x | |\n"
                "| 2 | Date | launch_date | |\n"
                "| 3 | Concept | concept_id | |\n"
                "| 4 | Angle word | angle_id | pain=A01; gift=A02 |\n"
                "| 5 | Type | format | UGC=ugc-talk; STAT=static-benefit |\n", encoding="utf-8")
            fmap = ad_name.load_field_map(m)
            p = ad_name.parse("SOCK-071126-C12-gift-STAT", fmap)
            self.assertTrue(p["ok"], p["errors"])
            self.assertEqual(p["fields"]["launch_date"], "2026-11-07")
            self.assertEqual(p["fields"]["angle_id"], "A02")
            self.assertEqual(p["fields"]["format"], "static-benefit")
            self.assertEqual(p["fields"]["persona_id"], "x")
            bad = ad_name.parse("SOCK-071126-C12-joy-STAT", fmap)
            self.assertFalse(bad["ok"])

    def test_cli_prints_json_and_build_round_trips(self):
        r = subprocess.run([sys.executable, str(SCRIPTS / "ad_name.py"),
                            "261107_C07_A03_P2_PA_ugc-talk_creator_enemy_H2_v1"],
                           capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('"angle_id": "A03"', r.stdout)
        name = ad_name.build_name({"launch_date": "2026-11-07", "concept_id": "C07", "format": "static-benefit"})
        self.assertEqual(name, "261107_C07_x_x_x_static-benefit_x_x_x_x")
        self.assertTrue(ad_name.parse(name)["ok"])


class LeaderboardTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        self.export = self.dir / "week.csv"
        write_csv(self.export, MCP_COLUMNS, week_rows())
        self.out = self.dir / "audits" / "leaderboard"

    def tearDown(self):
        self.tmp.cleanup()

    def board(self, *extra):
        code, out = run(self.export, "--out-dir", self.out, "--min-spend", "500",
                        "--winner-cpa-max", "150", "--winner-min-spend", "1000", *extra)
        self.assertEqual(code, 0, out)
        return out, (self.out / "2026-W45.md").read_text(encoding="utf-8")

    def test_aggregation_and_hit_rate(self):
        out, md = self.board()
        # New tested ads: 101 (winner) and 102 (not). 103 won but launched before the window.
        self.assertIn("hit rate (new) 1/2 (50.00%)", out)
        self.assertRegex(md, r"\| A01 \| 2 \| 2 \| 3,500\.00 \| [\d.]+% \| 25 \| 140\.00 \| 3\.14 \| 1 \| 1/2 \(50\.00%\) \|")
        self.assertRegex(md, r"\| A02 \| 2 \| 1 \| 3,100\.00 \|.*\| 1 \| 0/0 \|")
        self.assertIn("### By persona", md)
        self.assertIn("### By shape", md)

    def test_min_spend_floor(self):
        _, md = self.board()
        self.assertRegex(md, r"\| UN \| 1 \| 0 \| 100\.00 \|")  # 104 spent 100, under the floor of 500
        self.assertNotIn("261104_C09", md.split("### Top 10 tested ads by spend")[1].split("### Names")[0])

    def test_unparseable_names_are_listed(self):
        _, md = self.board()
        section = md.split("### Names that don't parse (1)")[1]
        self.assertIn("Summer sale ad - final FINAL", section)

    def test_no_winner_bar_means_no_hit_rate(self):
        code, out = run(self.export, "--out-dir", self.out)
        self.assertEqual(code, 0, out)
        self.assertIn("WARNING: no winner bar", out)
        self.assertIn("no bar", out)

    def test_ads_manager_columns_with_currency_suffix(self):
        export = self.dir / "ads-manager.csv"
        cols = ["Reporting starts", "Reporting ends", "Ad name", "Ad ID", "Amount spent (DKK)",
                "Results", "Purchases", "Purchases conversion value"]
        write_csv(export, cols, [
            ["2026-11-02", "2026-11-08", WEEK[0][1], "101", "1000.50", "99", "10", "4000"],
            ["2026-11-02", "2026-11-08", WEEK[0][1], "101", "999.50", "99", "10", "5000"],  # second ad set
        ])
        code, out = run(export, "--out-dir", self.out, "--min-spend", "500", "--winner-roas-min", "4")
        self.assertEqual(code, 0, out)
        md = (self.out / "2026-W45.md").read_text(encoding="utf-8")
        self.assertIn("2,000.00 DKK", md)        # rows of one ad are added up, currency kept
        self.assertIn("100.00 DKK", md)          # CPA from Purchases (20), not Results
        self.assertIn("| 4.50 |", md)            # ROAS 9000 / 2000

    def test_danish_semicolon_export_and_colmap(self):
        export = self.dir / "dansk.csv"
        export.write_text("Annoncenavn;Brugt beløb (DKK);Køb;Mærke\n"
                          f"{WEEK[0][1]};1.234,50;3;x\n", encoding="utf-8")
        code, out = run(export, "--out-dir", self.out, "--week", "2026-W45")
        self.assertEqual(code, 0, out)
        self.assertIn("1,234.50 DKK", (self.out / "2026-W45.md").read_text(encoding="utf-8"))
        code, out = run(self.export, "--out-dir", self.out, "--colmap", '{"spend": "purchase_value"}')
        self.assertEqual(code, 0, out)
        code, out = run(self.export, "--out-dir", self.out, "--colmap", '{"spend": "Nope"}')
        self.assertNotEqual(code, 0)

    def test_write_tags_upserts_and_keeps_breakdown_rows(self):
        tags = self.dir / "angle-bank" / "ad-tags.csv"
        tags.parent.mkdir(parents=True)
        cols = ["ad_id", "ad_name", "launch_date", "spend", "results", "cpa", "roas", "is_winner",
                               "concept_id", "angle_id", "persona_id", "awareness", "format", "voice", "shape",
                               "hook_family", "enemy", "mechanism", "proof", "close", "product_at",
                               "tag_source", "label"]
        old = {c: "" for c in cols}
        breakdown = {**old, "ad_id": "103", "ad_name": WEEK[2][1], "angle_id": "A09", "hook_family": "secret",
                     "tag_source": "breakdown", "label": "Inferred"}
        stale = {**old, "ad_id": "101", "ad_name": WEEK[0][1], "angle_id": "A05", "enemy": "the old cream",
                 "tag_source": "name", "label": "Verified"}
        with tags.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols)
            w.writeheader()
            w.writerow(breakdown)
            w.writerow(stale)
        out, _ = self.board("--write-tags", tags)
        self.assertIn("2 added, 1 updated, 1 breakdown rows kept", out)
        with tags.open(encoding="utf-8", newline="") as f:
            rows = {r["ad_id"]: r for r in csv.DictReader(f)}
        self.assertEqual(rows["103"]["angle_id"], "A09")            # breakdown row untouched
        self.assertEqual(rows["103"]["spend"], "")
        self.assertEqual(rows["101"]["angle_id"], "A01")            # name row refreshed
        self.assertEqual(rows["101"]["enemy"], "the old cream")     # fields the name lacks stay
        self.assertEqual(rows["101"]["is_winner"], "yes")
        self.assertEqual(rows["102"]["tag_source"], "name")
        self.assertEqual(rows["102"]["label"], "Verified")
        self.assertNotIn("105", rows)                               # unparsed names get no tags

    def test_write_tags_creates_the_file(self):
        tags = self.dir / "new" / "ad-tags.csv"
        self.board("--write-tags", tags)
        header = tags.read_text(encoding="utf-8").splitlines()[0]
        self.assertTrue(header.startswith("ad_id,ad_name,launch_date,spend"))
        self.assertTrue(header.endswith("tag_source,label"))

    def test_html_written_and_self_contained(self):
        angles = self.dir / "angles.csv"
        write_csv(angles, ["angle_id", "angle"], [["A01", "The shoes, not the knees"]])
        self.board("--angles", angles)
        page = (self.out / "2026-W45.html").read_text(encoding="utf-8")
        self.assertIn("prefers-color-scheme: dark", page)
        self.assertIn("class=\"bar\"", page)
        self.assertIn("A01: The shoes, not the knees", page)
        self.assertNotRegex(page, r"(src|href)=\"https?://")

    def test_takeaways_and_audit(self):
        notes = self.dir / "takeaways.md"
        notes.write_text("- A01 carried the week\n", encoding="utf-8")
        _, md = self.board("--takeaways", notes)
        self.assertIn("- A01 carried the week", md)
        code, out = run(self.export, "--audit")
        self.assertEqual(code, 0, out)
        self.assertIn("1 of 5 ads have names that don't parse", out)


if __name__ == "__main__":
    unittest.main()

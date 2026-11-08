"""The angle-bank gap matrix (v20).

angle-bank/scripts/gap_matrix.py reads angles.csv and ad-tags.csv and writes the gap
matrix as Markdown and a self-contained HTML heatmap. Every fixture here is synthetic
and written to a temp folder; no brand data.
"""
import csv
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from test_runtime_hooks import FACTORY

SCRIPT = Path(FACTORY) / ".claude" / "skills" / "angle-bank" / "scripts" / "gap_matrix.py"
SCAFFOLD = Path(FACTORY) / "templates" / "brand-scaffold" / "angle-bank"

ANGLE_COLUMNS = ["angle_id", "angle", "persona_ids", "awareness", "enemy", "ump", "ums", "quote", "quote_source",
                 "evidence_people", "status", "first_seen", "last_tested", "notes"]
TAG_COLUMNS = ["ad_id", "ad_name", "launch_date", "spend", "results", "cpa", "roas", "is_winner", "concept_id",
               "angle_id", "persona_id", "awareness", "format", "voice", "shape", "hook_family", "enemy",
               "mechanism", "proof", "close", "product_at", "tag_source", "label"]

ANGLES = [
    {"angle_id": "A01", "angle": "Sleeps through the night again", "persona_ids": "P1", "awareness": "PA+SA",
     "evidence_people": "12", "status": "won"},
    {"angle_id": "A02", "angle": "The cheap pillow is why your neck hurts", "persona_ids": "P1+P2",
     "awareness": "PA", "evidence_people": "3", "status": "live"},
    {"angle_id": "A03", "angle": "A gift that gets used every night", "persona_ids": "P2", "awareness": "UN+PR",
     "evidence_people": "9", "status": "idea"},
    {"angle_id": "A04", "angle": "Made to last ten years", "persona_ids": "P3", "awareness": "MA",
     "evidence_people": "2", "status": "idea"},
]


def tag(ad_id, angle, spend, winner="no", awareness="PA", persona="P1", launch="2026-08-01", **kw):
    return {"ad_id": ad_id, "ad_name": f"260801_x_{angle}_{persona}_{awareness}_ugc-talk_creator_enemy_H1_v1",
            "launch_date": launch, "spend": spend, "is_winner": winner, "angle_id": angle, "persona_id": persona,
            "awareness": awareness, "format": "ugc-talk", "voice": "creator", "shape": "enemy",
            "tag_source": "name", "label": "Verified", **kw}


TAGS = [
    tag("1", "A01", "5000", "yes", "PA"),
    tag("2", "A01", "3000", "yes", "PA+SA"),
    tag("3", "A01", "400", "no", "SA"),
    tag("4", "A02", "1000", "yes", "PA", "P2"),
    tag("5", "A02", "200", "no", "PA", "P1+P2"),
    tag("6", "A99", "700", "no", "PR", "P3"),
    tag("7", "A01", "20", "no", "UN"),
    tag("8", "A02", "300", "no", "SA", "P2", launch="2026-11-01"),
]


def write(path, columns, rows):
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            writer.writerow({c: row.get(c, "") for c in columns})


class GapMatrixTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name) / "angle-bank"
        self.dir.mkdir()
        self.angles = self.dir / "angles.csv"
        self.tags = self.dir / "ad-tags.csv"

    def tearDown(self):
        self.tmp.cleanup()

    def run_script(self, angles=ANGLES, tags=TAGS, *extra, angle_cols=ANGLE_COLUMNS, tag_cols=TAG_COLUMNS):
        write(self.angles, angle_cols, angles)
        write(self.tags, tag_cols, tags)
        r = subprocess.run([sys.executable, str(SCRIPT), "--angles", str(self.angles), "--tags", str(self.tags),
                            "--date", "2026-11-07", *extra], capture_output=True, text=True, encoding="utf-8",
                           env={**os.environ, "PYTHONIOENCODING": "utf-8"})
        md = self.dir / "gap-matrix-2026-11-07.md"
        return r, (md.read_text(encoding="utf-8") if md.is_file() else "")

    def row(self, md, label):
        lines = [line for line in md.splitlines() if line.startswith(f"| {label}")]
        self.assertTrue(lines, f"no row for {label}:\n{md}")
        return [c.strip() for c in lines[0].strip("|").split("|")]

    def test_matrix_counts(self):
        r, md = self.run_script(ANGLES, TAGS, "--min-spend", "50")
        self.assertEqual(r.returncode, 0, r.stderr)
        a01 = self.row(md, "A01")  # Angle, People, Status, UN, PA, SA, PR, MA
        self.assertEqual(a01[3], "-")  # the 20-spend UN ad is below the floor
        self.assertEqual(a01[4], "WON 2 ads, 2 won, 8,000")
        self.assertEqual(a01[5], "WON 2 ads, 1 won, 3,400")
        a02 = self.row(md, "A02")
        self.assertEqual(a02[4], "WON 2 ads, 1 won, 1,200")
        self.assertEqual(a02[5], "live 1 ad, 0 won, 300")  # launched six days ago
        self.assertIn("7 at or above the spend floor", md)
        self.assertIn("1 below the spend floor", r.stdout)

    def test_multi_value_awareness_and_persona_count_in_each_cell(self):
        r, md = self.run_script()
        p1 = self.row(md, "P1 |")  # Persona, UN, PA, SA, PR, MA
        self.assertEqual(p1[2], "WON 3 ads, 2 won, 8,200")  # PA: ads 1, 2, 5
        self.assertEqual(p1[3], "WON 2 ads, 1 won, 3,400")  # SA: ads 2, 3
        p2 = self.row(md, "P2 |")
        self.assertEqual(p2[2], "WON 2 ads, 1 won, 1,200")  # PA: ads 4, 5
        a03 = self.row(md, "A03")
        self.assertEqual(a03[3], "GAP")  # 9 people, fits UN, never tried
        a04 = self.row(md, "A04")
        self.assertEqual(a04[7], "-")  # 2 people: empty but not marked

    def test_lost_cells_and_gap_ranking(self):
        r, md = self.run_script()
        self.assertIn("lost 1 ad, 0 won, 700", self.row(md, "A99")[6])
        ranked = md.split("## Empty cells, ranked by evidence", 1)[1]
        first = [line for line in ranked.splitlines() if line.startswith("| 1 |")][0]
        self.assertIn("A03", first)

    def test_top_three_concentration_flag(self):
        r, md = self.run_script()
        self.assertIn("**Concentrated:**", md)
        self.assertIn("(concentrated)", r.stdout)
        spread = [tag(str(i), f"A0{i}", "1000", "yes") for i in range(1, 5)] + [tag("9", "A05", "1000", "yes")]
        extra = ANGLES + [{"angle_id": "A05", "angle": "Fifth angle", "awareness": "PA", "evidence_people": "1"}]
        r, md = self.run_script(extra, spread)
        self.assertNotIn("**Concentrated:**", md)
        self.assertIn("top 3 angles hold 60%", r.stdout)

    def test_unknown_angle_ids_are_reported_not_crashed(self):
        r, md = self.run_script()
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("angle A99 is not in angles.csv (1 ad, 0 winners, spend 700)", r.stdout)
        self.assertIn("A99 (not in angles.csv)", md)

    def test_missing_columns_fail_cleanly(self):
        r, _ = self.run_script(ANGLES, TAGS, tag_cols=[c for c in TAG_COLUMNS if c not in ("is_winner", "spend")])
        self.assertEqual(r.returncode, 2)
        self.assertIn("missing columns: spend, is_winner", r.stderr)
        self.assertNotIn("Traceback", r.stderr)
        self.assertFalse((self.dir / "gap-matrix-2026-11-07.html").exists())

    def test_empty_files(self):
        r, md = self.run_script([], [])
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("No winner spend in the file", md)
        self.angles.write_text("", encoding="utf-8")
        r = subprocess.run([sys.executable, str(SCRIPT), "--angles", str(self.angles), "--tags", str(self.tags)],
                           capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(r.returncode, 2)
        self.assertIn("is empty", r.stderr)

    def test_html_is_written_and_self_contained(self):
        r, _ = self.run_script()
        page = (self.dir / "gap-matrix-2026-11-07.html").read_text(encoding="utf-8")
        self.assertTrue(page.startswith("<!doctype html>"))
        self.assertIn("prefers-color-scheme: dark", page)
        self.assertIn("Sleeps through the night again", page)
        self.assertIn('class="c gap"', page)
        self.assertIn('class="c won"', page)
        self.assertNotIn("http://", page)
        self.assertNotIn("https://", page)
        self.assertNotIn("<script src", page)

    def test_scaffold_files_carry_the_contract_headers(self):
        for name, columns in (("angles.csv", ANGLE_COLUMNS), ("ad-tags.csv", TAG_COLUMNS)):
            lines = (SCAFFOLD / name).read_text(encoding="utf-8").splitlines()
            self.assertEqual(lines, [",".join(columns)], name)
        self.assertIn("It is not one of the folder's docs", (SCAFFOLD / "README.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()

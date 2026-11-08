"""scripts/factory-map.py: the factory map the improve-factory skill reads as its step 0.

The map replaces re-exploring the repo at the start of a factory change, so it must
run cleanly, name the skills and method docs that exist, and keep its sections apart.
"""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from test_runtime_hooks import FACTORY

SCRIPT = Path(FACTORY) / "scripts" / "factory-map.py"


def run(*args):
    return subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True,
                          text=True, encoding="utf-8", timeout=60)


class FactoryMap(unittest.TestCase):
    def test_full_map_names_skills_and_docs(self):
        result = run()
        self.assertEqual(result.returncode, 0, result.stderr)
        out = result.stdout
        self.assertIn("# Factory map", out)
        self.assertIn("**persona-gap**", out)
        self.assertIn("**hooks.md**", out)
        self.assertIn("## Agents", out)
        self.assertIn("craft catalog:", out)
        self.assertLess(len(out.encode("utf-8")), 30000, "the map should stay a quick read")

    def test_skills_section_omits_docs(self):
        result = run("--section", "skills")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("**persona-gap**", result.stdout)
        self.assertNotIn("## Method docs", result.stdout)
        self.assertNotIn("**hooks.md**", result.stdout)

    def test_docs_section_omits_skills(self):
        result = run("--section", "docs")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("**hooks.md**", result.stdout)
        self.assertNotIn("## Skills", result.stdout)

    def test_out_writes_utf8_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "map.md"
            result = run("--out", str(target))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("**persona-gap**", target.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()

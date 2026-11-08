"""The release check in scripts/check-release.py (CLAUDE.md rule 5).

Brains pin a release tag and /update-brain reads that release's migration and
notes by name, so a tag without them, or a note without the VERSION bump, must
fail before a brain can pin it.
"""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from test_runtime_hooks import FACTORY

SCRIPT = Path("scripts") / "check-release.py"


def run(root, *args, env=None):
    return subprocess.run(
        [sys.executable, str(Path(root) / SCRIPT), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        env={**os.environ, "GITHUB_REF_TYPE": "", **(env or {})},
    )


class ReleaseCheckTest(unittest.TestCase):
    def test_the_factory_passes(self):
        r = run(FACTORY)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def release(self, version="v2", notes=("v1", "v2")):
        """A temp factory with VERSION and a migration and release note per version."""
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp)
        (tmp / "scripts").mkdir()
        shutil.copy(Path(FACTORY) / SCRIPT, tmp / SCRIPT)
        (tmp / "VERSION").write_text(version + "\n", encoding="utf-8")
        for folder in ("migrations", "release-notes"):
            (tmp / folder).mkdir()
            (tmp / folder / "README.md").write_text("not a release\n", encoding="utf-8")
            for n in notes:
                (tmp / folder / f"{n}.md").write_text(f"# {n}\n", encoding="utf-8")
        return tmp

    def test_a_complete_release_passes_with_its_tag(self):
        r = run(self.release(), "v2")
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_a_tag_without_the_version_bump_fails(self):
        r = run(self.release(), "v3")
        self.assertEqual(r.returncode, 1)
        self.assertIn("tag v3 does not match VERSION v2", r.stdout)

    def test_the_tag_is_read_from_github_on_a_tag_push(self):
        root = self.release()
        bad = run(root, env={"GITHUB_REF_TYPE": "tag", "GITHUB_REF_NAME": "v3"})
        self.assertEqual(bad.returncode, 1, bad.stdout)
        branch = run(root, env={"GITHUB_REF_TYPE": "branch", "GITHUB_REF_NAME": "main"})
        self.assertEqual(branch.returncode, 0, branch.stdout)

    def test_a_missing_migration_fails(self):
        root = self.release()
        (root / "migrations" / "v2.md").unlink()
        r = run(root)
        self.assertEqual(r.returncode, 1)
        self.assertIn("migrations/v2.md is missing", r.stdout)

    def test_a_note_without_the_version_bump_fails(self):
        r = run(self.release(version="v2", notes=("v1", "v2", "v3")))
        self.assertEqual(r.returncode, 1)
        self.assertIn("has v3 but VERSION is v2", r.stdout)

    def test_a_malformed_version_fails(self):
        r = run(self.release(version="5"))
        self.assertEqual(r.returncode, 1)
        self.assertIn("is not v<number>", r.stdout)


if __name__ == "__main__":
    unittest.main()

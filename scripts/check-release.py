#!/usr/bin/env python3
"""Check that a release follows CLAUDE.md rule 5 before brains can pin it.

A release is `VERSION` bumped to vN, `migrations/vN.md`, `release-notes/vN.md`,
and the commit tagged vN. Brains pin the tag and `/update-brain` reads the notes
and migrations by name, so a tag pushed without them leaves every brain with a
release it can't apply. This checks:

  - `VERSION` holds one version, `v` and a number
  - `migrations/` and `release-notes/` both have a file for it
  - neither folder has a newer one (a note written but `VERSION` not bumped)
  - given a tag, the tag equals `VERSION`

    python3 scripts/check-release.py         # the files agree
    python3 scripts/check-release.py v6      # ...and VERSION is v6

In CI the tag comes from GITHUB_REF_NAME when GITHUB_REF_TYPE is "tag", so a tag
pushed without the bump fails its run. Branch pushes check the files only.
tests/test_release_check.py runs it on every PR.
"""
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTE_DIRS = ("migrations", "release-notes")
VERSION_RE = re.compile(r"^v(\d+)$")


def note_versions(folder: Path) -> list[int]:
    return sorted(int(m[1]) for p in folder.glob("v*.md") if (m := VERSION_RE.match(p.stem)))


def check(root: Path, tag: str | None) -> list[str]:
    try:
        version = (root / "VERSION").read_text(encoding="utf-8").strip()
    except OSError as err:
        return [f"VERSION: could not read ({err.strerror})"]
    m = VERSION_RE.match(version)
    if not m:
        return [f"VERSION: {version!r} is not v<number>"]
    number = int(m[1])

    errors = []
    for folder in NOTE_DIRS:
        found = note_versions(root / folder)
        if number not in found:
            errors.append(f"{folder}/{version}.md is missing")
        newer = [f"v{n}" for n in found if n > number]
        if newer:
            errors.append(f"{folder}/ has {', '.join(newer)} but VERSION is {version}: bump VERSION")
    if tag is not None and tag != version:
        errors.append(f"tag {tag} does not match VERSION {version}")
    return errors


def main() -> int:
    tag = sys.argv[1] if len(sys.argv) > 1 else None
    if tag is None and os.environ.get("GITHUB_REF_TYPE") == "tag":
        tag = os.environ.get("GITHUB_REF_NAME")
    errors = check(ROOT, tag)
    for e in errors:
        print(f"x {e}")
    if errors:
        return 1
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    print(f"ok release {version}" + (f", tag {tag}" if tag else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""SessionStart hook for a brand brain: catch a broken method mount before work starts,
and say where the build stands: only scaffolded (a `.scaffolded` marker at the root,
no build started) or partway through a build (a live BUILD-STATUS.md at the root).

The brain's method (prompts, craft knowledge, system docs) lives at brain-system/,
a git submodule of the Brand-brain factory pinned to a release tag. A folder that
arrives without it (or with it empty) leaves every method reference dangling until
it is initialized. This hook checks the mount at session start.

Syncing is NOT this hook's job, it only reminds the model how this brain is shared:
through git (pull before work, commit and push after, see /save-brain). In a cloud
run (CLAUDE_CODE_REMOTE=true) the same holds, in the run's own clone.
Origin: Parker's session-start hook, adapted for git-shared brains.
"""

import json
import os
import subprocess
from pathlib import Path

MOUNT = Path("brain-system")

SYNC_LINE = (
    " How this brain is shared: through git. Pull before you start "
    "(`git pull --rebase`), save finished work as small commits named by area and "
    "push (see /save-brain). If a pull clashes, combine both sides in the file and "
    "delete every <<<<<<<, ======= and >>>>>>> line. Never force-push, never commit "
    "secrets or customers' personal data, never edit inside brain-system/."
)


CLOUD_SYNC_LINE = (
    " How this brain is shared here: this is a cloud run, so pull first, do the "
    "work, then commit and push to main (`git pull --rebase` then `git push`), as "
    "/save-brain says. If no credential can push to the repo, say plainly at the end "
    "that the work could not be saved. Never force-push."
)


def sync_line() -> str:
    """The cloud run's reminder when one is signalled, the everyday one otherwise."""
    return CLOUD_SYNC_LINE if os.environ.get("CLAUDE_CODE_REMOTE") == "true" else SYNC_LINE


def mount_state() -> str:
    """'ok', 'empty' (gitlink present but never initialized), or 'absent'."""
    if not MOUNT.exists():
        return "absent"
    if not any(MOUNT.iterdir()):
        return "empty"
    return "ok"


def pinned_tag() -> str:
    try:
        out = subprocess.run(
            ["git", "-C", str(MOUNT), "describe", "--tags", "--exact-match"],
            capture_output=True, text=True, timeout=5,
        )
        return out.stdout.strip() if out.returncode == 0 else ""
    except Exception:
        return ""


SCAFFOLD_LINE = (
    " This brain is scaffolded, not built: a `.scaffolded` file sits at its root, so "
    "most of the vault CLAUDE.md maps doesn't exist yet. Work from the sources in "
    "tool-map.md (brain-system/system/data-access.md), save what the team tells you into running-notes/ and brand-lens.md, and offer "
    "/set-up-brain when a full build would change the answer. The marker comes off "
    "on its own once a build finishes its first phase; don't delete it yourself."
)

BUILD_UNDERWAY_LINE = (
    " BUILD-STATUS.md sits at the root, so a build ran here. If it isn't marked "
    "complete, the build stopped partway: the docs it wrote so far are real, so use "
    "them, and offer /set-up-brain to resume the rest rather than start over. If it "
    "is marked complete, only the build's closeout is left; /set-up-brain finishes it."
)


def build_started() -> bool:
    """A build is under way while its status file sits at the root; the build
    archives it into prompts-run-log/ when it finishes. A run_id in
    brain_config.json alone doesn't count: setup tracking records it before
    Phase 0 creates BUILD-STATUS.md, so nothing was built yet."""
    return Path("BUILD-STATUS.md").exists()

state = mount_state()

# A submodule checkout carries a .git *file* inside the mount. Plain tracked
# files there mean one of two very different things: the team deliberately
# decoupled (/disconnect-factory stamps posture own-factory/independent in the
# ledger), or this is a legacy brain still carrying the old vendored copy and
# not yet migrated. Only the ledger's posture separates them — never assume
# decoupled without it.
is_submodule = (MOUNT / ".git").exists()


def decoupled_by_choice() -> bool:
    try:
        ledger = Path("running-notes/standard-sync.md").read_text(encoding="utf-8")
    except OSError:
        return False
    for line in ledger.splitlines():
        if "posture" in line.lower():
            return "own-factory" in line or "independent" in line
    return False


if state == "ok" and not is_submodule and decoupled_by_choice():
    context = (
        "Session start check: brain-system/ holds this team's own copy of the "
        "method (this brain is decoupled from the factory — no submodule, no pin). "
        "It is theirs to edit and versions with the repo. /update-brain runs in "
        "decoupled mode here, per running-notes/standard-sync.md." + sync_line()
    )
elif state == "ok" and not is_submodule:
    context = (
        "Session start check: brain-system/ carries the method as an older "
        "vendored copy (plain files, no submodule) — this brain predates the "
        "current layout and has not been migrated. That's fine to work with "
        "today, but don't edit inside brain-system/ (updates would overwrite "
        "it), and don't treat this as a decoupled brain. The current standard "
        "mounts the factory as a pinned submodule; /update-brain can offer the "
        "v1 migration that converts this brain." + sync_line()
    )
elif state == "ok":
    tag = pinned_tag()
    pin = f" (pinned to factory release {tag})" if tag else ""
    context = (
        f"Session start check: the brain-system/ method mount is initialized{pin}. "
        "brain-system/ itself is read-only; factory updates arrive only through "
        "/update-brain moving the pin." + sync_line()
    )
else:
    context = (
        "Session start check: the brain-system/ method mount is "
        + ("EMPTY — it was never initialized here."
           if state == "empty" else "MISSING.")
        + " The brain's prompts, craft knowledge, and system docs all live in that "
        "mount, so nothing method-driven will work until it is initialized. Fix it "
        "before anything else: run `git submodule update --init brain-system`, "
        "then verify the directory has content (a local operation; allowed and expected). The mount "
        "is read-only — never edit inside it; /update-brain is how it updates. "
        "Where to read more: this repo's README.md and CLAUDE.md, and the "
        "factory's own README inside the mount once initialized." + sync_line()
    )

if build_started():
    context += BUILD_UNDERWAY_LINE
elif Path(".scaffolded").exists():
    context += SCAFFOLD_LINE

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": context,
    }
}))

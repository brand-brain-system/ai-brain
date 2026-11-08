# Brand routines: the bundle every brain ships with

What makes a shipped brain *self-running*: the moment the brain's repo is cloned and opened in Claude Code, the guard and context hooks are live and the routine skills (dreaming, self-improvement, idea
cycle, refresh, research, standard updates) are ready to run on demand or on a schedule. Origin: Parker's brand-routines bundle, adapted: no desktop-sync guard, no Codex twin, no usage logging, git is
how the brain is shared.

## What is in here, and where it lands in a brain

- **`claude/`** → the brain's **`.claude/`** (the dot is added when stamped, because a dot-folder at this path would be treated as configuration of the factory itself). Contents:
  - `settings.json`: the committed brain configuration. Permission rules keep `brain-system/` read-only; four hooks run through `hooks/run-hook.py` from the repo root, in bash on every platform, with `python3` or `python` whichever works
  - `hooks/`: `run-hook.py` (the launcher), `session-start.py` (checks the method mount is initialized and says how the brain is shared), `craft-context.py` (injects the live doc catalog every turn, bounded to 16 KB), `mount-guard.py` (blocks shell and file-tool writes into `brain-system/`), `pull-log.py` (records which data tools a session used, for the grounding check)
  - `skills/`: the eleven routine skills: `dream`, `self-improve`, `research-loops`, `update-brain`, `harvest-ideas`, `evaluate-ideas`, `refresh-context`, `save-brain` (how the brain is saved through git), `disconnect-factory`, `setup-routines`, `get-started`
- **`schedules/`** → the brain's **`schedules/`**: the six routine recipes (task, cadence, reads and writes, delivery, status, origin) plus the folder README. These are repo-native routines, not
  automations on a hosted product surface (`brain-system/system/schedules.md`). They ship as `status: not-yet-registered`; `/setup-routines` arms them per account

`scripts/scaffold-brain.py` copies these verbatim at scaffold time, and `scripts/sync-executable-layer.py` re-syncs them on every pin bump. Copies are verbatim on purpose: a team edit to a copy
reads as the team's own and stops updating, so keep these files brand-neutral. Brand-specific rules go in the brain's own `CLAUDE.md`, `brand-lens.md` and `running-notes/`.

## Changing a hook or a routine

Change it here, run the tests (`python -m unittest discover -s tests`), and release it with a migration note. The hook behaviours are covered by `tests/test_runtime_hooks.py`.

## Read next

- `brain-system/system/schedules.md`: repo-native routines vs automations elsewhere
- `brain-system/system/refresh-cadence.md`: how often each standing doc is re-run
- `brain-system/system/factory-and-brains.md`: the mount, the pin, the update path

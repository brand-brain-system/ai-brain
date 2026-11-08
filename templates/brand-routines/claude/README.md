# .claude: what makes the brain self-running

Open the brain's folder in Claude Code and everything here is live immediately: the hooks, the permission rules and the skills. Nothing needs setting up by the team except arming the schedules
(`/setup-routines`). Origin: Parker's .claude bundle, adapted for brains shared through git.

## What is here

| Piece | What it does |
|---|---|
| `settings.json` | Committed brain configuration. `permissions.deny` keeps `brain-system/` read-only. Hooks run in bash on every platform through the launcher, using `python3` or `python`, whichever works (on Windows `python3` is often a Store stub) |
| `hooks/run-hook.py` | The launcher: finds the brain's root from any folder and runs the named hook; a silent no-op outside a brain or a nested repo |
| `hooks/session-start.py` | SessionStart. Catches an empty or missing `brain-system/` mount (the fix is `git submodule update --init`), says how the brain is shared (pull, small commits, push; `/save-brain`), and notes if the brain is scaffolded but not built or mid-build |
| `hooks/craft-context.py` | UserPromptSubmit. Injects the live doc catalog from `brain-system/creative-strategy-context/expertise-routing.md` plus the user's profile if there is one, bounded to 16,000 bytes; falls back to a plain pointer if the catalog is missing |
| `hooks/mount-guard.py` | PreToolUse on Bash. Blocks shell writes into `brain-system/` (redirects, `rm`, `mv`, `cp`, `tee`, `sed -i`, Windows `copy` and `del`) while letting reads and mount operations (`git -C brain-system fetch`, its pin `checkout`) through. The file-edit tools are covered by the deny rules in `settings.json` |
| `hooks/pull-log.py` | PostToolUse on connected-tool calls. Records which data tools a session used, so the grounding check can tell a fresh read from a remembered one |
| `skills/` | The eleven routine skills below, which sit next to the craft skills copied from the factory |
| `settings.local.json` | (gitignored, you create it) instance-specific overrides: tool connections, model, theme. **Never commit secrets or connections** |

## The routine skills

`dream` (propose changes from recent work), `self-improve` (dispose of proposals and feedback), `research-loops` (open loops to hypotheses to validations), `update-brain` (offer a newer factory
release), `harvest-ideas` and `evaluate-ideas` (fill and rank the idea bank), `refresh-context` (re-run stale docs), `save-brain` (the git procedure), `disconnect-factory` (decouple from factory
updates, on request), `setup-routines` (arm the schedules), `get-started` (the walkthrough for a new person).

The schedules for the six routines are in `../schedules/`; `/setup-routines` registers them per account.

## Rules for this folder

- The hooks and routine skills are copied from the factory and re-synced on every pin bump. Don't edit them in a brain; change the factory
- A hook that fails must fail quiet (exit 0, no output) unless it is blocking something on purpose
- Keep the settings brand-neutral; brand rules belong in the brain's `CLAUDE.md`

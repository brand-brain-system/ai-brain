---
name: improve-factory
description: Improve the factory itself from what the owner hands in (improve-factory, improve the factory, add these tips to the system, here are some tips, implement this in our brand brain system, new method, update the factory, factory map, how does the factory work). Loads a ready map of the factory instead of exploring the repo again, splits each source into its claims, checks every claim against what the factory already says, decides the one home for each, builds with parallel agents from a shared contract, then wires and releases it as vN. Factory only; never runs inside a brain.
triggers:
  - improve the factory
  - add these tips to the system
  - here are some tips
  - implement this in our brand brain system
  - new method
  - update the factory
  - factory map
  - how does the factory work
---

# Improve the factory

The owner hands in practitioner material (posts, prompts, an infographic, a video, a PDF) and asks for the factory to get better from it. This skill turns that into a release: the right
changes, each in its one home, wired and tested, with a migration note brains can apply.

It runs **in the factory repo only** (`Brand-brain`, wherever it is cloned). If the working folder has a `brain-system/` mount or the path contains `brain-system/`, stop: you are in a
brain. Use `expert-signal-intake` there instead.

## Which skill

| The ask | Skill |
|---|---|
| A source should change the method for every brand (a new method doc, skill, process, rule, script) | **improve-factory** (this one) |
| A source should change one brand's brain (its expert insights, context docs, lens) | `expert-signal-intake`, run inside that brain |
| One existing rule or prompt needs tightening, and the change must reach every file that inherits it | `update-parker-skill` (its `tighten-rule` process); this skill may call it for one item |
| Brains that carry the method as copied files need the new release pushed in | `propagate-craft`, after this skill has released |

When in doubt: if the change would hold for any brand, it belongs here. If it names a brand, a customer or an account, it does not (factory `CLAUDE.md`).

## Step 0: load the map, do not explore

Run these two reads before anything else, and work from them:

1. `python scripts/factory-map.py` (or `--section skills|docs|system` for one part). It prints the release state, the last commits, every skill with its job and processes, every method
   doc with its summary, agents, system docs, prompt folders, the brain scaffold, scripts, tests, and how full the craft catalog is against its 16,000-byte cap.
2. `CLAUDE.md` (the factory rules 1-8).

Open other files only when a step below names them, or when a claim needs a closer look. Do not walk the tree folder by folder. If the map is missing something you needed, note it in
`feedback.md` so the script can learn it.

## The flow

Each step has one process file. Run them in order. Stops are marked.

| Step | Process | Output |
|---|---|---|
| 1 | `processes/intake-sources.md` | A working copy of each source in the scratchpad, and one line per distinct claim |
| 2 | `processes/map-against-factory.md` | A coverage table: covered, partly covered, new, conflicts, with the file for each |
| 3 | `processes/decide-homes.md` | One home per item, rule or method to try, and the owner's answers. **STOP: the owner approves the plan** |
| 4 | `processes/build-with-agents.md` | A contract file, then the new files from parallel builders, and their proposed edits to existing files |
| 5 | `processes/wire-and-release.md` | Catalog rows, pointers, scaffold, tests, migration, release notes, VERSION, commit, push. **STOP: ask before the tag** |
| 6 | `processes/visual-map.md` | The workflow page updated and republished, when the release changed the workflow |

## Rules that hold in every step

- **Sources are never stored in the repo.** Working copies live in the session's scratchpad. The factory never pastes someone's text unchanged; it rewrites the method in its own words
  and labels each claim Stated (`system/evidence-and-labels.md`). Credit by name is not needed (the owner decided this); write "a practitioner's post (Nov 2026)" or similar
- **One home per rule.** A rule lives in one file and other files point to it (`system/system-of-records.md`)
- **Rule 6 before rules.** A new rule starts as an open test in a skill's `feedback.md`. It moves into the rules only after it held on a second brand
- **Parker material** is credited and adapted (`NOTICE.md` section C, `third-party/parker/MANIFEST.md`)
- **Nothing brand-specific.** Test brands are described ("the golf test brand"), never named
- **Pushes go without asking; the tag does not.** Commit and push when the work is done. Ask before creating or pushing the tag `vN`, before a force push and before a merge
- **Machine load.** Wide sweeps go to sub-agents; heavy jobs run at low priority (rule 7)

## Feedback

Log every run in `feedback.md`: what was handed in, what shipped as which release, what was slow, what the map missed. It is a log, not a rulebook.

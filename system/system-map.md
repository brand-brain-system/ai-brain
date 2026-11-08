---
summary: "A one-page map of the whole system: factory and brains, what loads when, the phases, the skills, the learning loop and the routines, with the system doc that owns each."
---

# System map

Situational awareness for anyone (or any session) working in a brain. It names the layers and points to the doc that owns each; it does not repeat them. Origin: replaces the assistant's system map, which
described the assistant's product architecture (per-user memory, chat history, a hosted data layer). Update the row in the same change as the thing it describes.

## The layers

| Layer | What it is | Owned by |
|---|---|---|
| **Factory** | The shared method: skills, prompts, craft docs, templates, scripts. Mounted read-only in every brain at `brain-system/`, pinned to a release | `factory-and-brains.md`, `brain-scaffold.md` |
| **Brain** | One repo per brand: its profile, lens, personas, competitors, strategy, ideas, sprints, learnings. Shared through git | `master-file-structure.md`, `save-brain` |
| **Skills** | Copied into the brain's `.claude/skills/`; craft skills (hooks, headlines, scripts, ads, video, pages) and routine skills (dream, refresh, research, update) | `skills-catalog.md` |
| **Method docs** | The craft knowledge the skills and answers draw on: `brain-system/creative-strategy-context/`, catalogued in `expertise-routing.md` | `scripts/build-doc-map.py` |
| **Data** | What the brain reads: exports, public pages, connected tools, by route | `data-access.md`, `tool-roles.md`, the brain's `tool-map.md` |
| **Evidence rules** | Four labels, the audit by a second agent, the proof inventory wall, the two review gates | `evidence-and-labels.md`, `attribution-principle.md` |

## What loads when

At the start of a session: the brain's `CLAUDE.md`, `brand-profile-narrative.md`, `running-notes/brand-notes-from-org.md` and `running-notes/refresh-schedule.md`. Before any copy: `brand-lens.md`. When a
task names a craft: the doc catalog (injected every turn by the `craft-context` hook) points to the method docs; the skill's `SKILL.md`, then `strategy.md`, then one process file. Nothing is read "just
in case". The routing rules are in the brain's `CLAUDE.md`.

## The three phases

Audit (what is true), strategy (what to lead with), ideas and briefs (what to make); then the loop of making, measuring and learning. A person can start anywhere; the phases run silently underneath.
`three-phase-operating-model.md`.

## The learning loop

`running-notes/missing-context.md` → `open-loops/` → `hypotheses/` → `validations/` → `re-validations/`. A person confirms every verdict. `open-loops-system.md`.

## Routines

Written in `schedules/`, armed per account with `/setup-routines`: context refresh, dreaming, idea cycle, research cycle, standard updates, self-improvement; plus the data routines (site watch,
competitor ad watch, customer-language pull, season heads-up, brain hygiene, weekly creative report). `schedules.md`, `refresh-cadence.md`.

## Where records live

Every fact has one home, and other files point to it. `system-of-records.md` lists the homes.

## Skills

Craft and production skills are in `.claude/skills/` (`skills-catalog.md` has status). Planned or not yet imported are listed in the factory's `REWRITE-QUEUE.md`.

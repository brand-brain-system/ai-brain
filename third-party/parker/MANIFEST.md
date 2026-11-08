# Parker material in this factory

Source: `github.com/real-simple-labs/parker-brain`, release v39, commit `2a6f6c6` (read 12 Oct 2026). Licence text: [`LICENSE.md`](LICENSE.md) (PolyForm Noncommercial 1.0.0). The authors have said, on their course, that
participants may use it freely; see `NOTICE.md`, section C. Keep this folder, the licence copy and the attribution lines with any Parker file that is passed on.

The files below are kept under Parker's own names so that cross-references inside them still work and a later version can be diffed against upstream. Files marked *modified* were changed for this factory;
everything else is as Parker published it, apart from the one global change below.

**Global change in every file:** the mount name `parker-system/` became `brain-system/`.

| Here | From (in parker-brain) | Notes |
|---|---|---|
| `scripts/voice-lint.py` | `scripts/voice-lint.py` | *Modified 24 Oct 2026:* Danish patterns added (marked "(da)"), tests in `tests/test_voice_lint.py`. *7 Nov 2026 (v19):* nine English and eight Danish families after FeedHive's ai-slop-detector (`third-party/open-source-skills/`). The earlier English patterns as published |
| `scripts/grounding-check.py` | `scripts/grounding-check.py` | *Modified:* curly quotes count as straight; reads `.md`, `.txt`, `.csv`, `.json`; skips `sprints/` (our outputs) |
| `.claude/agents/context-grounding-review.md` | `.claude/agents/` | As published |
| `.claude/agents/creative-voice-review.md` | `.claude/agents/` | *Modified 24 Oct 2026:* one line pointing to the "Danish copy" section. Rest as published |
| `creative-strategy-context/*.md` (45 docs) | `creative-strategy-context/` | As published. Subfolders (`expert-insights/`, `gifting/`, `old-ads/`, `parker-taste/`) not imported, so a few cross-references dangle |
| `creative-strategy-context/ai-writing-tells.md` | `creative-strategy-context/` | *Modified 24 Oct 2026:* "Danish copy" section added (factory-written, a judgment from observation). *7 Nov 2026:* family 13 (leftovers, asides, post formulas). Rest as published |
| `creative-strategy-context/legal-ai-ugc.md` | `creative-strategy-context/` | *Modified 7 Nov 2026:* "EU and Denmark" section (AI Act art. 50, read in the Commission's FAQ; the Danish likeness proposal), shorter summary, scope line. Rest as published |
| `creative-strategy-context/adapting-scripts.md` | `creative-strategy-context/` | *Modified 7 Nov 2026:* "The shot sheet" in step 2 (factory text). Rest as published |
| `creative-strategy-context/{meta-creative-playbook,gifting-and-q4-creative,creator-briefs,advertising-luxury-and-higher-price-points,new-product-launches,creative-strategy-by-brand-size,static-ad-design,seasonality}.md` | `creative-strategy-context/` | *Modified 7 Nov 2026:* the frontmatter `summary` shortened so the craft catalog fits the hook's allowance. Bodies as published |
| `creative-strategy-context/{gifting-and-q4-creative,seasonality,ad-account-analysis}.md` | `creative-strategy-context/` | *Modified 22 Oct 2026:* pointers to our `black-friday-and-q4-data.md`; practitioner claims on gifting content and evergreen-vs-sale relabelled Stated beside the cross-brand data; "The day-7 read" added to `ad-account-analysis.md` (marked as factory text) |
| `creative-strategy-context/ad-formats/**/index.md`, `README.md` | `creative-strategy-context/ad-formats/` | As published |

### Stage 1 of Parker v1.1 (branch `parker-v1.1`, 12 Oct 2026), all as published apart from the global change

| Here | From | Notes |
|---|---|---|
| `prompts/**` (incl. `onboarding-runner.md`, `README.md`) | `prompts/` | Replaces our placeholder README |
| `.claude/skills/<23 skills>` | `.claude/skills/` | ad-account-analysis, ai-ad-generation, brand-idea-bank-maintenance, dream, evaluate-ideas, expert-signal-intake, harvest-ideas, headlines, hooks, improve-system, iterations, open-loops-advance, open-loops-validate, propagate-craft, recreate, refresh-context, scriptwriting, self-improve, self-improvement-intake, set-up-brain, setup-routines, update-parker-skill, weekly-creative-report |
| `templates/brand-routines/**`, `templates/*.md` | `templates/` | Routine skills, hooks, brain settings, schedules, doc templates |
| `system/*.md` (12 docs) | `system/` | All except the three below |
| `third-party/parker/system/{master-file-structure,brain-scaffold,growing-the-brain}.md` | `system/` | Parked: same names as ours; to be merged |
| `scripts/{sync-executable-layer,sync-open-loops-core,build-doc-map,usage-log}.py`, `scripts/propagate-to-brand-brains.sh` | `scripts/` | |
| `third-party/parker/scripts/{scaffold-brain,cloud-run-git}.py` | `scripts/` | Parked: name clash with ours / Parker's cloud backend |
| `.claude/skills/scriptwriting/` | same | *Modified 24 Oct 2026:* added `processes/script-from-cross-niche-story.md` (ours), three triggers in `SKILL.md`, one row each in `processes/INDEX.md` and `strategy.md`, and a `feedback.md`. Rest as published |
| `tests/*.py`, `fixtures/**`, `.github/workflows/*.yml` | same | Not yet adapted: tests target Parker's scaffold and will fail until stage 3 |

Not imported: `migrations/` and `release-notes/` (Parker's own history), `self-improvement/` (their traces), `.codex/`, `.agents/`, `AGENTS.md`, the `parker` output style, and the `creative-strategy-context/` subfolders.

## How to adapt a Parker file

1. Change it in place and say so in the "Notes" column here (*Modified: what and why*)
2. Remove dependencies on Parker's product (the Parker MCP, Parker Desktop, per-user chat history) or replace them with our tool roles (`system/tool-roles.md`)
3. Use our paths, our four evidence labels and our stop-for-a-person rules
4. Once a file has changed enough that it is ours, move it out of this table and note it as "now original"

# Master file structure

The canonical tree of a brand brain, what loads when, and the rules for growing it. The empty version is `templates/brand-scaffold/`; a brain's own `CLAUDE.md` carries the short layout table.

## Loading sequence

1. **Always, at the start of a session:** `brand-profile.md`, `running-notes/brand-notes-from-org.md`, `running-notes/refresh-schedule.md` (so a stale page is flagged without opening it), the brain's `CLAUDE.md`
2. **Before any copy:** `brand-lens.md` (voice, claims gate, proof inventory)
3. **When a team is active:** `teams/<team>/profile.md` and any `sub-context-docs/` the picked skill names
4. **When a skill runs:** its `SKILL.md`, then `strategy.md`, then the one process file the situation calls for, then only the components that process names
5. **Customer-facing skills also load** `personas/voice-of-customer/voice-of-customer.md` and filter by the persona and signal the task targets

Nothing else is read "just in case". The point of the structure is that a task can name exactly what it needs.

## The tree

```
<brand>/
├── CLAUDE.md                    the brain's rules and layout (the brain's own; never overwritten)
├── README.md                    the brain in one minute, fill order, completeness
├── .brain-version               which factory release built this
├── brand-profile.md             MAIN: the brand in one read
├── brand-lens.md                voice · claims gate · proof inventory · anti-language · what has worked
├── working-thesis-synthesis.md  what we believe about the brand's state, and how sure
├── brand-context/               the one-page Brand DNA export (generated)
├── sub-context-docs/            FOUNDATION: 11 docs every team reads
│     brand-identity-analysis · operations-and-team · website-and-product-audit ·
│     organic-channels-inventory · performance-targets-and-metrics · reputation-analysis ·
│     community-and-forums · customer-journey-and-persona-discovery ·
│     category-and-market-research · competitive-landscape · marketing-calendar-and-campaigns
├── personas/
│     personas-profile.md (MAIN) · persona-voice-library.md · lifecycle-journey-maps.md ·
│     brand-self-echo-detection.md · cross-persona-bias-notes.md
│     sources/                   one doc per evidence source (reviews, ad account, ad comments, surveys, forums...)
│     voice-of-customer/         voice-of-customer.md (MAIN) · voc-corpus-profile.md · phrases/ (9 types)
├── competitors/<rival>/         competitor-snapshot.md (MAIN) + sub-context-docs/ (9 pages) + teardown/ (how they grew)
├── teams/<team>/                8 teams: creative-strategy · performance · organic-social · search ·
│     profile.md                 influencer · brand-pr-comms · partnerships · retention
│     sub-context-docs/ · internal/ (this brand) · external/ (rivals) · landscape/ (category)
├── strategy/                    strategic-roadmap · offer-brief · product-priority · 3 strategy inputs · growth-plan
├── idea-bank/                   index.md (idea index) · concepts.md (concept register) · entries/ · evaluation-<date>.md
├── sprints/<date>-<slug>/       sprint-plan.md · briefs/ · ads/ · video/ · landing-pages/ · retro.md
│     _unplanned/briefs/         ad-hoc briefs with no planned round
├── briefs/_templates/           the six brief types
├── open-loops/ · hypotheses/ · validations/ · re-validations/      the learning pipeline
├── running-notes/               current-work · missing-context · brand-rules · success-definition ·
│                                brand-notes-from-org · org-and-usage · refresh-schedule · recent-validations · feedback
├── schedules/ · scripts/        routines written down, and the scripts they use
├── source-pulls/ · audits/      raw dated data · dated analysis runs
├── research-map/                quotes, groups and the ranked map.html
├── lifecycle/                   consent audit · flow map · flows/ (email and SMS drafts) · results
├── search-visibility/           prompt portfolio · runs.csv · readouts · fix list (AI answers and search)
├── expert-insights/ · dreaming/ · workflows/
├── assets/ · showcase/ · tool-map.md
├── brain-system/                the factory, mounted read-only at a pinned release
└── .claude/                     skills (copied from the factory) · settings
```

## Why it is shaped this way

- **Foundation, then views.** The 11 foundation docs hold facts about the brand; teams, strategy and ideas are views and decisions built on them. Change a fact once, in its home
- **Main files and satellites.** A folder has one MAIN file a reader opens first (`brand-profile.md`, `personas-profile.md`, `competitor-snapshot.md`) and satellite files for depth
- **Internal, external, landscape.** Audits inside a team are filed by what they are about: this brand, its rivals, or the category
- **Learning is a pipeline, not a pile.** Questions, guesses and verdicts live in different folders so you can see what is still unknown
- **Dated, never edited.** Raw pulls and audit runs are dated and kept as they were; analysis points to them

## Growing the tree

The tree is the core, not a closed set. A brand with email, SEO, PR or support work adds a first-class surface when someone will read it: a folder with a `README.md` saying what it holds, what fills it
and how often it is refreshed, a line in the brain's `CLAUDE.md` layout table, and a row in `running-notes/refresh-schedule.md`. If the surface is useful to every brand, propose it for the
scaffold instead (`system/growing-the-brain.md`).

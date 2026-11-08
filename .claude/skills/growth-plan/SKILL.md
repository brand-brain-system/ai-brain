---
name: growth-plan
description: Build a brand's whole-funnel marketing plan for the next 90 days and 12 months (growth-plan, marketing plan, vækstplan, markedsføringsplan, holistic plan, channel plan, "what should we do beyond Meta", 90-day plan, annual plan, fractional CMO plan). Scores where the brand stands at each stage of the customer journey (reach, convert, repeat, recommend, measure) from evidence in the brain, checks the unit economics, picks three bets, sequences a 90-day roadmap and a quarterly outlook around the brand's season calendar, and routes every move to the skill that does it, with a leading indicator and a kill criterion. Reads the strategic roadmap; doesn't replace it. Use when someone asks for a marketing plan, a growth plan, what to prioritise across channels, or where the brand is weakest outside paid social.
---

# Growth plan

Always run inside the brand's brain folder. The strategic roadmap (`strategy/strategic-roadmap.md`)
decides who to win and what to say in ads. This skill zooms out: **across the whole journey from
stranger to repeat buyer, where is the brand weakest, and what do we do about it, in what order?**
Paid social is one channel in it, not the whole plan.

Structure built on Corey Haines' open-source `marketing-plan` skill (MIT, credited in
`brain-system/third-party/marketingskills/MANIFEST.md`): stage-tagged moves, a scored current state,
a 90-day and 12-month horizon, and "every move names its mechanism and its leading indicator". Cut
from a SaaS plan to a DTC brand in Denmark and wired to our skills; the funding-stage budget tiers and
SaaS growth benchmarks are not used.

## Where the knowledge lives

| File | Answers |
|---|---|
| `SKILL.md` (this file) | The steps and what must never happen |
| `rubric.md` | How to score each stage 0-5, and what evidence each score needs |
| `plan-template.md` | The shape of `strategy/growth-plan.md` |
| `feedback.md` | What we've observed. A log, not a rulebook |
| `brain-system/creative-strategy-context/measurement-and-attribution.md` | How to read the numbers the plan is judged by |
| `brain-system/creative-strategy-context/offer-design.md` | The offer levers |
| brain: `strategy/` | The roadmap, offer brief and product priority this plan sits beside |
| brain: `running-notes/success-definition.md`, `brand-rules.md` | The business goal, the north star, margins if given |
| brain: `sub-context-docs/` | The eleven foundation reads (performance targets, marketing calendar, organic channels, website, reputation, operations and team) |

## Prerequisites
- **A built brain.** At least the foundation docs, personas and one ad-account read. Without them the
  plan is generic, which this factory counts as a failed answer. If the build hasn't run, say so and
  offer `/set-up-brain` first
- **The goal** from `running-notes/success-definition.md`. Missing: ask the human for the one business
  number the next 12 months are judged by (revenue, new customers, contribution margin) before step 1
- **What the team can actually do:** people, hours, agencies, monthly budget by line. Ask; a plan the
  team can't run is fiction. The answers go in `running-notes/brand-notes-from-org.md`, dated

## The steps

**1. Gather.** Read the brain across the stages (the table in `rubric.md` names the docs per stage),
plus `lifecycle/`, `search-visibility/`, `competitors/*/teardown/` and `research-map/` where they
exist. List what's missing per stage: a stage with no evidence is scored Data-limited, never guessed.

**2. Unit economics.** From the brand's own numbers only: average order value, gross margin,
new-customer cost (all spend ÷ new customers, from the store), repeat rate within the brand's window,
and what a customer is worth over 12 months. Each with its source and window. If margins aren't
shared, say what can't be judged (whether a discount or a channel pays) and carry on.

**3. Score the current state** per `rubric.md`: each stage and sub-area 0-5, one line of evidence, the
label. The lowest-scoring stages with the biggest business weight are where the plan goes.

**4. STOP: approve the diagnosis.** Show the scores, the economics and the gaps. The human corrects
what they know better; corrections are Stated by the brand and noted.

**5. Three bets.** The three moves that would most change the goal in 12 months, each tied to a weak
stage. For each: the mechanism (why it would work, in one sentence), the evidence, the cost and the
first proof point. Name the roads not taken and why (`strategy/strategic-roadmap.md` has a "roads not
taken" habit; follow it).

**6. The 90-day roadmap.** Weeks 1-2 **unblock** (tracking, consent, the offer basics, anything that
makes later work count), weeks 3-6 **foundation** (the flows, the pages, the fixes), weeks 7-12
**pace** (the repeatable work at a steady cadence). Each move: stage, owner, the skill that runs it,
the leading indicator, the kill criterion, and the date it's checked. The brand's season calendar
(`sub-context-docs/marketing-calendar-and-campaigns.md`, and `season-report` before Q4) is laid over
it so no move collides with a sale.

**7. The 12-month outlook.** One block per quarter: the milestone, which bet it advances, what has to
be true to move on, and the season it lands in.

**8. Plays to skip.** What looks tempting but the evidence, budget or Danish rules don't support. A
plan without a skip list hasn't made choices.

**9. STOP: approve the plan,** section by section, then write `strategy/growth-plan.md` per
`plan-template.md`. Each move that is a question, not a known fix, becomes an open loop
(`brain-system/system/open-loops-system.md`); each concept goes to the idea bank. Add the plan to
`running-notes/refresh-schedule.md` with a 90-day re-score.

**10. Re-score** after 90 days with the same rubric: which scores moved, which moves were killed and
why. A plan is a set of bets; say plainly which lost.

## Routing (which skill runs which move)

| Stage | Skills and docs |
|---|---|
| Reach: paid social | `ad-account-analysis`, `static-ads`, `video-edits`, `motion-ads`, `hooks`, `scriptwriting`, `iterations`, `season-report` |
| Reach: search and AI answers | `ai-search` |
| Reach: creators and organic | `creator-recruitment`, `harvest-ideas`, `brain-system/creative-strategy-context/organic-social-analysis.md` |
| Reach: rivals and openings | `competitor-teardown`, `persona-gap` (Mode B) |
| Convert: pages and offer | `new-landing-page`, `iterate-landing-page`, `cro-review`, `page-qa`, `brain-system/creative-strategy-context/offer-design.md`, `offer-ads` |
| Repeat | `lifecycle-flows` |
| Recommend | `lifecycle-flows` (review request), `creator-recruitment` (customers as creators) |
| Measure | `brain-system/creative-strategy-context/measurement-and-attribution.md`, `weekly-brain-report` |
| Customer understanding (all stages) | `research-map`, `persona-gap` (Mode A) |

A move with no skill behind it (PR, a retail deal, a referral program, a site rebuild) is written as a
task for a named person, with the same indicator and kill criterion. Don't invent a skill for it.

## Guardrails (never)
- Never invent a number: no market size, benchmark, margin, budget or forecast without a source. A
  projection is a range with its assumptions, labelled Inferred
- Never commit spend, hire, or sign anything; the plan proposes, people decide
- Never let the plan override the approved strategic roadmap. If the evidence says the roadmap is
  wrong, raise it as a finding for the roadmap's owner
- Never a move without a leading indicator and a kill criterion ("post more and hope" is not a move)
- Never a plan bigger than the team's stated capacity: if it doesn't fit, cut, and say what was cut

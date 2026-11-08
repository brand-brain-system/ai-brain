---
name: account-playbook
description: The start-to-finish plan for a brand whose Meta ad account we just got access to (account-playbook, new ad account, new client, we got access to the ad account, onboard an ad account, where do we start, ny kunde, start-to-finish plan, scale the account). Runs the existing skills in order through nine stages, from read-only access and a tracking check to the account read, winner breakdowns, market mining, the angle bank and gap matrix, the test plan, making the ads, and the weekly and monthly loops. Each stage has entry criteria, a skill, an output file, a stop for a person and an exit check, and the progress lives in running-notes/playbook-status.md. Does no analysis or writing itself, and never launches, pays for or changes anything in the ad account. Use after set-up-brain when someone asks what to do with a new ad account, where to start, or where a brand stands in that plan.
argument-hint: "[optional: 'status', or a stage number to jump to]"
---

# Account playbook: from ad-account access to a scaling system

The front door for one question: "we have a new brand and access to its Meta ad account. What
exactly do we do, start to finish?" This skill does not do the work. It runs the other skills in
the right order, stops for a person at each decision, and keeps one progress page true.

**Source:** built for v20 from practitioners' posts (Nov 2026) on finding new angles with the ad
account, angle banks and feedback loops, fitted to the skills we already have.
**Status:** *Written.* The order is Stated, not yet run end to end on a brand. Open test in
`feedback.md`.

## Before you start

1. **Is there a brain?** If `brain_config.json` is missing, or `.scaffolded` or a root
   `BUILD-STATUS.md` is still there, the brain isn't built. Route to `/set-up-brain` and come back
   when it hands off. A built brain starts here
2. **Read `feedback.md`** in this skill for open tests
3. **Read `running-notes/playbook-status.md`.** If it's missing (a brain older than v20), copy
   `brain-system/templates/brand-scaffold/running-notes/playbook-status.md` there and put the
   brand name in the title
4. **Pick the entry point and the pace** with `strategy.md`

## How a run goes

1. **Find the current stage:** the first stage on the status page that isn't `done` or `skipped`.
   Check its entry criteria in its process file. If they aren't met, the missing piece is the next
   action
2. **Show the person where they are,** in four lines: the stage, what's done, open stops, the next
   action. Plain words, no tour
3. **Run the next stage's skill, or offer to.** The process file names the exact skill and
   process. One skill at a time. Each skill runs with its own `SKILL.md`, its own stops and its own
   feedback log; this skill never restates their rules
4. **Update the status page after every skill run:** status, dates, the output link, open stops
   and the "Next action" line at the top
5. **Close a stage when its exit check passes:** mark it `done` with the date, write the next
   action, then save the brain as `/save-brain` says (a small commit named by area,
   `git pull --rebase`, `git push`, never force). The brain repo is on GitHub; data stays in the
   brain, never in the factory
6. **Stop at every human stop.** Ask through the question form, as `/set-up-brain` does, so the
   person gets notified. Mark a waiting stop on the status page under "Open stops"

Stages can overlap. Stage 3 needs no account data and can start on day 1 while Stages 1 and 2 run,
or before access arrives. The days are targets from the day access is granted (day 0), not
deadlines.

## The stages

| # | Stage | Days | Calls (skill: process) | Output in the brain | Stop | Exit check |
|---|---|---|---|---|---|---|
| 0 | Access and measurement | 0-2 | `ad-account-analysis`: `measurement-check`; `creative-leaderboard`: `naming-setup` | `tool-map.md` (Ad account row, Data routes); `audits/measurement-check-<date>.md`; winner and north star in `running-notes/brand-rules.md`; `running-notes/ad-naming.md` if the brand keeps its own names | A person connects the account and signs in; the strategist confirms the winner definition | Route written and checked; measurement read is "usable" or "usable with a caveat"; winner definition and naming settled |
| 1 | Account read | 1-3 | `ad-account-analysis`: `account-audit`, last 90 days | `audits/<YYYY-MM>/account-audit-<date>.md` | None, unless the measurement read was "not usable" | Audit saved with winners by the brand's definition, a structure note, the spend band and a monthly ad target |
| 2 | Winner breakdowns | 2-5 | `ad-breakdown`: `batch-winners` | `audits/breakdowns/<date>-<ad-slug>.md`; rows in `angle-bank/ad-tags.csv` | The strategist writes their own hypothesis before seeing each breakdown | Every winner has a breakdown and a tag row; "what the account scaled on" is written |
| 3 | Market mining and personas | 3-10 | `angle-bank`: `mine-market`; `research-map`; `persona-gap` Mode A (if needed) and Mode B | `source-pulls/`; `research-map/map.html`; `personas/personas-profile.md`; `audits/<YYYY-MM>/persona-gap-<date>/` | The strategist approves the research-map groups; Mode A's independent audit | Quote bank with source links; personas evidenced; own and rival ads tagged against them |
| 4 | Angle bank and gap matrix | 7-12 | `angle-bank`: `build-bank`, `map-account`, `gap-matrix` | `angle-bank/angles.csv`; `angle-bank/gap-matrix-<date>.md` and `.html` | The strategist agrees the top 5 gaps or changes them | Every angle has a persona, an awareness level and a quote; top 5 gaps named |
| 5 | Strategy and test plan | 10-14 | Phase 2 roadmap prompts; `angle-bank`: `next-tests`; `evaluate-ideas`; the sprint-plan prompt | `strategy/strategic-roadmap.md`; `sprints/<date>-<slug>/sprint-plan.md` | **STOP:** the strategist approves the plan and the budget split; prices shown before any spend | An approved plan: gaps picked, sprint size, test setup, budget split |
| 6 | Make | week 2-4 | Per concept: `scriptwriting`, `hooks`, `headlines`, `static-ads`, `video-edits`, `motion-ads`, `ai-ad-generation`; `creator-recruitment`; `brief-check`; `ad-policy-check` last | `sprints/<sprint>/briefs/`; `sprints/<sprint>/ads/` | Each skill's own stops; **STOP before launch:** the team launches, never Claude | Every ad passed `brief-check` and `ad-policy-check`, is named per the convention and handed to the team |
| 7 | Weekly loop | from week 3, every week | `creative-leaderboard`: `weekly-leaderboard`; `weekly-creative-report`; `iterations` Phase A; `ad-breakdown` on the best, `loser-breakdown` on the worst; `angle-bank` statuses; `harvest-ideas`, `evaluate-ideas` | `audits/leaderboard/<YYYY-Www>.md`; `audits/<YYYY-MM>/weekly-creative-report-<YYYY-WW>.html`; updated `angle-bank/angles.csv` | The report goes out only after a yes; renames and launches are the team's | The week's row on the status page is filled and the next batch is chosen from the leaderboard |
| 8 | Monthly loop and day-90 review | monthly; day 90 | `angle-bank`: `map-account`, `gap-matrix`; `persona-gap`; `ad-account-analysis`: `measurement-check`; `refresh-context`; `growth-plan` when ready | a new gap matrix; refreshed personas; the day-90 line in `feedback.md` logs | The strategist approves any change to the roadmap | The month's row is filled; at day 90 the top-5 result is logged |

Details per stage: `processes/INDEX.md`.

## What to say to the client

One line per stage, in the brain's language. Short and plain; adjust to the client.

| # | Line |
|---|---|
| 0 | "We have read-only access. First we check that your tracking counts right, because every later number rests on it." |
| 1 | "We're reading the last 90 days: what spends, what sells, and how the account is set up." |
| 2 | "We're taking your best ads apart to see why they won." |
| 3 | "We're reading what your customers say in their own words, to see who really buys and why." |
| 4 | "We're mapping which messages your buyers have heard and which they never have." |
| 5 | "Here is the test plan and the budget split. Nothing is made or spent until you approve it." |
| 6 | "We're making the ads. Each one is checked against Meta's rules before your team launches it." |
| 7 | "Every week you get what won, what's tiring and what we make next." |
| 8 | "Every month we redraw the map of gaps. At day 90 we check whether the gaps we picked became winners." |

## When access is partial

No live access and no export still leaves a plan: the public-only path in
`processes/stage-0-access.md`. Every number on that path is a labelled proxy.

## Rules

- **Orchestrate, don't do.** The work and its rules live in the skills this one calls. Point to
  them; never copy their rules here
- **Read-only on the ad account.** `ads_read` only, never `ads_management`. Claude never launches,
  pauses, renames, edits or changes a budget in the account. Renaming live ads is a hand-off to the
  team
- **No token, password or login in the brain repo or in chat.** The person who has the access
  signs in themselves
- **Stop for a person** before anything is sent, posted, published, launched or paid for, and show
  prices before spend (factory rule 4)
- **Meet the strategist where they are.** The stages are the order when the strategist hands us
  the account, not a gate (`brain-system/system/three-phase-operating-model.md`). If they ask for a
  script on day 2, write it and note it under "Run outside the order" on the status page
- **Label every claim** per `brain-system/system/evidence-and-labels.md`, and name every proxy
- **Keep the status page true.** It is the answer to "where are we" and what the next session
  resumes from
- **Light on the machine.** Heavy reads go to a small gathering agent; one heavy job at a time. Reads that don't need each other go out at once, each with a full brief (`brain-system/system/agent-teams.md`)

## Files

| File | What it is |
|---|---|
| `strategy.md` | Which entry point, and how fast to go by spend |
| `processes/INDEX.md` | The stage processes |
| `processes/stage-0-access.md` | Access, measurement, winner definition, naming; the Day 0 checklist; the public-only path |
| `processes/stage-1-2-read-and-breakdown.md` | The account read and the winner breakdowns |
| `processes/stage-3-4-angles.md` | Market mining, personas, the angle bank and the gap matrix |
| `processes/stage-5-plan.md` | Roadmap, picked gaps, test setup, sprint size, the approval |
| `processes/stage-6-make.md` | Shape, voice, the making skills, checks, naming, the hand-off |
| `processes/stage-7-8-loops.md` | The weekly and monthly loops and the day-90 review |
| `feedback.md` | The log, with the open test |
| brain: `running-notes/playbook-status.md` | The progress page (template in `brain-system/templates/brand-scaffold/running-notes/`) |

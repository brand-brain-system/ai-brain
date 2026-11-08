---
name: weekly-brain-report
description: Build the brand's weekly report as one clean, shareable page, from whatever data the brain has. The short version first (three things that matter), then what's working and dying in the account, competitors' moves and gaps, what customers are saying in their exact words, where the openings are (organic and affinity), and what to make next, with an optional blind-judging section. Every section is optional, every line carries an evidence label, and a section with no data says what it needs. Works from public data alone and gets sharper when an ad-account export is in the brain. Use when someone asks for the weekly report, the weekly read, the Monday report, the client report or the weekly creative strategy sprint.
---

# Weekly brain report

One page a strategist, a buyer or the brand's owner can read in five minutes. It is a template: the layout is fixed, the content comes from the brain's sources, and anything the brain can't see is shown as a
named gap instead of filled in. For the account-metrics report (north-star, trend, top creatives, tiring ads) see `weekly-creative-report`; this one is the wider creative read.

Origin: ours. The layout follows the weekly reports shown on the course (short version, working and dying, competitors, customer words, openings, what to make next); no text is copied.

## What ships with it

| File | What |
|---|---|
| `SKILL.md` | The steps and the rules |
| `schema.md` | The data file, section by section |
| `example.json` | A full example with a placeholder brand and made-up numbers, flagged on the page. Copy it as the starting point |
| `render_weekly.py` | Turns the data file into one HTML page (and a PDF with `--pdf`). Standard library only |

## Steps

1. **Find the brain and the week.** Work in the brand's brain. Name the week (Monday to Sunday) and read `running-notes/refresh-schedule.md` so a stale doc is flagged, not trusted
2. **Gather by route, not by tool.** For each section, read what `tool-map.md` says the brand can give (`brain-system/system/data-access.md`):
   - **Account:** the newest ad-account export in `source-pulls/`. None: mark the section `data_limited` and say what would fill it. Platform conversions and ROAS are the platform's claims; when the store's order count is in the brain it is the total, and the report never adds platforms together (`brain-system/creative-strategy-context/measurement-and-attribution.md`)
   - **Competitors:** the public ad library, per `persona-gap` mode B (what runs, formats, offers; ranks are impressions inside a start-date cohort, never sales). Compare with last week's read in `audits/`
   - **Voice of customer:** new reviews and comments since the last report, exact words with source and date; check them against `personas/voice-of-customer/`
   - **Openings:** organic outliers (public profiles) and affinity brands (ad library, other categories). End with a short "do not chase" list
   - **Next:** concepts from `idea-bank/` and the roadmap, each tied to a persona card and the evidence above
   - Use a small gathering agent for the reading and keep the judgment in the main session (`system/model-routing.md`)
3. **Read it like a strategist.** Triangulate: a finding on one surface is a candidate, on two or more it is a finding. Say what changed since last week and why it matters. Every point earns a "therefore"
4. **Write the data file** from `example.json`. Keep what you have, delete the sections you can't fill honestly (or mark them `data_limited` with `needs`). Quotes are exact and never shortened. Every item carries a label: Verified, Stated, Inferred or Data-limited (`evidence-and-labels.md`). Numbers carry their window and denominator
5. **Optional: blind judging.** For the concept shortlist, three independent agents judge each concept without seeing each other (track record, customer, assassin); survival needs 7 or more from at least 2 of 3. It is token-heavy: offer it, don't default to it
6. **Check it.** Run `scripts/grounding-check.py` on the data file against the brain (every quote traces to a file, every cited path exists) and `scripts/voice-lint.py` on the prose. Fix what fails
7. **Render and look.** `python3 brain-system/.claude/skills/weekly-brain-report/render_weekly.py report.json out.html --pdf` (or the copy in `.claude/skills/`). Open the page; check it at phone width. One render, no loop
8. **Save and share.** Put the data file and the page in `audits/<YYYY-MM>/` as `weekly-report-<YYYY-MM-DD>.json` and `.html`, commit and push (`/save-brain`). Say in one line where it is on GitHub and who should read it

## Rules

- **Invent nothing.** No number without a source and a date; a blank is "Data-limited" with what would resolve it
- **No performance claims from the ad library.** It shows what runs, not what works
- **Concept work is labelled** ("Concept, not commissioned by <brand>") in `meta.concept_label`
- **Nothing leaves without a person.** The report is a draft until a person approves it; sending it to a client is a person's act
- **Same layout every week.** Change the content, not the structure, so readers learn where to look. Change the layout only through a deliberate edit of the skill
- **Light on the machine.** One render per report

## Scheduling

A routine can run steps 1 to 8 weekly and push the result (`/setup-routines`), once the account export arrives on its own. Until then a person drops the export in the brain and asks for the report.

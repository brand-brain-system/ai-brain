---
name: season-report
description: Analyse a brand's last sale season from its own Meta data and turn it into this year's plan (season-report, Q4 report, Black Friday retro, Black Week analyse, sæsonrapport, julesalg, what did last Q4 teach us, plan Black Friday). Runs the cross-brand Q4 study on one brand (CPM by week, hit rate, when sale ads went on and off, how fast winners showed, new ideas vs new takes, deals, what won the sale week, audience shift, statics vs video, openers), sets each result beside the cross-brand number, writes a shareable report with a separate methods file, and ends with a dated plan for this year under the Danish price rules. Without an account export it runs a public-only plan from competitors' sale ads and the cross-brand data. Use before a big sale (Black Friday, Black Week, Christmas, Mother's Day, summer sale) or after one, when someone asks what last year's sale taught us, or for a Q4 plan. Does not make ads (offer-ads, static-ads) or the weekly report (weekly-creative-report).
---

# Season report

What last season can tell this brand about this one. The model is Parker's Q4 Ad Creative Report, a study of 432 brands (`brain-system/creative-strategy-context/black-friday-and-q4-data.md`); this
skill runs the same studies on one brand, in the same report form, and then turns them into a plan. Built 22 Oct 2026; not yet run on a brand.

One brand is a single "inside the brand" check by construction, so the trap the study guards against (big brands making an idea look good when everyone is added together) doesn't apply here. The trap
that does: small numbers. A brand with 300 ads in the season has about 30 winners. Every section says how many ads stand behind it.

## Files

| File | What |
|---|---|
| `strategy.md` | Which mode to run, and which sections to keep |
| `processes/data.md` | The export to ask for, and what each section can do without it |
| `processes/studies.md` | Every study, defined for one brand: the rule, the calculation, the threshold, the cross-brand number to set beside it |
| `processes/plan.md` | Turning the findings into this year's dated plan, under the Danish rules |
| `report-form.md` | The report form: two files, the section shape, the TL;DR and the limits |
| `template.html` | The page skeleton, filled in by hand |
| `feedback.md` | Generic lessons, a log |

## Steps

**0. Find the brain.** Run inside the brand's brain (`brand-lens.md` or `sub-context-docs/` in the folder). No brain: say the report runs from the brain and offer `/set-up-brain`. Never load another
brand's brain.

**1. Pick the season and the mode** (`strategy.md`). Default: last year's Q4, read for this year's Black Friday and Christmas. Name the windows with dates before pulling anything: the season (e.g. Oct 1
to Dec 31), the sale week, the comparison months, and this year's matching dates.

**2. Get the data** (`processes/data.md`). Check `source-pulls/` and `tool-map.md` first. Ask for what's missing in one message, with the exact export settings. Never fill a gap with an estimate: a section
without data is marked Data-limited with what would fill it.

**3. Run the studies** (`processes/studies.md`), in a small script or spreadsheet over the export, never by eye. Save the calculation next to the report (`season-report-<season>-<year>-calc.*`) so a
number can be checked. Run heavy reads at low priority (factory rule 7).

**4. Read it.** Load from `brain-system/creative-strategy-context/`: `black-friday-and-q4-data.md`, `ad-account-analysis.md`, `seasonality.md` and `gifting-and-q4-creative.md`; then `brand-lens.md` last. For
each study: what happened at this brand, the cross-brand number beside it, and whether the brand followed the pattern or broke it. A brand that breaks a pattern on solid numbers is the most useful finding
in the report. Label every finding (`brain-system/system/evidence-and-labels.md`): the brand's own numbers are Verified (dated export), the cross-brand numbers Stated, the reasons Inferred.

**5. Write the plan** (`processes/plan.md`): this year's calendar, what to make, what to test, what to have ready. Dates moved to this year, Danish rules applied, every price and date left to the brand.

**6. Write the report and the methods file** in the report form (`report-form.md`), from `template.html`. Audience as in `weekly-creative-report`: leadership gets the tight version, the team gets every
section.

**7. Check it.** `brain-system/scripts/grounding-check.py` on the report text against the brain, and `brain-system/scripts/voice-lint.py` on the prose. Then spawn the `context-grounding-review` agent on the
report and the methods file: every number traces to the calculation file, every cross-brand number to the data doc. Fix what fails.

**8. Look at it.** Open the page, check it at phone width, one render.

**9. Save and hand over.** `audits/<YYYY-MM>/season-report-<season>-<year>.html`, `-methods.html` and the calculation file; a line in `audits/INDEX.md` if the brain has one. Tell the person, in a few
sentences: the three findings that change this year's plan, where the files are, and which skill to run next (usually `offer-ads` with the plan's dates). **STOP:** the report is a draft until a person
on the team has read it; sending it to the brand is a person's act.

**10. Feed back.** Propose the doc updates the season calls for, each with its date and evidence: brand-specific ones in the brain (`running-notes/feedback.md`, `brand-lens.md` "what's worked",
`personas/` if the audience shifted), generic lessons in `feedback.md` here. A person applies them.

## Rules

- **Invent nothing.** Every number traces to the export and the calculation file. Prices, discounts and dates in the plan come from the brand
- **Spend picks the winners, inside the brand.** Never compare this brand's ROAS or CPA with the cross-brand numbers; they don't have any
- **Small numbers are shown, not used.** Thresholds in `processes/studies.md`
- **The cross-brand data is a reference, not a target.** "The brand launched fewer ads than the median US brand" is not a finding without a reason it matters
- **Patterns, not causes.** Every section's caveat line says what the number can't prove
- **Danish rules.** The plan never moves a price claim earlier than the offer period allows (`.claude/skills/offer-ads/offer-copy.md`). Not legal advice
- **Nothing leaves without a person.**

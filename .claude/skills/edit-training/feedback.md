# Feedback log

What we've observed about training: which sources gave the best rules, how many sessions it took
before calibration improved, what extraction got wrong. A log, not a rulebook: new lessons land here
with a date, and once confirmed they move into `SKILL.md`, leaving one line here saying where they
went. No brand details here; brand rules live in each brain.

## Log

**2026-11-02, added from Alex Cooper's newsletter (1 Nov 2026) and his live stream "AI Video Editing
Workflow" (13 Oct 2026). Not yet run**
- Step 7 (back-test the editor): his loop is to re-edit the last 25 ads each senior editor made, show
  them in one place, get the senior's notes on each, and repeat until the skill knows a good edit.
  Ours puts the shipped ad beside the skill's edit as v0/v1 on the review page (v0 sorts first,
  checked in `serve.py`'s `parse_name`; not yet tried in the browser)
- Step 8 (versions to approval): his measure is that most edits are approved at v1 or v2, sometimes
  v3 (Stated, his agency only). We read it from `review-notes.json` instead of counting by hand
- "Who trains": only his best editors train the skills; the person driving AI builds v1 and gets out
  of the way; budget time for the dip. His team reports 60-70 % less time per edit and one senior at
  5x edits a day (Stated, his Slack and his editor; no numbers shown)
- Frame.io MCP: he pulled 30 days of his team's comments into a feedback document and fed it to the
  skill. Beta, access on request; we haven't had access
- His own weak spot, kept here as a warning: general notes from his review app go into the rules
  file automatically, and he says he should check better what gets in. Our step 4 is that check;
  keep it

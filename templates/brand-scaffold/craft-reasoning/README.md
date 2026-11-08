# Craft reasoning

Customer language says what the *buyer* thinks. This folder holds what the *team* thinks: why an
edit is cut the way it is, why a brief picks one hook over another, why a comment on an ad was
right. It's what agents can't find anywhere else, and it's what makes `brief-check` and `video-edits`
edit and review like this brand instead of like everyone else.

It covers processes too, not only creative calls: how someone sets up a campaign, builds the
monthly report, onboards a creator, runs a test. Any task done with a narrated walkthrough (screen
recording plus talking) can later become a skill. The more people on the team who are very good at
their part record themselves, the better the agents get.

## How to capture it

Narrate while you work, then save the transcript here. Aqua Voice while editing, or a recorded
call with transcription switched on while an editor screen-shares.

Say the *why*, not just the what:
- "I cut after one second because this is ASMR and it has to feel like the organic feed"
- "No voiceover here, the sound of the product is the proof"
- "This hook goes first because the reviews keep saying X"
- "That comment is wrong: the magnet demo is the value prop, keep it"

## Files

One file per session: `<YYYY-MM-DD>-<who>-<what>.md`, e.g. `2026-11-04-<who>-ugc-rough-cut.md`.

At the top of each file:
```
Who: <name, role>
What: <the asset or task being worked on, with a link>
Format: <UGC / organic short-form / static / ...>
Source: <voice memo / meeting transcript / written notes>
```

Then the transcript, lightly cleaned. Don't summarise it away: the exact wording is the value.

## Where it goes next

The `edit-training` skill turns video-related sessions into rules: making-rules in
`craft-reasoning/video/*.md`, judging-rules in `craft-reasoning/video/review-rubric.md`, and it measures
how well the AI's feedback matches the team's in `craft-reasoning/video/calibration.md`. Other patterns
that show up in three or more sessions go in `running-notes/feedback.md`. Leave the source files
here: they're the evidence for the rules.

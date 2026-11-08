---
name: edit-training
description: Train the video editing and video feedback skills on a team's own craft (klip-træning, train the editor, edit reasoning, calibrate video feedback, teach Claude our edit style). Turns narrated editing sessions, spoken ad reviews and old review-tool comments into sourced edit rules and a review rubric in the brand brain, then calibrates brief-check's video feedback against real human comments until it agrees often enough to trust. Back-tests video-edits by re-editing ads the team already shipped, side by side with the human's edit, and counts how many versions edits need before approval. Use when someone wants to record an editor explaining their cuts, turn editor feedback into rules, make the AI video feedback or the AI edits better, back-test an edit style, or check how close the AI's comments are to the team's.
---

# Training the editor

`video-edits` and `brief-check` edit and review like everyone else until they learn how *this* team
thinks. This skill is how they learn: it turns the team's reasoning into written rules with sources,
and measures whether the AI's feedback now matches the humans'. Without it, taste feedback stays
generic, like asking for a script with no context.

Always run inside the brand's brain folder.

## When it's worth setting up (check at a new employer)

Worth it when at least two are true:
- The team makes video regularly (roughly 10+ ads a month), in-house or with regular freelancers
- There's a review tool with a comment history (Frame.io, Air, Drive comments, Figma, a Slack channel)
- One or more editors or creative leads have taste worth copying, and time for a few recordings
- Review rounds are a bottleneck: leads spend hours on first-pass comments

Not worth it yet when editing is fully outsourced to an agency with its own process, or when video
is rare. Then `brief-check`'s objective checks (spelling, shots, claims) are enough.

At a bigger company, start with **old comments** (source 3 below): it needs nobody's time, and the
data already exists.

**Who trains, and the time it takes.** Only the editors whose work the team would copy record
sessions and give back-test notes (step 7); a weaker editor's taste trains the skill to edit like
them. Whoever sets this up builds the first version (the brain, the review page, the first rules),
then steps back and lets those editors train it. Budget their time for it: the first rounds cost more
than they save, and a skill nobody had time to train turns out edits that save little. Tell the
editors plainly what's changing: their taste becomes the thing the skill learns from.

## Where the knowledge lives

| File | Answers |
|---|---|
| `SKILL.md` (this file) | How to capture, extract, approve and calibrate |
| `feedback.md` | What we've observed about training itself. A log |
| brain: `craft-reasoning/` | The raw material: transcripts, with source and date |
| brain: `craft-reasoning/video/*.md` | Rules for *making* edits (read by `video-edits`) |
| brain: `craft-reasoning/video/review-rubric.md` | Rules for *judging* edits (read by `brief-check`'s taste check) |
| brain: `craft-reasoning/video/calibration.md` | How often the AI's comments match the humans', and how many versions edits need before approval, over time |

## Sources, and how to capture them

1. **Narrated edit session.** An editor screen-records a normal edit in their own tool and talks
   through the *why*: "cut after one second because it's ASMR and has to feel like the feed", "no
   voiceover, the product sound is the proof", "I drop this B-roll, it's decoration, not
   demonstration". 20-40 minutes per session. Ask for ordinary work, not a performance
2. **Spoken review.** A creative lead watches 5-10 ads and says out loud what they'd comment and why.
   Faster than a full edit session, and it trains the reviewer directly
3. **Old review comments.** Export the comment history from the review tool (via the "Review tool"
   role in `tool-map.md`, or a CSV the human exports): the comment, the timestamp, the ad, and
   ideally the version before and after. Hundreds of real judgments, no recording needed. Frame.io
   has an MCP (in beta, Oct 2026; access on request): when the brand's tool map lists it as working,
   pull the last 30 days of comments through it instead of a CSV. Untested here
4. **Corrections from use.** Every time a human rewrites or rejects a `brief-check` comment or changes
   a `video-edits` cut, with one line on why. These come in by themselves once the skills are in use

Recordings need the person's OK to be recorded and kept in the brain, and they shouldn't include
anything confidential on screen that doesn't belong there (other clients, personal messages).

## The steps

**1. Transcribe and align.** Transcribe with the fal.ai speech-to-text model (as in `video-edits`:
`recommend_model`, `get_model_schema`, `get_pricing` first). For screen recordings, extract a frame at
each moment the person explains a decision, so the rule has a picture of what they meant. Save the
transcript in `craft-reasoning/` with the header that folder's README asks for.

**2. Extract rule candidates.** From each source, pull out decisions and the reason behind them. One
row each:

| Rule | Why (their words) | Applies to | Example | Source |
|---|---|---|---|---|
| Cut B-roll that doesn't demonstrate a value prop | "it's decoration, not proof" | UGC ads | `2026-11-04-editor-ugc.md` 12:40 | narrated edit |

"Applies to" matters: an ASMR rule doesn't belong in a testimonial ad, and a rule for one brand
doesn't belong in another's brain. Only extract what the person actually said or clearly did; don't
generalise beyond it.

**3. Merge with what's already there.** Candidates that match an existing rule add a source to it.
Contradictions are flagged, not settled by the agent: two editors disagreeing is useful information,
and the human decides.

**4. STOP: approve the rules.** Show the new candidates and the contradictions. A rule is
**confirmed** when the human approves it or when it has 3+ independent sources; otherwise it's a
**candidate**. Candidates can be used, labelled as such; confirmed rules are used without a label.

**5. Write them home.** Rules about making edits → `edit-style*.md` (right style file). Rules about
judging edits → `review-rubric.md`, grouped by what a reviewer looks at: hook, pacing, demonstration
of the value prop, B-roll, captions, sound, ending. Each rule keeps its sources.

**6. Calibrate.** This is how you know if it's working.
- Take 5-10 finished ads that humans already commented on, and that weren't used as training material
- Run `brief-check` Mode B on them *without* showing it the human comments
- Compare, per ad: **matched** (the AI made the same point), **missed** (a human point the AI didn't
  make), **wrong** (an AI point the human would reject; ask the human when unsure)
- Log the result in `calibration.md`: date, format, number of ads, matched / missed / wrong, and a
  line on what the misses have in common. Each miss is a rule candidate for the next round

Step 6 measures the reviewer. Step 7 trains and measures the editor.

**7. Back-test the editor.** Re-edit ads the team already shipped and let an editor judge the
results side by side with what they made.
- Pick recent ads of one format or edit style that one of the editors from "Who trains" made, with
  the raw footage and the brief still available. Start with 5-10; Alex Cooper runs the last 25 per
  senior editor. Never pick ads from the calibration set (step 6)
- Run `video-edits` in one-shot mode on each, with the brief and the footage only: the shipped ad
  is never shown to it
- Put each result in one review-page run folder next to the shipped ad: the shipped ad as
  `<ad>_v0_preview.mp4`, the skill's edit as `_v1`. Compare then shows the human's edit (v0) next to
  the skill's (v1), and the editor notes v1 as usual
- Notes about this ad are applied as normal (`video-edits` step 10), and the hook is re-rendered
  until approved. Notes that hold beyond this ad are rule candidates for step 2. They go through
  step 4 like any other source: never written to a style file unseen
- Repeat with a fresh set after the rules change. These ads are training material now; keep them
  out of later calibration sets

**8. Count versions to approval.** Every approved hook's version number is in its run folder's
`review-notes.json` (`approved`): v1 means approved as first rendered. Log the median and the share
approved at v1 or v2 per format in `calibration.md`, for back-tests and for ordinary runs. The
target: most edits approved at v1 or v2. When that number stops improving, the misses from step 6
and the notes from step 7 say what to train next.

**9. Lift approval when it's earned.** When calibration shows roughly 80% of human points matched,
with few wrong ones, over two rounds in a row for a format, and most edits of that format are
approved at v1 or v2, suggest that the human lift the approval step for that format in `tool-map.md`.
The human decides. Re-calibrate every month or so, and whenever the team's taste shifts (new lead,
new brand direction).

## Guardrails (never)
- Never invent a rule or a reason. Every rule points to a source a human can open
- Never train on one person's recording without their OK, and never keep recordings of people who
  didn't agree to it
- Never let a rule from one brand leak into another brand's brain; general lessons go in this
  skill's `feedback.md`, stripped of brand details
- The calibration set is never used as training material, or the score means nothing. Back-tested
  ads (step 7) are training material, so they never go into a calibration set
- Don't turn taste into fake precision: the rubric says what good looks like and why, not a
  points system

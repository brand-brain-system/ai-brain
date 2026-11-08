---
name: brief-check
description: Review creative against its brief (brief-check, QA, review edits, check footage, spell check, korrektur): check a creator's raw footage folder for missing must-have shots, or check finished ads (video or static) for Danish spelling and grammar, claims outside the brand lens, and whether they deliver what the brief asked. Drafts comments for the review tool and messages to creators, and posts nothing without approval. Use when someone asks to review footage, QA ads, check edits against a brief, spell check a batch or give feedback on creative. Tool-agnostic: reads the brain's tool-map.md.
---

# Brief check

Always run inside the brand's brain folder. The human approves before anything is posted, sent or
moved. Objective checks (spelling, missing shots, claims) come first because they have a right
answer. Taste checks (is this a good edit?) are only as good as the brain's craft reasoning, so
they're labelled as opinion until the skill has been trained.

## Where the knowledge lives

| File | Answers |
|---|---|
| `SKILL.md` (this file) | What to check, in what order, and what must never happen |
| `feedback.md` | What we've observed. A log, not a rulebook |
| brain: `tool-map.md` | Where briefs, footage and the review tool are, and how to reach them |
| brain: `sprints/<sprint>/briefs/` | The brief, including the "Must-have shots" and "Claims allowed" in its header |
| brain: `brand-lens.md` | Voice, claims gates, anti-language |
| brain: `craft-reasoning/` | Why the team edits the way it does: the source for taste checks |
| brain: `running-notes/feedback.md` | Brand-specific corrections from past reviews |

## Prerequisites (check first, ask if missing)
- **The brief.** No brief: stop and ask. Reviewing without one gives generic feedback. A brief
  without "Must-have shots" can still get the spelling and claims checks; say the shot check was skipped
- **`tool-map.md` filled in** for Brief store, Raw footage and Review tool. An empty role means
  human hand-off for that step: say so, don't guess where things are
- **A way to see the video.** Frames plus a transcript are enough: extract frames at the scene
  changes and every 1-2 s with ffmpeg, and transcribe with the fal.ai speech-to-text model that
  `video-edits` uses (check `get_model_schema`; Danish, word timestamps). No ffmpeg: ask before
  installing anything. Statics: read the PNG/JPG directly

## Mode A: raw footage (from a creator)

1. **List what arrived**: files, length, orientation, resolution, sound. Flag the unusable ones
   (wrong aspect ratio, no sound when sound was asked for, unreadable)
2. **Match against "Must-have shots"**, one line each: ✅ found (file + timestamp) / ⚠️ partly (what's
   missing) / ❌ missing
3. **Hooks and lines**: for a full-script brief, is every exact line and every hook take there?
   Quote the transcript where it deviates
4. **Claims**: anything said on camera that isn't in "Claims allowed", with timestamp
5. **Draft the creator message** in Danish, friendly and specific: what's great, what's missing,
   by when. One message, not a list of complaints
6. **STOP: approval.** Then send through the "Creator comms" role, or hand the text over
7. On approval, and only if the human says so: move the concept on the task board (e.g. filming →
   editing) and, if the tool map says how, assign an editor

## Mode B: finished ads (video or static)

For each ad in the batch:

1. **Text on screen and captions**: Danish spelling, grammar, and consistency with the approved
   copy. Watch for the usual traps: compound words split in two ("hud pleje" → "hudpleje"),
   da/når, nutids-r, comma use, English words that slipped in. When unsure, check
   Retskrivningsordbogen (dsn.dk/ordbog), don't guess. Transcript against script for spoken lines
2. **Claims**: every claim against "Claims allowed" and `brand-lens.md`. Offer prices and dates:
   against the offer brief (use the `offer-ads` rules for Danish price marketing)
3. **Brief delivery**: does it do what the brief's "Goal" and "Key message" say? Right persona,
   the must-have moments present, the length and aspect ratio right
4. **Marking**: if the creator will post it, the brief says "Reklame" first
4b. **Platform rules**: for ads that will run paid, the `ad-policy-check` result per ad (run it if it
   hasn't run on this version). Its stop and fix lines go into the table below
5. **Taste** (opinion, labelled): pace, hook strength, whether the visuals demonstrate the value
   prop. Base each point on a rule in the brain's `craft-reasoning/video/review-rubric.md` (confirmed rules
   unlabelled, candidates labelled "candidate"), or on `running-notes/feedback.md`, and cite it. No
   source: label it "untrained opinion" or leave it out. No rubric yet: the `edit-training` skill
   builds one

Output one table: ad, check, pass / fix / note, timestamp or position, the drafted comment.
Keep comments short and actionable, like a good creative lead would write them.

**STOP: approval.** The human edits, deletes or approves comments. Then post through the "Review
tool" role, or hand them over as a list to paste. After posting, optionally ping the editor through
"Team chat", again only on yes.

## Learning from the human's edits
When the human rejects or rewrites a comment, ask why in one line if it isn't obvious, then:
- A general lesson (applies to any brand) → `feedback.md` here, dated
- A brand lesson ("for this brand, keep the magnet demo; it shows the value prop") →
  the brain's `running-notes/feedback.md`
- A spoken explanation worth keeping word for word → a file in `craft-reasoning/`

## Guardrails (never)
- Never post, send, move or assign without a yes in this session, unless `tool-map.md` records
  that the human lifted approval for this skill
- Never invent a claim check result. If the brand lens doesn't cover a claim, flag it as "unknown,
  ask", not as pass
- Never judge a creator's appearance, voice or body. Feedback is about the brief and the craft
- Don't rewrite the creator's words into perfect written Danish. Spoken Danish is allowed to sound
  spoken; only fix what's wrong or off-brief

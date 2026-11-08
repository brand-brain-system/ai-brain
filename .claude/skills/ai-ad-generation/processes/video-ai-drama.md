# Process — AI Drama Ad

A long-form scripted drama (1-3 minutes) with a generated cast, built shot by shot: story, script
and shot list, cast and world, one start frame per shot, one clip per frame, then the stitched cut
handed to the edit. Picked when the user asks for a drama ad, a soap-opera or micro-drama style ad,
or a multi-character story longer than one clip can hold.

What the format is and why it works: `brain-system/creative-strategy-context/ai-drama-ads.md`.
How a paid generation is quoted, how a person stays the same, and how a clip is built:
`brain-system/creative-strategy-context/production.md`. This process owns the order of work and the
drama-specific checks; it does not repeat those rules.

**Status: experimental.** Adapted from one vendor's demo (ScaleBot, Oct 2026), not yet run on a
brand here. Log what held and what broke in this skill's `feedback.md`, and promote nothing into the
hard rules before it has held on a second brand.

## Two modes

- **Prompt pack** (default): steps 1-6 and the prompts for steps 7 and 9, written into the run
  folder for the user to generate in their own tool.
- **Generate**: when the brain has fal.ai connected and the user asks for it. Every paid step shows
  its quote (with the repair budget) and waits for a yes, per `production.md`, "Paying for
  generation".

## Required inputs

- **The story idea.** People, conflict, reveal. Optional: with none, propose two or three story
  shapes from `ai-drama-ads.md` grounded in the persona, and let the user pick.
- **What the viewer should come away knowing.** One product belief, plain words. Required.
- **Offer or CTA**, if any.
- **Length and aspect ratio.** Default 9:16.
- **Product reference image.** One clean pack shot from `assets/`. A product-free drama is allowed
  when the user asks for one.
- **Cast**: existing AI people from `assets/people/`, or let the process cast them.

## Execution

1. **Load the brand, then the persona's story.** Brand context, compliance, voice, and the
   strategy and idea bank per SKILL.md step 2. Then the persona's trigger moments, pains and
   aspirations from `personas/` and voice-of-customer: the drama's stakes come from there.

2. **Write the beats.** 5-8 beats: setup, open question, escalation, turn, reveal, payoff. Use
   the `scriptwriting` skill's `write-storytelling-script` process for the arc and
   `emotional-delivery-and-timing.md` for where the feeling lands. The product enters at the turn
   or later, as the plot's secret or reveal.

3. **Write the script as a shot list.** Copy `drama-shot-list-template.md` into the run folder as
   `shot-list.md` and fill it: the brief, pronunciation respellings for any name the model may
   mangle, the cast, the world, the beats, then every shot. Rules for shots:
   - One speaker per shot, one short line, delivery direction on every line
   - A shot's length fits the video model's clip length, checked at run time, with a whole second
     spare to trim (`production.md`, "Generated video clips")
   - Every shot states who is on screen and who faces whom
   - Mark the must-keep shots for the cutdowns

4. **Clean the script before anyone sees it.** Read it through as a viewer:
   - No line repeats a benefit another line already said; cut the weaker one
   - No character speaks like a label ("the brand says", "clinically shown", a list of ingredients)
   - Every number or result traces to a source or carries `[STAT NEEDED — verify before publishing]`
   - The story still makes sense with the product lines removed; if it doesn't, the plot is an ad
     read and needs rewriting
   Then run the grounding gate and the voice gate on the dialogue, per SKILL.md steps 7-8.

5. **Approval 1: the script and shot list.** Show the beats, the shot list and both gate receipts.
   Stop until the user approves or edits. An edited shot is changed in `shot-list.md`.

6. **Cast and world.** One reference sheet per character per `production.md`, "An AI person who
   stays the same", each with its fixed wardrobe colour, and one visual-guide frame per location.
   Generate one, show it, then the rest. The user approves each sheet and the world before any shot
   frame is made.

7. **Storyboard: one start frame per shot.** Each frame is a clean full-bleed image in the delivery
   ratio, built from the character sheets, the world frame and the product reference, per
   `production.md`. Make shot 1 first and look at it; then quote and make the rest.

8. **Continuity review of the frames.** Go through every frame against the shot before it, using
   the checklist in the shot list's continuity log: sitting or standing, who faces whom, positions in
   the room, props, wardrobe, time of day, the pack. Characters in conversation look at each other,
   not at the lens. **Fix problems in the frame, not later in the clip**: rewrite that shot's frame
   prompt with the correction stated positively, attach the earlier frame that shows the right
   staging as a reference, and regenerate. Refer to characters by wardrobe colour ("the woman in the
   red dress turns toward the woman in the green sweater"). Log every fix.

9. **Approval 2: the storyboard.** Show the frames in order with the continuity log. Stop for a yes.

10. **Clips.** One clip per frame, image-to-video from that frame. The clip prompt describes motion
    and the spoken line only (camera move, what moves, the line in quotes with delivery and the
    pronunciation respelling); the frame carries the look. Make shot 1 first at the draft resolution
    and watch it; its real price sets the quote for the rest. Then the batch at draft resolution.

11. **Clip review.** Watch every clip: a character speaking to the lens who shouldn't, a wrong
    speaker's mouth moving, a mangled product name, a warped start, a frozen stretch. A staging
    problem goes back to step 8 (fix the frame, regenerate the clip); a broken first half-second is
    trimmed, not regenerated. Upscale only approved clips.

12. **Assemble and hand over.** Join the approved clips in shot order with ffmpeg into one raw cut.
    If the cut has dead air (a still beat with no room sound), an audio-enhancement pass that rebuilds
    ambient sound under the dialogue is an option; quote it and keep the original next to it. Then
    hand the raw cut to `video-edits` (standard mode) for trimming silences, pacing, captions, the
    AI-content label and the cutdowns listed in the shot list.

13. **Log.** Every paid request in `jobs.json`, every stage in `costs.md`, per `production.md`.
    In `feedback.md`: which models held the faces across the cast, how many frames and clips needed
    fixing and why, and what the long cut cost against the quote.

## Output

- **STORY.** The beats, and the one belief the ad leaves behind.
- **SHOT LIST.** `shot-list.md` in the run folder, filled in.
- **CAST AND WORLD.** Identity parts and sheet paths per character; the world frame per location.
- **FRAME PROMPTS and CLIP PROMPTS.** One of each per shot, in code blocks, rebuilt from the shot
  list (prompt pack), or the generated files with their records (generate mode).
- **CONTINUITY LOG.** What was fixed and how.
- **Brand Context Applied**, **Grounding Review** and **Voice Review**, per SKILL.md.

## What never to do

- Let characters pitch: benefit lists, label language, or two lines saying the same thing.
- Make a shot frame before the cast sheets and the world are approved.
- Batch frames or clips before one has been made and looked at.
- Fix a staging problem by re-rolling the clip; fix the frame.
- Present a character as a real customer, or skip the AI-content label (`legal-ai-ugc.md`).
- Upscale clips that haven't been approved.

---
name: song-ads
description: Make an animated story ad carried by an original AI song (song-ads, music ad, song ad, AI song ad, animated story ad, sung ad, jingle ad): story spine and lyrics from the brand brain, a shot plan in takes, the song on fal.ai, approved character sheets, one storyboard image per take, cheap 480p draft clips, then 1080p for the approved takes only, assembled with ffmpeg and Danish captions. Every paid step shows its price and waits for a yes. Use when someone asks for a song ad, a music ad, an animated story ad with a song, or wants to recreate the AI song-ad format for a brand. Does not edit real footage (that is video-edits) and does not make static ads (static-ads).
argument-hint: "[brief ID or the idea in one line]"
---

# Music ads

## Goal

Make one animated story ad where an original song tells the story and the product is the turning point. The song, the characters and every clip are generated on fal.ai, and a human approves each stage before money is spent on the next. The result is a finished ad in the run folder, captioned, ready for a human to review and upload.

This skill does not edit filmed footage (`video-edits`), make statics (`static-ads`, `offer-ads`), or review finished ads against a brief (`brief-check`, which can run on the result). It never writes a story presented as a real customer's experience. The format came from a Scalebot tutorial (YouTube, shared 7 Oct 2026). Its steps are translated here to fal.ai and our brain, and its claims about performance are not used.

## What it can use

Always run inside a brand brain. Read these before step 1. Say which are missing, and what that blocks.

- **The brief:** `sprints/<sprint>/briefs/<brief-id>.md`, normally from the `storyboard.md` template with the required header from `briefs/README.md`. The "Deliverables" line sets length and aspect ratio; "Claims allowed" sets what the story may say about the product. No brief: write a draft brief from the person's idea and get it approved at the first stop.
- **Brand DNA:** `brand-context/brand-one-pager.md`, with the image prompt modifier and the physical product description. Missing: run `brand-dna` first. No characters or storyboards without it.
- **Claims gate:** `brand-lens.md`, the "Can claim" and "Cannot claim" lists, and the EU food and supplement section if the brand has one. This is the only source for what the product does in the story.
- **Personas:** `personas/personas-profile.md`, the entry moments. The hook comes from one of them. Empty: say so, and build the hook from customer language in `source-pulls/` instead, labelled Inferred.
- **Customer language:** `source-pulls/`. Lyrics borrow the words customers use for the problem.
- **Concept register:** `idea-bank/concepts.md`. The concept ID goes in front of every file name.
- **Product photos:** `assets/`. The product in every image and clip is drawn from these. None: stop before step 6 and ask for them.
- **Production rules:** `brain-system/creative-strategy-context/production.md`, "Paying for generation" (quote, repair budget, cost and time log), "Generated video clips" (start frame or reference, motion prompts, trim room, no generated screens) and "Reference images" (convert .avif to PNG).
- **Brand feedback:** `running-notes/feedback.md`, and this skill's own `feedback.md`.
- **Language:** the brand's market. Danish brands get Danish lyrics and captions. A brain whose CLAUDE.md names another market gets that market's language.
- **fal.ai MCP:** `recommend_model`, `get_model_schema`, `get_pricing`, `estimate_cost`, `upload_file`, `submit_jobs`, `wait_for_jobs`. Endpoints checked on 7 Oct 2026, re-check the schema on every run:
  - `elevenlabs/music/v2.5`: song from a composition plan. Up to 30 chunks, each 3,000-120,000 ms with its own lyric text and English style words, total up to 10 minutes. Optional audio style reference on the first chunk. $0.60 per minute
  - `minimax/music-3`: song from a style prompt plus lyrics, up to 300 seconds, $0.002 per second. No set length per section
  - `bytedance/seedance-2.5/image-to-video`: 4-30 second clips at 480p, 720p or 1080p. `draft: true` makes a 480p preview and returns a `draft_id`. Aspect ratio follows the start image. Billed per token, $0.0214 per 1,000
  - `bytedance/seedance-2.5/draft/complete`: turns a `draft_id` into the 1080p clip, within seven days, on the same account
  - `bytedance/seedance-2.5/reference-to-video`: up to 30 reference images (named @Image1, @Image2 ... in the prompt), plus video and audio references (MP3/WAV, 1.8-30.2 s in total), 50 files at most; aspect ratio set explicitly; `draft: true` works here too. The way to lock characters and the storyboard across a multi-shot take. Schema checked 11 Oct; how well it holds a character is untested
  - Image model for characters and storyboards: ask `recommend_model` for image editing with reference images, the same way `static-ads` does
  - Speech-to-text with word timestamps, the same way `video-edits` step 2 does
- **ffmpeg** for the rough cut and the final assembly, under the CPU budget in `video-edits` SKILL.md ("CPU budget").
- **Caption style:** `video-edits` step 7 ("Captions, styled by default") and the brain's `craft-reasoning/video/*.md` if one exists.

## How this skill runs

1. **Check the inputs and the story type.** Read everything above. The story is fiction told by invented animated characters, and the ad must not look like a real person's testimony. Write one line in `script.md` saying so. If the brief wants a real customer's story, stop: that needs the customer, their consent and their own words, and it is a different job.

2. **Write the story spine.** Six beats, one or two sentences each: the hook (a persona's entry moment, in the viewer's situation), the problem getting worse, the turning point where the product arrives, what the product does (only from "Can claim"), the payoff, the call to action. If the person supplies a script, check it beat by beat against the claims gate and mark every line that breaks it. A competitor's ad may give the structure. It never gives the words.

   WRONG: pasting a competitor's transcript in as the lyrics, or the payoff "she lost 10 kilos in a month" for a supplement.
   RIGHT: the competitor's beat order written as six empty beats, filled with this brand's persona, customer words and licensed claims.

3. **Write the lyrics and the shot plan.** Split the spine into takes. A take is one lyric line or couplet, 4-15 seconds long, with 1-6 shots. For each take, write the lyric, what each shot shows, which characters appear, whether the product is visible, and the take's length in seconds. Set the length to the brief's "Deliverables". If that is empty, propose a length and say what it costs, because cost grows with every second. Read the lyrics aloud in your head for rhythm. Then check every line against the claims gate and run the brand's spelling check (`brief-check` Mode B rules for Danish).

4. **Price the whole run** per `production.md`, "Paying for generation": the 25 % repair budget on its own line, and the clock time per stage logged in `costs.md` from here on. Use `estimate_cost` for the song and `get_pricing` for the rest. Seedance bills per token and does not expose the token count of a clip in advance. Price it from the real charge of the first draft clip (step 8), and until then write "video: unknown until the first draft". Unknown is never written as zero. Save the estimate in `costs.md`.

5. **STOP: approval 1, story and plan.** Show the spine, the lyrics, the shot plan and the cost estimate. The person changes beats, lines or takes. Rebuild only the takes a change touches, and log the reason for each change in one line in `run-notes.md`.

6. **Make the song: sample first.** Write the style in plain English: genre, tempo, mood, voice, instruments. Never an artist, band or song name. With ElevenLabs, build a composition plan with one chunk per section, so each section's length matches the takes. Generate a sample of the first 15-20 seconds only. Show it with its price.
   - **STOP: approval 2a, the sample.** On a no, change the style words and try again.
   - On a yes, generate the full song with the same plan and seed. Transcribe it and compare it with the lyrics. Lines that are mumbled, missing or changed go back to the person.
   - **STOP: approval 2b, the full song.** The approved song sets the timing: each take's length is now its section's real length in the song.

7. **Build the world and the characters.** First one world image: the setting and the look, in the brief's aspect ratio, with the Brand DNA prompt modifier. Describe the look in plain visual terms, never by naming a studio or an existing character. Then one sheet per character. A character who changes over the story gets one sheet per stage, each made from the approved sheet before it. Then the product, from the photos in `assets/`, unchanged.

   WRONG: "Pixar style", "like a Disney character", or a known cartoon character.
   RIGHT: the look described in plain words (rendering, lighting, proportions, palette), with original characters.

   **STOP: approval 3, one image at a time.** Each approved sheet is the reference for everything after it. Save them in `characters/` with the stage in the file name.

8. **Draw the storyboards.** One image per take, with the take's shots as panels in order, made with the world, character and product references. Draw take 1 and take 2 first.
   - **STOP: approval 4a, the first two storyboards.** Then draw every other take in one batch with `submit_jobs`.
   - **STOP: approval 4b, the storyboard grid.** Show every storyboard in a local HTML grid with approve and redo per take. Redraw only the takes marked redo.
   - The storyboard is the plan, never the first frame: image-to-video opens on the exact image it gets (`production.md`, "Generated video clips"). A **one-shot take** gets a clean start frame drawn from its approved panel (full-bleed, delivery ratio, same references) and goes image-to-video. A **multi-shot take** goes reference-to-video with the storyboard, the character sheets and the product photo as references, the shots named in order in the prompt. Write the route per take in `shot-plan.md`; the start frames show at approval 5a with the first clip.

9. **Draft the clips at 480p.** Render take 1 with `draft: true` and the take's real length, rounded up to a whole second so a warped start can be trimmed. The prompt describes motion and camera only (`production.md`). Read its real charge, write the per-second price into `costs.md`, and recompute the total for every take. Turn off the clip's own audio unless the brief wants sound effects under the song. If a character must sing on screen, use reference-to-video with that take's slice of the song as the audio reference, and check its schema first.
   - **STOP: approval 5a, the first clip and the real price.**
   - Then draft every other take in one batch. Save every `draft_id` in `jobs.json` with its date: the drafts expire after seven days.
   - Cut a 480p rough cut over the song with ffmpeg, at low priority.
   - Run the frame check on the rough cut (`video-edits` SKILL.md, "Frame check"), with strips at the take boundaries. Fixing a take means a new draft, so fix only what the check marks worst, and show the rest as open.
   - A take that fails a check (a warp past its first 0.5 s, the product changed, a broken face) is redrafted from the repair budget before this stop and listed with its reason; a warp only in the first 0.5 s is trimmed instead.
   - **STOP: approval 5b, the rough cut.** Fix a weak take by drafting it again with a changed prompt, never by drafting every take again.

10. **Finish at 1080p and assemble.** Complete only the approved drafts with `draft/complete`. Assemble with ffmpeg: clips cut to the song's section lengths, the song on top at about -14 LUFS, and captions of the lyrics in the `video-edits` style. The call-to-action end card can be a `motion-ads` card (real product photo, brand font, offer copied from the brief) rather than a generated clip. Render the full resolution once.

11. **Check the result.** Use ffprobe to confirm the length matches the song, and run `frame-check.py` once for the measurements (black and still stretches, loudness). Look at the frames at every take boundary: no black frames, no jumps in a character's face or clothes, the product the same as in `assets/`. Check the captions against the approved lyrics, and that the ad says nothing outside "Claims allowed". Run `ad-policy-check` on the cut (lyrics, captions, characters, end card; an obvious cartoon needs no AI label, a photorealistic person does: `legal-ai-ugc.md`). Write every check and its result in `run-notes.md`.

12. **STOP: approval 6, the finished ad.** Show the MP4 and the check results. Deliver to the run folder only. Upload nothing. Log lessons: this brand in `running-notes/feedback.md`, music ads in general in this skill's `feedback.md`.

## Output structure

### The run folder

`sprints/<sprint>/video/<YYYY-MM-DD>-<brief-id>-musik/`, holding:

- **`script.md`:** the story-type line from step 1, the six beats, the full lyrics, and the claim check (each product line with its source in `brand-lens.md`).
- **`shot-plan.md`:** one block per take, numbered: lyric, shots in order, characters, product visible yes/no, planned length, then the real length once the song exists.
- **`song/`:** the style text, the composition plan as JSON, the sample, the full song, its transcript, and a note on any line that came out wrong.
- **`characters/`:** the world image and every approved sheet, named `<character>-<stage>.png`, plus the product reference.
- **`storyboards/`:** one image per take, `T<nn>.png`, and `grid.html`.
- **`clips/`:** drafts as `T<nn>-draft.mp4`, finals as `T<nn>.mp4`.
- **`jobs.json`:** every fal request as `production.md`, "The ad record" sets out, plus its take and `draft_id`.
- **`costs.md`:** the estimate from step 4 with its repair budget, the update after the first clip, the repairs spent with their reasons, and the real total and clock time per stage at the end. Unknown amounts are written as unknown.
- **`run-notes.md`:** every change at a stop with its one-line reason, and the step 11 checks.
- **The ad:** `<concept-id>_<brief-id>_musik_<seconds>s.mp4`, plus `captions-<language>.srt`. If the brain is concept work, `run-notes.md` and the reply both say so.

### The reply to the person at each stop

What was made, what it cost so far, what the next step costs, and the question for this stop. At the end, "what I need from you" as in the brain's CLAUDE.md.

## Hard rules

- **Fiction stays visibly fiction.** Animated, invented characters. No first-person story presented as a real customer, and no real person or celebrity.
- **Claims only from the claims gate.** What the product does in the story, the lyrics and the captions comes from "Can claim" in `brand-lens.md`. Health, weight and disease outcomes stay out unless the brand lens names an approved claim.
- **No borrowed creative.** No competitor's script or lyrics, no artist, band or song names in a style prompt, no studio names or existing characters in an image prompt.
- **Price before every spend.** Every paid step shows its price first and waits for a yes at its stop. Unknown cost is written as unknown, never as zero.
- **Draft first, 1080p for approved takes only.** Never render a take at full resolution before its 480p draft is approved.
- **Batch only after a sample.** Song sample before the full song, two storyboards before the batch, one clip before the batch.
- **The product never changes.** Its shape, colour and label come from `assets/` in every image and clip.
- **The song sets the timing.** Takes are cut to the approved song's real section lengths, never stretched to fit.
- **Light on the PC.** Rough cuts at 480p and low priority, the full render once, as in `video-edits`'s CPU budget.
- **Nothing leaves the run folder.** No upload, no post, no message without a separate yes.
- **No performance claims.** A format seen in the Ad Library or a tutorial is not proof that it works. Never say it does.

## When NOT to use this skill

- The ad uses filmed footage or a creator: use `video-edits`.
- The brief is a static image ad: use `static-ads`, or `offer-ads` for offers.
- The story has to be a real customer's experience: that needs consent and the customer's own words, so write a creator brief instead.
- The brand's claims gate leaves the product nothing to do at the turning point: the story will either break the claims or say nothing. Say so and suggest another format.
- Someone wants only the prompts to paste into another tool: write the shot plan and prompts (steps 1-5) and stop there.

$ARGUMENTS

---
name: video-edits
description: Edit raw footage into ads in volume (video-edits, video edit, rough cut, klip, UGC edit, organic short-form edit, hook variations, cut down footage, B-roll): transcribe, deliver a trimmed cut for approval, then the edited version with B-roll (supplied, HTML-built or generated) and styled Danish captions, batch-rendered as every hook × length variation via ffmpeg, all inside Claude Code with no editing software; changes are made by re-rendering, not in a timeline. Has a one-shot mode (straight to a finished preview edit), matches a reference edit's style, batch-processes several footage folders at once, and can generate the footage itself as an AI talking head (AI avatar, AI UGC, talking avatar: the brand's AI person, an ElevenLabs voice and lip-sync on fal.ai). Heavy edits go to a human editor. Use when someone asks to cut down footage, edit a UGC or organic video, add B-roll, make hook variations of an existing ad, or says "apply the notes" on an edit in review.
---

# Video edits in volume

Always run inside the brand's brain folder. This skill does the part that costs editors time but
not taste: scrubbing a 10-minute take down to the usable 30 seconds, stitching the takes in brief
order, adding B-roll and captions, swapping hooks for variations. It doesn't pretend to do the
advanced edit.

**Two approvals, both on real video:** first the trimmed cut, then the edited versions. Watching a
cut is faster and more honest than reading an edit plan.

**Built for volume.** The body is cut once, and each hook and length is a new combination
(5 hooks × 3 lengths = 15 ads). Everything renders locally with ffmpeg: fast, the same result every
time, and no tokens spent on rendering. This is how Codex with GPT-6 Astra does it too (Alex Cooper's
setup: ffmpeg for cuts and compositing, browser only to capture HTML B-roll). Don't drive editing
software with computer use: it's slow and breaks at scale.

## Where the knowledge lives

| File | Answers |
|---|---|
| `SKILL.md` (this file) | The steps and what must never happen |
| `feedback.md` | What we've observed. A log, not a rulebook |
| `frame-check.py` | Contact sheets and measurements for the "Frame check" below; also used by `song-ads` and `motion-ads` |
| `cut-check.py` | Measures a cut before a human sees it: no word chopped at a piece's start or end, no stray piece, no pause left in, no flash segment or B-roll edge a few frames off a cut (steps 7 and 9) |
| `transcript-chunks.py` | Cuts audio over the model's 1,200 s limit into overlapping chunks and joins the transcripts again (step 2) |
| `review-grid/` | `serve.py` + `grid.html`: the edit review page (ads, hooks, versions, synced Compare, Approve, notes stamped to 0.1 s with the words spoken there, answers, transcript line, keys); `notes.py`: list, reply, add, next, status from the command line; notes in the run folder's `review-notes.json` (step 10) |
| `brain-system/creative-strategy-context/safe-zones.md` | Where Reels, Stories, Feed, TikTok and Facebook cover the frame: the one safe box and per-placement numbers |
| brain: `sprints/<sprint>/briefs/` | What the edit must achieve; the "Deliverables" and "Captions" lines |
| brain: `craft-reasoning/video/*.md` | How this brand's videos are cut (pace, captions, B-roll, sound). One file per distinct style, e.g. `edit-style-organic.md` (short-form for the brand's own profile) and `edit-style-ugc-ad.md`. Create on the first run from `craft-reasoning/` and the brand's best existing videos |
| brain: `tool-map.md` | Where footage lives; which editor the team finishes in |

## Prerequisites (check first, ask if missing)
- **The brief** (usually `edit-only.md` or `iteration.md`), or for organic content at least the
  script or the point of the video. Nothing: ask what the video is for before cutting anything
- **Which edit style** applies. Unclear: ask, don't blend two styles
- **ffmpeg** (installed 2026-09-29 via winget, build with libass for captions). Check with
  `ffmpeg -version`; if a shell can't find it, open a new terminal so PATH refreshes
- **Transcription** via the fal.ai MCP. Call `recommend_model` with "transcribe Danish speech with
  word-level timestamps", check `get_model_schema`, run `get_pricing` for the footage length. Extract
  the audio with ffmpeg first and upload it with `upload_file`. **Scribe v2 on fal rejects audio over
  1,200 s**, and only says so when the result is fetched (checked 14 Oct 2026). A file over about 18
  minutes: `python transcript-chunks.py split <audio> <dir>` cuts overlapping chunks, transcribe each,
  `merge` joins them on the original timeline (the file's header says how). Raw files of 30 minutes
  are normal
- **Footage access** through the "Raw footage" role in `tool-map.md`

## Modes

- **Standard** (default): brief + footage → trimmed cut → edited versions
- **One-shot**: when the human asks for it ("just edit it", a capability test, a brand whose style is
  already set). Run steps 1-4 and 6-7 without stopping, and deliver the edited version as a
  **preview** (540×960) together with the trimmed cut, `edl.md` and the B-roll plan, so a wrong take
  or hook can still be swapped. Approval 1 becomes a note, not a stop. The full-size render still
  happens once, after the human says yes to the preview
- **Iteration**: an existing ad plus its footage, and new hooks from an `iteration.md` brief. Keep
  the body, build the new hook versions. Skip to step 5 once the hook takes are found
- **Reference style**: the human gives a reference video with an edit they like. Break it down first
  (cut rhythm in seconds per shot, caption style and position, B-roll frequency, zooms, sound) into
  a short style sheet, with the shot sheet's framing and camera fields for its typical shots
  (`brain-system/creative-strategy-context/adapting-scripts.md`, step 2), and show it before editing. After rendering, compare against the reference
  and fix what's off, up to 3 rounds; then stop and show what's still different. A good result
  becomes a new `edit-style-*.md`
- **Batch**: several footage folders (e.g. 10 creator uploads). Run steps 1-4 for each folder in
  parallel with subagents, one per folder, and collect all trimmed cuts in one grid for approval 1.
  Subagents use a lot of tokens: say how many before starting
- **Mashup (experimental)**: a folder of existing footage plus the brand's winning ads as reference
  → new ad concepts cut from what already exists. Label outputs as experimental and log what
  worked in `feedback.md`
- **AI talking head**: no footage; a script and the brand's AI person. Generate the footage first
  ("AI talking head" below), then run the standard steps on it

## AI talking head
Adapted from Ecom Talent's workflow (course doc, 2026), moved onto fal.ai. The generated clips are
the raw footage; from step 1 on it's an ordinary edit. Every paid step shows its price
(`get_pricing`, quoted with the repair budget from `production.md`, "Paying for generation") and
waits for a yes. The clips are built per `production.md`, "Generated video clips".
1. **The person.** The brand's approved AI person from `assets/people/<name>/` (`production.md`,
   "An AI person who stays the same"). None yet: make one by that section and get the sheet approved
   first. Then one still per setting: the sheet plus a scene part written for talking to camera
   (phone at arm's length or on a stand, eye-level, mouth and face unobstructed, nothing in the hands
   that crosses the face)
2. **The script.** From the brief, split like footage: hooks H1, H2 ..., the body, the CTA. Each
   block is a separate generation, so a new hook costs one short clip, not a new video. Write it for
   the ear: short sentences, spoken Danish, numbers as words
3. **The voice, chosen once per person.** An ElevenLabs voice on fal (`search_models` "elevenlabs
   tts"; Eleven v4 was there on 10 Oct 2026), tried on one script line in Danish and approved. Save
   the endpoint, voice and settings in the person's `identity.md`, so every ad sounds the same.
   Ecom Talent cloned the voice from the first video in ElevenLabs instead; that needs an ElevenLabs
   account of our own (not set up)
4. **Make the clips.** Three routes; pick with `recommend_model`, confirm the schema, show the price:
   - **Audio first** (default, exact words): the voice reads each block → still + audio into a
     talking-head model (on fal 10 Oct: `fal-ai/sync-lipsync/v3/image-to-video`,
     `mirage-api/avatar-x/reference-to-video`, `fal-ai/infinitalk`)
   - **Natural motion + lip-sync** (Ecom Talent's "most realistic"): a silent image-to-video clip of
     the person talking and moving naturally, then a lip-sync model puts the voice on it
     (`fal-ai/sync-lipsync/v3`, `fal-ai/heygen/v3/lipsync/precision`, `veed/lipsync/v2`). Audio
     longer than the clip: loop the clip forward and back (Sync calls it "bounce")
   - **Speech in the video model** (Veo-style: the line written in the prompt). Danish
     pronunciation is unverified; if the voice drifts between clips, run it through
     `fal-ai/elevenlabs/voice-changer` to the saved voice
   Draft one hook at the cheapest setting first and look at it (mouth, teeth, hands, the face against
   the sheet, the Danish) before making the rest
5. **Hand over to the edit.** Save the clips in the run folder as raw footage and go to step 1.
   Transcribe and compare every clip with the script: a changed or mumbled word gets regenerated,
   never cut around. Natural flaws help it read as a phone video: a hand-held reframe, captions as
   usual. Log which route and models held the face and voice in `feedback.md`

## The steps

**1. Inventory.** List the files: length, orientation, resolution, frame rate, audio. Different
frame rates or resolutions get normalised in the render, so note them now.

**2. Transcribe** every file with word timestamps. Save as `transcript.json` in the run folder
`sprints/<sprint>/video/<YYYY-MM-DD>-<brief-id>/`. Fix brand and product names from the brief: transcription
gets them wrong.

**3. Find the takes.** The best complete take of each scripted line (fewest restarts, no stumbles,
ends cleanly), every hook take, and the outtakes to drop. For clips with no speech, extract frames
and describe what each shows.

**4. Trimmed cut.** Render one plain version fast: the best takes in brief order, outtakes gone,
no captions, no B-roll. Write `edl.md` beside it, split into building blocks:
- **Hooks**: every usable hook take, H1, H2 ... (render them as short separate clips too)
- **Body**: the long version, with segments marked that can drop for shorter lengths
- **CTA**: one or more endings

**5. STOP: approval 1, the trimmed cut.** Show the video, the hook clips and a short plan for the
edited version:
- **B-roll plan**: where it goes (timestamp) and what it shows, with the source for each (below)
- **Pacing line: something new on screen every 2-3 s** (the lead strategist's rule, 14 Oct 2026:
  viewers scroll on otherwise). List every planned change with its time: B-roll, a punch-in at a cut,
  a text callout or card popping up (`motion-ads`), a picture-in-picture. A person talking, gestures
  and captions changing don't count. No gap over 3 s, the first 3 s above all. Fill gaps from the
  creator's own B-roll and product shots first, then HTML-built screens, then cards, then generated
  clips (priced). **Too little footage with movement in it is normal, not an exception: then we add it
  ourselves** (slow push-ins below, cards, generated B-roll) and say what it costs
- **Feeling lines get pictures** (the lead strategist, 14 Oct 2026): where the speaker describes her
  life, the problem or how she feels ("stay-at-home mom", "decompress after a long day"), plan B-roll
  that shows the feeling, not just her face. Any format that conveys it: people acting out the
  emotion, stick figures, claymation, 3D animation, simple illustration. Pick what fits the brand, not
  one house style. Ask the creator for real footage in the brief (storyboard "Extra shots"); missing,
  plan it generated (step 6) or licensed stock, clearly illustration, never a generated person passed
  off as the creator or a customer
- **Music plan** (when the ad has music): the track follows the story, serious or darker under the
  problem, a lift or release at the turn to the product, out just before a punchline. Name the
  sections and where the change lands. Licensed tracks only (guardrails)
- **Hero first, then the matrix** (Alex Cooper's flow, adopted 14 Oct 2026): render one hook at one
  length (the hero) and take it through the notes loop until a version is approved; only then build
  the other hooks and lengths from the approved body. One body to perfect, fewer renders, less to
  review. The matrix lists what follows approval, e.g. H1-H5 × 15 s / 30 s: every hook × the brief's
  lengths by default; cut weak combinations and say why
- **Gaps**: what goes to a human editor (masks, keying, subject-tracking zooms, music cut to the
  beat). Kinetic-type hook cards and end or offer cards don't: `motion-ads` makes them as
  transparent `.mov` cards, laid over with ffmpeg like B-roll
The human fixes the cut (wrong take, too long, wrong order) and the plan. Note the reason for each
change in one line: it's craft reasoning (see "Learning").

**6. B-roll.** Sources, best first:
1. **Supplied**: the creator's B-roll, the brand's product clips, screenshots the human gives
2. **Built from HTML**: when the B-roll is something on a screen (a review, a comment, a tweet, a
   product page, an ad library, a chart). Build or open the page, capture it with the browser, and
   animate it with ffmpeg: a full-page screenshot scrolled with a crop is steady and repeatable;
   record the browser only when the page must move by itself. Real content only: a review shown as
   a review must be a real review, with the brand's permission to show it
3. **Generated with fal.ai**: product and texture shots, abstract visuals, and illustrative clips for
   the feeling lines in any format that shows the emotion (people acting it out, stick figures,
   claymation, 3D animation: a tired evening, a quiet moment), never copying a studio's characters. `recommend_model` for
   image-to-video with the product photo from `assets/`; the product must not change. Check
   `get_pricing` and state the cost first. Never generated people presented as customers or staff.
   **From a mood picture** (Ecom Talent's B-roll method, 2026): write the scene per `production.md`
   (`brain-system/creative-strategy-context/production.md`, "A scene from a mood picture"),
   make the still and check it, then image-to-video with one motion line: one camera move, what moves
   in the scene, and how fast ("slow push-in, steam rising from the cup, a hand lifts it"). Pay for the
   clip only once the still is right. **A person in it:** the brand's approved AI person from
   `assets/people/` ("An AI person who stays the same"), never a new face. A talking AI person
   is the "AI talking head" mode. The clip itself (start frame, sound off, trim room, cost log)
   follows `production.md`, "Generated video clips" and "Paying for generation"
Lay B-roll over the cut with ffmpeg overlays: full-frame cutaways while the voice carries on, or a
picture-in-picture window. Keep the creator's audio running underneath. **Nothing laid over the
footage covers the speaker's face or mouth:** picture-in-picture windows, cards and text go where the
face is not. Find the face in a frame; don't assume the framing (a tutorial's first graphics pass
put one on the speaker's forehead). **The "green screen" look** (the speaker small in a bottom corner,
something happening behind): a picture-in-picture of the speaker over full-frame B-roll, no keying
needed. A true cut-out of the person needs keying: human editor

**Placing B-roll, in whole frames** (idea from alyshadotmd/video-editing, adapted; untested in our
renders until the first run, log the result):
- Convert every a-roll cut and every B-roll edge to a frame number (time × frame rate, rounded) before
  placing anything. A time like 28.867 s at 30 fps falls between frames and leaves a stray frame of the
  talking head
- A B-roll edge within about 0.3 s (9 frames at 30 fps) of an a-roll cut moves onto the cut's frame. A
  slice that starts on a line's first word starts on the line's cut, so the face never flashes for a
  few frames first
- Two B-roll slices side by side: the second starts on the exact frame the first ends on
- No segment under 9 frames at 30 fps, talking head or B-roll. Scene detection misses these (two takes
  of the same person look alike), so write every edge to `edges.json` (`{"aroll": [...], "broll":
  [...]}`) and let `cut-check.py` list them

**CPU budget (the lead strategist's PC gets loud).** Rendering is the only heavy part, so do as little of
it as possible:
- **Check without rendering first.** Caption chunks, wording and timing are checked from the text
  (`render.py captions` prints them). Caption placement is checked on 2-3 single frames, not a
  full render. Most fixes never need a video render
- **Preview small:** 540×960, `veryfast`, 2 threads. The full 1080×1920 render happens **once**,
  after the human has approved the preview
- **Render the video track once** and cache it (hash of captions + filter settings). Music options,
  mixes and loudness only re-encode the audio and copy the video in (`-c:v copy`): seconds, not
  minutes
- **Always low priority, half the cores at most** (`BELOW_NORMAL_PRIORITY_CLASS` on Windows,
  `-threads` = cores/2), so the fan stays calmer and the PC stays usable
- Check a render by measuring (ffprobe, volumedetect on 2-3 windows, a few frames), not by
  rendering again

**7. Render with ffmpeg: the hero first, the matrix after approval.** One script in the run folder
(`render.py`) renders the hero, and after approval every combination, with the modes `captions` /
`preview` / `final`, so a re-run after a small change is one command.
- **Cut edges come from the sound, then the frame.** The transcript's word times are close, not exact:
  a piece starts at the first sound of its first word and ends after its last, found with
  `silencedetect` (`n=-35dB:d=0.3` for the speech stretches, `-30dB:d=0.2` for pauses inside a take),
  not from the transcript alone. A breath or lip smack before the first word is not part of the piece;
  a quiet last word is. Snap every edge to a whole frame (start rounds down, end rounds up), or later
  joins drift by a frame or two and let stray frames through. Joints get a ~20 ms audio fade.
  Write the kept pieces as `clips.json` for `cut-check.py` (step 9)
- **Cuts:** on the word boundaries, padded ~0.1 s so words aren't clipped. **At the end of a sentence
  or a take, keep about 0.4-0.5 s after the last word's end time** (the transcript's end time clips the
  word's tail, and the line needs a beat before the next one), but never into the next spoken word or a
  restart. The lead strategist's rule, 14 Oct 2026: three endings in one ad were cut half a second too
  early. Render each block once to an intermediate file, then combine per version
- **Jump cuts and zooms.** Cutting stumbles out of one take leaves jump cuts (same framing, the
  head jumps). Hide each one, in this order: cover it with B-roll if the plan has some there;
  otherwise a **punch-in**: alternate between two framings only, full frame and ~110% centred on the
  face, switching at the cut, never inside a shot. No third punch-in level. A shot shorter than ~1 s
  gets no punch-in: merge it or cover it. Cuts between different takes or angles need nothing. The
  fast punch-ins also carry the 2-3 s pacing: cut them in the pauses between words (the lead
  strategist liked them, 14 Oct 2026). `edit-style*.md` can override the percentages
- **Slow push-ins** (the lead strategist, 14 Oct 2026; before that, zoom moves were banned after a
  practitioner saw erratic AI zooms): on the speaker during feeling lines (the problem, how she feels,
  the change), and on B-roll that would otherwise sit still. One steady push per shot, about 100 to
  108-112 % over 3-6 s, centred on the face, never in the same shot as a punch-in, never on every
  shot. Untested in our renders: ffmpeg `zoompan` with `d=1` shimmers at whole-pixel steps unless
  the input is scaled up first; check a strip before using it
- **Format:** the brief's aspect ratio (default 9:16, 1080×1920), 30 fps, H.264 + AAC, loudness
  about -14 LUFS
- **Captions, styled by default:** an `.ass` file from the word timestamps, burned in. Chunks of
  2-4 words, bold sans-serif, white with a thick black outline, lower-middle, inside the one safe box
  of `safe-zones.md` (x 100-880, y 290-1340 at 1080×1920; measured on real phones in Oct 2026, one
  source). In the `.ass` style: Alignment 2, **MarginV at least 580** (the lowest line ends at y 1340;
  more sits higher), **MarginL 100, MarginR 200** (the like and comment column starts at x 886).
  Nothing else that matters (B-roll text, a picture-in-picture window, a card) outside that box
  either. `edit-style*.md` may move captions higher, never lower. Other formats: 4:5 feed, about 5 %
  margins. Rule history: bottom ~20 % until 10 Oct 2026 (MarginV 620), then top 14 % / bottom 35 % /
  sides 6 % from third-party guides (MarginV 700, MarginR 140; the right margin was too small),
  then the measured box on 25 Oct 2026. Max 3 words / 16 characters per chunk,
  always break at a full stop, small pop-in. Highlight key words by colour: **yellow** by default,
  **red** for the villain or something negative, **green** for the good or the solution (the lead strategist's
  preference, 2026-09-29). Style from `edit-style*.md` when set.
  Option "no captions" when the human will add platform captions in post
- **Also deliver** `captions-da.srt` per version, and for every preview a word file
  `<video stem>.words.json` (`[{"w": "word", "s": 1.23, "e": 1.5}]` on the video's own timeline) from
  the same word list the captions come from. No new transcription: the render knows which words are
  in the cut. The review page shows it as a live transcript line and stores the words with each note
- **Names:** `<brief-id>_H<n>_<length>s.mp4`, e.g. `B014_H3_15s.mp4`; with the concept ID from the brief header in front when the brief has one (`C07_B014_H3_15s.mp4`, see the brain's `idea-bank/concepts.md`). The ad's name in Ads Manager follows `brain-system/system/ad-naming-convention.md` (the handover lists it per file)

**8. Changes are re-renders, not a timeline.** The MP4s are the deliverable. When the human wants
something changed (another take, a shorter hook, a caption fixed), edit `edl.md` or the settings in
`render.py` and run it again: preview first, final once. No editing software is opened or written to.
**Every round is a new version, never an overwrite:** `<ad>_<hook>_v2_preview.mp4`, then `_v3`
(`python review-grid/notes.py next <run folder> <ad> <hook>` prints the next name), so the review page
shows them as v1 / v2 / v3 of one hook and the human can compare.

**Only on request: a file for a human editor.** When a human editor will finish an ad, hand over
the MP4, the `.srt` and the clean blocks from step 4 (any editor imports these). For DaVinci Resolve
or Final Cut, an FCPXML timeline in `timeline/` with cuts, B-roll on its own track and the `.srt`;
for Premiere, FCP7 XML. Untested until the human imports it once: say so in plain words, and never
call an unchecked file an editable project. (Writing CapCut projects directly was dropped on
2026-10-09, never run; see `feedback.md`.)

**Heavy edits → human editor.** `gaps.md` with timestamps and what's needed, plus the handover above.

**9. Check.** For each output, ffprobe the length, resolution and audio, and look at frames from the
start, the middle, every B-roll cut and every caption change: no black frames, no clipped words, B-roll
lined up with what's said, captions readable and in the safe area. Transcribe one full render per
hook and compare it with the EDL. Run `python cut-check.py --voice <audio> --clips clips.json --out
<preview> --edges edges.json --fps 30` on every version: PASS or fix first (a check not run is a fail).
It cannot hear a pause full of breathing, so also read the transcript of the cut: no gap between two
words over about 0.3 s (the held 0.4-0.5 s after a sentence's last word is the one exception). Then the **Frame check** (below) on the previews, before the human
sees them: the full check on one complete version, `--hook-only` on each other hook (the body is
shared).

**10. STOP: approval 2, the notes loop.** The edit review page (`review-grid/`, modelled on Alex
Cooper's): one tab per ad, v1 / v2 / v3 tabs per ad, Compare (two versions side by side), Approve.
The human pauses where something is off, presses **N**, types, **Enter**: the note is stamped to a
tenth of a second on that version ("0:18.6 on v2"), with a "general" tick for a note that holds for
every ad. Notes are saved in the run folder's `review-notes.json`, not copy-pasted.
- **Applying notes** (when the human says "apply the notes", adapted from Alex Cooper's apply-notes
  skill):
  1. `python review-grid/notes.py list <run folder>`: every open note with its version, time and the
     words spoken there
  2. Map each note to the edit's source (the EDL line, B-roll entry or caption) by its words, not
     the time alone: the times shift between versions
  3. Change the source (`edl.md`, `render.py`), never the exported MP4. Render the next version of
     every hook the note touches (a body note touches all of them)
  4. Check that each change landed: the frame check, and the new word file around the spot
  5. `notes.py reply <run folder> <id> "..."`: one concrete sentence per note, what changed, in which
     version, at the new time. A note that's ambiguous gets a question and `--keep-open`; a note that
     won't be done gets the reason
  6. A note ticked "general" or one that states a rule: propose it for `edit-style*.md` or
     `feedback.md` ("Learning"), shown to the human, never added unseen
  The page shows the answers within seconds, and a "v3 is ready" banner
- **QA notes:** frame-check findings the human should see can go on the page with
  `notes.py add <run folder> <video> <seconds> "..." --author QA` (blue edge, dismissable)
- **Repeat until the human approves a version.** Then build the matrix from the approved body
  (step 5, hero first), and check those with step 9
- **General notes** are the candidates for `edit-style*.md` or this skill's `feedback.md` ("Learning")
**Open it with `python review-grid/serve.py <run folder>`** (optionally `--checks checks.json`,
`{"<file>": "what the checks found"}`): it serves the previews on this PC only and opens the page in
the normal browser. Don't hand over `grid.html` as a file or open it in an app's HTML viewer: the
videos next to it won't load there. Start the server as its own process (on Windows `Start-Process`),
not a background job of the session: a session restart kills it and the videos stop loading
(happened 14 Oct 2026). It also writes `Open review.cmd` into the run folder: a double-click
starts the page again, or just opens it when it already runs. The page accepts changes only from
itself (a custom header and an Origin check), so another website can't write notes or approvals. A
hook counts as approved only while its approved version is the latest. Stop the server once every
hook is approved. Then run `ad-policy-check` on the picks that will run as paid ads (on-screen text,
captions, spoken lines, people, AI label), and `brief-check` Mode B on the picks if the human wants the full QA.

**11. Deliver** the picks (MP4 + `.srt`, plus the editor handover from step 8 if asked for) to the run folder, and upload through the "Raw
footage" or "Review tool" role only on yes.

## Frame check
Look at what was rendered the way a harsh motion director would, not a proud author, before any
human sees it. Adapted from the motion-design course's critique loop (movez Substack, Oct 2026), with
verdicts and evidence instead of its 1-10 scores, because a model scores its own work generously.
Used by this skill, `song-ads` and `motion-ads`.

1. **Sheets.** `python frame-check.py <preview.mp4> --strip <t> <t> ...`, with a strip at every
   fast moment (B-roll cut, caption pop, a card, a motion beat). It writes `frame-check/` beside the
   video: a contact sheet, phone-width sheets (360 px), the strips, and `report.md` with black
   stretches, still stretches of 2.5 s or more, and loudness. It decodes but never encodes video, at
   low priority: light on the PC
2. **Look at every sheet** and fill the verdict table in `report.md`: pass or fix, each with the
   time and sheet that shows it. A pass without a frame is not a pass.
   - **Hook:** frame 0 works alone (the thumbnail, muted autoplay): the message or product is on
     screen, not a logo, black or a fade from nothing; something moves by 0.5 s
   - **Phone size:** every word readable on the 360 px sheets without zooming
   - **Safe area:** no key text, product or CTA outside the box of `safe-zones.md` (x 100-880,
     y 290-1340 at 1080×1920), and nothing under a placement's covered area when the brief names one.
     Feed 4:5: about 5 % margins
   - **Something new every 2-3 s:** the report's "stretches with nothing new" (it counts visual
     changes, not movement, so a talking head with no cuts shows up) and the contact sheet. A
     stretch passes only as a planned hold (end card, CTA). The old still-stretch check passed an
     edit the human found far too static (14 Oct 2026); this one flagged 56 of its 67 s
   - **Motion:** in the strips, no text overlapping during swaps, no element popping in one frame
     by accident, no blurry text while scaling, no flash or black frames
   - **Product:** the same as in `assets/`, big enough to recognise at phone size
   - **Face:** in every strip and sheet, no graphic, card, picture-in-picture window or text over the
     speaker's face or mouth. The first thing to look at on a card laid over footage
   - **Generated clips:** a strip at the start of every generated clip. A warp or morph in its first
     0.5 s is trimmed, not regenerated (`production.md`, "Generated video clips"). No generated
     phone, app or website screen anywhere
   - **AI defaults:** centred title on a gradient, everything fading in, corner labels or frame
     borders, glow, particle bursts
   - **End:** the CTA readable and on screen long enough to read aloud
   - **Sound:** about -14 LUFS (report); cuts and hits on the words or the beat they belong to
3. **Fix the three worst**, re-render the preview, and run it again. **At most two rounds** (CPU).
   Then show the human, with anything still marked fix named, never hidden
4. **On the final render**, run `frame-check.py` once for the measurements only. No new looking
   rounds: the final is the approved preview at full size

## Learning
- Changes at approval 1 and feedback from the grid, with the reason → the brain's
  `edit-style*.md` if it's about this brand's style; `feedback.md` here if it's about editing in general.
  A grid note ticked "general" is a candidate for one of those; a note about this ad is applied and
  not kept. Write the candidates at the end of the run and show them: nothing reaches a style file
  or the skill unseen
- When an editor explains a cut out loud → save it in `craft-reasoning/`
- To train a style against ads the team already shipped, and to count versions to approval:
  `edit-training` steps 7-8
- Once a style is stable, the human can ask to turn it into its own skill (like Alex's
  "organic short-form edit"); until then, the style files do the job
- Consolidate after every third run: confirmed lessons move from `feedback.md` into this file

## Guardrails (never)
- Never change what someone says: no reordering words inside a sentence, no cutting "not" out, no
  stitching fragments into a line that was never said
- No AI-generated voice or face swapped onto a real creator's footage. An AI talking head is an
  invented person and is never presented as a real customer (a testimonial needs a real person)
- No other brand's ads, logos or content as B-roll in a paid ad for a brand. Showing an ad library
  is fine in organic content about advertising (the lead strategist's own content), not in a client's ad
- Never render over the raw footage or delete it. Output goes to the run folder only
- Claims in the edit, including in B-roll and captions, stay inside the brief's "Claims allowed"
- Music: only tracks the brand has the rights to for ads, or the platform's commercial library added
  at upload
- Never report a step as done that wasn't checked (the import test above is the classic case)

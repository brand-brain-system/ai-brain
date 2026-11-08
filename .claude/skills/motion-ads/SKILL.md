---
name: motion-ads
description: Turn an approved static ad into a short motion ad rendered from code (motion-ads, motion statics, animated static, animeret static, bevægelig annonce, kinetic type, motion graphics, hook card, end card, offer card, slutkort). Each page is a pure function of time, window.seek(t), rendered frame by frame with headless Chrome and ffmpeg, in 9:16, 4:5 and 1:1 from one timeline. Plans the motion beat by beat, checks stills, renders a small preview, looks at its own frames with the video-edits frame check, then renders the final once. Also makes transparent hook and end cards for video-edits and song-ads. Use when someone wants a picked static as a video, a motion version of a winning message, kinetic type, or a card to drop into an edit. No fal.ai spend. Does not edit footage (video-edits), make songs or generated clips (song-ads), or write new static copy (static-ads).
argument-hint: "[path to the approved static, or brief ID]"
---

# Motion ads

## Goal

Make a 6-10 second motion ad from a static that's already approved: same message, same words, same product, now moving. Or make a short card (hook card, end card, offer card) that `video-edits` or `song-ads` lays over or after their edit. Everything is drawn in HTML and rendered from code, so a change is an edit and a re-render, and the product and brand fonts stay exact.

The engine came from a motion-design course on Opus 5.5 (movez Substack, shared 10 Oct 2026): the `seek(t)` page, closed-form springs, the banned-defaults list and "make the model look at its own frames". It's rewritten here for Windows, for ads rather than showreels, and for the lead strategist's PC. The course's performance and "one prompt" claims are not used.

## What it can use

Always run inside a brand brain. Read these before step 1. Say which are missing, and what that blocks.

- **The approved static:** its run folder from `static-ads` or `offer-ads`: the HTML, the PNG and its ad record (`production.md`, "The ad record"). The motion ad uses its words and its layout. No approved static: write the copy with `static-ads` first. This skill doesn't write new ad copy
- **Brand DNA:** `brand-context/brand-one-pager.md`, for fonts (the real font from the site) and hex colours
- **Product images:** `assets/`. The product is the real photo or cut-out, never redrawn
- **Claims gate:** `brand-lens.md`. Every word on screen is either the approved static's copy or inside "Can claim"
- **Offer facts** (offer ads): the `offer-ads` fact list for the static. Prices, dates and codes are copied from it, never retyped
- **Concept register:** `idea-bank/concepts.md`. The concept ID goes in front of every file name. The ad's name in Ads Manager follows `brain-system/system/ad-naming-convention.md` (the handover lists it per file)
- **Music:** only a track the brand has the rights to for ads, or none (the platform's commercial library is added at upload). No synthesized music or sound effects
- **Brand feedback:** `running-notes/feedback.md`, and this skill's own `feedback.md`
- **The engine, in this skill's `lib/`:**
  - `template.html`: the starting page. Format switch (9x16, 4x5, 1x1), safe-area guide, font and image loading, render-mode guards, a live preview with scrubbing
  - `motion.js`: springs with named feels, `track()`, `stagger()`, `swapAlpha()`, `rng()`, `set()`
  - `render.mjs`: `node render.mjs index.html --format 9x16 --scale 0.5` renders the preview. `--stills 0,1.5,4` writes single frames, `--scale 1` is the final, `--alpha` gives a transparent ProRes 4444 `.mov` for cards, `--audio` adds a track at about -14 LUFS. No npm packages: it drives the installed Chrome (or Edge) directly. Tested 10 Oct 2026: 8 s at 540×960 in 6 s
- **The frame check:** `video-edits` SKILL.md, "Frame check", and its `frame-check.py`

## Modes

- **Motion static** (default): one approved static → a 6-10 second ad in the brief's formats
- **Card**: a hook card (kinetic type over the first 1-2 s of footage) or an end card or offer card (product, offer, CTA, 2-3 s), asked for by `video-edits` or `song-ads`. Render with `--alpha` when it goes over footage. Transparent background: set `#stage` and `body` to `transparent` in the page. A card over footage keeps clear of the speaker's face and mouth: look at a frame of the footage at the card's start, and lay the card out in the rest of the frame
- **Format set**: an approved motion ad re-laid out for another format. Reframe each element in the page's layout table (`L`); never crop one format into another

## How this skill runs

1. **Check the inputs.** Read everything above. Copy `lib/template.html` (as `index.html`) and `lib/motion.js` into the run folder, so the run doesn't depend on later changes to the skill.

2. **Plan the motion: a beat table.** One row per beat, 0.3-1.5 s each: time, what moves, which feel (below), and what the viewer should understand by then. The rules:
   - **Frame 0 works alone.** The first frame is the thumbnail and the muted autoplay's first impression: the static's message is on screen at t = 0, not a logo, a blank or a fade from nothing. The course called "everything fading in" the commonest AI default. Here the hook is there from the start and motion adds to it
   - **Something new every 1-2 seconds**, and nothing moves just to move. Each beat earns its place: the product arrives, a benefit lands, the price hits, the CTA settles
   - **The product is the hero.** Large, centred or clearly placed, on screen by about 1 s
   - **The CTA holds about 2 seconds.** Long enough to read, short enough not to be a dead end
   - **6-10 seconds in total** for a motion static (our default, not a proven length)
   - The copy is the approved static's, word for word. A new word goes back to `static-ads`'s copy checks first
   - The beat table goes in `motion-plan.md`, with formats and music (track or none)

3. **STOP: approval 1, the motion plan.** Show the beat table beside the static. Small (a few lines). The human changes beats, order or length. Log the reason for each change in one line in `run-notes.md`.

4. **Build the page.** Put the static's elements into `index.html`, each absolutely positioned, with positions per format in the layout table `L` and inside the safe area. Fonts: list every font and weight in `FONTS`. Motion only through `motion.js`:
   - **Feels:** `snappy` for buttons, chips and price hits; `default` for cards, containers and the camera; `heavy` for big type, the product and logos (no visible overshoot); `playful` for stickers and badges only (visible overshoot, sparingly)
   - A value with more than one target uses `M.track()`, never restarted springs
   - Text inside a box that changes uses `M.swapAlpha()`: in after the change starts, out before the next
   - Move words in a line with a lift (`y`), not a scale: scaling pushes them into their neighbours
   - **Banned** (the course's list plus ours): centred title on a gradient, everything fading in, corner labels and frame borders, glow on UI, particle bursts, slow Ken Burns drift on the product, 3D spins with no reason, bouncy easing on type, `will-change` on anything that scales (blurry text)
   - **The render contract:** `window.seek(t)` paints the frame for t. No CSS transitions or animations, no timers, no state carried between frames, no `Math.random` (use `M.rng(seed)`). Render mode enforces the last two and fails loudly

5. **Check stills before any video.** `node render.mjs index.html --stills <one time per beat>` for each format. Look at every still against the beat table: layout, overlaps, safe area (press `g` in the live preview for the guide), the product. Fix here; it costs a second, not a render.

6. **Preview and frame check.** Render the preview (`--scale 0.5`, 30 fps) of the main format. Run `frame-check.py` on it with `--strip` at the fast beats, and do the "Frame check" from `video-edits` SKILL.md: verdicts with the time that proves them, fix the three worst, at most two rounds. Then the other formats as stills only, unless the human asks for their previews.

7. **STOP: approval 2, the preview.** Show the preview MP4, the contact sheet and the filled verdict table, including anything still marked "fix". The human picks changes; edit `index.html` and repeat step 6 for the changed beats.

8. **Final render, once per format.** `--scale 1`, 30 fps; `--sub 2` (motion blur) only if the strips show the fast beats stutter. Add the music with `--audio` if there is a track. Then run `frame-check.py` once on each final for the measurements only (length, black, still stretches, loudness). No new looking rounds on the final: it's the approved preview at full size.

9. **STOP: approval 3, the finished ads.** Run `ad-policy-check` on them first and show its line per ad with them. Deliver to the run folder only. Log lessons: this brand in `running-notes/feedback.md`, motion ads in general in this skill's `feedback.md`.

## Output structure

### The run folder

`sprints/<sprint>/video/<YYYY-MM-DD>-<brief-id>-motion/`, holding:
- **`index.html` + `motion.js`**: the film. Opening `index.html` in a browser plays it live
- **`motion-plan.md`**: the beat table, formats, music, and the static it comes from (path)
- **`stills/`** from step 5, **`out/`** with previews and finals, **`frame-check/`** per preview
- **`run-notes.md`**: every change at a stop with its one-line reason, and the frame-check verdicts per round
- **The ads:** `<concept-id>_<brief-id>_motion_<format>_<seconds>s.mp4`, e.g. `C07_B014_motion_9x16_8s.mp4`
- **Cards:** `<concept-id>_<brief-id>_card-<hook|end|offer>_<format>.mov`, handed to the `video-edits` run folder that asked for them

### The reply at each stop

What was made, what the frame check found and fixed, what's still open, and the question for this stop. At the end, "what I need from you" as in the brain's CLAUDE.md.

## Hard rules

- **The approved static's words, or nothing new without the copy checks.** Prices, dates and codes are copied from the offer fact list
- **The real product.** The photo or cut-out from `assets/`, never redrawn, never changed in shape, colour or label
- **Real fonts and colours** from Brand DNA. A missing font is a stop, not a substitute
- **Light on the PC.** Stills before video, preview at half size, the final once, at below-normal priority (the renderer does this itself), as in `video-edits`'s CPU budget
- **Nothing leaves the run folder.** No upload, no post, without a separate yes
- **No performance claims.** A motion version is a format to test, not proof it will beat the static

## When NOT to use this skill

- There is no approved static or message yet: run `static-ads` or `offer-ads` first
- The ad needs filmed footage, a creator or a talking head: `video-edits`
- The ad needs generated scenes, characters or a song: `song-ads`
- The message belongs to its format (a long native story won't survive as 8 seconds of type): say so instead of forcing it
- Masks, keying, subject tracking or 3D product renders: those go to a human motion designer

$ARGUMENTS

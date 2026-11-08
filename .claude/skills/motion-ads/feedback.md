# motion-ads: feedback log

What we've observed on real runs. A log, not a rulebook. After every third run, confirmed lessons
move into SKILL.md.

## Engine tests (10 Oct 2026, placeholder page, no brand)

- `render.mjs` on Windows with the installed Chrome: 8 s at 540×960, 30 fps in 6 s; stills, 4x5 and
  1x1 layouts, and a transparent ProRes 4444 card all worked. Poppins from Google Fonts loaded
- The first frame check on the placeholder caught two real flaws: scaling words in a headline made
  them collide at 0.5 s (now a lift), and a 3.2 s still end (now DUR 7 with a ~2 s CTA hold)

## Open checks before the first real run

- Not yet tested: `--audio`, `--sub 2`, an `<img>` product cut-out with transparency, a card laid over
  real footage in `video-edits`
- 9:16 safe area is now the measured box x 100-880, y 290-1340 (`safe-zones.md`, 25 Oct 2026, one source, an iPhone creator's screenshots), not Meta's own page. The template's `g` guide was rewritten for it and is not yet looked at in a browser

## Tools looked at (4 Nov 2026, from a public list of 20 open-source motion tools; none tried)

- **Worth a test:** Lottie (`airbnb/lottie-web`, MIT) for animated icons and stickers on cards. It
  can jump to an exact frame (`goToAndStop`), so it fits `window.seek(t)`; the test steps are in
  `REWRITE-QUEUE.md` section 13A. Anime.js (`juliangarnier/anime`,
  MIT) only if `motion.js` gets too thin for longer timelines; its timelines can also seek
- **Not taken:** Remotion: our engine already does what we need, and Remotion asks for a paid
  company licence above a few employees (check its licence page before anyone builds on it).
  Three.js and its add-ons, Blender MCP, Jolt Physics, the GPU path tracer and ComfyUI: 3D and local
  GPU work no skill asks for, and heavy on a teammate's machine (factory rule 7). Manim: explainer
  diagrams, revisit if a brand needs a mechanism animation. Motion and Tweakpane: web UI tools, not
  render tools. OBS and LosslessCut: tools for a human, ffmpeg covers our side

## Runs

_(none yet)_

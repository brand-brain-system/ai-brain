# song-ads: feedback log

What we've observed on real runs. A log, not a rulebook. After every third run, confirmed lessons
move into SKILL.md.

## Open checks before the first paid run

- Do the music models sing Danish well enough for an ad? Test both on the 15-20 second sample of the
  first Danish run, and log which held up. Untested as of 7 Oct 2026
- Commercial-use terms for generated music (ElevenLabs Music, MiniMax Music) in paid ads: not checked.
  Read them before the first ad goes live
- What a 480p Seedance draft really costs per second: unknown until the first draft (step 9)
- How well `bytedance/seedance-2.5/reference-to-video` holds a character and follows a storyboard
  grid's shot order: untested (schema checked 11 Oct; multi-shot takes go this route since then)
- Time per stage: none logged yet. The first three runs set the time standard (`production.md`,
  "Paying for generation")

## Open tests from Alex Cooper's Singing Ads System (2026)

From his public Notion "The Complete AI Ad Stack" (read 17 Oct 2026). Stated: his production
notes, made with Suno and Seedance 2.5 on EcomBos, none run by us. Each moves into `SKILL.md` once
it has held on a second brand (factory rule 6).
- **The brand name sung wrong (step 6).** When the transcript shows the brand name misheard, fix
  only that word: respell it the way it should sound, with hyphens between syllables and the
  stressed syllable in capitals (his example: Luminessa → loo-MIN-ess-a), give it a line of its
  own, and regenerate only that section (one chunk of the ElevenLabs composition plan), with the
  style text unchanged. Never turn the whole lyric sheet into phonetics. Captions keep the real
  spelling. Likely needed on every Danish name; log each respelling that worked
- **Lyric rules (step 3).** Lines of 3-8 words; every line describes something that can be shown;
  the brand name sung clearly at least once, on its own line; the first line is the hook, with no
  warm-up line. Check each against the shot plan before approval 1
- **Singing from the first second (step 6).** Start the lyrics on a sung section and trim any
  leftover intro in ffmpeg. Don't write "no intro" in the style text: he found negative style
  words backfire. Log whether ElevenLabs' first chunk starts on the voice
- **One portrait per character, or a sheet (step 7).** Our step 7 makes a sheet per character and
  feeds it to reference-to-video. His singing and drama runs (Seedance 2.5) say a multi-image sheet
  made the model mix characters up, and that one clean portrait per character on a plain background
  fixed it (he reports 120+ credits lost across three attempts first). His Pixar and claymation pages
  recommend multi-angle boards instead, so the stack contradicts itself. **The test:** on the first
  multi-shot take, draft it at 480p both ways (sheets vs single portraits, same storyboard and
  prompt) and keep the one whose faces hold. He also found that pointing at the style image beat
  describing the look in words; our clip prompts already describe motion only (`production.md`)
- Describing the camera's position, and rewording a refused image: open tests in the `static-ads`
  skill's `feedback.md`; they apply to the storyboards too

## Runs

_(none yet)_

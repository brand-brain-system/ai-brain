# Intake: from what was handed in to a list of claims

## Input

Whatever the owner hands in: pasted posts, prompts, screenshots, an infographic, links, PDFs, videos or transcripts. Often several at once.

## Steps

1. **Save a working copy of each source in the session's scratchpad**, never in the repo. One file per source: `sources/S01-<short-slug>.md`. Put at the top: the kind of source (post, prompt,
   infographic, video), the date it was handed in, the link if there is one, and the author's role if it is known ("a media buyer", "a creative strategist"). No name is needed (the owner
   decided crediting by name isn't needed).
   - Pasted text: save it as given.
   - A screenshot or infographic: read it and write out what it says, box by box.
   - A link: fetch it and save the readable text. If it is behind a login or a wall, say so and ask for a paste.
   - A PDF: read the pages that matter; note the page numbers.
   - A video: get the transcript (captions, or a transcript the owner gives); note the timestamps of the parts that carry a method.
2. **Split each source into its distinct claims or methods.** One line each, in plain words, in the factory's voice, not the source's. A claim is one thing that could be true or false, or
   one method that could be tried. A list of ten tips is usually eight claims (two repeat).
3. **Number them** `S01-1`, `S01-2`... so every later table can point back.
4. **Mark the kind** of each line: `method` (a way to do something), `definition` (a name for something), `number` (a stated result), `tool` (a product or route), `rule` (a must or must not).
5. **Mark what it rests on:** shown data, one practitioner's experience, or nothing stated. Every claim is labelled **Stated** at this point (`system/evidence-and-labels.md`); nothing
   becomes Verified because a practitioner said it with confidence.
6. **Drop** what is pure promotion (a course pitch, "DM me"), and say what was dropped in one line.

## Output

`claims.md` in the scratchpad: a table with `id | claim (our words) | kind | rests on | source`. This is the input to `map-against-factory.md`.

## Rules

- Never copy the source text into the factory. The working copy is for reading; what ships is rewritten.
- A number from a source stays the source's number ("one practitioner reports a 2x hook rate"). It never becomes a benchmark without our own data.
- If two sources disagree, keep both lines and mark the conflict. The next step decides.

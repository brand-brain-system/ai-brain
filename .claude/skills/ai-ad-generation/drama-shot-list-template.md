# <Concept ID>: <title> (AI drama shot list)

Used by `processes/video-ai-drama.md`. Copy into the run folder as `shot-list.md` and fill it in.
The shot list is the single source of truth for the drama: every frame prompt, clip prompt and fix
is rebuilt from it, so edit the shot here first and regenerate from it, never patch a prompt alone.

## The brief

| Field | Value |
|---|---|
| Story idea | Who, the conflict, where the reveal lands (2-4 sentences) |
| What the viewer should come away knowing | The one product belief, in plain words |
| Offer / CTA | Optional; where it lands in the story |
| Persona | From `personas/personas-profile.md` |
| Length | Long cut in seconds; cutdown lengths |
| Aspect ratio | 9:16 / 4:5 / 1:1 / 16:9 |
| Image model / video model | Chosen at run time with `recommend_model` |
| Resolution plan | Draft resolution, upscale target |
| Language | Spoken language; untested languages get one test clip first |
| Product reference image | Path in `assets/`; one clean image of the pack |

## Pronunciation

How the video model should say names it is likely to mangle. Write the respelling used in every
dialogue line that contains the word.

| Word | Respelling in prompts |
|---|---|
| <product name> | <phonetic spelling> |

## Cast

One row per speaking character. The sheet and identity part follow `production.md`, "An AI person
who stays the same". The wardrobe colour is the character's handle in every prompt and fix.

| Character | Role in the story | Age / look (identity part) | Fixed wardrobe | Sheet | Approved |
|---|---|---|---|---|---|
| | hero | | | `assets/people/<name>/sheet.png` | |
| | rival | | | | |
| | confidant | | | | |

## The world

The visual guide: one approved frame that sets the look of every setting (light, palette, realism,
lens). List each location and the time of day it is in.

| Location | Time of day | Visual guide frame | Approved |
|---|---|---|---|
| | | | |

## Beats

The story in 5-8 beats before it becomes shots: setup, the open question, the escalation, the turn,
the reveal, the payoff. The product enters at the turn or later.

1.
2.

## Shots

One row per shot. One speaker per shot; a line short enough to fit the clip. `Keep` marks the
shots a cutdown can't lose.

| # | Beat | Shot title | A/B | Sec | Speaker | On cam | Line (with delivery) | Product | On screen (and who faces whom) | Visual direction | Keep | Frame | Clip |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | | A | | | yes | "" (warm, teasing) | no | | | yes | | |
| 2 | 1 | | A | | | | | | | | | | |

Frame and Clip columns: `todo`, `draft`, `fix: <reason>`, `approved`.

## Continuity log

Run after the frames are made and again after the clips. One line per problem: the shot, what is
wrong, the fix sent, the result.

| Shot | Problem | Fix sent (prompt + reference image) | Result |
|---|---|---|---|
| | | | |

Things to check on every shot: who is sitting and who is standing, who faces whom (eyes on the
other character, not the lens, unless the shot speaks to camera), where each character is in the
room, props in hand, wardrobe, time of day, the product's pack, and that a scene's staging still
makes sense against the shot before it.

## Cutdowns

| Version | Length | Shots used | Hook variant |
|---|---|---|---|
| Long cut | | all | H1 |
| | | | |

---
summary: "How generated ads are made: prompt anatomy, model settings, rendering and fixes, paying for generation (quote, repair budget, cost log), generated video clips, an AI person who stays the same. Shared by the static, offer, video, song and motion skills."
---

# Production: how an ad gets made

Owns the technical side of every AI-generated ad: the static-ad skills (`static-ads`,
`offer-ads`) and every generated clip (`video-edits`'s AI modes and B-roll, `song-ads`):
building prompts, model settings, rendering text, fixing errors, and paying for generation. What the
words say lives in the skill's `copy-guide.md`; what the ad must look like and the final check live
in `design-principles.md`. Every category's `prompts.md` follows this file.

## Paying for generation
Every skill that spends on fal.ai follows this. From Lorenzo Pravata's AI ad pipeline (Oct 2026, one
team's practice: Stated).
- **The quote:** units × the price from `get_pricing`, plus a repair budget of 25 % on its own line.
  Something always gets redone, so a quote without it is too low. Unknown prices are written as
  unknown, never as zero
- **The repair budget is approved with the quote.** It may be spent without asking again, but only
  on outputs that fail a check: the product changed, broken hands or faces, a warp, wrong text, a
  black or frozen stretch. Each repair is listed afterwards with its reason and price. A change of
  taste or direction is a new spend and asks first. Budget used up: stop and ask
- **The log:** `costs.md` in the run folder, per stage (images, repairs, clips, tests): quoted, real,
  and the clock time from start to finish of the stage, including the time spent waiting for a human.
  The first three runs of each format set our own time standard; until then, quote no times to
  anyone

## The default build: real image, rendered text
The image is the hook; the text is exact. So the default is the brand's real image (or a generated
one when none exists) with the text laid on top in HTML. HTML gives exact text, full control of
sizes and costs nothing. Let the image model write text only when the text is part of the scene
(handwriting on a post-it, a label). (test 28 Sep) A phone, app or website screen is never generated:
models get them wrong. Lay the real screenshot in with HTML, or turn the screen away from camera.

## Building a generation prompt
1. Start with the brand's image generation prompt modifier from `sub-context-docs/brand-identity-analysis.md`
2. Then: "Use the attached images as brand reference. Match the exact product design, packaging,
   colors and typography precisely." Some prompts replace this with a "Reference use" line (e.g.
   product color only, for native looks). Follow the prompt's own line when it has one
3. Then the template prompt with every gap filled
4. Attach the product photos and the real logo from `assets/`. Upload local files with fal
   `upload_file` (prepare, then PUT). Without the uploaded logo the model invents a wordmark (test 19 Sep)
5. Aspect ratio is a model parameter, not prompt text. "Suggested ratio" in `prompts.md` is a default
6. When the model writes text, attach the brand's type sheet ("Brand fonts" below) and write "FONT
   reference only, do not place it in the ad"
7. When the prompt describes a scene (the `ai-visual` prompts, lifestyle settings), attach one of the
   brand's own photos as a style reference for light, grain and depth, if it has any. A scene
   described from nothing comes out looking like stock (Madvera image-ad skill, 2026)

## Writing a standalone prompt (prompt pack, and any model-written layout)
A prompt that leaves the building (the `static-ads` prompt pack, a prompt handed to a
colleague's Higgsfield) has to work alone: no "see above", no blanks. Adds to the steps above, from
Alex Cooper's prompt anatomy (static-ad engine, 2026):
- **Reference line by format:** full-brand formats match product, colors and type; native and UGC
  formats use the product's "color and packaging ONLY. Do NOT use ad layouts or polish"; no-product
  curiosity formats use the brand for "visual tone ONLY. Do NOT include any product, logo, or branding".
  Leave the prompt modifier out of native formats: polish breaks the realism
- **Layout in zones with proportions:** "Top third:", "Left 55%:", "Bottom 20%:", with every element's
  position, relative size ("at least 35% of the frame height") and what overlaps what
- **Text elements:** every text in double quotes, verbatim, with weight, case and color per element.
  Fewer elements render better: a layout with six or more text elements is a candidate for two ads
- **Realism cues for native formats** (this is what sells the one-shot): camera ("iPhone photo, slight
  sensor grain, subtle corner vignette"), composition ("slightly off-center, edge of product cropped,
  found rather than composed"), handwriting ("uneven lowercase marker, one word heavier from pen
  pressure"), physical detail ("crooked, a crease, held by wrinkled tape"), and no logo overlay
- **Congruency before it ships:** casting matches the persona (age, setting, wardrobe); the scene
  matches the headline (a line about stretch shows someone stretching); light matches the feeling
  (relief isn't moody shadows); nothing fights the format (no CTA button on a native look, no grain
  on a premium hero)
- **Close** with two to four mood words and the ratio, and set the ratio in the tool too

## Composing a generated scene for the layout
When the model makes the image and HTML adds the text (the default build), write the scene for the
layout it will sit in (the golf test brand, 6 Oct 2026: right on the first try once written this way):
- **Product in the centre, large:** say where and how big ("the phone and holder fill about half the
  frame height, centred"). The text zone is named and left empty ("top 35% empty sky, nothing in it")
- **No text in the scene at all:** "no text, no letters, no numbers, no logos, no watermarks"; a screen
  in the scene shows a picture with "no readable text"
- **Unfamiliar product in use:** attach the brand's own in-use photo as the composition reference next
  to the product photo, and say which image is which ("Image 1 is the exact product; Image 2 shows how
  it is used")
- **Dark product on a dark background:** name each part's colour ("thick glossy BLACK outer rim around
  a matte dark gunmetal face, not light grey"); otherwise the model lightens it
- Generate the scene once at the panel's own ratio (a 1080 × 806 photo under a 544 px text panel is
  4:3), then lay the panel and text over it in HTML

## A scene from a mood picture
For when a picture (Pinterest, a saved post, a photo the human likes) has the feeling we want but not
our product or person. Describe it; don't attach it: attached, the model copies the stranger, their
clothes and any brand or text in it. Adapted from Ecom Talent's "Scene Builder" Gem (course, 2026);
Claude reads the picture itself, so there's no Gemini step.
- **Write the scene in four layers, in this order:**
  1. **Action and pose:** a candid moment mid-action (holding, pouring, adjusting), and where the eyes
     go. Not a pose for the camera
  2. **Wardrobe:** fabric, fit and colour ("ribbed cream knit tank", not "a top"), plus one or two
     props that place it in a real day (a takeaway cup, over-ear headphones)
  3. **Place and light:** the room or spot, two or three concrete objects behind the subject, the
     light source, its direction and colour temperature
  4. **Camera:** by format, below
- **Take the why, leave the who.** Keep the light, distance, angle, palette and where the subject sits
  in the frame. Drop every face, person, logo, readable text, other brand's product and recognisable
  place
- **Our layout and persona win.** Subject position and the empty text zone come from the template
  ("Composing a generated scene for the layout"); casting and wardrobe from the persona (the
  congruency rule above). Where the picture disagrees, follow the persona and layout
- **Camera by format.** Native and UGC looks: "shot on an iPhone, handheld, slightly off-center,
  light sensor grain, unedited look", plus the one or two flaws the moment would really have (motion
  blur only where something moves, a reflection only in a mirror shot). Piling on every flaw may read
  as a filter: untested, log the first result in the skill's `feedback.md`. Premium looks: a lens and
  light instead ("85mm, soft window light from the left"), no grain. Leave out "8K", "masterpiece",
  "Octane/Unreal render": they come from older models and likely pull a photo towards a 3D render
  (not tested)
- **Product in a hand:** use a mood picture where someone holds the same kind of product (a pouch, a
  bottle, a club); grip and hands come out more natural (Ecom Talent). Our product still comes from
  its photo: "Image 1 is the exact product"
- **Ad record:** the mood picture's link and the scene text, not the picture as a reference

## An AI person who stays the same
For an invented person who appears in more than one ad for a brand (a model in lifestyle statics, a
face in B-roll). Person and scene are two separate parts that never overlap, so a scene can't change
the face (Ecom Talent's Scene Builder: the scene part never mentions face or skin).
- **Cast from the persona:** age, setting and style from `personas/personas-profile.md`, not a stock face
- **Identity part, written once:** age, build, hair cut, colour and texture, skin tone, two or three
  distinctive features that lock the face (freckles across the nose, a small scar in one eyebrow), and
  the skin realism: "visible pores, faint redness around the nose, natural unevenness, no retouching"
- **Scene part, every time:** the four layers from "A scene from a mood picture", with no face, skin,
  age or hair colour in it. How the hair is worn that day (wet, tied up) may go in the scene
- **The image carries the identity; the text backs it up.** Make a reference sheet once (front,
  three-quarter, profile; same light; plain background) and get it approved. Save it with the identity
  part in `assets/people/<name>/` (`sheet.png`, `identity.md`). Every generation: attach the
  sheet, write "Image 1 is the person: keep face, hair and build identical", then the identity part,
  then the scene part. Several images in one run share one sheet, never a new face per ad
- **Plastic skin:** fix it in the prompt first (the skin realism line, the phone camera). Still
  plastic: a skin-detail upscaler on fal (`recommend_model`, price first). Ecom Talent uses Topaz
  Gigapixel ("Redefine realistic", 2x or more) for the same job
- **Model:** the course doc names Seedream v4 for a sharp face and Flux SRPO for an organic look (both
  2025). Choose at run time with `recommend_model`, and log which model held the face across a batch
  in `feedback.md`
- **Guardrails:** an invented person, never a real person's likeness. A model in a scene, not a
  witness: no quotes, reviews, before/after or first-person claims, and never presented as a customer
  or staff (misleading testimonials under the Danish marketing law). A photorealistic AI person or a
  realistic AI voice carries a visible label in the asset from its first frame (EU AI Act art. 50,
  since 2 Aug 2026: `legal-ai-ugc.md`, EU section), and the platform's own AI switch is checked in
  `ad-policy-check` before launch

## Open test: describe the product, or only reference it
Some prompts describe the product (pb-32, pb-40: packaging colors, label text). The Madvera image-ad
skill (2026) says the opposite: name the product, attach the photo, and write "place it as-is; do
not redraw or change the product or the text on its packaging", because describing it makes the model
redraw it. Our logged errors fit that (a count that drifted, a wrong number on a pack, misspelled
packaging text), but they don't prove it. **Next batch with the product in a scene:** 2-3 ads each
way, same template and model, compared with the product photos in step 7. Log the result in the
skill's `feedback.md`, make the winner the rule here, and delete this section.
- **Both arms start from the same clean product photo:** white background, PNG, upscaled when it's
  small (Ecom Talent's first two steps)
- **The "describe" arm, done properly** (Ecom Talent's product Gems describe it before every edit):
  shape and proportions, material and finish (matte, glossy, brushed), every colour by name, every
  label text in quotes exactly as printed, counts. Describe it; don't restyle it

## Filling the gaps
- `[GAP]` takes the approved copy exactly, character for character. One extra full stop and a quote
  is no longer verbatim (test 19 Sep)
- **Must be sourced** in each prompt lists gaps that need a real source. No source: cut the element
  from the layout
- Write every name, date, number and count into the prompt explicitly ("exactly four pieces").
  Models copy text from reference images (a real customer's name from a product photo ended up on a
  generated spoon) and drift on counts (four pieces became five) (test 19 Sep)

## Reference images
- The template image is an optional layout reference. Leave it out when it shows another brand's
  name or text
- The offer templates are Figma board screenshots with an "EXAMPLE" label and frame: crop to the ad
  itself before attaching one
- Small engravings or print on a product become unreadable when the product is small in the frame.
  Make it large, or add it afterwards from a real photo (test 19 Sep)
- **File format:** convert .avif and anything else that isn't JPG, PNG or WebP to PNG before upload
  (`python -c "from PIL import Image; Image.open('in.avif').save('in.png')"`; Pillow 12.3 reads AVIF
  on this PC). Shopify sites often serve AVIF, and Seedance 2.5 accepts JPEG, PNG and WebP only
  (schema checked 11 Oct). Save the PNG in `assets/` next to the original

## Brand fonts
Exact text in the wrong font still looks off-brand: Nano Banana chose its own font on 28 Sep. Method
from the Madvera image-ad skill (2026):
- **Find the real font, never guess from the look.** Which fonts the ads use comes from the brand's
  own ads (`sub-context-docs/brand-identity-analysis.md`). The name and file come from the brand's site: in
  the browser, `getComputedStyle(document.querySelector('h1')).fontFamily` (the first name in the
  stack), or the page CSS (`@font-face` sources, Google Fonts links). Note weight and case (watch
  `text-transform: uppercase`) per role: headline, subheads, body
- **HTML text layer:** load that font. Google Fonts by name; a self-hosted font from its `@font-face`
  file, for local rendering only (fonts are licensed: never pass the file on). For a client, ask for
  the files. No file: say so and name the stand-in in the ad record; never swap in a lookalike silently
- **Model-written text:** render one type sheet (each brand font at its real weight, one sample line,
  labelled by role, in the brand's case) to `assets/type-sheet.png` and attach it as a font
  reference (prompt step 6)
- Record the fonts and the sheet's path in `visual-vocabulary.md`

## The ad record
Next to every image that reaches the grid, save `<file name>.md`: concept ID, template id, persona, angle, the
exact text per slot, the full prompt, model and settings, reference images, any font stand-in, and
the fal endpoint, request ID and seed (the seed only when the model takes one). The record is the
recipe, so it holds the prompt as sent, not a tidied copy. The request ID is a backup:
`get_job_recipe` can return the exact inputs fal received, but only while fal still keeps them (its
lookup covers 90 days by default) and only when the payload was kept.
A revision rebuilds the whole prompt from the record with the change folded in. Never add "like
last time, but ...": the model has no memory of its last attempt, so write what the image should be,
not what to avoid. (Fixing one wrong word locally, per "Fixing a wrong text", is still fine.)

File names: `<nr>_<ratio>_<product>_<persona>_<angle>_<template id>`, ASCII only (æ, ø and å cause
PowerShell trouble), e.g. `3_4x5_Proteinbar_Morgenloeber_Maethed_pb-13`. When the brain has a
`idea-bank/concepts.md`, the concept ID goes in front: `C07_3_4x5_...`; a new persona × angle × offer that isn't
in the register yet gets a proposed ID there, marked "proposed", for the human to confirm with the
copy. Upload them to the ad account with the same names, and results can later be sorted by concept,
persona, angle and template.

**Everything else that is paid for** (a clip, a song, a voice, a character sheet, an AI person, a
start frame, generated B-roll) gets one entry per fal request in the run folder's `jobs.json`:
endpoint, request ID, seed, the prompt, the input files by name, what the output became (file name,
take or shot), draft or final, date and charge. Drafts, repairs and failed requests too: they are
what the repair budget in `costs.md` paid for. Write the entry when the request returns, not at the
end of the run.

## Model settings
- **Nano Banana 2** (`fal-ai/nano-banana-2`, `/edit` with reference images): use `resolution: "2K"`
  or higher; 1K gives 928 × 1152 px. It rendered Danish text including æ, ø and å correctly on the
  first try, but chose its own font and made small lines too small (test 28 Sep)
- **GPT Image 2.5 Flare Edit:** rendered Danish text correctly at medium quality (test 19 Sep)
- When a model writes text, give sizes as a share of the image height ("headline about 9 % of the
  image height, bottom line at least 3 %"). The minimum sizes are in `design-principles.md`
- Check `get_pricing` before a batch, and quote it per "Paying for generation"

## Generated video clips
For every clip made on fal.ai: B-roll, an AI person, an animated take. The skills own the steps;
this owns how a clip is built. Schemas checked 11 Oct 2026 on Seedance 2.5; re-check on every run.
- **Image-to-video starts on the exact image you give it.** The clip opens on that frame, and its
  aspect ratio follows the image (Seedance 2.5's `aspect_ratio` is fixed to `auto`). So the start
  image is one clean, full-bleed frame in the delivery ratio: never a storyboard grid, a character
  sheet or a collage. To land on a set frame (a product reveal), add `end_image_url`
- **Grids and sheets are references.** Reference-to-video takes up to 30 images, named @Image1,
  @Image2 ... in the prompt, with the aspect ratio set explicitly, plus audio references (MP3/WAV,
  1.8-30.2 s in total). fal's model notes say it often rejects images with human faces: fine for
  animated characters; a photoreal person goes image-to-video from a start frame
- **The prompt describes motion, not the picture.** One camera move, what moves in the scene, how
  fast ("slow push-in, steam rising from the cup, a hand lifts it"). The image carries the look, the
  characters and the product; describing them again makes the model redraw them. Lorenzo's team found
  simple clip prompts beat dense ones, and Seedance's own schema calls the prompt "the desired motion
  and action". For a multi-shot reference clip: the shots in order, each with its camera and action
- **Sound off unless wanted.** Seedance's `generate_audio` is on by default (same price): set it
  to false unless the brief wants the clip's own sound
- **One clip before the batch.** Its real charge sets the price for the rest. Speech or singing in a
  language other than English: one short test clip first, because models differ a lot by language
  (Lorenzo: Kling handles Italian poorly). Danish is untested on every model
- **Leave room to trim.** Generated clips often warp or morph in their first frames. Request whole
  seconds above the slot's length, and when only the start is broken, cut up to 0.5 s off with ffmpeg
  instead of paying for a new clip. The frame check (`video-edits`) looks at every clip's start
- **Log every request** in the run folder's `jobs.json` ("The ad record"), drafts and repairs too
- **No generated screens:** a phone, app or website shown in a clip is the real page captured in
  the browser and laid in with ffmpeg (`video-edits` step 6, B-roll type 2), or kept out of view

## Rendering HTML to PNG (Windows)
`msedge --headless=new --hide-scrollbars --force-device-scale-factor=1 --window-size=1200,1600 --screenshot=<file>.png <file>.html`,
then crop to 1080 × 1350 (or the format's size). The window size includes the browser frame, so a
window of exactly 1080 × 1350 cuts off the bottom (test 28 Sep). Load fonts from Google Fonts and
give them a few seconds (`--virtual-time-budget=6000`).

## Fixing a wrong text
Text a model got wrong is hard to fix with another edit (a doubled full stop survived a re-edit).
Fix it locally instead: cover the field with the background color and write the text again (HTML
overlay, or PowerShell System.Drawing). Safer and free (test 19 Sep)

**PowerShell gotchas:** save scripts with Danish text as UTF-8 with BOM, or æ, ø and å break in
PowerShell 5.1. Don't name a function `Erase` (alias for Remove-Item). Variables are
case-insensitive (`$W` and `$w` are the same)

## Adding a prompt for a new template
Show Claude the template image and ask for "the standardized prompt for this that works for any
brand", in the format used in the `prompts.md` files: layout in words, labelled gaps, a suggested
ratio, a Must be sourced line. Add it under "From our templates" with the id from `templates.csv`.

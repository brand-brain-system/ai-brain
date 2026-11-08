# AI visual: prompts

Four formats that only AI makes cheap: images that would need a special shoot, props or effects to
photograph. Rules for building the final prompt: `../production.md`. Where each idea comes from and
when to use it: "Make the invisible visible" and "Atypical text" in the skill's `design-principles.md`.

Sources: Alex Cooper's statics guide (2026, his favourite AI image ads) and Parker's format
definitions (`ad-formats\static\index.md`, "Atypical Text"; `visuals.md`, "Making the invisible
visible"), summarized in our own words. The web had almost no real examples of either format (search
30 Sep 2026: stock photos and polished ads only), so the templates below start as prompts, and
example images get added when we find or make good ones.

Rules on top of `production.md`:
- **The idea comes from customer language, not from us.** A sensation a customer describes ("it
  feels like needles"), a moment they name ("every morning in front of the mirror"). No quote, no
  image: surreal for its own sake is art, not an ad
- **Readable at feed size in half a second.** If the viewer has to work out what the picture means,
  it failed. One metaphor, not two
- **Claims stay inside the brand lens.** The format is loud, so the claim is tempting to make loud
  too. A health or cosmetic claim that isn't allowed in plain type isn't allowed on skin either
- **Attach a style reference** when the brand has its own photos (`production.md`, prompt step 7):
  it keeps the scene from looking like stock
- **No real people.** Bodies are generated or the brand's own consented photos. Crop tight (a foot,
  a shoulder, a hand holding still): generated hands and faces are where AI shows (test 19 Sep:
  hands and cutlery looked generated)

---

## From our templates

None yet. The three below are the starting templates.

---

## Our starting prompts

### AV1 · Invisible made visible
Suggested ratio: 4:5
Example image: none yet

What it does: shows a feeling or sensation that can't be photographed as a literal, physical image,
so the person who has it recognises it at once. The headline then names it in the customer's words.

Prompt: A realistic close-up photo of [BODY PART OR SITUATION where the problem is felt], shot like
a phone photo in [REAL SETTING], natural light, shallow depth of field. The problem is shown
literally as [PHYSICAL METAPHOR taken from a customer quote, e.g. small nails in the sole of a foot,
a heavy stone strapped to a back, a phone battery icon at 5 % over tired eyes], realistic and a
little unsettling, not cartoonish, not gory. Plenty of calm space [TOP / BOTTOM] for a headline;
no text in the image. [PRODUCT, if it appears: small, at the edge, not part of the metaphor.]

Headline: added in HTML afterwards (the default build). It names the sensation, ideally with the
customer's own words.

Must be sourced: the quote the metaphor comes from (source and month in the copy table).

### AV2 · Atypical text
Suggested ratio: 4:5
Example image: none yet

What it does: puts the headline on a real surface where no one expects ad copy, and the surface
itself belongs to the problem or the moment. The novelty of where the text sits is the hook.

Surfaces that fit Danish life (pick the one tied to the product's moment): a fogged bathroom mirror
after a shower, condensation on a cold window or a glass, frost on a car windscreen, breath on a
bus window, a finger written in dust or flour, sand on a beach, chalk on a pavement, marker or
lipstick on skin, a receipt, a steamed-up oven door.

Prompt: A realistic phone photo of [SURFACE] in [SETTING], [LIGHT], slightly imperfect framing so
it feels found, not staged. Written into the surface the way a person would really do it
([WRITING METHOD: a fingertip through the steam / a black marker on skin / a finger in the frost]):
"[HEADLINE, 3-7 words, exactly as approved]". The letters are uneven and hand-made but fully
readable, about [SIZE: 10-15 %] of the image height, placed [WHERE]. [PRODUCT, if it appears:
standing naturally nearby, e.g. on the sink shelf, sharp but not dominant.] No other text, no logo.

The text is part of the scene, so the model writes it (`production.md`, "The default build"). Check
it character for character, including æ, ø and å; two tries at most, then shorten the line or fix it
locally. Longer copy goes in the primary text above the ad, not on the surface.

Must be sourced: the headline, when it's a customer's words (source and month in the copy table).

### AV3 · Problem anatomy
Suggested ratio: 4:5
Example image: `sw-SW008-problem-anatomy-shoe-sole.webp` (an organic post, not an ad)

What it does: takes an everyday object the viewer knows by its outline, and fills that outline with
a literal, exaggerated version of what's hidden in it. Thin callout lines name each part. It works
for three reasons at once. The shape reads in half a second. Something that doesn't belong there
breaks the pattern (usually disgust, which holds attention). And the callouts turn the image into a
search, so people stay and read every label. It's AV1 with a diagram on top, and it suits unaware
audiences: it creates a problem the viewer hadn't thought about.

Objects that carry it: a shoe sole, a pillow, a kitchen sponge, a toothbrush head, a phone screen, a
reusable water bottle's lid, a washing machine seal, a dog's chew toy, a gym bag, a scalp or a patch
of skin seen up close. The object belongs to the problem the product solves (a doormat or indoor
shoes for the sole, a pillow protector for the pillow), and the product is **not** in the image; it
comes after the click or in a second ad.

**The positive version:** the same outline filled with what's good instead (a capsule, a bottle or a
bowl shaped from the real ingredients, each one labelled). Same mechanism, no disgust; for a brand
whose selling point is what's inside.

Prompt: A top-down studio photo of [OBJECT], seen [ANGLE, e.g. straight from below], centered on a
plain [PALE BACKGROUND COLOR] background with soft even light and a faint shadow. The object's outline
and surface texture [e.g. the tread pattern] stay intact and instantly recognizable at the edges.
Inside the outline, packed densely and realistically, is [WHAT'S HIDDEN, as physical things: e.g. a
cigarette butt, chewing gum, torn plastic, a crumpled receipt, mud, hair, mould spots], textured and
a little gross, not gory. The object fills about 70 % of the frame height, with empty space on both
sides for labels and above it for a headline. No text, no arrows, no logo.

Text and callouts in HTML afterwards (the default build): a two-line headline at the top with one word
in a meaningful colour (red for danger), and 6-10 short labels left and right, each with a thin line
ending in a dot on the part it names. After generation, read the image and place each dot on the
thing it points at; a line pointing at empty sole reads as fake.

Must be sourced: every label is a factual claim ("E. coli", "lead"). Each needs a real, dated source
(a study, an authority), or it's cut. The image may exaggerate, the labels may not. Health scares fall
under the Danish Marketing Practices Act like any other claim: no fear the facts don't back.

### AV4 · X-ray or cross-section
Suggested ratio: 1:1 or 4:5
Example image: none yet

What it does: shows a hidden cause in one second, the way a medical image would: the joint pushing
against a shoe, the clog below the skin's surface, the layer a scrub never reaches. From Alex
Cooper's Native Image Ads System (public Notion, read 17 Oct 2026), our words; untested by us. Fits
a hidden problem with a cause the buyer can't see (open test in the static-ads skill's
`feedback.md`). Fails for a problem that is only a feeling. In regulated categories it's the safer
choice than a transformation: education, not a promise.

Prompt: A [medical X-ray style image / clean educational cross-section diagram, professional
medical illustration style] of [BODY PART OR OBJECT], seen [WHERE THE CAMERA IS, e.g. top-down
through a see-through sneaker]. [THE HIDDEN CAUSE, described exactly: what presses on what, where
it sits.] A soft [red] glow on [THE POINT THAT MATTERS]. [For a cross-section: two side by side,
left [THE PROBLEM STATE], right [THE CLEAR STATE].] Realistic, not cartoonish, not 3D-rendered.
Calm space [TOP] for a headline; no text, no arrows, no logo.

Headline and labels in HTML afterwards. Never imply a permanent structural fix. If the model
refuses the image, see the open test on refusals in the static-ads skill's `feedback.md`.

Must be sourced: the mechanism shown is a claim. It comes from the brand lens or a real, dated
source, or the image isn't made.


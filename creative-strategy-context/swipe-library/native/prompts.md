# Native: prompts

Rules for building the final prompt: `../production.md`. Native ads look like a real post, not
an ad: phone-camera photos, platform UI, handwriting. Two rules on top of the general ones:
- No invented third-party accounts. A post or comment is either real (with permission for live
  use) or clearly the brand's own voice and handle.
- No logo overlay. The brand shows through the packaging, and the page name above the ad already
  says who's talking.

Related templates kept elsewhere because their main job is different: `offer/offer-049.png`
(post-it flash sale) and `testimonial/testimonial-21.webp` (handwritten note).

---

## From our templates

None yet. The four examples below are the starting templates.

---

## From the Adcrate playbook

### #20 · Editorial content card
Suggested ratio: 4:5
Example image: `pb-20-editorial-card.png`
Reference use: tone only. No polished ad layout.

Prompt: A full-bleed moody portrait of [PERSON in the world of the product], warm amber light,
50mm f/1.8, shallow depth of field, cinematic grade with warm highlights and cool shadows. Lower
45% is the text zone: a white rounded pill label "[CATEGORY TAG like TRENDING]" in centered
uppercase sans-serif, about a third of the frame wide. Below: a very large bold all-caps condensed
headline in white with key words in [HIGHLIGHT COLOR]: "[HEADLINE]", at least 35% of the frame
height. Bottom center: "[@BRAND'S OWN HANDLE]" in small white text. No product shot, no CTA, no
stars.

Must be sourced: any claim in the headline ("is blowing up on TikTok", "is replacing X") must be
true. Use the brand's own handle, never an invented culture account (the playbook version does).

### #29 · UGC + viral post overlay
Suggested ratio: 9:16
Example image: `pb-29-viral-post-overlay.png`
Reference use: product color only. No ad layout or polish; it must look native.

Prompt: A casual selfie of [PERSON] doing something mundane: [ACTION like brushing teeth]. iPhone
front camera, slightly grainy, home lighting, no professional setup. Overlaid in the center: a
realistic screenshot of a [PLATFORM like Reddit / X] post with [POST DETAILS like community name,
username, timestamp]. Post title in bold: "[OPINION HEADLINE about the problem the product
solves]". Post body: "[2-3 sentences]". The person seems to be reacting to it, not selling. No
product, no logo, no CTA. The hook is the opinion.

Must be sourced: a real post (with its real username and permission for live use) or clearly the
brand's own voice. Don't generate a fake post from a real platform user.

### #32 · Instagram Story with text bubbles
Suggested ratio: 9:16
Example image: `pb-32-story-text-bubbles.png`
Reference use: product color and packaging only.

Prompt: A casual iPhone photo of [HAND DESCRIPTION] holding [OUR PRODUCT with key packaging
details] at a slight angle over [SETTING like a clean desk with a notebook and a plant], natural
daylight, slightly warm, iPhone quality. Five Instagram Story text-tool bubbles with highlighted
backgrounds in varied colors, placed casually: 1 "[TOPIC + EMOJI]" large and bold; 2
"[EDUCATIONAL HOOK: a surprising fact about why the category matters]"; 3 "[WHY THIS PRODUCT: the
feature that makes it different, excited informal tone]"; 4 "[PERSONAL RESULT, first person, with
emoji]"; 5 "[SHORT ENDORSEMENT]". Hand-placed, not designed.

Must be sourced: the fact in bubble 2; bubble 4 is a real customer's or creator's words, used with
permission.

### #40 · Ugly post-it note on the product
Suggested ratio: 4:5
Example image: `pb-40-post-it.png` (the example adds a logo; our rule is no logo)

Prompt: A lifestyle product photo in [REAL-LIFE SETTING like a kitchen counter / bathroom shelf]
with [LIGHTING like soft daylight from a nearby window] and a naturally blurred background showing
[BACKGROUND DETAILS]. The frame is very slightly off-center, with the [LEFT / BOTTOM / RIGHT] edge
of the product slightly cropped; it feels found, not composed. Slight phone-camera grain and a
subtle natural vignette. Center, large and dominant: [FULL PRODUCT DESCRIPTION: packaging colors,
key label text, distinguishing features] on [SURFACE], angled slightly toward the viewer, with
[SCATTERED DETAIL like a few crumbs] around the base. Stuck on the front of the product: a
[POST-IT COLOR, yellow by default] square post-it, slightly crooked, realistic paper texture, one
horizontal fold crease, a slight curl at the bottom-right corner, held at the top by a small
wrinkled piece of [TAPE COLOR] tape. Handwritten in thick black marker, imperfect lowercase, not
centered or evenly spaced, one word slightly heavier from pen pressure: "[LINE 1: setup]" /
"[LINE 2: turn]" / "[LINE 3: punchline]" / "[LINE 4: optional final beat or emoji]". No signature.
The photo runs full-bleed to the bottom edge: no caption strip below it (Alex Cooper's picks
board, 16 Sep 2026: the strip "stands out and takes away from the image"). No logo overlay; the
brand shows only on the packaging. Name the exact surface the note is stuck to (the product's
front), or the model copies the reference's popcorn bowl (Honeylove run, 20 Sep 2026).
[MOOD: 3 adjectives].

Must be sourced: nothing numeric by default. The note's lines work best in real customer language.

---

## From Alex Cooper's Native Image Ads System (2026)

Five native looks from his public Notion "The Complete AI Ad Stack" (read 17 Oct 2026), written in
our own words. Prompt-only: no example image yet, and none of them has been run by us. Which one fits
which product is an open test in the static-ads skill's `feedback.md` ("pick the native format from
the problem type"). His rule for all five: one pain, one picture, one line. The image shows the
problem or a clue, not the product as hero; the caption does the selling (`copy-guide.md`, "Native
storytelling"). Every word on the image goes in quotes, exactly as approved, and is checked
character for character, including æ, ø and å.

### NI1 · Chalkboard lesson
Suggested ratio: 1:1 or 4:5
Example image: none yet
Fits: a myth to bust, or "the real reason" behind a problem the buyer has already tried to fix.
Fails when: the list is too long to read at thumbnail size (three lines at most).

Prompt: A real photo of a classroom chalkboard, written in white chalk with some dust and smudges,
square. At the top, a headline that reads exactly "[HEADLINE: the question or symptom in the
buyer's words]", with a simple chalk drawing of [THE MOMENT, described as one action, e.g. a dog
scratching behind its ear with a back leg]. Below it, a short chalk list of what it is not:
"[- NOT 1]" / "[- NOT 2]" / "[- NOT 3]". Then one line circled twice in chalk: "[THE REAL REASON]",
with a chalk arrow to a small doodle of it. At the bottom, a chalk box that reads "[PULL LINE, e.g.
Løsningen nedenfor]" with arrows pointing down. Real chalkboard photo, hand-drawn chalk look, all
text spelled exactly as written and clearly legible. No logo, no watermark, no other text.

Must be sourced: "the real reason" is a claim. It needs a source in the brain or the brand lens,
or it's cut.

### NI2 · Notebook sketch
Suggested ratio: 1:1 or 4:5
Example image: none yet
Fits: a simple "what you do / what it needs" contrast that explains a mechanism. Feels personal
and low-production.
Fails when: the point needs a real photo to land.

Prompt: A phone photo of a spiral notebook page lying on a desk, drawn and written by hand in blue
ballpoint pen. At the top, a headline that reads exactly "[HEADLINE]". Left, labelled "[LEFT
LABEL, e.g. det du gør]": a simple sketch of [THE WRONG WAY, as one pose or action], with an arrow
and the note "[NOTE]". Right, labelled "[RIGHT LABEL, e.g. det den har brug for]": [THE RIGHT WAY],
with the note "[NOTE]". At the bottom, the words "[PULL LINE]" circled in pen with an arrow
pointing down. Real notebook photo, hand-drawn ballpoint look, all text spelled exactly as written
and clearly legible. No logo, no watermark, no other text.

Must be sourced: the mechanism on the right side, from the brand lens.

### NI3 · Red-circle phone photo
Suggested ratio: 4:5
Example image: none yet
Fits: a visible problem the buyer would recognise in their own mirror (a bump, a stain, redness, a
worn spot). Cold traffic.
Fails when: there is nothing to see (a felt or hidden problem).

Prompt: A real, slightly imperfect phone photo of [BODY PART OR OBJECT, cropped tight to it only],
in [EVERYDAY SETTING AND LIGHT], shot the way a person photographs something to show a friend:
handheld, a little off-centre, unedited. [THE PROBLEM, described exactly: where it sits, its size,
its colour]. A hand-drawn red circle, as if added in a phone's markup tool, around [THE PROBLEM].
[OPTIONAL: one short handwritten-style red label "[LABEL]" next to the circle.] Plenty of calm
space [TOP / BOTTOM] for a headline; no other text, no logo. Nothing sensitive: no nudity, no
pinched skin.

Headline in HTML afterwards (the default build): the situation in the buyer's words, never an
assertion that the viewer has the condition (static-ads guardrails).

Must be sourced: the label, if it names a cause.

### NI4 · Notes app / text message
Suggested ratio: 4:5 or 9:16
Example image: none yet
Fits: "I've tried everything" and 3 am stories; low trust, high frustration.
Fails when: the ad has to explain a mechanism.

Built in HTML, not generated: a phone-style notes or message screen in the platform's look, with
the text set in a system font. Generated screens come out with gibberish text.

Must be sourced: the words are a real customer's, with permission (native rule above: no
first-person story we wrote). Without that, the note is visibly the brand's own voice, or the
template is skipped.

### NI5 · Review split
Suggested ratio: 1:1 or 4:5
Example image: none yet
Fits: "I did everything right" stories: the review names the villain, the image shows the hidden
side of the problem.
Fails when: no real review says it.

Prompt: A clean native ad image on a plain [WARM GREY] background, no people. At the top, a bold
headline that reads exactly "[HEADLINE]". Below it, two close-up photos side by side of the same
[SUBJECT]. Left, labelled "[LEFT LABEL]": [THE SIDE EVERYONE SEES]. Right, labelled "[RIGHT
LABEL]": [THE HIDDEN SIDE], with the camera position described exactly ([WHERE THE CAMERA IS and
WHAT FILLS THE FRAME]). [Leave the bottom fifth empty for the review strip.] Realistic photography,
not cartoonish, labels spelled exactly as written. No logo, no watermark, no other text.

The review strip (stars, the quote, first name) goes on in HTML, in neutral styling: no review
platform's logo or star graphic (static-ads guardrails).

Must be sourced: the quote is a real review, verbatim, with source; stars only with a real rating
from the proof inventory.

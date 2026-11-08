# Design principles for static ads

Owns what an ad must look like and the final check (step 7), for both `static-ads` and
`offer-ads`. Written from Alex Cooper's statics guide (2026), general design practice and our test runs. Builds on Parker's visual docs (`brain-system/creative-strategy-context/visuals.md` and `static-ad-design.md`). Read at step 2 (ideas)
and step 7 (check). Words: `copy-guide.md`. How it's made: `production.md` in the template library.
Depth if a point is unclear: `brain-system/creative-strategy-context/static-ad-design.md` (short, read it whole) and `visuals.md`, section "The eight principles".

## The funnel
Statics work at both ends, and a brand needs both.
- **Top of funnel (new customers):** `static-ads`. Assume nobody knows the brand
- **Bottom with an offer (sales, codes, collections on discount):** `offer-ads`. The ad may assume people know the brand
- **Bottom without an offer (a review plus a named product, a flavour or variant reminder, repeat purchase):** stays in `static-ads`, written for awareness "knows the product" (`copy-guide.md`). Product-first is fine here; brand recognition does part of the work (`testimonial/sw-SW004`, `text-led/sw-SW007`)

## Proven formats and where they live
Don't invent formats. Use the ones that work again and again, and spend the effort on the message.
The rows are in the order Alex Cooper uses them most (2026): for a first batch with no signal from
the brand yet, start from the top. His 12 formats cover 95-98 % of the statics his agency makes.
| Format | Category in the library |
|---|---|
| Headline + benefits | `features-benefits`, `text-led` |
| Testimonial | `testimonial` |
| Offer | `offer`, `sale-limited-time` (via `offer-ads`) |
| Persona ad | A choice of message, not a layout: any category |
| Collection (several products) | Missing. Add to `offer` when a brief needs it |
| Comparison: before/after, us vs them, timeline | `before-after`, `us-vs-them` (timeline missing) |
| Press / publication | `social-proof` (real press only) |
| Native, post-it, story text boxes | `native` (+ `offer/offer-049`) |
| Native storytelling (the caption sells) | `native/sw-SW005`, `native/hp-07`; copy in `copy-guide.md` |
| Apology ("We're sorry") | `text-led/hp-08-apology-letter` |
| Meme | `meme` |
| AI visual: invisible made visible, atypical text, problem anatomy, X-ray or cross-section | `ai-visual` (four prompts; one example image, `sw-SW008`) |
| Native image: chalkboard, notebook sketch, red-circle photo, notes app, review split | `native` NI1-NI5 (prompts only, untested; when to use them is an open test in `feedback.md`) |

## The image carries the ad
The copy only gets read if the image stopped the scroll first. The image has to:
- **Read in half a second:** what is it, and why keep looking? Obvious beats interesting
- **The product is the hero, in the middle.** The product, or the product in use, sits in the centre
  of the frame (or just below it), large (a third of the frame or more), sharp, with nothing covering
  it. Text goes in a panel above or below it, never across it. Off to one side, small, or sharing the
  frame with a second subject, it loses the 0.2-second test (the lead strategist, the golf test brand, 6 Oct 2026)
- **An unfamiliar product shows its job, not itself.** If a stranger can't tell from the shape what
  it does, show it doing it: the phone holder on the cart with a phone on it and the course map on
  the screen, not two holders on a floor. A packshot alone works only for things everyone knows by
  shape (a bottle, a shoe, a jar) (the golf test brand v1 → v2, 6 Oct 2026)
- **Show people:** a face or a body, ideally a real person with a clear expression, beats a product alone
- **Show a specific feeling:** frustration, embarrassment, doubt or relief beats generic happiness. Recognition comes first
- **Feel native, not polished:** phone photo, real surroundings and a bit of mess feel like the feed. Polish is a deliberate choice for certain formats, not the default
- **Break the pattern without confusing:** an unusual crop or a real texture stops the eye; art with no message doesn't
- **Pre-qualify the click:** show who it's for and what waits after the click
- **Match the message:** if the headline says "stretches", show it stretching. One image under five different headlines is wrong four times
- **Find the money shot:** the image that shows the benefit without words (a before/after, the product in use)
- **Look like the brand:** match the ad style in the brand's visual vocabulary. Clean type cards in the website's colors were judged as not the brand and not scroll-stopping (test 28 Sep)

## Element budget
A designed static has a menu of elements, and a good one picks from it rather than using all of
them. An annotated "anatomy of a winning ad" (shared 7 Oct 2026) showed hook, benefit, review,
proof badge, product, risk strip and CTA on one image: about 27 words, the stacked collage in
"What loses". Use it as a menu, not a recipe.
- **Always:** the hook and the product as hero. In formats where the text is the image (letter,
  post-it, review card, story bubbles), the text is the hero and the card's word budget rules
- **Then at most two of:** one benefit or supporting line; one proof element (a rating, a count, a
  quote or a press line, never two of them); one risk-reversal line. An offer ad's offer line counts
  as one of the two. Pick by the image's job in the copy table: proof when the doubt is "does it
  work?", risk reversal when the doubt is "what if it doesn't suit me, or the shipping eats the
  saving?"
- **Risk reversal:** one line, one or two promises ("Fri fragt · 30 dages returret"), small, along
  the bottom edge, where an in-image CTA would otherwise sit. Only from the proof inventory's
  "Risk reversal" row, never a statutory right (`SKILL.md`, guardrails). Optional: an ad without
  it can be complete (the outdoor-retail test brand v2, 7 Oct 2026, held with nothing on the bottom edge but the CTA)
- **CTA:** on the image, or left to Meta's button under the ad. One or the other carries the
  action; the bottom strip holds either an in-image CTA or a risk line, not both crowded together
- **Logo:** small, in one corner, never the first or second thing the eye lands on; the page name
  above the ad already says who's talking. Left out of anything that should read as a customer's
  review or post (checklist 8)

## AI visuals: three formats (ideas for step 2)
AI makes cheap what used to need a special shoot. Three different formats, all in `ai-visual`:
- **Make the invisible visible:** a feeling or sensation shown as a literal, physical image, so the
  person who has it recognises it at once. Pain as nails in a foot. Take it from customer language:
  when customers describe a sensation ("like walking on needles"), that's an image
- **Atypical text:** the headline written on a real surface where nobody expects ad copy (steam on a
  bathroom mirror, frost on a windscreen, marker on skin). The surface must belong to the problem or
  the moment: a mirror for a shampoo, a foot for foot pain. Text on the body stops people especially
  well in Cooper's accounts
- **Problem anatomy:** an everyday object known by its outline (a shoe sole, a pillow, a sponge),
  filled with a literal, exaggerated version of what's hidden in it, with callout labels. The shape
  reads instantly, the contents break the pattern, and the labels keep people reading. Every label
  is a claim and needs a source (`sw-SW008`)

Both must be about the brand's own problem or promise, not surreal for its own sake. They're loud
formats, so claims get checked against `brand-lens.md` like any other.

## Design checklist (step 7, on every final PNG)
People scan in milliseconds and land on what's biggest. Undirected, the eye moves in a Z: top left,
top right, bottom left, bottom right.
0. **Visual hook and brand style.** Does the image stop the scroll? Could the brand have posted it?
   Text alone only counts when the text is the image (post-it, letter, note). Does it stand out in
   both a light and a dark-mode feed? One strong colour does a lot (`testimonial/sw-SW004`); a white or
   near-black ad disappears in one of them
0b. **The 0.2-second test.** Look at the image at thumbnail size (about 300 px wide) for a blink:
   can you say what the product is and what it does? If not: show it in use, bigger, in the centre.
   Then the **two-second read**: count every word on the image. Headline, the supporting elements
   ("Element budget": at most two) and the CTA or risk line, about 15 words in all for a designed
   format; a third supporting element is a fix; nothing said twice (a price line and a
   badge with the same offer is twice). Formats where the text is the image (letter, post-it, review
   card, manifesto, story bubbles) follow their card's word budget instead (the lead strategist: "Every word has
   to fight for its place. It should be readable in under 2 seconds", 6 Oct 2026)
1. **What's seen first?** The hook is the biggest element. The order that works most often: hook,
   supporting line, product, proof, CTA. The CTA is always at the bottom, the last thing seen, never
   mid-image. It may be left to Meta's button when a risk-reversal line takes the bottom strip
   ("Element budget"). Offer ads put the offer first. **Read the CTA's words:** the category's language and what
   the product solves ("Get your phone a caddy →", "Shop pineapple coconut"), never "Shop now", "Buy
   now" or "Learn more", which Meta's button already says (`copy-guide.md`, ground rules)
2. **One element dominates.** Size, contrast and white space steer the eye. If everything is the same size, nothing leads
3. **Readable at feed size.** The ad shows at about 40 % of its width. At 1024 px wide: body text at
   least 34 px, headlines in cards 46 px or more, CTA 33 px or more. 26 px was too small (test 19 Sep)
4. **Easy to read.** Line breaks follow the meaning; two lines read faster than three. Emphasize the
   one word the line turns on, not half the sentence. The tools: a color block
   behind the word, a color that carries meaning (red for danger or pain, green for relief), a
   marker highlight, an underline or arrow pointing at it, a warp or distortion. One tool per ad;
   two start competing. Example from Cooper's guide: "nerve pain killer" on two lines with a red
   block behind "killer" read far faster than the same words in plain type across a light. No text on a busy background. No widow words,
   no place name split over two lines
5. **Message and image match**, and the direction holds (clear or curious, see `copy-guide.md`).
   The image does the job written for it in the copy table: installs that belief or removes that
   objection. Pretty but doing neither is a fix, however good it looks
6. **Enough for a stranger:** can someone who's never heard of the brand see what, who and why?
7. **Product and text are right.** The product matches the product photos. Every text matches the
   approved copy character for character. Typical model errors: a callout number that doesn't match
   the pack, a misspelled word on the packaging, repeated words, a brand name cut off on the wrapper
   (see `pb-13`, `pb-17`, `pb-26`, `pb-35` in the library). A multi-pack or variety pack shows the
   whole set somewhere (hero, a graphic, a strip at the bottom), never a single unit
8. **No logo on anything that should read as a real customer's review or post.** A logo takes away
   the feeling of reading a real customer; the page name above the ad already says who's talking
   (feedback 19 Sep). Everywhere else the logo is small and in a corner: if it's the first or
   second thing you see at thumbnail size, it's a fix ("Element budget")

Result per image: pass / fix / discard, with one line on why. Shown in the grid.

## What loses
- Too many elements competing, so nothing leads
- **The season as the message:** "BLACK FRIDAY" or "SALE" as the headline. Everyone says it that week;
  it sells nothing. The season is a small tag, the headline sells the product, one line carries the
  offer (the golf test brand v3 → v4, 6 Oct 2026)
- **The lonely packshot of an unfamiliar product:** beautiful, and nobody knows what it is
- Generic layouts that look like every other ad in the feed
- **The decorative split screen:** photo on one half, text on the other, equal weight. The eye picks
  neither. Exception: before/after and us vs them, where the split is the message
- **The stacked collage:** a headline block, a quote block, a benefit row and a product photo, each
  on its own. It reads as three ads in one frame. One ad, one argument, one entry point

## Testing
Vary message and image together, so each variant is coherent and aimed at one audience. Changing one
element at a time breaks the link between message and image. The one exception is the tone test in
step 9: the insight is held fixed on purpose, so the result says something about expression.

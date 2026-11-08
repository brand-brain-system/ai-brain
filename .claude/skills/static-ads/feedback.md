# Feedback log

What we've observed in runs and reviews. A log, not a rulebook: new lessons land here with a date,
and once confirmed they move to their home file (see the table in `SKILL.md`), leaving one line here
saying where they went. Consolidate after every third run. Write lessons generally, not about one brand.

## Open (not yet confirmed or moved)
- Clean type cards with no image (quote or review in large type) read well but have no visual hook.
  the lead strategist's verdict on the 28 Sep test: they wouldn't perform and don't look like the brand's ads.
  One test only; confirm on a run with real images before hardening further

- Describe the product in the prompt, or only reference its photo: open test in `production.md`, run
  on the next batch with the product in a scene (30 Sep)

**From Alex Cooper's "The Complete AI Ad Stack" (public Notion, read 17 Oct 2026; Stated, none run by us).**
Four open tests. Each moves to its home file once it has held on a second brand (factory rule 6).
- **Open test: pick the native format from the problem type.** For a problem/solution product, add
  three lines above the copy table before choosing templates: the problem type (*visible*: they can
  see it; *felt*: a sound, texture, sensation, sleep; *hidden*: inside the body or a cause they can't
  see; many products are two), the **first-notice moment** (where and when the buyer notices it, in
  customer words from `source-pulls/`), and what they already tried. Then the format follows from the
  type: visible → red-circle photo (`native` NI3), post-it, phone photo; felt → phone photo, notes
  app (NI4), handwritten note; hidden → X-ray or cross-section (`ai-visual` AV4), problem anatomy
  (AV3), chalkboard (NI1); needs the mechanism explained → chalkboard, notebook sketch (NI2), us vs
  them; social proof → review split (NI5); regulated (health, weight, skin, pets) → an educational
  diagram or a plain symptom photo, never a transformation. **The test:** on the next
  problem/solution batch, two or three concepts picked this way sit next to the normal picks; log
  which the human keeps at step 8. Home if it holds: `SKILL.md` step 1 and `design-principles.md`
- **Open test: the pull element.** A native image that only stops the scroll needs one thing that
  sends the eye into the caption: a real review strip, a "see below ↓" box, a plain unlabelled
  product with a "?". Nothing in our files had this. Try it on the native concepts in the same batch
  (with and without, when there are two). Home if it holds: `copy-guide.md`, "Native storytelling"
- **Open test: describe where the camera is, not the view's name** (applies to every generated
  image and clip). Cooper's "behind the bottom teeth" ad showed the front until the prompt said "as
  if shot with a dental mirror placed behind them, the underside of the tongue filling the top of the
  frame"; in his model shoot "low angle" came out at eye level until "the camera is near floor level
  looking steeply up". Two of his systems, none of our runs. When a view or angle matters, write the
  camera's position and what fills the frame. Home if it holds: `production.md`, "Building a
  generation prompt"
- **Open test: a refused generation.** When a model's content filter refuses an image (body, skin,
  health), reword it as education ("a clean educational diagram of ...") and remove alarming words;
  never resend the same wording. Cooper's pore cross-section passed on the reworded try. Log every
  refusal and the wording that passed. Home if it holds: `production.md`, "Model settings"

**From a public post with six tips on building a static ad skill (read 21 Oct 2026; Stated, none run by us).**
Three open tests. Most of the post we already do (template quality, a person at two stops, separate
skills, no app). Each moves to its home file once it has held on a second brand (factory rule 6).
- **Open test: cost per usable ad.** At the end of every run, add one line to `costs.md`: ads
  generated, ads kept at step 8, real spend, and spend ÷ kept. Copy that line here under the run's
  log entry, so the trend across runs and brands is in one place. The question: does it fall as the
  templates and feedback improve, and which categories cost the most per kept ad? Home if it holds:
  `production.md`, "Paying for generation"
- **Open test: feedback on the layout.** The grid in step 7 now has a per-layout field next to the
  per-ad and whole-skill fields (changed 21 Oct 2026). Layout notes go straight into that template's
  `notes` in `templates.csv` instead of being sorted out of ad notes by hand. The test: after two runs,
  do layout notes show up, and do they change which templates step 1 picks? If nobody uses the field,
  remove it. Home if it holds: it stays in `SKILL.md` step 7, and this line moves out of Open
- **Open test: results from the ad account feed the templates.** Today every lesson comes from a
  person's taste at the grid. Once a brand's statics have run long enough to read (the brand's own
  threshold in the brain; none: two weeks and the brand's normal spend per ad), match the launched ads
  to their ad records by concept ID, group them by template id, and write one dated line in each
  template's `notes`: ads launched, the brand's north-star metric against the account average, and the
  brand described, not named ("the golf test brand"). Taste and results are written as separate lines, never merged. The test: on a brand with an
  ad-account export, does the result line ever disagree with the grid pick, and does it change step 1?
  Home if it holds: `SKILL.md` step 1 (read result lines in `notes`) and a write-back step in
  `ad-account-analysis` or `weekly-creative-report`

## Log

**19 Sep 2026: concept ads, engraving brand (a job-application case), GPT Image 2.5 Flare Edit, medium quality, 3 ads**
- Danish text incl. æ, ø, å rendered correctly → `production.md` (Model settings)
- Model copied a real customer's name and date from a reference photo; count drifted from four to five pieces → `production.md` (Filling the gaps)
- Small engravings unreadable when the product is small → `production.md` (Reference images)
- Logo only faithful when uploaded as a reference → `production.md` (Building a generation prompt)
- A wrong full stop survived a re-edit; local fix worked → `production.md` (Fixing a wrong text)
- Quotes must be pasted character for character → `production.md` (Filling the gaps)
- Mobile sizes: 26 px too small; minimums set (the lead strategist) → `design-principles.md` (checklist 3)
- CTA always at the bottom (the lead strategist) → `design-principles.md` (checklist 1)
- No logo on a "review" (the lead strategist) → `design-principles.md` (checklist 8)
- PowerShell encoding and naming gotchas → `production.md` (Fixing a wrong text)
- Per ad: "Please don't buy this" (native testimonial) convincing person but generated-looking hands and cutlery, concept use only; "Life's hard. Make it harder" (text meme) landed first try; "We're Sorry" (letter) best of the three: calm, readable, credible product

**28 Sep 2026: test run, concept, a retailer brand with no own images in the brain, 2 ads (HTML render + Nano Banana 2)**
- the lead strategist's verdict: wouldn't perform. Setup and quality OK, but nothing visual stops the scroll and they don't look like the brand's own ads. Causes: visual vocabulary built from the website's CSS instead of the brand's ads; type cards with no visual hook; no brand images → `SKILL.md` (Prerequisites: visual vocabulary, assets), `design-principles.md` (The image carries the ad; checklist 0). The type-card point stays open above
- HTML-rendered text is exact, free and fast; use it as a layer on a real image → `production.md` (The default build)
- Headless Edge cut off the bottom at window size 1080 × 1350 → `production.md` (Rendering)
- Nano Banana 2 rendered Danish text correctly first try, but 1K is 928 × 1152 px, small lines came out too small and the font drifted → `production.md` (Model settings)
- The check caught a cropped bottom, a place name split over two lines and a widow word before the human saw them; it has to run on the final PNG → `design-principles.md` (checklist 4), `SKILL.md` (step 7)
- No images and no visual vocabulary: the skill must stop and ask → `SKILL.md` (Prerequisites)
- Templates testimonial 25 (pb-16) and 27 (pb-19) without an image lack a hook → their `notes` in `testimonial/templates.csv`

**6 Oct 2026: the golf test brand, one Black Friday concept, four rounds of the lead strategist's feedback (Nano Banana 2 edit scene + HTML text layer)**
- Dark product drifted lighter; naming each part's colour fixed it → `production.md` (Composing a generated scene)
- Scene with no text + HTML text in the brand's real font: exact copy first time → `production.md` (Composing a generated scene)
- v1 packshot of an unfamiliar product failed the 0.2-second test; in use passed; then "make the product more center" → `design-principles.md` (The image carries the ad; checklist 0b; What loses), `SKILL.md` (step 1)
- v2 had ~30 words in 7 elements; cut to 6 words → `design-principles.md` (checklist 0b, two-second read), `offer-ads/offer-copy.md`
- v3 headline "BLACK FRIDAY" and CTA "SHOP NOW" too generic → `copy-guide.md` (ground rules), `design-principles.md` (checklist 1, What loses), `offer-ads/offer-copy.md`
- The kept headline came from the brand's own running testimonial ad → `copy-guide.md` ("The brand's own winner"), `SKILL.md` (step 2)
- The CTA rule already existed and was broken anyway, because step 7 never read the CTA's words → `SKILL.md` (step 7)
- Found while consolidating: the headline patterns suggested "No X. No Y. Just Z." while the AI check bans it → fixed in `copy-guide.md`

**7 Oct 2026: the outdoor-retail test brand, two concepts (a Christmas gift ad and an advice ad), HTML render with the brand's own product photos, the lead strategist's feedback on v1**
- v1 was a review as a text card on a plain background, with a return-policy line in a bottom band. Verdict: doesn't look like a real ad, no product, no person, the review was the whole ad. The failure was building a testimonial type card for a retailer, where the product is what's bought → `design-principles.md` (The image carries the ad; What loses)
- What held in v2: the product in a white panel in the centre (a person wearing it for the gift; the shoe alone, because everyone knows its shape), the review as a smaller card overlapping the panel's lower edge, a two-line headline above, a CTA pill at the bottom, nothing legal on the image. Read the review card as a layer on a real product photo, not as the ad → `production.md` (The default build)
- Product photos for a brand that isn't a client: take them from the brand's own shop image server (resize in the URL, e.g. `?width=1200`), save in `img/produkter/`, and say in the document that they come from its shop. No generated people or products → `SKILL.md` (Prerequisites: `assets/`)
- A packshot with white background sits in a white panel with a soft shadow; sized so the whole shoe is visible. Zoomed too far, the toe and heel were cut → `design-principles.md` (checklist 0b)
- the lead strategist asked for the Trustpilot logo on the review. That conflicts with the guardrail (no review-platform logo without a licence) and checklist 8 (a logo takes away the feeling of a real customer). Kept a plain-text source line and left the decision to him. **Open:** record his answer, and whether a licensed brand may use the logo, in `design-principles.md`
- Headless Edge renders 24 px narrower and 93 px shorter than `--window-size`: request (width + 24) × (height + 93), then crop to exactly 1080 × 1350 with System.Drawing in PowerShell → `production.md` (Rendering), which already has the 28 Sep cut-off note

**7 Oct 2026: review of an annotated "anatomy of a winning ad" graphic (no run)**
- Most of its elements were already covered (hook, one benefit, product as hero, real reviews, proof). Its example ran ~27 words in six elements, so it went in as a menu with a budget, not a recipe → `design-principles.md` (Element budget; checklist 0b)
- Gaps closed: risk reversal had no home or role → `brand-dna` (proof inventory "Risk reversal" row, research step 8), `SKILL.md` (prerequisites, step 1 `needs` and fit rule 4, step 5 bottom-strip swap, guardrail on statutory rights), `offer-ads/SKILL.md` (step 1); no logo-size rule → `design-principles.md` (Element budget; checklist 8); the CTA on the image was mandatory → optional when a risk line takes the bottom strip, `design-principles.md` (checklist 1)
- Not yet tried in a run. Confirm on the next batch whether a risk line earns its words against an in-image CTA

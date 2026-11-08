---
name: static-ads
description: Build static image ads in volume for a brand (statiske annoncer, statics, ad creatives): pick proven templates from the swipe file, write copy from real customer language, get human approval, generate images via an image MCP (fal.ai or Higgsfield) with text rendered on top, check every output, review in a grid, make variants, and learn from feedback. Use when someone asks for statics, static ads, statiske annoncer, ad creatives or a batch of image ads for a brand. For offers, Black Friday, Christmas or sales, use offer-ads instead.
---

# Static ads in volume

Always run inside the brand's brain folder, so the brand, personas and customer language are known. The human approves in two places: copy before generation, and the pick afterwards. Never try to automate the whole way from the start.

## Where the knowledge lives
This skill is our own method, built on Parker's craft docs, Alex Cooper's material and our own test runs. Each rule has one home:

| File | Answers |
|---|---|
| `SKILL.md` (this file) | In what order, and what must never happen |
| `copy-guide.md` | What the words say |
| `design-principles.md` | What the ad must look like, and the final check |
| `brain-system/creative-strategy-context/production.md` | How it's made: prompts, model settings, rendering, fixing errors |
| `feedback.md` | What we've observed. A log, not a rulebook |

When a rule changes, change it in its home only. Other files point, they don't repeat.

- **Provenance:** see `NOTICE.md`. Built on Parker's craft docs (used with Simple Labs' permission), Alex Cooper's material and our own test runs
- **Alex Cooper's static-ad engine** (Adcrate, shared through the Parker course for participants to use and adapt): merged in on 6 Oct 2026. From it: the template cards (`brain-system/creative-strategy-context/swipe-library/cards/`), the fit rules in step 1, the run modes, the grounding check, and parts of the prompt anatomy in `production.md`. Credit stays in the text

## Modes (pick from the ask; say which in one line)
- **Full run** (default when the brain is filled and the ask says make, generate or produce): all nine steps
- **Dry run** (default the first time for a brand, for a brand that isn't a client, or when the ask says plan, concepts, show me): steps 1-5, then the finished prompts and the cost from `get_pricing`. Nothing is generated or spent. Saved in `sprints/<date>-dry-run/`
- **Prompt pack** (the ask wants prompts to paste into Nano Banana, Higgsfield or Gemini, or a doc to hand to someone): one finished, standalone prompt per template that fits, for one product. Steps 1-4 as normal, then "Prompt pack" below instead of steps 5-9
- **Calibration** ("run all", "test every template"): every template that passes the fit rules gets one concept; the rest are listed with the rule that excluded them. After the grid, record per template whether it was strong, weak or forced for this brand's category in the template's `notes`. A pattern across brands goes in the card's "Adaptation notes"

## Prerequisites (check first, ask if missing)
- **Brand type, two axes.** (1) Problem/solution or lifestyle, per product: does it fix a problem the customer knows she has, or does it sell identity and desire? This steers the headline patterns in step 3. (2) Own product brand, retailer or service: for a retailer, customers often buy the store, the guidance and the delivery, not one product, so pick templates where the experience can carry the image
- **Visual vocabulary with ad style.** `sub-context-docs/visual-vocabulary.md` must describe how the brand's own ads look: photo type, crop, settings, who's in the frame, how the product is handled, how text sits on the image. Sources in this order: the brand's own ads (Meta Ad Library), its organic content, competitors, inspiration. The website's colors and fonts come last. Mark each visual as *in play* (the brand has made it), *adjacent* (seen elsewhere, and the brand could make it) or *out of reach*. Method: `brain-system/creative-strategy-context/visual-vocabulary-method.md`, Part 2 (what to catalog) and Part 3 (the three levels)
- **Brand DNA.** `sub-context-docs/visual-vocabulary.md` needs the colors (hex), fonts, product description and image generation prompt modifier, and `brand-lens.md` needs its proof inventory. Missing: run the `brand-dna` skill first. The proof inventory is the only source for review counts, ratings, customer numbers, press and seals in an ad, and its "Risk reversal" row the only source for guarantees, shipping and return promises. A brain made before 7 Oct 2026 may hold the guarantee in `sub-context-docs/brand-profile-narrative.md`: move it, with its source
- **Offer brief** (`strategy/offer-brief.md`), if the brain has one: every headline traces back to it. The rule lives in `copy-guide.md`, decision 0. Not required; its absence is named in one line
- **`assets/`:** product photos and logo, ideally the brand's own ad photos. No images: stop and ask for them. Don't fall back on plain text cards
- **Templates:** the master library `brain-system/creative-strategy-context/swipe-library/`, one folder per category with `templates.csv` (columns `angle`, `swap`, `needs`, `notes`) and `prompts.md`. Read from there, never copied into the brain. The brand's rejected templates are in the brain's `running-notes/feedback.md` under "Per template"
- **Open tests:** this skill's `feedback.md`, section "Open". Run every open test that fits the batch, name it in the copy table, and log the result there
- **An image MCP.** fal.ai: call `recommend_model` with the task "ad image from a layout reference and product photos, the product must not change", check `get_model_schema`, and run `get_pricing` before a batch. Higgsfield: GPT Image 2 keeps the product best

## The nine steps

**1. Pick templates.** Template quality sets output quality. First pick the category from the brand's situation (trust, competition, a product that shows itself, real press, too polished already, strong customer language, the experience is the sale, a live offer; the category introductions in `brain-system/creative-strategy-context/ai-static-ad-generation.md`, section "Format Library", only the category introductions). Then pick templates from `templates.csv`:
- `needs`: skip when the brand lacks the real input (e.g. `review-count` without a real number, `press` without real press, `offer` without a live offer, `guarantee` without a non-statutory promise in the proof inventory's "Risk reversal" row)
- `swap`: for a difficult product (small print, engravings, many parts, clothes on a body), `easy` only
- `notes`: read the lessons already recorded on the row
- visual vocabulary: prefer templates whose image is *in play* or *adjacent* for the brand
- an unfamiliar product (strangers can't tell from its shape what it does): prefer templates where it
  can be shown in use; a packshot-only template takes an in-use swap or is skipped (`design-principles.md`)
- **Fit rules, for templates with a card** (`brain-system/creative-strategy-context/swipe-library/cards/INDEX.json` holds every card's fit data in one file; read it instead of the cards). Applied in order, the first failing rule decides (Alex Cooper's engine, `strategy.md`, section 4):
  1. Product fit: `product_fit` includes `universal` or the brand's product type. Colorway arrays need 3+ real colorways; multi-product layouts need several products or a real bundle; high-personality layouts need the brand to allow humor
  2. Urgency: a deadline device on the image is out unless a real deadline exists
  3. Assets: the photo the layout needs (packshot, lifestyle, UGC, face, hands, before/after) exists, or a legal swap does (hands instead of a face, a setting the brand has shown). Otherwise out
  4. Inputs: the proof the layout is built on exists in the brain: verbatim reviews (a long one for long-review cards), real comments, verified stats (four for a stat surround, three if a callout is dropped), press, counts, colorways, an honest category contrast, a visible transformation, a guarantee or other risk reversal (seal and value-add layouts)
  5. Proof bans: an element the brand can't show drops; a card whose whole job is that element is out
  6. Tone and claims (soft): a tone the brand doesn't use is a named "tone stretch"; a `claim_sensitive` card for a health brand gets flagged for the human. Neither excludes
- the brain's `running-notes/feedback.md`: skip the brand's rejected templates
Show the picks together with the copy table in step 3, so the human approves template and copy in one go.

New templates for the library (only when a brief lacks a format): the Meta Ad Library, Foreplay or Atria. The public Ad Library shows no spend or results, so its ads are picked for being clear and swappable, never as proven winners. Build an HTML page of candidates, let the human pick, and save only the picks in the right category with a row in `templates.csv`. 50 to 100 in total is enough. A good template is clear rather than clever, and the product can obviously be swapped.

**2. Research.** Before reading anything, ask the human for their own angle in one or two lines: which persona, which feeling, which idea they'd bet on. Research tests it alongside Claude's own; the copy table marks which headlines come from the human's angle. No angle: carry on, don't push. This keeps the strategy thinking with the person, and leaves a record of it.

Then find the white space: what the brand doesn't already say. If the brain has a `persona-gap` Mode B audit (the xlsx and `analyse.md` in its research folder, the diagnosis in `strategy/strategic-roadmap.md`), read its gap tables: empty cells in the persona × awareness matrix, and personas with a bigger share of customer voice than of ads. No audit: list the brand's live ads (Meta Ad Library, country DK) and tag them roughly by persona and awareness, Mode B steps B1-B3 without the spreadsheet; or ask the human what's running. Aim at least half the batch at gaps; the rest may build on structures that already work. This is coverage, not performance: an empty cell means nobody has tried it, not that it would win. Label gap-driven ads **Inferred (white space)**.

Then read the brand's live ad copy (Meta Ad Library, the brand's page, sorted by impressions): which
texts run in many ads, and which customer quotes the brand has chosen to run. They're headline
sources (`copy-guide.md`, "The brand's own winner"). Then use the brain: customer language, personas, what has worked. Find emotionally loaded lines in reviews, comments and Reddit, angles that are big in customer language but untested in the ads, and feelings that can become an image ("AI visuals: three formats" in `design-principles.md`). If the brand's own winning headlines exist, collect them as the baseline: the strongest new headline is often a new version of a structure that already works.

**3. Copy.** One copy per picked template, per `copy-guide.md`. When the template has a card, its "Copy skeleton" sets the word budget per zone: stay within it, since text that runs long breaks the layout and renders worse. Show a table: template (category + id), persona, the gap it fills (persona × awareness cell from step 2, or "none: builds on what runs"), where the selling happens (in the ad / in the caption / after the click), idea path and pattern, one column per text slot the template has, named by position (hook, subline-top, pill-1, cta: count them off the template image, so step 7 can check each one character for character; for native storytelling: the full primary text, per `copy-guide.md`), source of the wording, what the image shows (so message and image match), and the image's job: the one belief it installs or the one objection it removes, in a few words (e.g. "removes: 'it won't arrive in time'"). An image with no job is decoration; change it before the table goes to the human.

**4. STOP: copy approval.** Generate nothing before yes. First run the copy check, chiefing, the AI check and the persona panel in `copy-guide.md`, and flag what fails before the human sees the table. Then trace every quote: save the copy table as `copy.md` in the run folder and run `python -X utf8 brain-system/scripts/grounding-check.py copy.md <brain folder>`. An UNTRACED quote is either from a pull made this session (save that pull in `source-pulls/` first, then re-run) or invented (cut it). Every number in the copy must be in the proof inventory.

**5. Build the ad.** Start from the template's story (the card's "The story this ad tells", when it has one; its "Adaptation notes" list which swaps break the layout): what does it want the viewer to believe or feel, and how do image and text do it together? Keep the structure (same number of text elements, same length, same device such as a number, question or quote). Don't add elements the template doesn't have. One allowed swap: a strip along the bottom edge (a `cta`, `badge` or `disclaimer` zone on the card) may carry one risk-reversal line instead, when the image's job is to remove a buying risk (`design-principles.md`, "Element budget"). It replaces the zone's content; nothing is added. Source: `brain-system/creative-strategy-context/\1, "Core Philosophy" and "Mistakes To Avoid". The build itself (real image with rendered text, or a generated image, prompts, rendering) follows `production.md`.

**6. Generate** the images that need generating, via the MCP, with the settings in `production.md`, quoted and logged per its "Paying for generation". If `production.md` has an open test, run it in this batch.

**7. Check and grid.** Read every final PNG against the design checklist in `design-principles.md` (it includes the text-against-copy and product checks). Run the 0.2-second test on a 300 px-wide thumbnail, count the words for the two-second read, and read the CTA's words, before the human sees anything: these three caught every round of the lead strategist's feedback on the 6 Oct the golf test brand ad. Give each image pass / fix / discard with one line on why, and save its ad record (`production.md`, "The ad record"). Then build the grid as a local HTML page in the run folder: number, image, a button to show the template beside it, the check result, "keep", a feedback field per ad, per layout (the template id, so the note lands in that template's `notes`) and for the whole skill, and a button that copies picks and feedback into the chat, each note tagged ad, layout or skill. Don't publish it as an Artifact when the ads carry a real brand's name and the brand isn't a client.

**8. STOP: pick.** The human picks. Expect a share not to hold up; that's the price of volume, and it's cheap.

**After the pick, before anything goes to the ad account:** run `ad-policy-check` on the picked images (copy, image text, people, landing page). A **stop** goes back to step 4 for that ad.

**9. Variants and final pick.** Three modes; ask which, or pick by what the test should answer:
- **New angle** (default): message and image change together (a new persona gets a new headline and a new image), not one element at a time. Answers "which insight wins?"
- **Tone test:** the insight stays fixed, word for word from the approved copy, and only the tone changes: blunt, curious, humorous, clinical (four at most). The image changes only where the tone demands it. Answers "we trust this insight, how should it sound?", and is the fix when a strong insight produced a flat ad. Every tone version still goes through the copy check and `brand-lens.md`
- **Format spread:** the message stays fixed, and each variant is built in a clearly different format: a call-out headline, a native story, a testimonial, a native storytelling caption, a meme (three to five). Not the same layout with a new headline: Cottrell's reason is that Meta's Andromeda treats near-identical ads as one asset (his experience, not verified), so the variants must look different at a glance. Answers "how far does this message carry?" Only for a message that's already earned it: the human picked it in step 8, or it has a real result. A message that isn't sharp enough to say in one sentence isn't ready. Some messages belong to their format (a long story won't survive as a one-line static); say so instead of forcing it. Source: Fraser Cottrell (2026). The format-swap pre-check and "what never to do" are in `brain-system/creative-strategy-context/iterations.md`. When a static message wins, note in the brain that it's a candidate for video too (UGC, founder, podcast); `video-edits` or a brief takes it from there. The quickest video version is the static itself in motion: `motion-ads` animates the picked static with the same words and product, no new copy

New grid; final picks saved in `sprints/<date>-<slug>/ads/<date>/` with their records. For each final pick, write the Meta text that runs with it (`copy-guide.md`, "Meta text for the picks") and show it for approval with the picks.

## Prompt pack (mode)
Finished prompts someone can paste into Nano Banana 2 (or Higgsfield, Gemini) with the product photos attached, with no gaps left to fill. The research, copy and approval are the same as a full run; only the output changes.

- **Which templates:** every template that passes the fit rules, for one named product. Default: the 40 Nano Banana templates (`pb-01` to `pb-40` across the category folders). List the ones left out, each with the rule that excluded it, so the reader sees the whole set was considered
- **"No edits needed" means no blanks, not invented proof.** Every gap is filled from the brain: hex colors, fonts and the prompt modifier from `sub-context-docs/visual-vocabulary.md`, the product's physical description, verbatim reviews with name and source, numbers from the proof inventory. An element the brain can't fill honestly is removed from that prompt (no star row without a real rating, no press bar without real press), and the line under the prompt says what was removed and why. Never a plausible-looking stand-in
- **Each prompt:** built per `production.md` ("Building a generation prompt" and "Writing a standalone prompt"): reference line, the brand's prompt modifier (left out for native looks), layout in zones with proportions, every text in quotes exactly as approved, light and lens, realism cues for native formats, mood and ratio. Under it: what to attach (which files in `assets/`), the aspect ratio to set in the tool, the sources behind its proof, and the template image for comparison
- **The doc:** `sprints/<date>-prompt-pack-<product>/prompts.md`, one section per template in library order, opening with the brand's prompt modifier and the attach list. Concept work for a brand that isn't a client says so at the top, and each prompt asks for a small "Concept" label in a corner (see guardrails)
- **STOP:** the copy table is approved before the doc is written, as in step 4. Generating from the pack later is a full run from step 6

## Feedback
Write all feedback from the grid and chat in `feedback.md` here, dated. Write the lesson generally, not about the single brand. Feedback that only applies to one brand goes in the brain's `running-notes/feedback.md` instead. A lesson about one template goes in that template's `notes` in `templates.csv`. A template that's bad for every brand is removed from the library; one that's bad for one brand is rejected in that brain's feedback.

**Consolidate after every third run:** move confirmed lessons from `feedback.md` into their home file (see the table above) and leave one line in the log saying where they went.

## Optional review agent
After generation, a subagent can compare each image with the product photos (shape, logo, text on the pack) and the copy with the approved copy. It doubles the usage, so only on yes.

## Guardrails (never)
- Separate skills for top of funnel, offers and iterations on own winners. One big skill gets expensive in tokens. Offers, Black Friday, Christmas and sales: use `offer-ads`
- No claim, number, quote, reviewer name, review count, "verified" badge, press logo or award that isn't in the brand's own materials or a real, dated source. Missing a number: write "[NUMBER MISSING]", don't guess
- No statutory right sold as a perk: 14 days' right of withdrawal and 2 years' reklamationsret are the law, and presenting them as a feature of the offer is misleading marketing. Only a promise beyond the legal minimum (a 30-day return window, a money-back guarantee) goes on an image
- Comparisons must be fair and checkable. Use a generic, unbranded competitor product unless a real competitor is named deliberately
- Review cards use neutral styling. Don't imitate a review platform's logo, colors or star graphics (Trustpilot, Google, Amazon) unless the brand is licensed; write the source in plain text
- No first-person customer story, comment or post that we wrote. A customer's voice is a real customer's words, with permission; otherwise it's the brand's own voice, openly
- No copy that asserts or implies the reader has a condition or other personal attribute ("Do you have eczema?"): Meta rejects it. Describe the situation instead (`copy-guide.md`, "Native storytelling"). The platform rules have their home in `ad-policy-check`
- Real staff and owners appear only in real photos with consent. No names of them in generated ads and no AI people presented as staff. When an angle needs them, the ad becomes a brief for a real shoot
- Concept ads for brands that aren't clients are labeled as concept, also in the image itself (small text in a corner), so an exported file can't pass as a real ad

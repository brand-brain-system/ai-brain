---
name: offer-ads
description: Build static offer ads in volume (offer-ads) for Black Friday, Black Week, Cyber Monday, Christmas (jul), mellemdagssalg and other sales or campaigns with a discount, code, free gift or free shipping. Starts from an approved offer brief with real prices and dates, picks offer templates from the master library, writes copy that follows the Danish price-marketing rules, checks every price in the finished images and collects feedback. Use when someone asks for Black Friday ads, offer ads, sale ads, udsalgsannoncer or a discount campaign. For evergreen statics without an offer, use static-ads.
---

# Offer ads in volume (Black Friday, Christmas, sales)

Sister skill to `static-ads`: the same nine steps, built around an offer. Always run inside the brand's brain folder. The human approves in three places: the offer brief, the copy and the pick. A wrong number in an offer ad isn't just bad copy, it can be illegal, so no number is ever invented.

## Where the knowledge lives
Shared with `static-ads` (read them, don't copy them):
- `.claude/skills/static-ads/copy-guide.md`: what the words say
- `.claude/skills/static-ads/design-principles.md`: what the ad must look like, and the check
- `brain-system/creative-strategy-context/production.md`: prompts, model settings, rendering, fixing errors
- `brain-system/creative-strategy-context/swipe-library/`: the templates. `offer-q4/` holds Alex Cooper's 74 offer templates (Adcrate offer-statics, shared through the Parker course; merged 6 Oct 2026), each with a card in `offer-q4/cards/`: layout, story, copy skeleton with word budgets, the mechanics it can carry, adaptation notes and a prompt skeleton
- Modes: dry run and prompt pack work as in `static-ads` ("Modes", "Prompt pack"). A brand's first campaign, or a brand that isn't a client, defaults to a dry run

Offer-specific, in this folder:
- `offer-copy.md`: offer copy, Danish number format, the Danish price-marketing rules, campaign phases
- `offer-brief-template.md`: the offer brief
- `feedback.md`: offer-specific lessons (a log, like the one in `static-ads`)

## Prerequisites
- `assets/` with product photos and logo. No images: stop and ask
- The brand's visual vocabulary with ad style, in `sub-context-docs/visual-vocabulary.md` (see `static-ads`, Prerequisites)
- An image MCP (fal.ai: `recommend_model`, `get_model_schema`, `get_pricing` before a batch)

## Step 0. Offer brief (STOP: approval)
Fill in `offer-brief-template.md` and save it as `sprints/<YYYY-MM-DD>-<campaign>/ads/offer-brief.md` in the brain. The numbers come from the brand or the human, never from the model. Ask when something is missing. If the before-price can't be documented (lowest price in the last 30 days), the ad may not say "spar", "før/nu" or show a percentage: use an offer without a price comparison instead (gift, free shipping, bundle). Generate nothing before the brief is approved.

## The nine steps

**1. Pick templates.** From `offer/`, `offer-q4/` and `sale-limited-time/`, plus templates in other categories whose `needs` includes `offer`, `code`, `deadline` or `real-event`. For `offer-q4` templates, apply the fit rules on the card in order, the first failing rule decides (Alex Cooper's offer-statics, `strategy.md` section 4): (1) urgency: a countdown or "ending soon" device only with a real deadline in the brief; (2) assets: the photo it needs exists, or a legal swap does (hands instead of a face, one product's quantity ladder instead of a multi-product line); (3) mechanic: the card's `mechanics_compatible` overlaps the brief's offer; a code box needs a code, a strikethrough or was/now needs the documented 30-day lowest price; (4) proof: a quote zone needs a verbatim sourced quote, and a rating, count or press zone the brand can't fill takes the card's swap or the card is out. Read the picked card's copy skeleton (word budget per zone) and adaptation notes; fetch its full-size image (`image_url`) only once it's picked. Then filter all templates:
- `needs` against the brief: `guarantee` only with a real guarantee (the brain's proof inventory, "Risk reversal"; never a statutory right, `static-ads` guardrails), `review-count` only with a real number, and so on
- `swap`: difficult product, `easy` only
- `notes`, the brain's `running-notes/feedback.md` (rejected templates) and `feedback.md` here
- the offer type: a gift template for a gift offer, price templates only when the price may be shown
Missing a format for the brief: find new templates as in `static-ads` step 1 and save them in the library.

**2. Research.** First ask the human for their own angle, as in `static-ads` step 2. Then, short: why buy right now, who gives it as a gift (Q4), the biggest objections, and emotionally loaded customer language from the brain. The offer doesn't sell the product on its own. In gift season the buyer isn't the user: write to the giver, and show the recipient's reaction rather than the product. Don't reinvent for the sale; adapt the brand's evergreen winners and past sale winners. Depth: `brain-system/creative-strategy-context/gifting-and-q4-creative.md`, sections "The buyer is not the user", "Do not reinvent for the sale" and "The phases of a Q4 sale" (our phase model is in `offer-copy.md`). For dates and what won the sale week across brands: `brain-system/creative-strategy-context/black-friday-and-q4-data.md`, "Moving the calendar to this year". If the brain has a season report for last year's sale (`audits/*/season-report-*`), read its "Plan for this year" first: the brand's own data beats the cross-brand numbers.

**3. Copy.** One copy per template, per `offer-copy.md` and `copy-guide.md`. Table: template (category + id), phase, headline, offer line, terms line, source, and the image's job (as in `static-ads` step 3; in offer ads usually removing a buying-now objection such as "will it arrive before Christmas"). Below the table, a fact list with every number, date and code in the copy, and where in the brief it comes from.

**4. STOP: approval of copy and fact list.** Before the human sees them, run the copy check, chiefing, the AI check and the persona panel in `copy-guide.md`. The panel's strict reviewer also checks every price claim against `offer-copy.md`. Trace every quote with the grounding check, as in `static-ads` step 4.

**5. Build the ad** as in `static-ads` step 5, following `production.md`. Prices, dates and codes go in exactly as approved, in Danish number format (`offer-copy.md`). Seasonal touches (black and gold, Christmas) as an accent, not instead of the brand's own style.

**6. Generate** the images that need generating, with the settings in `production.md`, quoted and logged per its "Paying for generation".

**7. Check numbers and design (always).** Read every final PNG and compare every price, percentage, date and code with the fact list. At the same time, run the design checklist in `design-principles.md`; in an offer ad, the offer is usually the hook and must be seen first. Deviations are marked in the grid and never get "keep" without a fix (how to fix: `production.md`).

**8. Grid and STOP: pick.** As in `static-ads`, with the number check result shown per ad. Then `ad-policy-check` on the picks before launch, as in `static-ads`.

**9. Variants and final pick.** Phase variants (teaser, live, last day, Cyber Monday), formats (1:1, 4:5, 9:16), and season (Christmas) under the rules `offer-copy.md` sets for follow-on campaigns. Final picks saved in the campaign folder from step 0.

## Feedback
Offer-specific lessons go in `feedback.md` here, dated. General model and layout lessons go in `static-ads/feedback.md`, so both skills learn from them. Brand-specific lessons go in the brain's `running-notes/feedback.md`. Consolidate after every third run, as in `static-ads`.

## Guardrails (never)
- No number, date or code outside the approved brief
- All guardrails in `static-ads` apply here too
- Concept ads for brands that aren't clients are labeled as concept, and prices in them are labeled as examples
- This isn't legal advice. If the brand is unsure about a price comparison, ask the brand and point to the Danish Consumer Ombudsman's guidance

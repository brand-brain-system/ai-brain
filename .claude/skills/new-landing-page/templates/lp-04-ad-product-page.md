# lp-04 Product page built for ads

**Use when:** The buyer already wants the category. The decision happens in the buy box, so put the offer and the risk reversal there, on an ad-only URL or price.

**Buying phase it serves:** Evaluation to Purchase

**The brand needs:** product, price, product_page_or_checkout_url. **Helps to have:** risk_reversal, reviews, clinical_or_proof, press, founder_note.

## Why it works

Not the store's product page: a custom version with the buy box at the top, an ad-only price or offer, a risk reversal under the button, and proof blocks in the order a nervous first-time buyer needs them. Honeylove and Laura Geller each put their biggest page spend behind one.

## Reference pages (in the swipe file)

- Honeylove: https://www.honeylove.com/pages/crossover-bra (screenshot `honeylove-1.jpg`, breakdown `brands/honeylove.md`)

## Section contract

| # | Section | Required | Its job | What to write |
|---|---|---|---|---|
| S01 | offer bar | yes | The exact offer or code (the named ad's, when there is one) | text 6-12 words |
| S02 | buy box | yes | Hero buy box: name, what's inside, rating, anchor to ad price, options, risk reversal | heading: product name + category claim 4-10 words; rating_line allowlisted; options 1-3; includes 3-5; guarantee or try-first line 6-15 words; cta 2-4 words; image |
| S03 | benefits | yes | "Perfect for": 3-4 buyer problems in their words | 3-4 items, title 3-8 words, body 10-25 words |
| S04 | press bar | optional | Press or awards on record | names only |
| S05 | comparison table | optional | Us vs an unnamed typical competitor | 4-6 rows |
| S06 | stat strip | optional | Clinical or testing proof | 2-3 allowlisted stats with timeframe labels |
| S07 | timeline | optional | Results timeline | 3 steps (week 1, week 4, week 12) |
| S08 | founder note | optional | Why I made this / why we let you try it | 1-2 paragraphs, 30-60 words; signoff |
| S09 | reviews | yes | Reviews, ideally tagged by time used | 3-6 verbatim |
| S10 | faq | yes | Choosing the variant, will it suit me, how to use, returns | 4-6 Q&A |

## Adaptation notes

No ad-only price: the offer bar carries the ad's code or offer instead. No risk reversal: use the standard guarantee; never invent a trial.

## Watch-outs

The offer on the page must match the ad exactly (Open Farm's ad promised WELCOME20; the page never showed it).

_Generated from `templates/INDEX.json` by `scripts/lp-validate-templates.py --write-cards`. Edit the JSON, not this file._

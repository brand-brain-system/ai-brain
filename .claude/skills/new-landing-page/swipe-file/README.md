---
title: Landing page swipe file
owner: Alex Cooper
built: 2026-09-29
purpose: Template library for the landing-page skill Alex is demoing in the Parker webinar (week of 2026-09-28)
window: last 90 days, 2026-07-01 to 2026-09-28, Meta-reported
status: research reference. The templates and page teardowns are safe to show. Everything under "Private evidence" and every "Where the money goes" table in brands/ is client ad-account data. Do not screen-share it.
---

# Landing page swipe file

**Trimmed 2026-10-01** to the 14 pages and 7 templates Alex kept (from 35 pages and 10 templates), then the same day to **11 pages and 5 templates**: Alex removed 1 Quiz finder (primal-queen-2) and 7 Angle-swap short page (honeylove-2a, honeylove-2b) after testing every template on two brands. The five templates were renumbered 1 to 5 the same day (old 2, 3, 4, 6, 8 became 1, 2, 3, 4, 5). The research findings and rules below were drawn from the full 12-brand set and still mention those brands.

What the biggest Parker accounts actually send paid traffic to, and the reusable outlines behind those pages.

**How it was built.** We took 12 of the highest-spending brands Parker can reach. For each one we pulled the top 40 ad groups by 90-day Meta spend and grouped them by landing page. Then we toured the two or three pages carrying the most money, section by section, on a phone-sized view. "Most successful" here means the pages Meta keeps putting the most money behind, read against each account's own CPA and ROAS. It is not a controlled test of page against page.

**To look through the pages,** open `index.html` in this folder (double-click it in Finder). It shows all 14 pages as phone-width screenshots, filterable by template, with links to each live page and breakdown. Private spend numbers stay hidden until you switch them on. The screenshots live in `screenshots/`, captured 2026-09-29.

**To build a page from one,** press **Build this one** on its card in `index.html` and paste the copied line to Claude with the brand's name. That runs the `new-landing-page` skill in `../new-landing-page/` (its `README.md` has the nine steps).

**How to use it.** Start with the seven master templates below. Each one names when to use it, the outline to fill, the rules that make it work, and the live pages it came from. The brand files in `brands/` hold the full teardowns, the top ads behind every page (with Parker and media links), and a template outline for each page.

## The brands

| Brand | Category | Pages torn down | File |
|---|---|---|---|
| Rugiet | Men's sexual health (telehealth) | Reasons listicle, head-to-head advertorial | `brands/rugiet.md` |
| Grüns | Gummy greens supplement | Limited flavor drop | `brands/gruns.md` |
| Laura Geller Beauty | Makeup for mature skin | Standalone kit page for beginners | `brands/laura-geller.md` |
| Honeylove | Bras and shapewear | Ad-built product page, first-person advertorial | `brands/honeylove.md` |
| Primal Queen | Women's beef organ supplements | Founder-story long sales page, founder-letter advertorial | `brands/primal-queen.md` |
| mindbodygreen | Supplements | Doctor-recommends listicle | `brands/mindbodygreen.md` |
| Harry's | Men's grooming | Head-to-head review advertorial | `brands/harrys.md` |
| The Perfect Jean | Men's jeans | 5 reasons page on the store | `brands/the-perfect-jean.md` |

## The biggest finding: one template, many front doors

The big accounts don't build one page. They build **one template and clone it for every winning angle**, changing only the top of the page.

- Primal Queen runs its long founder page as `/pages/tiktok`, then clones it for libido, perimenopause, Canada and international traffic. Only the headline and testimonials change.
- Honeylove makes a short page per winning ad angle ("actually lifts", "best bra for mature", "worth the penny"). Every one sits on the same buy box.
- Grüns runs at least five versions of its card-flip game, plus a page per celebrity and creator.
- Rugiet runs the same numbered-reasons page for two products (Ready and Go Long).
- Seed sends almost everything to one quiz and swaps only the promo code in the link, one code per creator.

**For the skill, that means the job isn't "write a landing page."** It's this: pick the template once, then write a new top of page (headline, three benefits, featured review, proof) for each ad angle, so the page says what the ad said.

## The master templates

### 1. Reasons-why listicle

**Seen at:** Rugiet (https://get.rugiet.com/ready), mindbodygreen (https://shop.mindbodygreen.com/pages/lp-magnesium-listicle), The Perfect Jean (https://theperfectjean.nyc/pages/5-reasons-why-to-try-the-perfect-jean). Also a Parker house build in the Grüns look, `tpj-gruns-1` (`pages/tpj-gruns-1.html`, 2026-10-01): kept because Alex liked the design, not because it has spend behind it.

**Use when:** lots of different creators and angles feed one page, and the buyer needs several reasons, not one. It works for Exploration and early Evaluation.

**Outline**
1. Offer bar: [discount] + [code or "applied automatically"].
2. Headline: ["N reasons [customer count] [audience] love / switched to [product]"], or ["Why doctors recommend [product] for [problem]"]. Keep the ad's voice or joke.
3. Byline (advertorial style): [author name + relatable title + photo + last-updated month]. Or a celebrity or expert note, with a pull quote taken from the ad.
4. Subhead: [one-line product truth] + [3 proof points].
5. Optional comparison table: [us vs 2 named rivals on price, build, range, returns, signature feature].
6. Reasons 1 to N, each: [numbered claim headline] + [2 to 3 sentences with a number] + [image] + [call to action]. Order: [core benefit or speed first] → [fit or range] → [reviews and repeat buying] → [guarantee] → [durability or lasting results] → [price vs rivals] → [the social payoff or zero risk last].
7. Trick from mindbodygreen: make the last reason "results build over months", so the article sells the bigger plan before the buy box.
8. Authority wall: [logos] + [named experts].
9. Offer card or buy box: [from $X] + [crossed-out anchor] + [what's included] + [plan cards] + [risk reversal].
10. Reviews with short headlines, then FAQ, then a sticky footer: [claim discount] + ["discount active"].

**Rules:** Put a call to action under every reason, all pointing to one link that already has the discount applied. A standalone page with no site menu beat the on-store version at The Perfect Jean (see the private evidence below).

### 2. Founder-story long sales page

**Seen at:** Primal Queen (primalqueen.com/pages/tiktok, and the founder-letter version at primalqueen.com/pages/marrow).

**Use when:** the product has a mechanism story (an old secret in a new format), the founder is the proof, and the audience is problem-aware and willing to read. It suits buyers 35+ who have "tried everything".

**Outline**
1. Countdown bar: [offer] ends in [timer].
2. Hero: [headline naming 2 to 3 symptoms] + [subhead: old secret, new format] + [product shot] + [call to action] + trust bar [customer count, rating, guarantee length, shipping].
3. Testimonial strip: [5 one-line named quotes, each on a different benefit].
4. Founder intro: [name, photo, the symptoms they had, before and after].
5. "I tried everything": [6 to 8 alternatives the reader has tried].
6. Mechanism: [why this ingredient] → [why you can't just take it raw] → [the product as the easy form].
7. Proof by numbers: [ingredient vs everyday food, with footnotes] + [purity badges].
8. Timeline: [1 week, 1 month, 3, 6, 12 months].
9. Objection: [taste, pill count, or habit] → [format or freebie that solves it].
10. Comparison table: [us vs the common alternative, 8 to 10 rows].
11. Who it's for, and who it's not for.
12. Enemy story: [who moved people away from the old way] + [what we believe].
13. Buy box: [countdown] + [subscription default with anchor, sale price, and every freebie priced in dollars] + [smaller tier] + [guarantee, cancel anytime, ship-today cutoff].
14. Stories tabbed by symptom, then an FAQ of 8 to 12 questions.

**Rules:** Clone it per symptom or audience and change only the headline and testimonials. The founder-letter version opens on one specific scene with a loved one. It closes with "a month from now..." and the founder's sign-off.

### 3. Advertorial (third-party review, head-to-head, or first-person)

**Seen at:** Rugiet (https://www.thecustomerdigest.com/post/rugiet-ready-vs-ro-sparks-vs-hims-hard-mints-vs-bluechew), Harry's (https://www.thequalityedit.com/articles/harrys-tattoo-frost-vs-hustle-butter-comparison), Honeylove (https://www.popdust.com/i-tried-honeyloves-crossover-bra-heres-my-honest-take-2665043503).

**Use when:** the category has a known incumbent to beat, or the audience trusts editorial more than ads. Older buyers read news-style and blog-review formats as content, not ads.

**Outline (head-to-head version)**
1. Publisher look: [site menu] + [advertorial or sponsored label] + [disclosure].
2. Headline: ["[You] vs [Rival 1] vs [Rival 2]: which [category] actually works?"] + [date] + [byline] + ["reviewed by [expert]"].
3. Top pick box: [product] + [exclusive code] + [call to action].
4. Intro: [how common the problem is, with a source] + [a named tester with an age] + ["we tested N; one clear winner"].
5. What to look for: [2 to 3 criteria that happen to match your unique mechanism].
6. Comparison table with winner cells highlighted.
7. Rounds 1 to 4: [criterion] + [winner line] + [proof or quote] + [call to action with code]. Concede one honest tie. Close on price per use.
8. Overall winner + expert quote + final call to action, then a reference list.

**Outline (first-person version):** [who I am + what never worked] → [failed fixes] → [where I found it] → [my doubts] → [objection handled] → [first use] → [a full-day test with one "I forgot I had it on" moment] → [result] → [proof and price] → [reader-only discount with a time limit, linked to the matching landing page, not the homepage].

**Rules:** Make sure the article covers the same product and angle as the ad. Honeylove's Popdust piece dates from 2023, was written for Google traffic, and reviews a different bra than the ad sending people to it.

### 4. Product page built for ad traffic

**Seen at:** Honeylove (https://www.honeylove.com/pages/crossover-bra).

**Use when:** the buyer is already sold on the category, and the product page is where they decide. The brands spending $1M+ on product pages don't send ads to the standard store page. Honeylove builds a custom `/pages/` version. Laura Geller runs a "-special" URL with a Meta-only price.

**Outline**
1. Promo bar: [the exact code or offer the ad promised].
2. Risk-reversal banner (if you have one): [$0 today / trial length / free returns].
3. Hero and buy box high on the page: [product name + category claim] + [what's inside in one line] + [rating + review count] + [crossed-out anchor → ad-only price] + [variant picker] + [quiz link for the hardest choice] + [subscription preselected, with a free gift on the first order].
4. Two buttons if you can: [buy now] and [try first for $0].
5. "Perfect for": [3 to 4 buyer problems in their words].
6. Press bar + three benefits + comparison against an unnamed competitor.
7. Clinical proof: [3 stats with timeframes] + [study details].
8. Results timeline: [week 1, week 4, week 12].
9. Fit, size or shade tool, then what's included and how to use it.
10. Founder note: [why I made this] + [why we let you try it free].
11. Reviews (tabbed by months of use at mindbodygreen), then FAQ, then a cross-sell row priced to clear the free-shipping threshold.

### 5. Offer lander (trial, free gift, or limited drop)

**Seen at:** Laura Geller standalone kit page (https://shop.laurageller.com/bsk-pro-aging-essentials), Grüns limited flavor (https://gruns.co/pages/first-order-raspberry-lemonade).

**Use when:** the ad is selling a specific offer: a low-cost trial, a product plus a free gift, or a limited variant.

**Outline**
1. Review strip or countdown bar.
2. Hero: [headline that is the ad's own value line] + [one-line pain relief] + [product or kit shot] + [call to action naming the offer, e.g. "Get the $10 starter set" or "Claim my free gift"] + [shipping and money-back line].
3. Icon row: [4 short promises].
4. Who it's for: [3 specific frustrations] + [a jab at the category leader's price].
5. Offer card: [trial price] + [crossed-out anchor] + [you save] + [what's in the kit] + [add to cart].
6. Pick your free gift (gift version): [2 to 3 gift options, each with a dollar value].
7. Proof: [headline clinical stat] + [results timeline] + [a buying checklist from a named expert that only your product passes].
8. Price comparison table vs a named rival, with a dated source footnote.
9. Reviews, FAQ, final call to action with the price stack.

**Rules:** Harry's runs at least 4 test versions behind one URL (story, engineering, value). Test the page the way you test ads.

## Which template for which ad

| If the ad... | Use | Why |
|---|---|---|
| Comes from many creators with different angles | 1. Reasons-why listicle | One page holds every angle, with a call to action under each reason |
| Tells a founder or origin story to a problem-aware, older buyer | 2. Founder-story long page | Older buyers will sit with a longer story, and the founder is the proof |
| Picks a fight with a known incumbent | 3. Head-to-head advertorial | It borrows editorial trust and makes the comparison for them |
| Speaks to a buyer who already wants the category | 4. Product page built for ads | The decision happens in the buy box, so put the offer and risk reversal there |
| Sells a trial, a free gift, or a limited drop | 5. Offer lander | The headline is the offer, word for word |

## Rules that held across the 12 brands

1. **The headline says what the ad said.** Harry's trial page opens on the ad's own line, word for word. Honeylove's angle pages repeat each ad's promise. Grüns lifts the celebrity pull quote from the ad itself. The breaks are real too:
   - Open Farm's top ad promises code WELCOME20, and the Canadian page it lands on never shows it.
   - mindbodygreen's cortisol ads land on a page that never says "cortisol".
   - iRESTORE sends educational ads to a sale-led hub.
   - Honeylove's Popdust article reviews a different bra than the ad.
2. **Subscription is the default, and every freebie gets a dollar value.** Grüns, Primal Queen, OneSkin, Seed and mindbodygreen all preselect the subscription. Primal Queen and iRESTORE put a price on every free item. Grüns lists what you give up if you pick one-time.
3. **Take the risk out inside the buy box.** Laura Geller's "try it for $0, pay only if you keep it" sits right under add to bag. Harry's leads with a $10 trial. Primal Queen says who the product is not for.
4. **A results timeline is on almost every page.** Seed, OneSkin, mindbodygreen and Primal Queen all show week-by-week or month-by-month results. mindbodygreen uses the timeline to sell the three-month plan.
5. **The page multiplies the angle and the offer. It doesn't replace them.** At mindbodygreen, the listicle and the plain product page for the same product landed at nearly the same CPA. Primal Queen's clones all run close to the account average. Open Farm's standard store pages all ran worse than their account. My read (inferred): pick the template for the ad's job, and don't expect the page type alone to rescue a weak angle or offer.
6. **Sometimes the best page is no page.** OneSkin's "Comment LOTION" posts send people to a direct message, not a page, and beat every page the brand runs on CPA.
7. **These buyers skew older, and they read.** In the 30-day pull, most spend at Laura Geller, Honeylove, mindbodygreen and Rugiet went to people 45 and up. Long pages with authority, timelines and editorial framing fit how that audience decides.

## Private evidence (do not screen-share)

Summed from the top 40 ad groups per brand by 90-day spend (2026-07-01 to 2026-09-28), Meta-reported. Page CPA is summed spend divided by summed purchases. Full tables are in each brand file.

| Page | Template | 90-day spend behind it | Page CPA | Account CPA |
|---|---|---|---|---|
| Rugiet `get.rugiet.com/ready` | Reasons listicle | $1,906,619.48 | $308.61 | $259.43 |
| Rugiet Customer Digest head-to-head | Advertorial | $380,876.02 | $217.52 | $259.43 |
| Honeylove `/pages/crossover-bra` | Product page built for ads | $1,507,562.44 | $70.30 | $62.93 |
| Primal Queen `/pages/tiktok` | Founder long page | $1,422,874.18 | $134.96 | $129.23 |
| The Perfect Jean 5 reasons (on store) | Reasons listicle | $151,607.82 | $91.22 | $92.90 |
| mindbodygreen magnesium listicle | Reasons listicle | $207,350.15 | $146.64 | $167.79 |


## Gaps

- **Screenshots are phone-width captures from 2026-09-29, cut off at 3,400 pixels tall.** Pop-ups were removed before capture on 8 pages (the Honeylove angle pages, The Perfect Jean's 5 reasons page, all three mindbodygreen pages, Open Farm's product page, and Laura Geller's best sellers grid). Open the live URLs to see the full pages.
- **Seed's quiz** is only seen through step 1 of 13. Going further means agreeing to Seed's health-data consent. Someone needs to click through it by hand and record the steps and the result screen.
- **Primal Queen's beef organ quiz** (try.primalqueen.com/f/PW56E33T) builds itself with scripts and couldn't be read.
- **OneSkin's Fermat funnel page** now redirects to the product page, and its limited summer duo page returns a 404.
- **Review widgets and some prices** load by script, so a few of them weren't captured (iRESTORE hub prices, some review lists). Each gap is marked in its brand file.
- **Spend covers only the top 40 ad groups** per brand, which is 42% to 63% of each account's spend where measured. It's Meta-reported, and no page comparison here is a controlled test.

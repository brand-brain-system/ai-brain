# Process: research the brand and fill the brief (step 2)

Goal: a complete `brief.json` the scripts can read and a `brief.md` a strategist can check, every field sourced, nothing guessed, and a clear read on whether the brand can fill the picked template.

## Steps

1. **Decide the source of truth.** A brand with a built brain: fill from the docs in the auto-fill map in `brief-schema.md`, quoting the doc and line for each field in `brief.md`. No brain: fill from the pasted context only and set `external: true`.

2. **Settle the angle; pull the ad only if one was named.** The angle (what the page sells, to whom) comes from the ask. If the ask gives none, propose one from the evidence (the brain, the account's proven lines from a top-ads pull, the customer voice) and state it in one line at intake; do not block on it, and never ask for an ad (Alex, 2026-10-01: "We don't have to necessarily do this. I don't like forcing this into the skill."). Record it in `brief.json` `angle`. If the reviewer named an ad: with a Parker ad link or id, `search_facebook_ads_sql` with `adIds` and `include: ["scripts"]` returns the hook, the ad copy, the angle, the landing URL it uses today and who it is reaching. With "the winners for <product>", pull the top ads by spend for the last 30 days and read the top three. Record in `brief.json` `ad`: the hook verbatim, the angle in one line, the person it speaks to, and the offer exactly as the ad states it. Keep the Parker link and the media link in `brief.md`. If the reviewer only described the ad, write "described by <name>, <date>". No ad named: leave `ad` null.

3. **Pull the buyer's words, at volume, from every source Parker has** (Alex, 2026-10-01: "ensure that we're using as much of the customer voice from Parker, whether it be customer reviews, ad comments, or whatever, to influence the copywriting"). Method: `brain-system/creative-strategy-context/customer-review-mining-method.md` (golden nuggets, denominators, theme rates, the brand-self-echo watch). The page's copy is built from this bank, so the bank comes before a single line is written. Run all of these that exist for the brand, in parallel:
   - **Reviews, semantic:** at least four `search_customer_reviews_semantic` pulls of up to 50 each: the page's angle in the buyer's terms, the pain before the product, the result after it, and the top objection (fit, durability, price, "is it for me"). Add `minRating 4` for outcome language and `maxRating 3` for objections.
   - **Reviews, counts:** `search_customer_reviews_sql` with `returnData false` on each theme's keywords, so every theme carries a count out of the total ("1,109 of 41,883"). A phrase without a denominator is an anecdote.
   - **Ad comments:** `search_facebook_ad_comments_semantic` on the angle and on the objections across the account (people in their own words before they bought), plus, when an ad is named, `search_facebook_ad_comments_sql` with its `adId`.
   - **Post-purchase survey**, if connected: `semantic_search_post_purchase_survey` on why they bought and what almost stopped them.
   - **Reddit and TikTok**, when the category is talked about there: `search_reddit_posts_and_comments`, `search_tiktok_videos` on the problem in plain words. Unprompted language from outside the brand's own channels is the strongest kind.
   - **The brain's customer-voice docs** (`personas/voice-of-customer/`, `personas/persona-voice-library.md`): read them, then re-check any phrase you plan to use against a fresh pull.
   Into `brief.json` `voc` (schema in `brief-schema.md`): a **bank** of 30 or more verbatim phrases, each tagged with its kind (pain, outcome, objection, trigger, metaphor, identity), its source and date, and its theme count; `claims.reviews` (full, verbatim reviews with name, rating, platform, date: the only quotes the page may show as quotes); and `story.objections` in the buyer's own words. Record every pull with its query and count in `voc.pulls`. If a source is not connected, say so in `brief.md` and name what it would add.

4. **Fill every field in the schema.** Prices as they will print. Every number that may appear on the page goes on `claims.allowlist`. `urgency_allowed` from the brand's stated rule, not from the calendar. `tokens` from the brand's identity doc: the closest Google Fonts match to their type, their button colour as `accent`.

5. **Check the template fit** (`strategy.md` section 4). Walk the template's `requires` and each section's proof needs against the brief. Write a "Template fit" block in `brief.md`: which sections run as written, which take the card's adaptation, which optional sections drop and why, which photos exist and which are needed.

6. **Find the photos.** The brand's asset folder first (`other/brand-assets/` in a brain). List each with what it shows. For photos on the brand's own site, ask before saving them: name the files and the source, and save into `<run>/assets/` only on a yes. Never take an image from a reference page.

7. **Ask once for the gaps.** One message. Each missing field with why it matters in a clause. The standing gaps are the offer (number, code, dates), the button link, and any proof the template needs that is not on record. Leave the offer as `[OFFER]` and say the page will carry the placeholder until it is stated. Do not wait on taste questions; only on facts.

8. **Write `brief.md`.** A readable version of the JSON with a Sources block: every doc line used, every pull made, every field stated by a person with name and date, and the Template fit block.

## What never to do

- Infer a price, a discount, a guarantee window, a review count or a rival's fact from category norms.
- Shorten or tidy a review. The quote stays as written or is not used.
- Write a named ad's hook from memory. Pull it.
- Fill the auto-fill from memory of the docs. Open them; line numbers move.

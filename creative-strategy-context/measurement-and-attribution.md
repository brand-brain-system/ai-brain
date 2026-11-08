---
summary: "Reading DTC numbers when tools disagree: store as truth, survey, holdout tests, incremental CPA."
---

# Measurement and attribution

Ours. How to answer "which marketing actually made the sales?" for a direct-to-consumer brand, and
how to write the answer so nobody mistakes a model for a fact. Used by `ad-account-analysis`,
`weekly-brain-report`, `season-report`, `lifecycle-flows` and `growth-plan`. The definitions of the
metrics themselves (ROAS, MER, NC CPA, attribution windows) live in `ad-metrics-glossary.md`.

Built on Corey Haines' open-source `attribution` skill (MIT, `brain-system/third-party/marketingskills/MANIFEST.md`),
cut to the DTC case and rewritten in our words and labels. The paradigm descriptions (MTA, MMM,
incrementality) are standard practice; nothing here is a measured result of ours yet.

## The one rule

**Count orders once, in one place; let every tool argue only about where they came from.** The store
(Shopify or whatever the brand sells through) is the source of truth for how many orders and how much
revenue. Meta, Google, GA4 and the email tool each explain a share of those orders, and their shares
add up to more than 100 %, because each one claims every order it touched under its own rules.

So never add platform conversions together. Meta says 100, Google says 80, the email tool says 60, the
store had 150 orders: the brand had 150 orders with overlapping claims, not 240.

## Why each source is wrong in its own direction

| Source | Leans towards | Because |
|---|---|---|
| **Meta Ads Manager** | Counting too much for Meta | Click and view windows (`ad-metrics-glossary.md`, "Attribution Window"): a person who saw an ad and bought a day later through Google is still a Meta purchase. Modelled conversions fill gaps it can't see |
| **Google Ads** | Counting too much for Google, especially branded search | People who already decided (often because of an ad elsewhere) search the brand name and click the ad |
| **GA4 and other web analytics** | Last click; too little for social | Loses people across devices and in in-app browsers, loses those who decline cookies, and files the unknown under "direct" |
| **The email and SMS tool** | Counting too much for email | Credits an order to a message opened or clicked days before, however the buyer arrived |
| **Post-purchase survey** | The memorable touch | People remember the TikTok or the friend, not the retargeting ad that came after |
| **The store** | Nothing (for counts) | It holds the real orders; it only knows the last click's source, if that |

## What to use, by size

Match the effort to the size of the decision.

- **Small brand, one or two channels:** the store as truth, UTM tags on every link, last non-direct
  click in GA4, and a post-purchase survey. That is enough. A media mix model is overkill
- **Growing brand, several channels:** add **MER** (store revenue ÷ total ad spend) and new-customer
  cost (all spend ÷ new customers from the store) as the board numbers, read platform ROAS only for
  comparing ads inside one platform, and run one incrementality test a quarter on the channel whose
  budget would hurt most to get wrong (usually Meta retargeting or branded search)
- **Large brand, offline or brand spend (TV, podcasts, outdoor, big influencer deals):** a media mix
  model (Meta's Robyn and Google's Meridian are open source) on 2-3 years of weekly data, checked
  against incrementality tests. Needs real swings in spend to learn anything

## The post-purchase survey

The cheapest honest signal there is, and the only one that sees word of mouth, podcasts, organic
TikTok and a friend's recommendation.

- **Where:** the order-confirmation page (most survey apps for Shopify do this), right after the order
- **The question, in Danish:** "Hvor hørte du første gang om os?" One answer from a short list of the
  brand's real channels (Instagram, Facebook, TikTok, Google, en ven eller familie, en podcast, en
  artikel, en butik, andet) plus a free-text box. Randomise the list order if the tool allows
- **Free text is customer language.** It goes to the research map (`research-map` skill) like any
  other quote, with its source
- **Read it as awareness, not credit.** "22 % say TikTok" means TikTok is where 22 % first noticed
  the brand, not that it earned 22 % of revenue. Use it to settle arguments between platforms and to
  spot channels the pixels can't see. Never turn it into a multiplier on platform numbers
- **It's a pull, not a census.** Note the response rate. A 15 % response rate from mostly loyal
  customers is a skewed sample; say so beside every share (`brain-system/system/evidence-and-labels.md`, "Every
  table states its limit")

## Incrementality: did it cause the sale?

The only way to know whether a channel *caused* orders that wouldn't have happened anyway is to hold
it back from some people and compare.

**Designs a DTC brand can actually run:**
- **Holdout in email and SMS flows:** a random 10 % don't get the flow. The difference in order rate
  is the flow's real effect. The cleanest test a brand has, and free (`lifecycle-flows`)
- **Meta's own lift test** (Conversion Lift, where the account has access): Meta withholds the ads
  from a random control group. Needs enough conversions; check the requirements in the account
- **Geo test:** run a channel in some regions and not in comparable ones. Denmark is small, so regions
  are few and noisy; prefer the platform's lift test when it's available
- **On/off:** switch a channel off for a set period and watch the store's total. Cheap but weak:
  seasons, sales and other campaigns move the total too. Only for a clear question ("does branded
  search do anything?") and read with that caveat

**Reading a result (no statistics needed):**
1. **Lift = the exposed group's rate minus the control's.** Exposed 4.2 %, control 3.6 %: the channel
   added 0.6 points. The other 3.6 would have bought anyway, which is why last-click ROAS overstates
2. **Look at the range, not the point.** "5 % lift, between -2 % and +12 %" includes zero: no proof of
   anything. The test was too small to decide, not a sign the channel is dead
3. **Incremental CPA = spend ÷ the extra orders.** That is the number that should move budget, and it
   is almost always worse than the platform's CPA. That's the point of the test
4. **Log it as an open loop or a validation** in the brain (`brain-system/system/open-loops-system.md`). One test is
   one result; a rule needs two

## The blind spots

- **"Direct" is a junk drawer:** typed URLs, but also dark social (DMs, group chats), app-to-web
  switches, and anything tracking lost. A large direct share usually means a top of funnel that works
  where nobody can see it
- **Branded search harvests demand made elsewhere.** Split branded from non-branded in every report,
  or the channel that made people search gets defunded
- **AI assistants** (ChatGPT, Perplexity, Google's AI answers) recommend products and send people via
  branded search or direct. Invisible in analytics; the `ai-search` skill checks it from the outside
- **Consent:** people who decline cookies vanish from GA4 and partly from the pixels. The store still
  counts them; another reason it is the source of truth

## How to write it in the brain

Every attribution statement carries its label (`brain-system/system/evidence-and-labels.md`):
- The store's order count and revenue for a window: **Verified** (name the export and date)
- A platform's claimed conversions or ROAS: **Stated** by the platform. Write "Meta reports ..."
- Channel shares from a survey: **Verified** as survey answers, with n, response rate and window;
  their meaning as credit is **Inferred**
- A lift test result: **Verified** for the test, with its range; the rule it suggests is **Inferred**
  until it holds twice

The readout form, for any report that answers "where did sales come from":

| Channel | Platform claims | GA4 (last non-direct) | Survey (first heard) | Our read | Label |
|---|---|---|---|---|---|

Under the table: the source of truth and its total, what can't be seen, and the one test worth
running next.

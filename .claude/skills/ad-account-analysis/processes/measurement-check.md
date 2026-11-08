# Process — Measurement Check

Is the account counting right? Every other process reads Meta's numbers as if they were true. If
the pixel double-counts, misses half the purchases or optimises for the wrong event, a creative read
on top of it is wrong in a way no lens can see. This check comes first when the numbers look odd,
the first time an account is read, after a site, theme or checkout change, and once a month.

Read-only. It looks at settings, diagnostics and numbers; it changes nothing in Events Manager, Ads
Manager or the store.

Built 7 Nov 2026 on the open-source `claude-ads` (MIT, Daniel Agrici: its Meta control catalog,
conversion-tracking reference and cold-start contract) and the tracking checklist in
`irinabuht12-oss/marketing-skills` (MIT). Rewritten for a Danish Shopify brand on Meta; their
thresholds were not taken over as rules. Credits: `third-party/open-source-skills/MANIFEST.md`.
How to read the numbers once they are trusted: `brain-system/creative-strategy-context/measurement-and-attribution.md`.

## Required inputs

Ask once for what's missing. A screenshot is enough for every item.

- **Events Manager, the dataset (pixel) used for the ads:** the Overview (events by browser and
  server over the last 7-28 days), Diagnostics, and Event Match Quality for Purchase
- **The ad account:** the optimisation event and attribution setting of each live campaign, and
  purchases and purchase value for the last 28 days
- **The store, same 28 days:** orders and revenue (Shopify Analytics, net of tests and cancellations),
  and how the pixel is installed (Shopify's Facebook & Instagram app and its data-sharing level, a
  server-side tool, or a hand-installed tag)
- **One link from a live ad**, to read its URL parameters
- What changed recently on the site (new theme, new checkout, a consent banner, a new app)

## The controls

Each gets **pass**, **fail**, **unknown** (the evidence isn't there: say what would settle it) or
**n/a**. Never infer one from another: a new ad account doesn't prove a new pixel, and raw events
don't prove that purchases are counted.

| # | Control | Pass looks like |
|---|---|---|
| 1 | Pixel fires on the store | Page view, view content, add to cart, initiate checkout and purchase all arrive, from the store's own domain |
| 2 | Server events (Conversions API) | Purchase arrives from both browser and server. Shopify's app at its highest data-sharing level does this; a hand-installed tag usually doesn't |
| 3 | Deduplication | Browser and server copies of one purchase share an event ID and count once. Diagnostics shows no deduplication warning; Meta purchases are not far above store orders (row 6) |
| 4 | Event Match Quality, purchase | Read Meta's score and its own advice as Meta's view, not a grade. A low score with email and phone missing from server events is the fixable case |
| 5 | Domain verified | The store domain is verified in Business Settings |
| 6 | Counts reconcile | Meta's purchases (at the account's attribution setting) against store orders, same 28 days. Meta usually claims less than the store at 7-day click and can claim more with view-through; a Meta count **above** store orders at click-only is a double-count until proven otherwise. Write both numbers, never a verdict without them |
| 7 | Value and currency | Purchase value in DKK, matching the order value (with or without VAT and shipping, consistently). A value of 0, a fixed value or a foreign currency is a fail |
| 8 | Optimising for the business event | Sales campaigns optimise for purchase, not add to cart or view content, unless the human chose that on purpose (a new pixel with too few purchases: write the reason) |
| 9 | Attribution setting known and stable | The same setting across the campaigns compared, and no change inside the period being read. A change splits the period: say where |
| 10 | URL parameters | Live ads carry UTM parameters (source, medium, campaign, content with the ad name or ID), so GA4 and the store's reports can see Meta |
| 11 | Consent | The banner fires the pixel only after consent where the brand's setup says so; the share of visitors who decline is known or marked unknown. Declines make Meta and GA4 count less than the store, which is normal |
| 12 | Data freshness | Events arrived in the last 24 hours; no gap since the last site change |

**Maturity, three separate reads.** Account: has it spent before, and when did it start? Pixel:
when did valid events start? Purchases: how many purchases did the optimisation event record in the
last 7 and 28 days? Mark each **cold** only when the evidence shows it; otherwise **unknown**. When
any is cold, the creative read that follows says so and makes no benchmark comparison, and a new
pixel is never a reason to call an ad bad.

## Execution

1. **Collect the inputs** and write down what is missing as **unknown**, not as a fail.
2. **Run the controls in order.** 1-3 first: if purchases aren't arriving or are counted twice,
   stop the rest of the analysis and say so in the headline read.
3. **Trace one real order** when access allows: one order number from the store, the matching
   purchase event in Events Manager's test or activity view (browser and server, one counted), and
   its value. One traced order beats a page of settings screenshots.
4. **Write the reconciliation line** (control 6) with both numbers and the window, in the form
   `measurement-and-attribution.md` uses. The store is the truth for how many orders there were.
5. **Rank the fails by impact on the read:** no purchase event or a double count first (every number
   is wrong), then wrong value or optimisation event (the algorithm learns the wrong thing), then
   missing server events, match quality and parameters (fewer purchases seen, weaker reports).

## Output

The process's headline read is one of three:
- **Numbers usable**: the creative processes can run as normal
- **Usable with a caveat**: name it ("Meta sees about 70 % of store orders; compare ads with each
  other, not with the store's CPA")
- **Not usable yet**: name the fix and who does it (the person with Shopify or Events Manager
  access, often outside the team). No creative verdicts until it is fixed

Then the control table with the evidence per row, and the fix list. Every fix follows the
recommendation rule in `SKILL.md`. Save it in the brain's `audits/` as
`measurement-check-<YYYY-MM-DD>.md`, so the next read can see what changed.

## Never

- Change a setting, install an app, edit the theme or send test purchases with real payment
- Call tracking healthy from settings screenshots alone: "configured" is not "counting right"
- Add platform conversions together, or treat Meta's diagnostics as proof
- Ask for or store a pixel access token, API key or customer data in the brain or this repo

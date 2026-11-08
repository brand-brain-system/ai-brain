# Flow library

The flows a DTC brand usually needs, each with its job, trigger, timing, exit and legal basis. Timings
are starting points to test, not rules: the brand's own results in `lifecycle/results.md` win. Basis
codes: **C** = consent (mail and/or SMS, covering the range), **E** = the existing-customer exception
(similar products only), **S** = service message (no product offer). Rules behind the codes:
`dansk-lovgivning.md`.

Structure informed by Corey Haines' `emails` and `sms` skills (MIT); timings and copy rules
rewritten for Danish law and DTC. Their benchmark figures are US vendor numbers and are not used.

## Before the first order

| Flow | Job | Trigger | Messages and timing | Exit | Basis |
|---|---|---|---|---|---|
| **Welcome** | Turn a signup into a first order; set the voice | Joins the list (popup, footer) | 3-5 emails over 7-14 days: 1) deliver what the signup promised, now; 2) why the brand exists, in a customer's words; 3) the best proof (a real review, the guarantee from the proof inventory); 4) the main objection answered from VoC; 5) a reminder of the code, if one was promised, with its end date | Orders | C |
| **Browse reminder** | Bring back someone who looked at a product | Viewed a product, no cart, identified profile | 1 email after 2-6 hours: the product, one reason from reviews | Adds to cart or orders | C (see the cart rule) |
| **Cart reminder** | Recover a started order | Added to cart, no checkout | 2-3 emails: 1 hour, 24 hours, (72 hours). Discount, if any, only in the last, never the first: an early code teaches people to abandon | Orders | C, consent required (Verified) |
| **Checkout reminder** | Same, for someone who reached checkout | Started checkout, no order | As the cart reminder, first one sooner (30-60 min); SMS only on an SMS consent | Orders | C |
| **Back in stock** | Tell people who asked | Signed up on a sold-out product | 1 email (or SMS if they chose it) when stock returns | Orders | The signup is the consent to this message |

## After the first order

| Flow | Job | Trigger | Messages and timing | Exit | Basis |
|---|---|---|---|---|---|
| **Order and shipping** | Reassure, cut "where is my order" mail | Order, shipped, delivered | Confirmation, shipped with tracking, delivered. No product blocks | — | S |
| **How to use it** | Get the product used right, so it works and isn't returned | Delivered | 1-2 emails after delivery: how to start, the mistake customers mention most in reviews | Return | S if purely how-to with no offer (Inferred); otherwise E |
| **Review request** | Real reviews from every buyer | Delivered + time to try (product-dependent, often 7-14 days) | 1 email, plus 1 reminder at most. Neutral, about this purchase, no reward | Reviews | Not marketing when neutral (Verified, four conditions) |
| **Post-purchase cross-sell** | The second order | 14-30 days after delivery | 1-2 emails: the product that goes with the one they bought | Orders | E (similar products only) or C |
| **Replenishment** | Reorder before they run out | Usage time of the product (from the brand: "a 250 ml bottle lasts ~6 weeks") minus a week | 1-2 emails, optional SMS | Reorders | E (same product) or C |
| **Second-order nudge** | Turn a one-time buyer into a repeat buyer | No second order after the brand's typical repeat window | 2-3 emails: best-seller among similar products, a customer story, then an offer if the human approves | Orders | E or C |

## Keeping the list alive

| Flow | Job | Trigger | Messages and timing | Exit | Basis |
|---|---|---|---|---|---|
| **Win-back** | Bring back a lapsed customer | No order in ~2x the typical repeat window | 2-3 emails over 3-4 weeks: what's new, a reason to return, last a direct question "skal vi blive ved med at skrive?" | Orders or clicks | E or C |
| **Sunset** | Stop mailing people who stopped reading | No opens or clicks in 90-180 days | 1-2 emails asking whether to keep writing; no answer, suppress | Clicks | C/E. Also protects deliverability, and old unused consents can lapse (Verified) |
| **SMS consent upgrade** | Add SMS for those who want it | Engaged email subscriber | 1 email with a neutral link to update the consent. Never by SMS | Updates consent | C (Verified route) |

## Campaigns (not flows)

Campaigns to the list follow the brand's marketing calendar and offers. Build order and the
sale-period rules come from `offer-ads` and `season-report`; every price claim follows `offer-copy.md`.
A campaign suppresses people who are inside a cart, checkout or welcome flow that day, so nobody gets
two messages selling at once.

## SMS

SMS is a layer on top of email, not a copy of it. Use it where speed matters: shipping, a checkout left
minutes ago, a drop or a sale's first and last hour, back in stock. Sender name first, one point, one
link, opt-out line. Danish letters fit 160 characters per part; an emoji or a curly quote cuts it to 70.
Fewer sends than email: each one costs money and an opt-out is permanent.

## The minimum program

For a brand with nothing running, in this order: welcome, cart and checkout reminders (to consented
profiles), order and shipping (clean), review request, post-purchase cross-sell or replenishment,
win-back, sunset. `strategy.md`, "Build order" says how to change the order for a brand.

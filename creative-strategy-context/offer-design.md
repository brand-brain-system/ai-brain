---
summary: "Building the offer itself: value levers, bundles, guarantees beyond the law, true urgency."
---

# Offer design

Ours. The offer is the thing the customer actually gets for the money: the product, how it is
packaged, what comes with it, what happens if it doesn't work, and why buy now. Better copy on a
weak offer moves slowly; a stronger offer with plain copy moves at once. Many "we need better ads"
problems are offer problems.

Where this sits: `strategy/offer-brief.md` (the `offer-brief` prompt) is the *argument* every ad
traces back to; the `offer-ads` skill handles one *sale* with real prices and dates. This doc is the
*construction* underneath both: what is on the table. Price-marketing rules have one home,
`brain-system/.claude/skills/offer-ads/offer-copy.md`; this doc points there.

Built on Corey Haines' open-source `offers` skill (MIT, `brain-system/third-party/marketingskills/MANIFEST.md`),
which adapts Alex Hormozi's value equation from *$100M Offers* (Stated: a practitioner framework, not
measured). Rewritten for physical products and Danish law; their service and course examples are not
used.

## The value equation

    perceived value = (dream outcome × belief it will work) ÷ (time to result × effort and risk)

Four levers. Price is what the value is compared against, not the value itself, so most "lower the
price" requests are really "raise the top or shrink the bottom" requests.

| Lever | For a physical product it means | Raised by | Evidence in the brain |
|---|---|---|---|
| **Dream outcome** ↑ | The life after the problem, in the customer's words | Naming the real goal behind the purchase | `personas/voice-of-customer/` desire phrases; research-map "desire" groups |
| **Belief it will work** ↑ | "Will it work for someone like me?" | Reviews from people like them, a demo, a guarantee, a named mechanism | `brand-lens.md` proof inventory; review mining (`customer-review-mining-method.md`) |
| **Time to result** ↓ | How soon they notice a difference, and delivery time | Fast delivery stated, a first result they can feel early, a starter kit | Reviews that say when it started working |
| **Effort and risk** ↓ | Choosing, setting up, using, returning | Fewer choices, a default bundle, a how-to, an easy return, a guarantee | VoC objections; returns reasons if the brand shares them |

**Diagnose first.** Score each lever 1-5 from the evidence above (say what each score rests on). The
lowest is where the next offer change goes. Change one lever at a time so the result can be read.

## The DTC levers

| Lever | What it does | What it costs | Watch for |
|---|---|---|---|
| **Bundle** (kit, set, 2-pack) | Fewer decisions, higher order value, the full result instead of half | Margin per unit; stock of the parts | A bundle "price" against a sum of parts is a saving claim: the parts' normal prices must be real (`offer-copy.md`) |
| **Free-shipping threshold** | Lifts order value towards the threshold | Shipping cost on the orders that pass | Set it a bit above the current average order; read the order-value spread first, not a rule of thumb |
| **Gift with purchase** | Adds value without cutting the price | The gift's cost and stock | A gift tied to a purchase is fine when the condition is stated; it is not "gratis" in the sense of free (`offer-copy.md`, "Avoid"; markedsføringsloven, Bilag 1 nr. 20) |
| **Subscribe-and-save** | Repeat orders, lower cost per order | The discount, every time; churn handling | Easy to pause and cancel, terms clear before purchase |
| **Starter or trial size** | Lowers risk for a first purchase | Margin; may attract people who never return | Follow with a replenishment flow (`lifecycle-flows`) |
| **Guarantee beyond the law** | Moves risk from the customer to the brand | Refunds | See "Guarantees" below. Never present a statutory right as one |
| **Objection-closing extra** | A small add-on that answers the top objection ("fits?" → free size exchange; "how do I use it?" → a guide) | Small, often digital or operational | Each extra must close a named objection from VoC; a pile of extras reads as inflation |
| **Real urgency** | A reason to buy now | Nothing if true | Only true deadlines and true stock (Bilag 1 nr. 7); see `offer-copy.md` for the 10-day rule on price reductions |
| **A discount** | Moves people who were nearly there | Margin, and it teaches people to wait | The weakest lever for a new customer: it says "worth less". Prefer value levers; keep discounts for real seasons and for customers |

## Guarantees

- **Never sell the law as a perk.** Presenting rights the customer has by law as a special feature of
  the offer is always misleading (markedsføringsloven, Bilag 1 nr. 10; read 31 Oct 2026). In Denmark
  that covers the 14-day right of withdrawal for online purchases and the 2-year right to complain
  about defects. "14 dages fuld returret" or "2 års reklamationsret" as a selling point is out
- **A real guarantee goes beyond the law:** a longer return window, returns on used products ("prøv
  den i 60 dage"), free return shipping, a result promise with clear conditions. It comes from the
  proof inventory's "Risk reversal" row in `brand-lens.md`, which only the brand fills
- **A commercial guarantee needs a written statement** on a durable medium by delivery, saying that
  the statutory complaint right still applies, who gives the guarantee and how to use it
  (markedsføringsloven, the section on handelsmæssig garanti; Verified that the requirement exists,
  read 31 Oct 2026). The brand writes it; copy only points to it
- **Conditions in plain sight.** "Pengene tilbage" with hidden conditions is a misleading omission

## Urgency and scarcity that are true

Real reasons to act now for a product brand: a dated sale (within `offer-copy.md`), a limited batch
that really is limited, a seasonal product, a delivery cut-off ("bestil før 20. december"), an
early-access window for subscribers. Each one must be provable, and the claim must stop being made
when it stops being true. A countdown that resets, "only 3 left" that never moves, or "last chance"
followed by an extension is illegal (Bilag 1 nr. 7) and gets screenshotted.

## Naming the offer

A named offer ("Startsættet", "Prøvepakken") reads as a thing to buy rather than a discount to
compare. Say what's in it in the name or right under it. No superlatives the claims gate doesn't
allow.

## How to use this in a brain

1. Read the current offer as the customer meets it (product page, cart, checkout) and write it down
   plainly: what, price, what comes with it, guarantee, deadline
2. Score the four levers with evidence; name the weakest
3. Propose one change, with its cost in kroner per order where the brand has given margins
   (`running-notes/success-definition.md`), and the metric that will show whether it worked
   (conversion rate, order value, return rate)
4. A person approves. Then it becomes an open loop and a test, not a rule (`brain-system/system/open-loops-system.md`)
5. When the offer changes, `strategy/offer-brief.md` and `brand-lens.md` (risk reversal) are updated
   by their owners, and the copy skills pick it up from there

Labels: a lever score is **Inferred** (say the evidence); a cost per order from the brand's numbers is
**Stated** by the brand; a test result is **Verified** for that test.

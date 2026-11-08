# Which mode

| Mode | When | What it delivers |
|---|---|---|
| **Audit** (default first run) | No `lifecycle/consent-audit.md` yet, or the human asks "what are we missing?" | The consent audit, the flow map with legal basis per flow, red flags, the ranked gaps (steps 2-4) |
| **Build** | The audit exists and a flow is picked | One flow, written and checked, as copy or as a draft in the platform (steps 5-8) |
| **Capture** | The brand wants more subscribers, or the audit found a weak signup | The signup form or popup: offer, consent text, timing, design brief (below) |
| **Campaign calendar** | A season, a launch or a sale is coming | The list campaigns for the period, dated, each with its basis and suppressions, pointing to `offer-ads` for the offer creative |
| **Results** | 30 or 90 days after a flow went live | `lifecycle/results.md` updated, and the next test proposed (step 9) |

## Build order

Start from `flows.md`, "The minimum program", then move a flow up when the brain says so:
- **The brand sells a consumable** (skincare, coffee, supplements, pet food): replenishment moves to
  second place. Ask the human how long one unit lasts; never guess it
- **Reviews are thin** (the proof inventory has few or old reviews): the review request moves up,
  because every static, landing page and ad that needs proof depends on it
- **High price, long consideration** (`brain-system/creative-strategy-context/advertising-luxury-and-higher-price-points.md`):
  the welcome flow carries more proof and objection-handling, and the cart reminder gets longer gaps
- **Gifting is a big share** (Q4, `brain-system/creative-strategy-context/gifting-and-q4-creative.md`): the buyer
  is not the user. Post-purchase cross-sell to the buyer is weaker; a "next year" reminder may not be
  similar products under the exception. Use consent
- **Few consents, many buyers**: the existing-customer exception carries the program. Fix the
  checkout text first (all seven conditions), then build flows on it

Rank the gaps by: how many people hit the trigger per month (from the platform or the store) ×
how close they are to buying × whether the legal basis is already in place. Say the numbers you used
and where they came from; a gap with no volume figure is ranked Data-limited.

## Capture

The signup form is where the legal basis is made, so it is part of this skill, not only a CRO task.
- **The offer:** a discount on the first order, early access, a guide or a prize draw. Never a "free
  gift" for the signup (consent counts as payment). A discount is fine when the product can also be
  bought without signing up
- **The consent text, in Danish, in the form itself:** which brand, which channels ("på mail og sms"
  as separate tick boxes if both), which products ("inden for vores produktsortiment" if the range is
  obvious), and that consent can be withdrawn at any time. No pre-ticked boxes
- **Timing:** not on the first second of the first page. After some engagement (scroll, time, a
  second page) or on exit, and never on top of the checkout. Mobile: a small bar or a slide-in rather
  than a full-screen cover
- **Evidence:** double opt-in where the platform supports it; screenshot the form and save it in
  `lifecycle/consent-audit.md` every time it changes
- **Out of scope here:** the popup's look and the A/B test setup. Hand the design brief to whoever
  builds the site, and the page context to `cro-review` if the form sits on a landing page

## Before the first brand

Written 31 Oct 2026 and not yet run on a brand. The legal file rests on the 2021 spam guidance; the
review-reward and cookie points are open (Data-limited). Run the audit on a test brand first and log
what broke in `feedback.md`.

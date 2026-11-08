---
name: lifecycle-flows
description: Plan, audit and write a brand's email and SMS program for the Danish market (lifecycle-flows, email flows, SMS flows, Klaviyo flows, welcome flow, velkomstflow, abandoned cart, forladt kurv, post-purchase, win-back, replenishment, nyhedsbrev, signup popup, tilmelding, retention, CRM). Audits how consents are collected and which flows run, ranks the missing flows, writes each email and SMS from the brand's customer language, and checks every message against the Danish spam ban (markedsføringsloven § 10), the existing-customer exception and the price rules. Drafts only: never activates a flow, sends a campaign or changes a list. Use when someone asks for email flows, SMS, a welcome series, cart reminders, a retention or lifecycle audit, a signup popup, or "what should we send our customers". Tool-agnostic: reads the brain's tool-map.md.
---

# Lifecycle flows (email and SMS, Danish market)

Always run inside the brand's brain folder. Paid social buys the first order; the email and SMS
program decides whether the second one happens, and for most brands it is the cheapest revenue they
have. This skill builds that program the Danish way: every message has a legal basis written next
to it, the copy comes from what customers actually say, and nothing goes live without a person.

The flow ideas build on Corey Haines' open-source `emails` and `sms` skills (MIT, credited in
`brain-system/third-party/marketingskills/MANIFEST.md`), rewritten for Danish law and our brain.
Several of their US templates would be illegal here ("selling fast" without it being true, a cart
reminder without consent, a discount for a review), which is why the legal file comes first.

## Where the knowledge lives

| File | Answers |
|---|---|
| `SKILL.md` (this file) | The steps and what must never happen |
| `strategy.md` | Which mode to run, and in which order to build flows |
| `dansk-lovgivning.md` | The Danish rules for consent, the existing-customer exception, cart reminders, review requests and service messages, with sources and labels |
| `flows.md` | The flow library: trigger, timing, job, legal basis and exit for each flow |
| `feedback.md` | What we've observed. A log, not a rulebook |
| `brain-system/.claude/skills/offer-ads/offer-copy.md` | The price-marketing rules (before-price, 10 days, "gratis"). Every discount in an email follows them |
| `brain-system/creative-strategy-context/measurement-and-attribution.md` | How to read flow revenue honestly (the platform's own number flatters it) |
| brain: `personas/voice-of-customer/voice-of-customer.md` | The words the emails are written in |
| brain: `brand-lens.md` | Voice, claims gate, proof inventory, risk reversal |
| brain: `lifecycle/` | The audit, the flow map, the drafts and the results (README there) |
| brain: `tool-map.md` | "Email and SMS platform" and "Store platform" roles |

## Prerequisites (check first, ask if missing)
- **The platform and access**, from `tool-map.md`: which email/SMS tool (Klaviyo, Rule, Shopify Email,
  Mailchimp, ...) and how Claude reaches it (connector, export, screenshots). No access: run on what
  the human pastes or screenshots, and say so
- **The capture points**: every place an email or phone number enters the list (popup, footer,
  checkout, account, contests, in-store). Screenshots or URLs. The legal basis of every later message
  depends on these
- **The brand lens and voice of customer.** Without them the copy turns generic: run the build first
- **The offer rules**: which discounts the brand allows in flows (none, a welcome code, free shipping),
  and the margin floor. Never invent a discount

## The steps

**1. Pick the mode** from `strategy.md` (audit, build, capture, campaign calendar). A brain with no
`lifecycle/consent-audit.md` starts with the audit, whatever was asked, unless the human says
otherwise: a beautiful flow sent on the wrong basis is a fine.

**2. Consent audit** (`lifecycle/consent-audit.md`). For each capture point: the exact consent text,
a screenshot, which channels it names (mail, SMS), which brand, whether withdrawal is mentioned in the
text itself, whether the box is pre-ticked, and what is offered for signing up. Check each against
`dansk-lovgivning.md`, "Valid consent" and "The existing-customer exception". Label every finding
Verified (seen on the page, dated) or Data-limited (couldn't see it). Flag in red: a free gift for
signing up, a pre-ticked marketing box outside checkout, SMS sent on an email-only consent, cart
reminders to people without consent, consents with no record of how they were given.

**3. Flow map** (`lifecycle/flow-map.md`). From the platform: every live flow with trigger, filters,
number of messages, timing, and the last 90 days of recipients and attributed revenue if visible.
Mark each with its legal basis (consent, existing-customer exception, service message) and whether
that basis holds. Then the gaps: which flows from `flows.md` are missing, ranked by
`strategy.md`, "Build order".

**4. STOP: approve the audit and the build order.** Show the red flags first, then the ranked gaps.
Legal flags go to the human as findings, not as advice: "a lawyer should confirm" where the
guidance is unclear.

**5. Write the flow** (`lifecycle/flows/<flow>/`). One file per flow: the flow sheet (trigger,
filters, exit conditions, timing, legal basis, discount if any) and every message:
- **Email:** subject (under ~45 characters, says what's inside), preview text that adds to the
  subject, body, one main call to action, footer with sender, unsubscribe link and promotion terms
- **SMS:** sender name first, one point, one short link, opt-out line. Count characters: up to 160
  per part with Danish letters (æ, ø, å are in the GSM-7 set), but one emoji or a curly quote drops
  the part to 70. Say the part count next to each SMS
- The copy follows the brand lens and the voice of customer: the customer's own words for the
  problem and the result, no claim the claims gate doesn't allow, no number outside the proof
  inventory. One job per message (`flows.md` names it)
- Danish copy passes `brain-system/scripts/voice-lint.py` and the AI-tells list
  (`brain-system/creative-strategy-context/ai-writing-tells.md`, "Danish copy")
- Every discount follows `offer-copy.md`: real, with its condition and end date stated, and only
  where the human approved it

**6. Checks before a person sees it.** Run the two review gates (`brain-system/system/evidence-and-labels.md`,
"Two review gates"): grounding, then voice. Then the legal pass, message by message, against
`dansk-lovgivning.md`, "Checklist per message". A service message that grew a product block is now
marketing: fix it or move the block.

**7. STOP: approve the copy.** Show the flow sheet and every message together, with the legal basis
per message.

**8. Hand over or set up as draft.** With a yes, either hand the copy over in the platform's shape, or
build it in the platform through the connector **as a draft / manual status only**. Never set a flow
live, never schedule a campaign, never import or edit a list, never change consent fields. Log what
was created in `lifecycle/flows/<flow>/setup.md`.

**9. After 30 and 90 days: results** (`lifecycle/results.md`). Recipients, click rate, orders,
revenue per recipient, unsubscribe and spam rates, per message. Read the platform's attributed
revenue as an upper bound (`measurement-and-attribution.md`); where a flow is big enough, propose a
holdout (a random 10 % who don't get it) and log it as an open test in `feedback.md`.

## Guardrails (never)
- Never activate a flow, send or schedule a campaign, or send a test to anyone but the human's own
  address
- Never send marketing without a valid basis. If the basis is unclear, the message waits
- Never offer a free gift in return for signing up, and never make a purchase depend on saying yes to
  marketing (`dansk-lovgivning.md`)
- Never write urgency, stock or "last chance" that isn't true; never a before-price that breaks
  `offer-copy.md`
- Never offer a reward for a review, and never only ask happy customers for one
- Never use a list, phone number or email bought from or shared by someone else
- Never store or segment on sensitive data (health, religion, sexuality, ethnicity), not even
  inferred from purchases. A health product's buyer list is itself sensitive: segment by product
  bought, never by a condition
- Personal data stays in the platform. The brain holds counts, copy and screenshots of forms, never
  customer lists

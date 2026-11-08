# Danish rules for email and SMS marketing

What `lifecycle-flows` follows, with the source for each rule. Labels as in the brains: **Verified**
(read in the primary source), **Stated** (a secondary source says it, not checked against the
primary), **Inferred** (our reasoning, with what it rests on), **Data-limited** (not checked; says what
would settle it). A working guide, not legal advice: for a paid client or a large program, have the
employer's lawyer confirm the consent setup.

Main source, read in full for this file: Forbrugerombudsmanden, *Vejledning om spamforbuddet* (2021),
chapters 6 to 11. Page numbers below are the guidance's own. Last checked: 2026-10-31.

Related rules that live elsewhere (one home each): the price-marketing rules in
`brain-system/.claude/skills/offer-ads/offer-copy.md`; outreach to creators in
`brain-system/.claude/skills/creator-recruitment/dansk-lovgivning.md`.

## The spam ban (markedsføringsloven § 10, stk. 1)

- **Verified.** Marketing by electronic mail (email and SMS) to a specific person needs that person's
  prior consent. A message that *asks* for consent is itself marketing, so you can't email people to
  ask if you may email them. (Kap. 7, p. 22)
- **Verified.** Breaking it can be fined when the business acted negligently (§ 37, stk. 3), and the
  business that sends, or on whose behalf it's sent, carries the responsibility. (Kap. 12, p. 39)

## Valid consent (kap. 7)

- **Verified.** Consent must be voluntary, informed, unambiguous and specific, read the same way as a
  GDPR consent. Withdrawal must be easy and free. (p. 22)
- **Verified.** The consent text itself must say that consent can be withdrawn. A link to the text is
  not enough; without it the consent is invalid. (p. 22, p. 25)
- **Verified.** The text must say which business (or brand) sends, and **which channels**: "mail",
  "sms". "Elektronisk post", "markedsføring" or "mail, sms mv." don't stretch to other channels. A mail
  consent never covers SMS. (pp. 23-25)
- **Verified.** It must be clear which products or categories the marketing is about. A brand whose
  range is well known can ask for "inden for vores produktsortiment"; products outside what people
  associate with the brand need naming. (p. 27)
- **Verified.** A pre-ticked box is not consent. Consent must be separate from the terms of trade.
  (p. 26)
- **Verified.** Buying may not depend on saying yes to marketing. A discount for saying yes is allowed
  when the product can also be bought at the normal price without saying yes. (p. 22-23, cases 15/02855,
  14/03912)
- **Verified.** If something is marketed as **"gratis"** or a gift, receiving it may not require a
  marketing consent: the guidance treats consent as payment, so "free gift when you sign up" is
  misleading. (p. 23, cases 15/08448, 18/05068)
- **Verified.** A prize draw ticket for signing up is allowed, under a separate guidance on contests;
  the consent must be as clear as the prizes. (p. 23, p. 25) *Data-limited:* that separate guidance
  (*Brug af konkurrencer ... ved indhentelse af forbrugernes samtykke*) was not read; read it before
  running a signup contest.
- **Verified.** Adding SMS to an existing mail consent needs a new consent. You may email the
  subscriber a neutral invitation to update the consent by link, but not text them to ask. (pp. 27-28)
- **Verified.** A consent can lapse when it isn't used for a long time; for consents collected in a
  contest the guidance points to about a year. Otherwise case by case. (p. 32)
- **Data-limited.** Consent from children and young people (section 7.7) was not read for this file.
  If the brand's buyers include under-18s, read it first.

## The existing-customer exception (§ 10, stk. 2; kap. 9)

Lets a shop email or text **its own customers** about **its own similar products** without a prior
consent. All seven conditions must hold, and the exception is read narrowly. (pp. 33-34)

- **Verified.** 1) The person bought something. A gift, a download, a contest entry, a quote or an
  account without a purchase is not a purchase, so those need consent. 2) The customer gave the
  address themselves in connection with the sale (pre-filled from their own account counts).
  3) They were told clearly, at the purchase, that they'll get marketing to that address.
  4) They were told at that moment that they can say no, easily and free. **A pre-ticked box they can
  untick is enough here.** 5) Every later message offers the opt-out. 6) Only the shop's own
  products, from the same legal entity: no partners, no sister company. 7) Only **similar products**.
- **Verified.** "Similar" means the same product category as what was bought; accessories and
  equipment for the product count. Bought a sofa: fabric care counts. Bought fabric care: sofas don't.
  Bought a bicycle: a helmet counts, a moped doesn't. The shop may define "similar" at the moment the
  address is given, but can't stretch it into other product groups. (pp. 34-35)
- **Verified.** The shop must be able to document how the checkout looked when the customer gave the
  address. (p. 38)
- **Inferred, from condition 7.** A brand with one product line (say, only golf accessories) can send
  its whole range to buyers; a brand spanning categories (skincare and supplements) must split by what
  each customer bought, or rely on consent.

## What counts as marketing, and what doesn't (kap. 6)

- **Verified: cart reminders are marketing.** A "tabt kurv" email needs prior consent. The consent can
  be given once for the future (a reminder every time I leave a cart in this shop) and must be
  withdrawable. (pp. 20-21, case 15/09634)
- **Inferred, from the same passage.** The same goes for browse-abandonment and back-in-stock
  messages to people who didn't ask for them. A back-in-stock alert the person signed up for is a
  consent to that message.
- **Inferred.** A valid email-marketing consent that covers the brand's product range covers cart
  and browse reminders by email too, since they are marketing of that range. Most Danish shops
  therefore send them only to subscribers. Confirm with the brand's lawyer if the consent text is
  narrow ("nyhedsbrev" only).
- **Verified: service messages are not marketing.** Order confirmation, shipping and delivery notices
  are service messages. (p. 20, case 16/06077) A message stops being service the moment it offers
  more products: an email offering add-on products is marketing. (p. 19) A logo with a neutral link to
  the shop is fine; any other promotion is not. (p. 19)
- **Inferred.** So "you might also like" blocks in order and shipping emails need consent or the
  existing-customer exception (and then only similar products). Without either, keep service emails
  clean.
- **Verified: reorder prompts lean towards marketing.** An optician's invitation to a sight test was
  marketing because it could lead to new glasses; for a customer with an ongoing lens subscription it
  was a service message. (pp. 19-20, case 18/06364) **Inferred:** a replenishment reminder for a
  one-off purchase is marketing (basis: consent or the existing-customer exception, where the same
  product clearly counts as similar); a notice about an active subscription's next delivery is
  service.
- **Verified: satisfaction surveys** are not marketing when their purpose is to measure satisfaction
  and they hold no product talk or branding beyond a signature and logo. (p. 17)

## Review requests (kap. 6)

- **Verified.** Asking a customer to review a specific purchase on a rating site is not marketing when
  all four hold: the shop sold the product; it asks right after the sale; it asks them to review that
  purchase; and the message is completely neutral, with no marketing. Logo and signature allowed.
  (p. 18, case 18/06294)
- **Verified.** Asking someone who has said no to these requests breaks good marketing practice
  (§ 3); a purchase term can make the request part of the deal unless that's unreasonable. (p. 18)
- **Inferred, from "completely neutral".** A discount in return for a review, a cross-sell block, or
  "share your love" wording makes the request marketing, so it then needs consent or the exception.
- **Data-limited.** Rewards for reviews, and asking only satisfied customers, are governed by
  Forbrugerombudsmanden's *retningslinjer om offentliggørelse af brugeranmeldelser* and the review
  platforms' own rules. Not read for this file. Until it is: no rewards, ask every buyer.

## What every marketing message must contain (§ 10, stk. 3; kap. 10)

- **Verified.** 1) Clear that it's marketing. 2) Terms of discounts, gifts and contests easy to find
  and clear. 3) Clear who it's from. 4) No links to sites that don't meet 1-3. 5) A way to stop the
  messages; an unsubscribe link is enough. (p. 36)

## Documentation (kap. 11)

- **Verified.** The business must prove every consent: who, when, and the circumstances, including
  what the person saw. A name, address and time isn't enough; an IP address isn't enough. Keep a
  screenshot, film or image series of the form. (pp. 37-38)
- **Verified.** Double opt-in is recommended. A confirmation email is weaker evidence. Neither repairs
  a consent that was invalid to begin with. (p. 37)
- **Verified.** Keep the documentation while the consent is used and two years after its last use
  (the limitation period). The person can't demand that this proof is deleted in that time. (p. 38)

## Tracking that feeds the flows

- **Inferred.** Browse and cart triggers rely on the email tool's tracking script on the site, which
  sets cookies and identifies visitors. That tracking falls under the site's cookie consent. Check that
  the cookie banner names the email tool and that the tool only tracks after consent. Data-limited
  until checked against the Danish cookie order (cookiebekendtgørelsen) and the Datatilsynet guidance.

## SMS specifics

- **Verified (same rules).** SMS is electronic mail under § 10: everything above applies, and a mail
  consent never covers SMS. (pp. 13-14, p. 25)
- **Inferred.** Danish law sets no fixed sending hours that we found. Send in the daytime; a text at
  night is a fast way to an opt-out and a complaint under good marketing practice (§ 3).

## Checklist per message

Run before every message reaches a person for approval.

1. Basis: consent (which text, which channel), the existing-customer exception (all seven, and is the
   product similar?), or service (no product offer in it)?
2. Sender clear, marked as marketing, opt-out link or SMS opt-out line
3. Discount or gift: real, terms stated, end date stated, and within `offer-copy.md`
4. Urgency, stock and "last chance": true and provable, or removed
5. Review request: neutral, right after the sale, about that purchase, no reward
6. No partner's or sister company's products under the exception
7. No claim outside the brand lens's claims gate; no number outside the proof inventory

## Sources
- Forbrugerombudsmanden, Vejledning om spamforbuddet (2021):
  https://forbrugerombudsmanden.dk/media/bjajzdv1/vejledning-om-spamforbuddet-2021-a.pdf
- Markedsføringsloven: https://www.retsinformation.dk/eli/lta/2024/1420
- Price rules: `brain-system/.claude/skills/offer-ads/offer-copy.md` (its own sources)

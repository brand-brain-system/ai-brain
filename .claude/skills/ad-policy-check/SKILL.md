---
name: ad-policy-check
description: Check paid ads against the ad platform's own rules and the rules of the Danish market before they launch (ad-policy-check, policy check, annonceregler, will Meta reject this, ad disapproved, afvist annonce, rejected ad, AI label, AI-mærkning). Reads the copy, the text in the image or on screen, what the picture shows and who is in it; fetches Meta's current policy text for the rules that apply; returns pass, fix or stop per ad and platform with the policy quoted, an honest rewrite and the labels the ad needs. Also diagnoses a disapproval and finds the line that caused it. Use before any paid ad goes live, after static-ads, offer-ads, video-edits, motion-ads, song-ads or ai-ad-generation, when Meta has rejected an ad, or when an ad gets no delivery. Checks only; never submits, launches or edits in the ad account.
---

# Ad policy check

The last gate before a paid ad goes to the ad account. Most disapprovals are preventable: a line
that implies the viewer has a condition, a fake play button, an unlabelled AI person. A rejected ad
costs a day; repeated rejections can restrict the account. This skill catches them first.

**What it is not.** Not legal advice, and not Meta's review: Meta decides. Claims are checked
first in their own home (`brand-lens.md`, the brief's "Claims allowed", `brief-check`); a line cut
there is not reworded here. This skill checks the **rules about how something may be said and
shown**, not whether it is true.

Built 7 Nov 2026 on the open-source `goose-skills` (`ad-policy-check`, `meta-ad-policy-checker`,
MIT, GooseWorks) and the "recommendation boundary" in `claude-ads` (MIT, Daniel Agrici). Rewritten
for our paths, our labels and the Danish market; credits in `third-party/open-source-skills/MANIFEST.md`.

## Where the knowledge lives

| File | Answers |
|---|---|
| `SKILL.md` (this file) | The order of checks, the platform rules we know, the verdicts |
| `feedback.md` | Disapprovals seen, rules that drifted, false alarms. A log, not a rulebook |
| `brain-system/creative-strategy-context/legal-ai-ugc.md` | The AI label (EU AI Act art. 50) and AI people |
| `brain-system/.claude/skills/offer-ads/offer-copy.md` | Danish price marketing (before-prices, "spar", 30-day lowest price, period) |
| `brain-system/.claude/skills/creator-recruitment/dansk-lovgivning.md` | Hidden advertising and the "Reklame" marking (markedsføringsloven § 6) |
| `brain-system/creative-strategy-context/algospeak.md` | Words that throttle delivery without a rejection |
| brain: `brand-lens.md` | Claims gate, health-claim rules for the category, never-say list |
| brain: `running-notes/feedback.md` | This brand's past disapprovals (the strongest local evidence) |

One home per rule: the Danish legal rules stay in the files above; this skill points at them and
checks that they were applied. The platform rules below have their home here.

## Inputs (ask once for what's missing)

1. The ads: headline, primary text, description, CTA button, the words in the image or on screen
   (end cards and captions included), and the image or frames. For video, the transcript and frames
   at each scene change (as `brief-check` extracts them)
2. Where it runs: platform(s) and placements, and the country (Denmark unless told otherwise)
3. The landing page URL, if there is one, and **who the ad runs from**: the Page and Instagram
   account shown at the top of the ad (the brand, a real creator's partnership ad, or another Page)
4. The brand's category. Regulated (food or supplements with health or nutrition claims, cosmetics
   with effect language, alcohol, weight loss, finance, crypto, gambling, dating, products for
   children, medicine, medical devices) changes the rules a lot
5. A Meta special ad category (housing, employment, credit, social issues/politics), if any. Rare
   for DTC; if it applies, say so in the hand-off so whoever launches sets it
6. Mode: **pre-launch** (default) or **disapproval** (an ad was rejected or gets no delivery)

## Step 1: which rules apply

Always: personal attributes, sensational content and fake interface elements, misleading claims and
non-functional landing pages, engagement bait, grammar and profanity, AI-made content.
Add by identity: the ad runs from any Page other than the brand's own (Page identity and, for a
creator, branded content).
Add by content: health or body (health and wellness, body image, before-and-after); prices, sales
or "free" (the Danish price rules); a creator's face or name (branded content and the "Reklame"
marking); alcohol, supplements, weight loss, cosmetics with effect language (their category rules);
a competitor named or shown (comparisons, trademarks); music (licence).

## Step 2: fetch the live policy text

Meta's rules change, and a list in a file goes stale. For each rule from step 1, fetch Meta's
current page from the Advertising Standards (`transparency.meta.com/policies/ad-standards/`). The
index is rendered by script, so search the policy title on that domain and open the canonical
page (example: Personal attributes is under
`.../ad-standards/objectionable-content/privacy-violations-personal-attributes/`). Never build a
URL from a rule name. Fetch each page once per run, not once per ad. When a page can't be fetched,
say so and use the rules below as the fallback, labelled "from the factory list, not checked today".
A batch of ten ads needs three to six pages, not thirty.

## Step 3: the rules we know (fallback and checklist)

**Meta (Facebook, Instagram)**
- **Personal attributes.** No assertion or implication that the viewer has a trait: race,
  ethnicity, religion or beliefs, age, sexual orientation, gender identity, disability, physical or
  mental health (conditions included), vulnerable financial status, voting status. Meta extends
  it to the viewer's family. "Kan du ikke sove?", "Din tørre hud…", "Har du eksem?", "Er du over
  50?" → rejected. Situation and behaviour pass: "kl. 11, og huden strammer allerede", "til dem der
  ligger og genspiller samtaler i sengen", "mine albuer". "Du" and "din" are allowed as long as no
  trait follows. First person from a real customer passes the rule; from a generated person it is
  banned anyway (`legal-ai-ugc.md`)
- **Body image and before/after.** Nothing that makes people feel bad about their body; no before
  and after for weight loss; for skin, hair and health, before/after needs the human's yes and the
  brand's evidence (same light, no retouch, a typical result). Prefer old routine vs new routine
- **Fake interface and sensational content.** No fake play buttons, close X, notification badges,
  fake DMs, fake system dialogs or fake platform UI; no shock images. Native formats (a note, a
  text message, a review card) are fine when they don't pretend to be a function of the app
- **Branded content.** A creator's face or name in a paid ad needs their permission and the
  paid-partnership label in the platform, as well as the "Reklame" marking where Danish law needs it
- **AI-made content.** A photorealistic AI person, an AI voice that could pass as real, or a
  realistic generated scene with people: the visible label in the asset (`legal-ai-ugc.md`, EU
  section) **and** the platform's AI disclosure switch when it is offered. One does not replace the
  other
- **Who the ad runs from.** The name at the top must be the advertiser, or a real creator or
  publisher who agreed to it and is labelled as a paid partnership. A made-up publication ("The
  Health Journal" run by the brand) or a made-up person (an invented name with an AI headshot,
  "sharing what worked for me") is a **stop**, whatever the post that suggested it calls it
  ("ad camouflage", "persona page"). Meta: its rules on authentic identity and inauthentic
  behaviour for Pages (fetch the current text). Denmark: the blacklist in markedsføringsloven
  bilag 1 (UCPD Annex I, points 11, 22 and 23c: paid editorial without marking, posing as a
  consumer, fake consumer endorsements). The honest version of the same idea: a real creator's
  partnership ad, or the founder's own profile, labelled
- **Text in the image.** Short: a hook and at most one proof line. Heavy text loses delivery
- **Landing page.** It loads, it sells what the ad sells at the price the ad says, and it carries
  every claim the ad makes. A page claim that would be flagged in the ad is flagged here too

**TikTok.** Stricter on supplements, weight and "too good to be true" results; no exaggerated
before/after; no imitation of TikTok's own interface; music only from the Commercial Music Library or
licensed/generated; its AI-generated content label for realistic synthetic media.

**Google (Demand Gen, Shopping, Performance Max).** Unclear prices, missing terms or unavailable
offers count as misrepresentation; product images carry no promotional text, watermark or border;
no gimmicky capitals or symbols.

**Every platform.** No rival logo or celebrity look-alike without permission; music licensed or
generated, never "the song from the reference"; health, alcohol and finance keep their category
rules in every placement.

**The Danish rules, checked through their homes.** Price marketing (`offer-copy.md`): before-prices
and "spar" only with a documented 30-day lowest price, a period stated or the 10-day rule, no
statutory right sold as a perk. Marking (`dansk-lovgivning.md`): "Reklame" first when a creator
posts it. Health claims (`brand-lens.md`): only the EU register's wording for what the product
contains. Children: no direct appeal to buy. The AI label (`legal-ai-ugc.md`).

## Step 4: judge each ad, element by element

For every element (headline, body, description, CTA, image text, picture, people, audio, landing
page) against every applicable rule, write a finding only when you can point at the exact words or
the exact place in the frame:

| Field | What goes in it |
|---|---|
| Where | ad id, element, the exact words or the frame and timestamp |
| Rule | the policy name, the URL fetched, and a short quote from it (under 15 words) |
| Verdict | **stop** (a clear "you may not": will be rejected), **fix** (likely rejected or throttled), **note** (an edge case Meta sometimes flags) |
| Why | one line from the quoted rule |
| Rewrite | the same offer and the same audience, said differently. A rewrite that changes the offer or the audience is a different ad: say so instead |

Rules for the judge:
- **Quote or drop it.** A finding with no rule text behind it (fetched today, or the fallback list
  labelled as such) is a guess. Drop it
- **Find the whole class.** One "Kan du ikke…?" usually means more in the batch. Check every ad
  for the same pattern before reporting
- **Never "pass" what you couldn't check.** Write "not checked: <rule>, <why>" (no frames, no
  landing page, page wouldn't load)
- **Fix honestly.** Rephrase to the rule, remove the fake element, add the label. Never disguise a
  violation to get past review (algospeak to hide a health claim is still the health claim)
- **Category doubts go to a person.** A regulated category with no rule in `brand-lens.md`: flag
  the whole set "needs a legal check before launch" and stop

## Step 5: report

One line per ad and platform in chat: `pass (Meta)` · `fix: <what> (<rule>)` · `stop: <what>
(<rule>)`. The table goes in `sprints/<sprint>/ads/policy-check-<YYYY-MM-DD>.md` with the policy
pages and the date they were fetched, the labels to add, and the switches to set at launch (AI
disclosure, paid partnership, special ad category). If any ad is **stop**, the batch doesn't go to
launch until it is fixed or dropped.

**STOP: approval.** The human accepts or rejects each rewrite. Rewrites that change on-image
text go back through the producing skill's own copy and image checks before anything is
re-rendered. Nothing is submitted from here.

## Disapproval mode

When Meta has rejected an ad, or an ad spends almost nothing:
1. Get the stated reason from the human (the rejection text in Ads Manager or Account Quality) and
   the ad itself. A screenshot is enough
2. Map the reason to the exact element. It is often the text, not the image; for video, check the
   on-screen text, the captions and the spoken words
3. Fetch that one policy page, quote it, and give the smallest honest fix. If the ad doesn't break
   the rule as written, say so: the human can request a review in Account Quality
4. Run the whole check on the fixed ad, not only the flagged line
5. Log it: the reason, the line, the fix and whether it passed after the fix, in the brain's
   `running-notes/feedback.md` (brand) and, generalised, in `feedback.md` here. Three rejections of
   the same kind in one brain become a never-say line in its `brand-lens.md`, with the human's yes

## Where it is called from

`static-ads` and `offer-ads` after the copy approval and again on the finished images; `video-edits`,
`motion-ads` and `song-ads` on the final render; `ai-ad-generation` on the prompt pack (the spoken
lines and the people in it); `brief-check` Mode B on finished ads. Any later route that writes to an
ad account (an MCP or API) runs this first and does nothing on a **stop**.

## Guardrails (never)

- Never submit, launch, edit, pause or appeal in the ad account
- Never rewrite a claim to keep it: claims are cut in their own check, not softened here
- Never call an ad safe: "no issues found against <rules> fetched <date>" is the strongest wording
- Never invent a policy, a quote, a threshold or a past rejection
- Never help set up a Page that hides who is advertising (a made-up publication or person), and
  never move a flagged ad to placements where the Page name shows less to get it past the check

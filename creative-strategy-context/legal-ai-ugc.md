---
summary: "Disclosure rules for AI-generated people in ads: the principle (label synthetic humans, not AI products or backgrounds), the EU AI Act's deepfake label (art. 50, since 2 Aug 2026) as it binds a Danish brand, the Danish likeness proposal, and New York's S.8420-A. Not legal advice."
doc: legal-ai-ugc
status: drafted
source: practitioner summary of NY S.8420-A (social thread), pending verification against the statute
last_updated: 2026-11-07
---

# Legal: AI UGC

**This is not legal advice.** It's a practical summary of where the law is heading on AI-generated people in ads, built from a practitioner breakdown of one law, not the statute text itself. The specific figures below — bill number, dates, penalties — are as reported by that source and should be confirmed against the actual statute and with the brand's own counsel before anyone relies on them. This area is also moving fast: New York is first, other states are expected to follow, so treat this as a live picture, not a settled one. When a brand is about to run AI creative at scale, the safe move is to verify current law in every market the ad will show.

## The principle that generalizes

Strip away the specifics and here's the durable rule, the one worth teaching a creative team now:

**If your ad shows an AI-generated human made to look like a real person, disclose it. If the AI made a product, a background, or a wide scene with no person in it, you don't.**

That line — people versus no people — is the whole distinction, and it's the part that will likely survive as more states write their own versions. A synthetic model holding your product needs a label. A product-only shot or an AI background with no human in it does not.

This doesn't ban AI creative and it isn't a reason to kill an AI pipeline. It asks for honesty about the synthetic human, which is four words in a corner, not a reason to throw out a productivity engine. The overcorrection — dropping AI entirely to avoid a label — costs far more than the label does.

## The first law: New York S.8420-A

New York became the first US state to require advertisers to disclose AI-generated people in ads. The details, as reported:

- **What it covers.** Disclosure of "synthetic performers" — AI-generated humans meant to look like real people in image *or* video creative. Both statics and video are in scope.
- **When.** In effect as of June 9, 2026. (The source framing was "days, not months" — that window has now passed, so for any brand running paid media in New York, this is a current obligation, not a future one.)
- **Why it matters beyond New York.** It's the first law of its kind in the US, and New York is openly positioning it as a template other states will copy. Build the habit now and you're ahead of the wave, not scrambling behind it.

## Who's in scope, and who's liable

- **It's about the audience, not the advertiser's address.** The law reaches any ad shown to people in New York, regardless of where the brand or agency sits. Based in Austin or London doesn't matter — if New Yorkers can see the ad, it's in scope.
- **It's channel-agnostic.** This is not a Meta thing. The same AI-model creative needs the disclosure everywhere it runs in New York — Meta, Google, YouTube, TikTok, programmatic, CTV. So compliance is a cross-channel audit of every live asset, not a single platform toggle.
- **The advertiser and agency carry it, not the platform.** Don't wait for a platform switch to handle this. The obligation sits on whoever creates the ad — the brand and its agency both. The compliance responsibility stops with the advertiser.
- **Penalties, as reported:** $1,000 for a first violation, $5,000 for each one after.

## What "conspicuous" means

The disclosure has to be conspicuous. The statute reportedly doesn't spell out exact wording or placement — but the safe read is to treat it the way influencer disclosures are judged: prominent and unavoidable. A tiny gray watermark tucked in a corner is asking for a fine. Make the label clear enough that a normal viewer would actually notice it.

## EU and Denmark: the AI Act's deepfake label (Article 50)

Added 7 Nov 2026 for the Danish market, read in the European Commission's Article 50 FAQ
(digital-strategy.ec.europa.eu, "Transparency obligations under Article 50 AI Act") and Regulation (EU) 2024/1689. This is the
rule that binds a Danish brand; the New York law below only matters for ads shown in New York. Not legal advice.

- **Since 2 August 2026, a deployer must disclose a deepfake.** The brand that publishes the ad is the deployer; the
  model maker is the provider. The disclosure has to reach the viewer "upon first exposure at the latest", be
  perceivable without tools (a visible or audible label), and the brand cannot lean on the invisible watermark the
  model put in the file. Content made before 2 Aug 2026 need not be relabelled; the grace period to 2 Dec 2026 is for
  providers' marking only, not for us
- **What a deepfake is** (art. 3(60)): AI-generated or manipulated image, audio or video that resembles real persons,
  objects, places or events and would falsely appear authentic. Three tests together: it resembles something, that
  thing exists or plausibly could, and it would pass as real. The audience's expectation counts: an obviously
  illustrated or animated world is not one; backgrounds and ordinary special effects are named as unlikely to be
- **For ads, read it as the people line above, widened:** a photorealistic AI person, an AI voice that sounds like a
  real speaker, a cloned voice, or a generated "real" scene with people in it gets a visible label in the asset
  ("AI-genereret" or "Lavet med AI", on screen from the first frame it appears, plus said or shown again if the ad is
  long). A product packshot, a generated background, kinetic type and an obvious cartoon (the `song-ads` look) do not
  trigger it; say so in the run notes rather than adding a label nobody needs
- **Evidently artistic, satirical or fictional work** gets a lighter duty: disclose "in an appropriate manner" that
  doesn't spoil the work (an end-card line or the caption). An ad is rarely "evidently fictional" if it shows a person
  who looks like a customer; don't use the exception to skip the label on a realistic AI person
- **The platform label is separate.** Meta and TikTok add their own AI tags (Meta's "AI info"). Those don't discharge
  the brand's art. 50 duty, and the brand's label doesn't replace the platform's switch. Do both; the platform side is
  checked in `ad-policy-check`
- **Fines** under the Act reach €15 million or 3 % of worldwide turnover, scaled for SMEs; enforcement is national
- **Danish consumer law already went further for ads.** A generated person speaking as a customer, an expert or a
  member of staff is misleading marketing (markedsføringsloven §§ 5-6) whatever the AI Act says; the factory's
  guardrails ban it (`static-ads`, `video-edits`, `song-ads`). The label never rescues a fake testimonial
- **Likeness of real people (Stated, check status):** Denmark has proposed amending the copyright act so a person
  controls realistic digital imitations of their face, voice and body, with exceptions for satire and parody (EU IP
  Helpdesk, 1 Jun 2026: expected in force 1 Jul 2026; not confirmed as passed when this was written). Until checked on
  ft.dk, treat any AI look-alike or sound-alike of a real, identifiable person as needing that person's written consent

## What this means when the assistant generates AI creative

When the assistant produces AI creative that includes a synthetic human meant to look real — an AI UGC creator, an AI spokesperson, an AI model holding the product — it should put the label into the asset itself (EU section above) and list it in the run notes, so the brand doesn't ship it unlabeled. When the AI output is product-only, a background, or a scene with no person, the requirement doesn't attach, and the assistant shouldn't invent one. The people-versus-no-people line is the trigger to watch for.

This is a flag to raise, not a legal judgment to make on the brand's behalf. Point to the obligation, note it's a moving and market-specific area, and let the brand and its counsel make the call.

## Source and limits

- **Source:** a practitioner thread summarizing New York S.8420-A, captured 2026-07-11. It's a secondary read of the law, not the statute, and not legal counsel.
- **Source, EU section:** the European Commission's Article 50 FAQ and Regulation (EU) 2024/1689, read 2026-11-07 (primary). The Danish likeness proposal: EU IP Helpdesk news, 2026-06-01 (secondary; status unconfirmed). Found while comparing the factory with the open-source `claude-ads` and `goose-skills` repos (MIT), whose compliance notes flagged the gap; no text taken from them.
- **Verify before relying:** confirm the bill number, effective date, penalty amounts, and disclosure specifics against the statute itself, and check whether other states have since passed comparable laws in the markets a brand runs in.
- **Scope:** the disclosure question for AI-generated people in the EU, Denmark and New York. Platforms' own AI labels are checked in the `ad-policy-check` skill. Right of publicity outside Denmark isn't covered yet.

## Related

- `ai-static-ad-generation.md`, `veo3-video-prompting.md`, `ai-animation-prompting.md` — where AI creative that may contain synthetic humans gets generated; the disclosure trigger lives at that step.
- `algospeak.md` — the sibling compliance layer: platform content policy and the guardrails that keep a brand's account alive.

This is everything I know about the legal side of AI UGC.

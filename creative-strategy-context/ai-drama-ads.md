---
summary: "AI drama ads: long-form scripted soap-opera stories (1-3 min) made entirely with AI characters, where the product is the plot's secret or reveal. What the format is, why it holds attention, story shapes, the product's role, cast and compliance rules, cutdowns, and when it fits a brand."
---

# AI drama ads

Ours. Built from a vendor walkthrough of an automated drama-ad pipeline (ScaleBot on YouTube, Oct 2026)
and the drama ads that brand accounts were scaling on Meta at the time. One vendor's demo plus what
was visible in the feed: **Stated, not tested here.** The first runs on a brand go in
`ai-ad-generation`'s feedback before any of this hardens into rules (CLAUDE.md, rule 6). The how-to
is `.claude/skills/ai-ad-generation/processes/video-ai-drama.md`; this doc is the what and the why.

## What the format is

A short scripted drama, usually 1-3 minutes, shot entirely with generated characters: a cast of
three or four, a setting that looks like a real home, restaurant or party, spoken dialogue between
the characters, and a plot with a betrayal, a rivalry or a secret. The product sits inside the plot
as the thing that explains the twist. It reads like a clip from a micro-drama app or a daytime soap,
not like an ad, until the product turns up as the answer.

To tag it in an account read: the container is the scripted multi-character story with dialogue
between characters (not to camera). It stacks with `Humour` when it is played for laughs, and it is
distinct from a creator skit, where one person plays every part to camera.

## Why it holds attention

- **Transport, not persuasion.** A viewer following a story stops arguing with it. The hook's job
  (`hook-psychology.md`: notice, qualify, intrigue, move, transport) is done by the plot's open
  question: did she really come? who is the new woman? why does she look like that?
- **The open loop pays for the length.** A 3-minute ad survives only if every beat raises or tightens
  a question the viewer wants answered. Long length is a cost, never a feature.
- **Recognisable feelings, invented people.** The audience recognises the emotion (being left,
  being compared, being underestimated) even though nobody on screen is real. The persona's emotional
  stakes come from `personas/personas-profile.md` and the trigger moments in voice-of-customer, not
  from the writer's idea of drama.
- **Cheap volume.** Once the cast and world exist, a new episode, a new ending or a new hook costs a
  few shots, not a shoot.

## Two inputs, kept apart

Every drama needs two separate inputs, and mixing them is the most common way the script goes wrong:

1. **The story idea.** Who the people are, what the betrayal or conflict is, where the reveal
   lands. This is the drama.
2. **What the viewer should come away knowing.** The one product belief the ad leaves behind,
   stated plainly ("the results look so natural nobody guesses her age"). This is the message.

The story carries the message; it never states it the way a voiceover would. When a character starts
listing benefits, the story has turned into an ad read.

## Story shapes that carry a product

- **The reveal by comparison.** Someone assumed the rival was younger, richer, luckier; the twist is
  that the difference is the product. The product is the secret.
- **The double take.** A character who left, doubted or dismissed the hero sees them later and
  can't look away. The product is the before-and-after, told through someone else's reaction.
- **The secret shared.** One character lets another in on what they use. The product changes hands
  as a favour, which is the most natural place for it to be named.
- **The underdog wins.** The hero is underestimated at the start and turns it round at the end,
  with the product as part of how.

The product belongs at the turn, not at the opening. Introduce it once the viewer wants the answer.

## The product's role

- **A prop with a plot job.** The product appears when the story needs it: in a hand, on a vanity,
  passed across a table. Use the brand's real product image as the reference so the pack is right.
- **Characters talk like people.** A character never says "the brand says", never reads a claim off
  a label and never repeats a benefit another character just said. One plain line about what it did
  for them beats three about what it contains.
- **Claims are still claims.** Anything a character says about results is an advertising claim in
  the brand's mouth. Every number traces to a source or is marked `[STAT NEEDED — verify before
  publishing]`; compliance walls apply to dialogue as they do to a headline.

## Cast

- **Three or four speaking characters** is the sweet spot: the hero, the antagonist or rival, a
  confidant who lets the audience hear what the hero thinks, and optionally one more for the reveal.
- **Cast from the persona.** The hero is the brand's buyer, with age, setting and style taken from
  the persona, not a stock face.
- **Make them easy to tell apart.** Distinct hair, build and a fixed wardrobe colour per character
  ("the woman in the red dress"). The colour doubles as the handle for fixing frames later.
- **Every character is invented.** Never a real person's likeness, never presented as a customer.

## Length and cutdowns

- **The long cut** (1-3 min) is the story in full and runs where viewers watch long video.
- **Cutdowns** (30-60 s) keep the setup, the turn and the reveal, and drop the middle. Plan them in
  the shot list from the start by marking which shots are must-keep.
- **Hooks are swappable.** The opening line or the first beat can be regenerated as variants without
  touching the rest, so test hooks before testing new stories.

## Compliance

- **AI disclosure.** Every character is synthetic, so `legal-ai-ugc.md` applies in full: label the
  creative as AI-made, conspicuously. Check Meta's current AI-content labelling at the time of
  launch.
- **Fiction, not testimony.** A character's story is a dramatisation, never a customer review.
  No "real results" framing, no on-screen text that presents a character as a real customer, and no
  before-and-after claims beyond what the brand can prove.
- **Danish market.** Hidden advertising and misleading testimonials under markedsføringsloven apply:
  the ad must be recognisable as an ad, at least by the end, and the drama must not pose as a real
  customer's experience. Health and beauty claims follow the brand's compliance file.

## When it fits, when it doesn't

Fits when the product changes how someone looks, feels or is seen by others (skincare, hair, fitness,
fashion, confidence products), when the brand's buyer lives a recognisable social story, and when the
account already gets long watch time on video.

Doesn't fit when the product needs a demo to be understood, when the brand's voice can't carry
melodrama (premium-restrained brands: see `advertising-luxury-and-higher-price-points.md`), or when
the account has no test budget for a 1-3 minute production. A brand outside the obvious categories
can still use it played for laughs, with smaller stakes (a rivalry in a club, a friendly wager)
instead of a betrayal.

## Related

- `.claude/skills/ai-ad-generation/processes/video-ai-drama.md`: the production method
- `production.md`: paying for generation, an AI person who stays the same, generated video clips
- `scriptwriting.md`, `emotional-delivery-and-timing.md`, `spoken-script-voice.md`: the writing
- `legal-ai-ugc.md`: disclosure for synthetic people

# Process: video breakdown

A deep read of one video ad, part by part. Adapted from a practitioner's breakdown prompts (Nov 2026), rewritten and
regrouped; the "make your own version" part is left out on purpose, because `recreate` and `iterations` own that.

Write into `../breakdown-template.md`. Every section gets a label (Verified, Inferred, Data-limited). Quote speech and
on-screen text verbatim with the timestamp (`0:07`). Describe visuals plainly. A section the ad doesn't touch says
"Not in this ad", which is a finding too.

## Before you start

- The strategist's read is in the header, or "No hypothesis given" (`../SKILL.md`, step 2). Don't read it again until
  Part J: the breakdown should be your own read
- You have the video itself, the transcript with word timestamps, and small frames (one a second is plenty; one every
  half second for the first 3 seconds)
- For our ad: the numbers block in the header is filled and labelled. For a competitor ad it says "Not our ad: no
  performance data"
- Terms mean what `brain-system/creative-strategy-context/creative-vocabulary.md` says. Note: UMP there is the
  mechanism of the *problem* (the root cause), UMS the mechanism of the *solution*. What some prompts call a "unique
  mechanism of proof" is called **proof of mechanism** here

## Part A. Transcript and inventory

**A1. Full transcript.** Every spoken line with its timestamp, and every on-screen text with the second it appears and
leaves, in one timeline. Mark who speaks (creator, expert, customer, founder, voiceover, song, skit character, AI).
Note length, aspect ratio, and whether captions are burned in. What you couldn't hear or read is Data-limited

## Part B. Hook and opening

**B1. Hook, three layers.** Write each separately, with its timestamp:
- the spoken hook (the first line said)
- the visual hook (what the first frame and first second show)
- the on-screen text hook (the first words on screen)

For each: which awareness level it talks to, and does it work with the sound off? Name the hook family
(`callout`, `story`, `show`, `claim`, `question`, `secret`; defined in `winning-script-patterns.md`). Do the three
layers say the same thing, or does each add something?

**B2. Visual elements.** The opening visuals, the B-roll and what each piece proves, overlays and graphics, the colours
that carry the frame, transitions and cutting pace (cuts per 10 seconds early vs late), any demo, and each pattern
interrupt with its timestamp (a zoom, a sound, a prop, a change of place)

**B3. The lead.** How the hook hands over to the body. The line or cut that does it, and what promise the viewer is
carried on. Where would a viewer drop if the lead were weak?

## Part C. Audience and awareness

**C1. Awareness level.** Where the viewer starts (unaware, problem aware, solution aware, product aware, most aware),
and the line that shows it. Does the ad move them up, and where?

**C2. Sophistication.** How many similar claims the category has heard (S1-S5), and how the ad gets around them: a new
mechanism, a sharper proof, an identity, a new enemy, or nothing. Quote the line that does it

**C3. Who it's for.** The demographic the ad shows and implies (age, life stage, situation), read from people, places,
words and problems on screen. Then the closest persona in `personas/personas-profile.md`, and why. Mark Inferred

**C4. Trigger events.** The moment in the viewer's life the ad speaks into (a wedding, a new baby, a bad night, a
holiday), stated or implied

**C5. Behaviours targeted.** What the viewer does now that the ad names or shows (scrolls reviews, buys the cheap one,
skips the routine)

**C6. Past attempts.** The fixes and products the viewer has already tried, as the ad names them, and how it treats
them (blamed, dismissed, respected)

## Part D. Story and structure

**D1. Story structure.** Setup, conflict, resolution, with timestamps. Whose story is it, and what is at stake?

**D2. Big idea.** The one idea the whole ad hangs on, in one sentence. If it takes a paragraph, there isn't one

**D3. Product timing.** The second the product or brand is first named or shown, as a share of runtime (that is
`product_at`). Why there? What did the ad have to do before it could name the product? Compare with the timing
pattern in `winning-script-patterns.md`

## Part E. Desire and emotion

**E1. Main desire.** The one core want it speaks to, in the customer's words where you can quote them

**E2. Secondary desires.** The other motivations stacked on top (status, saving time, being a good parent)

**E3. Life Force 8.** Which of the eight it pulls (list: `creative-vocabulary.md`, "LF8"), the primary one and at most
one secondary. Quote the line or point to the frame

**E4. Emotional valence and intensity.**
- Dominant charge: positive (moving toward something) or negative (moving away from something)
- Valence map: how the charge shifts across the ad, with timestamps (negative in the problem, positive in the vision)
- Peak intensity 1-10, with the line or frame that is the peak
- Intensity arc: the level at the hook, in the body, at the close, with timestamps
- Calibration (`creative-vocabulary.md`, "Emotional valence and intensity"): is this level right for this viewer's
  awareness and sophistication? Say whether the ad over-agitates (feels like a pitch, loses trust) or under-agitates
  (no reason to act now), and the evidence

**E5. Emotions targeted.** Write them as the viewer would feel them: "I feel...", "I'm tired of...", "Finally..."

## Part F. Belief and mechanism

**F1. Belief transfer.** The beliefs the viewer must hold before buying, in order, and how the ad moves each one
(a demo, a story, a number, a reframe, an authority). Mark the belief the ad works hardest on

**F2. Objections.** Every objection the ad answers, where, and the technique: pre-empting it, a demo, a quote, a
guarantee, a reframe, humour. Name the obvious objection it leaves open

**F3. Competitive disqualification.** How the ad rules out the alternatives: the old fix, the cheap copy, doing
nothing. Is the enemy specific ("most oat milks aren't clean") or vague ("bad ingredients")? That is `enemy`

**F4. Mechanism.** Three things, kept apart:
- USP: a feature or claim the product has (made in Denmark, 30 days' supply)
- UMP: the root cause of the problem as the ad explains it, and why past fixes failed
- UMS: how the product fixes that exact cause
Is there one mechanism said simply, with a "because"? Then `mechanism: yes`. A list of features is not a mechanism

**F5. Proof of mechanism.** What makes the mechanism believable: a demo, a study, an expert, a before and after, a
timeline ("Week 1... Week 2..."), a personal result, a number. Map it to `proof`

**F6. New, Easy, Safe, Big.** How the ad makes the offer feel new, easy to do, low risk, and worth it. Quote each one.
Name the missing one

**F7. Benefit stacking.** The benefits in the order they come, and how each builds on the last. Where does it stop
adding and start listing?

## Part G. Offer and CTA

**G1. CTA.** The action asked for, the words, the timestamp. Urgency (real or none), the friction it removes
(free returns, guarantee, "takes two minutes"), and the offer if there is one. Map it to `close`. Does the script
carry the offer, or does it sit at the end?

## Part H. Craft and native fit

**H1. Engagement maintenance.** How it keeps people watching: pacing, open loops, pattern interrupts, a question held
back, visual change. Mark the stretch where attention most likely drops, and why

**H2. Conversational language.** Slang, fragments, rhetorical questions, contractions, first person, deliberate
imperfection (a restart, a laugh, "okay so"). Quote two or three. Does it sound spoken or written? (What spoken
sounds like: `brain-system/creative-strategy-context/spoken-script-voice.md`)

**H3. Native integration.** Would a fast scroller take it for a post? Styling, editing, the opening frame, length,
platform features used (captions, stickers, a stitch, a reply to a comment), and the red flags it avoids or shows
(studio light, logo first, a price card up front)

**H4. Positioning.** Friend or convert (someone like me who found the answer), authority (someone who knows), or a
hybrid. Name the evidence: what they say, wear, where they stand, how they talk. That and the speaker give `voice`

## Part I. Formula

**I1. The ad formula.** The full sequence with timestamps, as one line, for example:
`Hook (0:00) -> Problem agitation (0:04) -> Personal story (0:11) -> Solution intro (0:22) -> Mechanism (0:27) ->
Social proof (0:38) -> Benefit stack (0:45) -> CTA (0:55)`.
Then the five-shape read: which shape it is (`symptom`, `enemy`, `story`, `objection`, `authority`, `offer`, `other`,
see `winning-script-patterns.md`), and the ladder step it opens on (`awareness-script-ladder.md`)

## Part J. Close the breakdown

**J1. What the numbers say about the parts** (our ad only). Tie each number to the part it reads: hook rate to Part B,
hold rate and average watch time to Parts D and H, CTR to Part G, CPA and ROAS to the whole. Compare with the account
benchmark for the same period, not a generic one. Every link is Inferred. If the numbers can't carry a read (low
spend, tracking in doubt), say so and stop the link there

**J2. Why it worked, in five lines.** Five short lines a strategist could brief from. Each cites a part. For a
competitor ad: "why it is probably still running", Inferred

**J3. Tag block and pattern check.** Fill both from `../breakdown-template.md`

**J4. Your read vs the breakdown.** Now read the strategist's answers again and write the comparison (`../SKILL.md`,
step 8)

## Light pass (for batch-winners)

A1, B1, D3, F3, F4, I1, the tag block and J2 only. Mark the file "Light pass" in the header.

---
summary: "The written AI-slop signs — vocabulary, rhetoric, and formatting tells that mark generated copy — and the lint-then-judge review every creative deliverable passes before it ships."
status: pending the strategist's review [~]
purpose: The doctrine of written AI tells across every creative deliverable — headlines, hooks, overlay and static copy, ad-prompt spoken lines, iteration copy, and the written surface of scripts. The spoken twin is spoken-script-voice.md; this doc covers what shows up on the page.
source: "Generalized from Wikipedia: Signs of AI writing (en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), retrieved 2026-07-03. The sign inventory is stated by that source and adapted here for marketing creative; the WRONG/RIGHT contrasts are the assistant's application of it."
---

# AI Writing Tells

## Why this document exists

The strategy layer makes the ideas sound. The brand vault, the personas, the customer language, the method docs — when those are loaded, the *thinking* behind a script or a headline is right. The remaining failure is the execution layer: copy that carries a sound idea in a voice no human uses. Readers can't always name why a line feels generated, but they feel it, and the feeling costs trust and performance.

The tells are not mysterious. They are a finite, named inventory — catalogued publicly by the editors who screen thousands of AI-written submissions — and most of them are mechanically detectable. This doc is that inventory, adapted for marketing creative, plus the discipline for applying it without false positives.

**Scope: creative deliverables only.** This doctrine applies to scripts, headlines, hooks, overlay and static copy, the spoken lines inside AI-generation prompts, and iteration copy — the words a customer will read or hear. It is never applied to context docs, prompts, system docs, or analysis. Those are internal working surfaces with their own standards, and running the tells check against them is a known over-application.

**Relationship to `spoken-script-voice.md`.** That doc is canonical for the spoken register — how winning scripts sound out loud, the twelve spoken tells, the read-aloud test, the brand voice-profile method. This doc is canonical for the *written* signs: the vocabulary, rhetoric, and formatting patterns that mark generated text whether or not it will be spoken. Scripts pass both. Headlines, statics, and overlays pass this one plus the voice-profile check. Where the two docs name the same tell — the em-dash cadence, the balanced triplet, the "not just X" frame — the spoken doc carries the deeper treatment for scripts and this doc carries the pattern for everything else.

## How the check runs: lint, then judge

The check is two layers, in order, and the order matters.

**Layer 1 — the mechanical scan.** Run `scripts/voice-lint.py` on the draft. It detects the pattern-shaped tells below deterministically: flagged-word hits, the named constructions, dash cadence, balanced triplets, weasel attributions. It reports per line with a density score. The linter cannot be argued with, which is the point — it exists so no draft ships because the writer talked itself into "this one's fine."

**Layer 2 — the judgment pass.** A reviewer who did not write the draft reads the linter output plus the draft against the brand's voice profile and decides three things: which mechanical flags are real (a customer verbatim containing a flagged word stays — see the false-positive discipline below), what the linter can't see (register drift, too-clean grammar, sameness of rhythm, brand-fingerprint mismatch), and the line-level rewrite for every real flag. The reviewer rewrites lines, never strategy: the hook format, the framework beats, the claims, and the sourced customer language are load-bearing and stay.

A flag is fixed by rewriting the line in the brand's register — pulled from the voice profile and the winning corpus — not by thesaurus-swapping the flagged word for its nearest synonym. Swapping "elevate" for "enhance" trades one tell for another. The fix is to say the plain thing the way the brand's real winners say it.

## The sign families

### 1. AI vocabulary

Certain words appear in generated text at many times their human rate. The tier list drifts as models retrain — early lists led with "delve" and "tapestry," later ones with "showcase," "foster," "elevate," "seamless" — so the signal is **density, not any single hit**. One "unlock" is a word; three flagged words in four lines is a fingerprint.

The working list lives in `scripts/voice-lint.py` so it stays maintained in one place. The families: importance-inflators ("pivotal," "crucial," "testament"), texture words ("vibrant," "meticulous," "intricate," "seamless"), transformation verbs ("elevate," "unlock," "empower," "transform," "revolutionize"), and brochure adjectives ("renowned," "unparalleled," "groundbreaking").

- WRONG (AI): "Unlock effortless comfort with our meticulously crafted denim."
- RIGHT: "These are the first jeans I haven't thought about all day."

### 2. Inflated significance

Generated copy can't say a plain thing plainly. Everything "stands as," "serves as a testament," "plays a vital role," "marks a turning point" in an "evolving landscape." In creative, this reads as the brand grading its own homework.

- WRONG (AI): "This fabric represents a breakthrough in everyday comfort."
- RIGHT: "The fabric stretches four ways. That's it. That's the trick."

### 3. Negative parallelism and the balanced triad

"It's not just X, it's Y." "Not only… but also." "No X, no Y, just Z." And the smooth rule-of-three: "style, comfort, and durability." These are the most recognizable constructions in the inventory because models reach for them as sentence-level default rhythm. Real people use contrast and lists too — the tell is the *balance*, three items of matching weight, the elevation frame doing the work the claim should do. The spoken doc's treatment (Tells 2 and 3) governs scripts; the pattern is banned in headlines and statics the same way.

- WRONG (AI): "It's not just a jacket — it's confidence, comfort, and craftsmanship."
- RIGHT: "It's a jacket. It just fits like someone measured you first."

### 4. Copula avoidance and participle tails

Generated text dodges "is" and "has": products "feature," "offer," "boast," "provide a range of." And sentences trail into an unattributed "-ing" synthesis: "…, highlighting the brand's commitment to quality," "…, ensuring all-day comfort." The tail asserts a conclusion nobody stated and no source supports — it is inference laundered into the sentence's slipstream.

- WRONG (AI): "The waistband features soft-brushed elastic, ensuring comfort from morning to night."
- RIGHT: "The waistband is brushed elastic. It doesn't dig in. I've had it on since 7am."

### 5. Vague attribution

"Experts agree." "Studies show." "Customers rave." Weasel attribution with no named source. This one is already covered by the attribution rules everywhere else in the system — in creative it is doubly banned because it is both a tell and a compliance risk. A claim either carries its real source or it isn't made.

- WRONG (AI): "Dermatologists agree that consistency is key."
- RIGHT: "My dermatologist told me to stop switching products every two weeks. So I did."

### 6. Puffery register

"Commitment to excellence." "Rich heritage." "Nestled in the heart of." "A diverse array." Brochure language nobody says out loud. The brand's real winners almost never contain it — which makes it a banned-by-absence class across virtually every voice profile, even before the profile is built.

### 7. Formatting tells

The em-dash cadence — clauses stacked on dashes for theatrical breath — is the most famous one, and it compounds: one dash is punctuation, a draft full of paired dashes is a fingerprint. Also in this family: bold-key-term mechanics, bullet lists where a sentence belongs, curly and straight quotes mixed in one piece, headline-case applied where the brand's corpus doesn't use it, and the "Conclusion"-shaped ending that summarizes what the reader just read. Formatting is register: match the brand's corpus, not the model's defaults.

### 8. Signposted transitions and the question you're not actually asking

"But here's the thing." "The best part?" "Say goodbye to X, say hello to Y." "That's where [product] comes in." Formulaic bridges that real speech never uses twice. The spoken corpus contains "but here's the thing" zero times.

The question form deserves its own name because it is one of the biggest tells: the rhetorical self-question the speaker immediately answers — "Honestly?" "Sound familiar?" "Crazy, right?" "The result?" — in copy or in dialogue. Humans don't interview themselves mid-thought; they connect the clauses and keep going. The one exception is a question hook: an opener deliberately built as a real question to the viewer. Anywhere else, the question mark is aimed at no one and reads as generated.

### 9. Sycophancy and throat-clearing

Openers that praise the premise or restate the brief before saying anything: "Great question," "In today's fast-paced world," "When it comes to comfort." The first line of any creative deliverable is the most expensive real estate it has; a throat-clear spends it on nothing. Related: the "whether you're a busy mom or a weekend athlete" audience-enumeration, which names everyone and lands with no one. And the **manufactured-intimacy opener** — "Okay, can I be real for a second?" "Can I be honest with you?" "Let me be real." "Real talk." — performed vulnerability that asks permission to be authentic instead of just being it. It shows up on AI-written hooks constantly; a real person opens on the confession, not the request to make one. (Spoken treatment: Tell 13 in `spoken-script-voice.md`.)

### 10. Elegant variation

Synonym-cycling to avoid repeating a word real speech would just repeat: "the jeans… the denim… the garment… the piece." Repetition is how the human voice underlines. The variation is the tell.

### 11. Flat rhythm (staccato) and its mirror

Every sentence the same length. The usual form is a run of short declaratives ("It works. It's fast. You'll love it.") that reads as a machine imitating confidence; the mirror is a block of long sentences with no place to land. Human prose varies, and the default for body text (letters, posts, emails, descriptions, long-form copy) is **two long sentences, then one short one**: long is roughly 15 to 30 words and carries a reason, a detail or a number, short is 2 to 7 words and lands the point. Never three short sentences in a row, never four long ones.

Scope: body text only. Hooks, headlines, overlay text, lists, citations and spoken lines in a script are exempt, because copy for the eye or the ear is allowed to be clipped. A brand's or person's voice profile may set its own ratio and wins over this default. It is a rhythm check, not a word counter: one clipped run is noise, a whole page of it is the tell. The deterministic scan of this is not in `voice-lint.py` yet; until it is, the judgment pass and the read-aloud test carry it.

### 12. The tells that moved around the dash

Once the em dash became the famous tell, models used it less and the signs moved into the words around it. These come from one practitioner's public post (4 Nov 2026, a list he keeps for his own writing bots; *Stated*, no counts) and are scanned in `voice-lint.py` under the names in brackets. Like every family here, they are flags to judge, not bans.

- **The drama adverb** [AI vocabulary: "quietly"]. "Claude quietly shipped the best feature of the year." Delete it; if it shipped, it shipped.
- **Plain contrast** [plain contrast]. "It's not a chatbot, it's a coworker." The cousin of family 3 without the "just". Say what it does: "It answers my client emails."
- **The fake deadline** [fake deadline]. "Set this up before Monday." Say how long it takes. A real offer deadline in an ad is a different thing, and under the Danish price rules it has to be true.
- **Talking to a crowd** [crowd address]. "Most people use Claude wrong." Talk to the one person reading and say what you do instead.
- **The upgrade simile** [like-a-pro upgrade]. "Research like a $150/hour analyst." Show what it researched and let the reader judge the price.
- **The line that sounds deep** [fake-deep line]. "That's the whole game." "Setup is the part everyone skips." It repeats the sentence before it. Cut it.
- **Three of everything up top** [fragment triplet]. "Write. Edit. Ship." The one-word-sentence form of the balanced triad. Keep the one reason you believe.
- **Adjectives in a pile.** "A powerful, seamless, game-changing workflow." The lint only sees the flagged words in it; the judgment pass catches the pile. Name the thing.
- **Sirens and arrows** [sirens and arrows]. An alarm emoji, BREAKING in capitals, an arrow pointing at the link. Write the news as a normal sentence.

The fix is the one at the top of this doc: say the actual thing. A synonym for a flagged word is a new tell.

### 13. Leftovers, asides and post formulas

Added 7 Nov 2026 after FeedHive's open-source `ai-slop-detector` (MIT; 120 patterns in nine families, compared with this
doc line by line; credits in `brain-system/third-party/open-source-skills/MANIFEST.md`). Most of its list was already here.
These were not, and are scanned in `voice-lint.py` under the names in brackets, with Danish twins marked "(da)":

- **Chatbot residue** [chatbot residue]. "Certainly!", "Here is a punchier version:", "Would you like me to…" left in
  the deliverable. Delete it
- **Gap markers and citation debris** [placeholder or citation debris]. "[Your Brand]", "XX%", "[3]", "oaicite". Our own
  "[NUMBER MISSING]" and "[STAT NEEDED]" are flagged on purpose: they mark a gap a person must fill before anything ships
- **Telling the reader how to read it** [interpretive aside]. "That last point matters more than it sounds", "Read that
  again", "Let that sink in". Show why, or cut it
- **Correcting yourself for effect** [rhetorical self-correction]. "It's fast. Or rather, instant." Say the second thing
- **Performed spontaneity** [fake-unscripted scaffolding]. "And honestly…", "So yeah…" at the start of a line. In a
  script a real creator may say it; the judgment pass decides, because it's only a tell when it's written in
- **Two hedges on one claim** [hedge stacking]. "May potentially help." Give the evidence or cut the claim
- **"Imagine a world where"** and **"What if I told you"** [imagine-a-world opener]. Describe what it does today
- **Post formulas** [engagement bait]. "Thrilled to announce", "Agree?", "That's it. That's the post.", "the ultimate
  guide". Mostly organic and LinkedIn, but they leak into ad copy
- **Things that live somewhere** [lives-and-sits metaphor]. "Where your data lives." Say where it is stored or shown

Two checks from the same list stay with the judgment pass, because no regex can see them:
- **The portability test.** Could the sentence move unchanged to a rival brand's ad? Then it says nothing about this
  product. Rewrite with the detail only this brand has
- **Made-up specifics.** An invented name, number or example presented as real ("Sarah saved 10 hours a week") is a
  fabrication before it is a tell, and the grounding review bounces it

## Danish copy

Everything above is the English inventory. Danish copy carries most of the same tells, translated, plus a few of its own. The Danish list below is factory-written and a **judgment from observation, not a counted corpus**; treat it as a starting point and prune it when a run shows a false positive. `scripts/voice-lint.py` scans for it and marks the hits "(da)". The same density rule holds: one hit is a word, a cluster is a fingerprint.

**Translated tells.** The English constructions carried straight over:
- "Det er ikke bare et X, det er et Y", "ikke kun… men også", "mere end bare"
- "Her er sagen", "men her er det interessante", "sig farvel til X", "det er her X kommer ind"
- The self-question: "Og resultatet?", "Sandheden?", "Lyder det bekendt?"
- Throat-clearing: "I dagens hurtige verden", "når det kommer til", "forestil dig"
- Puffery and calques: "spiller en afgørende rolle", "til næste niveau", "frigør dit fulde potentiale", "dykke ned i", "sømløs", "banebrydende"
- "Hvilket understreger…" as the participle tail; "studier viser" and "eksperter er enige" with no source

**The contrast tack-on.** "Træk historien ud. Ikke ordene." and "Ikke X. Men Y." are the Danish form of negative parallelism, and in practice the one a Danish strategist hears first. Say what the thing is and drop the thing it is not.

**English punctuation.** A comma before "og" in a list ("blå, grønne, og røde") is English; Danish does not use it. Ignore the flag when "og" starts a new main clause. Matching-weight triplets ("blød, behagelig og holdbar") are the same tell as in English.

**Written for the eye.** Danish drafts tend to be too complete: every sentence a full main clause, no dropped subjects, no "altså", "så", "jo". Spoken Danish is looser. The lint cannot see this; the judgment pass and the read-aloud test can.

**Personal choices are not tells.** Whether a person uses an English loanword or the Danish word for the same thing, keeps a connecting "så" in a conditional, or likes a blunt joke, is a voice-profile decision for that person, not a universal flag. Record it in their profile, never here.

## The false-positive discipline

This section is load-bearing. The source inventory itself carries the caveat, and it survives the adaptation:

- **One flagged word is not a verdict. Clustering is.** The linter reports density for a reason. A single "unlock" in an otherwise human draft is noise; judge the pattern.
- **Customer verbatims are exempt — register-aware.** If a real customer said "this seriously transformed my mornings," the verbatim's *language* ships untouched, flagged word and all. Real language beats the list, always. The reviewer's job is to check the *source*, not to sand the quote. In **written deliverables** the whole verbatim ships as-is. In **spoken deliverables** the exemption covers the customer's vocabulary, not their typed cadence: a written review pasted into a script as a spoken line is itself a tell, and the fix is voicing it — same words, re-cadenced for the mouth — per the written-vs-spoken rule in `spoken-script-voice.md`.
- **The brand's corpus outranks the inventory.** If a brand's winning ads genuinely use a pattern on this list, the voice profile records that and the profile wins. The list describes model defaults, not universal bans.
- **Humans increasingly write like models.** The tells are drifting into human speech, which is exactly why the check is density-and-pattern, never gotcha-on-a-word.
- **Clean-but-generic is the residual failure.** Stripping every tell from a draft written without brand context produces copy that offends no one and sounds like no one. The tells check removes the AI surface; only the voice profile and real customer language supply a voice. If a draft passes the lint and still sounds like anybody, the problem is upstream — a thin voice profile — and the fix is more corpus, not more scrubbing. The voice reviewer says so with a `needs-corpus` verdict, which ends the gate and names the missing corpus instead of flagging the same lines forever.

## When this doc gets refreshed

The vocabulary tiers and pattern list drift with model generations — the source inventory is versioned by era for exactly this reason. When a new tell family shows up in the wild (in reviewed drafts, in the source article's updates, or in expert signals), it lands here and in `scripts/voice-lint.py` in the same pass, and the doc map regenerates.

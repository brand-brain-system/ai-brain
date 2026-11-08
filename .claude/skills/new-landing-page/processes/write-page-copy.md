# Process: write and check the copy (step 3)

Goal: `page.json` filled section by section for the brand, to the template's contract, then checked and gated as one page before the reviewer sees it.

## Before writing

1. **Three things open:** the template card, the primary reference's screenshot and breakdown, and `brief.md`. Do not write from the contract alone; look at how the reference does each section.
2. **Name the read in two sentences,** at the top of `copy/notes.md`: who lands on this page and in what state (the buying phase from `brain-system/creative-strategy-context/emotional-delivery-and-timing.md`: a Trigger reader needs her problem mirrored; an Evaluation reader needs one hesitation named and resolved, not more information), and the one promise the page makes her (the angle, or the named ad's promise when there is one). Every section is written for that person and that promise.

## Customer voice first (Alex, 2026-10-01)

The page should sound like the people who buy, because it is mostly their words. Before writing a section, find the phrases in `brief.json` `voc.bank` that do its job, and build the line from them: lift a short phrase as written, or keep the customer's key words and order and trim. Write a line from scratch only where no customer phrase can do the job, and say so in the trace.

- **Where it matters most:** the hero subhead and bullets, every reason title and lead line, the FAQ questions (asked the way buyers ask them in ad comments), the "who it's for" lines, and the button labels where a customer phrase fits.
- **Trace every one.** Each section in `page.json` gets a `voc` list (on the section, beside `fields`, not inside it): `{"line": "<field path, e.g. items[3].title>", "from": "<the verbatim phrase>", "source": "<review Name date | ad comment date | survey | reddit>"}`. Lines written without a phrase get `"from": null` with a one-word reason ("spec", "offer", "legal"). `lp-copy.py check` reports the share of key lines traced, and the approval table shows each section's customer words beside the copy.
- **Quotes stay quotes.** A phrase built into a headline is not presented as a quote. Anything inside quote marks or attributed to a person is a full verbatim from `claims.reviews`.
- **Watch the echo.** A phrase that traces back to the brand's own ad copy ("feels like sweatpants") is the brand talking to itself; prefer the customer's own image.

## Per section, in template order

3. **Write to the job.** Each section in `page.json` carries its `job` and `guide` (word budgets, item counts). Fill its `fields`. Rules by kind of content:
   - **Hero:** the headline states the page's promise (`brief.json` `angle`) in the customer's words where they do the job. When an ad is named, it repeats the ad's promise in the ad's own words and voice (`ad.hook`, `ad.angle`) and shows the ad's offer.
   - **Numbers:** the allowlist only. The offer is `[OFFER]` until stated. A proof number the brief lacks is `[STAT NEEDED: verify before publishing]`.
   - **Reviews:** `claims.reviews` verbatim, with the name and detail on record. Pick the review from someone closest to the page's buyer (the named ad's person, if any). Never shorten; pick a different real quote if one is too long.
   - **Quiz steps and FAQ:** from `story.objections` and `voc`, in the buyer's words. Quiz answer options are real objections and goals, not invented segments.
   - **Comparison rows and rounds:** only `claims.rivals` facts, sourced and dated. Concede what is true of the rival.
   - **Founder, expert and author sections:** only the people and the story on record. No invented bylines.
   - **Buttons:** short, a different verb where the template repeats them, all to the one link.
   - **Everything else:** the brand's register (`voice_rules.register`), plain words, claims inside `health_wording` and `positioning_rails`. For audiences 45 and up: clarity over cleverness, say what it does and whether it works.
4. **Photos:** set each image to `{"src": "assets/<file>", "alt": "..."}` for a photo the brand has, or `{"placeholder": "what the photo should show"}`. Never describe the product's look in copy to stand in for a photo.
5. **Optional sections:** fill the ones the brand can fill honestly; delete the others from `page.json` (do not leave empty shells). Required sections stay; if one cannot be filled, use the card's adaptation and note it for the copy table.
6. **Page details:** `meta.title` (brand and page name) and `meta.cta_url` if it differs from the brief's.

## Then, once for the page

7. **Collect and check.**
   ```bash
   python3 <skill>/scripts/lp-copy.py collect <run>
   python3 <skill>/scripts/lp-copy.py check <run>
   ```
   The check fails on a number off the allowlist, a review that is not verbatim, a kill-list pattern, a missing required section, or sections out of template order. Fix `page.json` and re-run until it passes. Its notes (open placeholders, empty fields) go on the handoff list.

8. **Judge pass, yourself,** against the read from step 2 and the customer voice: could a key line have used a customer's words and did not; is the trace honest; does the hero state the angle (and match the ad, if one is named); does each section do its job and only its job; could a line be cut with nothing lost; does the page name the reader's hesitation rather than adding pressure; is there one idea per section. Fix or cut.

9. **Grounding gate.** Spawn `context-grounding-review` (the factory's `.claude/agents/`) as a general-purpose subagent with the prompt in `references/agent-briefs/review-gates.md`. Bounced: fix, re-run until grounded.

10. **Voice gate.** Spawn `creative-voice-review` the same way, in parallel with grounding, on `copy/all-copy.md`, deliverable type "landing page copy". It runs `voice-lint.py`. Rewrite flagged lines within the same word budget; re-run until ships.

11. **Record** both verdicts and the lint density before and after in `copy/notes.md`; they go into the run README at the end.

## Never

- Carry a sentence, a headline, a number, a name or an image over from the reference page. Structure only.
- Bloat. If the guide says 4 to 10 words, the line has 4 to 10 words.
- Add a section, badge, star row, counter or disclaimer the template does not have.
- Substitute a lookalike for missing proof (an unnamed "as seen in", a rounded-up count, a composite review).
- Run the gates on a sample. The whole page's copy goes through both.

## Lessons

- **Never name a field `cards` (2026-10-01, Winks lp-02 run).** `lp-copy.py` skips any key called `cards`, so card copy under that name is never collected into `copy/all-copy.md`, never number-checked and never seen by either gate. Use `tiles` (or any other name) for a section's card list.

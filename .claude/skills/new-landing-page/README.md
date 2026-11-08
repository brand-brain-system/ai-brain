# New Landing Page: how to use it

Turns a brand and an angle (plus an ad when one is named) into one finished landing page by recreating a page structure that big accounts put real spend behind. You pick the template from the swipe file, approve the copy in chat, give feedback on a draft, and get a final page with a handoff list. Built by Alex Cooper, 2026-09-30, for Parker course session 6, on the same production line as Offer Statics and the Static Ad Engine.

`SKILL.md` is the full workflow Claude follows. This page is the short version for people running it.

## Run it

1. Open the swipe file (`swipe-file/index.html`), find the page you want to make, and press **Build this one**. It copies a line like `LANDING PAGE TEMPLATE: lp-01 Reasons-why listicle (reference: tpj-1, The Perfect Jean)`.
2. In Claude Code, say **"landing page for <brand>"** and paste that line.
3. Answer the one intake message (the offer, the button link, anything the brand may not say; the angle only if you want a different one from the one proposed).

## The nine steps

| | Step | You get | You do |
|---|---|---|---|
| **A. Plan the page** | 1. Pick the template | The five templates, if you have not picked | Pick one (the swipe page's line, a name, or "like the Grüns one") |
| | 2. Research the brand | One message with the questions only you can answer | Answer them |
| | 3. Write and check the copy | Nothing yet: the copy is checked for true numbers, real quotes and human-sounding lines | Nothing |
| | 4. **You approve the copy** | **Copy table in chat**, one row per section: what that section does on the reference page beside the brand's copy | Reply `approved`, or edits like `S03 headline: "old" -> "new"`, or `cut S07` |
| **B. Make the page** | 5. Build the page | Nothing yet: the page is rebuilt to look like the reference page you picked, in the brand's colours, with real photos and only the approved words | Nothing (say yes or no if it asks to generate a missing photo) |
| | 6. Check the build | Nothing yet: desktop and phone screenshots are compared to the reference, then the actual page is tested in a browser for links, forms, overflow, interactions and console errors | Nothing |
| | 7. **The draft page** | An HTML file of the landing page, sent in chat; a temporary shareable review URL only when you ask for one | Open it in a browser; reply with notes by section ("S03: ...") or "approved" |
| **C. Finish** | 8. Revise | A new HTML file, one line per change | Reply with more notes; repeat until it is right |
| | 9. Final page | The final HTML file, a phone screenshot, passing browser-QA report, and the handoff list | Hand it to whoever puts it live |

Two gates are yours: the copy (step 4) and the draft (step 7). Nothing is built before the first; nothing is called final before the second.

## What you need first

- **The brand's brain**, or a paste of what it sells, its prices, its offer and what it may claim.
- **The angle**: what the page sells and to whom. Optional: if you leave it out, Parker proposes one from the brand's evidence.
- **An ad (optional)**: if the page is for a specific ad, give the Parker link and the headline will repeat what the ad promised. Never required.
- **Product photos**: at least one clean product shot. Missing photos show as labelled boxes and go on the handoff list.
- **Connectors**: Parker (reviews, comments, and the ad if you name one). Image generation is optional and only ever runs after you say yes to the cost.

## Giving notes

Reply in chat. Name the section when it helps (the sections are S01, S02 ... in page order, the same numbers as the copy table). A note about this page changes this page. A note about the template ("offer landers should always ...") changes it for every brand. A note about the skill changes its rules. Each is logged in `references/feedback-log.md`. If you'd rather tap sections on a page and leave notes there, ask for the draft board.

## Placeholders

`[OFFER]`, `[STAT NEEDED: ...]` and photo boxes are highlighted on the page until the brand confirms those facts. The skill never fills them with a plausible guess.

## What's in this folder

| Path | What |
|---|---|
| `SKILL.md` | The workflow and hard rules Claude follows |
| `strategy.md`, `brief-schema.md` | How to run it and recommend a template; the brief fields |
| `processes/` | One file per step, including `apply-feedback.md` (the learning loop) |
| `templates/` | The 5 templates: `INDEX.json` (what the scripts read) and a readable card each |
| `scripts/` | Start a run, the copy check and table, the page builder, screenshots, functional browser QA, comparison strips and the board |
| `assets/` | The board page |
| `references/` | Feedback boards and log, the review-gate prompts, fallback method docs and review agents |

**Installed for every session:** `~/.claude/skills/new-landing-page` is a symlink to this folder, so the skill loads in any brain and edits here are the only copy (2026-10-01). Home is the Parker AI brain's `.claude/skills/`, moved from `company/gtm/parker-course/session-prep/session_6/` on 2026-10-01; the symlinks were repointed in the same pass.

If there is already a landing page and the job is to change, improve, adapt, or create a new version of it, use `iterate-landing-page` instead. That workflow uses the existing page as its baseline and never opens the template picker.

**The swipe file** lives inside this folder at `swipe-file/` (moved in on 2026-10-01). To use the skill somewhere else, copy this whole folder into that place's `.claude/skills/`; the swipe file comes with it.

**Showing it to other people:** the templates and the swipe file's screenshots are public pages and safe to show. The spend numbers in the swipe file (hidden on its page until switched on) and any brand's brief, copy or page are client material.

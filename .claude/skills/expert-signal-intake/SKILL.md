---
name: expert-signal-intake
description: Turn a knowledge source the strategist hands the assistant — an expert video, transcript, tweet, post, newsletter, podcast, article, or report — into an exact, verbatim proposal of what the assistant would change, for the strategist to approve, modify, or deny before anything is written. Use when the strategist drops a source and wants the assistant to learn from it.
triggers:
  - add this expert link
  - upload this expert video
  - analyze this expert video
  - save this video to the assistant
  - save this expert insight
  - drop this into the assistant's brain
  - keep the assistant in the loop
  - save this tweet
  - save this YouTube video
  - save this TikTok
  - ingest this expert content
  - add this to expert insights
  - make a context doc from this
  - turn this into a context doc
  - teach the assistant this
---

# Knowledge Source Intake

## Goal

The strategist hands the assistant a knowledge source. The assistant studies it, decides which part of the system should learn from it, and writes the **exact change it would make — verbatim** — as a proposal for the strategist to approve, modify, or deny. **The assistant does not touch the real context docs, knowledge docs, skills, or prompts until the strategist approves.** On approval, the assistant applies the approved text exactly; on modify, it applies the strategist's version; on deny, nothing is written and the receipt records the decision.

This is an **approval-gated, propose-first** model. The deliverable is a precise plan of what would change, shown before it happens — not a change already made to a live surface. (This replaces the earlier draft-first model, where the assistant wrote `[~]` drafts directly into the real docs and the strategist reviewed them in place. The gate now comes before the write, not after.)

## What "exact and verbatim" means

The proposal is worthless if the strategist has to imagine the change. Every proposal states the literal edit:

- **Editing an existing doc** — show the exact target file, where the change goes, and the precise text, as an old → new (or the exact block to insert and the line/section it follows). The strategist should be able to read it as the diff it will become.
- **Creating a new doc** — show the full proposed file content, verbatim, and its exact path.
- **A tool-use or process change** — quote the exact lines to be added or replaced in the skill or process file.

No summaries standing in for the change. "Add a section on X to hooks.md" is not a proposal; the actual section text is.

## The four components the assistant can update

A the assistant skill is just deciding how to accomplish a task from the context and tools available. Four things make up that capability, and every knowledge source proposes a change to one or more of them. The assistant's first real decision on intake is which:

1. **Context docs** — knowledge tied to a specific subject the assistant reasons about: brand, competitor, and creative-strategy context. Most creative-strategy expert content lands here.
2. **Knowledge docs** — broader marketing, platform, or method knowledge not tied to one brand and not itself a process. Platform mechanics, measurement frameworks, category truths.
3. **Tool calls** — when the source changes which the data routes tool or data source to reach for, or how to read its output. Updates the tool-use guidance a skill carries.
4. **Processes** — when the source changes how the assistant does a task: a step, an ordering, a check. Updates a process doc inside a skill.

## Two proposal stances

The assistant chooses one based on how clear and how corroborated the learning is.

- **Propose a change.** When the assistant can responsibly say exactly what should change, write the verbatim proposal against its real target surface. This is the default. It is still a proposal — nothing is written until the strategist approves.
- **Watch (no change proposed).** When the source is a single, mixed-confidence claim that should not reshape a surface until corroborated, do not manufacture a change. Record it as a watch item with its promotion condition and route the pattern to `parker-taste/patterns-to-monitor/`. One unverified source does not earn a change proposal.

There is also a real third outcome: **no change warranted.** If the source largely duplicates what the assistant already holds, say so plainly and propose nothing. Adding near-duplicate material is bloat, and bloat makes the doc worse. A clear "already covered, here's where" is a valid and valuable result.

## How this skill runs

1. **Acquire the source in full.** Prefer uploaded video through Gemini in the assistant Vault for video. Use pasted content, transcript, screenshots, or a user note when that is what the strategist provides. Never process a partial: if a transcript is cut off or a link is inaccessible, get the rest before extracting.

2. **Study it before proposing anything.** Read the whole source, and read the sibling surface it would touch, before writing a proposal. A proposal about hooks that does not use the hooks doc's vocabulary proves the source was skimmed.

3. **Extract the learning.** Separate the expert claim, the evidence basis, and the assistant's inference. Note source limits and confidence. Be brutally honest about value-vs-noise: will this materially change how the assistant reasons or only add length?

4. **Save the provenance receipt.** Write the signal record under `expert-insights/inbox/` using the expert-signal-db schema. This records where the source came from and its limits. Saving the receipt is the one thing that happens to the filesystem without approval, because it is a record of the source, not a change to the assistant's knowledge.

5. **Classify against the four components and decide the stance** — propose a change, watch, or no-change-warranted. Default to updating a living surface over creating a new one; check existing docs first.

6. **Write the verbatim proposal.** State the exact target surface(s) and the literal change against each — old → new for edits, full content for new docs — per "exact and verbatim" above. **Do not modify or create the real surface.** Persist the proposal as the review-queue entry in `expert-insights/context-update-candidates/` (full verbatim plan, marked `proposed — pending the strategist`), and present the same plan to the strategist directly so he can act on it live. One queue entry per intake, so the strategist has a single place to see everything waiting.

7. **Make the idea-bank decision.** Every source gets checked for idea-bank value. Verify the idea is genuinely new before proposing an idea-bank entry: search the skills and processes, the context docs, the knowledge docs, and the existing idea-bank entries. If the assistant already has it, sharpen the existing surface instead and record an already-covered decision. A genuinely new idea is proposed (not written) to its bank: brand-specific to `idea-bank/`, reusable cross-brand to the factory's `creative-strategy-context/parker-taste/idea-bank/` (read-only in a brand brain, so there it stays a proposal for the the assistant team). Idea-bank entries follow the same gate — proposed, then created on approval.

8. **Wait for the strategist's decision, then act.** On **approve**, apply the proposed text exactly to its target surface and update the queue entry to `applied`. On **modify**, apply the strategist's adjusted version and record what changed. On **deny**, write nothing to the surface and mark the queue entry `denied` with the reason. The provenance receipt stays either way.

9. **Report.** Lead with the proposal — the source you read, which of the four components it touches, and the exact change you are proposing — so the strategist is reviewing the real plan, not a description of it.

## Output structure

### Saved Receipt
The provenance record (expert-signal-db schema) — the only thing written without approval.

### Proposal
For each target surface: the component, the exact path, whether it is an edit or a new doc, and the **verbatim** change (old → new, or full new-doc content). This is what the strategist approves, modifies, or denies.

### Stance And Honesty Note
Propose-a-change, watch, or no-change-warranted — and a straight read on whether this adds real value or would be bloat.

### Idea-Bank Decision
Proposed brand idea-bank entry, proposed taste idea-bank entry, or no-idea-bank reason.

### Source Limits
What the assistant accessed and what remained unavailable.

## Hard rules

- **The approval gate is mandatory.** Never create or modify a real context doc, knowledge doc, skill, or process from a source before the strategist approves. The only pre-approval write is the provenance receipt in `inbox/`.
- **Proposals are verbatim.** Show the literal change — old → new for edits, full content for new docs. A summary is not a proposal.
- Study the full source, and the sibling surface, before proposing. Never extract from a partial.
- Default to a stance honestly: propose only what you can responsibly specify; watch what is too thin; and say "no change warranted" when the source duplicates what the assistant already holds. Anti-bloat is a feature.
- Keep the expert claim separate from the assistant's inference. Preserve attribution. Use short quotes only when needed.
- Use narrative reconstruction for any video, ad, or visual source.
- Do not turn one expert's opinion into universal law. A mixed-confidence single-source claim that would change method is a watch item, not a proposed change.
- Do not default to net-new docs. Propose updating the living surface unless the learning is genuinely distinct.
- Every source gets an idea-bank routing decision, under the same gate.
- One review-queue entry per intake, carrying the full verbatim proposal, so the strategist never has to dig and never has to imagine the change.

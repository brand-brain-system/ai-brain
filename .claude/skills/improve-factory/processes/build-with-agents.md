# Build with parallel agents

## Input

The approved `plan.md` from `decide-homes.md`.

## Steps

**First, check a team pays.** Builders earn their cost when the release has new files that split into independent pieces (`system/agent-teams.md`, section 1). A release that is mostly small edits to existing files is built by the lead alone, and steps 1-5 are skipped.


1. **Write the shared contract first**, in the scratchpad: `vN-contract.md`. Builders read it before anything else. It holds what more than one builder must agree on:
   - The release number and the rule that nothing brand-specific lands in the factory
   - A table of the new pieces: piece, path, builder
   - The layouts to follow (skill layout, method doc layout with the 240-byte summary, script rules)
   - Every shared name: file paths in the brain, CSV columns, tag fields and their allowed values, naming conventions, IDs
   - Which existing pieces to reuse and never duplicate (from `coverage.md`)
   - Who wires what: **the lead wires; builders create only their own files**
2. **Split the work so no two builders touch the same file.** One builder per skill, one for all new method docs, one per script with its test. Shared docs are never given to a builder.
3. **Start the builders in parallel**, one `factory-builder` agent each (`.claude/agents/factory-builder.md`: only the tools a builder needs), with the brief below. Each owns its own new files only. For a change to an existing file, it returns the exact edit
   (file, old text, new text) in its report instead of making it.
4. **While they run**, the lead prepares the wiring: the catalog rows, the migration skeleton, the release notes skeleton. The lead never edits a builder's files.
5. **Read every report.** Check each new file exists, follows the contract and passes its own test. Collect the proposed edits into one list for `wire-and-release.md`. Where two builders
   propose edits to the same file, merge them by hand.
6. **One review pass** on the new prose: no brand names, no source text pasted unchanged, claims labelled, paths are brain paths or `brain-system/` paths inside skills.

## Builder brief template

Copy, fill the brackets, send one per builder.

```
You are building part of release v[N] of the Brand-brain factory repo at [factory path] (Claude Code skills and craft docs for
Meta ad creative strategy; brand brains are separate repos that mount this factory at brain-system/). Read first:
1. [factory path]/CLAUDE.md (the factory rules; obey them)
2. [scratchpad path]/v[N]-contract.md (what this release adds; other agents build the other pieces in parallel)
3. `python scripts/factory-map.py` output, then only these files: [the files this builder needs, from coverage.md]

The owner's request, in their words: "[quote]". Context: [one or two lines].

YOUR JOB: create
(a) [path]: [what it holds, sections, rules]
(b) [path]: [...]
(c) [test path]: [what it checks]. Run it and make it pass.

Create only these files; edit nothing else. Style: English, plain words, short sentences, no em dashes, no emojis. Sources are
rewritten in our words, labelled Stated, never pasted unchanged. Run `python scripts/voice-lint.py <file>` on new prose; fix real
tells. Do not commit.

Final report (under 250 words): files with line counts, test results, and every edit you recommend in existing files
(file, exact old text -> new text).
```

## Output

The new files in place and not committed, plus one list of proposed edits to existing files for the lead.

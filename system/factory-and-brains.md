# Factory and brains

Two kinds of repo, one direction of travel: the method flows from the factory into every brain; what a brain learns flows back only by being generalised and promoted.

## The two kinds

| | Factory (`Brand-brain`) | Brain (one per brand) |
|---|---|---|
| Holds | Skills, templates, method docs, the swipe library, system docs, scripts | The brand's data and decisions: profile, lens, personas, competitors, strategy, ideas, sprints, learnings |
| Changes when | The method improves | The brand's work moves |
| Edited by | Whoever improves the method, through a reviewed change | The whole team, daily |
| Contains brand data | Never | Always; that is its job |
| Visible to | The team | The team working on that brand (and the brand, if shared) |

A brain never edits the factory. A lesson learned on a brand that should help every brand is *promoted*: generalised, stripped of brand details, credited, and committed to the factory in a pull request.

## How a brain carries the factory

1. **A read-only mount.** The factory is a git submodule at `brain-system/`, pinned to a release tag (`v1`, `v2`...). The brain's `.claude/settings.json` denies edits under `brain-system/`.
2. **Copied skills.** Claude Code loads skills only from `.claude/skills/`, so `python brain-system/scripts/scaffold-brain.py sync` copies the factory's skills (and agents) into the brain's own
   `.claude/`. The copies are never edited by hand.
3. **Shared knowledge read in place.** Method docs, `production.md` and the swipe library are read from `brain-system/creative-strategy-context/`, never copied into the brain.
4. **A version stamp.** `.brain-version` records the pinned release and commit so anyone can see what the brain was built with.

## Making a brain

`python scripts/scaffold-brain.py init <folder> --name "<Brand>" --category "<category>" --factory-url <url> --pin vN` writes the empty brain (templates with the brand name filled in), copies the
skills, writes `.brain-version`, initialises git and mounts the factory. No AI is involved, it takes seconds, and it never overwrites a file that already exists, so it is safe to re-run.
What happens next (the build) is the job of the `build-brain` skill and the fill order in the brain's `README.md`.

## Updating a brain

The `update-brain` routine (weekly, or on request):

1. Compare the pinned tag with the newest release tag
2. Show `release-notes/` for every release in between and `migrations/vN.md` for each
3. On a yes: move the pin, apply the migrations in order (they say exactly which brain files to add or change), re-run `sync`
4. Record what was applied and what was declined in `running-notes/`. A declined change stays declined until someone asks again

A migration is written for a person and an AI to follow: what changed, why, the exact steps, how to check it worked.

## Releasing the factory

1. Change the factory on a branch; test the change on a brain (test brands count)
2. Add `migrations/vN.md` and `release-notes/vN.md`; bump `VERSION`
3. Merge, tag `vN`, push the tag. `python scripts/check-release.py vN` first: it fails when `VERSION`, the two notes and the tag
   disagree. The "Release check" workflow runs it on every PR and tag push; a tag that fails there gets deleted, fixed and pushed again
4. Brains see the new tag at their next `update-brain`

## Working together in a brain

Several people and several Claude Code sessions share one brain through git. The rules are in the brain's `CLAUDE.md` ("Working together"): pull before you start, push when done, small commits, one writer
per file, branches for big rewrites, no secrets, images through Git LFS.

## One brain per client

At an agency every client has its own brain, and a routine runs inside one brain only, so one client's data can never appear in another's report. A strategist who wants one overview can use a digest
that links to each brain's latest report; the data stays in its brain.

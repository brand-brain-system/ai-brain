---
name: save-brain
description: How this brain saves and shares itself through git - the required knowledge for anything save, sync, backup, clone, share or "is my work saved" shaped in a brand brain. Pull before work, small commits, push after; combine clashes by keeping both sides; never force-push. Use whenever work in the brain is done, when a teammate's changes should come in, or when git reports a clash.
---

# Save brain: pull, commit, push

A brand brain is a git repo on GitHub that the team shares. Several people and several Claude Code sessions (scheduled routines included) write to it. Git is how everyone's work meets: saving is
a commit and a push, and getting a teammate's work is a pull. Origin: Parker's save-brain skill, rewritten for teams that host their own repo (the assistant's "self-managed" case).

## Before starting work

```
git pull --rebase
git submodule update --init
```

The second line makes sure the method mount `brain-system/` is present and at the pinned release. Never move the pin here; that is `/update-brain`'s job.

## Saving

When a piece of work is done (a doc written, a batch of ads filed, notes updated), save it:

```
git add -A
git commit -m "<area>: <what changed>"
git pull --rebase
git push
```

- **One topic per commit**, named by area: `personas: add the gift-buyer card`, `sprints: file the black-friday statics`, `running-notes: log the Q4 offer`
- **Check what you add.** `git status --short` first. Never add `.env` files, keys, tokens, exports with customers' personal data, or anything the brain's `CLAUDE.md` keeps out
- **Images, video and PDFs** go through Git LFS automatically (`.gitattributes`); nothing to do
- A push refused as `non-fast-forward` or `fetch first` only means someone saved meanwhile: `git pull --rebase`, then push again

## When a pull clashes

Two people changed the same lines. Git marks them:

```
<<<<<<< HEAD
the version from one side
=======
the version from the other side
>>>>>>> <commit>
```

Edit each file so it keeps everything meaningful from **both** sides in the right place, delete every marker line, then `git add <file>` and `git rebase --continue`. `git diff --name-only --diff-filter=U`
lists the files still to combine. If both sides made the same decision differently (two verdicts, two prices), don't pick: keep both, mark the conflict in `running-notes/missing-context.md`, and ask
the person.

## Big rewrites

A rewrite of a whole standing doc (personas, the roadmap, the offer brief) goes on a branch, `git switch -c <area>-<what>`, is pushed, and is merged after a person has read it. Say so in
`running-notes/current-work.md` while it is open, so nobody edits the same doc on `main`.

## Scheduled routines and cloud runs

A routine running in the cloud works in its own clone: pull first, do the job, save with the commands above, push to `main`. It needs a GitHub credential that can push to this repo, set up by a
person once (a deploy key or a fine-grained token stored in the scheduler's secrets, never in the repo). Without one it ends by saying plainly that its work could not be saved.

## Is my work saved?

`git status --short --branch`: no changed files and no `ahead` count means everything is on GitHub.

## Talking to the user

Most people on a brand team aren't git people and don't need to be. Say "saved and shared", "your teammate's changes are in", "two edits touched the same lines; here is how I combined them". Show git
commands only to someone who wants them.

## Hard rules

- Never force-push, never rewrite history that is already pushed, never delete a branch someone else made
- Never commit secrets or customers' personal data
- Never edit or commit inside `brain-system/` (it is read-only; changes to the method go to the factory repo)
- If saving fails (no credential, no network), say so; never leave someone believing unsaved work is backed up

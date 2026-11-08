---
name: set-up-brain
description: The front door to building a brand's brain. Run this when standing up a new brand. It welcomes the person, finds the brand's brain repo, settles the data routes (exports, public pages, connected tools), asks the short brand intake, runs the build from the onboarding runner (audit, strategy, ideas), verifies it, saves it to GitHub and hands off to /get-started. Use when someone says set up a brain for a brand, build the brand brain, onboard a brand, or start a new client.
argument-hint: "[optional: the brand name]"
---

# Set up the brain: build a brand's brain from scratch

This is the front door. Someone wants a brain for their brand, and your job is to take them from nothing to a finished, saved brain they understand, warmly and at their pace. Origin: Parker's set-up-brain
skill, rewritten for brains shared through git and fed by exports and public data instead of a managed data connection.

**The whole thing is a teaching moment, not a batch job.** Many people running this have never used Claude Code or git. Narrate in plain language what you're about to do, why it matters and what they'll
have when it's done. Keep the machinery out of sight.

Before a build, read `feedback.md` here for open trials, and log what the build taught you there.

## Calibrate to their comfort first

Get a read on how comfortable they are with Claude Code, git, and files and folders. Ask lightly, or infer it from how they talk. A beginner needs the ground floor explained with nothing assumed; a fluent
user wants you to move fast and skip the tour. This read shapes the whole run, the same way it shapes `/get-started`.

## How this sounds

Follow the voice in `prompts/_voice-block.md`: plain words, short sentences, no emojis, no em dashes, no invented vocabulary. You talk like a good colleague walking someone through something.

## The sequence

Run these in order, following `prompts/onboarding-runner.md` for the exact mechanics. Talk at the moments that matter; let the long stretches run quiet. Whenever the run needs something from them (a
comfort read, an intake answer, the roadmap call, a blocker), **ask through the question form, never as a plain chat question**: the form is what notifies them, and a chat question strands the build
where nobody sees it.

0. **Find out what already exists, before any pitch.** Run the runner's existence check ("Before anything: find out what already exists"). A fully built brain is a retrieval, not a build: say so and go to `/get-started`. A mid-build brain gets an offer to resume. Only a scaffolded or empty brain gets the full run.
1. **Welcome and orient them, then get the go-ahead.** Follow the runner's orientation: what a brand brain is, the three phases, where they're in control, what they get. Set the time and cost expectation honestly and ask for a real go/no-go, with the lighter first pass as an option.
1b. **Tools and data routes, before the build and not after.** Ask what the team works in and get it connected (Notion, Drive, Slack, Gmail, calendar). Then settle the data routes: for each source in `brain-system/system/data-access.md`, what can the brand give (an ad-account export, review and survey exports)? Write the answers into `tool-map.md`. Ask for the ad-account export first; nothing changes the audit more.
2. **Be in the brand's brain repo.** The brain is a separate private repo for the brand. A person creates the empty repo on GitHub; you clone it (or work in the clone you were opened in) and `git pull --rebase`. Never write brand data into a factory clone.
3. **Attach the method library and run the scaffold.** Mount the factory at `brain-system/` as a read-only submodule pinned to the newest release tag, then `python3 brain-system/scripts/scaffold-brain.py init --brand-name "<name>" --brand-id <slug>`. A plain script, no AI, seconds. Commit and push the result.
4. **Run the brand intake: what only they can tell you.** The short, skippable set about what the sources can't show: their objective, north-star metric, how they define a winner, ad naming convention (none yet: offer `brain-system/system/ad-naming-convention.md`; they keep theirs: `creative-leaderboard` naming-setup maps it into `running-notes/ad-naming.md`), where they read performance, who they consider real competitors, optional unit economics. Answers go to `running-notes/` and `brand-lens.md`. Anything skipped becomes a line in `missing-context.md`.
5. **Read in.** The scaffold shipped the method, so there is nothing to copy: read the entry context the runner names and open the build log.
6. **Run the build.** Execute the prompts in dependency order per the runner: Phase 1 audit, Phase 2 strategy (with its gate honored per their intake answer), Phase 3 ideation. Speak at phase boundaries, a few plain sentences on what just got built and what starts now. Everything between boundaries goes to `BUILD-STATUS.md` and the run log.
7. **Verify the build and confirm it's saved.** Run the build verification; once it passes, make sure `.scaffolded` is gone and archive `BUILD-STATUS.md` into `prompts-run-log/`, in that order. Then commit by area, `git pull --rebase`, `git push`, and check there is no `ahead` count.
8. **Hand off to `/get-started`.** Lead with one plain sentence about the real schedule state (what's registered and when it runs, with `/setup-routines` to adjust it, or that the routines run on demand). Then run `/get-started` to walk them through the finished brain. If the brand has a Meta ad account, end by offering `/account-playbook`: it takes the brand from ad-account access to the weekly loop.

## Hard rules

- **The brand gets its own repo.** Never write brand data into the factory or a factory clone
- **The method is mounted, never copied.** `brain-system/` is a git submodule of the factory. If the mount command is blocked or needs approval, ask through the form and wait; never copy the factory's files in as a substitute
- **The setup files come from the scaffold script, never by hand.** It copies method files verbatim and seeds the brand's starting files; hand copies drift
- **A stop is a pause; an undo lands on the scaffold, never on an empty folder.** A stop keeps everything for the next session to resume. Undo only when they clearly ask for it; never offer it yourself
- **The intake is never a gate.** Skippable, calibrated, personal. Skipped items are open questions in `missing-context.md`, and the build runs as normal without them
- **Nothing leaves without a person.** Nothing is sent, posted, published or paid for without a yes
- **Teach at the moments, run quiet between them.** Neither a silent grind nor a wall of narration
- **Keep `BUILD-STATUS.md` true at every state change.** It is the answer to "where are we", and the ledger a dead session resumes from
- **Defer the detail to the runner.** `prompts/onboarding-runner.md` is the canonical build method. Follow it; don't reinvent it here
- **End on `/get-started`.** The build isn't the deliverable; a person who can use it is

## Deliverable

A finished brand brain in its own repo, built from the brand's real data and public sources, shaped by whatever intake they chose to give, verified and pushed to GitHub, and a person who has been walked
through it and handed off to `/get-started`.

---
name: setup-routines
description: Arms the brand brain's standing routines (refresh-context, dream, harvest+evaluate ideas, research-loops, update-brain, self-improve) as scheduled cloud agents so they run on cadence without being asked. The job definitions already travel with this repo; this skill registers the schedules, which are per-account and can't be committed. The onboarding build runs it at the stamp step (build mode, no questions); run it yourself after cloning the brain onto a new account, or any time the schedules need changing. Use when someone says arm the routines, schedule the brain, set up the cron jobs, or turn on dreaming.
---

# Setup routines: arm the schedules

The routine *jobs* (`/refresh-context`, `/dream`, `/harvest-ideas`, `/evaluate-ideas`, `/research-loops`, `/update-brain`, `/self-improve`) already travel with this repo and are live wherever the folder
lands. What does **not** travel is the *schedule*: cloud agents are bound to an individual account and can't travel with the folder. This skill registers them for this account. Origin: Parker's
setup-routines skill, rewritten for brains hosted on GitHub.

## How it works

For each routine below, create a scheduled cloud agent (a "routine") whose source repository is **this brain's own repo on GitHub** and whose prompt runs the corresponding skill in that copy (step 2 has
the exact prompt). Use the **`/schedule`** skill to create each one. The cadence and prompt for each are also recorded in `../schedules/*.md`; those docs are the canonical recipe and this skill is the
guided installer.

Two modes. **Build mode:** the onboarding build invokes it at the stamp step: register all six routines at the default cadences with no questions, using the user's timezone when the session already
knows it and the suggested times otherwise. The build's go-ahead covers consent and its finish carries the disclosure. **Guided mode:** a person invokes it: confirm their timezone, which routines they
want, and that the data sources they need are connected, then register what they pick.

Check the scheduling capability first. If cloud scheduling isn't available (a different harness, or an account without it), record scheduling as deferred in the build record, leave the recipes
inactive, explain that the skills work on demand (`/dream`, `/refresh-context` and the rest), and return successfully. A team's own cron is separate setup.

**Say what it costs, plainly, once.** Every scheduled run is a real Claude Code session doing real reading and writing, and it draws from the same usage as everything else on the account. Six routines
with dreaming daily is a meaningful standing draw, and dreaming is the biggest single driver. In guided mode, say this before registering and let it shape their picks (dreaming a few days a week instead
of daily is a fine choice). In build mode, make sure the finish's disclosure sentence carries it: what's running, when, that it uses this account's usage, and that a run can only save if its cloud
environment can push to the brain's repo.

## The routines to register

| Routine | Skill | Cadence | Suggested cron |
|---|---|---|---|
| Context refresh | `/refresh-context` | Weekly | Mon 06:00 |
| Dreaming | `/dream` | Daily | 05:00 daily |
| Idea cycle | `/harvest-ideas` then `/evaluate-ideas` | Weekly | Mon 07:00 |
| Research cycle | `/research-loops` | Weekly | Wed 06:00 |
| Standard updates | `/update-brain` | Weekly | Mon 05:30 |
| Self-improvement | `/self-improve` | Weekly | Fri 16:00 |

Times are suggestions; confirm against the user's timezone and rhythm. Dreaming runs earliest so its proposals are ready for a morning suggestion; the research cycle runs mid-week so Monday's refresh
feeds it; self-improve runs at the end of the week so it can dispose of the week's proposals.

## Steps

1. **Confirm prerequisites** (guided mode only): timezone, connected tools, and that the user wants all six or a subset. Build mode skips this and registers the full set at the defaults.
   - **Check what's already armed, live state first.** List this account's live schedules via `/schedule`; that is the ground truth for this account. Then read the status lines in `../schedules/*.md`, the only visibility into other accounts. Treat those lines as claims: if a line says this account armed a routine but the live list disagrees, trust the live list and fix the line
   - **One owner per routine.** If a teammate has already armed a routine, don't arm it again: two accounts running the same weekly refresh means every routine fires twice, doubles the usage, and has two runs pushing generated docs into the same repo. The right setup is one person owning each schedule
2. **Register each routine** via `/schedule`, one per row above: all six in build mode, and in guided mode the ones the user picked. **Prefix every schedule's name with the brand**: "[brand]: dream", "[brand]: standard updates", because schedules are account-level and an account running two brain repos would otherwise hold two indistinguishable "dream" jobs; the prefix is also what the reconcile step matches on. For the idea cycle, schedule a single weekly agent that runs `/harvest-ideas` then `/evaluate-ideas`.
   - **The run gets the brain from GitHub.** Set the routine's source repository to this brain's repo. Its cloud environment needs push access to that repo (the account's GitHub connection, or a deploy key or fine-grained token stored in the scheduler's secrets, never in the repo), read access to the factory repo (the `brain-system` submodule), and network access that allows `github.com`. If a routine can't push, it still does the work but can't save it: say so to the person plainly
   - **The prompt is the preamble plus the job.** Fill in the brand's name:

     > This is a scheduled cloud run for the brand brain of [brand]. Start with `git pull --rebase` and `git submodule update --init`. Work only in this repository. Run the job below by following its skill in `.claude/skills/`. When you are done, save as `/save-brain` says: small commit named by area, `git pull --rebase`, `git push` to `main`, which you have permission to do. If the push is refused because someone saved meanwhile, pull with rebase and push again. If it clashes, keep both sides and say so. Never force-push. If you cannot push, say so plainly at the end.
     >
     > You are running unattended. A message without a tool call ends the run. Never end on a summary that announces the next step, an offer to continue, a list of decisions that do not block you, or a milestone report. Keep a checklist and tick it as you go. Time matters: the earlier a correct result, the better; the budget is [N] minutes. Stop when the checklist is done or you are truly blocked, and write what blocked you to `running-notes/routine-log.md`. Draft only: never send, post, publish, pay or delete.
     >
     > Run the /dream routine for this brand brain. Follow the skill exactly; propose, never apply.

     The unattended block is the one in `brain-system/system/agent-teams.md` (section 9). Set [N] a little above how long the routine should take (about 20 for dream, 45 for the idea cycle), and set the scheduler's own timeout, where it has one, as the hard stop.

     The job line stays minimal and lets the committed SKILL.md carry the method; each schedule's recipe in `../schedules/` has its own job line.
3. **Verify.** List the scheduled routines back to the user with their next-run times, and confirm each points at the right skill.
4. **Record.** Note in each `../schedules/[slug].md` that the schedule is registered for this account (status: active, who registered it and when). The new line replaces the old one, a "needs re-arm" note included, so the schedule doc reflects reality and a teammate's later `/setup-routines` run can see the routines are already owned. Commit and push the change like any other.

## Notes

- **Re-runnable safely.** If a routine is already registered, update it rather than duplicating. List existing routines first and reconcile, matching on this brand's name prefix, so another brain's routines on the same account are never touched
- **A subset is fine.** A user may want only dreaming and ideas at first. Register what they confirm; leave the rest documented in `../schedules/` for later
- **Manual fallback.** Every routine can also be run on demand by invoking its skill directly (`/dream`, `/self-improve`, ...) without any schedule, which is useful for a first manual pass before arming the cron
- Self-contained: this skill registers schedules that point at in-repo skills. It does not depend on the factory beyond the mounted method

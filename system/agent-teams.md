# Agent teams: when to spawn, how to brief, what it may cost

The one home for how the factory and its brains use subagents. Skills point here instead of carrying their own wording. Token habits in general (new topic, new session; which model
tier) stay in `model-routing.md`.

**Source and status.** Built in v22 from a practitioner's article on agent teams for Claude Opus 5.5 (Nov 2026), rewritten in our words; the article's claims about the model are
*Stated*, not tested by us. The review tiers, effort levels and caps below are **on trial** until the pilot in `REWRITE-QUEUE.md` (section 16) has measured them on real work. Log what
you see in `.claude/skills/improve-factory/feedback.md`.

## 1. Most jobs need no team

A team costs coordination, extra calls and new ways to fail. Spawn only when at least one of these is true:

1. **The work splits** into parts that don't need each other's results, so they can run at once
2. **The reading would flood** the main conversation with text nobody needs afterwards (many pages, an export, a long ad list)
3. **A part needs other permissions or another expertise** than the rest, above all an independent critic that did not write the work

None true: the main session does the job alone. One job with one clear check is faster and cheaper as one session.

## 2. Three roles

| Role | Who in our setup | Does | Never does |
|---|---|---|---|
| Orchestrator | The main session running the skill | Plans, splits, briefs, waits, assembles, decides | The bulk reading |
| Specialist | `gather` (reads), `factory-builder` (writes factory files) | One narrow job, returns in the asked format | Judge, rank or recommend (`gather`); touch files outside its brief (`factory-builder`) |
| Critic | `context-grounding-review`, `creative-voice-review` | Checks finished work against a standard, sends it back | Edit the work; it reports |

The orchestrator in our creative skills also writes: it holds the brand context, and a separate writer would need that whole context in its brief for no gain.

## 3. The brief

A subagent sees nothing of the conversation. The brief is all it has. Every spawn uses this shape:

```
ROLE     the agent and its one job
GOAL     the user's ask, quoted
INPUTS   every file path, finding, decision and constraint it needs
LIMITS   what it must not touch or decide
RETURN   the exact format and a length cap; "not found" instead of a guess
STOP     when to stop, and what to return if blocked
```

A brief that says "now write it up" without the material makes the agent guess. When a return must survive exactly (a reviewer's verdict, a quote), the orchestrator keeps it verbatim
and does not summarise it. The receipt blocks in the creative skills already work this way.

## 4. Run independent work at once

Name the independent steps in the skill and dispatch them in one message: three gatherers on three sources finish in the time of the slowest. Work that needs their results waits for
all of them. Builders and gatherers never share a file.

## 5. Effort per role

| Role | Model | Effort |
|---|---|---|
| `gather` | small (haiku) | low |
| `creative-voice-review` | mid (sonnet) | medium |
| `context-grounding-review` | large (opus) | medium; high only if the pilot shows misses |
| `factory-builder` | inherit | medium |
| Main session | the person's choice | medium; high for strategy calls; xhigh only for runs over about 30 minutes |

Each agent file carries its effort in its frontmatter. When a spawn tool takes an effort value, pass the same one.

## 6. Review tiers

What the output is for decides how far the two creative gates run. The skill picks the tier from the ask and states it in the output; it never asks the user to choose.

| Tier | When | Gates |
|---|---|---|
| **Ship** (default) | Anything that goes to a client, an editor, a creator, a page or the ad account | Grounding gate, then voice gate, exactly as the skill says |
| **Draft** | The user asks for options, ideas or a first pass to react to, or says it is internal | `scripts/grounding-check.py` and `scripts/voice-lint.py` in the main session, then one `creative-voice-review` pass. The output is headed "Draft: not reviewed for ship" |
| **Read** | Account reads, data pulls, breakdowns with no new copy | No creative gate. `evidence-and-labels.md` still applies |

A draft the user picks to use becomes Ship: run both gates on the picked items before they leave the brain. In doubt, Ship.

**Round caps.** Each gate runs three rounds at most. After the third, ship with the open objections shown as unresolved, never as passed. The grounding gate gets a reading list from
the orchestrator: the method docs it routed to and the session's pull log. It reads those in full and may add a doc it finds missing; it does not re-derive the whole routing.

## 7. Least power

A tool left out of an agent's list does not exist for it. Give each role only what its job needs:

| Role | Tools |
|---|---|
| Reader (`gather`) | Read, Grep, Glob, WebFetch, WebSearch |
| Critic | Read, Grep, Glob, plus Bash only to run its named check script |
| Builder (`factory-builder`) | Read, Grep, Glob, Edit, Write, plus Bash only to run its own test |

No subagent gets the Agent tool, and none sends, posts, publishes, pays or deletes (factory rule 4).

## 8. Caps

The brain's `.claude/settings.json` (from `templates/brand-routines/claude/settings.json`) and the owner's global settings set:

- `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` = 1: specialists never spawn their own
- `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` = 5: at most five at once

A spend ceiling (`max_budget_usd`) exists only in the Agent SDK. Use it if a routine is ever run from our own script. In the Claude app, spend is guarded by these caps and by showing
prices before any paid generation (`creative-strategy-context/production.md`).

## 9. Unattended runs

Scheduled routines run with nobody watching. The prompt `/setup-routines` registers carries this block after the save preamble:

```
You are running unattended. A message without a tool call ends the run.
Never end on: a summary that announces the next step, an offer to continue,
a list of decisions that do not block you, or a milestone report.
Keep a checklist and tick it as you go. Time matters: the earlier a correct
result, the better; the budget is [N] minutes. Stop when the checklist is done
or you are truly blocked, and write what blocked you to running-notes/routine-log.md.
Draft only: never send, post, publish, pay or delete.
```

The time budget is a pacing hint. Set it a little above the time the routine should take. The hard stop is the schedule's own timeout, where the runner offers one.

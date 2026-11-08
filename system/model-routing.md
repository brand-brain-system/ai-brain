# Model routing: spend less, get the same work

Every message in a session resends the whole conversation. A session is a snowball: turn 1 is cheap, turn 30 is expensive, and most of the cost is re-reading things nobody is thinking about any more.
Two levers, in order of value: **have fewer tokens in the conversation**, then **make each token cheaper**.

## Habits that matter most

1. **New topic, new session.** Don't ask about one brand in a session full of another's research
2. **Delegate the gathering, keep the thinking.** Reading many pages or files for facts belongs in a subagent on a small model that returns a short structured briefing; the raw text never enters the
   main conversation. Judgment (positioning, which angle, what a rival's move means) stays in the main session, which has the context
3. **Say when a thing is done.** "Drop the job ad" lets the session stop carrying it
4. **Finish the thought, then restart** when a session has grown sluggish

## Which model

| Model tier | Good at | Use for |
|---|---|---|
| Small and fast | Reading, extracting, sorting, following a clear format | Gathering agents: fetch pages, scan files, pull facts, tag ads from a rubric |
| Mid | Most real work: writing, analysis, research, code | The default for skills |
| Large | Judgment, nuance, hard problems | Strategy calls, diagnosis, audits of synthesis, anything that decides money or positioning |

Escalate when the task has genuine judgment in it; don't escalate by default.

## In the factory

When to spawn an agent at all, how to brief it, effort per role, review tiers and caps: `agent-teams.md`.


- Skills that gather in volume (`persona-gap` pulls, `competitor-ad-watch`, `customer-language-pull`) delegate the reading to a gathering agent and keep the synthesis
- The independent audit of a synthesis (`evidence-and-labels.md`) runs on a different agent from the one that wrote it, and on a mid or large tier
- Image and video generation costs real money: every skill shows the price first (`production.md`, "Paying for generation")
- Heavy local renders run small first, once at full size, at low priority

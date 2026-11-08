# Brain hygiene

```
Name:        brain-hygiene
Kind:        routine
Owner:       the strategist on this brand
Schedule:    monthly, first Friday 15:00
Skill:       prompt below
Reads:       the whole brain
Writes:      nothing directly; proposals only
Report:      a short checklist in chat
Ends when:   n/a (routine)
Needs:       nothing
Triggers:    not armed (template)
Started:     -
```

## Prompt

Go through the brain and list, without changing anything:

1. **Open loops** in `missing-context.md` older than 30 days: still open, answered somewhere else,
   or no longer relevant?
2. **Hypotheses** with no new evidence in 60 days.
3. **Personas:** cards with no audit line or an audit older than 90 days; "Testing now" pointing
   to a hypothesis that's already in `validations.md`; a card failing the finish check.
3b. **`current-work.md`** items that look finished or stuck.
4. **Stale sources:** durable docs whose newest source is older than 6 months, and playbooks
   older than 6 months (the playbooks README says re-check them).
5. **Routines:** every file in `schedules/` marked as armed, and whether its trigger still exists.
   Loops whose project is done should be stopped.
6. **Contradictions:** a fact in one doc that another doc or a newer source pull contradicts.
7. **Skills catalog:** the factory's `system/skills-catalog.md` against what's actually there: skills
   added or changed, routines armed or stopped, scheduled tasks, gaps closed. A stale map makes
   every transcript review wrong, so list each mismatch.

Each item gets a proposed action. A human approves before anything is edited or removed.

## Why it earns its keep

A brain that's never cleaned slowly starts giving confident answers from stale facts. This is the
monthly review the routines README already asks for, done by the agent.

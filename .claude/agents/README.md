# Agents

Independent agents that skills spawn, each with its own context: reviewers so they judge the work rather than defend it, and a gatherer so raw reading stays out of the main conversation.

- `context-grounding-review.md`: was the draft built from the right documents, and does every quote and number trace to a file in the brain (runs `scripts/grounding-check.py` first)
- `creative-voice-review.md`: does it read human and on-brand (runs `scripts/voice-lint.py` first)
- `gather.md`: reads many pages or files on a small model and returns a short sourced briefing; no judgment (`system/model-routing.md`)
- `factory-builder.md`: builds one piece of a factory release from the contract, with only the tools that job needs (`improve-factory`, build-with-agents). Factory only

When to spawn, how to brief, the effort per role, the review tiers and the caps: `system/agent-teams.md`. A generic copy of `gather` also lives in the owner's global
`~/.claude/agents/` so folders outside the factory have it; inside the factory and brains, this one wins.

The two reviewers come from Parker, used with permission (`third-party/parker/MANIFEST.md`). Adapt them as the brain's labels and paths evolve.

# Idea bank

This README explains the folder. It is not one of the folder's docs, so leave it out of any list or index of them.

Creative ideas worth making, captured from conversations, audits and the market, and ranked before anything is built from them.

## What lives here

- `index.md`: the searchable list of active ideas.
- `entries/[YYYY-MM-DD]-[concept-slug].md`: one idea per file: what it is, where it came from, and the evidence behind it.
- `evaluation-[date].md`: a ranked evaluation of the bank, the input to the next sprint.
- `concepts.md`: the concept register. Ideas that made it onto a sprint's concept map, each with an ID (`C07`) that every brief, ad set and file name carries, so results can be read per concept. Seeded empty.

The spec is `brain-system/prompts/ideas-and-briefs/brand-idea-bank.md`, and the evaluation is `brain-system/prompts/ideas-and-briefs/idea-evaluation.md`. The skills that keep the bank are in `.claude/skills/`: `harvest-ideas`, `evaluate-ideas` and `brand-idea-bank-maintenance`. The method is in `brain-system/creative-strategy-context/ideation-and-brainstorming.md`.

A new brain starts with this folder empty except for the concept register's header. The build fills it in Phase 3.

# Feedback log

What we've learned running improve-factory: which steps were slow, what the map missed, what a release needed that the checklist didn't say. A log, not a rulebook: a lesson lands here with
a date, and once it has held on a second run it moves into `SKILL.md` or the process it belongs to, leaving one line here saying where it went. No brand details here.

## Log

**2026-11-07, the run that made this skill (release v20)**
- Handed in: a batch of practitioner material on Meta ads (posts, prompts, an infographic). Topics: mining angles from customer words, breaking down ads part by part, an awareness ladder
  for scripts, keeping an angle bank, shared vocabulary for the team, and a study of 100 winning scripts. All labelled Stated; nothing pasted unchanged
- Shipped as v20: method docs for vocabulary, the awareness ladder, winning-script patterns and angle discovery; skills `ad-breakdown`, `angle-bank`, `creative-leaderboard`,
  `account-playbook` and this one; an ad naming convention; `scripts/factory-map.py`
- What was slow: before any analysis, the session had to explore the whole repo again to learn which skills, docs and rules exist and where each rule lives. That is the reason the map
  script exists, and why step 0 is "load the map, do not explore"
- What worked: one shared contract file in the scratchpad, then parallel builders that each owned their own files and returned proposed edits; the lead did all wiring
- Open test: does step 0 (the map plus `CLAUDE.md`) cut the exploring at the start of the next run? Log how many files were opened before the coverage table was done, and what the map
  should have shown but didn't

**2026-11-08, three posts (release v21)**
- Handed in: posts on TOF/BOF against awareness, "ad camouflage" from made-up Pages, and a flow for all-AI ads
- Shipped as v21: the funnel tag fixed (it was derived from awareness, the very mix-up one post names), a product-aware section in `angle-discovery.md`, a Page-identity stop in
  `ad-policy-check`, AI format by awareness in `ai-ad-generation`. Camouflage declined
- What worked: the map plus one grep sweep found the conflict in four reads; the job was small enough to build without builder agents, which saved the contract and re-reads
- Map gap: it doesn't show where tags are defined and derived. A tag index (tag, home, who reads it) would have found the funnel rule at once

**2026-11-08, agent-teams article (release v22)**
- Handed in: a practitioner's article on agent teams for Claude Opus 5.5 (orchestrator, specialists, critic, least power, briefs, parallel work, effort per role, caps, time budget,
  early stops). First a proposal page, approved by the owner, with the draft review tier as an explicit yes
- Shipped as v22: `system/agent-teams.md`, effort lines on the agents, `factory-builder`, review tiers in six creative skills, parallel lines in five long skills, the unattended block in
  `setup-routines`, spawn caps in the brain settings. Outside the factory: a global `CLAUDE.md`, a global `gather` and caps, a `post-review` agent in the personal-brand repo
- What worked: the map plus the proposal meant no exploring; mostly one-line edits, so the lead built it alone (the article's own first rule)
- Open test: the pilot in `REWRITE-QUEUE.md` section 16. Until it has run, tiers, effort and caps are on trial. Check that agent frontmatter reads `effort:` and that the two cap
  variables are honoured on the installed Claude Code version

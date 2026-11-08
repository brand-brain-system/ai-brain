# Stage 0: access and measurement (days 0-2)

Get read-only access, check that the tracking counts right, and settle what a winner is and how
ads are named. Bad tracking poisons every later read, so the tracking check comes before any
creative read.

## Entry criteria

- The brain is built (`/set-up-brain` handed off) and `running-notes/playbook-status.md` exists
- Someone at the brand has said yes to giving us access

## The Day 0 checklist

The tick boxes are on the status page. What each one means:

1. **Access granted at view level.** The brand gives the team member access to the ad account in
   Meta's business settings, with the lowest role that can see performance, plus view access to
   the Events Manager dataset the ads use. The brand does this, not Claude. Role names change; use
   what Meta shows
2. **A route chosen and written in `tool-map.md`.** One of the four routes below. Fill the "Ad
   account" row and the "Own ad account" line under "Data routes", with the date you checked it
3. **The tracking check's inputs collected.** The list is in
   `.claude/skills/ad-account-analysis/processes/measurement-check.md` ("Required inputs").
   Screenshots are enough
4. **The winner definition and north star confirmed.** Read `running-notes/success-definition.md`
   and `running-notes/brand-rules.md` (filled in the brand intake). If either is blank, ask the
   strategist through the form and write the answer there. Never invent one
5. **Naming settled.** Run `creative-leaderboard` `naming-setup`
6. **Who launches, who approves.** Name the person who launches ads and the person who approves
   plans and spend, on the status page. Claude does neither
7. **Day 0 written on the status page,** with the entry point from `../strategy.md`

## The access routes, best first

The route order and the reasons are in `brain-system/system/data-access.md`. In practice:

**1. Meta's Ads MCP server, read-only.** The person who holds the access sets it up and signs in;
Claude never handles their password or token.
- Add the server (`https://mcp.facebook.com/ads`) with `claude mcp add --transport http` at local
  scope, the default, which keeps it in that person's own Claude Code config. Never
  `--scope project`: that writes `.mcp.json` into the brain repo
- Grant `ads_read` only. Meta's setup page lists `ads_mcp_management` for the server itself plus
  `ads_read` or `ads_management`: pick `ads_read`, never `ads_management`. With read-only rights the
  server can't change campaigns, budgets or ads whatever a prompt says
- **First run on a brand:** list the tools the server exposes and note which fail without
  `ads_management`. Pull the last 28 days at ad level and check it against an export of the same
  window. Log both, with no brand details, in `.claude/skills/ad-account-analysis/feedback.md`.
  The full test is in `brain-system/REWRITE-QUEUE.md`, section 10. Until the numbers match an
  export once, label MCP pulls "not yet checked against an export"
- If any exposed tool can write, never call it

**2. An Ads Manager export** at ad level, last 90 days, the columns in `data-access.md`, saved as
`source-pulls/ad-account-YYYY-MM-DD.csv`. Never edit the file; a new pull is a new dated file.

**3. A person pastes it,** for a single number or a small table. Label it Stated until an export
backs it.

**4. None of these:** the public-only path below.

## Calls

1. `ad-account-analysis`, process `measurement-check`. Its headline read decides what happens next:
   - **Numbers usable:** go on to Stage 1
   - **Usable with a caveat:** go on, and copy the caveat to the status page so every later stage
     carries it
   - **Not usable yet:** Stages 1 and 2 wait. Name the fix and who does it on the status page
     under "Open stops". Stages 3 and 4 can run meanwhile
2. `creative-leaderboard`, process `naming-setup`. A brand that keeps its own convention gets it
   mapped once in `running-notes/ad-naming.md`. Otherwise new ads follow
   `brain-system/system/ad-naming-convention.md` from Stage 6. Renaming live ads is the team's job
   in Ads Manager

## Outputs

`tool-map.md` (route and date), `audits/measurement-check-<YYYY-MM-DD>.md`, the winner definition
and north star in `running-notes/brand-rules.md`, `running-notes/ad-naming.md` when the brand keeps
its own names, and the Day 0 boxes ticked on the status page.

## Stops

- The person with access connects the account and signs in
- The strategist confirms the winner definition and north star
- A failed tracking check waits for the person who can fix it, often outside the team

## Exit check

- [ ] A route is written in `tool-map.md` with a date, and a first pull worked
- [ ] The measurement read is "usable" or "usable with a caveat", or Stage 0 stays open with the
      fix and its owner named
- [ ] The winner definition and north star are written in the brand's words
- [ ] Naming is settled: the brand's map, or our convention for new ads

## When access is partial

| What's missing | What to do |
|---|---|
| Events Manager or store numbers | Run `measurement-check` anyway; the missing controls are **unknown**, not fails. Ask once for the screenshots |
| The MCP route | Use an export. It is the default route anyway |
| An export, but the MCP works | Use the MCP, labelled as above until it has matched an export once |
| Both the MCP and an export | The public-only path |

**The public-only path.** It still gives a plan, and every number on it is a proxy, said out loud
(`data-access.md`, "No account access means proxies").
- **Stage 0:** `measurement-check` can't run. Mark it `skipped: no account access` and keep the
  access ask under "Open stops"
- **Stage 1:** a public read of the brand's own live ads in the Meta Ad Library, country set to
  the brand's market, through `persona-gap` Mode B. Share of ads stands in for share of spend.
  Label it Data-limited
- **Stage 2:** break down the brand's longest-running ads as "proxy winners (run time), not
  winners". Never call a winner from the Ad Library
- **Stages 3 and 4:** as normal. `angle-bank` `map-account` reads the Mode B tags; label the
  account side of the gap matrix Inferred
- **Stage 5:** the plan is provisional and says so on its first line
- **Stage 7:** the leaderboard and the weekly report need results. Mark them
  `skipped: no results data` and ask for a weekly export. Don't arm the weekly report routine
  without read access
- Ask for access again each time a stage closes. When it arrives, re-run Stages 0-2

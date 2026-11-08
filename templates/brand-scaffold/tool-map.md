# Tool map

Skills never name a product. They name a **role** ("the review tool", "the brief store"), and this
file says which tool fills that role at this brand and how Claude reaches it. When the employer or
client uses different software, only this file changes: the skills stay the same.

Fill it in during the first week. For each row, check what is actually connected: run
`/mcp` in a terminal session or ask Claude to list its connectors. Don't write a connector here
that you haven't seen working.

## Access levels

How Claude reaches a tool, best first. Use the best level that works and write it in the table.

1. **MCP / connector**: API access, fast and precise (e.g. Notion, Google Drive, Slack, Figma)
2. **Scraper service**: a paid scraper that fetches public data where the browser gets blocked
   (Reddit blocks bot traffic; Instagram and TikTok comments and reel transcripts are hard to reach).
   Apify is the common one: ready-made scrapers ("actors") reached through its official MCP server
   (github.com/apify/apify-mcp-server). Each actor has its own price, per result or per call, and
   Apify moves the rest to pay-per-usage on 1 Oct 2026: check the actor's price and run a small
   test before a routine depends on it. Public data only; never an actor that needs someone's login.
   **Not active in the lead's own brains** (no paid account, decided 2026-09-29): kept ready, not
   switched on. Until it is, routines skip the sources that need it and say so in their report. To
   activate: create the account, connect the MCP, run one small test, and fill in the table row below
3. **Export / local folder**: the tool syncs to a local folder or exports files (Drive for desktop,
   Dropbox, a CSV export from the PM board). Claude reads and writes the files
4. **Browser**: Claude drives the web app in the browser. Slow; use it for jobs that run
   unattended, and stop for anything behind a login or a CAPTCHA
5. **Human hand-off**: Claude prepares the output (comments, a CSV, a message) and the human
   pastes it in. Always works, and it's the fallback when access is missing

When Claude says it can't reach a source, ask once more for another way before settling for a lower
level: the first answer is often the quickest, not the only one.

## Roles

| Role | Used by | Tool at this brand | Access level | How (connector name / folder path / URL) | Checked (date) |
|---|---|---|---|---|---|
| Brief store: where briefs live | brief-check, video-edits | | | | |
| Raw footage: where creators upload | brief-check, video-edits | | | | |
| Review tool: where edits get comments | brief-check, edit-training (old comments) | | | | |
| Task board: concepts and their status | brief-check, creator-recruitment | | | | |
| Creator comms: how creators are contacted | creator-recruitment | | | | |
| Creator tracker: the roster and pipeline | creator-recruitment | `creators/tracker.csv` (default) | Local folder | | |
| Video editor: only if a human finishes edits | video-edits | None by default: edits render in Claude Code with ffmpeg, changes are re-renders (2026-10-09) | MP4 + `.srt` handover; FCPXML for DaVinci Resolve / Final Cut | | 2026-10-09 |
| Ad account: where ads launch (read-only for Claude) | account-playbook, ad-account-analysis, ad-breakdown, angle-bank, creative-leaderboard, weekly-creative-report | | Meta Ads MCP (`ads_read` only, never `ads_management`; local scope, token never in the repo) / export / pasted | | |
| Competitor ad library: rivals' live ads | competitor-ad-watch | Meta Ad Library (default; the data routes if connected) | Browser | facebook.com/ads/library, country Denmark, no login | |
| Customer language: reviews, forums, comments | customer-language-pull | Trustpilot and brand site (browser); Reddit, Instagram/TikTok comments (scraper service, e.g. Apify) | Browser / Scraper service | | |
| Swipe file: saved ads and static templates | static-ads, offer-ads | the lead's master library | Local folder | `brain-system/creative-strategy-context/swipe-library/` | 2026-09-29 |
| Team chat: where people get pinged | all | | | | |
| Email and SMS platform: flows, campaigns, consents | lifecycle-flows (drafts only) | | | | |
| Store platform: orders, products, checkout texts | lifecycle-flows, growth-plan, competitor-teardown (own store as comparison) | | | | |
| Site analytics: sessions, sources, conversion | growth-plan | | | | |
| AI assistants: ChatGPT, Google AI, Perplexity | ai-search | Built-in browser or Chrome (default), logged out where possible | Browser | | |

Examples of what goes in the "Tool at this brand" column: Notion / Google Docs / Airtable / Monday /
Asana for briefs and tasks; Google Drive / Dropbox / SharePoint for footage; Frame.io / Air /
Google Drive comments / Figma for review; CapCut / Premiere / DaVinci / Final Cut for editing.
For the competitor ad library, a paid ad-research tool (e.g. Gethookd) through its MCP, only if it's
connected and checked; show its price before signing up, and its rankings are still proxies, not spend.
For the ad account, a creative-reporting tool through its MCP (e.g. Adnova) can stand in for the
Ads Manager export, read-only, once it's connected and its numbers match an export for the same dates.

## Rules

- **Writing to a shared tool needs approval.** Posting comments, moving tasks, sending messages:
  the skill shows the draft first. The human can lift this for a single skill once its output has
  been right for a while. Write that down here, with the date:
  - _(none yet)_
- **Never paste logins into chat or into this file.** If a tool needs a login, the human logs in
  in the browser and Claude continues from there.
- **A role nobody has filled** means the skill falls back to human hand-off. Say so in the output;
  don't guess.

## Data routes (filled at the start of the build)

For each source the prompts read, which route this brand gives (see `brain-system/system/data-access.md`). One line each; "none" is an honest answer and becomes a gap in `running-notes/missing-context.md`.

| Source | Route (connector / export / public page / scraper / pasted) | Where it lands | Checked (date) |
|---|---|---|---|
| Own ad account (spend, results) | | `source-pulls/ad-account-<date>.csv` | |
| Rivals' ads | Meta Ad Library, browser | `audits/` | |
| Ad comments | | `source-pulls/` | |
| Customer reviews | | `source-pulls/` | |
| Post-purchase survey | | `source-pulls/` | |
| Reddit and forums | | `source-pulls/` | |
| Organic social | | `source-pulls/` | |
| Attribution tool | | `source-pulls/` | |
| Store orders (the source of truth for counts) | | `source-pulls/` | |
| Email and SMS platform (flows, list size, consents) | | `lifecycle/` | |

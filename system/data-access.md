---
summary: "How the brain reaches data without a managed data connection: for every data tool the prompts name, the route we use (export, public page, browser, scraper), what it can and can't show, and how the result is labelled."
---

# Data access

Origin: replaces the assistant's tool inventory (`data-access.md`), which describes the assistant's own data connection. Brand-brain has no such connection. The prompts and skills still name the tools they were written
against (`search_facebook_ads_sql` and so on); **wherever one is named, use the route in this table**, and record which routes this brain has in `tool-map.md`. A route that isn't available is a named
gap in `running-notes/missing-context.md`, never a guess.

## Routes, best first

Same ladder as `tool-roles.md`: a connector (an MCP the team has added) → an export the team drops in → a public page read in the browser → a scraper service (public data only, off until an account
exists) → a person pastes it in. Use the best that works.

## The map

| The prompts say | Route here | What it can't show | Label |
|---|---|---|---|
| `search_facebook_ads_sql`, `search_facebook_ads_semantic` (own ad account: spend, ROAS, hook rate, formats) | An Ads Manager export at ad level (CSV with spend, purchases, CPA, hook and hold rate, frequency, dates, creative names), saved as `source-pulls/ad-account-<date>.csv`; or Meta's Ads MCP server (`https://mcp.facebook.com/ads`), `ads_read` only, never `ads_management`, added at local scope so the token stays out of the repo, labelled "not yet checked against an export" until one pull matches an export (setup: `account-playbook` stage 0). Without either: the brand's own live ads from the public Ad Library | Public view has **no spend or results**; never rank or call a winner from it | Export: Verified (dated). Public view: Verified for what runs, Data-limited for performance |
| `search_competitor_facebook_ads` | The Meta Ad Library in the browser (country set to the brand's market, no login), method in `persona-gap` mode B: tag every ad, rank by impressions only within a start-date cohort | Spend, results, targeting | Verified for what runs; ranks are proxies, say so |
| `search_facebook_ad_comments_sql/semantic` | Comments export from Meta Business Suite or Ads Manager, or a copy of the comments on the ad's public post | Only what the team exports or what the page loads | Stated if pasted, Verified if exported with ids |
| `search_customer_reviews_sql/semantic` | The brand's review widget page or export (Judge.me, Loox, Yotpo, Stamped: CSV), plus Trustpilot read in the browser (200 most recent without login) | Trustpilot caps at 200; reviews are written after buying and rarely show the trigger | Verified with counts and date spread |
| `semantic_search_post_purchase_survey`, `lookup_post_purchase_survey` | The survey tool's export (Fairing, KnoCommerce, Shopify). If none exists: add the post-purchase question to `running-notes/missing-context.md` | Nothing without an export | Verified if exported |
| `search_reddit_posts_and_comments` | Reddit in the browser (search the category and the problem, read the threads, save quotes with url and date); a scraper service if one is on in `tool-map.md` | Search quality; no sampling guarantees, so no shares | Verified quotes, never shares |
| `search_and_manage_organic_social` | The brand's and rivals' public profiles in the browser; own analytics export for reach and saves | Rivals' reach and watch time | Verified for what is posted |
| `search_tiktok_videos`, `analyze_video_from_url` | TikTok search and Creative Center in the browser; for a video's words, transcribe it with the `video-edits` transcription step | Metrics beyond what the page shows | Verified for what is shown |
| `get_webpage` | Fetch or open the URL (browser if the page needs scripts) | Pages behind a login | Verified, dated |
| `search_swipe_file` | `creative-strategy-context/swipe-library/` and the team's own saved ads folder | Anything the team hasn't saved | Verified |
| `search_triple_whale_attribution`, `search_northbeam_attribution` | The tool's own export or dashboard screenshot from the team | Anything not exported | Stated until the export is saved |
| `list_custom_metrics` | The export's column names; ask the team which events count as a purchase | | |
| `brand_discovery` | `persona-gap` mode B on a rival's page, plus the competitive set in `competitors/_competitive-set.md` | | Inferred |
| `get_current_time` | The system date (`date`) | | |
| `get_available_brands`, `get_brand_persona` | This brain: `brain_config.json`, `CLAUDE.md`, `sub-context-docs/brand-profile-narrative.md`, `brand-lens.md` | | |
| `search_chat_history` | `git log`, `running-notes/current-work.md`, `running-notes/feedback.md` and the files in `sprints/`. Chat history isn't stored | What was only said aloud | |
| `update_custom_working_memory` | Write to `running-notes/` (or the doc that owns the fact), commit | | |
| `fetch_image` | Download the image to `assets/` or the run folder (browser or `curl`) | | |
| `update_parker_brain_setup_status`, `manage_insights_subscriptions` | Not used. Build progress lives in `BUILD-STATUS.md` | | |

## Rules

- **Check once, at the start of a build.** The runner asks which of these routes the brand can give (an ad-account export, a review export, a survey export, a connector) and writes the answer into
  `tool-map.md`. Prompts then run on those routes and name the missing ones in their output
- **An export is a dated file.** Save it under `source-pulls/` with the date in the name, never edit it, and cite it. A claim about the present tense uses the newest export and says its date
- **No account access means proxies, said out loud.** *Share of ads* stands in for *share of spend*, impression rank for reach, review mentions for customers. Every table states its limit in the table
- **Public data only, no logins.** Never log in, post, buy or submit a form to read a source. Where a site blocks automated reading, use the page as a person sees it and don't work around the block
- **Writing to a shared tool needs approval**, as in `tool-roles.md`
- **Light on the machine.** Read many pages with a small gathering agent that returns a short briefing (`model-routing.md`), not by pasting pages into the main conversation

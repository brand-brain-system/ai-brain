# Tool roles

Skills never name a product. They name a **role** ("the review tool", "the brief store", "the ad account"), and the brain's `tool-map.md` says which tool fills that role for this brand and how
Claude reaches it. When a client uses different software, only `tool-map.md` changes; the skills stay the same.

## Access levels, best first

1. **Connector / MCP:** API access, fast and precise (Notion, Drive, Slack, an ads platform)
2. **Scraper service:** a paid scraper for public data the browser can't reach (some forums, social comments). Check the price per result and run a small test first. Public data only, never anything that
   needs someone's login. Off by default until an account exists
3. **Export or local folder:** the tool syncs or exports files; Claude reads and writes them
4. **Browser:** Claude drives the web app. Slow; for unattended jobs; stop at a login or a CAPTCHA
5. **Human hand-off:** Claude prepares the output; a person pastes it in. Always works; the fallback

Use the best level that works and write it in the table. When Claude says it can't reach a source, ask once more for another way before settling for a lower level.

## Standard roles

Brief store · raw footage · review tool · task board · creator comms · creator tracker · video editor (if a person finishes) · ad account · competitor ad library · customer language sources ·
swipe file · team chat · email and SMS platform · store platform · site analytics · AI assistants. The scaffold's `tool-map.md` lists each with the skills that use it.

## Rules

- **Writing to a shared tool needs approval.** Skills show the draft first; a person can lift this per skill, in writing, with a date
- **Don't write a connector into the table that you haven't seen working**
- **Image and video generation** go through the generation tool named in `production.md`; every paid step shows its price first

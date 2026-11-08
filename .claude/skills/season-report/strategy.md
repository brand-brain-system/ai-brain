# Which mode

Pick by what the brain can see. Say the mode in the report's "How to read this report" box.

| Mode | When | What it delivers |
|---|---|---|
| **Full retro** | A daily, ad-level export for last year's season (`processes/data.md`) | Every study the export allows, the brand beside the cross-brand number, and the plan |
| **Short retro** | Only an ad-level export for the whole season (no daily rows) | Studies 2, 5, 6, 12 and 13 for the season as a whole (no CPM curve, no sale-week winners, no on/off dates, no day-7 read, no monthly gifting); the plan |
| **Public-only plan** | No account data: a new brand, a pitch, or a brand that won't share | The cross-brand findings, competitors' sale ads from the Ad Library (swipe-file rule in `brain-system/creative-strategy-context/black-friday-and-q4-data.md`), and the plan. Every account section is Data-limited. A pitch is labelled as concept |
| **One question** | Someone asks one thing ("when should Black Friday ads go live?") | That study only, in the section shape from `report-form.md`, in chat or as one page |

## Which season

- **Q4 (default):** Oct 1 to Dec 31 last year, with Jul 1 to Sep 30 as the baseline and January for the tail. Sale week: the brand's own sale dates if the brain has them (`strategy/`, an old offer
  brief in `sprints/`), otherwise Black Friday week as in the study (Thursday eight days before Black Friday to the Tuesday after Cyber Monday)
- **Other seasons** (Mother's Day, Father's Day, summer sale, mellemdagssalg): same studies, windows set from the brand's own sale dates. There is no cross-brand number to set beside them; say so, and
  compare with the brand's previous year instead if it exists

## Which sections

All on in a full retro. Drop a section only when the data can't support it, and list dropped sections in the methods file with the reason. Keep the numbering from `processes/studies.md` so reports from
different years line up.

## Before the first brand

Built 22 Oct 2026 from the cross-brand study and not yet run. Run it first on a test brand with a real export and log what broke in `feedback.md`.

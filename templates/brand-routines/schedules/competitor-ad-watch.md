# Competitor ad watch

```
Name:        competitor-ad-watch
Kind:        routine
Owner:       the strategist on this brand
Schedule:    weekly, Monday 07:00 (before the week's planning)
Skill:       prompt below
Reads:       sub-context-docs/competitive-landscape.md; the "Competitor ad library" role in tool-map.md
             (default: the public Meta Ad Library in the browser, no login)
Writes:      source-pulls/ad-library-<YYYY-MM-DD>.md; "Last seen" section in competitors/<rival>.md
Report:      max 5 lines in chat or a team-chat draft; one line "no changes" when nothing moved
Ends when:   n/a (routine)
Needs:       nothing beyond public data; works from day one without account access
Triggers:    not armed (template)
Started:     -
```

## Prompt

For the brand and each rival in `sub-context-docs/competitive-landscape.md`, open the Meta Ad Library
(country: Denmark, active ads) and compare with the most recent `source-pulls/ad-library-*.md`:

1. **New since last week:** each new ad, described so a reader can picture it: format, hook or
   headline, offer, visual, landing page.
2. **Still running:** ads that were already there last time, with their start date. Long runners
   are an outside signal of a winner, but it's a proxy: label it Inferred, never as
   performance. A stronger one in the EU: the library sorts by total impressions
   (`sort_data[mode]=total_impressions`). Record each ad's rank and compare ranks only among ads
   with the same start date; a campaign with a bigger budget gets more impressions regardless.
3. **Stopped:** ads from last week that are gone.
4. **Shifts:** a new offer, a new angle, a format they haven't used before, a seasonal push starting.

Describe what the rival is doing, not how this brand should copy it (source capture stays separate
from adaptation; see `CLAUDE.md`). Ideas it sparks go in the report as one line each, marked as ideas.

## Why it earns its keep

Answers "what are the competitors doing right now?" before anyone asks, and builds a dated history,
so "how long has that ad been running?" has an answer. It only reads public data, so it's the
safest routine to show a new employer first.

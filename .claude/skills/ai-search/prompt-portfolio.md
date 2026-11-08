# The prompt portfolio

Which questions you track decides what the numbers mean. A list full of easy definition questions
reports healthy visibility while the brand loses every shortlist that sells.

## Start from the decision

Write one line at the top of the portfolio: the decision these numbers will drive ("Are we on the
shortlist when Danish buyers ask for [category] for [situation]?"). Every prompt should bear on it.

## Where the questions come from (best first)

1. Questions customers say they asked ("what did you ask before you bought?" in a survey or interview)
2. The words in the voice of customer and the research map: the situation, the problem, the trigger
3. Search terms the brand already gets (Search Console, if the brand shares it), rewritten as
   someone would ask an assistant: a full sentence with their situation in it
4. Reviews and forum threads in the category, Danish ones first

Write in Danish, the way people type: "Hvad er den bedste hovedpude til nakkesmerter, når man sover
på siden?", not "hovedpude nakke". Don't translate an English list; Danish buyers compare on other
things (price in kroner, Danish delivery and returns, Danish test results, where to buy locally).

## Intent families

| Family | Shape (Danish) | Why it matters |
|---|---|---|
| Problem | "Hvordan slipper jeg af med [problem]?" | Early; does the answer name the product type at all? |
| Category, best for | "Hvad er den bedste [kategori] til [situation/persona]?" | The shortlist question. Weight it most |
| Comparison | "[Brand] eller [konkurrent]?", "alternativ til [konkurrent]" | Head to head |
| Trust | "Er [brand] godt?", "Hvad siger anmeldelserne om [brand]?" | What the answer says when someone already knows the name |
| Facts | "Hvad koster [brand/produkt]?", "Kan man returnere [brand]?", "Hvor kan man købe [produkt] i Danmark?" | Where wrong facts show up |
| Gift (if relevant) | "Gaveidé til [person] der [situation]" | Q4 and occasions |

Weight by business value: most prompts in "category, best for" and "comparison"; a few in the rest.

## Three cohorts

- **Core (15-25):** the set you report on. Changes only through a new version
- **Exploratory:** new situations, new rivals, seasonal questions. Rotates freely; promote a prompt to
  the core in the next version when it proves useful
- **Controls (2):** one where the brand should always appear (its own name plus the category) and one
  where it never should (an unrelated category). If either moves, the assistant changed, not the brand

Group the core prompts into **topics** (a buying situation: "neck pain, side sleeper") with 2-4
prompts each. Report by topic, not by single prompt.

## Versioning

The portfolio file starts with `version: N`, the date, and a change log line for every addition,
removal or rewording, with the reason. Compare two periods only on the prompts both share.

## Run log columns (`search-visibility/runs.csv`)

`date, portfolio_version, prompt_id, topic, cohort, assistant, run, mentioned, recommended, position,
competitors, cited_urls, wrong_facts, screenshot`

- `assistant`: chatgpt, google-aio, google-aimode, perplexity, gemini, copilot
- `run`: 1-3
- `mentioned`, `recommended`: yes / no. "Recommended" means on the list of suggestions the answer
  gives, not only named in passing
- `position`: the brand's place in that list, blank if not on it
- `competitors`: rivals named, separated by `;`, using the names in `competitors/_competitive-set.md`
- `cited_urls`: URLs the answer cites, separated by `;`
- `wrong_facts`: short note, blank if none
- `screenshot`: file name in `search-visibility/<date>/`

One run per row, never a summary row. The tally script reads exactly these columns.

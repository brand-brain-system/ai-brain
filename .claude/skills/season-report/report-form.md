# The report form

The form of the cross-brand Q4 report (`brain-system/creative-strategy-context/black-friday-and-q4-data.md`, "Where this came from"), made ours. It makes a data report readable for a busy reader and
checkable for a skeptical one. Other reports may point here; the form lives in this file.

## Two files

- **The report:** what a CMO or founder reads. Plain words, one idea per section
- **The methods file** ("How we built this report"): the data and its dates, the column mapping, every rule and threshold, the tag definitions and agreement rate, the dropped sections and why, the
  detailed tables, and the path to the calculation file. Each report section links to its part of the methods file

## The page, in order

1. **Cover:** the season, the brand, and four number tiles (ads that spent, spend, the sale week's dates, the season's dates)
2. **How to read this report:** a box of four short definitions: what's in it, what a winner is, the middle ad (median), and the dates. Plus the mode (`strategy.md`) and the one main limit
3. **What's inside:** the numbered list of sections
4. **The sections,** each in the same shape:
   - the number and name (e.g. "04 How fast winners showed")
   - **the finding as the headline,** one or two sentences, with the number in it ("Most of last year's winners were top spenders within 3 days.")
   - a short plain explanation: what we measured, in words a reader without Meta knowledge follows; define a term the first time it appears
   - number tiles for the two to four numbers that matter
   - **one chart or table,** with a caption that names the sample, the window and the definition. Groups under the size rule marked *
   - **beside it:** the cross-brand number, one line, labelled
   - **a "!" line:** what this number can't prove
   - a link: "How we measured this"
5. **TL;DR:** one line per section, the finding with its number
6. **Actions you could take:** the plan from `processes/plan.md`, short. Softly worded ("having … ready by …"), each tied to its section
7. **Limits:** what the data can't tell (who bought, profit, cause, placements), and the size of the sample

## Writing rules

- The headline says what happened, not what the section is about
- One idea per section; a second idea is a second section or the methods file
- Every number has its window and its denominator. Exact as calculated; shares to whole percent unless a smaller difference matters
- Plain words: "cost to show an ad 1,000 times (CPM)", "the middle ad", "made the top 10 %"
- Report what didn't hold as clearly as what did. A pattern that looked strong and didn't survive the re-run is a finding
- No evidence labels printed in the report; certainty in words ("our read is", "too few ads to say"). The methods file keeps the labels
- The brand's language for the report (the brain's `CLAUDE.md` header); the methods file may stay in English if the team reads it

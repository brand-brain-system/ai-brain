# Feedback log

What we've observed in AI-search runs: which assistants show which sources in Danish, which fixes
moved a topic, what broke in the browser. A log, not a rulebook: new lessons land here with a date,
and once confirmed on a second brand they move into `SKILL.md` (factory rule 6), leaving one line here
saying where they went. Brand-specific lessons go in the brain's `running-notes/feedback.md`.

## Open tests

- **31 Oct 2026, which Danish sources the answers cite.** The vendor studies behind the original
  skill are about US English answers (Reddit, G2, Wikipedia). For Danish product questions we expect
  price comparison sites, Danish retailers, Trustpilot, Forbrugerrådet Tænk tests and Danish media
  instead (Inferred, untested). Log the top cited domains from the first two brands' tallies and
  rewrite `SKILL.md` step 5's source kinds from what shows up
- **31 Oct 2026, three runs enough?** The skill runs each prompt 3 times per assistant. Check on the
  first brand how often the brand's recommendation flips between runs; if it flips often, raise to 5

## Log

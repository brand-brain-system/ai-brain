# Customer language pull

```
Name:        customer-language-pull
Kind:        routine
Owner:       the strategist on this brand
Schedule:    weekly, Wednesday 07:00 (every other week for a brand with few reviews)
Skill:       prompt below
Reads:       public reviews (Trustpilot, the brand's site); Reddit/forums in the category and public
             Instagram/TikTok comments, through the scraper service in tool-map.md when the browser
             is blocked; ad comments only if the "Ad account" or page access in tool-map.md allows it
Writes:      source-pulls/<source>-<YYYY-MM-DD>.md (verbatim); proposals appended to
             hypotheses/, marked "proposed by customer-language-pull"
Report:      max 5 lines; quiet ("nothing new") when there's no new language
Ends when:   n/a (routine)
Needs:       nothing for reviews; a scraper service (tool-map.md) for Reddit and social comments;
             not active yet, so skip those sources and name them in the report as skipped;
             page or ad-account access for comments on the brand's own ads
Triggers:    not armed (template)
Started:     -
```

## Prompt

Pull everything new since the last dated file in `source-pulls/` for each reachable source. Save it
verbatim (quote, source, date, product), as `source-pulls/README.md` describes. Then compare with
`personas/voice-of-customer/voice-of-customer.md` and report only what's new:

- **New phrases** customers use for the problem, the product or the result, quoted exactly
- **New objections or complaints**, and whether one is showing up more often than before
- **Trigger moments** ("I bought it when...") are rare in reviews: flag every one you find, and
  say which ranked entry moment in `personas/personas-profile.md` it adds to, or that it's a new one
- **A possible angle**, one line each, pointing to the quote it rests on

Don't rewrite `voice-of-customer.md`; propose changes in the report. A hypothesis goes in
`hypotheses/` as a proposal, never straight into `validations.md`.

## Why it earns its keep

Angles come from the customer's own words, not the team's guesses, and every idea can be traced
back to a quote. It keeps the voice-of-customer doc from going stale three months after onboarding.

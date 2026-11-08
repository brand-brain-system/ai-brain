# Creators

The brand's creator pool: who we know, who fits, and where each conversation stands. Filled by the
`creator-recruitment` skill and kept up to date by hand or by its optional check-in loop.

## Files

- `tracker.csv`: one row per creator. The only place creator details are stored
- `briefs-sent/`: add when the first collaboration starts. One file per collaboration, with the
  agreed terms (fee, deliverables, usage rights, marking)

## The approach, in one paragraph

The Danish market is small. A shortlist of 30-80 creators who fit, each with a written reason,
beats a scraped list of thousands. We build a community over time: creators who've done good work
once get the next brief first. The Danish legal rules the skill follows are in the skill's
`dansk-lovgivning.md`. The two that shape this folder: store only what the collaboration needs,
and delete creators who never replied (see "Retention" below).

## Tracker columns

| Column | Meaning |
|---|---|
| `handle` | Main profile handle |
| `platform` | TikTok / Instagram / YouTube / other |
| `profile_url` | Public profile link |
| `followers` | Rounded, with the date checked in `checked` |
| `niche` | What they make content about |
| `persona_fit` | Which persona in `personas/personas-profile.md` they'd speak to, and why (one line) |
| `evidence` | Link to 1-2 posts that show the fit |
| `business_contact` | Only a contact they publish for business inquiries. Never a private one |
| `status` | `shortlist` / `approved` / `contacted` / `replied` / `negotiating` / `booked` / `delivered` / `declined` / `no-reply` |
| `rate` | What they quoted, in DKK, once known |
| `last_contact` | Date |
| `next_step` | What happens next, and who does it |
| `quality` | After delivery: 1-5, and one line on why |
| `checked` | Date the row was last verified |
| `notes` | Anything else that matters for the next brief |

## Retention

- `shortlist` or `approved` and never contacted: delete after 6 months
- `no-reply` or `declined`: delete 6 months after `last_contact`
- `delivered`: keep while there's a working relationship

The 6 months is our own choice, not a legal number: GDPR asks us to keep personal data no longer
than necessary and to set a limit. Change it here if the employer has its own policy.

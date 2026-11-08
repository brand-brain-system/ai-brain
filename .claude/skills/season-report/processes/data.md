# The data

The routes are in `brain-system/system/data-access.md`; this is what the season report needs from them. Save every export under `source-pulls/` with the date in the name, never edit it, and write in
the methods file which file each section used.

## Ask for this, in one message

Exports from Meta Ads Manager (Reports, or the ads table exported), for the brand's account:

1. **Ad level, by day,** from 1 Jul to 31 Jan around the season (at least 1 Oct to 31 Jan). Columns: ad ID, ad name, campaign name, ad set name, day, amount spent, impressions, reach, purchases,
   purchase value, and the ad's created date if the export offers it
2. **Account level, by week, broken down by gender,** same dates: amount spent and impressions per gender
3. **The ads' words and type:** body text, headline, and whether each ad is an image, video or carousel. If the export can't carry them, a list from the team or the brand's own ads from the Ad Library
   (labelled as such)
4. **The sale itself:** the offer, its dates, and the dates of any other offer in the season (an old offer brief in `sprints/` may hold them)

Column names differ between Ads Manager versions. Check what the files hold before computing and write the mapping in the methods file. The currency is the account's; don't convert.

If the brand uses Northbeam or Triple Whale, take the Meta export anyway: the study picks winners by spend, which only Meta has per ad.

## What each section needs

| Section (`studies.md`) | Needs | Without it |
|---|---|---|
| 1 CPM by week | 1 or 2 | Data-limited |
| 2 Volume and hit rate | 1 (created date or first spend day) | Data-limited |
| 3 When sale ads went on | 1 + 3 (which ads name the sale) | Data-limited |
| 4 How fast winners showed | 1 | Data-limited |
| 5 New ideas or new takes | 3 for the season and the year before | Data-limited |
| 6 Deal types | 3 + 4 | From the brand's offer brief only, no performance |
| 7 What won the sale week | 1 + 3, with each ad tagged | Data-limited |
| 8 Cyber Monday | 1 + 3 | Data-limited |
| 9 When the sale stopped | 1 + 3 | Data-limited |
| 10 Audience shift | 2 | Data-limited |
| 11 Gifting | 1 + 3 | Data-limited |
| 12 Statics vs video | 1 + 3 (type) | Data-limited |
| 13 How winners opened | 1 + 3 | Data-limited |

## Launch date

The created date is the launch date when the export has it. Without it, use the first day with spend and say so in the methods file: an ad switched on long after it was made then looks new.

## Tagging the ads

Studies 5, 6, 7, 11, 12 and 13 need each ad tagged. Tag from the ad's words and, for the top spenders, the creative itself. One tag set, written in the methods file before tagging:

- **Deal:** none / percent off / money off / buy one get one / free gift / bundle / free shipping / code; the number if stated
- **Event named:** Black Friday / Black Week / Cyber Monday / Christmas / none
- **Kind:** offer ad (built around the deal), urgency (a deadline or "last chance"), founder, celebrity or creator with a following, single-creator UGC, hope-led (the outcome the buyer wants), plain
  headline static, benefit-list static, question headline, made to look like a social post, gifting (a gift, a giver or a recipient is the subject)
- **Format:** image, video, carousel
- **Opener:** teaches or reveals, starts a story, calls out who it's for, talks like a friend, leads with the deal, states the benefit, other

Tag with a small agent per batch of ads, then check a random 10 % by hand and write the agreement rate in the methods file. Below 80 %, fix the tag definitions and tag again.

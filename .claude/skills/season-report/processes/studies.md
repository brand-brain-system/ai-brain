# The studies, for one brand

Adapted from the cross-brand study's rules (`brain-system/creative-strategy-context/black-friday-and-q4-data.md`). The numbering matches that doc's findings so a reader can set them side by side. Every
rule here is ours and untested until the first run (`../feedback.md`).

## Shared rules

- **Winner:** an ad in the top 10 % of the brand's ads by spend in the window, with at least the minimum spend. The window needs 10+ ads with spend
- **Minimum spend:** the brand's own threshold if `running-notes/brand-rules.md` has one; otherwise 1 % of the brand's Meta spend in that window. Write the amount in the methods file. (The study used
  $2,500, too high for most Danish brands)
- **Made the top 10 %:** winners in a group ÷ ads with spend in that group, in that window. Compare a group with the brand's own rate for all ads in the window, as a ratio
- **Better or worse:** a ratio of 1.2 or more is better, 0.8 or less worse, in between "about the same". Only for groups that pass the size rule
- **Size rule:** a group with fewer than 30 ads with spend, or fewer than 5 winners, is shown with a * and not used for advice. Fewer than 10 ads: not shown
- **Re-run once another way** for every "better" or "worse": at the top 20 % (more winners), and for kinds of ads also with offer ads taken out. Say if the direction holds
- **Median, not average,** for anything per ad (spend, run length); say "the middle ad"
- **Spend is the only performance measure.** Purchases and value only for order size (study 6), and labelled Meta-reported

## 1. CPM by week

Weekly CPM = spend ÷ impressions × 1,000, Monday to Sunday, Jul 1 to Jan 31. Show the brand's curve, its own early October level (Oct 1-14) and each week as a ratio to it. Mark the sale week and the
cheapest week. **Beside it:** cross-brand +24 % the week before Black Friday week, +49 % in it, cheapest the week after Christmas. **Caveat:** CPM is the price of being seen, and the brand's own spend
changes move its CPM too.

## 2. Volume and hit rate

New ads = ads launched Oct 1 to Dec 31 (launch date: `data.md`). Count them, per week. Hit rate = share of new ads whose spend through Jan 31 passed the minimum spend, and the share passing 4 times
it. Ads that took half the season's spend: sort all ads with season spend, count until half the spend is covered. Median run of the winners (days with spend). **Beside it:** the cross-brand size group the
brand belongs to (finding 2), and `brain-system/creative-strategy-context/creative-volume.md`. **Caveat:** every ad ID counts; copies in new ad sets inflate the count.

## 3. When the sale ads went on

A sale ad is one whose words name the sale or carry its deal. The brand's on date = the first spend day of its first sale ad. For the sale week's winners: the first spend day of each, as a running share
by date ("a third were running by …"). Started small: winners that ran before the sale with daily spend under a quarter of their sale-week daily spend. **Beside it:** half of brands on by 10 days before
Black Friday, a third of winners running four weeks before. **Caveat:** an early winner may have run without the deal and had it added later; check the top few by hand.

## 4. How fast winners showed

For every ad launched in the season: the first day it was in the brand's top 10 % of spenders that day. For the season's winners, days from first spend to that day: share by day 1, 3, 7, 14. The day-7
test: of new ads that ran 7+ days, the share that became winners among those that were top spenders within 7 days, and among those that weren't. **Beside it:** 75 % by day 7; 34 % vs 2 %. **Caveat:**
Meta's early pick feeds itself; it doesn't prove a slow ad was bad.

## 5. New ideas or new takes

Read the season's new winners (up to 30, biggest first) beside the brand's earlier ads, oldest first. Each is one of: brand-new idea (angle, story or claim not in any earlier ad), new take (same idea, new
hook, edit, format, offer or translation), same words (identical words to an earlier ad). Also: the share of the season's winners made before Oct 1. **Beside it:** 18 % new, 54 % new takes, 27 % same
words; 31 % made before October. **Caveat:** judged by reading; a second reader on a sample of 10, agreement in the methods file.

## 6. Deal types and order size

Share of spend on ads with a deal, by deal type, and by depth for percent-off. Made the top 10 % by deal type, among the deal ads. Order size = Meta-reported purchase value ÷ purchases, by period (Oct,
Nov 1-19, sale week, Dec, Jan), only with 50+ purchases in the period. **Beside it:** percent off 62 % of deal spend; no deal type won inside brands; order size +3 % in the sale week. **Caveat:** one brand
usually runs one or two deal types, so this mostly can't compare types; say so instead of ranking them. Order size is Meta's own count.

## 7. What won the sale week

Made the top 10 % in the sale week by kind of ad (tags in `data.md`), as a ratio to the brand's sale-week rate, with the size rule and the re-run without offer ads. Also the whole sale period and the
whole season. **Beside it:** the table in finding 7. **Caveat:** an ad can carry several kinds; say how overlaps were counted.

## 8. Cyber Monday

Share of spend on the brand's top ads on the Monday and Tuesday after Black Friday by what they named: Black Friday or Black Week, Cyber Monday, a deal with no event, no deal. **Beside it:** Black Friday
wording 28 %, Cyber Monday 5 %.

## 9. When the sale stopped

Off date = last spend day of the brand's biggest sale ad; also the last spend day of any sale ad. Run length. Share of spend on deal ads by period: Oct 1-15, Nov 1-19, the sale week, Dec 3-20, Dec 26-31,
Jan 1-15. **Beside it:** half off by the day after Cyber Monday; deal share 15 % → 37 % → 22 %. **Caveat:** the Danish 30-day rule shapes December offers; read December deal share with the brand's own
offer dates.

## 10. Audience shift

Share of spend delivered to women by week, against the brand's own summer share (Jul-Sep). Name the group: usually men (35 % or less in summer), usually women (65 % or more), mixed. The weeks it moved
10+ points from summer. **Beside it:** usually-men brands 13 % → 30 % in early December → 17 % before Christmas. **Caveat:** who Meta reached, not who bought. Check against purchases by gender only if
the brand's shop data has it.

## 11. Gifting

Gifting ads' share of spend and of ads by month (as far back as the export goes), and made the top 10 % for gifting ads against the brand's other ads by month. **Beside it:** inside brands, gifting did
no better (finding 11). **Caveat:** usually few gifting ads; the size rule decides whether this is advice.

## 12. Statics vs video

Statics' share of spend by month; made the top 10 % for statics and videos over the season; in the sale week, split by deal / no deal. Share of the sale-week winners launched during the sale, by
format. The brand's single biggest ad of the season and its format. **Beside it:** statics 3.7 % vs video 5.3 %; with a deal 13.4 % vs 13.2 %. **Caveat:** video runs in more placements.

## 13. How winners opened

The opener tag for the season's winners, by format, as shares. **Add the base rate:** the same shares for all ads with spend, so the table shows whether winners opened differently from what the brand
made. The cross-brand study lacked this. **Beside it:** video teaches or reveals 15 %; statics lead with the deal 28 %, the benefit 20 %. **Caveat:** a pattern among winners, not a cause.

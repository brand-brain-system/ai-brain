# Offer (Q4 library): prompts

74 offer ads from the Black Friday / Cyber Monday / holiday window, picked by Alex Cooper from
Parker's Meta ad library pull (12-16 Sep 2026, selected by impressions within that pull: a sign of
spend, not proof of results). Mostly US brands and US price devices.

**The prompt for each template is in its card** (`cards/oq-NNN.md`, "Prompt skeleton"), together
with the layout forensics, the story, the copy skeleton (word budget per zone) and adaptation notes.
Build the final prompt from it per `../production.md`.

- **Danish price rules first.** "Was/now", strikethrough, "save X" and percentage devices only with a
  documented lowest price from the last 30 days (`offer-ads/offer-copy.md`). Without one, take
  the card's own swap to a gift, bundle or free-shipping offer, or skip the template
- **Reference image:** `thumbs/` holds a 236 × 420 preview. Fetch the full-size ad from the card's
  `image_url` only for a template the run picks, save it in the run folder, and crop out the original
  brand before attaching it as a layout reference (or leave it out when its text would leak)
- **Only real offers:** no invented discounts, gifts, deadlines or stock limits

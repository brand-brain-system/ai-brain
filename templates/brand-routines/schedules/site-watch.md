# Site watch

```
Name:        site-watch
Kind:        routine
Owner:       the strategist on this brand
Schedule:    daily, <TIME> Europe/Copenhagen (fill in when armed; send even when nothing changed)
Skill:       prompt below; captures with brain-system/scripts/site-capture.mjs and stitch.py
Reads:       the brand's (or a rival's) public website on a phone; source-pulls/site-watch/pages.json
Writes:      source-pulls/site-watch/ (latest/, previous/, archive/, diffs/, reports/)
Report:      a short summary in chat every day, before/after images only for real visual changes
Ends when:   n/a (routine)
Needs:       nothing beyond the public site; Node and Python with Pillow on the machine that runs it
Triggers:    not armed (template)
Started:     -
```

the lead's daily website monitor prompt (2026), fitted to the brain's folders. It watches the
brand's own site, or a competitor's (one brain per brand watched; a rival's site goes in that
rival's brain, or in `competitors/<rival>/site-watch/`).

## Set up once

1. Fill `source-pulls/site-watch/pages.json` with the shopping path, priority pages first:
   ```json
   [
     {"name": "home", "url": "https://..."},
     {"name": "collections", "url": "https://.../collections/all"},
     {"name": "<product>", "url": "https://.../products/<product>"},
     {"name": "<landing-or-offer-page>", "url": "https://..."}
   ]
   ```
   Names become file names and stay the same every day (`home.png`, `<product>.png`)
2. Write down the cart step: which product and option (e.g. subscription) goes in the cart, and any
   quiz URL. Put them in `source-pulls/site-watch/README.md`
3. **First run = baseline.** Capture every page, send the human three sample screenshots and the page
   list to approve, and start comparing the next day

## Prompt

Shop the site on a phone the way a normal customer would, screenshot every page on the shopping path,
compare each one with the day before, and send a short summary of what changed. Send it every day,
even when nothing changed.

**1. Move yesterday aside.** Move `latest/` to `previous/` (replacing the old `previous/`). Always
take fresh screenshots from the live site; never reuse earlier files.

**2. Capture the pages.** From the brain folder:
`node brain-system/scripts/site-capture.mjs source-pulls/site-watch/pages.json source-pulls/site-watch/latest`
It keeps a 390 × 844 phone viewport (the same width every day, or every page looks "changed"),
scrolls slowly to the bottom and back so lazy images, reviews and logos load, removes cookie walls
and pop-ups (not the promo bar), captures the full page from the promo bar to the footer in pieces
and stitches them (pages taller than ~8,192 px still reach the footer), and writes per page a `.png`,
the raw `.html` and a `.json` of facts. Then look at each image: grey placeholders where images or
reviews should be, or an image that stops before the footer, means run that page again.

**3. Quiz and cart, by hand in the browser** (the built-in browser at 390 × 844, or the Chrome
extension):
- Quiz: quizzes reset during a full-page capture. Take a viewport screenshot of the landing screen
  and the first two steps, picking the first answer each time (`latest/quiz-step0.png` to `step2`)
- Cart: empty it first, then add exactly 1 of the product and option from the README, so quantities
  don't pile up. Screenshot the cart (`latest/cart.png`) and note the line items and prices.
  **Never go to checkout, enter personal or payment details, or buy anything**

**4. Write down the facts per page** (compare text, not just pixels). The `.json` files hold most of
it; check them against the screenshot and add what's missing:
- The exact promo or announcement bar text. Reload 2-3 times and search the saved `.html` for other
  promo text: note which version showed, and which are A/B alternates in the code
- The home hero headline, subheadline and main button text
- Product names, the price of every option (subscription, multi-pack, one-time), strikethrough prices
  and discount badges
- Review counts, star ratings and trust-badge numbers
- Free gifts, bundle contents, savings claims, guarantee and free-shipping thresholds
- Main product claims, and any new, missing or renamed products or sections
- Any 404s (`http_status`), errors or broken images (`broken_images`)

Save them to `reports/<YYYY-MM-DD>.md`, so tomorrow's run compares text against text.

**5. Compare.** Today's facts against yesterday's report first, then the screenshots for visual
changes (new images, layout shifts, moved sections). Separate real changes from noise:
capture-width differences, stitching problems, lazy-load placeholders and leftover cart quantities
are noise. A small review-count bump is minor: mention it, don't lead with it. For each real visual
change, make a cropped before/after:
`python brain-system/scripts/stitch.py --side previous/<page>.png latest/<page>.png diffs/<YYYY-MM-DD>/<page>-<what>.png --top <y> --height <h>`

**6. Archive.** Copy `latest/` to `archive/<YYYY-MM-DD>-mobile/`.

**7. Daily summary (in chat).**
- Lead with the most important change: a new promo, price, offer, gift, headline, button or product.
  On quiet days, start with "No meaningful changes today."
- Then the smaller changes (review counts, badge numbers), each with the old and new value
- Then a short confirmation of what stayed the same (promo bar, hero, prices, quiz, cart total), so
  the reader knows it was checked
- Capture problems in one line
- Attach before/after images for real visual changes only. Short, plain English

Describe what changed, not what the brand should do about it. An idea it sparks goes in as one line,
marked as an idea; a competitor's new offer worth reacting to goes in `running-notes/current-work.md`.

## Files

```
source-pulls/site-watch/
  pages.json, README.md          the page list, the cart and quiz steps
  latest/                        today's captures, same file names every day
  previous/                      yesterday's captures
  archive/YYYY-MM-DD-mobile/     a permanent copy of each day
  diffs/YYYY-MM-DD/              before/after side-by-sides of what changed
  reports/YYYY-MM-DD.md          the day's facts and summary
```

The archive grows by roughly 1-3 MB per page per day. Keep it out of a shared git repo (add
`source-pulls/site-watch/archive/` to `.gitignore`) and thin it to one day a week after three months.

## Why it earns its keep

Offers, prices and headlines on a brand's site change quietly; a dated record answers "when did they
start that offer?" and "what was the price before Black Friday?" (the 30-day lowest price the Danish
price rules ask for). It reads public pages only and never buys or logs in, so it's safe to run from
day one. Tested on 6 Oct 2026: a 3,438 px phone page captured to the footer in 17 seconds.

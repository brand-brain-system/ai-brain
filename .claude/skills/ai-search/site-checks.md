# Site checks

Read-only checks on the brand's own site. Each finding gets a label: Verified (seen, with the URL and
date), Data-limited (needs access the skill doesn't have, such as Search Console or Merchant Center).
Google's position (its guide on AI features, Stated): there is no special markup or file needed for
AI Overviews and AI Mode; they rest on the same ranking as ordinary search. So these checks are
ordinary good practice first. The other assistants read the same pages.

## 1. Can the bots reach the pages?

Open `/robots.txt` and the response the shop's firewall or CDN gives. Bots have different jobs, so
check them one by one, not as one group:
- **Search and answer bots** (they decide whether the brand can be found and cited): Googlebot,
  Bingbot, `OAI-SearchBot` (ChatGPT search), `PerplexityBot`, `Claude-SearchBot`
- **Fetch-on-request bots** (a user's assistant opening a page): `ChatGPT-User`, `Perplexity-User`,
  `Claude-User`
- **Training bots** (blocking them is a business choice, not a visibility fix): `GPTBot`, `ClaudeBot`,
  `Google-Extended` (Gemini training; does not affect Google Search)

A rule for a named bot replaces the `*` rules for that bot. Flag any search or answer bot that is
blocked by accident. The brand decides about training bots; note the choice, don't make it.

## 2. Are the facts readable as text?

On the main product pages, view the page without JavaScript (or the page source) and check that these
are in the HTML as text, not only in images or loaded by a widget: product name, price in kroner,
sizes or variants, what it is made of or contains, delivery time, return terms, the guarantee, and
the review rating and count. If you can't select it with the mouse, an assistant may not read it.

## 3. Structured data

In the page source, look for JSON-LD of type `Product` (name, image, brand, offers with price,
priceCurrency `DKK`, availability) and, where the brand shows reviews, `AggregateRating` that matches
the visible rating. `Organization` on the front page with the brand name, logo and its official
profiles. Test one page in Google's Rich Results Test. Flag markup that claims ratings not shown on
the page: that is misleading markup, not a quick win.

## 4. Product feed and shopping surfaces

Ask the human whether the brand has a Google Merchant Center feed and whether it is approved
(Data-limited without access). For a Shopify store, the catalog itself is read by shopping agents:
titles, descriptions, variants, GTIN and prices should be complete and match the product pages. A
mismatch between feed, page and markup is a top fix.

## 5. Indexed at all?

Search Google for `site:<domain>` and for the brand name. Missing product pages, an old domain still
ranking, or a retailer outranking the brand's own page for its own product name go in the readout.

## 6. Optional extras

`/llms.txt` (a short plain-text map of the site for AI tools) is cheap and harmless; no assistant has
said it ranks by it. Don't spend a fix-list slot on it before 1-5 are clean.

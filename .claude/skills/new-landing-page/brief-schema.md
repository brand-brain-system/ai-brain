# Brief schema

The brief is two files in the run folder: `brief.md` (readable, every field with its source) and `brief.json` (what the scripts read). Fill both. A field's source is a doc path and line, or "stated by <name>, <date>" when the reviewer typed it. Nothing is guessed; a missing field is asked for once.

## Fields (`brief.json`)

```json
{
  "brand_name": "Brand",
  "what_it_is": "one line on the product, in the brand's own terms",
  "external": false,
  "template": "lp-01",
  "cta_url": "https://brand.com/products/hero?discount=CODE",

  "angle": "what the page sells and to whom, in one line (from the ask, or proposed from the evidence)",
  "ad": {
    "source": "Parker ad link, ad name, or 'described by <name>, <date>'",
    "hook": "the ad's opening line or headline, verbatim",
    "angle": "what the ad promises, in one line",
    "person": "who the ad speaks to (age, situation), if it names one",
    "offer_in_ad": "the offer exactly as the ad states it"
  },

  "products": [
    {"name": "Hero product, size", "one_time_price": "$65", "subscription_price": "$48", "unit": "bag", "per_use": "$1.71 a day"}
  ],
  "offer": {
    "mechanics": ["Percent off", "Free gift", "Subscription"],
    "headline_number": "[OFFER]",
    "code": null,
    "auto_applied": false,
    "dates": null,
    "guarantee": "30-day money-back guarantee",
    "gifts": [{"name": "Shaker", "value": "$15"}],
    "options": [{"label": "Subscribe", "price": "$48", "anchor": "$65"}, {"label": "One time", "price": "$65"}]
  },

  "claims": {
    "allowlist": ["$48", "$65", "$15", "30-day", "30 days"],
    "banlist": ["review_count", "press", "efficacy stats"],
    "reviews": [{"quote": "verbatim", "name": "Reviewer N.", "detail": "rating, platform, date", "source": "doc or pull"}],
    "stats": [{"number": "84%", "label": "what it measures", "source": "study or doc"}],
    "press": [],
    "experts": [{"name": "Dr. Name", "credential": "title", "relationship": "advisor / reviewer / customer", "source": "doc"}],
    "rivals": [{"name": "Rival or 'typical category product'", "facts": [{"claim": "price per serving $2.10", "source": "their site, date"}]}],
    "health_wording": "the claim wording the brand may use",
    "positioning_rails": ["rules the brand's lens sets"]
  },

  "story": {
    "founder": "the founder story in the brand's own words, with source, if the template needs it",
    "mechanism": "why the product works, in the brand's approved wording",
    "objections": ["the 4-8 things buyers say before they buy, from reviews, comments and support"],
    "timeline": [{"when": "Week 1", "what": "only what the brand may claim"}]
  },
  "voc": {
    "bank": [{"phrase": "verbatim words a customer used", "kind": "pain | outcome | objection | trigger | metaphor | identity", "source": "review Name, date | ad comment, date | survey | reddit | tiktok", "theme_count": "1,109 of 41,883 (keywords: ...)"}],
    "pains": ["verbatim phrases"],
    "outcomes": ["verbatim phrases"],
    "pulls": ["each Parker pull made: tool, query, count, date"],
    "not_connected": ["sources Parker could not reach for this brand, and what they would add"]
  },

  "voice_rules": {
    "kill_list": ["em dashes", "that's not X, that's Y", "no X, no Y, just Z", "invented reviews, counts or press"],
    "register": "how the brand sounds; any pack or site lines usable verbatim"
  },
  "urgency_allowed": false,
  "audience": "who lands on this page: the angle's buyer, from personas and the account's demographics",

  "assets": {
    "photos": [{"file": "assets/packshot.jpg", "shows": "one pouch on white", "source": "brand asset folder"}],
    "needed": ["lifestyle photo for the hero", "founder portrait"]
  },
  "tokens": {
    "palette": {"bg": "#ffffff", "ink": "#1a1a1a", "muted": "#6b6b6b", "accent": "#0b6b4f", "accent_ink": "#ffffff", "soft": "#f4f2ee", "line": "#e6e3dd"},
    "fonts": {"heading": "Fraunces", "body": "Inter"},
    "logo": {"text": "BRAND", "src": null}
  }
}
```

Field notes:

- `cta_url` is the one link every button uses. Ask for the version with the offer already applied; if the brand cannot do that, say so in the handoff.
- `angle` is required; `ad` is optional and null unless the reviewer named an ad (never ask for one). When present, `ad` is what makes message match checkable. `hook` and `offer_in_ad` are verbatim. If the reviewer gives a Parker ad link, pull it; never reconstruct an ad from memory.
- `claims.allowlist` is matched as substrings after removing commas: write each number the way it will appear on the page. Every number in `offer`, `products`, `gifts`, `stats` and `rivals` must also be on the allowlist, or the check fails.
- `claims.reviews` are verbatim, never shortened. The check compares every quote in a reviews section against this list.
- `voc.bank` is the raw material for the page's own words. 30 or more phrases from at least three sources where the brand has them; each keeps its source, date and theme count. Lines built from it are traced in `page.json` (see `write-page-copy.md`).
- `rivals` facts need a source and a date. A comparison against "typical [category]" still needs facts the brand can back.
- `tokens.fonts` are Google Fonts family names (the page loads them from there). Pick the closest match to the brand's own type and say so in `brief.md`. `palette.accent` is the button colour.
- `assets.photos` are files in the run's `assets/` folder. A published board cannot show images from another site, so photos are always local.
- Extra keys are fine; the scripts ignore what they do not read.

## Auto-fill map for a brand brain

Paths are inside the brand's brain. Open each file: not every brain has every doc, and line numbers move.

**In our brains, read these instead of the Parker doc names in the table:**
products, prices, offer, guarantee, mechanism, founder story → `sub-context-docs/brand-profile-narrative.md`; voice, kill list,
claims allowlist and banlist, review count, rating, press → `brand-lens.md` (claims gate and proof
inventory); palette, fonts, logo, photo style → `sub-context-docs/visual-vocabulary.md` and `assets/`;
audience and objections → `personas/`; verbatim reviews and the customer-voice bank →
`source-pulls/`; rivals → `competitors/`. The one-page summary is `brand-context/brand-one-pager.md`.

| Field | Source |
|---|---|
| products, prices, per-use maths, gifts, options, cta_url | `sub-context-docs/website-and-product-audit.md` |
| guarantee, positioning_rails, kill_list, register, palette, logo, fonts | `brand-lens.md`, `CLAUDE.md` hard rules, `running-notes/brand-rules.md`, `sub-context-docs/visual-vocabulary.md` |
| claims.allowlist, banlist, health_wording, stats, press, experts | the brain's claims ledger if it has one, else `brand-lens.md` and `brand-identity-analysis.md`; everything not on record is out |
| claims.reviews, voc, story.objections | `personas/voice-of-customer/`, plus live Parker pulls: `search_customer_reviews_semantic`, `search_facebook_ad_comments_semantic` |
| story.founder, story.mechanism | `sub-context-docs/visual-vocabulary.md`, `website-and-product-audit.md` |
| rivals | `competitors/` profiles; facts re-checked against the rival's own site on the day |
| ad | a Parker `search_facebook_ads_sql` pull of the named ad (`adIds`), or the account's top ads by spend for the product if the reviewer says "the winners" |
| audience | `personas/`, `sub-context-docs/ad-account-evaluation.md`, a named ad's demographics, if any |
| urgency_allowed | the brand's stated rule in `brand-lens.md` or `running-notes/brand-rules.md` |
| offer number, code, dates | almost never on record: `[OFFER]` until the reviewer states it |

## What gets asked, and how

One message, every missing field, with the reason each matters ("without a sourced rival price the comparison table drops"). The minimum viable brief: what it sells, one price, the offer, the button link, what it may not claim, whether urgency is fine, and at least one product photo. Everything else has a safe default: no reviews section, no stats, no press, labelled photo boxes.

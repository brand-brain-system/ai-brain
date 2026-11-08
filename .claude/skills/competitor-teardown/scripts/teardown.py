#!/usr/bin/env python3
"""Public, dated evidence for a competitor teardown. Stdlib only.

    python3 teardown.py catalog <domain> [--out catalog.csv] [--pages 20]
    python3 teardown.py stack   <domain> [--months 24]
    python3 teardown.py hero    <url>    [--months 24]
    python3 teardown.py ads     <name>   [--domain <domain>]

catalog  A Shopify store's public /products.json: every listed product with the date it was
         added, its price range and whether any variant has a compare-at price above the price.
         Prints launches per month, the share on sale, and the store's own best-selling order.
stack    Monthly Wayback Machine captures of the front page: the first and last month each
         known tool's script appears (pixels, email, reviews, payments). Dated moves.
hero     Monthly captures of one URL: the months its title, first headline or meta description
         changed (positioning shifts, sale banners in the title).
ads      Links to the rival's ads in the Meta Ad Library (Denmark) and Google's transparency center.

Everything prints as JSON with the pull date, so the numbers can be rechecked. The script asks
politely (an honest user agent, a pause between archive requests) and stops on a block (403, 429)
instead of working around it. Evidence: what it finds is Verified for the capture it came from;
a tool's first month is when it first shows in the archive, not when it was installed.
"""
import argparse
import csv
import datetime as dt
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "Brand-brain competitor research (public pages; contact via the brand that runs it)"
ARCHIVE_PAUSE = 1.5  # seconds between Wayback requests; rule 7, and the archive is a shared resource

# (tool, group, pattern). Patterns match script and link URLs in the page source.
TOOLS = [
    ("Shopify", "store", r"cdn\.shopify\.com|myshopify\.com"),
    ("WooCommerce", "store", r"woocommerce"),
    ("Meta pixel", "ads", r"connect\.facebook\.net/[^\"']*fbevents|fbq\("),
    ("TikTok pixel", "ads", r"analytics\.tiktok\.com"),
    ("Google Ads", "ads", r"googleadservices\.com|AW-\d{6,}"),
    ("Pinterest tag", "ads", r"s\.pinimg\.com/ct|pintrk\("),
    ("Snap pixel", "ads", r"sc-static\.net/scevent"),
    ("Google Tag Manager", "analytics", r"googletagmanager\.com/gtm\.js"),
    ("Google Analytics 4", "analytics", r"googletagmanager\.com/gtag/js\?id=G-"),
    ("Hotjar", "analytics", r"static\.hotjar\.com"),
    ("Microsoft Clarity", "analytics", r"clarity\.ms"),
    ("Klaviyo", "lifecycle", r"klaviyo\.com"),
    ("Rule", "lifecycle", r"rule\.io|rulemailer"),
    ("Mailchimp", "lifecycle", r"list-manage\.com|chimpstatic\.com"),
    ("Omnisend", "lifecycle", r"omnisnippet|omnisend\.com"),
    ("Privy", "lifecycle", r"privy\.com"),
    ("Trustpilot widget", "reviews", r"widget\.trustpilot\.com"),
    ("Judge.me", "reviews", r"judge\.me"),
    ("Yotpo", "reviews", r"yotpo\.com"),
    ("Okendo", "reviews", r"okendo\.io"),
    ("Recharge", "subscriptions", r"rechargepayments\.com|rechargecdn"),
    ("Skio", "subscriptions", r"skio\.com"),
    ("Rebuy", "upsell", r"rebuyengine\.com"),
    ("Gorgias", "support", r"gorgias\.(chat|io)"),
    ("Klarna", "payments", r"klarna"),
    ("ViaBill", "payments", r"viabill"),
    ("MobilePay", "payments", r"mobilepay"),
    ("Cookiebot", "consent", r"cookiebot\.com"),
    ("Cookie Information", "consent", r"cookieinformation\.com"),
]


def today() -> str:
    return dt.date.today().isoformat()


class Blocked(Exception):
    pass


def get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=30) as res:
            charset = res.headers.get_content_charset() or "utf-8"
            return res.read().decode(charset, errors="replace")
    except urllib.error.HTTPError as err:
        if err.code in (401, 403, 429):
            raise Blocked(f"{err.code} from {url}: the site or archive said no. Stop here, don't work around it")
        raise


def detect(source: str) -> list[str]:
    return [tool for tool, _, pattern in TOOLS if re.search(pattern, source, re.I)]


def monthly_captures(url: str, months: int) -> list[tuple[str, str]]:
    start = (dt.date.today() - dt.timedelta(days=31 * months)).strftime("%Y%m")
    query = urllib.parse.urlencode({
        "url": url, "output": "json", "from": start, "filter": "statuscode:200",
        "collapse": "timestamp:6", "fl": "timestamp,original"})
    rows = json.loads(get(f"https://web.archive.org/cdx/search/cdx?{query}") or "[]")
    return [(r[0], r[1]) for r in rows[1:]]


def archived(timestamp: str, original: str) -> str:
    return get(f"https://web.archive.org/web/{timestamp}id_/{original}")


def month_of(timestamp: str) -> str:
    return f"{timestamp[:4]}-{timestamp[4:6]}"


def cmd_catalog(domain: str, out: str | None, pages: int) -> dict:
    products, complete, stopped = [], False, None
    for page in range(1, pages + 1):
        try:
            data = json.loads(get(f"https://{domain}/products.json?limit=250&page={page}"))
        except (urllib.error.HTTPError, json.JSONDecodeError) as err:
            if page == 1:
                sys.exit(f"products.json not readable on {domain} ({err}). Not a Shopify store, or it's switched off")
            stopped = f"page {page}: {err}"
            break
        if not data.get("products"):
            complete = True
            break
        products += data["products"]
        time.sleep(0.5)
    rows = []
    for p in products:
        variants = p.get("variants") or []
        prices = [float(v["price"]) for v in variants if v.get("price")]
        compare = [float(v["compare_at_price"]) for v in variants if v.get("compare_at_price")]
        on_sale = any(v.get("compare_at_price") and float(v["compare_at_price"]) > float(v["price"])
                      for v in variants if v.get("price"))
        rows.append({
            "handle": p.get("handle", ""), "title": p.get("title", ""), "type": p.get("product_type", ""),
            "created": (p.get("created_at") or "")[:10], "published": (p.get("published_at") or "")[:10],
            "min_price": min(prices) if prices else "", "max_price": max(prices) if prices else "",
            "max_compare_at": max(compare) if compare else "", "on_sale": on_sale, "variants": len(variants)})
    if out:
        with open(out, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0]) if rows else ["handle"])
            writer.writeheader()
            writer.writerows(rows)
    by_month: dict[str, int] = {}
    for r in rows:
        if r["created"]:
            by_month[r["created"][:7]] = by_month.get(r["created"][:7], 0) + 1
    try:
        page = get(f"https://{domain}/collections/all?sort_by=best-selling")
        seen = []
        for handle in re.findall(r"/products/([a-z0-9][a-z0-9-]*)", page, re.I):
            if handle.lower() not in seen:
                seen.append(handle.lower())
        bestsellers = seen[:30]
    except (urllib.error.HTTPError, urllib.error.URLError):
        bestsellers = []
    result = {
        "domain": domain, "pulled": today(), "products": len(rows), "complete": complete,
        "on_sale": sum(1 for r in rows if r["on_sale"]),
        "added_by_month": dict(sorted(by_month.items())),
        "bestsellers_in_order": bestsellers,
        "note": ("created = when the product was added to the store; published can be reset by a relaunch. "
                 "on_sale = a variant's compare-at price is above its price, which says nothing about whether "
                 "that before-price is lawful. Best-selling order is the store's own sort, which some themes "
                 "override. Hidden products are not listed."),
    }
    if stopped:
        result["stopped_at"] = stopped
    elif not complete:
        result["truncated_at_pages"] = pages
    return result


def cmd_stack(domain: str, months: int) -> dict:
    captures = monthly_captures(f"{domain}/", months)
    first, last, failed = {}, {}, []
    for timestamp, original in captures:
        try:
            for tool in detect(archived(timestamp, original)):
                first.setdefault(tool, month_of(timestamp))
                last[tool] = month_of(timestamp)
        except (urllib.error.HTTPError, urllib.error.URLError):
            failed.append(timestamp)
        time.sleep(ARCHIVE_PAUSE)
    try:
        live = detect(get(f"https://{domain}/"))
    except (urllib.error.HTTPError, urllib.error.URLError):
        live = []
    start = month_of(captures[0][0]) if captures else None
    tools = [{"tool": tool, "group": group, "first_seen": first.get(tool), "present_at_start": first.get(tool) == start,
              "last_seen_archive": last.get(tool), "live_now": tool in live}
             for tool, group, _ in TOOLS if tool in first or tool in live]
    return {"domain": domain, "pulled": today(), "captures": len(captures), "failed_captures": failed,
            "tools": tools,
            "note": ("first_seen is the first monthly capture with the tool's script; it may be older. "
                     "Tools loaded through a tag manager or only after cookie consent don't show, so "
                     "live_now false is not proof the tool is absent.")}


def hero_of(source: str) -> dict:
    def first(pattern: str) -> str:
        m = re.search(pattern, source, re.I | re.S)
        return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", m.group(1)))).strip() if m else ""
    return {"title": first(r"<title[^>]*>(.*?)</title>"), "h1": first(r"<h1[^>]*>(.*?)</h1>"),
            "description": first(r"<meta[^>]+name=[\"']description[\"'][^>]+content=[\"']([^\"']*)")}


def cmd_hero(url: str, months: int) -> dict:
    changes, previous = [], None
    for timestamp, original in monthly_captures(url, months):
        try:
            hero = hero_of(archived(timestamp, original))
        except (urllib.error.HTTPError, urllib.error.URLError):
            continue
        signature = (hero["title"], hero["h1"], hero["description"])
        if any(signature) and signature != previous:
            changes.append({"month": month_of(timestamp),
                            "capture": f"https://web.archive.org/web/{timestamp}/{original}", **hero})
            previous = signature
        time.sleep(ARCHIVE_PAUSE)
    return {"url": url, "pulled": today(), "changes": changes,
            "note": "Rows are months where the title, first headline or meta description changed. Open the capture to see the page."}


def cmd_ads(name: str, domain: str | None) -> dict:
    q = urllib.parse.quote(name)
    return {"name": name, "pulled": today(),
            "meta_ad_library": ("https://www.facebook.com/ads/library/?active_status=all&ad_type=all"
                                f"&country=DK&q={q}&search_type=keyword_unordered"),
            "google_ads_transparency": f"https://adstransparency.google.com/?region=DK&domain={urllib.parse.quote(domain or name)}",
            "note": "The libraries show what runs, never how it performs (brain-system/system/evidence-and-labels.md)."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("catalog"); p.add_argument("domain"); p.add_argument("--out"); p.add_argument("--pages", type=int, default=20)
    p = sub.add_parser("stack"); p.add_argument("domain"); p.add_argument("--months", type=int, default=24)
    p = sub.add_parser("hero"); p.add_argument("url"); p.add_argument("--months", type=int, default=24)
    p = sub.add_parser("ads"); p.add_argument("name"); p.add_argument("--domain")
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")  # Danish letters survive a Windows pipe
    try:
        if args.cmd == "catalog":
            result = cmd_catalog(args.domain, args.out, args.pages)
        elif args.cmd == "stack":
            result = cmd_stack(args.domain, args.months)
        elif args.cmd == "hero":
            result = cmd_hero(args.url, args.months)
        else:
            result = cmd_ads(args.name, args.domain)
    except Blocked as err:
        print(f"STOP: {err}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

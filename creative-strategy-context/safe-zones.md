---
summary: "Where each platform's buttons and text cover a 1080x1920 frame: the one safe box (x 100-880, y 290-1340) and per-placement numbers for Reels, Stories, Feed, TikTok and Facebook, measured on real phones by one creator in Oct 2026. Used by video-edits and motion-ads."
---

# Safe zones for 9:16 video and statics

Where the platforms' own buttons and text sit on top of a 1080×1920 frame. **One home for these numbers:** `video-edits` and `motion-ads` point here; statics and offer ads should check against it too.

**Source and confidence.** Measured by one creator from iPhone screenshots (1290×2796) of the real apps in October 2026 (github.com/alyshadotmd/video-editing, `post-preview`), not from Meta's or TikTok's own specs. *Stated, one source; the numbers below are hers, re-expressed by us.* They replace the older third-party percentages (top 14 %, bottom 35 %, sides 6 %), which cut the top and sides too close and the bottom too far. Check one real post per placement on a phone before trusting a number to the pixel, and log the result in the skill's `feedback.md`.

## The one box that is safe everywhere

Keep text, faces, product and CTA inside **x 100–880, y 290–1340**.

- Clears the top bar on every placement, the right-hand buttons on Reels and TikTok, the bottom name and caption block on Reels and TikTok, and the 4:5 crop on the Instagram feed.
- The right edge is 880, not 1015: Reels and TikTok buttons start at x 886 and 907.
- For ads, stay above y 1340: Reels ad buttons start at y 1347, Story ad buttons on video at y 1543.

## Per placement (what is covered, in video pixels)

| Placement | Trimmed or covered |
|---|---|
| Instagram Reels | sides trimmed ~97 px each; top bar to y 206; right buttons from x 886 (from y 870, ads from y 1004); bottom block from y 1469 (ads with button from y 1347); progress bar from y 1714 |
| Instagram Stories | nothing trimmed; top to y 129 (224 for a shared Reel); ad button from y 1543 (video, no "Followed by" line), 1595 with it; "Followed by" line from y 1852 |
| Instagram Feed | 4:5: visible y 91–1829; nothing covered on the video |
| TikTok For You | sides trimmed ~54 px; top tabs to y 228; right buttons from x 907 (from y 1020); bottom-left block from y 1755–1795 organic, 1597 for an ad; ad bar y 1812–1893 |
| Facebook Feed | ads shown 2:3: visible y 150–1770; organic 4:5: visible y 285–1635; mute button bottom right x 968–1041 |
| Facebook Reels | sides trimmed ~57 px; top icons to y 217; right buttons from x 930 (organic from y 1196, ads from y 1399); bottom-left block from y 1740 organic, 1540 ads |

## How to check

1. Take the frames that matter: the hook, every headline or card, every caption change, the end card.
2. An element is safe when its whole box (outline and shadow included) sits inside the one box and outside every covered area of the placements the ad runs on.
3. Report a miss with the placement name and the overlap in pixels. Faces and products stay fully visible too: the apps put text on top of them.

## In ffmpeg `.ass` captions at 1080×1920

Alignment 2 (bottom centre): `MarginV` 580 puts the lowest line at y 1340; use more to sit higher. `MarginL` 100, `MarginR` 200. Captions already sit higher than the box needs (chest height), so the bottom edge rarely binds; the right margin is the one that was wrong before.

## Other formats

4:5 feed and 1:1: keep about 5 % margins, and remember the feed crop above removes y 0–91 and 1829–1920 of a 9:16 file.

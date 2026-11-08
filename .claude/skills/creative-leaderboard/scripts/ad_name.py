#!/usr/bin/env python3
"""Parse an ad name into the shared creative tags (the factory's ad naming convention).

    python3 ad_name.py "261107_C07_A03_P2_PA_ugc-talk_creator_enemy_H2_v1"
    python3 ad_name.py "<name>" --naming-map running-notes/ad-naming.md
    python3 ad_name.py --build launch_date=2026-11-07 concept_id=C07 angle_id=A03 format=ugc-talk

The convention has one home: brain-system/system/ad-naming-convention.md. In short:
  YYMMDD_concept_angle_persona_awareness_format_voice_shape_hook_version
Fields are split by "_", a value never holds "_" (use "-"), and "x" means unknown.
Anything after the tenth field is kept as `extra` (a length or a ratio, say).

A brand that keeps its own convention writes a field map in running-notes/ad-naming.md;
load it with --naming-map (or load_field_map() when imported). Standard library only.
"""
import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

FIELDS = ["launch_date", "concept_id", "angle_id", "persona_id", "awareness", "format",
          "voice", "shape", "hook", "version"]

AWARENESS = ["UN", "PA", "SA", "PR", "MA"]
FORMATS = ["ugc-talk", "podcast", "street", "skit", "vsl", "ai-anim", "ai-avatar", "song", "demo",
           "mashup", "founder-talk", "static-benefit", "static-compare", "static-review",
           "static-meme", "static-native", "static-offer", "carousel", "motion", "other"]
VOICES = ["creator", "expert", "customer", "founder", "vo", "song", "skit", "ai", "other", "none"]
SHAPES = ["symptom", "enemy", "story", "objection", "authority", "offer", "other"]

PATTERNS = {
    "concept_id": (re.compile(r"^c(\d+)(-\d+)?$", re.I), "C07 (or C07-2)"),
    "angle_id": (re.compile(r"^a(\d+)$", re.I), "A03"),
    "persona_id": (re.compile(r"^p(\d+)$", re.I), "P2"),
    "hook": (re.compile(r"^h(\d+)$", re.I), "H2"),
    "version": (re.compile(r"^v(\d+)$", re.I), "v1"),
}
CHOICES = {"awareness": AWARENESS, "format": FORMATS, "voice": VOICES, "shape": SHAPES}

# Ads Manager adds " - Copy" (English) or " - Kopi" (Danish) when an ad is duplicated.
COPY_SUFFIX = re.compile(r"\s*[-–]\s*(copy|kopi)(\s+\d+)?\s*$", re.I)
UNKNOWN = "x"


class FieldMap:
    """How a name is laid out: separator, which position holds which field, value maps."""

    def __init__(self, positions, separator="_", date_format="YYMMDD", min_fields=None,
                 value_maps=None, source="convention"):
        self.positions = positions            # {1: "launch_date", ...}, 1-based
        self.separator = separator
        self.date_format = date_format
        self.min_fields = min_fields or (max(positions) if positions else 0)
        self.value_maps = value_maps or {}    # {"format": {"ugc": "ugc-talk"}}, keys lower-case
        self.source = source


def default_map() -> FieldMap:
    return FieldMap({i + 1: f for i, f in enumerate(FIELDS)})


def _strptime_format(token: str) -> str:
    out = token.upper()
    for k, v in (("YYYY", "%Y"), ("YY", "%y"), ("MM", "%m"), ("DD", "%d")):
        out = out.replace(k, v)
    return out


def parse_date(raw: str, token: str = "YYMMDD"):
    try:
        return datetime.strptime(raw, _strptime_format(token)).date()
    except ValueError:
        return None


def _strip_ticks(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == "`" and value[-1] == "`":
        return value[1:-1]
    return value


def load_field_map(path) -> FieldMap:
    """Read a brand's field map from running-notes/ad-naming.md (format in the convention doc)."""
    text = Path(path).read_text(encoding="utf-8-sig")
    separator, date_format, min_fields = "_", "YYMMDD", None
    positions, value_maps = {}, {}
    for line in text.splitlines():
        m = re.match(r"^\s*[-*]?\s*(separator|date_format|min_fields)\s*:\s*(.*)$", line, re.I)
        if m:
            key, value = m.group(1).lower(), _strip_ticks(m.group(2))
            if key == "separator":
                separator = value if value else "_"
            elif key == "date_format":
                date_format = value.strip() or "YYMMDD"
            elif value.strip().isdigit():
                min_fields = int(value.strip())
            continue
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or not cells[0].isdigit():
            continue  # header or the --- line
        pos = int(cells[0])
        ours = _strip_ticks(cells[2]).strip().lower() if len(cells) > 2 else ""
        if ours in ("", "x", "-", "none"):
            continue
        if ours not in FIELDS:
            raise ValueError(f"{path}: position {pos}: '{ours}' is not one of our fields "
                             f"({', '.join(FIELDS)}, or x to skip)")
        if ours in positions.values():
            raise ValueError(f"{path}: '{ours}' is mapped twice")
        positions[pos] = ours
        if len(cells) > 3 and cells[3]:
            pairs = {}
            for pair in cells[3].split(";"):
                if "=" in pair:
                    theirs, mine = pair.split("=", 1)
                    pairs[_strip_ticks(theirs).strip().lower()] = _strip_ticks(mine).strip()
            if pairs:
                value_maps[ours] = pairs
    if not positions:
        raise ValueError(f"{path}: no field rows found (need | Position | Their field | Our field | Value map |)")
    return FieldMap(positions, separator, date_format, min_fields, value_maps, source=str(path))


def _check(field: str, raw: str, fmap: FieldMap):
    """Return (normalised value, error or None)."""
    value = raw.strip()
    mapped = fmap.value_maps.get(field, {})
    if value.lower() in mapped:
        value = mapped[value.lower()]
    if value.lower() == UNKNOWN:
        return UNKNOWN, None
    if field == "launch_date":
        d = parse_date(value, fmap.date_format)
        if d is None:
            return value, f"launch_date '{raw}' is not a date in {fmap.date_format}"
        return d.isoformat(), None
    if field in PATTERNS:
        rx, example = PATTERNS[field]
        m = rx.match(value)
        if not m:
            return value, f"{field} '{raw}' should look like {example} or x"
        letter = {"version": "v"}.get(field, field[0].upper())
        if field == "concept_id":
            return f"C{m.group(1)}{m.group(2) or ''}", None
        return f"{letter}{m.group(1)}", None
    if field in CHOICES:
        allowed = CHOICES[field]
        norm = value.upper() if field == "awareness" else value.lower()
        if norm not in allowed:
            return value, f"{field} '{raw}' is not in the list ({', '.join(allowed)}, or x)"
        return norm, None
    return value, None


def parse(name: str, fmap: FieldMap = None) -> dict:
    """Parse one ad name. Returns fields (every field, 'x' when absent), ok, errors, extra."""
    fmap = fmap or default_map()
    original = name or ""
    result = {"name": original, "ok": False, "errors": [], "fields": {f: UNKNOWN for f in FIELDS},
              "extra": [], "copy": False, "map": fmap.source}
    work = original.strip()
    if not work:
        result["errors"].append("empty name")
        return result
    if COPY_SUFFIX.search(work):
        result["copy"] = True
        work = COPY_SUFFIX.sub("", work)
    parts = work.split(fmap.separator)
    if len(parts) < fmap.min_fields:
        result["errors"].append(f"has {len(parts)} fields, expected at least {fmap.min_fields} "
                                f"split by '{fmap.separator}'")
    errors = result["errors"]
    for pos, field in sorted(fmap.positions.items()):
        if pos > len(parts):
            continue
        raw = parts[pos - 1].strip() if " " in fmap.separator else parts[pos - 1]
        if raw.strip() == "":
            errors.append(f"field {pos} ({field}) is empty: use x for unknown")
            continue
        if " " in raw.strip() or (" " not in fmap.separator and raw != raw.strip()):
            errors.append(f"field {pos} ({field}) '{raw}' has a space")
            continue
        value, err = _check(field, raw, fmap)
        if err:
            errors.append(err)
        else:
            result["fields"][field] = value
    last = max(fmap.positions) if fmap.positions else 0
    result["extra"] = [p.strip() for p in parts[last:] if p.strip()]
    result["ok"] = not errors
    return result


def build_name(fields: dict) -> str:
    """Build a convention name from tag values. Missing or empty fields become x."""
    out = []
    for f in FIELDS:
        v = str(fields.get(f, "") or "").strip() or UNKNOWN
        if f == "launch_date" and v != UNKNOWN:
            d = None
            for token in ("YYYY-MM-DD", "YYMMDD", "YYYYMMDD"):
                d = parse_date(v, token)
                if d:
                    break
            v = d.strftime("%y%m%d") if d else v
        v = v.replace("_", "-").replace(" ", "-")
        out.append(v)
    return "_".join(out)


def main(argv=None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Parse an ad name into the shared creative tags, "
                                 "or build a name with --build.")
    ap.add_argument("name", nargs="*", help="the ad name (quote it)")
    ap.add_argument("--naming-map", help="the brand's field map, e.g. running-notes/ad-naming.md")
    ap.add_argument("--build", action="store_true",
                    help="build a name from field=value pairs instead of parsing")
    args = ap.parse_args(argv)
    if args.build:
        pairs = dict(p.split("=", 1) for p in args.name if "=" in p)
        bad = [k for k in pairs if k not in FIELDS]
        if bad:
            ap.error(f"unknown fields: {', '.join(bad)} (use {', '.join(FIELDS)})")
        print(build_name(pairs))
        return 0
    if not args.name:
        ap.error("give an ad name")
    fmap = load_field_map(args.naming_map) if args.naming_map else None
    result = parse(" ".join(args.name), fmap)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())

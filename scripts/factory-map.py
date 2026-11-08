#!/usr/bin/env python3
"""Print a compact map of the factory, so a session can start from it instead of re-exploring.

The improve-factory skill runs this as its step 0: one read gives the release
state, every skill with its one-line job and its processes, every method doc
with its summary, the agents, system docs, prompt folders, the brain scaffold,
scripts, tests, and how full the craft catalog is against the cap the brain's
craft-context hook enforces.

    python scripts/factory-map.py                     # everything
    python scripts/factory-map.py --section skills    # header + skills only
    python scripts/factory-map.py --section docs      # header + method docs only
    python scripts/factory-map.py --section system    # header + the rest
    python scripts/factory-map.py --out map.md        # write to a file

Standard library only. Works without git (the git lines then say so).
Output is UTF-8 on every OS, Windows too. tests/test_factory_map.py runs it.
"""
import argparse
import ast
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".claude" / "skills"
AGENTS = ROOT / ".claude" / "agents"
ROUTINE_SKILLS = ROOT / "templates" / "brand-routines" / "claude" / "skills"
KB = ROOT / "creative-strategy-context"
CATALOG_DOC = KB / "expertise-routing.md"
HOOK = ROOT / "templates" / "brand-routines" / "claude" / "hooks" / "craft-context.py"
DOC_EXCLUDE = {"expertise-routing.md", "brand-brain-CLAUDE-template.md", "README.md"}
DEFAULT_CAP = 16000
SKILL_CHARS = 150
DOC_CHARS = 140
MAX_PROCS = 8
# Lines that are not the doc's own description: headings, tables, quotes, lists, metadata.
SKIP_LINES = ("#", "---", "|", ">", "- ", "* ", "Updated", "Origin", "Last updated", "Status")
SECTIONS = ("skills", "docs", "system", "all")


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return ""


def git(*args: str) -> str | None:
    try:
        out = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True,
                             text=True, encoding="utf-8", timeout=20)
    except (OSError, subprocess.SubprocessError):
        return None
    return out.stdout.strip() if out.returncode == 0 else None


def frontmatter(text: str) -> dict[str, str]:
    """Top-level `key: value` lines of a YAML frontmatter block (no YAML library)."""
    text = text.lstrip("﻿")
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fields = {}
    for line in text[3:end].splitlines():
        if not line or line[0] in " \t-#" or ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields


def first_sentence(text: str, limit: int) -> str:
    # Drop the trigger-word lists in parentheses: the map wants the job, not the triggers.
    text = re.sub(r"\s*\([^()]{25,}\)", "", " ".join(text.split()))
    # A sentence ends at ". " outside parentheses (trigger lists hold dots and commas).
    depth = 0
    for i, ch in enumerate(text):
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        elif ch == "." and depth == 0 and (i + 1 == len(text) or text[i + 1] == " "):
            text = text[: i + 1]
            break
    return shorten(text, limit)


def shorten(text: str, limit: int) -> str:
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    cut = text[: limit - 3].rsplit(" ", 1)[0]
    return cut.rstrip(",;:") + "..."


def body_line(text: str) -> str:
    """First plain paragraph after the frontmatter, for a file without a description."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        text = text[end + 4:] if end != -1 else text
    for para in re.split(r"\n\s*\n", text):
        para = para.strip()
        if para and not para.startswith(SKIP_LINES):
            return " ".join(para.split())
    return ""


def names(folder: Path, pattern: str = "*", dirs: bool = False) -> list[str]:
    if not folder.is_dir():
        return []
    items = [p for p in folder.glob(pattern) if p.name != "__pycache__" and not p.name.startswith(".")]
    items = [p for p in items if p.is_dir() == dirs]
    return sorted(p.name for p in items)


# --- header -----------------------------------------------------------------

def catalog_size() -> str:
    text = read(CATALOG_DOC)
    m = re.search(r"<!-- DOC-MAP:START -->\n(.*?)\n<!-- DOC-MAP:END -->", text, re.DOTALL)
    if not m:
        return "craft catalog: no DOC-MAP block found in creative-strategy-context/expertise-routing.md"
    table = m.group(1).strip()
    table_bytes = len(table.encode("utf-8"))
    cap, instruction = DEFAULT_CAP, None
    try:
        tree = ast.parse(read(HOOK))
        for node in tree.body:
            if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                name = node.targets[0].id
                if name == "MAX_CONTEXT_BYTES":
                    cap = int(ast.literal_eval(node.value))
                elif name == "INSTRUCTION":
                    instruction = str(ast.literal_eval(node.value))
    except (SyntaxError, ValueError):
        pass
    if instruction is None:
        return (f"craft catalog: table {table_bytes:,} bytes, cap {cap:,} "
                "(hook instruction not read; real headroom is smaller)")
    # The hook injects INSTRUCTION + this lead-in + the table (profile excluded here).
    lead = ("\n\nThe craft catalog (generated from expertise-routing.md; "
            "paths are relative to brain-system/creative-strategy-context/):\n")
    injected = len((instruction + lead + table).encode("utf-8"))
    status = "fits" if injected <= cap else "OVER: the hook falls back to a pointer"
    return (f"craft catalog: table {table_bytes:,} bytes; injected with the hook instruction "
            f"{injected:,} of {cap:,} bytes ({status}, headroom {cap - injected:,} before any user profile)")


def header() -> list[str]:
    version = read(ROOT / "VERSION").strip() or "?"
    tags = git("tag", "--list", "v*", "--sort=-v:refname")
    latest = tags.splitlines()[0] if tags else "none (or no git)"
    out = ["# Factory map", "",
           f"- VERSION: {version}; latest tag: {latest}"
           + ("" if latest == version else " (VERSION and tag differ: a release is in progress or untagged)")]
    for folder in ("migrations", "release-notes"):
        vs = sorted((int(p.stem[1:]) for p in (ROOT / folder).glob("v*.md") if p.stem[1:].isdigit()))
        out.append(f"- {folder}/: newest v{vs[-1]}" if vs else f"- {folder}/: none")
    status = git("status", "--short")
    if status is None:
        out.append("- git: not available")
    else:
        changed = [ln[3:] for ln in status.splitlines() if ln.strip()]
        shown = ", ".join(changed[:8]) + (f", +{len(changed) - 8} more" if len(changed) > 8 else "")
        out.append(f"- working tree: {'clean' if not changed else f'{len(changed)} changed: {shown}'}")
    out.append(f"- {catalog_size()}")
    log = git("log", "--oneline", "-5")
    out += ["", "Last commits:"] + ([f"- {ln}" for ln in log.splitlines()] if log else ["- (no git log)"])
    out += ["", "Rules: CLAUDE.md (factory rules 1-8). Release steps: .claude/skills/improve-factory/processes/wire-and-release.md.", ""]
    return out


# --- sections ---------------------------------------------------------------

def skills_section() -> list[str]:
    routine = set(names(ROUTINE_SKILLS, dirs=True))
    rows = names(SKILLS, dirs=True)
    out = [f"## Skills ({len(rows)}, .claude/skills/)", ""]
    for name in rows:
        folder = SKILLS / name
        text = read(folder / "SKILL.md")
        desc = frontmatter(text).get("description") or body_line(text)
        line = f"- **{name}**: {first_sentence(desc, SKILL_CHARS) if desc else '(no description)'}"
        extras = []
        procs = [p[:-3] for p in names(folder / "processes", "*.md") if p != "INDEX.md"]
        if procs:
            more = f", +{len(procs) - MAX_PROCS} more" if len(procs) > MAX_PROCS else ""
            extras.append(f"{len(procs)} process{'es' if len(procs) > 1 else ''}: " + ", ".join(procs[:MAX_PROCS]) + more)
        parts = [n for n in ("strategy.md", "scripts", "references") if (folder / n).exists()]
        if parts:
            extras.append("has " + ", ".join(parts))
        if name in routine:
            extras.append("routine twin in templates/brand-routines")
        if extras:
            line += " [" + "; ".join(extras) + "]"
        out.append(line)
    only_routine = sorted(routine - set(rows))
    if only_routine:
        out += ["", "Routine-bundle skills (templates/brand-routines/claude/skills/, synced into brains): "
                + ", ".join(only_routine)]
    return out + [""]


def docs_section() -> list[str]:
    docs = [p for p in sorted(KB.glob("*.md")) if p.name not in DOC_EXCLUDE]
    out = [f"## Method docs ({len(docs)}, creative-strategy-context/; summary cap 240 bytes)", ""]
    for p in docs:
        summary = frontmatter(read(p)).get("summary")
        out.append(f"- **{p.name}**: {shorten(summary, DOC_CHARS) if summary else '(NO SUMMARY: missing from the catalog)'}")
    subdirs = names(KB, dirs=True)
    if subdirs:
        out += ["", "Folders: " + ", ".join(f"{d}/" for d in subdirs)]
    return out + [""]


def system_section() -> list[str]:
    out = ["## Agents (.claude/agents/)", ""]
    for p in sorted(AGENTS.glob("*.md")):
        if p.name == "README.md":
            continue
        desc = frontmatter(read(p)).get("description", "")
        out.append(f"- **{p.stem}**: {first_sentence(desc, 120)}")
    out += ["", "## System docs (system/)", ""]
    for p in sorted((ROOT / "system").glob("*.md")):
        if p.name == "INDEX.md":
            continue
        text = read(p)
        out.append(f"- **{p.name}**: {shorten(body_line(text), 110)}")
    top = [p.name + ("/" if p.is_dir() else "") for p in sorted(ROOT.iterdir())
           if p.name not in (".git", "__pycache__") and not p.name.endswith(".pyc")]
    groups = [
        ("Top level", top),
        ("Prompt folders (prompts/)", [f"{d}/" for d in names(ROOT / "prompts", dirs=True)]
         + names(ROOT / "prompts", "*.md")),
        ("Brain scaffold (templates/brand-scaffold/)", [f"{d}/" for d in names(ROOT / "templates/brand-scaffold", dirs=True)]
         + names(ROOT / "templates/brand-scaffold")),
        ("Templates (templates/)", names(ROOT / "templates", "*.md")),
        ("Scripts (scripts/)", names(ROOT / "scripts")),
        ("Tests (tests/, run: python -m pytest tests -q)", names(ROOT / "tests", "*.py")),
        ("Global knowledge (global/knowledge/)", names(ROOT / "global/knowledge")),
        ("Third party (third-party/, credits in NOTICE.md)", [f"{d}/" for d in names(ROOT / "third-party", dirs=True)]),
        ("Releases", [f"migrations/ ({len(names(ROOT / 'migrations', 'v*.md'))} notes)",
                      f"release-notes/ ({len(names(ROOT / 'release-notes', 'v*.md'))} notes)"]),
    ]
    for title, items in groups:
        out += ["", f"## {title}", "", ", ".join(items) if items else "(none)"]
    return out + [""]


def build(section: str) -> str:
    lines = header()
    if section in ("skills", "all"):
        lines += skills_section()
    if section in ("docs", "all"):
        lines += docs_section()
    if section in ("system", "all"):
        lines += system_section()
    return "\n".join(lines).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Print a compact markdown map of the factory.")
    parser.add_argument("--section", choices=SECTIONS, default="all",
                        help="which part to print after the header (default: all)")
    parser.add_argument("--out", help="write the map to this file instead of printing it")
    args = parser.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    text = build(args.section)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"wrote {args.out} ({len(text.encode('utf-8')):,} bytes)")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())

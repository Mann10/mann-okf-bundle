#!/usr/bin/env python3
"""
OKF MCP Server — exposes the knowledge bundle via Model Context Protocol.

Start with:
    python serve/mcp_server.py

Then connect your MCP client (e.g., opencode, Claude Desktop) to stdio.
"""

from pathlib import Path
import json
import os
import sys

from mcp.server.fastmcp import FastMCP

BUNDLE_DIR = Path(__file__).parent.parent / "knowledge"

mcp = FastMCP(
    "OKF Bundle Server",
    instructions="""\
# OKF Knowledge Bundle — Progressive Disclosure Protocol

This server exposes an OKF v0.1 knowledge bundle about agentic AI workflows.

## Protocol (MUST follow this order)

### Step 1 — Index
Call `okf_index` first. This lists everything available, grouped by type.
Do NOT skip this step — you need to know what exists before you can search.

### Step 2 — Find or Browse
Use `okf_find` to search for keywords, or re-read the index output
to identify relevant concepts/workflows.

### Step 3 — Read
Call `okf_read` with the path to a specific file.

### Step 4 — Explore Relationships
Call `okf_concepts` to see how concepts connect (supports, contradicts).

## Citation Rules
Every claim MUST cite: `type` + `title` + section heading.
If a claim has no source in the bundle, say: "This is not covered in the knowledge base."
NEVER fabricate quotes, timestamps, or section names.
""",
    log_level="INFO",
)


# ── Helpers ──────────────────────────────────────────────────────────

RESERVED = {"index.md", "log.md"}


def get_all_md_files():
    files = []
    if BUNDLE_DIR.exists():
        for root, _, filenames in os.walk(BUNDLE_DIR):
            for f in filenames:
                if f.endswith(".md") and f not in RESERVED:
                    files.append(Path(root) / f)
    return sorted(files)


def parse_frontmatter(filepath):
    content = filepath.read_text(encoding="utf-8")
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            return parts[1].strip(), parts[2].strip()
    return "", content


def get_frontmatter_field(frontmatter, field):
    for line in frontmatter.split("\n"):
        if line.strip().startswith(f"{field}:"):
            raw = line.split(":", 1)[1].strip().strip('"').strip("'")
            if raw.startswith("[") and raw.endswith("]"):
                items = [x.strip().strip('"').strip("'") for x in raw[1:-1].split(",")]
                return ", ".join(items)
            return raw
    return None


# ── Tools ────────────────────────────────────────────────────────────


@mcp.tool(
    description="[STEP 1] List everything in the knowledge bundle grouped by type. Always call this first."
)
def okf_index() -> str:
    """List all concepts and workflows with their type, title, and description."""
    files = get_all_md_files()
    groups = {}
    for f in files:
        rel = f.relative_to(BUNDLE_DIR)
        frontmatter, _ = parse_frontmatter(f)
        title = get_frontmatter_field(frontmatter, "title") or rel.stem
        concept_type = get_frontmatter_field(frontmatter, "type") or "Unknown"
        desc = get_frontmatter_field(frontmatter, "description") or ""
        groups.setdefault(concept_type, []).append({"title": title, "path": str(rel), "desc": desc})

    lines = ["# OKF Bundle Index", ""]
    for group_type, entries in groups.items():
        lines.append(f"## {group_type} ({len(entries)})")
        lines.append("")
        for e in entries:
            lines.append(f"- **{e['title']}**")
            if e["desc"]:
                lines.append(f"  {e['desc']}")
            lines.append(f"  → `{e['path']}`")
            lines.append("")

    lines.append(f"**Total: {len(files)} files**")
    return "\n".join(lines)


@mcp.tool(
    description="[STEP 2] Search the bundle for a keyword. Returns file paths with match counts and snippets."
)
async def okf_find(keyword: str) -> str:
    """Search for a keyword across all knowledge files."""
    files = get_all_md_files()
    results = []
    kw = keyword.lower()

    for f in files:
        content = f.read_text(encoding="utf-8")
        if kw in content.lower():
            count = content.lower().count(kw)
            lines = content.split("\n")
            first_line = 1
            snippet = ""
            for i, line in enumerate(lines, 1):
                if kw in line.lower():
                    first_line = i
                    snippet = line.strip()[:150]
                    break
            results.append({
                "path": str(f.relative_to(BUNDLE_DIR)),
                "count": count,
                "line": first_line,
                "snippet": snippet,
            })

    results.sort(key=lambda x: x["count"], reverse=True)

    if not results:
        return f"No results found for '{keyword}'."

    lines = [f"# Search results for '{keyword}'", f"Found in {len(results)} file(s):", ""]
    for r in results:
        lines.append(f"## {r['path']} ({r['count']} matches, line {r['line']})")
        lines.append(f"> {r['snippet']}")
        lines.append("")

    return "\n".join(lines)


@mcp.tool(
    description="[STEP 3] Read a specific concept or workflow file. Provide path relative to knowledge/ (e.g. 'concepts/execution-traces.md')."
)
async def okf_read(filepath: str) -> str:
    """Read a file and return its full content with citation info."""
    fp = BUNDLE_DIR / filepath
    if not fp.exists():
        fp = BUNDLE_DIR / filepath.replace("knowledge/", "")
    if not fp.exists():
        return f"ERROR: File not found: {filepath}"

    content = fp.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(fp)
    title = get_frontmatter_field(frontmatter, "title") or fp.stem
    concept_type = get_frontmatter_field(frontmatter, "type") or "Unknown"
    tags = get_frontmatter_field(frontmatter, "tags") or ""

    header = [
        f"# {title}",
        f"**Type:** {concept_type}",
        f"**Path:** `{fp.relative_to(BUNDLE_DIR)}`",
    ]
    if tags:
        header.append(f"**Tags:** {tags}")
    header.append("")

    citation = [
        "",
        "---",
        f"**Cite as:** `{concept_type}` / `{title}` + section heading",
    ]

    return "\n".join(header + [body] + citation)


@mcp.tool(
    description="[STEP 4] Get the relationship graph between concepts — which support or contradict each other."
)
async def okf_concepts() -> str:
    """Return the concept relationship graph from relationships.json."""
    rel_path = BUNDLE_DIR / "concepts" / "relationships.json"
    if not rel_path.exists():
        return "No relationships.json found in the bundle."

    data = json.loads(rel_path.read_text(encoding="utf-8"))
    lines = ["# Concept Relationships", ""]

    concepts = data.get("concepts", [])
    if concepts:
        lines.append("## Concepts")
        lines.append("")
        for c in concepts:
            lines.append(f"### {c.get('id', '?')}")
            lines.append(f"- Type: {c.get('type', '?')}")
            supports = c.get("supports", [])
            contradicts = c.get("contradicts", [])
            if supports:
                lines.append(f"- Supports: {', '.join(supports)}")
            if contradicts:
                lines.append(f"- Contradicts: {', '.join(contradicts)}")
            lines.append("")

    themes = data.get("cross_video_themes", [])
    if themes:
        lines.append("## Cross-Concept Themes")
        lines.append("")
        for i, t in enumerate(themes, 1):
            lines.append(f"{i}. {t}")
        lines.append("")

    disagreements = data.get("disagreements", [])
    if disagreements:
        lines.append("## Disagreements/Tensions")
        lines.append("")
        for d in disagreements:
            lines.append(f"- {d}")
        lines.append("")

    return "\n".join(lines) if len(lines) > 2 else "No relationship data available."


# ── Main ─────────────────────────────────────────────────────────────

def main():
    mcp.run()


if __name__ == "__main__":
    main()

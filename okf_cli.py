#!/usr/bin/env python3
"""
OKF CLI - stdlib-only tool for querying the knowledge bundle.
Commands: index, find, read
"""

import argparse
import os
import sys
from pathlib import Path

BUNDLE_DIR = Path(__file__).parent / "knowledge"
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


def get_field(frontmatter, field):
    for line in frontmatter.split("\n"):
        if line.strip().startswith(f"{field}:"):
            raw = line.split(":", 1)[1].strip().strip('"').strip("'")
            if raw.startswith("[") and raw.endswith("]"):
                items = [x.strip().strip('"').strip("'") for x in raw[1:-1].split(",")]
                return ", ".join(items)
            return raw
    return None


def cmd_index(args):
    """List everything grouped by type."""
    files = get_all_md_files()
    subpath = args.subpath
    if subpath:
        target = (BUNDLE_DIR / subpath).resolve()
        files = [f for f in files if target in f.parents or f.parent == target]

    print("\n" + "=" * 60)
    print("  OKF BUNDLE INDEX")
    print("=" * 60)

    groups = {}
    for f in files:
        rel = f.relative_to(BUNDLE_DIR)
        frontmatter, _ = parse_frontmatter(f)
        title = get_field(frontmatter, "title") or rel.stem
        t = get_field(frontmatter, "type") or "Unknown"
        desc = get_field(frontmatter, "description") or ""
        groups.setdefault(t, []).append((title, str(rel), desc))

    for group_type, entries in groups.items():
        print(f"\n  {group_type} ({len(entries)})")
        print("  " + "-" * 40)
        for title, path, desc in entries:
            print(f"  {title}")
            if desc:
                print(f"    -> {desc}")
            print(f"    -> {path}")

    print(f"\n  TOTAL: {len(files)} files")
    print("=" * 60 + "\n")


def cmd_find(args):
    """Search for keyword across all content."""
    keyword = args.keyword.lower()
    files = get_all_md_files()
    results = []

    for f in files:
        content = f.read_text(encoding="utf-8").lower()
        if keyword in content:
            count = content.count(keyword)
            lines = f.read_text(encoding="utf-8").split("\n")
            first_line = 1
            snippet = ""
            for i, line in enumerate(lines, 1):
                if keyword in line.lower():
                    first_line = i
                    snippet = line.strip()[:100]
                    break
            results.append({
                "path": str(f.relative_to(BUNDLE_DIR)),
                "count": count,
                "line": first_line,
                "snippet": snippet,
            })

    results.sort(key=lambda x: x["count"], reverse=True)

    print(f"\n  Found '{args.keyword}' in {len(results)} file(s):\n")
    for r in results:
        print(f"  {r['path']} ({r['count']} matches, line {r['line']})")
        print(f"    | {r['snippet']}")
        print()


def cmd_read(args):
    """Read a specific file with full context."""
    filepath = BUNDLE_DIR / args.filepath
    if not filepath.exists():
        print(f"ERROR: File not found: {args.filepath}")
        sys.exit(1)

    content = filepath.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(filepath)
    title = get_field(frontmatter, "title") or filepath.stem
    t = get_field(frontmatter, "type") or "Unknown"

    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)
    print(f"  Source: {filepath.relative_to(BUNDLE_DIR)}")
    print("-" * 60)
    print(body)
    print("=" * 60)
    print(f"\n  Cite as: '{t}' / '{title}' + section heading")
    print("=" * 60 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="OKF CLI - Query the knowledge bundle",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python okf_cli.py index
  python okf_cli.py index concepts
  python okf_cli.py find "execution trace"
  python okf_cli.py read concepts/execution-traces.md
        """,
    )
    subparsers = parser.add_subparsers(dest="command")

    index_parser = subparsers.add_parser("index", help="List all concepts and workflows")
    index_parser.add_argument("subpath", nargs="?", default=None, help="Filter by subpath (e.g. concepts)")

    find_parser = subparsers.add_parser("find", help="Search for keyword across the bundle")
    find_parser.add_argument("keyword", help="Keyword to search for")

    read_parser = subparsers.add_parser("read", help="Read a specific page")
    read_parser.add_argument("filepath", help="Path relative to knowledge/ (e.g. concepts/execution-traces.md)")

    args = parser.parse_args()

    if args.command == "index":
        cmd_index(args)
    elif args.command == "find":
        cmd_find(args)
    elif args.command == "read":
        cmd_read(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

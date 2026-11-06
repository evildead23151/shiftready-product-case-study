#!/usr/bin/env python3
"""Validate relative Markdown links without requiring third-party packages."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
REFERENCE_DEF = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)", re.MULTILINE)


def strip_title(destination: str) -> str:
    destination = destination.strip()
    if destination.startswith("<") and ">" in destination:
        return destination[1 : destination.index(">")]
    return destination.split(maxsplit=1)[0] if destination else ""


def is_external(destination: str) -> bool:
    parts = urlsplit(destination)
    return bool(parts.scheme or parts.netloc)


def check_target(source: Path, destination: str) -> str | None:
    destination = unquote(strip_title(destination))
    if not destination or destination.startswith("#") or is_external(destination):
        return None

    path_part = destination.split("#", maxsplit=1)[0].split("?", maxsplit=1)[0]
    if not path_part:
        return None

    target = (source.parent / path_part).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        return f"link escapes repository: {destination}"

    if not target.exists():
        return f"missing target: {destination}"
    return None


def main() -> int:
    failures: list[str] = []
    markdown_files = sorted(ROOT.rglob("*.md"))

    for source in markdown_files:
        text = source.read_text(encoding="utf-8")
        destinations = [match.group(1) for match in MARKDOWN_LINK.finditer(text)]
        destinations.extend(REFERENCE_DEF.findall(text))

        for destination in destinations:
            issue = check_target(source, destination)
            if issue:
                failures.append(f"{source.relative_to(ROOT)}: {issue}")

    if failures:
        print("\n".join(failures))
        print(f"\nFound {len(failures)} broken local Markdown link(s).")
        return 1

    print(f"Validated local Markdown links across {len(markdown_files)} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Rebuild The Close Map's generated catalogs from canonical files."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
MAP = ROOT / "sample-map"


def read_frontmatter(text: str) -> dict[str, str]:
    raw = text.split("\n---\n", 1)[0][4:]
    result: dict[str, str] = {}
    for line in raw.splitlines():
        if line.startswith(" ") or not line.strip() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip()
    return result


def noun_index() -> str:
    rows: list[tuple[str, str, str, str]] = []
    for card in sorted((MAP / "objects").glob("*/*.md")):
        text = card.read_text(encoding="utf-8")
        meta = read_frontmatter(text)
        title = re.search(r"^# (.+)$", text, re.M)
        if not title:
            raise SystemExit(f"Missing H1 in {card.relative_to(ROOT)}")
        rows.append(
            (
                title.group(1),
                meta["universe"],
                meta["status"],
                card.relative_to(MAP / "objects").as_posix(),
            )
        )
    body = "# Noun Index\n\n| Noun | Universe | Status | Card |\n|---|---|---|---|\n"
    body += "".join(
        f"| {name} | {universe} | {status} | `{path}` |\n"
        for name, universe, status, path in sorted(rows)
    )
    return body + "\nGenerated from object frontmatter by `generate_close_map.py`; do not edit by hand.\n"


def main() -> None:
    canonical_entry = (MAP / "CLAUDE.md").read_bytes()
    for name in ("AGENTS.md", "routing.md"):
        (MAP / name).write_bytes(canonical_entry)
    (MAP / "objects/_index.md").write_text(noun_index(), encoding="utf-8")
    print("Generated AGENTS.md, routing.md, and objects/_index.md from canonical sources.")


if __name__ == "__main__":
    main()

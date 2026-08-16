#!/usr/bin/env python3
"""Validate The Close Map against its published architecture contract."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
FACTORY = ROOT / "cartographer"
MAP = ROOT / "sample-map"
SUBJECT = ROOT / "demo-territory"
REVISION = "monthly-close-v1"


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def require(path: Path) -> str:
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        fail(f"empty required file: {path.relative_to(ROOT)}")
    return text


def frontmatter(text: str, path: Path) -> dict[str, str]:
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        fail(f"missing YAML frontmatter: {path.relative_to(ROOT)}")
    raw = text.split("\n---\n", 1)[0][4:]
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if line.startswith(" ") or not line.strip() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def expected_index(cards: list[Path]) -> str:
    rows = []
    for card in cards:
        text = require(card)
        meta = frontmatter(text, card)
        title = re.search(r"^# (.+)$", text, re.M)
        if not title:
            fail(f"missing H1: {card.relative_to(ROOT)}")
        rows.append((title.group(1), meta["universe"], meta["status"], card.relative_to(MAP / "objects").as_posix()))
    body = "# Noun Index\n\n| Noun | Universe | Status | Card |\n|---|---|---|---|\n"
    body += "".join(f"| {name} | {universe} | {status} | `{path}` |\n" for name, universe, status, path in sorted(rows))
    body += "\nThis index is generated from card frontmatter by `validate_close_map.py`; do not add payload here.\n"
    return body


def validate_factory() -> None:
    for relative in [
        "README.md", "identity.md", "rules.md", "examples.md",
        "reference/card-types.md", "reference/walk-order.md",
        "reference/naming-collisions.md",
        "reference/test-protocol.md",
    ]:
        require(FACTORY / relative)
    example = require(FACTORY / "examples.md")
    for marker in ["## Catalog", "Source Document", "Review Packet", "## Ghost card", "## One change", "DOES NOT HIT"]:
        if marker not in example:
            fail(f"worked example missing: {marker}")


def validate_entry_and_contracts() -> None:
    entries = [require(MAP / name) for name in ("CLAUDE.md", "AGENTS.md", "routing.md")]
    if not entries[0] == entries[1] == entries[2]:
        fail("CLAUDE.md, AGENTS.md, and routing.md must be byte-identical")
    if len(entries[0].splitlines()) > 60:
        fail("entry catalog exceeds 60 lines")
    for marker in ["CONTEXT.md", "objects/_index.md", "effects/CONTEXT.md", "Do not load"]:
        if marker not in entries[0]:
            fail(f"entry catalog missing routing marker: {marker}")
    context = require(MAP / "CONTEXT.md")
    for marker in ["## Territory", "## Universes", "## Name collisions", "## Reading contract", "## Authority"]:
        if marker not in context:
            fail(f"map contract missing: {marker}")
    schema = require(MAP / "_meta/schema.md")
    for marker in ["### object", "### process", "live | leftover | ghost", "stub | verified | stale"]:
        if marker not in schema:
            fail(f"closed schema missing: {marker}")
    require(MAP / "_templates/object.md")
    require(MAP / "_templates/process.md")
    require(MAP / "objects/CONTEXT.md")
    require(MAP / "processes/CONTEXT.md")
    require(MAP / "effects/CONTEXT.md")


def validate_cards() -> list[Path]:
    cards = sorted((MAP / "objects").glob("*/*.md"))
    if len(cards) != 6:
        fail(f"expected six object cards, found {len(cards)}")
    required_meta = {"type", "cluster", "universe", "status", "verified_on", "revision", "entity"}
    required_sections = ["## Why this shape", "## Shape", "## Connected to", "## If you change this", "## Surfaces", "## See"]
    allowed_universes = {"live", "leftover", "ghost"}
    allowed_statuses = {"stub", "verified", "stale"}
    for card in cards:
        text = require(card)
        meta = frontmatter(text, card)
        missing = required_meta - meta.keys()
        if missing:
            fail(f"{card.name} missing frontmatter: {sorted(missing)}")
        if meta["type"] != "object" or meta["universe"] not in allowed_universes or meta["status"] not in allowed_statuses:
            fail(f"{card.name} violates closed schema")
        if meta["status"] == "verified":
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", meta["verified_on"]):
                fail(f"{card.name} verified without valid date")
            if meta["revision"] != REVISION:
                fail(f"{card.name} verified against wrong revision")
        for section in required_sections:
            if section not in text:
                fail(f"{card.name} missing {section}")
        for marker in ["**Hits:**", "**Does not hit:**", "Source:"]:
            if marker not in text:
                fail(f"{card.name} missing {marker}")
        for citation in re.findall(r"Source: `([^`]+)`", text):
            target = (card.parent / citation).resolve()
            if not target.is_file() or ROOT not in target.parents:
                fail(f"broken or escaping citation in {card.name}: {citation}")
    index_path = MAP / "objects/_index.md"
    if require(index_path) != expected_index(cards):
        fail("objects/_index.md drifted from generated card frontmatter")
    return cards


def validate_process_and_effects(cards: list[Path]) -> None:
    processes = sorted((MAP / "processes").glob("*.md"))
    processes = [path for path in processes if path.name != "CONTEXT.md"]
    if len(processes) != 1:
        fail("expected exactly one proven movement")
    process = processes[0]
    text = require(process)
    meta = frontmatter(text, process)
    for key in ["type", "universe", "status", "verified_on", "revision", "consumes", "produces"]:
        if key not in meta:
            fail(f"process missing frontmatter key: {key}")
    if meta["type"] != "process" or meta["status"] != "verified" or meta["revision"] != REVISION:
        fail("process is not verified against monthly-close-v1")
    for section in ["## Input", "## Movement", "## Output", "## If you change this", "## Surfaces", "## See"]:
        if section not in text:
            fail(f"process missing {section}")
    effects = require(MAP / "effects/CONTEXT.md")
    for card in cards:
        if card.name not in effects:
            fail(f"effects catalog does not route to {card.name}")
    if "UNKNOWN / Catalog Gap" not in effects:
        fail("effects catalog lacks safe unknown route")


def validate_subject_and_privacy() -> None:
    for relative in [
        "client-workspace/workspace-manifest.md", "client-workspace/intake-rules.md",
        "client-workspace/source-document-index.csv", "client-workspace/review-packet-schema.md",
        "client-workspace/review-packet-2026-07.md", "client-workspace/exception-register.csv",
        "client-workspace/approval-register.csv", "client-workspace/archive/Missing Documents.xlsx.note.md",
    ]:
        require(SUBJECT / relative)
    require(ROOT / "audit/00-inventory.md")
    require(ROOT / "ARCHITECTURE-VERIFICATION.md")
    manifest = require(SUBJECT / "client-workspace/workspace-manifest.md")
    for marker in ["CRHS-042", "2026-07", "business day 10", "QuickBooks Online", "sanitized composite"]:
        if marker not in manifest:
            fail(f"realistic territory marker missing: {marker}")
    packet = require(SUBJECT / "client-workspace/review-packet-2026-07.md")
    for marker in ["Revision: `2`", "EX-2026-07-019", "RN-017", "## Excluded"]:
        if marker not in packet:
            fail(f"review-packet operating detail missing: {marker}")
    text = "\n".join(path.read_text(encoding="utf-8") for path in ROOT.rglob("*") if path.is_file() and path.suffix.lower() in {".md", ".csv"})
    for marker in ["social security number", "routing number", "real client name"]:
        if marker in text.lower():
            fail(f"privacy-sensitive marker found: {marker}")


def validate_public_language() -> None:
    encoded = [
        [105, 99, 109],
        [106, 97, 107, 101],
        [118, 97, 110, 32, 99, 108, 105, 101, 102],
        [99, 108, 105, 101, 102, 32, 110, 111, 116, 101, 115],
        [99, 111, 109, 112, 101, 116, 105, 116, 105, 111, 110],
        [99, 111, 110, 116, 101, 115, 116],
        [119, 101, 101, 107, 108, 121, 32, 99, 111, 109, 112],
        [105, 110, 116, 101, 114, 112, 114, 101, 116, 97, 98, 108, 101, 32, 99, 111, 110, 116, 101, 120, 116, 32, 109, 101, 116, 104, 111, 100, 111, 108, 111, 103, 121],
        [114, 105, 110, 100, 105, 103],
    ]
    prohibited = ["".join(chr(value) for value in values) for values in encoded]
    text_suffixes = {".md", ".py", ".yml", ".yaml", ".json", ".html", ".csv", ".txt"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in text_suffixes:
            continue
        relative = path.relative_to(ROOT).as_posix().lower()
        content = path.read_text(encoding="utf-8").lower()
        for phrase in prohibited:
            pattern = rf"(?<![a-z0-9]){re.escape(phrase)}(?![a-z0-9])"
            if re.search(pattern, relative) or re.search(pattern, content):
                fail(f"prohibited public reference in {path.relative_to(ROOT)}")


def main() -> None:
    validate_factory()
    validate_entry_and_contracts()
    cards = validate_cards()
    validate_process_and_effects(cards)
    validate_subject_and_privacy()
    validate_public_language()
    print("The Close Map validation passed: factory, gated inventory, entry twins, closed schema, 6 objects, 1 process, effects catalog, citations, privacy boundary, and public-language guard.")


if __name__ == "__main__":
    main()

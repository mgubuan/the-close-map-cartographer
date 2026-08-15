# The Close Map

**Change one thing. Know what else moves. Load nothing you do not need.**

The Close Map is a folder-based cartographer for a bookkeeping document-to-review system. It gives a newly hired bookkeeper and a cold AI model the same small set of doors into a real body of work—without copying client data or loading the entire operation.

## Run the live demonstration

**[Open the client-facing Change Radius demo →](https://intelligencesolved.com/close-map)**

Try these two questions first:

1. `Statements move from email to the portal.`
2. `Is Missing Documents.xlsx the live tracker?`

The first produces a bounded change radius. The second springs the ghost trap: a plausibly named workbook still exists, but no live control writes to or reads from it.

## What is here

```text
cartographer/       The drop-in cartographer folder
demo-territory/     A synthetic, privacy-safe bookkeeping workspace
sample-map/         The source-cited map left by the cartographer
audit/              The inventory-before-cards artifact
validate_close_map.py
test-results.md
```

The deliverable is `cartographer/`. Point it at a real, sanitized body of work and it leaves a small routing catalog, a map contract, a closed schema, a verified noun shelf, real movement cards, and a change-impact catalog.

## The front door

The sample catalog routes change intent to one card:

| If you need to change… | Open |
|---|---|
| Where client evidence arrives | `sample-map/objects/bookkeeping/source-document.md` |
| How missing information is represented | `sample-map/objects/bookkeeping/exception.md` |
| What a reviewer receives | `sample-map/objects/bookkeeping/review-packet.md` |
| What makes work officially approved | `sample-map/objects/bookkeeping/approval.md` |
| A tracker that may no longer be wired | `sample-map/objects/bookkeeping/missing-documents-tracker.md` |

The generated map uses a strict, inspectable system-map architecture: byte-identical entry twins, a map contract, a closed schema, copyable object/process templates, a generated noun index, verified noun cards, one proven movement, and a change-impact catalog. Every card names:

- what the noun is;
- why it has its current shape;
- whether it is `LIVE`, `LEFTOVER`, `GHOST`, or `UNKNOWN`;
- the source evidence establishing that status;
- what a change `Hits`;
- what it `Does not hit`;
- when another card may be opened; and
- when the reader must stop.

## The core rule

> Existence is not liveness. Movement is liveness.

A file is not live because its name sounds official. `LIVE` requires evidence that something currently writes it, reads it, or makes an operational decision from it.

## Privacy boundary

The demonstration is synthetic. The cartographer cites paths, schemas, headings, and controls; it does not copy credentials, tax IDs, account numbers, balances, transaction contents, or client-identifying values.

## Validate

```bash
python validate_close_map.py
```

The validator checks structural completeness, status vocabulary, catalog doors, source citations, and the sanitized demonstration boundary. It does not pretend structural checks prove semantic understanding; a fresh-session blind-reader test is still required and is marked honestly in `test-results.md`.

## Later reader

The later reader is a newly hired bookkeeper or cold AI assistant who must change an intake or review system without confusing `received` with `complete`, treating a ghost tracker as live, or ingesting the entire firm library.

Built and maintained by [Intelligence Solved](https://intelligencesolved.com/).

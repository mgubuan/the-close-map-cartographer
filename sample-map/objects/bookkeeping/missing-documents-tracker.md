---
type: object
cluster: bookkeeping
universe: ghost
status: verified
verified_on: 2026-08-15
revision: demo-v1
entity: demo-territory/client-workspace/archive/Missing Documents.xlsx.note.md
---

# Missing Documents Tracker

`Missing Documents.xlsx` is a retained workbook name with no live writer, reader, or decision connection.

## Why this shape

The card exists as a tripwire: the filename implies current authority, while source evidence establishes that the live missing-information object is `Exception`.

## Shape

- Retained historical artifact.
- No live writer.
- No live reader.
- No live decision consumes it.

## Connected to

- **owns:** nothing in the live system.
- **owned-by:** archive only.
- **joins:** no live object.
- **looks-like-but-is-not:** the live `Exception` register.

## If you change this

- **Hits:** nothing in the live close workflow.
- **Does not hit:** live exception status; follow-up ownership; review readiness; close completion.

## Surfaces

| Surface | Role |
|---|---|
| Live workflow | none |
| Archive | retains name only |

## See

- Source: `../../../demo-territory/client-workspace/archive/Missing Documents.xlsx.note.md`
- Source: `../../../demo-territory/client-workspace/intake-rules.md`


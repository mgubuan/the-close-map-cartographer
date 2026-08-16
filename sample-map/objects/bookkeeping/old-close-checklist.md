---
type: object
cluster: bookkeeping
universe: ghost
status: verified
verified_on: 2026-08-16
revision: monthly-close-v2
source_revision: fd52389ac7ddf95244ad93f039573b402e900e56
entity: demo-territory/client-workspace/archive/Old Close Checklist.xlsx.note.md
---

# Old Close Checklist

A retired workbook whose official-looking name remains visible but has no current writer, reader, or downstream decision.

## Why this shape

It remains a card because plausible old names are tripwires for new bookkeepers and cold models.

## Shape

- Archived filename and explicit no-current-use note.

## Connected to

- **owns:** nothing live.
- **owned-by:** historical archive only.
- **joins:** no live close object.
- **looks-like-but-is-not:** the current `Client Records Ready` control.

## If you change this

- **Hits:** nothing in the live monthly close.
- **Does not hit:** current status; reconciliations; review readiness; report delivery.
- **Open next only if:** current records-readiness status is needed → `client-records-ready.md`.
- **Stop:** after confirming the file has no current writer, reader, or downstream decision.

## Surfaces

| Surface | Role |
|---|---|
| Historical archive | retains only |

## See

- Source: `../../../demo-territory/client-workspace/archive/Old Close Checklist.xlsx.note.md`

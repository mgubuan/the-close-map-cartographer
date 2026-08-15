---
type: object
cluster: bookkeeping
universe: live
status: verified
verified_on: 2026-08-15
revision: demo-v1
entity: demo-territory/client-workspace/intake-rules.md
---

# Source Document

Evidence received through an allowed channel and assigned a stable workspace, period, type, and source identity.

## Why this shape

Identity must remain stable when the intake channel changes; arrival through email or a portal is not itself the document's operational identity.

## Shape

- Accepted channels: controlled intake email or client portal.
- Required identity: workspace ID, period, document type, source reference.
- Blocking conditions become live exceptions.

## Connected to

- **owns:** source reference used by a review packet.
- **owned-by:** `Client Workspace` until linked to work.
- **joins:** `Exception`, `Review Packet`.
- **looks-like-but-is-not:** a document in a folder is not proof of review or approval.

## If you change this

- **Hits:** intake location and permissions; identity and naming; duplicate detection; missing-evidence exception creation; review-packet source links.
- **Does not hit:** chart of accounts; reconciliation logic; reviewer approval threshold; financial-report format.

## Surfaces

| Surface | Role |
|---|---|
| Intake channel | writes evidence |
| Bookkeeper | reads, identifies, links |
| Review packet | reads source reference |

## See

- Source: `../../../demo-territory/client-workspace/intake-rules.md`
- Source: `../../../demo-territory/client-workspace/review-packet-schema.md`


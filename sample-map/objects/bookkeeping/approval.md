---
type: object
cluster: bookkeeping
universe: live
status: verified
verified_on: 2026-08-15
revision: monthly-close-v1
entity: demo-territory/client-workspace/approval-register.csv
---

# Approval

The explicit `approved` event showing that the CAS Manager accepted revision 2 of `PK-CRHS-2026-07` at a recorded time after returning revision 1.

## Why this shape

Approval needs an explicit actor, target, status, and timestamp; folder placement and filenames cannot establish the control.

## Shape

- Approval-event ID, packet ID, packet revision, reviewer role, status, timestamp, and note reference.
- An event history that preserves both return and approval.

## Connected to

- **owns:** explicit acceptance state for one packet.
- **owned-by:** named reviewer.
- **joins:** `Review Packet`.
- **looks-like-but-is-not:** an `Approved` folder or reviewed filename.

## If you change this

- **Hits:** approval schema; close readiness for the packet; delivery eligibility; reopening rules.
- **Does not hit:** source-document contents; prior periods; other packets; client acceptance unless separately recorded.

## Surfaces

| Surface | Role |
|---|---|
| CAS Manager | writes return or approval event |
| Close readiness | reads approval |
| Delivery control | reads approval |

## See

- Source: `../../../demo-territory/client-workspace/approval-register.csv`
- Source: `../../../demo-territory/client-workspace/review-packet-schema.md`
- Source: `../../../demo-territory/client-workspace/review-packet-2026-07.md`

---
type: object
cluster: bookkeeping
universe: live
status: verified
verified_on: 2026-08-15
revision: demo-v1
entity: demo-territory/client-workspace/approval-register.csv
---

# Approval

Explicit evidence in `approval-register.csv` that a named reviewer accepted a defined review packet at a recorded time.

## Why this shape

Approval needs an explicit actor, target, status, and timestamp; folder placement and filenames cannot establish the control.

## Shape

- Approval ID, packet ID, reviewer, status, recorded timestamp.
- Exactly one defined packet target.

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
| Reviewer | writes approval |
| Close readiness | reads approval |
| Delivery control | reads approval |

## See

- Source: `../../../demo-territory/client-workspace/approval-register.csv`
- Source: `../../../demo-territory/client-workspace/review-packet-schema.md`


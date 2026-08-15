---
type: object
cluster: bookkeeping
universe: live
status: verified
verified_on: 2026-08-15
revision: demo-v1
entity: demo-territory/client-workspace/exception-register.csv
---

# Exception

An unresolved condition, represented in `exception-register.csv`, that blocks a defined item from becoming review-ready.

## Why this shape

The blocker needs its own identity, affected item, owner, and status so it can move independently without implying that every client record is blocked.

## Shape

- Keys: exception ID, workspace ID, period, affected item, type, owner, status.
- Current live system: `exception-register.csv`.

## Connected to

- **owns:** current follow-up status for one affected item.
- **owned-by:** named exception assignee.
- **joins:** `Source Document`, `Review Packet`.
- **looks-like-but-is-not:** `Missing Documents.xlsx` is a ghost tracker, not this live object.

## If you change this

- **Hits:** exception queue; follow-up ownership; review readiness for the affected item; open-exception packet disclosure.
- **Does not hit:** every document for the client; unrelated accounts or periods; final approval before resolution is verified.

## Surfaces

| Surface | Role |
|---|---|
| Intake triage | writes |
| Bookkeeper | reads and writes |
| Reviewer | reads disclosed exceptions |

## See

- Source: `../../../demo-territory/client-workspace/exception-register.csv`
- Source: `../../../demo-territory/client-workspace/intake-rules.md`


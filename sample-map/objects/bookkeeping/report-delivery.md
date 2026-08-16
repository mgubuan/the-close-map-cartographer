---
type: object
cluster: bookkeeping
universe: live
status: verified
verified_on: 2026-08-16
revision: monthly-close-v2
entity: demo-territory/client-workspace/close-delivery-register.csv
---

# Report Delivery

The versioned release of reviewed financial reports to an approved recipient with a controlled reopen rule.

## Why this shape

Delivery is an event, not a folder name; preserving version, recipient, time, and reopen authority prevents silent replacement.

## Shape

- Workspace, period, version, status, reviewer, recipient, timestamp, and reopen rule.

## Connected to

- **owns:** the delivered version and replacement history.
- **owned-by:** the approving reviewer.
- **joins:** `Bookkeeping Review` and every upstream control reopened by a later change.
- **looks-like-but-is-not:** a PDF in a delivery folder is not evidence it was reviewed or sent.

## If you change this

- **Hits:** approval; recipients; report versioning; reopen log; client notification.
- **Does not hit:** current work for other clients; unchanged reports; future periods without carryforward impact.

## Surfaces

| Surface | Role |
|---|---|
| Reviewer | writes release approval |
| Client contact | reads delivered reports |

## See

- Source: `../../../demo-territory/client-workspace/close-delivery-register.csv`

---
type: object
cluster: bookkeeping
universe: live
status: verified
verified_on: 2026-08-15
revision: demo-v1
entity: demo-territory/client-workspace/review-packet-schema.md
---

# Review Packet

The bounded work records, evidence links, reconciliations, and disclosed exceptions handed to one reviewer for one workspace and period.

## Why this shape

A bounded packet makes the review target explicit; it prevents a folder or an entire client history from becoming an ambiguous approval surface.

## Shape

- Packet ID, workspace, period, preparer, reviewer.
- Work-record IDs, source references, reconciliation evidence.
- Disclosed open exceptions and submitted timestamp.

## Connected to

- **owns:** the exact review boundary.
- **owned-by:** assigned preparer until submission, assigned reviewer during review.
- **joins:** `Source Document`, `Exception`, `Approval`.
- **looks-like-but-is-not:** a folder named `Approved` is not approval evidence.

## If you change this

- **Hits:** packet schema; preparer handoff; reviewer view; evidence links; disclosed exceptions; approval target.
- **Does not hit:** raw intake backlog; unrelated clients or periods; source-document contents; approval threshold unless the approval contract also changes.

## Surfaces

| Surface | Role |
|---|---|
| Bookkeeper | writes packet |
| Reviewer | reads packet |
| Approval register | names packet target |

## See

- Source: `../../../demo-territory/client-workspace/review-packet-schema.md`


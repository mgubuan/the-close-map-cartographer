---
type: object
cluster: bookkeeping
universe: live
status: verified
verified_on: 2026-08-16
revision: monthly-close-v2
entity: demo-territory/client-workspace/month-end-entry-log-2026-07.csv
---

# Month-end Entry

A supported recurring, correcting, or authorized external entry posted for the close period.

## Why this shape

Manual entries can change proven balances, so support, authority, and downstream reopening must travel with the entry.

## Shape

- Entry type, effective period, affected accounts, support, preparer, status, and approver.

## Connected to

- **owns:** the recorded adjustment and its support.
- **owned-by:** preparer within engagement scope and designated approver.
- **joins:** `Account Reconciliation`, `Key Balance Verification`, `Bookkeeping Review`.
- **looks-like-but-is-not:** a saved draft or CPA email is not a posted entry.

## If you change this

- **Hits:** affected account balances; related reconciliations; tie-outs; review; delivered reports when already issued.
- **Does not hit:** accounts outside the entry; unrelated client records; prior approved entries.
- **Open next only if:** the entry changes a completed review → `bookkeeping-review.md`.
- **Stop:** when support, date, accounts, amount, authority, posting status, and reopened controls are explicit.

## Surfaces

| Surface | Role |
|---|---|
| Bookkeeper | writes approved entries |
| CPA or reviewer | writes authority, reads result |

## See

- Source: `../../../demo-territory/client-workspace/month-end-entry-log-2026-07.csv`

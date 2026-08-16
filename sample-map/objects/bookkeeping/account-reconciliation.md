---
type: object
cluster: bookkeeping
universe: live
status: verified
verified_on: 2026-08-16
revision: monthly-close-v2
entity: demo-territory/client-workspace/reconciliation-register-2026-07.csv
---

# Account Reconciliation

The period control tying each bank, credit-card, loan, and selected balance-sheet account to independent support.

## Why this shape

Each account must move independently because a change can reopen one reconciliation without invalidating all others.

## Shape

- Account type, period, status, preparer, reviewer, and evidence.

## Connected to

- **owns:** proven account balances.
- **owned-by:** the preparer and reviewer.
- **joins:** `Transaction Completion`, `Key Balance Verification`, `Month-end Entry`.
- **looks-like-but-is-not:** a matching bank-feed balance is not a reconciliation.

## If you change this

- **Hits:** account frequency; evidence; risk classification; reviewer workload; downstream review status.
- **Does not hit:** transaction category policy; client request deadlines; delivery contacts.

## Surfaces

| Surface | Role |
|---|---|
| Bookkeeper | writes reconciliation |
| Reviewer | reads evidence, writes sign-off |

## See

- Source: `../../../demo-territory/client-workspace/reconciliation-register-2026-07.csv`

---
type: object
cluster: bookkeeping
universe: live
status: verified
verified_on: 2026-08-16
revision: monthly-close-v2
entity: demo-territory/client-workspace/transaction-review-2026-07.csv
---

# Transaction Completion

The verified state that period activity is posted, matched, supported, categorized, and checked for duplicates and wrong-period items.

## Why this shape

Downloaded is not complete; completion requires explicit controls whose status can be reviewed independently.

## Shape

- Control, status, owner, and evidence reference for one workspace and period.

## Connected to

- **owns:** transaction-ready input to reconciliation.
- **owned-by:** `Client Records Ready` and the preparer.
- **joins:** `Account Reconciliation`, `Key Balance Verification`.
- **looks-like-but-is-not:** a cleared bank feed is not a completed transaction review.

## If you change this

- **Hits:** posting settings; preparer workload; support rules; transaction-complete sign-off; affected reconciliations.
- **Does not hit:** statement deadlines; report recipients; unrelated account controls.

## Surfaces

| Surface | Role |
|---|---|
| Bookkeeper | writes completion evidence |
| Reviewer | reads exceptions and sign-off |

## See

- Source: `../../../demo-territory/client-workspace/transaction-review-2026-07.csv`

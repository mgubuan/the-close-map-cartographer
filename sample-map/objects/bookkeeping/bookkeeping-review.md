---
type: object
cluster: bookkeeping
universe: live
status: verified
verified_on: 2026-08-16
revision: monthly-close-v2
entity: demo-territory/client-workspace/close-review-2026-07.md
---

# Bookkeeping Review

The bounded review of balance-sheet reasonableness, profit-and-loss variances, owner activity, payroll expense, and disclosed exceptions.

## Why this shape

A review must name its tests and thresholds; opening a report is not evidence that unusual balances were investigated.

## Shape

- Review tests, thresholds, explanations, open exceptions, reviewer, and status.

## Connected to

- **owns:** review notes and sign-off.
- **owned-by:** the assigned senior reviewer.
- **joins:** every upstream close control and `Report Delivery`.
- **looks-like-but-is-not:** report access is not review completion.

## If you change this

- **Hits:** comparison rules; explanation requirements; reviewer workload; sign-off criteria; delivery readiness.
- **Does not hit:** transaction posting rules; statement deadlines; delivery channel.

## Surfaces

| Surface | Role |
|---|---|
| Bookkeeper | reads returned notes, writes corrections |
| Reviewer | reads reports, writes sign-off |

## See

- Source: `../../../demo-territory/client-workspace/close-review-2026-07.md`

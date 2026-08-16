---
type: object
cluster: bookkeeping
universe: live
status: verified
verified_on: 2026-08-16
revision: monthly-close-v2
source_revision: fd52389ac7ddf95244ad93f039573b402e900e56
entity: demo-territory/client-workspace/balance-verification-2026-07.csv
---

# Key Balance Verification

The comparison of AR, AP, payroll liabilities, sales tax, loans, clearing accounts, and other scoped balances to their supporting reports.

## Why this shape

Not every important balance is proven by a bank reconciliation; each needs its own authoritative report and tolerance.

## Shape

- Balance, ledger value reference, support reference, difference, owner, and review status.

## Connected to

- **owns:** supported subledger and liability balances.
- **owned-by:** the close reviewer.
- **joins:** `Month-end Entry`, `Bookkeeping Review`.
- **looks-like-but-is-not:** a zero balance is not proof that the control was performed.

## If you change this

- **Hits:** required reports; tolerance; difference ownership; balance-sheet review checklist.
- **Does not hit:** unrelated reconciliations; report delivery channel; client intake method.
- **Open next only if:** resolving a difference requires a supported entry → `month-end-entry.md`.
- **Stop:** when source report, ledger accounts, tolerance, owner, reviewer, and difference treatment are explicit.

## Surfaces

| Surface | Role |
|---|---|
| Bookkeeper | writes tie-out |
| Reviewer | reads difference and approves status |

## See

- Source: `../../../demo-territory/client-workspace/balance-verification-2026-07.csv`

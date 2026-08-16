---
type: process
universe: live
status: verified
verified_on: 2026-08-16
revision: monthly-close-v2
consumes:
  - ../objects/bookkeeping/client-records-ready.md
produces:
  - ../objects/bookkeeping/report-delivery.md
---

# Records to Delivery

The proven movement that takes one client period from received records to reviewed, versioned financial reports.

## Input

- `Client Records Ready`

## Movement

1. Confirm required records or owned exceptions. Source: `../../demo-territory/client-workspace/close-checklist-2026-07.md`.
2. Complete transaction review. Source: `../../demo-territory/client-workspace/transaction-review-2026-07.csv`.
3. Reconcile accounts and verify key balances. Sources: `reconciliation-register-2026-07.csv` and `balance-verification-2026-07.csv`.
4. Post supported month-end entries and refresh affected controls. Source: `../../demo-territory/client-workspace/month-end-entry-log-2026-07.csv`.
5. Review books, resolve or disclose exceptions, and deliver one approved version. Sources: `close-review-2026-07.md` and `close-delivery-register.csv`.

## Output

- `Report Delivery`

## If you change this

- **Hits:** step ownership; completion evidence; downstream reopening; review readiness; report versioning.
- **Does not hit:** tax policy; accounting-policy decisions; unrelated client periods.

## Surfaces

| Surface | Role |
|---|---|
| Bookkeeper | prepares and records evidence |
| Senior reviewer | reviews, returns, and approves |
| Client contact | supplies records and reads reports |

## See

- Source: `../../demo-territory/client-workspace/close-checklist-2026-07.md`
- Source: `../../demo-territory/client-workspace/transaction-review-2026-07.csv`
- Source: `../../demo-territory/client-workspace/reconciliation-register-2026-07.csv`
- Source: `../../demo-territory/client-workspace/balance-verification-2026-07.csv`
- Source: `../../demo-territory/client-workspace/month-end-entry-log-2026-07.csv`
- Source: `../../demo-territory/client-workspace/close-review-2026-07.md`
- Source: `../../demo-territory/client-workspace/close-delivery-register.csv`

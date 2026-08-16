---
type: process
universe: live
status: verified
verified_on: 2026-08-16
revision: monthly-close-v2
source_revision: fd52389ac7ddf95244ad93f039573b402e900e56
consumes:
  - ../objects/bookkeeping/client-records-ready.md
produces:
  - ../objects/bookkeeping/report-delivery.md
---

# Records to Delivery

The proven monthly-close movement that takes one client period from received records to reviewed, versioned financial reports.

## Input → Movement → Output

**Input:** `Client Records Ready` supplies the bounded period, required records, owners, and disclosed exceptions.

**Movement:** The bookkeeper completes seven human-reviewed gates in order; a failed or reopened gate invalidates only the dependent work identified by the relevant object card.

**Output:** `Report Delivery` records the approved version, recipient, delivery evidence, and reopening history.

## Why this shape

The close is one real operating movement with seven independently reviewable controls. Treating it as a single checkbox would hide incomplete evidence; treating every checklist row as a separate process would duplicate the source workflow.

## Steps

1. Confirm required records or owned exceptions. Source: `../../demo-territory/client-workspace/close-checklist-2026-07.md`.
2. Complete transaction review. Source: `../../demo-territory/client-workspace/transaction-review-2026-07.csv`.
3. Reconcile accounts and verify key balances. Sources: `../../demo-territory/client-workspace/reconciliation-register-2026-07.csv` and `../../demo-territory/client-workspace/balance-verification-2026-07.csv`.
4. Post supported month-end entries and refresh affected controls. Source: `../../demo-territory/client-workspace/month-end-entry-log-2026-07.csv`.
5. Review books, resolve or disclose exceptions, and deliver one approved version. Sources: `../../demo-territory/client-workspace/close-review-2026-07.md` and `../../demo-territory/client-workspace/close-delivery-register.csv`.

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

- Objects: `../objects/bookkeeping/client-records-ready.md` → `../objects/bookkeeping/transaction-completion.md` → `../objects/bookkeeping/account-reconciliation.md` → `../objects/bookkeeping/key-balance-verification.md` → `../objects/bookkeeping/month-end-entry.md` → `../objects/bookkeeping/bookkeeping-review.md` → `../objects/bookkeeping/report-delivery.md`
- Source: `../../demo-territory/client-workspace/close-checklist-2026-07.md`
- Source: `../../demo-territory/client-workspace/transaction-review-2026-07.csv`
- Source: `../../demo-territory/client-workspace/reconciliation-register-2026-07.csv`
- Source: `../../demo-territory/client-workspace/balance-verification-2026-07.csv`
- Source: `../../demo-territory/client-workspace/month-end-entry-log-2026-07.csv`
- Source: `../../demo-territory/client-workspace/close-review-2026-07.md`
- Source: `../../demo-territory/client-workspace/close-delivery-register.csv`

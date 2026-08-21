# Worked Map: Demo Bookkeeping Close

This worked map uses a privacy-safe reconstruction of recurring monthly-close work directly operated and supervised during more than twenty years of controllership. The example client and record contents are synthetic; the operating controls and handoffs reflect real close work. Source records remain authoritative.

## Catalog

| Change intent | Open first |
|---|---|
| Change required records or deadlines | `map/objects/bookkeeping/client-records-ready.md` |
| Change transaction review | `map/objects/bookkeeping/transaction-completion.md` |
| Change reconciliation frequency | `map/objects/bookkeeping/account-reconciliation.md` |
| Add a balance tie-out | `map/objects/bookkeeping/key-balance-verification.md` |
| Change manual-entry rules | `map/objects/bookkeeping/month-end-entry.md` |
| Change review thresholds | `map/objects/bookkeeping/bookkeeping-review.md` |
| Change report delivery or reopening | `map/objects/bookkeeping/report-delivery.md` |

## Card excerpt: Client Records Ready

- **Universe:** live
- **Source:** `demo-territory/client-workspace/close-checklist-2026-07.md`
- **Hits:** request schedule, reminders, missing-record ownership, reconciliation start, close target.
- **Does not hit:** transaction categories, review thresholds, prior delivered reports.

## Card excerpt: Report Delivery

- **Universe:** live
- **Source:** `demo-territory/client-workspace/close-delivery-register.csv`
- **Hits:** approval, recipients, versioning, reopen log, client notification.
- **Does not hit:** other clients, unchanged reports, unrelated periods.

## Ghost card: Old Close Checklist

- **Universe:** ghost
- **Evidence:** the archive note names no current writer, reader, or downstream decision.
- **Hits:** nothing in the live close workflow.

## One change

Question: What moves if low-risk accounts change from monthly to quarterly reconciliation?

```text
Primary card: Account Reconciliation

HITS
- account risk classification
- monthly close checklist
- quarterly schedule
- reviewer visibility

DOES NOT HIT
- bank and credit-card monthly rules
- transaction categorization
- report recipients

OPEN NEXT ONLY IF
- a supported balance changes -> Key Balance Verification

STOP
- stop when eligible accounts, risk limits, approval, due dates, and return-to-monthly rule are explicit
```

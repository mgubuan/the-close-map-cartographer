# Change-Impact Catalog

Open one primary card. Open a second only when the primary card requires it.

| If you are changing… | Open first | Open next only if… |
|---|---|---|
| required records, deadlines, or reminders | `../objects/bookkeeping/client-records-ready.md` | transaction readiness changes → `transaction-completion.md` |
| posting, matching, categorization, or transaction review | `../objects/bookkeeping/transaction-completion.md` | an account balance changes → `account-reconciliation.md` |
| reconciliation frequency, evidence, or review | `../objects/bookkeeping/account-reconciliation.md` | a supported balance changes → `key-balance-verification.md` |
| AR, AP, payroll, tax, loan, or clearing tie-outs | `../objects/bookkeeping/key-balance-verification.md` | an entry is required → `month-end-entry.md` |
| recurring, correcting, or externally approved entries | `../objects/bookkeeping/month-end-entry.md` | statements change → `bookkeeping-review.md` |
| variance thresholds, reasonableness, or reviewer rules | `../objects/bookkeeping/bookkeeping-review.md` | delivery readiness changes → `report-delivery.md` |
| recipients, versions, delivery, or reopening | `../objects/bookkeeping/report-delivery.md` | an upstream control is invalidated → open only that card |
| whether the old checklist controls live work | `../objects/bookkeeping/old-close-checklist.md` | current status is needed → `client-records-ready.md` |

If no row matches, stop with `UNKNOWN / Catalog Gap`. Do not infer a waterfall.

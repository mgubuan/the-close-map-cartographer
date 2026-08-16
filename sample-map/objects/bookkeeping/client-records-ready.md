---
type: object
cluster: bookkeeping
universe: live
status: verified
verified_on: 2026-08-16
revision: monthly-close-v2
source_revision: fd52389ac7ddf95244ad93f039573b402e900e56
entity: demo-territory/client-workspace/close-checklist-2026-07.md
---

# Client Records Ready

The period-specific gate showing whether every required statement, report, receipt set, and client answer is received or represented by an owned exception.

## Why this shape

Receipt alone is not readiness; each requirement needs a period, due date, owner, affected account, and blocking decision.

## Shape

- Required record, due date, status, owner, affected account, blocking status.

## Connected to

- **owns:** the input boundary for `Transaction Completion`.
- **owned-by:** the current close checklist.
- **joins:** `Transaction Completion`, `Account Reconciliation`.
- **looks-like-but-is-not:** a bank-feed connection is not a received statement.

## If you change this

- **Hits:** client request schedule; reminders; missing-record ownership; earliest reconciliation date; close target.
- **Does not hit:** transaction category rules; review thresholds; delivered prior-period reports.
- **Open next only if:** the definition of transaction-ready changes → `transaction-completion.md`.
- **Stop:** when requirements, owners, due dates, reminders, exceptions, and close-timing consequences are explicit.

## Surfaces

| Surface | Role |
|---|---|
| Client contact | writes records and answers |
| Bookkeeper | reads requirements, writes status |

## See

- Source: `../../../demo-territory/client-workspace/close-checklist-2026-07.md`

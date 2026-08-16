# The Close Map

**Change one part of the close. Know what else must change. Load nothing you do not need.**

The Close Map is a folder-based cartographer for a bookkeeping firm’s monthly close. It gives a newly hired bookkeeper or cold AI model a small set of doors into one realistic July close without copying client data or loading the entire operation.

## Live demonstration

[Open the bookkeeping Close Map →](https://intelligencesolved.com/close-map)

The demo and this repository share the same territory:

1. Client Records Ready
2. Transaction Completion
3. Account Reconciliation
4. Key Balance Verification
5. Month-end Entry
6. Bookkeeping Review
7. Report Delivery
8. Old Close Checklist — a named file with no live wiring

## What is here

```text
cartographer/       Drop-in instructions that create a map
demo-territory/     Privacy-safe source records for one July close
sample-map/         The source-cited map left by the cartographer
audit/              Inventory completed before cards were written
validate_close_map.py
test-results.md
```

The deliverable is `cartographer/`. Point it at a real, sanitized body of work. It inventories the territory, creates a small catalog, writes source-cited noun cards, proves one movement, records change impact, and gives a later reader a stopping rule.

## Front door

| If you need to change… | Open |
|---|---|
| Required records, deadlines, or reminders | `sample-map/objects/bookkeeping/client-records-ready.md` |
| Posting, matching, or transaction review | `sample-map/objects/bookkeeping/transaction-completion.md` |
| Reconciliation frequency or evidence | `sample-map/objects/bookkeeping/account-reconciliation.md` |
| AR, AP, payroll, tax, loan, or clearing checks | `sample-map/objects/bookkeeping/key-balance-verification.md` |
| Supported month-end entries | `sample-map/objects/bookkeeping/month-end-entry.md` |
| Review thresholds or sign-off | `sample-map/objects/bookkeeping/bookkeeping-review.md` |
| Delivery, versioning, or reopening | `sample-map/objects/bookkeeping/report-delivery.md` |
| Whether the old checklist is current | `sample-map/objects/bookkeeping/old-close-checklist.md` |

Every card explains what the noun is, why it has that shape, what a change affects, what it does not affect, who reads or writes it, and which source wins when the map disagrees.

## How a cold reader walks

1. Open `sample-map/CLAUDE.md`.
2. Use `sample-map/effects/CONTEXT.md` to choose one card.
3. Open that card and one cited source.
4. Open another card only when the first card requires it.
5. Stop at first-order impact.

Never load the entire objects folder.

## Privacy boundary

The demonstration is a sanitized composite. Identities, dates, and contents are synthetic. The map cites paths, schemas, headings, and controls; it does not copy credentials, tax identifiers, account numbers, balances, transaction contents, or client-identifying values.

## Validate

```bash
python validate_close_map.py
```

The validator checks structure, entry twins, the closed schema, eight cards, one movement, source citations, status vocabulary, privacy boundaries, and public-language constraints.

Built and maintained by [Intelligence Solved](https://intelligencesolved.com/).

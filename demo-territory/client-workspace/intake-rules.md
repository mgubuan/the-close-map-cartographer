# Monthly Close Intake Rules

## Expected evidence

| Evidence | Expected by | Accepted source |
|---|---:|---|
| Operating-bank statement | Business day 3 | Client portal |
| Business-card statement | Business day 3 | Client portal |
| Payroll register and cash report | Business day 4 | Payroll-provider export in client portal |
| Merchant settlement report | Business day 4 | Client portal |
| Loan statement | Business day 5 | Client portal |
| Vendor support requested during coding | As requested | Portal or controlled intake email |

## Identity before use

Every accepted file receives a stable `document_id`, workspace, close period, evidence type, source channel, received timestamp, and storage reference in `source-document-index.csv`. A file sitting in Downloads, an inbox, or a client-named folder is not close evidence until it has that identity.

Files are duplicate candidates when workspace, period, evidence type, and source reference match an existing row. A replacement receives its own ID and points to the superseded record; it does not silently overwrite history.

## Exceptions

Create or update `exception-register.csv` when expected evidence is late, unreadable, duplicated, belongs to the wrong period, cannot be matched, or needs client clarification. Each exception must name one affected item, one owner, one next action, a due date, and a status.

`archive/Missing Documents.xlsx.note.md` is retained historical context. It is not the live follow-up queue.

## Review readiness

A missing item does not automatically block the entire close. The Senior Bookkeeper decides whether it blocks a named work record, must be disclosed in the review packet, or can remain open after submission. Reviewer approval remains separate from evidence receipt and review readiness.

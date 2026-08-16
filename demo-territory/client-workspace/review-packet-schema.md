# Review Packet Contract

A review packet is the bounded handoff for exactly one workspace and close period. It is not the client folder, the QBO file, or every document received during the month.

## Required header

- packet ID, workspace, and period;
- preparer and reviewer roles;
- submitted timestamp and packet revision;
- overall state: `draft`, `submitted`, `returned`, or `approved`.

## Required contents

- completed work-record IDs for bank, card, payroll, merchant, loan, and close-review work;
- source-document references supporting those work records;
- reconciliation evidence references without copied balances;
- material review notes and preparer responses;
- every open exception that affects reviewer judgment or delivery readiness;
- explicit items excluded from this packet.

## Return and resubmission

A reviewer return does not erase the original submission. The packet revision increments, the review note remains visible, and the preparer resubmits the same packet identity.

A folder named `Approved`, a checked checklist, or a reviewer opening the packet is not approval. Approval exists only as an `approved` event in `approval-register.csv` naming the packet revision, reviewer, and timestamp.

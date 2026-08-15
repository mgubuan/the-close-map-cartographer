# Worked Map: Demo Bookkeeping Close

This is one worked map of the supplied synthetic territory. The subject source remains authoritative.

## Catalog

| Change intent | Open first |
|---|---|
| Change where evidence arrives | `map/objects/bookkeeping/source-document.md` |
| Change missing-information ownership | `map/objects/bookkeeping/exception.md` |
| Change the review handoff | `map/objects/bookkeeping/review-packet.md` |
| Change what counts as approved | `map/objects/bookkeeping/approval.md` |
| Decide whether an old tracker is live | `map/objects/bookkeeping/missing-documents-tracker.md` |

## Card excerpt: Source Document

- **Universe:** live
- **Source:** `demo-territory/client-workspace/intake-rules.md`
- **Hits:** intake location, identity, duplicate detection, missing-evidence exceptions, review-packet evidence links.
- **Does not hit:** chart of accounts, reconciliation logic, approval threshold, report format.

## Card excerpt: Review Packet

- **Universe:** live
- **Source:** `demo-territory/client-workspace/review-packet-schema.md`
- **Hits:** packet schema, preparer handoff, reviewer view, approval target.
- **Does not hit:** raw intake backlog, unrelated periods, source-document contents.

## Ghost card: Missing Documents Tracker

- **Universe:** ghost
- **Evidence:** retained file note plus the current intake rule.
- **Why:** the workbook still has an authoritative name, but no live control writes it, reads it, or decides from it.
- **Hits:** nothing in the live close workflow.

## One change

Question: What moves if statements stop arriving by email and start arriving through the portal?

```text
Primary card: Source Document

HITS
- intake location and permissions
- document identity and naming
- duplicate detection
- missing-document exception creation
- review-packet source links

DOES NOT HIT
- chart of accounts
- reconciliation rules
- reviewer approval threshold
- financial-report format

OPEN NEXT ONLY IF
- ownership changes → Exception
- evidence presented to review changes → Review Packet

STOP
- stop when intake, identity, duplicate, exception, and review-link consequences are known
```


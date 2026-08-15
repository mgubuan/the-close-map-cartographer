---
type: process
universe: live
status: verified
verified_on: 2026-08-15
revision: demo-v1
consumes:
  - ../objects/bookkeeping/client-workspace.md
  - ../objects/bookkeeping/source-document.md
produces:
  - ../objects/bookkeeping/exception.md
  - ../objects/bookkeeping/review-packet.md
---

# Document to Review

The live movement that identifies received evidence, represents blocking conditions, and assembles a bounded packet for review.

## Input

- `Client Workspace`
- `Source Document`

## Movement

1. Accept evidence through an allowed channel and assign workspace, period, type, and source identity. Source: `../../demo-territory/client-workspace/intake-rules.md`.
2. Create or update an exception when evidence is missing, unreadable, duplicated, or unmatched. Source: `../../demo-territory/client-workspace/intake-rules.md`.
3. Assemble the defined work and evidence references into one review packet. Source: `../../demo-territory/client-workspace/review-packet-schema.md`.

## Output

- `Exception` when a blocking condition exists.
- `Review Packet` when the bounded handoff is assembled.

## If you change this

- **Hits:** intake identity, exception creation, packet membership, preparer-to-reviewer handoff.
- **Does not hit:** accounting treatment, chart of accounts, reviewer approval authority, client acceptance.

## Surfaces

| Surface | Role |
|---|---|
| Intake channel | writes source evidence |
| Bookkeeper | identifies evidence, writes exceptions, assembles packet |
| Reviewer | reads packet |

## See

- Source: `../../demo-territory/client-workspace/intake-rules.md`
- Source: `../../demo-territory/client-workspace/review-packet-schema.md`


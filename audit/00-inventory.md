# Slice 0 — Complete Pre-change Inventory

Inventory completed: 2026-08-16. Source snapshot: `fd52389ac7ddf95244ad93f039573b402e900e56`.

The repeating unit is one client's monthly bookkeeping close. The map form is a system map: durable close controls are the nouns, the records-to-delivery close is the proven movement, and the effects catalog routes change questions.

This inventory was completed before the alignment changes documented in `02-migration-map.md`. No source file is deleted by the migration.

## Subject territory

| Source | Last changed | Role | Universe | What refers to it / decision |
|---|---|---|---|---|
| `workspace-manifest.md` | 2026-08-15 | catalog | leftover | Prior intake-and-packet model; retained as revision history and explicitly superseded by the current checklist. |
| `intake-rules.md` | 2026-08-15 | contract | leftover | Prior evidence-intake model; referenced by the prior manifest and retained for historical context. |
| `source-document-index.csv` | 2026-08-15 | product | leftover | Prior document-level evidence log; no current workflow card uses it. |
| `exception-register.csv` | 2026-08-15 | product | leftover | Prior missing-item queue; no current workflow card uses it. |
| `review-packet-schema.md` | 2026-08-15 | factory | leftover | Prior handoff schema; retained with its packet example. |
| `review-packet-2026-07.md` | 2026-08-15 | product | leftover | Prior preparer-to-reviewer packet; replaced by the current review record. |
| `approval-register.csv` | 2026-08-15 | product | leftover | Prior packet approval log; replaced by named approval evidence in current controls. |
| `archive/Missing Documents.xlsx.note.md` | 2026-08-15 | dead | leftover | Historical spreadsheet note; intake rules say it is not the live queue. |
| `close-checklist-2026-07.md` | 2026-08-15 | contract | live | Owns the current seven-step close, scope, owners, timing, and completion gates. |
| `transaction-review-2026-07.csv` | 2026-08-15 | product | live | Source for `Transaction Completion`. |
| `reconciliation-register-2026-07.csv` | 2026-08-15 | product | live | Source for `Account Reconciliation`. |
| `balance-verification-2026-07.csv` | 2026-08-15 | product | live | Source for `Key Balance Verification`. |
| `month-end-entry-log-2026-07.csv` | 2026-08-15 | product | live | Source for `Month-end Entry`. |
| `close-review-2026-07.md` | 2026-08-15 | product | live | Source for `Bookkeeping Review`. |
| `close-delivery-register.csv` | 2026-08-15 | product | live | Source for `Report Delivery`. |
| `archive/Old Close Checklist.xlsx.note.md` | 2026-08-15 | dead | ghost | Named like a control but explicitly has no live writer, reader, or decision. |

## Repository areas

| Area | Role | Decision |
|---|---|---|
| `README.md`, `PROJECT-SUMMARY.md` | catalog | Keep owner-facing; route AI workflow questions to the map entry. |
| `cartographer/` | factory | Keep structurally separate from the filled example. |
| `sample-map/CLAUDE.md` | catalog | Keep as the canonical map entry. |
| `sample-map/AGENTS.md`, `sample-map/routing.md` | catalog | Generate from `CLAUDE.md`; never hand-edit. |
| `sample-map/CONTEXT.md`, shelf `CONTEXT.md` files | contract | Keep exact reads, job, writes, and human checks. |
| `sample-map/_meta/`, `sample-map/_templates/` | factory | Add immutable source-revision requirements. |
| `sample-map/objects/` | product | Keep eight demonstrated nouns; generate the index. |
| `sample-map/processes/` | product | Keep one proven end-to-end movement and make Input → Movement → Output explicit. |
| `sample-map/effects/` | catalog | Keep routing-only; no copied impact narratives. |
| `audit/` | product | Keep evidence of inventory, migration approval, and cold walk. |
| `validate_close_map.py` | factory | Expand to validate provenance, generated artifacts, links, and bounded reading. |
| `generate_close_map.py` | factory | Add deterministic index and routing-twin generation. |
| `ARCHITECTURE-VERIFICATION.md`, `test-results.md` | product | Refresh after validation. |

## Approved target

- One `bookkeeping` object cluster.
- Seven live controls, one ghost control, and eight explicitly classified leftover source files.
- One canonical entry file with two generated twins.
- One generated noun index.
- One traceable source snapshot on every verified card.
- No additional object cards for files that are merely evidence containers rather than durable close controls.

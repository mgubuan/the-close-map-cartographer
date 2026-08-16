# Approved Migration Map

Approved by the repository owner on 2026-08-16 with the instruction to proceed.

## Structural decision

The existing shape is retained because it already separates the reusable factory, authoritative bookkeeping territory, map, and audit evidence. The migration tightens provenance and generation rather than renaming audience-facing folders.

| Current path | Target path | Role | Action |
|---|---|---|---|
| `demo-territory/client-workspace/workspace-manifest.md` | same | catalog / leftover | Mark as superseded prior-state orientation and route to the current checklist. |
| Eight prior intake-and-packet files | same | factory/product/dead / leftover | Retain, classify, and prevent them from impersonating the live close. |
| Seven current close sources | same | contract/product / live | Freeze at the recorded source snapshot. |
| Retired checklist note | same | dead / ghost | Retain as the deliberate false-door test. |
| `sample-map/CLAUDE.md` | same | catalog | Remain the only hand-edited map entry. |
| `sample-map/AGENTS.md`, `sample-map/routing.md` | same | generated catalog | Rebuild byte-for-byte from `CLAUDE.md`. |
| `sample-map/objects/_index.md` | same | generated catalog | Rebuild deterministically from object frontmatter. |
| Verified cards | same | product | Add immutable source snapshot metadata. |
| `records-to-delivery.md` | same | product | Preserve one real monthly-close movement; make the three-part movement and its citations explicit. |
| `validate_close_map.py` | same | factory | Add drift, provenance, process-link, source-state, and token-budget checks. |
| new generator | `generate_close_map.py` | factory | Provide the only supported way to refresh generated catalogs. |

## Human gate result

No deletion, broad move, or speculative shelf was approved. Implementation may proceed only within the target above. Website and downloadable-package synchronization happens after the local repository passes generation, validation, privacy scanning, and the cold walk.

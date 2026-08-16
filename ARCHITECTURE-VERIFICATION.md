# Architecture Verification

Audited on 2026-08-15 against The Close Map's published operating contract.

## Product contract

| Requirement | Evidence |
|---|---|
| Folder-based cartographer | `cartographer/` is the reusable factory |
| Realistic, specific body of work | `demo-territory/client-workspace/` is a privacy-safe July close with records readiness, transaction review, reconciliations, balance checks, entries, review, delivery, and reopen rules |
| In-force territory | Source describes a current operating system, not a postmortem |
| Territory is not the mapping method | The subject is bookkeeping work; the method remains in the factory |
| Explicit identity | `identity.md` names cartographer, territory, human reader, and model reader |
| Explicit rules | `rules.md` defines nouns, movement, universes, citations, Hits, Does not hit, and no-slurp behavior |
| Complete worked example | `examples.md` shows catalog, two live cards, one ghost, and one change radius |
| Closed card types | `cartographer/reference/card-types.md` |
| Gated walk order | `cartographer/reference/walk-order.md` |
| Naming collisions | `cartographer/reference/naming-collisions.md` |
| Stranger-readable README | `cartographer/README.md` routes setup and enforces catalog → one card → source → stop |
| Catalog and doors | `sample-map/CLAUDE.md` and `sample-map/effects/CONTEXT.md` |
| Source citation, not second specification | Every verified card has `See`; validation resolves every cited path |
| Hits / Does not hit | Required and validated on every object and process card |
| Ghost marked | `missing-documents-tracker.md` is `universe: ghost` with evidence |

## Architecture invariants

| Invariant | Evidence |
|---|---|
| One folder, one job | Factory, subject, audit artifact, and map product are separate; object/process shelves have contracts |
| Small stable entry | `sample-map/CLAUDE.md` is under 60 lines and carries routing only |
| Numbering encodes order | Mapping slices are numbered 0–5; the inventory artifact is `00-inventory.md` |
| Explicit folder contracts | Root, object, process, and effects contracts state reading behavior and checks |
| Factory vs product | `cartographer/` is reusable; `sample-map/` is the filled product |
| Outputs are edit surfaces | Inventory, cards, indexes, and contracts are plain editable files |
| Load only what is needed | Entry and effects catalog route to one primary card and one cited source |
| Plain, linked, queryable | Markdown/YAML frontmatter and relative paths form the graph |
| Filesystem is state | Card frontmatter exposes universe/status; validation regenerates and checks the noun index |
| Instantiate by copying | `_templates/object.md` and `_templates/process.md` are the only card stamps |

## Cold-walk test

| Test | Result |
|---|---|
| Map is one hop from repository entry | Root README links the map and live demonstration |
| Colliding names resolve before a card | `sample-map/CONTEXT.md` defines Client, Statement, Complete, Reviewed, Owner, and the ghost tracker |
| One card states what, why, source, and waterfall | Enforced by `validate_close_map.py` |
| Effects catalog routes a stated change | Six change doors plus a safe catalog-gap result |
| `See` lands on subject source | Every citation is resolved during validation |
| Entry twins do not drift | Byte equality is enforced for `CLAUDE.md`, `AGENTS.md`, and `routing.md` |

## Honest boundary

Structural validation and browser behavior are proven. An independent cold-reader transcript remains a separate semantic test and is not fabricated.

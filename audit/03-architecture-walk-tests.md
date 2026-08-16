# Architecture Walk Tests

Tested: 2026-08-16 against source snapshot `fd52389ac7ddf95244ad93f039573b402e900e56`.

Each test begins at the owner-facing `README.md`, follows the AI starting route to `sample-map/CLAUDE.md`, selects one effects row and one primary card, and follows that card's single authoritative source. A second card is allowed only when the primary card's explicit gate is true.

| Question | Primary route | Source reached | Result and stop |
|---|---|---|---|
| What is account reconciliation? | `effects/CONTEXT.md` → `account-reconciliation.md` | `reconciliation-register-2026-07.csv` | PASS — definition, proof, owner, impact, and non-impact found; stopped at source. |
| What changes if a low-risk account reconciles quarterly? | `effects/CONTEXT.md` → `account-reconciliation.md` | `reconciliation-register-2026-07.csv` | PASS — frequency, risk criteria, evidence, review, and return-to-monthly trigger identified; no unsupported account list invented. |
| Is the old checklist active? | `effects/CONTEXT.md` → `old-close-checklist.md` | archived checklist note | PASS — ghost status and absence of live wiring found; current route points to Client Records Ready. |
| What changes if report delivery moves from business day ten to seven? | `effects/CONTEXT.md` → `report-delivery.md` | `close-delivery-register.csv` | PASS — delivery timing, approval readiness, recipient/version evidence, and reopening implications found; accounting policy excluded. |
| Where would a payroll-clearing tie-out be added? | `effects/CONTEXT.md` → `key-balance-verification.md` | `balance-verification-2026-07.csv` | PASS — tie-out belongs in key balance verification; month-end entry opens next only if the tie-out requires an entry. |
| What does changing the close reviewer affect? | `effects/CONTEXT.md` → `bookkeeping-review.md` | `close-review-2026-07.md` | PASS — review responsibility, return path, approval evidence, and delivery readiness found; preparer posting rules excluded. |
| What if no catalog row matches? | `effects/CONTEXT.md` | none | PASS — stops at `UNKNOWN / Catalog Gap` instead of inferring a workflow. |

## Reading budget

Automated estimates for `README.md` + map entry + one object card range from 2,005 to 2,081 tokens. The validator fails outside the 2,000–8,000-token bounded-walk range.

## Verdict

All seven routes pass. The map answers the named question without loading the object shelf, makes the first-order change radius explicit, and stops rather than inventing missing firm policy.

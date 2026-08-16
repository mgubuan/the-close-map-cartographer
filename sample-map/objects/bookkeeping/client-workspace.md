---
type: object
cluster: bookkeeping
universe: live
status: verified
verified_on: 2026-08-15
revision: monthly-close-v1
entity: demo-territory/client-workspace/workspace-manifest.md
---

# Client Workspace

The access and record boundary for the fictional `CRHS-042` July close: one client alias, one period, assigned bookkeeping roles, named systems, and a business-day-10 approval target.

## Why this shape

Workspace and period identity prevent one engagement's evidence, roles, and controls from leaking into another engagement.

## Shape

- Workspace ID `CRHS-042` and period `2026-07`.
- Senior Bookkeeper, Client Accounting Services Manager, and client Operations Manager roles.
- Client portal, controlled intake email, QuickBooks Online, payroll, and merchant surfaces.
- Named source index, exception register, review packet, and approval register.

## Connected to

- **owns:** engagement-specific evidence and operational records.
- **owned-by:** assigned bookkeeping roles.
- **joins:** `Source Document`, `Exception`, `Review Packet`.
- **looks-like-but-is-not:** a contact person or legal-entity master record.

## If you change this

- **Hits:** client-specific intake rules; assigned roles; period and packet ownership; access boundaries.
- **Does not hit:** another client's records; firm-wide approval policy; global document taxonomy.

## Surfaces

| Surface | Role |
|---|---|
| Intake | writes within boundary |
| Senior Bookkeeper | reads and writes |
| CAS Manager | reads assigned packet and approves |

## See

- Source: `../../../demo-territory/client-workspace/workspace-manifest.md`

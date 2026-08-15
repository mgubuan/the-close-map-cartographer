---
type: object
cluster: bookkeeping
universe: live
status: verified
verified_on: 2026-08-15
revision: demo-v1
entity: demo-territory/client-workspace/workspace-manifest.md
---

# Client Workspace

The access and record boundary for one sanitized bookkeeping engagement, named `DEMO-001` in the demonstration source.

## Why this shape

Workspace and period identity prevent one engagement's evidence, roles, and controls from leaking into another engagement.

## Shape

- Workspace ID and period convention.
- Assigned preparer and reviewer roles.
- Named live intake, exception, and approval systems.

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
| Bookkeeper | reads and writes |
| Reviewer | reads assigned packet |

## See

- Source: `../../../demo-territory/client-workspace/workspace-manifest.md`


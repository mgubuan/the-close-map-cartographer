# Workflow Integrity Checks

These checks keep the example useful when a bookkeeping firm adapts it.

| What must remain true | How this repository checks it |
|---|---|
| Every close step has an authoritative record | Each workflow page links to an existing file in `demo-territory/client-workspace/`. |
| A summary cannot silently replace the operating record | Source files remain authoritative when a workflow page disagrees. |
| A change does not reopen the entire close | Every page states what the change affects and what can remain unchanged. |
| Old spreadsheets cannot impersonate current status | The retired checklist is clearly marked and has no current owner, reader, or decision. |
| New team members have one starting point | `sample-map/CLAUDE.md`, `AGENTS.md`, and `routing.md` contain identical navigation. |
| The workflow does not guess beyond bookkeeping scope | Unknown or policy-dependent questions stop and route to an authorized reviewer. |
| Client information stays out of the example | The territory is a sanitized composite with synthetic identifiers and no balances or credentials. |
| The downloadable example does not drift | `validate_close_map.py` checks the folder structure, links, statuses, and required content. |

## What automation proves

Running `python validate_close_map.py` verifies that:

- all eight workflow pages use the expected structure;
- all source links resolve;
- the seven active close controls and retired checklist appear in the index;
- the complete records-to-delivery path exists;
- workflow-navigation files agree;
- the privacy and public-language checks pass.

Automation cannot decide whether a firm’s accounting policy is correct or whether an individual close is materially accurate. Those decisions remain with the firm’s authorized reviewer.

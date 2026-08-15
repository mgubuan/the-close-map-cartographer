# Cold Reader Test Protocol

Run every test in a new session with no project memory.

## Inputs

- The cartographer folder.
- Read-only access to the sanitized territory.
- One question at a time.

## Required tests

1. **Front door:** find the correct card from the catalog in one hop.
2. **Change radius:** name at least one correct `Hit` and `Does not hit`.
3. **Ghost trap:** reject a plausibly named but unwired tracker.
4. **Authority:** identify which live source wins when names disagree.
5. **Restraint:** stop without opening unrelated cards or copying client values.
6. **Dual reader:** a human and a cold model can use the same catalog.

## Record

- Files inspected.
- Cards opened.
- Sources cited.
- Ghosts mistaken as live.
- Sensitive values copied.
- Whether the reader stopped at the declared boundary.

Never publish invented benchmark results. Preserve the raw transcript or mark the test `NOT RUN`.


# Test Results

- `python validate_close_map.py` passes the published architecture contract.
- Entry twins are byte-identical and shorter than 60 lines.
- Entry twins and the noun index rebuild deterministically with `python generate_close_map.py`.
- Eight object cards validate against the closed schema, `monthly-close-v2`, and source snapshot `fd52389ac7ddf95244ad93f039573b402e900e56`.
- Every verified card cites an existing source and states `Hits` and `Does not hit`.
- The effects catalog routes every card and includes a safe unknown path.
- The records-to-delivery process cites all seven live source controls.
- The retired checklist is marked as a ghost with no current writer, reader, or decision.
- Public-language and privacy-boundary checks pass.
- The complete 16-file territory inventory distinguishes seven live close sources, eight retained prior-state files, and one ghost.
- Subject entry + map entry + one card estimates 2,005–2,081 tokens.
- Seven architecture walk questions pass; see `audit/03-architecture-walk-tests.md`.

A documented fresh-session walk is recorded in `audit/01-cold-reader-walkthrough.md`. The first run exposed an over-reading failure; after explicit next-card gates and stop conditions were added, the second isolated reader opened one object card, one cited source, answered correctly, reported unknown firm policy, and stopped at first-order impact.

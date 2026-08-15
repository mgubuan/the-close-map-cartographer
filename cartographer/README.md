# The Close Map Cartographer

The Close Map turns a live bookkeeping operations folder into a small, source-cited system map. Its reader may be a new bookkeeper or a cold AI model. Both follow the same rule:

> Load the catalog, open one card, follow its citations, and stop.

## What to provide

- One sanitized bookkeeping operations folder someone will actually change.
- The current SOPs, trackers, folder conventions, and system exports that govern it.
- No credentials, tax IDs, account numbers, balances, or client document contents.

## Walk order

1. Read `identity.md` and `rules.md`.
2. Inventory the territory before writing any cards.
3. Follow the gated slices in `reference/walk-order.md`.
4. Resolve naming collisions using `reference/naming-collisions.md`.
5. Classify every candidate object as `live`, `leftover`, or `ghost` from evidence; use `status: stub` when verification is incomplete.
6. Use only the closed types in `reference/card-types.md`.
7. Write the small entry catalog and stub index before card bodies.
8. Write only verified nouns and real movements needed to answer change questions.
9. Build the change-impact doors after the cards, never before them.
10. Run the tests in `reference/test-protocol.md`.

## Output contract

The completed map contains the smallest applicable subset of:

```text
map/
├── CLAUDE.md
├── AGENTS.md
├── routing.md
├── CONTEXT.md
├── _meta/schema.md
├── _templates/
├── objects/{CONTEXT.md,_index.md,<cluster>/}
├── processes/       only when a real movement is proven
└── effects/CONTEXT.md
```

`CLAUDE.md`, `AGENTS.md`, and `routing.md` are generated as byte-identical routing twins. Every verified card records a verification date, revision, authoritative citations, `Hits`, and `Does not hit`. A card points to source; it never replaces source.

## One rule

Never load the entire source folder or the entire `objects/` folder into context. If a question cannot be routed from the effects catalog, stop and report the missing door.

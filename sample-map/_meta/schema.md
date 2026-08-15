# Closed Map Schema

## Naming

Machine-facing files use kebab-case. Object cards live under `objects/bookkeeping/`. Entry twins are generated from `CLAUDE.md` and must remain byte-identical.

## Universes

`live | leftover | ghost`

## Verification status

`stub | verified | stale`

`verified` requires `verified_on`, `revision`, and at least one subject-source citation. `stale` means the card once had evidence but the named revision is no longer current.

## Closed node types

### object

Required frontmatter: `type`, `cluster`, `universe`, `status`, `verified_on`, `revision`, `entity`.

Required sections: Why this shape, Shape, Connected to, If you change this, Surfaces, See.

### process

Required frontmatter: `type`, `universe`, `status`, `verified_on`, `revision`, `consumes`, `produces`.

Required sections: Input, Movement, Output, If you change this, Surfaces, See.

No additional type is valid until this schema changes.


# Closed Card Types

The Close Map emits exactly two card types.

## Object

A durable noun someone can identify, cite, and change: `client-workspace`, `source-document`, `exception`, `review-packet`, `approval`, or a ghost/leftover object that might be mistaken for one of those.

Required fields:

- `type: object`
- `cluster`
- `universe: live | leftover | ghost`
- `status: stub | verified | stale`
- `verified_on`
- `revision`
- `entity`

Required sections: one-sentence identity, Why this shape, Shape, Connected to, If you change this, Surfaces, and See.

## Process

A real, repeated movement connecting objects. Do not create a process card for aspiration, policy alone, or a story about the month.

Required fields:

- `type: process`
- `universe: live | leftover | ghost`
- `status: stub | verified | stale`
- `verified_on`
- `revision`
- `consumes`
- `produces`

Required sections: Input, Movement, Output, If you change this, Surfaces, and See.

No third card type may be introduced without first changing the schema and the catalog.


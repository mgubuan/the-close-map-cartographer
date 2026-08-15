# Mapping Rules

## 1. Inventory before cards

List folders, records, trackers, SOPs, queues, and integrations before naming map objects. Record observed writers, readers, owners, and decisions.

## 2. Map nouns, not the weekly story

Good nouns include `Source Document`, `Exception`, `Review Packet`, and `Approval`. Do not write a top-to-bottom month-end tour.

## 3. Prove liveness

- `live`: currently written, read, or used to make an operational decision.
- `leftover`: retained intentionally but no longer participates in the live system.
- `ghost`: looks authoritative but has a name and no live wiring.

When evidence is insufficient, keep the candidate `status: stub`. `UNKNOWN / Catalog Gap` is a safe query result, not a fourth universe.

Existence is not liveness. Movement is liveness.

## 4. Cite; do not copy

Cite paths, headings, schemas, and control locations. Never copy credentials, tax IDs, account numbers, balances, transaction contents, or client-identifying values into a card.

## 5. Bound every change

Every noun card must contain:

- `Hits`: objects or controls that normally move with this noun.
- `Does not hit`: the plausible neighbor a cold reader might change incorrectly.
- `Open next only if`: an explicit gate for loading another card.
- `Stop`: the condition under which the reader has enough context.

## 6. Separate operational states

Never collapse `received`, `processed`, `review-ready`, `approved`, and `delivered`. A filename or folder location is not proof of approval.

## 7. Map; do not diagnose

Do not explain why a failure happened, prescribe a fix, audit quality, or generate accounting advice. Describe the current object, its movement, its authority, and its change radius.

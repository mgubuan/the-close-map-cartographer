# Cold-Reader Walkthrough

Tested: 2026-08-16

## Purpose

Test whether a fresh AI reader with no prior repository context can answer one bookkeeping workflow-change question by starting at the repository entry, opening the minimum source-backed path, and stopping without scanning the full map.

## Reader isolation

- New ephemeral Codex CLI session.
- Read-only filesystem access.
- User configuration and local execution rules ignored.
- Internet use and git-history inspection prohibited by the prompt.
- No files from this repository were supplied in the prompt.
- The model received only the repository working directory, reader role, change question, and output requirements.

## Test question

> Our firm wants to change low-risk balance-sheet accounts from monthly reconciliation to quarterly reconciliation. What parts of the monthly-close workflow must change, what can remain unchanged, and what must be defined before this change is safe to adopt?

The reader was instructed to list every file opened, explain why it was necessary, state where it stopped, and identify anything it could not verify.

## Run 1 — failed bounded-walk test

The first reader produced a materially correct operational answer but opened 13 files. It began in the owner-facing root README, jumped directly to the Account Reconciliation card, and then treated every relationship on that card as permission to continue through transaction completion, balance verification, entries, review, and delivery.

### Result

- Correct primary control: yes.
- Correct operational answer: yes.
- Used cited source: yes.
- Followed catalog-first entry: no.
- Opened one primary card: no.
- Stopped at first-order impact: no.
- Verdict: **FAIL**.

### Correction prompted by the failure

1. The root README now tells AI readers to begin at `sample-map/CLAUDE.md` for workflow-change questions.
2. Every object card now has an explicit `Open next only if` gate.
3. Every object card now has an explicit `Stop` condition.
4. The validator now fails if either field is missing.

## Run 2 — passed bounded-walk test

The same question and isolation rules were given to a second ephemeral session after the navigation correction.

### Files opened, in order

1. `README.md` — repository entry and AI starting instruction.
2. `sample-map/CLAUDE.md` — map entry and catalog-first reading contract.
3. `sample-map/effects/CONTEXT.md` — routed reconciliation-frequency changes to one primary card.
4. `sample-map/objects/bookkeeping/account-reconciliation.md` — established affected work, unaffected work, next-card gate, and stop condition.
5. `demo-territory/client-workspace/reconciliation-register-2026-07.csv` — verified the card against current source.

No other object card was opened.

### Reader answer

The reader correctly concluded that the workflow must update:

- reconciliation frequency for eligible accounts;
- off-month evidence requirements;
- low-risk classification criteria;
- reviewer workload and approval;
- downstream review status so `not due` is not mistaken for `missing`.

It correctly left transaction-category policy, client request deadlines, delivery contacts, transaction completion, and key balance verification unchanged unless the new policy changes a posted balance or supported tie-out.

It required the firm to define eligible accounts, risk criteria, approver, quarterly due dates, off-month evidence, and the trigger that returns an account to monthly reconciliation.

### Stop decision

The reader stopped at the reconciliation register because the primary card permits `key-balance-verification.md` only when a supported AR, AP, payroll, tax, loan, or clearing balance changes. The proposed change concerned frequency, risk, evidence, and review cadence; the source showed no specific supported balance change.

### Honest unknowns

The reader did not invent the firm’s eligible-account list, risk criteria, quarterly calendar, off-cycle triggers, or approver authority. It reported that those decisions were not present in the cited source.

### Result

- Correct primary control: yes.
- Correct operational answer: yes.
- Catalog-first routing: yes.
- Exactly one object card opened: yes.
- One authoritative source opened: yes.
- Unrelated object shelf avoided: yes.
- Stopped at first-order impact: yes.
- Unknown firm policy reported without guessing: yes.
- Verdict: **PASS**.

## Reproduction command

The test used a fresh ephemeral, read-only `codex exec` session from the repository root. The prompt above can be reused with another fresh model or a human new hire. A CLI model-cache warning appeared after the completed answers because the installed client did not recognize one remote model metadata value; both test commands exited successfully and the warning did not alter repository access or the final responses.

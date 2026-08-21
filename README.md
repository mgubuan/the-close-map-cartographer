# The Close Map for Bookkeeping Firms

**A source-linked guide to what must change—and what can stay put—when a bookkeeping firm adapts a client's monthly close.**

Most close checklists tell someone what to mark complete. They do not explain what “done” means, what proof belongs with the task, or which later work must be repeated when something changes.

The Close Map fixes that. Start with one practical change, open one relevant control, verify it against source, and stop after the affected work is clear.

## Start with a change, not a folder tour

| If you are asking… | Open first |
|---|---|
| What changes if this client needs statements by business day three? | [Client Records Ready](sample-map/objects/bookkeeping/client-records-ready.md) |
| Can low-risk accounts be reconciled quarterly instead of monthly? | [Account Reconciliation](sample-map/objects/bookkeeping/account-reconciliation.md) |
| What changes if this client needs a payroll-liability tie-out? | [Key Balance Verification](sample-map/objects/bookkeeping/key-balance-verification.md) |
| What changes if a smaller client uses a lower variance threshold? | [Bookkeeping Review](sample-map/objects/bookkeeping/bookkeeping-review.md) |
| What must happen before a delivered month can be reopened? | [Report Delivery](sample-map/objects/bookkeeping/report-delivery.md) |
| Is `Old Close Checklist.xlsx` still controlling the close? | [Old Close Checklist](sample-map/objects/bookkeeping/old-close-checklist.md) |

Each page tells the reader what the control owns, which source proves it, what else the proposed change touches, which nearby work it does **not** touch, and when to stop. For any other change, use the [change-impact catalog](sample-map/effects/CONTEXT.md).

## See it before you use it

[Try the interactive bookkeeping workflow →](https://intelligencesolved.com/close-map)

Choose a change such as:

- Require statements by business day three.
- Add a payroll-liability tie-out.
- Move low-risk accounts to quarterly reconciliation.
- Set different variance thresholds for different clients.
- Require approval before reopening a delivered month.

The demo shows which close step to update first, what else must change, what can remain unchanged, and which decisions belong with the client’s CPA or another authorized reviewer.

## The territory being mapped

| Step | The bookkeeper can call it complete when… |
|---|---|
| 1. Client Records Ready | Every required statement, report, receipt set, and answer has arrived—or has an owner, due date, and documented effect on the close. |
| 2. Transactions Complete | Activity is posted, matched, supported, categorized, and checked for duplicates and wrong-period entries. |
| 3. Accounts Reconciled | Bank, credit-card, loan, and other selected accounts agree with independent support. |
| 4. Key Balances Verified | AR, AP, payroll, sales tax, loans, clearing accounts, and other scoped balances agree with their supporting reports. |
| 5. Month-end Entries Posted | Recurring, correcting, and externally approved entries are supported, authorized, and reflected in affected checks. |
| 6. Books Reviewed | The balance sheet and P&L pass the firm’s review rules, unusual activity is explained, and open questions are visible. |
| 7. Reports Delivered | The approved report version is sent to the right contact and any later reopening creates a documented replacement. |

The repository also identifies `Old Close Checklist.xlsx` as retired. Its name looks official, but updating it does not update the current close.

## Find a control by name

| If your firm wants to change… | Start here |
|---|---|
| Client requirements, deadlines, or reminder ownership | [Client Records Ready](sample-map/objects/bookkeeping/client-records-ready.md) |
| Posting, matching, categorization, or transaction review | [Transaction Completion](sample-map/objects/bookkeeping/transaction-completion.md) |
| Reconciliation frequency, support, or approval | [Account Reconciliation](sample-map/objects/bookkeeping/account-reconciliation.md) |
| AR, AP, payroll, sales-tax, loan, or clearing checks | [Key Balance Verification](sample-map/objects/bookkeeping/key-balance-verification.md) |
| Recurring or manual month-end entries | [Month-end Entry](sample-map/objects/bookkeeping/month-end-entry.md) |
| Review thresholds, explanations, or reviewer responsibility | [Bookkeeping Review](sample-map/objects/bookkeeping/bookkeeping-review.md) |
| Report recipients, versions, delivery, or reopening | [Report Delivery](sample-map/objects/bookkeeping/report-delivery.md) |

Each page answers four practical questions:

1. What is this close control responsible for?
2. What evidence proves it is complete?
3. What else must change when the control changes?
4. What nearby work can stay as it is?

## Use it with your firm

There are two ways to use this repository:

### Adapt the example

Start in [`demo-territory/client-workspace/`](demo-territory/client-workspace/). It is a privacy-safe reconstruction of recurring monthly-close work directly operated and supervised during more than twenty years of controllership. The example client, identifiers, dates, and record contents are synthetic; the operating boundaries, handoffs, controls, and naming collisions reflect real close work. Replace them with sanitized versions of your own, then update only the corresponding pages in [`sample-map/objects/bookkeeping/`](sample-map/objects/bookkeeping/).

### Map an existing close folder

Copy [`cartographer/`](cartographer/) into a private working project alongside a sanitized close folder. Give the folder to your AI assistant and ask it to follow `cartographer/README.md`. It will inventory the current files before describing the workflow, distinguish current records from old ones, and create a small source-linked guide.

Do not upload client names, account numbers, credentials, payroll details, tax identifiers, transaction values, or unsanitized financial records.

## What the folders contain

```text
cartographer/       Reusable instructions for mapping another close folder
demo-territory/     Privacy-safe reconstruction of recurring close work
sample-map/         The finished guide to that example close
audit/              The initial file inventory
validate_close_map.py
test-results.md
```

## Verify the package

```bash
python generate_close_map.py
python validate_close_map.py
```

The generator rebuilds the noun index and navigation twins from their canonical sources. The validator checks that every workflow page points to a real source snapshot, the current, retained, and retired records are clearly distinguished, generated files have not drifted, and the package contains no prohibited public references.

The documented [cold-reader walkthrough](audit/01-cold-reader-walkthrough.md) records both an initial over-reading failure and the successful retest after explicit next-card gates and stopping rules were added.

The broader [architecture walk tests](audit/03-architecture-walk-tests.md) exercise seven common lookup and change questions and record the bounded reading path for each.

The example is educational workflow infrastructure, not accounting, tax, payroll, or legal advice. Decisions outside the bookkeeping engagement should go to the designated CPA, controller, payroll specialist, or client approver.

Built by [Intelligence Solved](https://intelligencesolved.com/) for bookkeeping firms that want a close their team can run without relying on tribal knowledge.

## AI starting point

When an AI assistant is answering a workflow-change question, begin at [`sample-map/CLAUDE.md`](sample-map/CLAUDE.md). Follow its catalog-first rule instead of browsing the folder tree or following every relationship named on a card.

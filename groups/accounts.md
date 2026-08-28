---
name: accounts
title: One customer
bots: [desk, health, notes, tickets, replies, claims]
---

# accounts

Account lane. Sits on one customer, not the whole book. @health ranks churn and expansion evidence. @notes capture the last promise. @tickets draft the bug they hit. @replies draft the next message. @claims check every claim in that draft. @desk names who owns the leftover. Never contact the customer and never change the account.

## Roster

| Bot | Job in this group |
| --- | --- |
| desk | Front door. Rank leftovers after the pack runs. |
| health | Watch list row for this account, with links. |
| notes | Last call. Decisions, owners, the promise. |
| tickets | Internal issue draft from their report. |
| replies | Customer-facing draft. Next action plus sources. |
| claims | Audit the draft. Blockers only. |

## Handoff

1. You name the account and drop the thread, ticket, or notes.
2. @health returns evidence of risk or expansion.
3. @notes extract the last promise. Missing owner stays missing.
4. @tickets draft an internal issue if there is a defect.
5. @replies draft what you might send.
6. @claims list unsourced claims in that draft.
7. @desk rank what is still open.

## Kickoff

```text
Account: <name>
Sources: <thread, ticket, call notes>

@health rank churn or expansion evidence with links. Do not contact them.
@notes return the last promise, owners, and due dates. Do not invent an owner.
@tickets if there is a defect, draft the issue. Do not create it.
@replies draft the next customer message with a source for each claim. Do not send.
@claims list every claim in that draft that lacks a source. Do not rewrite for style.
@desk rank what is still open and name the owner. Do not send anything.
```

## Hard stop

Never email, call, or Slack the customer. Never refund, never change the account, never open the GitHub issue unless you send it.

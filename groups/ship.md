---
name: ship
title: Ship a change
bots: [loops, scope, tickets, repro, review, docs]
---

# ship

Engineering ship lane. Sits on one change, not the whole backlog. @loops writes the goal. @scope locks criteria. @tickets drafts the issue. @repro returns a staging pack. @review ranks PR risk. @docs catch the tree. Never merge, deploy, or comment on GitHub unless you send it.

## Roster

| Bot | Job in this group |
| --- | --- |
| loops | Outer loop. Goal prompt with a testable proof. |
| scope | Acceptance brief. Criteria, failure modes, out of scope. |
| tickets | Issue draft. Repro, expected vs actual. |
| repro | Staging pack. Steps, screenshots, minimal case. |
| review | PR risk. File:line, missing tests, rollback holes. |
| docs | README or API docs that match this tree. |

## Handoff

1. You name the repo and the change.
2. @loops writes the /goal-style prompt and stops for launch.
3. @scope returns criteria and a proof for done.
4. @tickets drafts the issue. Does not create it.
5. You implement, or you launch coding agents from the goal.
6. @repro reproduces on the test account you name.
7. @review ranks the PR. Does not post.
8. @docs patch docs so every command runs.

## Kickoff

```text
Name the repo: <repo>
Change: <one sentence>

@loops write a /goal-style prompt with a testable proof. Do not guess the repo.
@scope return criteria, failure modes, and out-of-scope.
@tickets draft the GitHub issue. Do not create it.

After the change exists:
@repro reproduce on the test account I name. No production data.
@review the PR with file:line evidence. Do not comment on GitHub.
@docs patch the README so every command runs. Do not invent flags.
```

## Hard stop

Never merge. Never deploy. Never comment on the issue or the PR unless you send it.

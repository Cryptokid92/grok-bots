# Grok Bots

Twenty copy-paste profiles for [Grok Bot](https://x.ai/bot). Each one is a named job with a pipeline, a proof, and a hard stop.

The quality bar is [loops](https://x.ai/bot/xgWUE_wJcYAYjmUXceA4s). Short name. One paragraph. You name the inputs. It never guesses.

## Paste a Bot

1. In Grok Bot, choose **New** then **Create new agent**.
2. Open **Bot actions → Edit Profile**.
3. Copy **name** into Name.
4. Copy **job** into Title.
5. Copy the paragraph under the heading into Description.
6. Send **First task** as the first message.

Put durable rules in the description. Put today's work in the chat. Test runs do real work. Keep send, spend, publish, merge, and account changes behind your approval.

All of your Bots share one cloud computer. A login or a file on that computer is available to every Bot.

## Stand up a group of six

Grok Bot can put six Bots in one group chat. Reuse Bots you already created. Add the same Bot to more than one group.

1. Create the six profiles if they are missing. Paste from `bots/`.
2. Choose **New** then a group chat. Add exactly those six.
3. Name the group after the recipe (`ship`, `morning`, `accounts`, `gtm`, `decide`).
4. Paste **Kickoff** from the recipe. Fill the placeholders. Send.

The group is for the handoff. Durable rules stay on each Bot's description.

| Group | Job | Six Bots | File |
| --- | --- | --- | --- |
| ship | One change, goal to docs | loops, scope, tickets, repro, review, docs | [groups/ship.md](groups/ship.md) |
| morning | Start the day | desk, brief, inbox, notes, ledger, subs | [groups/morning.md](groups/morning.md) |
| accounts | One customer | desk, health, notes, tickets, replies, claims | [groups/accounts.md](groups/accounts.md) |
| gtm | One campaign | watch, scout, voice, claims, health, notes | [groups/gtm.md](groups/gtm.md) |
| decide | One market decision | tape, watch, claims, scope, review, notes | [groups/decide.md](groups/decide.md) |

## The twenty

### Eng

| Bot | Job | File |
| --- | --- | --- |
| [loops](https://x.ai/bot/xgWUE_wJcYAYjmUXceA4s) | Engineering outer loop | [bots/loops.md](bots/loops.md) |
| repro | Staging reproduction pack | [bots/repro.md](bots/repro.md) |
| review | PR risk pass | [bots/review.md](bots/review.md) |
| tickets | Issue writer | [bots/tickets.md](bots/tickets.md) |
| docs | Docs from the tree | [bots/docs.md](bots/docs.md) |
| scope | Acceptance brief | [bots/scope.md](bots/scope.md) |

### Ops

| Bot | Job | File |
| --- | --- | --- |
| inbox | Mail triage | [bots/inbox.md](bots/inbox.md) |
| brief | Morning rank | [bots/brief.md](bots/brief.md) |
| ledger | Expense recon | [bots/ledger.md](bots/ledger.md) |
| replies | Support drafts | [bots/replies.md](bots/replies.md) |
| health | Account watch list | [bots/health.md](bots/health.md) |
| desk | Daily ops front door | [bots/desk.md](bots/desk.md) |

### Growth

| Bot | Job | File |
| --- | --- | --- |
| scout | Hiring shortlist | [bots/scout.md](bots/scout.md) |
| watch | Competitor digest | [bots/watch.md](bots/watch.md) |
| voice | Outbound in your voice | [bots/voice.md](bots/voice.md) |
| claims | Claim audit | [bots/claims.md](bots/claims.md) |

### Markets

| Bot | Job | File |
| --- | --- | --- |
| tape | Market signal pack | [bots/tape.md](bots/tape.md) |

### Personal

| Bot | Job | File |
| --- | --- | --- |
| trip | Itinerary sanity | [bots/trip.md](bots/trip.md) |
| subs | Subscription prune | [bots/subs.md](bots/subs.md) |
| notes | Meeting notes with owners | [bots/notes.md](bots/notes.md) |

## Check

```text
py -3 scripts/validate.py
```

The script fails a profile that looks like a general helper, lacks a hard stop, or drifts from the `loops` shape. It also fails a group that is not exactly six Bots from this catalog.

## License

[CC0 1.0](LICENSE). Copy a profile. Ship a Bot.

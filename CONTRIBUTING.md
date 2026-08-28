# Add a Bot

Match [bots/loops.md](bots/loops.md). That profile is the bar.

1. Add `bots/<name>.md` with `name`, `job`, `category`, `plugins`.
2. Use a short lowercase name.
3. Write one description paragraph: what it is, where it sits, what it returns, and a hard stop.
4. Add a First task the user can send as the first message.
5. Add a row to [README.md](README.md).
6. Run `py -3 scripts/validate.py`.

Do not add a general helper. Do not put secrets in a profile. Share links are public.

## Add a group

1. Add `groups/<name>.md` with `name`, `title`, and exactly six `bots` slugs from `bots/`.
2. Reuse existing Bots. Do not invent a seventh specialist for a pack.
3. Include Roster, Handoff, Kickoff, and Hard stop.
4. @-mention every Bot on the roster in the file.
5. Run `py -3 scripts/validate.py`.
6. Add a row to the group table in [README.md](README.md).

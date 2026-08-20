# FlexPay AU Second Brain (local-only)

A living Markdown wiki for the synthetic FlexPay AU programme, built per
[a second-brain blueprint](../ai-second-brain-blueprint.md) — local-only,
Version 0/1 (manual local wiki + generated state + read-only chat connection). See
[synthetic-dataset-reading-guide.md](synthetic-dataset-reading-guide.md) for the
dataset-specific quirks this build corrects for, and [CLAUDE.md](CLAUDE.md) for the
full operating contract.

## Layout

```
CLAUDE.md              operating contract (Claude Code loads this automatically)
index.md               catalog of durable pages
log.md                 append-only refresh/ingest history + as-of cursor
current-state.md/.json generated snapshot — do not hand-edit
entity-index.json      generated name/alias → page-path map — do not hand-edit
projects/ people/ decisions/    durable, agent-maintained pages
sources/{slack,notion,gdrive}/  immutable per-refresh capture files
bin/                    regenerate-state, retrieve, lint-wiki
tests/                  acceptance-checklist.md
```

## Commands

All scripts are stdlib-only Python 3, run from the repo root.

```bash
python3 bin/regenerate-state     # rebuild current-state.md/.json + entity-index.json
python3 bin/lint-wiki            # structural checks: links, orphans, frontmatter, staleness
python3 bin/retrieve "query"     # local text search over pages + entity aliases
```

## Running a refresh

Refresh has no CLI — it's a chat request to Claude Code, because capture needs live
Slack/Notion/Drive tool access that a plain script doesn't have. In a Claude Code
session opened in this directory:

```
refresh through 2026-08-14
```

or just `refresh` to let it pick the next natural cutoff. Rules (full detail in
`CLAUDE.md`):

- The as-of date can only move forward. Asking for a date earlier than the cursor
  already in `log.md` is refused, not silently reinterpreted.
- Slack threads are cut at the individual message's embedded timestamp, not the
  thread boundary.
- Re-running the same as-of date should be a no-op if nothing changed.

## Troubleshooting

- **`bin/lint-wiki` fails on a broken link / orphan page** — the refresh that
  introduced it didn't finish integration; check `log.md`'s latest entry for what was
  in flight.
- **`current-state.md` looks stale** — regenerate it: `python3 bin/regenerate-state`.
  If `log.md`'s cursor is newer than what's shown, that's the signal something didn't
  get regenerated after the last refresh.
- **A source lane looks empty in `log.md`** — check whether the entry says
  `unavailable` (access/auth problem) vs `no material activity` (queried fine, nothing
  new). They're recorded as different things on purpose.

## Recovery

Every refresh is a local git commit. To roll back a bad refresh:

```bash
git log --oneline          # find the commit before the bad refresh
git revert <bad-commit>    # or: git reset --hard <good-commit> if uncommitted elsewhere
python3 bin/regenerate-state
```

## What's deliberately out of scope

No GitHub, no branches/PRs, no unattended-automation tooling, no service identities, no scheduler,
no MCP read-only service, no privacy redaction pipeline (nothing here is real). No
Gmail/Calendar/Granola/Linear/Jira/Glean lanes — they don't exist in this exercise.
No ground-truth/answer-key file is ever read — see `CLAUDE.md`.

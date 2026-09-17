# FlexPay AU Second Brain (local-only)

A living Markdown wiki for the synthetic FlexPay AU programme, built per a
second-brain blueprint — local-only, Version 0/1, as a practical exercise in
applying AI tooling to programme-management work. See
[synthetic-dataset-reading-guide.md](synthetic-dataset-reading-guide.md) for the
dataset-specific quirks this build corrects for, and [CLAUDE.md](CLAUDE.md) for the
full operating contract.

By [Giles Davis](https://www.linkedin.com/in/gilesbdavis/)

## Context for reviewers

### The blueprint this method is based on

This wiki's method (schema, refresh workflow, contradiction-resolution rules) was
originally set out in a private "second-brain blueprint" document written by a
former colleague. That document isn't in this repo. It was written by someone
else, for a problem they needed to solve.

What I have done is

* Built from scratch a synthetic programme to have something real to run the
  method against (see [synthetic-dataset-reading-guide.md](synthetic-dataset-reading-guide.md))
* Setup required connectors to Slack, Notion, GDrive in order for Claude Code to
  access the synthetic programme artefacts
* Instructed Claude Code to use the blueprint to generate the wiki, and cater for
  ongoing refreshes of the wiki (as 'synthetic time' passes in the programme and
  activities progress, slack comments posted, decisions made and recorded in the
  RAID log, etc)
* Implemented 14 enhancements to the base Claude instructions, and created the
  associated addendums/build-history-addendums.md file, so that when I implement
  the blueprint against a real programme in future, those can be incorporated.
  These were also shared with my former colleague in case they wanted to fold
  any of them into their version
* Built the supporting tooling (`bin/lint-wiki`, `bin/regenerate-state`,
  `bin/retrieve`) that mechanically checks the wiki for broken links, orphan
  pages, missing frontmatter, and fabricated or misdated quotes, and
  deterministically rebuilds its generated state and search index — since the
  blueprint describes the method, not the code that enforces it

Where CLAUDE.md, the addendums, or synthetic-dataset-reading-guide.md reference
"the blueprint," that's what they mean: a source I built against, not something
reproduced here.

### Why there's no UI

There's deliberately no UI in this repo, and there isn't meant to be one. The
programme's "raw" data (a synthetic Slack workspace with posts from pretend
stakeholders, a Notion milestone board, a RAID log, meeting notes) lives in
those actual connected apps, not as files here.

When Claude Code actions a "refresh", it reads them live through each app's
own connector, the same way it would for a real programme.

What's committed to this repo is the output of that process: the generated
wiki, its generated state, and the instruction/tooling layer that produced it.

It's the generated wiki (plain text markdown files) that Claude Code uses as
context when I ask it specific questions, rather than needing to interrogate
the source data.

A real programme would generate more of these files, and larger ones.

The repo can be cloned to a local machine. Claude Code can then be asked key
questions (e.g. "what's the biggest current risk to the delivery deadline?",
"where do I need to focus my time today?") and it will respond.

A UI tool such as Obsidian can also be used to understand the relationships
between those markdown files / programme entities.

However you will not have access to the source programme collateral, since
the underlying Slack/Notion/Drive workspaces aren't public.

So to best appreciate the application of this LLM wiki concept, and how I see
it enabling a programme manager to be more effective, please reach out for a
walkthrough.

## Layout

`wiki/` holds only the knowledge system — nothing implementation- or test-related.
Everything else at the repo root is operating machinery or exercise documentation.
The split is tool-independent by design: `wiki/` uses plain CommonMark links and
plain YAML/JSON only, no vendor-specific syntax, so it can be opened as an Obsidian
vault, browsed as plain files, or read by any other Markdown-aware tool without
modification.

```
CLAUDE.md              operating contract (Claude Code loads this automatically)
README.md              this file
bin/                    regenerate-state, retrieve, lint-wiki
tests/                  acceptance-checklist.md
synthetic-dataset-reading-guide.md   dataset addendum (test-harness doc, not wiki content)

wiki/                                the knowledge system
  index.md               catalog of durable pages
  log.md                 append-only refresh/ingest history + as-of cursor
  current-state.md/.json generated snapshot — do not hand-edit
  entity-index.json      generated name/alias → page-path map — do not hand-edit
  projects/ people/ decisions/    durable, agent-maintained pages
  sources/{slack,notion,gdrive}/  immutable per-refresh capture files
```

Paths inside `wiki/` content (frontmatter citations, page-to-page links) are relative
to `wiki/` itself, so it stays portable regardless of where the repo lives on disk or
what tool opens it.

## Commands

All scripts are stdlib-only Python 3, run from the repo root.

```bash
python3 bin/regenerate-state     # rebuild wiki/current-state.md/.json + wiki/entity-index.json
python3 bin/lint-wiki            # structural checks: links, orphans, frontmatter, staleness
python3 bin/retrieve "query"     # local text search over wiki/ pages + entity aliases
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
  already in `wiki/log.md` is refused, not silently reinterpreted.
- Slack threads are cut at the individual message's embedded timestamp, not the
  thread boundary.
- Re-running the same as-of date should be a no-op if nothing changed.

## Troubleshooting

- **`bin/lint-wiki` fails on a broken link / orphan page** — the refresh that
  introduced it didn't finish integration; check `wiki/log.md`'s latest entry for what
  was in flight.
- **`wiki/current-state.md` looks out of sync** (not the same thing as a "stale" page —
  see below) — regenerate it: `python3 bin/regenerate-state`. If `wiki/log.md`'s cursor
  is newer than what's shown, that's the signal something didn't get regenerated after
  the last refresh.
- **`bin/lint-wiki` warns a page is "stale"** — a different meaning: a durable page's
  `updated:` frontmatter date hasn't moved in over 30 story-days relative to
  `wiki/log.md`'s as-of cursor (in-story time, not wall-clock time — see `CLAUDE.md`).
  It's a warning, not an error (`bin/lint-wiki` still exits 0), and it's printed to the
  terminal only — nothing writes it into `current-state.md` or `log.md`.
- **A source lane looks empty in `wiki/log.md`** — check whether the entry says
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

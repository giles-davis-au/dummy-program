# Log — append-only

Each entry is one refresh (or build event). Never edit a past entry. The most recent
`## Refresh — as-of` heading is the wiki's current as-of cursor — refreshes may only
move it forward.

## Refresh — as-of 2026-10-01

**First build (Version 0).** No prior cursor existed, so this refresh captured the
programme's full history from kickoff (2026-07-08) through the requested cutoff of
2026-10-01, across all three lanes.

**Coverage:**
- **Slack** — complete. Full history pulled from all 8 in-scope channels
  (`slack_get_channel_history` returned `has_more: false` for every channel; no
  threads present). 34 substantive messages captured, filtered to embedded in-story
  timestamps ≤ 2026-10-01. See [sources/slack/2026-10-01.md](sources/slack/2026-10-01.md).
- **Notion** — complete. Live-enumerated the "To Do List" parent page; found the
  FlexPay Program Tracker database (10 milestone rows, direct data-source query) and
  the FlexPay AU — Programme Overview page. See
  [sources/notion/2026-10-01.md](sources/notion/2026-10-01.md).
- **Google Drive** — complete. Live search on the target folder found the Weekly
  Programme Meeting Notes doc (5 meeting entries, 2026-07-10 through 2026-09-08) and
  the RAID Log sheet (4 risks, 2 assumptions, 0 issues, 5 decisions). See
  [sources/gdrive/2026-10-01.md](sources/gdrive/2026-10-01.md).

**Pages created:** 1 project ([projects/flexpay-au.md](projects/flexpay-au.md)),
5 decisions (D1–D5), 8 people. 14 durable pages total.

**Contradictions resolved:**
1. **Programme RAG status** (Notion "🟢 Green," last-updated 2026-07-28) vs. Giles
   Davis's 2026-08-15 Slack post moving it to Amber. Resolution: **new wins** — the
   Notion page predates the change and simply hasn't been re-edited; not a genuine
   conflict. Amber is recorded as current status.
2. **D4's decided date** — meeting notes doc groups it under the 2026-08-14 sync;
   RAID log's Decisions table and two independent same-day Slack posts (Giles,
   Grace) place the actual confirmation on 2026-08-18. Resolution: **new wins** —
   used 2026-08-18 (RAID log + 2x Slack corroboration outweighs the doc's grouping),
   with the discrepancy noted on [decisions/d4-gtm-spend-gate.md](decisions/d4-gtm-spend-gate.md).
3. **Milestone statuses M06, M07, M09** — Notion showed "Not started" for all three,
   but dated Slack evidence showed active work underway in each case (support
   playbook drafting, PDS review/sign-off, GTM asset production). Resolution: **new
   wins** — corroborated statuses recorded on [projects/flexpay-au.md](projects/flexpay-au.md)
   instead of Notion's raw value, per CLAUDE.md's Notion status caveat (never trust
   Notion status alone).

**Single-source claims flagged:** D5 (QR checkout wallet scope) appears only in the
RAID log, with no corroborating Slack or meeting-note mention found anywhere in the
full capture window. Flagged on [decisions/d5-qr-wallet-launch-scope.md](decisions/d5-qr-wallet-launch-scope.md).

**Informal signal, not promoted:** Dan Foster's 2026-08-19 remark in #flexpay-eng
about load-test results (response-time degradation above ~200 concurrent requests)
is real but has not been escalated into a RAID entry or meeting-note mention. Per
CLAUDE.md's informal-signal rule, it is not recorded as a tracked risk or decision —
noted as additional context on risk R1 (which already existed in the RAID log,
raised 2026-08-01) on [dan-foster.md](people/dan-foster.md) and
[projects/flexpay-au.md](projects/flexpay-au.md), framed as informal,
single-source, and unescalated.

**Judgment items for the owner:** none blocking — all contradictions above were
resolvable without a genuine conflict. Worth a heads-up: M07's confirmed PDS
sign-off date (4 October) falls 2 days after the tracker's M07 due date (2 October);
not treated as a formal risk since it's a minor, already-flagged slip and not
independently corroborated as a "risk" by any RAID entry, but flagged here for
visibility.

**Checks:** `bin/lint-wiki` — 0 errors, 0 warnings (14 pages checked). `wiki/index.md`
lists all 14 durable pages, no orphans. `current-state.md` / `.json` /
`entity-index.json` regenerated via `bin/regenerate-state`.

## Post-build corrections — 2026-10-01 (not a new refresh, as-of cursor unchanged)

`bin/lint-wiki` gained two new content checks after this refresh (verbatim-quote
verification; relative-date-language flagging on cited Slack messages — see
`addendums/giles-blueprint-addendums.md` §9/§11 for why — renumbered from §8/§9
in a later addendum restructuring pass). Running them surfaced
several accuracy defects that predated the checks. Per the owner's explicit
direction — this dummy-program is an active exercise for evaluating the wiki
pattern itself, not a live production audit trail, so the priority here is the
durable pages reading as if these checks had existed from the start, not
preserving a warts-and-all history of when each bug was caught — all are
corrected in place, including one inside a `sources/**` file, which is otherwise
never edited after creation. That exception is scoped to this build phase and
logged here explicitly rather than done silently:

- **`decisions/d4-gtm-spend-gate.md`** and **`sources/gdrive/2026-10-01.md`**
  (its "Discrepancy note") both quoted Grace Lindqvist's 2026-08-18 Slack message
  as containing the word "today" in quote marks — it doesn't. The date itself
  (2026-08-18) was and remains correct, established independently by the
  message's own embedded timestamp; only the fabricated quote fragment is
  removed. The `sources/**` edit is the one exception noted above.
- **`projects/flexpay-au.md`** (Milestones table) and **`people/maya-chen.md`**
  both claimed "beta build started 2026-08-11" — Maya's message, posted Tuesday
  2026-08-11, says the build "starts Monday" (2026-08-17, six days later); the
  post date and the announced start date had been conflated. Both reworded to
  state only what's evidenced.
- **`people/maya-chen.md`** similarly softened "started Console wireframes"
  (tied to 2026-08-05) to reflect that the source says "starting... this week,"
  not that it started that specific day.
- **`people/ben-okafor.md`** and **`people/grace-lindqvist.md`** each claimed
  "Notion shows M06/M09 as 'Not started'" without citing the Notion source for
  that claim on that specific page (the project page had it; these didn't).
  Added `sources/notion/2026-10-01.md#notion-m06` and `#notion-m09` to their
  frontmatter respectively.

**Checks after correction:** `bin/lint-wiki` — 0 errors, 11 warnings. All 11
reviewed individually and confirmed as expected false positives from the two new
heuristic checks (either quoting CLAUDE.md's own defined vocabulary rather than a
source, or citing a message with incidental relative-date language that isn't
actually load-bearing for any nearby claim) — not further action items.

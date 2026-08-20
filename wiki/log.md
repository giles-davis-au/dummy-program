# Log — append-only

Each entry is one refresh (or build event). Never edit a past entry. The most recent
`## Refresh — as-of` heading is the wiki's current as-of cursor — refreshes may only
move it forward.

---

## Build — 2026-08-20 (real-world date; not an as-of cursor)

Initial scaffold created per the local-only Version 0/1 build (see `CLAUDE.md`,
`README.md`). Folders, `bin/` scripts, and this log established. No durable content
yet — see the first refresh below.

---

## Refresh — as-of 2026-07-15

**Requested by:** owner, as part of the initial build, to prove the ingest loop before
handing control back for further manually-invoked refreshes.

**Coverage:**

- Slack — complete for `flexpay-programme`, `flexpay-product`, `flexpay-eng`,
  `flexpay-legal`, `flexpay-compliance`, `flexpay-finance`. No material activity in
  `flexpay-csops` or `flexpay-gtm` in this window (both members' first messages are
  dated after 2026-07-15).
- Notion — partial by design: milestone list ingested as structural fact; the
  Programme Overview page excluded (its content is dated 2026-07-28, after this
  cursor). No milestone status asserted — none corroborated yet.
- Google Drive — partial: only the 2026-07-10 meeting-notes section and RAID rows
  dated `<= 2026-07-15` (D1, A2) ingested; later sections/rows excluded even though
  visible in the same document.

**Pages touched:** `projects/flexpay-au.md` (new), `decisions/d1-ml-credit-engine.md`
(new), all 8 `people/*.md` (new). `index.md` updated to list them.

**Contradictions:** none — first refresh, nothing to contradict yet.

**Judgment items for the owner:** none.

**Checks run:** `bin/regenerate-state` (10 pages picked up), `bin/lint-wiki` — 0
errors, 0 warnings.

**Commit:** see git log for the commit covering this as-of date.

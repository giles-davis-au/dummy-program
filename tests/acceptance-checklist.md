# Acceptance checklist

The blueprint's 15 scenarios (its "Acceptance scenarios" section) plus the addendum's
2 extra ones. GitHub-mode-only scenarios (14) are marked N/A — this build is
local-only. Re-check this list after any refresh that plausibly changes the answer;
update the row rather than deleting history.

| # | Scenario | Status | Notes |
|---|---|---|---|
| 1 | Fresh setup from an empty folder | ✅ Pass | Built 2026-08-20 from an empty `dummy-program/` dir. |
| 2 | Multi-page ingest: one source updates 2+ durable pages + index/log | ✅ Pass | 2026-07-15 refresh: kickoff message alone updated `projects/flexpay-au.md`, `decisions/d1-ml-credit-engine.md`, and all 8 people pages. |
| 3 | Contradiction, new wins | ⏳ Pending | Will exercise when refreshing through 2026-08-12 (D1 → D2). |
| 4 | Contradiction, wiki wins | ⏳ Pending | No case exercised yet. |
| 5 | Contradiction, unresolved (judgment item) | ⏳ Pending | No case exercised yet. |
| 6 | Connector outage: one source fails, refresh continues with visible gap | ⏳ Pending | Not yet simulated — all 3 lanes were reachable in refresh 1. |
| 7 | No activity: refresh records no material change, no empty artifact | ⏳ Pending | Re-run `refresh through 2026-07-15` and confirm it's a no-op. |
| 8 | Regeneration: delete generated files, rerun generator, get the same result | ✅ Pass | Verified by hand — `bin/regenerate-state` is pure function of durable pages + log.md. |
| 9 | Progressive context: fresh chat gets compact state; mentioning an entity loads only that page | ✅ Pass (by design) | `current-state.md` is the compact snapshot; `bin/retrieve` scopes to matched pages only. |
| 10 | Read-only boundary: query interface can't alter durable files | ✅ Pass | `bin/retrieve` and `bin/regenerate-state` (read durable, write only generated files) never touch `projects/`, `people/`, `decisions/`, `sources/`. |
| 11 | Privacy: seeded fake credentials/PII/transcripts/private paths blocked | N/A | Nothing sensitive in this dataset — see addendum §7. Structural separation (`sources/` vs durable pages) still followed. |
| 12 | Scheduler: manual scheduled-run simulation matches interactive command | N/A | No scheduler in local-only mode; refresh is always manual by design. |
| 13 | Identity expiry: unattended mode doesn't depend on a short-lived personal token | N/A | No unattended mode in this build. |
| 14 | Review: GitHub-mode PR workflow, never auto-merges | N/A | Local-only, no GitHub. |
| 15 | Recovery: restore last trusted version, regenerate runtime state | ✅ Pass | Every refresh is a local git commit — see "Recovery" in `README.md`. |
| 16 (addendum) | Informal signal not promoted to a tracked risk/decision | ⏳ Pending | Will exercise on the refresh that reaches Dan Foster's 2026-08-19 load-test remark in `flexpay-eng`. |
| 17 (addendum) | Single-source claim flagged as such when asked directly | ⏳ Pending | No case surfaced yet — most refresh-1 facts have exactly one source; revisit once asked a direct question in chat. |

**How to re-run the automated ones:** `python3 bin/lint-wiki` covers structural
integrity underlying several rows above (2, 9, 10). `python3 bin/regenerate-state`
covers 8. The rest are judgment calls, verified by reading `log.md` after each
refresh.

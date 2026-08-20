---
type: person
id: dan-foster
status: active
updated: 2026-10-01
sources:
  - sources/slack/2026-10-01.md#slack-eng-20260709-1012
  - sources/slack/2026-10-01.md#slack-eng-20260805-1638
  - sources/slack/2026-10-01.md#slack-eng-20260814-1705
  - sources/slack/2026-10-01.md#slack-eng-20260819-1402
  - sources/slack/2026-10-01.md#slack-programme-20260805-1641
  - sources/gdrive/2026-10-01.md#raid-decisions
---

# Dan Foster

**Function:** Engineering. Co-leads the Product & Engineering workstream with Maya
Chen.

## Timeline

- **2026-07-09** — Spun up the eng workstream board; first priority was nailing the
  merchant API contract with Product to unblock parallel credit-engine work,
  targeting early August.
- **2026-08-04** — Co-decided [D5 — QR wallet launch scope](../decisions/d5-qr-wallet-launch-scope.md)
  with Maya Chen. Single-source claim — see the decision page.
- **2026-08-05** — Merchant Console API contract signed off between Product and
  Eng — **M01 done**. Moved into credit engine integration and Console beta build,
  M02 target Sept 12.
  [sources/slack/2026-10-01.md#slack-programme-20260805-1641](../sources/slack/2026-10-01.md#slack-programme-20260805-1641)
- **2026-08-14** — Credit engine integration ~40% done, still on track for Sept 12
  (milestone M02 — see [flexpay-au.md](../projects/flexpay-au.md)); Console beta
  build also underway off Maya's handoff.
- **2026-08-19** — Ran an informal load test against the new decision engine;
  response times degraded noticeably above ~200 concurrent requests. Not yet clear
  whether this is a real ceiling or a staging-environment artifact. **Not escalated
  to a RAID risk** as of this refresh — per CLAUDE.md's informal-signal rule, this
  sits below "working draft" and is not treated as tracked programme state, though
  it's directly relevant to the existing formal risk **R1** ("engine not yet
  load-tested at national volumes," raised 2026-08-01, owned by Dan). Maya Chen
  agreed a proper load test is worth running before the pilot.
  [sources/slack/2026-10-01.md#slack-eng-20260819-1402](../sources/slack/2026-10-01.md#slack-eng-20260819-1402)

## Notes

Owns milestones **M02** (credit engine integration) and **M05** (PCI-DSS
penetration test) on the tracker, and RAID risk **R1**. See
[flexpay-au.md](../projects/flexpay-au.md).

---
type: decision
id: d2-rules-based-credit-model
status: current
updated: 2026-10-01
decided: 2026-08-12
sources:
  - sources/gdrive/2026-10-01.md#gdoc-20260812-sync
  - sources/gdrive/2026-10-01.md#raid-decisions
  - sources/slack/2026-10-01.md#slack-programme-20260812-1715
  - sources/slack/2026-10-01.md#slack-compliance-20260812-1740
  - sources/slack/2026-10-01.md#slack-finance-20260812-1810
  - sources/slack/2026-10-01.md#slack-legal-20260812-1802
---

# D2 — Launch with a rules-based credit model plus manual review

**Decision:** Launch with a simpler, explainable rules-based credit decision model
plus a manual review queue for edge cases, instead of the fully automated ML model
planned under [D1 — ML-based credit engine](d1-ml-credit-engine.md). The ML-based
model is deferred to a post-launch iteration. **Supersedes
[D1](d1-ml-credit-engine.md).**

**Decided by:** Giles Davis, Owen Mackay, Isla Novak — at the 2026-08-12 weekly sync.

**Rationale:**
- Compliance (Owen Mackay) needed something easier to explain and evidence for the
  AUSTRAC AML/CTF assessment than a fully automated ML model.
- Finance (Isla Novak) wanted a more conservative, better-understood risk exposure
  profile at initial scale — the programme carries the lending exposure entirely on
  Money Ltd's own balance sheet, with no external credit partner to share it.

This is the most heavily corroborated decision in the programme so far — the same
decision, dated 2026-08-12, is independently confirmed by the meeting notes doc, the
RAID log's Decisions table, and four separate people posting to four different Slack
channels the same day: Giles ([Slack, #flexpay-programme](../sources/slack/2026-10-01.md#slack-programme-20260812-1715)),
Owen ([Slack, #flexpay-compliance](../sources/slack/2026-10-01.md#slack-compliance-20260812-1740)),
Isla ([Slack, #flexpay-finance](../sources/slack/2026-10-01.md#slack-finance-20260812-1810)), and
Priya ([Slack, #flexpay-legal](../sources/slack/2026-10-01.md#slack-legal-20260812-1802)).

**Downstream effects:**
- Priya Shah re-based PDS drafting assumptions on the rules-based model — see
  [priya-shah.md](../people/priya-shah.md).
- Dan Foster re-scoped M02 engineering work around the rules-based approach — see
  [dan-foster.md](../people/dan-foster.md) and
  [flexpay-au.md](../projects/flexpay-au.md).

Source: [sources/gdrive/2026-10-01.md#gdoc-20260812-sync](../sources/gdrive/2026-10-01.md#gdoc-20260812-sync),
[sources/gdrive/2026-10-01.md#raid-decisions](../sources/gdrive/2026-10-01.md#raid-decisions)

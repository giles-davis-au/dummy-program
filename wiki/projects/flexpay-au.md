---
type: project
id: flexpay-au
status: active — RAG Amber
updated: 2026-10-01
sources:
  - sources/slack/2026-10-01.md#slack-programme-20260708-0900
  - sources/slack/2026-10-01.md#slack-gtm-20260722-1000
  - sources/slack/2026-10-01.md#slack-programme-20260805-1641
  - sources/slack/2026-10-01.md#slack-finance-20260806-1015
  - sources/slack/2026-10-01.md#slack-csops-20260810-1400
  - sources/slack/2026-10-01.md#slack-product-20260811-0918
  - sources/slack/2026-10-01.md#slack-eng-20260814-1705
  - sources/slack/2026-10-01.md#slack-compliance-20260815-0950
  - sources/slack/2026-10-01.md#slack-programme-20260815-1005
  - sources/slack/2026-10-01.md#slack-compliance-20260818-1120
  - sources/slack/2026-10-01.md#slack-gtm-20260819-1115
  - sources/slack/2026-10-01.md#slack-product-20260819-1510
  - sources/slack/2026-10-01.md#slack-csops-20260819-1600
  - sources/slack/2026-10-01.md#slack-legal-20261001-0947
  - sources/notion/2026-10-01.md#notion-overview
  - sources/notion/2026-10-01.md#notion-m01
  - sources/notion/2026-10-01.md#notion-m02
  - sources/notion/2026-10-01.md#notion-m03
  - sources/notion/2026-10-01.md#notion-m04
  - sources/notion/2026-10-01.md#notion-m05
  - sources/notion/2026-10-01.md#notion-m06
  - sources/notion/2026-10-01.md#notion-m07
  - sources/notion/2026-10-01.md#notion-m08
  - sources/notion/2026-10-01.md#notion-m09
  - sources/notion/2026-10-01.md#notion-m10
  - sources/gdrive/2026-10-01.md#raid-risks
  - sources/gdrive/2026-10-01.md#raid-assumptions
---

# FlexPay AU

In-house BNPL (buy-now-pay-later) installment product: QR checkout, merchant
onboarding, and an own-built credit decisioning engine, funded off Money Ltd's own
balance sheet (no external credit partner). Three workstreams: **Product &
Engineering** (Maya Chen, Dan Foster), **Compliance / Legal / Finance** (Owen Mackay,
Priya Shah, Isla Novak), **Operations & Launch Readiness** (Ben Okafor, Grace
Lindqvist). Sponsored and run by Giles Davis, who chairs the weekly programme sync.

**Target GA: 16 November 2026.**
[sources/slack/2026-10-01.md#slack-programme-20260708-0900](../sources/slack/2026-10-01.md#slack-programme-20260708-0900)

## Programme status

**RAG: Amber**, since 2026-08-15 — Giles Davis moved it from Green due to newly
published AUSTRAC transaction-monitoring guidance (July 2026) putting the M03
AML/CTF sign-off date at risk (see risk R2 below).
[sources/slack/2026-10-01.md#slack-programme-20260815-1005](../sources/slack/2026-10-01.md#slack-programme-20260815-1005)

The Notion "FlexPay AU — Programme Overview" page still shows "🟢 Green," but it
carries an explicit "Last updated: 2026-07-28" line — before the Amber call — so it
simply hasn't been re-edited since, not a genuine conflict. See
[sources/notion/2026-10-01.md#notion-overview](../sources/notion/2026-10-01.md#notion-overview).

## Milestones

Status column reconciles the Notion tracker's raw value against dated Slack /
meeting-note evidence, per CLAUDE.md's Notion caveat (a Notion status alone is never
trusted). Three milestones (marked †) needed correction — Notion showed "Not
started" where dated evidence showed work already underway.

| ID | Milestone | Owner | Due | Notion status | Corroborated status |
|---|---|---|---|---|---|
| M01 | Merchant Console API contract finalized | Dan Foster | 2026-08-05 | Done | **Done** — confirmed by Dan Foster, [Slack 2026-08-05](https://gbd-dummy-program.slack.com/archives/C0BRF7YRF98/p1787198855085669) ([Notion](https://app.notion.com/p/3c261566afbf8142be59dd998a055e72)) |
| M02 | In-house credit decision engine integration complete | Dan Foster | 2026-09-12 | In progress | **In progress**, ~40% as of [Slack 2026-08-14](https://gbd-dummy-program.slack.com/archives/C0BRH6WPSQZ/p1787198875998609) ([Notion](https://app.notion.com/p/3c261566afbf8153b9b3c40e88e31551)) |
| M03 | AML/CTF risk assessment sign-off (AUSTRAC) | Owen Mackay | 2026-09-25 | In progress | **In progress**, at risk of slipping per [Slack 2026-08-18](https://gbd-dummy-program.slack.com/archives/C0BRF81U0P4/p1787199165863869) — see risk R2 ([Notion](https://app.notion.com/p/3c261566afbf813ca51cd9b0a789a877)) |
| M04 | Merchant onboarding portal (Console) beta | Maya Chen | 2026-09-18 | In progress | **In progress** — beta build started [Slack 2026-08-11](https://gbd-dummy-program.slack.com/archives/C0BRBEYG5NZ/p1787199149312689), feedback round done [Slack 2026-08-19](https://gbd-dummy-program.slack.com/archives/C0BRBEYG5NZ/p1787199151279559) (risk R3) ([Notion](https://app.notion.com/p/3c261566afbf8113b563dfed016a781a)) |
| M05 | PCI-DSS / security penetration test complete | Dan Foster | 2026-09-30 | Not started | **Not started/unconfirmed** — no corroborating Slack or notes activity found ([Notion](https://app.notion.com/p/3c261566afbf81508d06c69c8b266359)) |
| M06 † | Customer support playbook & training complete | Ben Okafor | 2026-10-10 | Not started | **In progress** — first draft of playbook structure up [Slack 2026-08-10](https://gbd-dummy-program.slack.com/archives/C0BRH78PDED/p1787199179284279); Ben syncing with Maya on support docs [Slack 2026-08-19](https://gbd-dummy-program.slack.com/archives/C0BRH78PDED/p1787199181173359) ([Notion](https://app.notion.com/p/3c261566afbf81f58037dc4dc8e19b66)) |
| M07 † | PDS approved by Legal | Priya Shah | 2026-10-02 | Not started | **In progress, completion confirmed** — outside counsel review clean, sign-off confirmed for **4 October** (2 days after the tracker's due date) per Priya's [Slack 2026-10-01](https://gbd-dummy-program.slack.com/archives/C0BR91NM3FD/p1787199156672889) post; not yet complete as of this refresh's cutoff ([Notion](https://app.notion.com/p/3c261566afbf8168be76e8ab9412d416)) |
| M08 | Pilot merchant cohort live (10 merchants, Sydney) | Ben Okafor | 2026-10-20 | Not started | **Not started** — consistent with evidence, due date is after this refresh's cutoff ([Notion](https://app.notion.com/p/3c261566afbf8102b07ae244247a618a)) |
| M09 † | GTM campaign assets finalized | Grace Lindqvist | 2026-10-28 | Not started | **In progress** — concepting underway since [Slack 2026-07-22](https://gbd-dummy-program.slack.com/archives/C0BR91ZDD1R/p1787199183064139), asset production kicked off [Slack 2026-08-19](https://gbd-dummy-program.slack.com/archives/C0BR91ZDD1R/p1787199187111339) ([Notion](https://app.notion.com/p/3c261566afbf81949e28f6c0136c9e86)) |
| M10 | General Availability — national launch | Giles Davis | 2026-11-16 | Not started | **Not started** — consistent with evidence ([Notion](https://app.notion.com/p/3c261566afbf81b09275e5acfe9d267a)) |

Every fact above is now cited inline (Slack for corroboration, Notion for the raw
tracker row) — no separate lookup needed. See the "Team" section below, or
[index.md](../index.md)'s People list, for each person's fuller timeline.

## Decisions

| ID | Decision | Decided | Status |
|---|---|---|---|
| [D1](../decisions/d1-ml-credit-engine.md) | In-house ML-based credit decision engine | 2026-07-10 | Superseded by D2 |
| [D2](../decisions/d2-rules-based-credit-model.md) | Rules-based credit model + manual review | 2026-08-12 | Current |
| [D3](../decisions/d3-sydney-pilot.md) | Sydney-only pilot (10 merchants) before national rollout | 2026-08-14 | Current |
| [D4](../decisions/d4-gtm-spend-gate.md) | GTM spend gated on Sydney pilot success | 2026-08-18 | Current |
| [D5](../decisions/d5-qr-wallet-launch-scope.md) | Apple Pay / Google Pay at launch, NFC deferred | 2026-08-04 | Current — single-source |

## Risks

From the [RAID log](https://docs.google.com/spreadsheets/d/11gmeOS49ECmWJGkD1XIJZDExR5iPgzhllL0Op0fdeVU/edit)
(Risks table). Three of the four are independently corroborated by a dated Slack
post from the owning function on the same raised date — **R1 is not**: no Slack
message matching its 2026-08-01 raised date was found anywhere in the capture, so
it's RAID-log-only, single-source (this page previously claimed all four were
corroborated — that was wrong for R1, corrected here):

| ID | Risk | Severity | Owner | Raised |
|---|---|---|---|---|
| R1 | Credit decision engine not yet load-tested at projected national volumes — risk of checkout latency/timeouts at GA | High | Dan Foster | 2026-08-01 — single-source, RAID log only |
| R2 | New AUSTRAC transaction-monitoring rules (Jul 2026) may require AML/CTF rework, threatening M03 | High | Owen Mackay | [Slack 2026-08-15](https://gbd-dummy-program.slack.com/archives/C0BRF81U0P4/p1787199164078059) |
| R3 | Console beta onboarding UX friction (document upload step) — risk to merchant adoption | Medium | Maya Chen | [Slack 2026-08-19](https://gbd-dummy-program.slack.com/archives/C0BRBEYG5NZ/p1787199151279559) |
| R4 | Balance-sheet capital allocation for BNPL lending exposure not yet finalized — could cap pilot cohort or delay GA | Medium-High | Isla Novak | [Slack 2026-08-06](https://gbd-dummy-program.slack.com/archives/C0BRBEW05KP/p1787199169766649) |

**R1 — additional informal context (not a status change):** Dan Foster ran an
informal load test on 2026-08-19 and saw response-time degradation above ~200
concurrent requests. Per CLAUDE.md's informal-signal rule this has **not** been
escalated into a RAID entry or meeting-note mention, so it does not change R1's
logged severity or status here — it's noted as real but informal, single-source,
and unescalated. See [dan-foster.md](../people/dan-foster.md) for the full remark
and citation.

## Assumptions

| ID | Assumption | Linked risk | Owner | Raised |
|---|---|---|---|---|
| A1 | In-house credit engine supports national volumes without redesign | R1 | Dan Foster | 2026-08-01 |
| A2 | Existing balance-sheet lending authority is sufficient without new regulatory approval | R4 | Isla Novak | 2026-07-15 |

## Issues

None formally logged as of this refresh (2026-10-01) — "no material activity," not
"unavailable."

## Team

Giles Davis (sponsor, see [giles-davis.md](../people/giles-davis.md)) ·
[maya-chen.md](../people/maya-chen.md) & [dan-foster.md](../people/dan-foster.md)
(Product & Engineering) · [owen-mackay.md](../people/owen-mackay.md),
[priya-shah.md](../people/priya-shah.md) & [isla-novak.md](../people/isla-novak.md)
(Compliance / Legal / Finance) · [ben-okafor.md](../people/ben-okafor.md) &
[grace-lindqvist.md](../people/grace-lindqvist.md) (Operations & Launch Readiness).

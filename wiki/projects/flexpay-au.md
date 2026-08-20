---
type: project
id: flexpay-au
status: active — RAG Amber
updated: 2026-10-01
sources:
  - sources/slack/2026-10-01.md#slack-programme-20260708-0900
  - sources/slack/2026-10-01.md#slack-programme-20260815-1005
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
| M01 | Merchant Console API contract finalized | Dan Foster | 2026-08-05 | Done | **Done** — confirmed by Dan Foster 2026-08-05 |
| M02 | In-house credit decision engine integration complete | Dan Foster | 2026-09-12 | In progress | **In progress**, ~40% as of 2026-08-14 |
| M03 | AML/CTF risk assessment sign-off (AUSTRAC) | Owen Mackay | 2026-09-25 | In progress | **In progress**, at risk of slipping — see risk R2 |
| M04 | Merchant onboarding portal (Console) beta | Maya Chen | 2026-09-18 | In progress | **In progress** — beta build started 2026-08-11, feedback round done 2026-08-19 (risk R3) |
| M05 | PCI-DSS / security penetration test complete | Dan Foster | 2026-09-30 | Not started | **Not started/unconfirmed** — no corroborating Slack or notes activity found |
| M06 † | Customer support playbook & training complete | Ben Okafor | 2026-10-10 | Not started | **In progress** — first draft of playbook structure up 2026-08-10; Ben syncing with Maya on support docs 2026-08-19 |
| M07 † | PDS approved by Legal | Priya Shah | 2026-10-02 | Not started | **In progress, completion confirmed** — outside counsel review clean, sign-off confirmed for **4 October** (2 days after the tracker's due date) per Priya's 2026-10-01 post; not yet complete as of this refresh's cutoff |
| M08 | Pilot merchant cohort live (10 merchants, Sydney) | Ben Okafor | 2026-10-20 | Not started | **Not started** — consistent with evidence, due date is after this refresh's cutoff |
| M09 † | GTM campaign assets finalized | Grace Lindqvist | 2026-10-28 | Not started | **In progress** — concepting underway since 2026-07-22, asset production kicked off 2026-08-19 |
| M10 | General Availability — national launch | Giles Davis | 2026-11-16 | Not started | **Not started** — consistent with evidence |

Sources: [sources/notion/2026-10-01.md](../sources/notion/2026-10-01.md) (all
milestone rows), corroborating Slack posts cited on each person's page (see
[people/](../people/)).

## Decisions

| ID | Decision | Decided | Status |
|---|---|---|---|
| [D1](../decisions/d1-ml-credit-engine.md) | In-house ML-based credit decision engine | 2026-07-10 | Superseded by D2 |
| [D2](../decisions/d2-rules-based-credit-model.md) | Rules-based credit model + manual review | 2026-08-12 | Current |
| [D3](../decisions/d3-sydney-pilot.md) | Sydney-only pilot (10 merchants) before national rollout | 2026-08-14 | Current |
| [D4](../decisions/d4-gtm-spend-gate.md) | GTM spend gated on Sydney pilot success | 2026-08-18 | Current |
| [D5](../decisions/d5-qr-wallet-launch-scope.md) | Apple Pay / Google Pay at launch, NFC deferred | 2026-08-04 | Current — single-source |

## Risks

From the RAID log, all corroborated by dated Slack posts from the owning function
(see each person's page for the matching post):

| ID | Risk | Severity | Owner | Raised |
|---|---|---|---|---|
| R1 | Credit decision engine not yet load-tested at projected national volumes — risk of checkout latency/timeouts at GA | High | Dan Foster | 2026-08-01 |
| R2 | New AUSTRAC transaction-monitoring rules (Jul 2026) may require AML/CTF rework, threatening M03 | High | Owen Mackay | 2026-08-15 |
| R3 | Console beta onboarding UX friction (document upload step) — risk to merchant adoption | Medium | Maya Chen | 2026-08-19 |
| R4 | Balance-sheet capital allocation for BNPL lending exposure not yet finalized — could cap pilot cohort or delay GA | Medium-High | Isla Novak | 2026-08-06 |

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

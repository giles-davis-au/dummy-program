---
type: project
id: flexpay-au
status: active
updated: 2026-07-15
sources:
  - sources/slack/2026-07-15.md#giles-2026-07-08
  - sources/gdrive/2026-07-15.md#meeting-2026-07-10
  - sources/notion/2026-07-15.md#tracker-structural-2026-07-15
---

# FlexPay AU

**Summary:** Programme kicked off 2026-07-08, targeting national GA 16 Nov 2026; all
three workstreams are underway, no milestones confirmed complete yet.

## Overview

FlexPay AU is a fully in-house BNPL (buy-now-pay-later) installment product — QR
checkout, merchant onboarding, own credit decisioning engine — funded off the
company's own balance sheet (no external credit partner). Target GA: **16 November
2026**. Kicked off 2026-07-08 by Giles Davis (sponsor).
[sources/slack/2026-07-15.md#giles-2026-07-08](../sources/slack/2026-07-15.md),
[sources/gdrive/2026-07-15.md#meeting-2026-07-10](../sources/gdrive/2026-07-15.md)

## Workstreams

- **Product & Engineering** — [Maya Chen](../people/maya-chen.md), [Dan Foster](../people/dan-foster.md)
- **Compliance / Legal / Finance** — [Owen Mackay](../people/owen-mackay.md), [Priya Shah](../people/priya-shah.md), [Isla Novak](../people/isla-novak.md)
- **Operations & Launch Readiness** — [Ben Okafor](../people/ben-okafor.md), [Grace Lindqvist](../people/grace-lindqvist.md)

Sponsor / programme lead: [Giles Davis](../people/giles-davis.md).
[sources/gdrive/2026-07-15.md#meeting-2026-07-10](../sources/gdrive/2026-07-15.md)

## Milestones (from Notion tracker, structural only)

Per the Notion caveat in `CLAUDE.md`, the tracker has no per-row history, so status is
not asserted here yet — only the plan as it stands. None of these ten milestones have
dated corroboration of a status change as of this refresh.

| ID | Milestone | Owner | Due |
|---|---|---|---|
| M01 | Merchant Console API contract finalized | Dan Foster | 2026-08-05 |
| M02 | In-house credit decision engine integration complete | Dan Foster | 2026-09-12 |
| M03 | AML/CTF risk assessment sign-off (AUSTRAC) | Owen Mackay | 2026-09-25 |
| M04 | Merchant Console beta | Maya Chen | 2026-09-18 |
| M05 | PCI-DSS / security penetration test complete | Dan Foster | 2026-09-30 |
| M06 | Support playbook & training complete | Ben Okafor | 2026-10-10 |
| M07 | PDS approved by Legal | Priya Shah | 2026-10-02 |
| M08 | Pilot merchant cohort live (Sydney, 10 merchants) | Ben Okafor | 2026-10-20 |
| M09 | GTM campaign assets finalized | Grace Lindqvist | 2026-10-28 |
| M10 | General Availability — national launch | Giles Davis | 2026-11-16 |

[sources/notion/2026-07-15.md#tracker-structural-2026-07-15](../sources/notion/2026-07-15.md)

## Decisions

- [D1 — in-house ML credit decision engine](../decisions/d1-ml-credit-engine.md) —
  current as of this refresh, decided at kickoff 2026-07-10.

## Timeline (events known as of 2026-07-15)

- **2026-07-08** — Programme kickoff (Slack, `flexpay-programme`).
- **2026-07-09** — Product and Eng workstreams both spin up scoping/planning.
- **2026-07-10** — Kickoff / weekly sync; D1 decided.
- **2026-07-11** — Legal starts PDS drafting.
- **2026-07-14** — Compliance starts AML/CTF risk assessment, targeting M03 by Sept 25.
- **2026-07-15** — Finance starts capital allocation modelling (A2 assumption raised).

## Open loops

- Priya (Legal) is blocked on the credit model approach being locked in before PDS
  drafting can fully proceed. [sources/slack/2026-07-15.md#priya-2026-07-11](../sources/slack/2026-07-15.md)
- Dan/Maya owe the Merchant Console API contract by early August (per kickoff notes).
  [sources/gdrive/2026-07-15.md#meeting-2026-07-10](../sources/gdrive/2026-07-15.md)

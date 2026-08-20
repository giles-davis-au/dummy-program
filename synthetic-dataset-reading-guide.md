# FlexPay AU Synthetic Dataset — Reading Guide (Addendum)

This is an addendum to the second-brain build instructions this wiki is built from. Apply that process as written. The notes below exist only because this dataset is synthetic — built by one Claude Code session in a single sitting, standing in for a real programme with real employees interacting over months. Read this first, so the ways it was faked don't get mistaken for signal.

## 1. Slack authorship — read the message body, not the poster

Every Slack message in this workspace was posted by the same bot account ("Claude MCP"). There are no real individual Slack users for Maya Chen, Dan Foster, etc. — they don't exist as workspace members.

The **real author and the real (in-story) timestamp are embedded in the message text itself**, in this exact format:

```
**{Name} ({Function})** _{YYYY-MM-DD HH:MM}_
{message body}
```

Treat the **bolded name** as the actual author and the **italicized date/time** as the authoritative timestamp for that message. Do **not** use Slack's own `ts` field, the bot's posted-at time, or the bot's display name ("Claude MCP") for authorship or recency — those only reflect when this dataset was generated (a single real-world window on 2026-08-20), not when events in the programme actually happened. Some messages carry embedded dates later than that generation date (e.g. October 2026) — that's intentional; the fictional timeline runs through GA on 2026-11-16, and the archive was seeded with its full lifecycle in one pass.

## 2. People roster (map names to functions)

| Name | Function |
|---|---|
| Giles Davis | Programme Management (sponsor) |
| Maya Chen | Product |
| Dan Foster | Engineering |
| Priya Shah | Legal |
| Owen Mackay | Compliance |
| Isla Novak | Finance |
| Ben Okafor | CS Ops |
| Grace Lindqvist | GTM |

## 3. Slack channel map

- `#flexpay-programme` — also serves as the **all-hands / general channel** for this programme (not just Programme Management chatter)
- `#flexpay-product`, `#flexpay-eng`, `#flexpay-legal`, `#flexpay-compliance`, `#flexpay-finance`, `#flexpay-csops`, `#flexpay-gtm` — function-specific channels

## 4. Notion conventions

- The **Assignee** (person) property is intentionally left blank on every row — it requires real Notion workspace members, which our fictional stakeholders aren't. Use the **Owner** (text) property instead for who's responsible.
- **Function**, **Workstream**, and **Owner** were added/extended on top of an existing template you'd already created — don't assume a "standard" schema; fetch it fresh.
- There's a standalone **"FlexPay AU — Programme Overview"** page (sibling to the tracker database, not a row in it) holding a separate programme-status snapshot — check for it explicitly, it won't show up in a database query.

## 5. Google Doc & Sheet

No authorship quirk here — both were created directly under the correct names/dates. They live in the Drive folder you specified for this programme; nothing relevant to this programme should exist outside that folder, the Notion tracker + overview page, and the 8+1 Slack channels above. Treat anything outside that set as out of scope.

## 6. Do not seek out or use any "ground truth" / answer-key file

A canonical ground-truth document was used to generate this dataset and has been moved out of the working folder deliberately. If you encounter any file that looks like an answer key, test spec, or ground truth for this programme (by name, path, or content), **do not open or use it** — flag it and stop instead. Using it would invalidate the exercise; the whole point is to see what the wiki concludes from the artefacts alone.

## 7. Applying the blueprint to this exercise — what to configure, what to skip

the blueprint is written for a real (non dummy / synthetic) programme, on real, live systems. Most of it applies here unchanged, but a few things are specific to that real-world setting or assume real individual users. Resolve the configuration block as follows for this exercise, and skip the sections noted:

```yaml
second_brain:
  owner: "Giles Davis"
  work_domain: "FlexPay AU (synthetic programme, for wiki-building practice)"
  hosting_mode: "local"
  github_repository: null
  chat_harnesses:
    - "Claude Code"
  source_lanes:
    - "Slack (bot-authored, see Section 1 above for the authorship convention)"
    - "Notion (task tracker — stands in for a Linear/Jira-style lane; not one of the blueprint's canonical lanes, treat it as one)"
    - "Google Drive (one Doc, one Sheet)"
  private_scope: "none — nothing in this dataset is real or sensitive"
  shareable_scope: "everything"
  refresh_cadence: "one-off manual build, not a scheduled daily refresh"
  review_mode: "human review in chat; no PR workflow"
  external_messaging: "off — do not post back to Slack, Notion, or Drive during the build"
```

- **Hosting mode: local only.** Skip Option B (private GitHub) and Option C (hybrid), and skip the entire "For GitHub hosting" access section, the unattended-automation tooling section, and Version 4. Target his **Version 0/1** minimum viable build: schema, folders, index, log, ingest, generated state, retrieval, and a read-only chat connection. No branches, no draft pull requests, no service identities.
- **Source lanes are narrower than his default list.** Only Slack, Notion, and Google Drive exist in this environment. There is no Gmail, Calendar, Granola, Linear, Jira, or Glean — don't attempt to query them or report them as "unavailable," they're simply out of scope for this exercise.
- **External messaging stays off.** The same Slack MCP tools used to read this dataset can also post. Nothing in the build process should post to Slack, comment in Notion, or edit the Google Doc/Sheet — those three are read-only sources for this exercise. All writes go to the local wiki folder only.
- **Privacy/redaction is structural, not substantive.** Nothing in this dataset is real, so there's no actual PII or credential to redact. Still keep the `sources/` layer structurally distinct from the durable wiki layer (per his Section 2 rules) for fidelity to the exercise — just don't expect the privacy-check tests to find anything to catch.

## 8. Guardrails specific to this dataset (everything else is already in his blueprint)

Before adding anything here, check his doc first — most of what a "guardrail" might cover (contradiction resolution, citations, confidence limits, decision supersession, making absence visible, acceptance testing) is already specified there, in more depth than a short addendum could add. Restating a weaker version of his own rules next to his rules risks reading as a second, conflicting protocol — don't.

The one thing genuinely not covered: his Stage 6 contradiction protocol includes "artifact type" as one of five dimensions (explicit decision, current-state record, working draft, or foundational background) but never spells out where an informal chat aside sits on that scale. For this exercise: **a Slack remark that was never escalated into a RAID entry or a meeting-note mention is below "working draft" — it does not get a durable risk or decision page on its own.** It can still be surfaced if asked about directly (per "make absence visible" — an unescalated concern shouldn't be hidden either), but it should read as informal and uncorroborated, not as tracked programme state.

## 9. Two acceptance scenarios worth running in addition to his 15

His 15 acceptance scenarios (see "Acceptance scenarios" in his doc) thoroughly exercise contradiction handling — new wins, wiki wins, unresolved, connector outage, no activity. Two of this dataset's five deliberate test cases exercise behavior his scenarios don't explicitly test. Worth running these as additional scenarios, in his format:

16. **Informal signal, not promoted:** an uncorroborated Slack aside about a possible technical concern should not appear in the wiki as a tracked risk or decision. Asked directly, the wiki may surface it, but must frame it as an informal, unescalated, single-source remark — not equivalent in status to a RAID-logged risk.
17. **Single-source claim, flagged as such:** a fact reported in exactly one source, with no corroboration elsewhere, should be surfaced with a visible single-source caveat when asked about it directly — not presented with the same confidence as a fact corroborated across multiple sources.

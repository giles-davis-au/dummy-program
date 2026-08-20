# Source Addressability — Addendum

> An addendum to an AI second-brain blueprint. Apply that process as
> written; this closes one specific gap discovered while building a second brain
> against real connectors (Slack, Notion, Google Drive) for a synthetic programme.
> Programme-agnostic — reuse this on any build, not just that one.

## The gap

The blueprint's schema section says the instruction file should define "which live
sources to check." Built literally, that reads as satisfied by *naming* the sources —
"the Q3 Planning database," "the #finance-ops channel," "the shared Drive folder."
That's not enough on its own, for two separate reasons:

1. **A name isn't a resolvable address.** A fresh agent session — or the same session
   after context is lost — has to re-*search* for something named only in prose, and
   hope the match is unambiguous. One connected workspace tends to have near-duplicate
   names over time (an old "Q3 Planning" and a new one, a renamed channel). A stable
   ID (channel ID, page ID, folder ID) doesn't have that problem; a name does.
2. **A named list goes stale the moment the source grows.** If the schema file
   enumerates "the tracker database and the overview page" as the Notion scope, that
   list is a snapshot from whenever someone wrote it. A new child page added six
   months later — a steering-committee deck, a new workstream's page — isn't in scope
   until a human notices and edits the instruction file. That's exactly the kind of
   manual upkeep a second brain is supposed to eliminate, not reintroduce.

Both problems showed up in practice: an instruction file that named Slack channels,
a Notion database, and a Drive folder by name only, with zero recorded IDs. Fixing it
after the fact meant re-deriving identifiers that had already been resolved once
during the original build and simply never written down — wasted work that a stable
ID, recorded once, would have avoided entirely.

## The rule

**Every source lane gets a resolvable root identifier recorded in the schema file, not
just a name — and any lane whose contents can grow gets a live re-enumeration
instruction anchored to that root, not a hardcoded list of what it currently
contains.**

Concretely, for each lane:

- **Record the stable ID/address**, not only the display name: a channel ID, a page or
  database ID, a folder ID, a mailbox/label ID — whatever the connector's own
  addressing scheme is. Include a direct link where the connector's UI supports one,
  for a human to click straight through.
- **If the lane has a natural container-with-children shape** (a parent page with
  child pages, a folder with files, a workspace with channels), anchor to the
  container's ID and instruct: *re-enumerate the container's current contents at the
  start of every refresh's capture step — never rely on a remembered list.* State the
  currently-known contents as an illustrative snapshot, explicitly labeled as
  non-exhaustive, so it's still useful as a sanity check without being treated as the
  ceiling of what's in scope.
- **Anything a per-item evidence-quality caveat applies to** (e.g. "this connector
  doesn't expose real per-row history," "this page type carries its own
  last-updated marker") should be phrased generically enough to apply to an item
  discovered later by the live enumeration, not hardcoded to only the items named at
  build time. If the caveat only actually applies to one specific, structurally
  unique item, say that explicitly rather than leaving it ambiguous whether it
  generalizes.

## Where this fits in the blueprint

- **Section "3. Schema and instruction layer"** — add "resolvable source identifiers
  and, for growable sources, a live-enumeration instruction" to the list of things the
  schema should define, alongside citation rules and contradiction resolution.
- **Section "Required deliverables" (machine build contract)** — deliverable #2 (the
  canonical instruction file) should explicitly cover "source identifiers and
  traversal," not just "ingest, query, refresh, lint, citations, contradictions,
  privacy, and page conventions."
- **"Non-negotiable behaviors"** — add: *Never hardcode a static list of child
  pages/files/channels for a source whose contents can grow. Anchor to a stable
  parent/root ID and re-enumerate live at each refresh.*
- This is a distinct concern from the existing Source-layer rule "link to the
  original system when permitted" — that rule is about citing *captured evidence*
  back to its origin. This addendum is about the schema file being able to
  *relocate its own sources* without a human re-supplying URLs each time. Keep both;
  neither replaces the other.

## A template for the schema file's source-scope section

```
- **{Lane}** — anchored at {container type} `{stable ID}` ({direct link if the
  connector supports one}). At the start of every refresh's capture step,
  re-{list/fetch/enumerate} this {container} fresh and treat whatever it currently
  contains as in scope — never rely on a remembered list. As of {date}, that's
  {known children/items}, but this is illustrative, not exhaustive: something added
  later is picked up automatically by the next refresh's live enumeration, with no
  edit to this file required.
```

## Why it's worth the extra sentence

The cost of writing this at build time is small — a few extra lines per lane, once.
The cost of skipping it compounds: every future refresh either re-derives identifiers
that were already known once, or silently misses anything added to a source after the
schema file was last hand-edited. For a wiki whose entire value proposition is "stop
re-deriving the same knowledge on every query," leaving the *source addressing itself*
un-derived is the same failure one layer up.

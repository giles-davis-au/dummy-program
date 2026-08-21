# Giles' Blueprint Addendums

Addendum to [ai-second-brain-blueprint.md](../ai-second-brain-blueprint.md) and to
[CLAUDE.md](../CLAUDE.md). **Maintained by the owner (Giles Davis)** — Claude Code
should read this file before a refresh, alongside CLAUDE.md, but should not write
to it (see CLAUDE.md's "What the agent may edit"). Where an entry here conflicts
with CLAUDE.md or the blueprint, this file wins — it exists precisely to record
corrections made after those files were last edited.

This is a single, running file: every tweak/gap discovered while building or
running a wiki off the blueprint gets its own section below, in the order
discovered. Each section starts with a short *context* line explaining what
prompted it, then the detail. This file supersedes two earlier separate files
(`source-addressability-addendum.md`, `live-link-citation-completeness.md`), whose
content is folded in below unchanged in substance.

## Contents

1. [Source Addressability](#1-source-addressability)
2. [Live-Link Citation Completeness](#2-live-link-citation-completeness)
3. [Anchor Navigation: Heading-as-Slug, Not `<a id>` Tags](#3-anchor-navigation-heading-as-slug-not-a-id-tags)
4. [Known Gap: CLAUDE.md's Link-Path Wording vs. Actual Lint Behavior](#4-known-gap-claudemds-link-path-wording-vs-actual-lint-behavior)
5. [Self-Audit Against a Rule's Full Literal Scope](#5-self-audit-against-a-rules-full-literal-scope)
6. [Flag Unverified Claims About External Tool Behavior](#6-flag-unverified-claims-about-external-tool-behavior)
7. [Track Deferred Items](#7-track-deferred-items)

---

## 1. Source Addressability

*Context: discovered while building the FlexPay AU wiki — the blueprint's schema
guidance says to define "which live sources to check," and built literally that
reads as satisfied by naming sources in prose alone. It isn't. Programme-agnostic —
reuse on any build, not just this one.*

**Status:** already reflected in this repo's `CLAUDE.md`, "Source scope" section
(resolvable IDs recorded per lane, live re-enumeration instruction, illustrative-
not-exhaustive framing). No further CLAUDE.md change needed here — kept below for
the blueprint-level "why" and template.

### The gap

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

### The rule

**Every source lane gets a resolvable root identifier recorded in the schema file, not
just a name — and any lane whose contents can grow gets a live re-enumeration
instruction anchored to that root, not a hardcoded list of what it currently
contains.**

Concretely, for each lane:

- **Record the stable ID/address**, not only the display name: a channel ID, a page or
  database ID, a folder ID, a mailbox/label ID — whatever the connector's own
  addressing scheme is. Include a direct link where the connector's UI supports one,
  for a human to click straight through. (See [§2](#2-live-link-citation-completeness)
  below — that section is this same requirement applied to a refresh's *output*, not
  just the schema file. Both were needed; neither replaces the other.)
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

### Where this fits in the blueprint

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

### A template for the schema file's source-scope section

```
- **{Lane}** — anchored at {container type} `{stable ID}` ({direct link if the
  connector supports one}). At the start of every refresh's capture step,
  re-{list/fetch/enumerate} this {container} fresh and treat whatever it currently
  contains as in scope — never rely on a remembered list. As of {date}, that's
  {known children/items}, but this is illustrative, not exhaustive: something added
  later is picked up automatically by the next refresh's live enumeration, with no
  edit to this file required.
```

### Why it's worth the extra sentence

The cost of writing this at build time is small — a few extra lines per lane, once.
The cost of skipping it compounds: every future refresh either re-derives identifiers
that were already known once, or silently misses anything added to a source after the
schema file was last hand-edited. For a wiki whose entire value proposition is "stop
re-deriving the same knowledge on every query," leaving the *source addressing itself*
un-derived is the same failure one layer up.

---

## 2. Live-Link Citation Completeness

*Context: discovered during the FlexPay AU wiki's 2026-10-01 Version 0 build.
CLAUDE.md already required a live link next to every quoted fact, but that rule
turned out to have a narrower scope than intended — see below.*

**Status:** incorporated into this repo's `CLAUDE.md`, "Live-link citations"
section, 2026-10-01.

### What this corrects

CLAUDE.md's Live-link citations section already required a real, clickable link
"next to the quoted text, at capture time" for every fact pulled from Slack,
Notion, or Google Drive. In practice, this got applied inconsistently: quoted facts
got proper links, but the capture step's own **live-enumeration listing** — the
"here's what I found when I re-enumerated the Notion parent page / Drive folder"
step that CLAUDE.md's refresh workflow requires at the start of capture — did not.
Google Drive file IDs and a Notion page ID were recorded as bare text in backticks
(e.g. `` `16gr13nLMHj4EH_cLYkX2rLlUDkYScFk_cBwAsPlk8ig` ``) instead of as
hyperlinks, so there was no click-through at that point in the file — even though a
working link (the `viewUrl` / page URL) had already been fetched and was sitting
right there in the tool result.

### The rule (now also in CLAUDE.md, "Live-link citations")

Every entity a refresh names in a capture file — including the live-enumeration
listing of what Notion/Drive returned, not just quoted facts pulled from it
afterward — must be a real hyperlink to its own live URL (`viewUrl` / page URL), not
a bare ID in backticks. If an ID is worth keeping for reference (a Drive file ID, a
Notion page ID), keep it, but alongside the link, not instead of it.

**Example:**

Before (not clickable):
> 1. **FlexPay AU — Weekly Programme Meeting Notes** (Doc, `16gr13nLMHj4EH_cLYkX2rLlUDkYScFk_cBwAsPlk8ig`)

After (clickable, ID kept for reference):
> 1. **[FlexPay AU — Weekly Programme Meeting Notes](https://docs.google.com/document/d/16gr13nLMHj4EH_cLYkX2rLlUDkYScFk_cBwAsPlk8ig/edit)** (Doc, id `16gr13nLMHj4EH_cLYkX2rLlUDkYScFk_cBwAsPlk8ig`)

**Log:** corrected 2026-10-01 in
[wiki/sources/gdrive/2026-10-01.md](../wiki/sources/gdrive/2026-10-01.md) and
[wiki/sources/notion/2026-10-01.md](../wiki/sources/notion/2026-10-01.md) (both
files' "Live enumeration result" sections). Rule added to CLAUDE.md's "Live-link
citations" section the same day.

---

## 3. Anchor Navigation: Heading-as-Slug, Not `<a id>` Tags

*Context: direct follow-on from [§2](#2-live-link-citation-completeness), same
build. The fix above made every entry a real hyperlink, but the per-section anchors
those links pointed at turned out not to work in practice.*

**Status:** incorporated into this repo's `CLAUDE.md`, "Live-link citations"
section, 2026-10-01.

The internal per-section anchors this scheme depends on — so a citation could
deep-link into one specific dated section of a multi-entry capture file, not just
the file as a whole — turned out not to work once tested in the owner's actual
daily tools.

**What was tried first:** a bare `<a id="anchor-id"></a>` placed on its own line
immediately before each dated section's heading, e.g.:

```
<a id="gdoc-20260814-sync"></a>
### 2026-08-14 — Weekly Sync
```

Clicking a citation like `sources/gdrive/2026-10-01.md#gdoc-20260814-sync` from a
decision or person page opened the right *file* in both Obsidian and VS Code, but
always landed at the top of it, not at the tagged section — confirmed by the owner
testing both apps directly.

**Root cause (best understanding — not verified against either app's source):**
`<a id>` fragment-scrolling is native *browser* behavior. It works when a tool
renders the markdown to real HTML in an actual browser tab (e.g. GitHub's web
view), where the browser's own "scroll element with this id into view" logic
handles it. Obsidian and VS Code instead use their own internal link routers, which
almost certainly resolve a link's `#fragment` against a **heading's own
auto-slugified text**, not an arbitrary HTML `id` sitting next to it. Since the
anchor's id (`gdoc-20260814-sync`) never matched the adjacent heading's text
(`2026-08-14 — Weekly Sync`), neither app's router had anything to jump to.

**Fix — confirmed working in both Obsidian and VS Code by direct owner test:** make
the heading *itself* the anchor string, instead of a separate tag next to it. The
human-readable label moves to a bold line directly underneath:

```
### gdoc-20260814-sync
**2026-08-14 — Weekly Sync.**
```

Because every anchor id already used lowercase kebab-case, this is stable under
essentially any heading-slugification algorithm — no fragment string anywhere else
in the wiki needed to change when this was rolled out; only the capture files' own
heading formatting did.

**Rule going forward:** every per-section citation anchor inside a capture file
must be the section's own Markdown heading (`### the-anchor-id`) — never a separate
`<a id="...">` tag next to a differently-worded heading. Put the human-readable
label as a bold line immediately below the heading, not in the heading text itself.

**On tool-agnosticism:** this doesn't reintroduce proprietary syntax — a heading and
a standard `#fragment` link are still plain CommonMark. What changed is which
*rendering-behavior assumption* the mechanism relies on: the original `<a id>`
approach assumed genuine browser-style fragment navigation, which only holds for
tools that render markdown to a real, independently-navigable web page (GitHub's
web view, a static site in a real browser). Obsidian and VS Code instead resolve
links via their own internal routers keyed to heading text — a behavior shared by
most markdown-aware apps with in-app navigation, which makes heading-as-slug the
*broader*-compatibility choice between the two, not a narrower one tuned to two
specific apps.

**Log:** corrected 2026-10-01, same day as §2. Replaced every per-section anchor
across all three capture files
([wiki/sources/slack/2026-10-01.md](../wiki/sources/slack/2026-10-01.md),
[wiki/sources/notion/2026-10-01.md](../wiki/sources/notion/2026-10-01.md),
[wiki/sources/gdrive/2026-10-01.md](../wiki/sources/gdrive/2026-10-01.md), 53
anchors total). No citation links elsewhere in the wiki needed to change, since the
fragment strings themselves were unchanged — only the capture files' own heading
formatting was.

---

## 4. Known Gap: CLAUDE.md's Link-Path Wording vs. Actual Lint Behavior

*Context: noticed while writing §2/§3's fix. Sat correctly-flagged-but-unfixed for
several turns after permission to edit CLAUDE.md had already been established via
unrelated approvals earlier in the same conversation — itself the motivating
example for [§7](#7-track-deferred-items) below.*

CLAUDE.md's "Repository layout" section states that markdown links *between pages
inside* `wiki/` should be written relative to `wiki/` itself, with no `wiki/`
prefix — the same convention used for frontmatter `sources:` citations. But
`bin/lint-wiki` (via `check_link_targets` in
[bin/_wikilib.py](../bin/_wikilib.py)) actually resolves in-body markdown links
relative to *the current file's own directory* (standard file-relative resolution),
while it resolves frontmatter `sources:` citations relative to `wiki/` root. These
are two different resolution rules, but CLAUDE.md's text currently describes only
one. The Version 0 build followed the lint script's actual behavior (file-relative
for body links, root-relative for frontmatter), which is why it passes lint — but a
future session that instead follows CLAUDE.md's literal wording for body links
would write root-relative links that then fail lint.

**Status:** fixed in this repo's `CLAUDE.md`, "Repository layout" section,
2026-10-01 — now states the frontmatter (root-relative) and body-link
(file-relative) rules as two distinct conventions, matching `bin/lint-wiki`'s
actual behavior.

---

## 5. Self-Audit Against a Rule's Full Literal Scope

*Context: surfaced when reflecting on why §2 (live-link completeness) was missed
in the first place, even though CLAUDE.md already had a live-link rule at build
time. This is a process habit, not a wiki-content rule — it's about how a session
should review its own output, and applies well beyond link citations.*

**Status:** incorporated into this repo's `CLAUDE.md`, new "Self-review habits"
section, 2026-10-01.

When a rule is stated with an implicit scope ("record a live link... next to the
quoted text"), it's easy to satisfy the rule for the specific case being handled in
the moment while missing other cases the rule's *intent* clearly covers but its
*literal wording* doesn't explicitly name. §2 is a concrete example: the live-link
rule was written with quoted facts in mind, and got applied faithfully to quoted
facts — but a refresh's live-enumeration listing is arguably "the same kind of
thing" (an entity a reader would want to click through to) without being literally
"quoted text." Nothing forced a check of whether the rule's *purpose* extended
further than its *letter*.

**Habit going forward:** after applying a rule to the task at hand, take one
additional pass asking "does this rule's evident *purpose* cover anything else this
file/page/output contains, even if the rule's literal wording doesn't name it
explicitly?" This is cheap when done immediately after writing something (the
content is already loaded), and expensive when skipped (it surfaces later as a bug
report, or worse, silently never surfaces at all). Applies to any rule with an
implicit scope, not just citation rules — e.g. a frontmatter-completeness rule, a
contradiction-resolution rule, a staleness check.

---

## 6. Flag Unverified Claims About External Tool Behavior

*Context: surfaced from §3 (anchor navigation) — the original `<a id>` design was
presented with more confidence than was warranted, since it depended on an
assumption about Obsidian/VS Code's internal behavior that was never actually
tested before being asserted.*

**Status:** incorporated into this repo's `CLAUDE.md`, new "Self-review habits"
section, 2026-10-01.

Claude Code has no way to open Obsidian or VS Code and observe how they resolve an
internal link click — that's a fact about specific third-party software that can
only be established by testing it in the actual app, not derived from reasoning
about the CommonMark spec or general markdown-rendering principles. §3's root cause
is exactly this: a plausible-sounding, spec-compliant design (`<a id>` anchors)
was asserted as if it would work everywhere, when it was really an *untested
assumption* about two specific apps' internal routing.

**Habit going forward:** when a design choice depends on how a specific external
tool, connector, or renderer behaves — and that behavior hasn't been directly
observed (via a tool call, a test, or the owner confirming it) — say so explicitly
as an assumption, not as a settled fact. Where practical, propose a small,
reversible test before rolling the assumption out broadly (this is what actually
happened once the gap was caught: one section was converted and owner-tested before
all 53 anchors were converted). This doesn't mean hedging everything — most
in-repo, verifiable claims (does a file exist, does a script exit 0, does lint
pass) don't need this treatment, since they can and should just be checked
directly. It's specifically for claims about behavior outside anything Claude Code
can directly inspect or execute.

---

---

## 7. Track Deferred Items

*Context: surfaced from noticing that §4 (the link-path wording gap) sat
correctly-flagged-but-unactioned across several conversation turns — even after
the reason it was originally held back (needing the owner's go-ahead to edit
CLAUDE.md) had already been resolved by unrelated approvals earlier in the same
conversation. Distinct from [§5](#5-self-audit-against-a-rules-full-literal-scope):
that one is about missing a rule's scope in the moment; this one is about a gap
that *was* caught correctly, then dropped over time.*

Correctly deferring something — logging a genuine contradiction as a judgment item
per CLAUDE.md's contradiction-resolution rule, or holding off an instruction-file
edit until the owner explicitly authorizes it — is not the same as resolving it.
Once flagged, a deferred item needs to be actively tracked and re-checked, not just
recorded once and left. Two concrete failure shapes, both real:

1. **The blocking constraint quietly lifts, but nothing re-checks the item.**
   Example: a CLAUDE.md edit is correctly held back pending the owner's
   permission; permission is later granted for a *different* edit; the earlier,
   still-open item doesn't get resurfaced just because the door is now open. This
   is exactly what happened with §4.
2. **New evidence resolves an old open item, but nothing connects the two.**
   Example, in the context of a wiki refresh: a genuine conflict between two
   sources gets logged in `wiki/log.md` as a judgment item for the owner. Two
   refreshes later, unrelated new evidence happens to settle the dispute — but
   the session processes it only for whatever fact it's *about*, and never checks
   whether it also resolves a previously-logged open item. The owner is left
   seeing "unresolved — needs your input" in the log long after it's actually
   been settled.

**Habit going forward:** before declaring any piece of work "done" — a refresh, a
requested fix, a chat response — scan for outstanding flagged/deferred items from
earlier in the same session (or, for a refresh, from `wiki/log.md`'s open judgment
items) and check whether anything just discovered or just permitted resolves one
of them. If so, close the loop explicitly (update the log entry, make the
previously-blocked edit) rather than leaving it to the owner to notice the
connection themselves.

**Status:** incorporated into this repo's `CLAUDE.md`, new "Self-review habits"
section, 2026-10-01 (third bullet).

---

## Log

- **2026-10-01** — File created, consolidating `source-addressability-addendum.md`
  and `live-link-citation-completeness.md` (content folded into §1 and §2–§4
  respectively, unchanged in substance) into this single running file, per the
  owner's request. §5 and §6 added as new entries at the same time.
- **2026-10-01 (follow-up)** — §1–§6 marked with incorporation status against this
  repo's `CLAUDE.md` (all now incorporated except §4, which was also fixed at the
  same time). §7 added, surfaced from noticing §4 itself sat flagged-but-unactioned
  across several turns even after permission to edit CLAUDE.md was already
  established.

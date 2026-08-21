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
8. [Verification Tooling Needs the Same Intent-vs-Letter Audit as Prose Rules](#8-verification-tooling-needs-the-same-intent-vs-letter-audit-as-prose-rules)
9. [Verify Aggregate Claims Against Every Instance They Describe](#9-verify-aggregate-claims-against-every-instance-they-describe)
10. [Mechanical Checks for the Two Sub-Categories of §9 That Are Actually Checkable](#10-mechanical-checks-for-the-two-sub-categories-of-9-that-are-actually-checkable)

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

### Follow-up: a "real hyperlink" isn't real until it's verified to resolve

Fixing the *completeness* gap above (every entity gets a link) surfaced a deeper
one: some of those links were 404s. The owner queried the wiki about milestone M07
and got a Notion citation, `https://app.notion.com/3c261566afbf8168be76e8ab9412d416`,
that didn't resolve — copy-linking the same page directly from Notion's own UI gave
`https://app.notion.com/p/M07-...-3c261566afbf8168be76e8ab9412d416?source=copy_link`
instead.

**Root cause:** two different Notion MCP tools return a `url`-labeled field for the
same page, and they disagree. `notion-fetch` returns
`https://app.notion.com/p/{id}` (confirmed correct — resolves with a plain HTTP
`200`). `notion-query-data-sources` (used to pull the milestone tracker's rows)
returns a bare `https://app.notion.com/{id}`, missing the required `/p/` path
segment — confirmed to `404`. All 10 milestone-row citations in this build came
from the query tool, so all 10 had the same defect, not just M07.

**Important distinction from [§3](#3-anchor-navigation-heading-as-slug-not-a-id-tags):**
that section is about how a *markdown viewer* (Obsidian, VS Code) navigates links
*internal to the wiki* — the URL was never wrong, only the in-app scrolling
behavior varied by tool. This is a different failure entirely: the recorded URL
string itself is malformed and doesn't resolve *anywhere, in any client* — not a
viewer-behavior question at all, just a data-correctness bug from trusting a
tool's field name ("url") without checking the value.

**Rule going forward (extends the rule above, doesn't replace it):** a URL-shaped
field returned by a connector is not automatically a working link. Before recording
it as a citation:
- **Cross-check** — if more than one tool call returns a URL-labeled field for the
  same object, and they disagree, that disagreement is itself the signal something
  is wrong; don't pick one arbitrarily.
- **Verify resolution directly** where practical (an HTTP request, a fetch) — cheap,
  connector-agnostic, and decisive when the target doesn't require auth to view.
- **Where verification is inconclusive** (e.g. an auth-walled platform redirects
  every request, valid URL or not, to the same login page) fall back to asking the
  human to confirm one representative link, rather than guessing.
- **Do this once, at first integration of a source lane** — not on every refresh.
  Once a connector's confirmed-working URL template is known (e.g. Notion:
  `https://app.notion.com/p/{id}`), record that template in the schema file itself,
  the same way Slack's permalink formula is already spelled out explicitly. This
  generalizes beyond Notion: adding a new source platform in a future build (Asana,
  Trello, Jira, ...) shouldn't require the owner to pre-supply the correct URL
  format from memory — Claude can and should discover and verify it the same way,
  using the same two generic techniques, then write the confirmed format down so
  it's never re-derived (and potentially gotten wrong again) later.

**Status:** incorporated into this repo's `CLAUDE.md`, "Live-link citations"
section, 2026-10-01 (Notion bullet corrected; new paragraph on connector URL
verification added).

**Log:** all 10 malformed milestone-row URLs in
[wiki/sources/notion/2026-10-01.md](../wiki/sources/notion/2026-10-01.md) corrected
2026-10-01, each verified via direct HTTP resolution (`200`) before being written.

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

## 8. Verification Tooling Needs the Same Intent-vs-Letter Audit as Prose Rules

*Context: the owner spotted an unlabeled, faded node in Obsidian's graph view,
linked to `flexpay-au`. Traced to `wiki/projects/flexpay-au.md` linking to
`../people/` — the directory — instead of a specific note. `bin/lint-wiki` had
already passed cleanly on this file every time it was run.*

### The gap

This isn't a repeat of [§5](#5-self-audit-against-a-rules-full-literal-scope) —
that one is about a *person* (Claude) applying a rule too narrowly. This is about
a *script*. `bin/lint-wiki`'s `check_link_targets` verified a link target with
`os.path.exists(resolved)`. That's `True` for a directory, not just a file — so a
link to `../people/` passed the check, even though it isn't a link to a note at
all. The check satisfied the *letter* of "does this path exist" while missing the
actual *intent* of the check, which is "does this link resolve to a page a reader
can open." A directory link is broken in every context that matters (it opens
nothing sensible in any viewer, and Obsidian's graph correctly renders it as an
unresolved node) — but the automated safety net didn't catch it, because the net
itself was checking a weaker property than the one it was meant to guarantee.

### Why this is worth its own entry, not folding into §5

§5 is about auditing *Claude's own reasoning* against a rule's full intent in the
moment. This is about auditing *the deterministic tooling* a build relies on to
catch mistakes automatically, after the fact, without depending on a human (or an
LLM) noticing. They call for different responses: §5's fix is a habit ("take one
more pass"); this one's fix is a code change (tighten the check once, and it's
fixed for every future page, forever — no repeated vigilance required). Automated
verification is the higher-leverage fix wherever it's available, precisely because
it doesn't rely on remembering to apply a habit correctly every single time.

### The rule

**When writing or reviewing a structural/lint check, verify it actually enforces
the property it claims to enforce — not a weaker, easier-to-satisfy proxy for it.**
Concretely, for a link-integrity check: verify the target is a *file*
(`os.path.isfile`), not merely that *some path* exists
(`os.path.exists`, which is also true for directories). The general version:
whenever a check's implementation is more permissive than the plain-English
description of what it's supposed to guarantee, that gap is exactly where bugs
will silently pass through undetected — and worse than a missing check, because a
passing check creates false confidence that the property actually holds.

### Where this fits in the blueprint

Any future build's equivalent of `bin/lint-wiki` should get the same scrutiny this
one just did: read each check's implementation next to its own stated purpose (in
its docstring or the surrounding prose) and ask whether the code actually verifies
that purpose, or something weaker that happens to overlap with it most of the
time. Do this once, when the tooling is first written or extended — not only after
a bug like this one surfaces in practice.

**Status:** fixed in this repo's `bin/lint-wiki`, `check_link_targets`,
2026-10-01 — both the body-link check and the frontmatter `sources:` citation
check now use `os.path.isfile()`. Verified by injecting a directory link into
`wiki/projects/flexpay-au.md`, confirming lint now errors on it, then restoring
the file with no diff.

---

## 9. Verify Aggregate Claims Against Every Instance They Describe

*Context: caught while adding inline citations to `flexpay-au.md`'s Risks table
(an unrelated formatting task). The table's intro sentence claimed "all
[4 risks] corroborated by dated Slack posts from the owning function." Re-deriving
each risk's specific evidence for the citation work turned up no Slack message
anywhere in the capture matching R1's raised date — the claim was false for 1 of 4,
and had been sitting in the wiki, unnoticed, since the Version 0 build.*

### Why this is fundamental, not a minor accuracy nit

The owner's own framing on discovering this: *"it is fundamental that the wiki can
be trusted to be correct... as soon as that trust is lost, it ceases to be
valuable."* A wiki whose summary sentences can't be trusted without independently
re-deriving the evidence behind them has lost the entire point of being a
second brain — the owner would have to re-verify everything the wiki tells them
anyway, which is exactly the manual overhead the pattern exists to eliminate. A
broken link is annoying; a false claim stated with full confidence is worse,
because nothing about it *looks* wrong. R1's sentence read identically confident
whether or not it was true.

### Why this got past every existing check

Traced against the blueprint directly (not from memory):

- **Blueprint's Acceptance checklist**, "every durable claim has a usable
  citation" — satisfied. R1 *did* have a citation (the RAID log). This checks that
  a claim has *some* citation, not that a *summary sentence about several claims*
  is true for every one of them. Citation presence and generalization accuracy are
  different properties.
- **Blueprint's Stage 6, contradiction resolution** — not triggered. Nothing about
  this was a contradiction between sources; it was an omission — a generalization
  that was never checked against the specific case that broke it.
- **Blueprint's Stage 7, compile and test** (broken links, orphans, staleness,
  secrets, formatting, regression tests) — entirely structural. The link that
  existed was valid; the defect was semantic, in the prose above the table, not in
  anything a structural check inspects.

Nothing caught it. It surfaced only because an unrelated task happened to require
re-deriving R1's specific evidence. If that task hadn't touched R1, the false
claim could have sat there indefinitely — this is distinct from
[§5](#5-self-audit-against-a-rules-full-literal-scope) (applying someone else's
stated rule too narrowly in the moment) and from
[§8](#8-verification-tooling-needs-the-same-intent-vs-letter-audit-as-prose-rules)
(tooling checking a weaker property than it claims to) — this is a session's own
generated summary text never being checked against the individual facts it
purports to summarize.

### The rule

**Before writing any sentence that generalizes across multiple facts — "all N are
X," "every Y has been Z," "N of M are corroborated" — verify it against each
individual instance the generalization covers, not just the ones that prompted it
or come easily to mind.** A generalization drawn from a few clear examples (R2,
R3, R4 each explicitly said "raising this as a risk") is exactly the shape of
claim that's easiest to over-extend to a case that doesn't actually fit (R1). The
fix isn't "add more lint rules" — this class of bug is semantic, not structural,
and no automated check can verify it without re-deriving the evidence itself.
It's a discipline: re-derive, don't infer, before asserting a pattern holds
universally.

### Where this fits in the blueprint

Add to Stage 7 ("compile and test") or the Acceptance checklist directly: *any
sentence asserting a pattern across multiple durable claims (a count, an "all/every"
statement, a corroboration-rate claim) must be checked against each instance it
covers before publication, not inferred from a representative sample.* This is a
distinct requirement from "every claim has a citation" and should be stated as
such, not assumed to be covered by it.

**Status:** incorporated into this repo's `CLAUDE.md`, "Self-review habits"
section, 2026-10-01 (fourth bullet). The false claim itself corrected the same
day — see `wiki/projects/flexpay-au.md`'s Risks section.

---

## 10. Mechanical Checks for the Two Sub-Categories of §9 That Are Actually Checkable

*Context: direct follow-on from §9. Auditing every citation by hand against
§9's discipline caught real bugs (see §9's log) but also proved unreliable on
its own — a manual re-check of "just the citations I touched" missed a second,
uncorrected instance of the exact same date-conflation bug living on a
different page (`people/maya-chen.md`), only found once this section's tooling
existed and ran wiki-wide. Matches [§8](#8-verification-tooling-needs-the-same-intent-vs-letter-audit-as-prose-rules)'s
own point: tooling beats vigilance because it doesn't get tired on item ten.*

§9 identified three failure sub-categories, not one: fabricated/inaccurate
direct quotes, relative-date language conflated with absolute dates, and
paraphrases overclaiming precision the source doesn't support. Only the first
two are mechanically checkable at all — the third requires understanding what a
paraphrase *implies* versus what the source *establishes*, which is a judgment
call no deterministic script can make. `bin/lint-wiki` now has one check for
each of the first two, both warnings (heuristic, not certain):

- **`check_quote_verbatim`** — extracts quoted text (12+ chars, to filter noise
  like short structural references) from a durable page's body and confirms it's
  a literal substring somewhere in that page's cited sources. Catches a
  fabricated quote with certainty; can't catch an unquoted paraphrase, since
  there's nothing to string-match.
- **`check_relative_date_language`** — flags any Slack source a page cites whose
  content contains relative-date words (day names, "tomorrow," "this/next/last
  week/month") as worth a second look. Can't verify the nearby claim is *wrong*,
  only that it's citing something where getting it wrong is easy — genuinely
  heuristic, expect false positives on messages where the relative language
  isn't actually load-bearing for any claim drawn from them.

Run against this repo's own wiki, these two checks found: one exact duplicate
of the already-fixed M04 bug on a second page nobody had thought to re-check;
one further imprecise paraphrase ("since" implying an unevidenced start date);
two pages missing a citation for a Notion-status claim they were making; and,
resolving a false-negative in the first regression test, a *third* instance of
the D4 misquote living inside a `sources/**` capture file's own analytical
commentary — see the "Post-build corrections" entry in `wiki/log.md` for the
full list and how that last one was handled given `sources/**`'s normal
immutability.

**Status:** both checks added to this repo's `bin/lint-wiki`, 2026-10-01.
Regression-tested: a directly-injected fabricated quote and a reintroduced
directory-link-style bug (see §8) both now produce the expected lint failure;
restoring the file afterward produces a clean diff. No CLAUDE.md change — same
reasoning as §8, this is tooling closing a gap the existing rule already
described, not a new prose rule.

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
- **2026-10-01 (follow-up 2)** — New subsection added under §2, after the owner
  caught a Notion citation link (M07) that 404'd. Root cause: two Notion MCP tools
  return disagreeing `url` fields for the same page, and the wrong one was trusted
  for all 10 milestone-row citations. Distinguished explicitly from §3 (that's
  about viewer navigation behavior for links internal to the wiki; this is about
  external URL correctness, unrelated to which app reads the wiki). All 10 URLs in
  `wiki/sources/notion/2026-10-01.md` corrected and HTTP-verified. CLAUDE.md's
  Notion bullet and a new connector-URL-verification paragraph added the same day.
- **2026-10-01 (follow-up 3)** — §8 added, after the owner spotted an unresolved
  node in Obsidian's graph view traced to a directory link (`../people/`) in
  `wiki/projects/flexpay-au.md` that `bin/lint-wiki` had never flagged.
  `check_link_targets` tightened from `os.path.exists` to `os.path.isfile` for
  both body links and frontmatter citations. No CLAUDE.md change — this was a
  tooling gap, not a prose-rule gap.
- **2026-10-01 (follow-up 4)** — §9 added, after discovering `flexpay-au.md`'s
  Risks table falsely claimed all 4 risks were Slack-corroborated when R1 had no
  matching Slack message at all. Traced against the blueprint directly: the
  Acceptance checklist's "every claim has a citation" was satisfied by R1 anyway,
  since it never checked whether a *summary sentence about several claims* held
  for each one. Rule added to CLAUDE.md's "Self-review habits" (fourth bullet);
  the false claim corrected in the same commit as the Risks table citation work.
- **2026-10-01 (follow-up 5)** — §10 added: built `bin/lint-wiki` checks for the
  two mechanically-checkable sub-categories of §9 (verbatim quotes, relative-date
  language). Running them found a second, uncorrected copy of the M04 bug on
  `people/maya-chen.md`, a similar imprecise paraphrase on the same page, two
  pages missing a Notion citation, and a third copy of the D4 misquote inside a
  `sources/**` file's own commentary. All corrected; the `sources/**` edit is a
  scoped, explicitly-logged exception to normal immutability (see
  `wiki/log.md`'s "Post-build corrections" entry), authorized for this
  active-build-phase exercise specifically, not a general practice.

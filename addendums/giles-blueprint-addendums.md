# Giles' Blueprint Addendums

*This section (the file intro) is itself dummy-program/maintenance-specific —
exclude from merge, same as every section's "Build notes" and the file-level
`## Log`.*

Addendum to [ai-second-brain-blueprint.md](../ai-second-brain-blueprint.md) and to
[CLAUDE.md](../CLAUDE.md). **Maintained by the owner (Giles Davis)** — Claude Code
should read this file before a refresh, alongside CLAUDE.md, but should not write
to it (see CLAUDE.md's "What the agent may edit"). Where an entry here conflicts
with CLAUDE.md or the blueprint, this file wins — it exists precisely to record
corrections made after those files were last edited.

Claude Code has been the tool used to build and iterate on this wiki throughout,
and `CLAUDE.md` is accordingly the canonical instruction file named throughout
this addendum. The blueprint itself is **not** Claude-specific, though — it names
`AGENTS.md` *or equivalent* as the canonical instruction file, precisely so a
different agent/tool can be substituted. A build using a different tool would
read every "CLAUDE.md" reference below as "this build's equivalent canonical
instruction file."

This is a single, running file: every tweak/gap discovered while building or
running a wiki off the blueprint gets its own numbered section below. Sections
are grouped thematically (source/citation mechanics, then self-review and
verification habits), not in original discovery order — the order they were
actually found in is preserved in the `## Log` at the bottom instead.

**Each section splits into two parts.** The main body — rule, rationale, "Where
this fits in the blueprint," and any illustrative example — is written to stand
alone with zero knowledge of this specific build. This is the part meant to
actually merge into a v2 blueprint: usable for a different programme, or by
someone with no context of this exercise at all. A trailing **"Build notes
(dummy-program-specific — exclude from merge)"** subsection, set off by its own
heading and a horizontal rule, carries the concrete FlexPay AU example that
surfaced the gap and this repo's own incorporation status — useful for tracking
this build's progress, not for merging. The file-level `## Log` at the bottom is
entirely build tracking too, for the same reason.

## Contents

**Source & citation mechanics**

1. [Source Addressability](#1-source-addressability)
2. [Live-Link Citation Completeness](#2-live-link-citation-completeness)
3. [Anchor Navigation: Heading-as-Slug, Not `<a id>` Tags](#3-anchor-navigation-heading-as-slug-not-a-id-tags)
4. [Label Which Lane an Inline Citation Points To](#4-label-which-lane-an-inline-citation-points-to)
5. [Render Cited URLs as Hyperlinks, Not Plain Text](#5-render-cited-urls-as-hyperlinks-not-plain-text)

**Self-review & verification habits**

6. [Self-Audit Against a Rule's Full Literal Scope](#6-self-audit-against-a-rules-full-literal-scope)
7. [Flag Unverified Claims About External Tool Behavior](#7-flag-unverified-claims-about-external-tool-behavior)
8. [Track Deferred Items](#8-track-deferred-items)
9. [Verification Tooling Needs the Same Intent-vs-Letter Audit as Prose Rules](#9-verification-tooling-needs-the-same-intent-vs-letter-audit-as-prose-rules)
10. [Schema-Doc Wording Must Match What Its Own Lint Tooling Enforces](#10-schema-doc-wording-must-match-what-its-own-lint-tooling-enforces)
11. [Verify Aggregate Claims Against Every Instance They Describe](#11-verify-aggregate-claims-against-every-instance-they-describe)
12. [Mechanical Checks for the Two Sub-Categories of §11 That Are Actually Checkable](#12-mechanical-checks-for-the-two-sub-categories-of-11-that-are-actually-checkable)

**Appended (not yet relocated to its thematic group — see its own placement note)**

13. [Frontmatter Must Be a Complete Source Manifest, Not a Subset](#13-frontmatter-must-be-a-complete-source-manifest-not-a-subset)
14. [Reference a Non-Durable Item by Its Smallest Containing Heading](#14-reference-a-non-durable-item-by-its-smallest-containing-heading)

---

## 1. Source Addressability

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
  — that section is this same requirement applied to a refresh's *output*, not
  just the schema file. Both are needed; neither replaces the other.)
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

### Why this matters

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

Both problems showed up in practice: an instruction file that named channels, a
database, and a folder by name only, with zero recorded IDs. Fixing it after the
fact meant re-deriving identifiers that had already been resolved once during the
original build and simply never written down — wasted work that a stable ID,
recorded once, would have avoided entirely.

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

### Build notes (dummy-program-specific — exclude from merge)

Discovered while building the FlexPay AU wiki: the instruction file named Slack
channels, a Notion database, and a Drive folder by name only, with zero recorded
IDs, before this rule was applied.

**Status:** already reflected in this repo's `CLAUDE.md`, "Source scope" section
(resolvable IDs recorded per lane, live re-enumeration instruction, illustrative-
not-exhaustive framing). No further CLAUDE.md change needed here — kept above for
the blueprint-level "why" and template.

---

## 2. Live-Link Citation Completeness

### The rule

Every entity a refresh names in a capture file — including the live-enumeration
listing of what a container search returned, not just quoted facts pulled from it
afterward — must be a real hyperlink to its own live URL, not a bare ID in
backticks. If an ID is worth keeping for reference, keep it, but alongside the
link, not instead of it.

A URL-shaped field returned by a connector is not automatically a working link,
either. Before recording it as a citation:
- **Cross-check** — if more than one tool call returns a URL-labeled field for
  the same object, and they disagree, that disagreement is itself the signal
  something is wrong; don't pick one arbitrarily.
- **Verify resolution directly** where practical (an HTTP request, a fetch) —
  cheap, connector-agnostic, and decisive when the target doesn't require auth to
  view.
- **Where verification is inconclusive** (e.g. an auth-walled platform redirects
  every request, valid URL or not, to the same login page) fall back to asking
  the human to confirm one representative link, rather than guessing.
- **Do this once, at first integration of a source lane** — not on every
  refresh. Once a connector's confirmed-working URL template is known, record
  that template in the schema file itself, the same way a chat platform's
  permalink formula would be spelled out explicitly. This generalizes to any new
  source platform added later — the owner shouldn't need to pre-supply the
  correct URL format from memory; verify and record it once, using the
  techniques above.

### Why this matters

A "record a live link next to the quoted text" rule is easy to satisfy for
individual cited facts while missing a different part of the same file: the
capture step's own live-enumeration listing — "here's what was found when a
container was searched" — needs the identical treatment, since it's also
something a reader would want to click through to verify. But it isn't
literally "quoted text," so a narrow reading skips it. IDs end up recorded as
bare backtick text instead of hyperlinks, even when a working link was already
available in the same tool result.

Separately, even a link that *is* present can still be wrong: different tool
calls against the same connector can return disagreeing `url`-labeled fields for
the same object — one correct, one malformed — and trusting whichever one
happens to be used first produces citations that look identical in the markdown
but silently fail to click through.

### Example

Before (not clickable):
> 1. **Some Document Name** (Doc, `abc123def456...`)

After (clickable, ID kept for reference):
> 1. **[Some Document Name](https://.../abc123def456.../edit)** (Doc, id `abc123def456...`)

### Where this fits in the blueprint

Add to the schema/instruction file's citation rule: it must explicitly cover a
refresh's live-enumeration listing, not only facts quoted from a source
afterward. And add: *before trusting any URL-shaped field a connector returns,
verify it actually resolves — a field named "url" isn't proof it's correct, and
different tool calls against the same connector can disagree.*

---

### Build notes (dummy-program-specific — exclude from merge)

Discovered during the FlexPay AU wiki's Version 0 build. Google Drive file IDs
and a Notion page ID were recorded as bare text in backticks in the "Live
enumeration result" sections of the capture files, instead of as hyperlinks,
even though a working link had already been fetched. Corrected in
`wiki/sources/gdrive/2026-10-01.md` and `wiki/sources/notion/2026-10-01.md`.

Follow-up: the owner queried the wiki about a specific milestone and got a
Notion citation that 404'd — copy-linking the same page directly from Notion's
own UI gave a working URL in a different format. Root cause traced to two
Notion MCP tools (`notion-fetch` vs. `notion-query-data-sources`) returning
disagreeing `url` fields for the same page; `notion-fetch`'s
`https://app.notion.com/p/{id}` format is confirmed correct, the query tool's
bare `https://app.notion.com/{id}` (no `/p/` segment) 404s. All 10
milestone-row citations in this build had come from the query tool, so all 10
shared the defect, not just the one that was noticed.

**Important distinction from [§3](#3-anchor-navigation-heading-as-slug-not-a-id-tags):**
that section is about how a *markdown viewer* (Obsidian, VS Code) navigates
links internal to the wiki — the URL was never wrong there, only the in-app
scrolling behavior varied by tool. This was a different failure: the recorded
URL string itself was malformed and didn't resolve anywhere, in any client — a
data-correctness bug, not a viewer-behavior question.

**Status:** incorporated into this repo's `CLAUDE.md`, "Live-link citations"
section, 2026-10-01 (both the original completeness fix and the follow-up
verification rule). All 10 malformed milestone-row URLs in
`wiki/sources/notion/2026-10-01.md` corrected the same day, each verified via
direct HTTP resolution (`200`) before being written.

---

## 3. Anchor Navigation: Heading-as-Slug, Not `<a id>` Tags

### The rule

Every per-section citation anchor inside a capture file must be the section's
own Markdown heading (`### the-anchor-id`) — never a separate `<a id="...">`
tag next to a differently-worded heading. Put the human-readable label as a
bold line immediately below the heading, not in the heading text itself. Use
lowercase kebab-case for the anchor id — that form survives essentially any
heading-slugification algorithm unchanged, so it stays stable across
renderers.

### Why this matters

The internal per-section anchors a multi-entry capture file depends on — so a
citation can deep-link into one specific dated section, not just the file as a
whole — need a mechanism that actually works in the tools the owner reads the
wiki in day to day, not just one that's spec-compliant in principle.

**What doesn't work:** a bare `<a id="anchor-id"></a>` placed on its own line
immediately before a section's heading:

```
<a id="some-anchor-id"></a>
### 2026-08-14 — Some Meeting
```

Clicking a citation to that anchor opens the right *file* in Obsidian and VS
Code, but lands at the top of it, not at the tagged section.

**Root cause:** `<a id>` fragment-scrolling is native *browser* behavior. It
works when a tool renders markdown to real HTML in an actual browser tab (e.g.
GitHub's web view), where the browser's own "scroll element with this id into
view" logic handles it. Obsidian and VS Code instead use their own internal
link routers, which resolve a link's `#fragment` against a **heading's own
auto-slugified text**, not an arbitrary HTML `id` sitting next to it. If the
anchor id never matches the adjacent heading's actual text, neither app's
router has anything to jump to.

**Fix:** make the heading *itself* the anchor string, instead of a separate tag
next to it. The human-readable label moves to a bold line directly underneath:

```
### some-anchor-id
**2026-08-14 — Some Meeting.**
```

Because the anchor id is already lowercase kebab-case, this is stable under
essentially any heading-slugification algorithm — no fragment string elsewhere
in the wiki needs to change when this is rolled out; only the capture files'
own heading formatting does.

### On tool-agnosticism

This doesn't reintroduce proprietary syntax — a heading and a standard
`#fragment` link are still plain CommonMark. What changes is which
*rendering-behavior assumption* the mechanism relies on: the `<a id>` approach
assumes genuine browser-style fragment navigation, which only holds for tools
that render markdown to a real, independently-navigable web page. Obsidian and
VS Code instead resolve links via their own internal routers keyed to heading
text — a behavior shared by most markdown-aware apps with in-app navigation,
which makes heading-as-slug the *broader*-compatibility choice, not a narrower
one tuned to two specific apps.

### Where this fits in the blueprint

Add to the schema/instruction file's citation-anchor guidance: *per-section
citation anchors must be the section's own heading, in lowercase kebab-case,
never a separate `<a id>` tag next to a differently-worded heading* — and note
this was only discovered by directly testing in the owner's actual tools, not
by reasoning about the CommonMark spec alone (see [§7](#7-flag-unverified-claims-about-external-tool-behavior)).

---

### Build notes (dummy-program-specific — exclude from merge)

The literal example that surfaced this: a citation to
`sources/gdrive/2026-10-01.md#gdoc-20260814-sync` opened the right file in
both Obsidian and VS Code but always landed at the top, not at the tagged
2026-08-14 meeting section — confirmed by the owner testing both apps
directly, then confirmed fixed the same way.

**Status:** incorporated into this repo's `CLAUDE.md`, "Live-link citations"
section, 2026-10-01. Rolled out across all three capture files
(`wiki/sources/slack/2026-10-01.md`, `wiki/sources/notion/2026-10-01.md`,
`wiki/sources/gdrive/2026-10-01.md`, 53 anchors total) the same day. No
citation links elsewhere in the wiki needed to change, since the fragment
strings themselves were unchanged — only the capture files' own heading
formatting was.

---

## 4. Label Which Lane an Inline Citation Points To

### The rule

**A citation's visible link text must make clear which lane it points to** —
Slack, chat tool, ticketing system, shared drive, whatever the source actually
is — not just that it's a link at all. A citation that resolves correctly but
reads as `[2026-08-14](url)` or `([finance-team](url))` technically satisfies
"record a citation" while still leaving the reader — human or a future session
reusing the citation — unable to tell what they're about to click through to
without hovering or clicking first. Concretely: `[Slack 2026-08-14](url)` or
`([Notion](url))`, not a bare date or a bare channel name. Applies anywhere a
citation is inlined into prose or a table cell — capture files and durable
pages alike, not only whichever page happens to be getting written that day.

### Why this matters

A citation rule that only requires a link to *exist and resolve* doesn't also
guarantee the link is self-describing. Those are different properties, and a
wiki can satisfy the first while failing the second silently — nothing about a
working-but-unlabeled link looks broken. Fixed once, in one place, when a human
happens to notice it, this kind of gap doesn't propagate to every other page
that has the same unlabeled pattern; it needs to be a stated rule from the
start, not a one-off correction.

### Where this fits in the blueprint

Add to the schema/instruction file's citation-format guidance (wherever
live-link citation rules are defined): *citation link text must self-identify
its source lane.* Pair with an explicit example of the required format and a
counter-example of the failure (bare date, bare channel/room name) so it's
unambiguous at build time, not something a session has to infer.

### Illustrative example (generic, not tied to any specific programme)

A decision page cites four messages as corroboration, using each channel's
name as the link text: `(#finance)`, `(#legal)`. Nothing in the link text
itself says these came from a chat tool at all — a reader has to infer that
from a sentence elsewhere on the page ("four people posted in four different
channels"), not from the citation itself.

---

### Build notes (dummy-program-specific — exclude from merge)

Raised when a mocked-up Milestones table cell — `~40% as of
[2026-08-14](url)` — didn't make clear that link was Slack, while a Notion
link right next to it was self-labeled. Fixed in the Milestones/Risks tables
at the time, but not written down as a rule and not applied retroactively — a
later audit of the Decisions pages found `d2-rules-based-credit-model.md`
still has four inline citations (`([programme](...))`, `([compliance](...))`,
`([finance](...))`, `([legal](...))`) with the same unlabeled pattern.

**Status:** rule incorporated into this repo's `CLAUDE.md`, "Live-link
citations" section, 2026-10-01. `d2-rules-based-credit-model.md`'s four links
not yet retroactively fixed.

---

## 5. Render Cited URLs as Hyperlinks, Not Plain Text

### The rule

**Any cited URL, in chat or in wiki content, is rendered as an actual
markdown hyperlink — `[label](url)` — never as bare/plain text.** This is a
low bar and an easy one to satisfy once stated; the gap tends to be purely
that it was never stated, and the narrowest reading of a "include the live
link" rule technically permits the failure.

### Why this matters

A citation rule that says to "include the live link along with the fact"
without also saying the link has to actually *be* a link is satisfied, in its
narrowest possible reading, by a URL presented as plain text — the reader
still has to copy-paste it themselves, which is exactly the friction the whole
live-link-citation concept exists to remove.

### Where this fits in the blueprint

Add explicitly to the citation rule: a cited URL is always rendered as a
markdown hyperlink, never as bare text, in both wiki content and in a chat
response synthesizing from it.

---

### Build notes (dummy-program-specific — exclude from merge)

The owner asked for a URL and got it back as bare text — technically correct,
functionally useless for the stated goal of being able to click straight from
a fact to its origin.

**Status:** incorporated into this repo's `CLAUDE.md`, "Live-link citations"
section, 2026-10-01.

---

## 6. Self-Audit Against a Rule's Full Literal Scope

### The rule

**Habit:** after applying a rule to the task at hand, take one additional pass
asking "does this rule's evident *purpose* cover anything else this
file/page/output also contains, even if the rule's literal wording doesn't
name it explicitly?" Applies to any rule with an implicit scope — citation
completeness, frontmatter requirements, contradiction handling, staleness
checks.

### Why this matters

When a rule is stated with an implicit scope (e.g. "record a live link... next
to the quoted text"), it's easy to satisfy the rule for the specific case being
handled in the moment while missing other cases the rule's *intent* clearly
covers but its *literal wording* doesn't explicitly name. This is cheap to
catch immediately after writing something (the content is already loaded) and
expensive to catch later — it surfaces as a bug report, or worse, never
surfaces at all.

### Where this fits in the blueprint

Add as a stated review habit alongside the schema's citation/contradiction
rules: applying a rule correctly to the immediate case isn't the same as
checking whether its purpose extends further than its literal wording within
the same output.

---

### Build notes (dummy-program-specific — exclude from merge)

Surfaced when reflecting on why [§2](#2-live-link-citation-completeness) (live-link
completeness) was missed in the first place, even though CLAUDE.md already had
a live-link rule at build time: the rule was written with quoted facts in
mind, and got applied faithfully to quoted facts — but a refresh's
live-enumeration listing is arguably "the same kind of thing" without being
literally "quoted text." Nothing forced a check of whether the rule's purpose
extended further than its letter.

**Status:** incorporated into this repo's `CLAUDE.md`, "Self-review habits"
section, 2026-10-01.

---

## 7. Flag Unverified Claims About External Tool Behavior

### The rule

**Habit:** when a design choice depends on how a specific external tool,
connector, or renderer behaves — and that behavior hasn't been directly
observed (via a tool call, a test, or the owner confirming it) — say so
explicitly as an assumption, not as a settled fact. Where practical, propose a
small, reversible test before rolling the assumption out broadly. This doesn't
mean hedging everything — anything verifiable in-repo (does a file exist, does
a script exit 0, does lint pass) should just be checked directly, not hedged.

### Why this matters

An AI agent has no way to open a specific third-party app and observe how it
behaves — that's a fact about specific software that can only be established
by testing it directly or having a human confirm it, not derived from
reasoning about a spec or general principles. A plausible-sounding,
spec-compliant design can still be wrong if it rests on an untested assumption
about how a particular tool's internals actually work.

### Where this fits in the blueprint

Add as a stated review habit: before asserting how a specific external tool
will render, navigate, or resolve something, distinguish "verified by testing"
from "inferred from general principles" explicitly, and propose the cheapest
test that would confirm or disconfirm the assumption before committing to it
broadly.

---

### Build notes (dummy-program-specific — exclude from merge)

Surfaced from [§3](#3-anchor-navigation-heading-as-slug-not-a-id-tags) (anchor
navigation) — the original `<a id>` design was presented with more confidence
than was warranted, since it depended on an untested assumption about
Obsidian/VS Code's internal link-routing behavior. What actually happened once
the gap was caught: one section was converted and owner-tested before all 53
anchors were converted, rather than rolling out the fix blind.

**Status:** incorporated into this repo's `CLAUDE.md`, "Self-review habits"
section, 2026-10-01.

---

## 8. Track Deferred Items

### The rule

**Habit:** before declaring any piece of work "done" — a refresh, a requested
fix, a chat response — scan for outstanding flagged/deferred items from
earlier in the same session (or, for a refresh, from the log's open judgment
items) and check whether anything just discovered or just permitted resolves
one of them. If so, close the loop explicitly (update the log entry, make the
previously-blocked edit) rather than leaving it to the owner to notice the
connection themselves.

### Why this matters

Correctly deferring something — logging a genuine contradiction as a judgment
item per the contradiction-resolution rule, or holding off an instruction-file
edit until the owner explicitly authorizes it — is not the same as resolving
it. Once flagged, a deferred item needs to be actively tracked and re-checked,
not just recorded once and left. Two concrete failure shapes, both real:

1. **The blocking constraint quietly lifts, but nothing re-checks the item.**
   An edit is correctly held back pending the owner's permission; permission
   is later granted for a *different* edit; the earlier, still-open item
   doesn't get resurfaced just because the door is now open.
2. **New evidence resolves an old open item, but nothing connects the two.**
   A genuine conflict between two sources gets logged as a judgment item for
   the owner. A later refresh's unrelated new evidence happens to settle the
   dispute — but the session processes it only for whatever fact it's
   *about*, and never checks whether it also resolves a previously-logged
   open item. The owner is left seeing "unresolved — needs your input" long
   after it's actually been settled.

### Where this fits in the blueprint

Add as a stated review habit, paired with the contradiction-resolution
protocol: a judgment item logged as unresolved needs periodic re-checking
against new evidence and against newly-granted permissions, not just a
one-time log entry.

---

### Build notes (dummy-program-specific — exclude from merge)

Surfaced from noticing that [§10](#10-schema-doc-wording-must-match-what-its-own-lint-tooling-enforces)
(the link-path wording gap) sat correctly-flagged-but-unactioned across
several conversation turns — even after the reason it was originally held
back (needing the owner's go-ahead to edit CLAUDE.md) had already been
resolved by unrelated approvals earlier in the same conversation.

**Status:** incorporated into this repo's `CLAUDE.md`, "Self-review habits"
section, 2026-10-01 (third bullet).

---

## 9. Verification Tooling Needs the Same Intent-vs-Letter Audit as Prose Rules

### The rule

**When writing or reviewing a structural/lint check, verify it actually
enforces the property it claims to enforce — not a weaker, easier-to-satisfy
proxy for it.** Concretely, for a link-integrity check: verify the target is a
*file* (`os.path.isfile`), not merely that *some path* exists
(`os.path.exists`, which is also true for directories). The general version:
whenever a check's implementation is more permissive than the plain-English
description of what it's supposed to guarantee, that gap is exactly where bugs
will silently pass through undetected — and worse than a missing check,
because a passing check creates false confidence that the property actually
holds.

### Why this matters

A structural check can satisfy the *letter* of its own stated purpose ("does
this path exist") while missing the actual *intent* ("does this link resolve
to a page a reader can open"). A broken result that technically passes the
check is worse than an obviously-missing check, because nothing signals that
anything needs attention — the automated safety net looks like it's working.

### Why this is a distinct entry, not folded into a person's own self-review habit

Auditing *a person's own reasoning* against a rule's full intent in the moment
(see [§6](#6-self-audit-against-a-rules-full-literal-scope)) and auditing *the
deterministic tooling* a build relies on to catch mistakes automatically call
for different responses: the former's fix is a habit ("take one more pass");
the latter's fix is a code change — tighten the check once, and it's fixed for
every future case, forever, with no repeated vigilance required. Automated
verification is the higher-leverage fix wherever it's available, precisely
because it doesn't rely on remembering to apply a habit correctly every single
time.

### Where this fits in the blueprint

Any lint/verification tooling a build relies on should get this scrutiny when
first written or extended, not only after a bug surfaces in practice: read
each check's implementation next to its own stated purpose (docstring or
surrounding prose) and ask whether the code actually verifies that purpose, or
something weaker that happens to overlap with it most of the time.

---

### Build notes (dummy-program-specific — exclude from merge)

The owner spotted an unlabeled, faded node in Obsidian's graph view, linked to
the project page. Traced to a durable page linking to `../people/` — the
directory — instead of a specific note. `bin/lint-wiki` had already passed
cleanly on this file every time it was run, because `check_link_targets`
verified a link target with `os.path.exists(resolved)`, which is `True` for a
directory, not just a file.

**Status:** fixed in this repo's `bin/lint-wiki`, `check_link_targets`,
2026-10-01 — both the body-link check and the frontmatter `sources:` citation
check now use `os.path.isfile()`. Verified by injecting a directory link into
a durable page, confirming lint now errors on it, then restoring the file with
no diff.

---

## 10. Schema-Doc Wording Must Match What Its Own Lint Tooling Enforces

### The rule

When a schema/instruction file states a path or format convention, and that
convention is also enforced by lint tooling, the two must agree — and if the
tooling implements two different rules for two different cases (e.g.
frontmatter citations resolved one way, body links resolved another), the
prose must describe both distinctly, not collapse them into one blended
description.

### Why this matters

A schema file's prose is what a human or a future session reads and follows
when writing new content; the lint tooling is what actually enforces
correctness. If they drift apart — the prose says one convention, the code
checks a different one — content that follows the prose fails lint, and
content that passes lint doesn't necessarily match the documented convention.
A build that happens to follow the tooling's actual behavior (because whoever
built it inferred it from testing, not from re-reading the prose) still passes
lint while silently contradicting its own documentation, which then misleads
the next person or session that trusts the written rule instead of the code.

### Where this fits in the blueprint

Whenever a schema file states a structural convention that lint tooling also
checks, verify the two agree by testing, not by assuming the prose was written
correctly — the same intent-vs-letter audit [§9](#9-verification-tooling-needs-the-same-intent-vs-letter-audit-as-prose-rules)
recommends for tooling applies symmetrically to the prose that describes it.

---

### Build notes (dummy-program-specific — exclude from merge)

CLAUDE.md's "Repository layout" section stated that markdown links *between
pages inside* `wiki/` should be written relative to `wiki/` itself, with no
`wiki/` prefix — the same convention used for frontmatter `sources:`
citations. But `bin/lint-wiki` (via `check_link_targets` in
`bin/_wikilib.py`) actually resolves in-body markdown links relative to *the
current file's own directory* (standard file-relative resolution), while it
resolves frontmatter `sources:` citations relative to `wiki/` root — two
different resolution rules, but CLAUDE.md's text described only one. The
Version 0 build followed the lint script's actual behavior, which is why it
passed lint — but a future session following CLAUDE.md's literal wording for
body links would write root-relative links that then fail.

**Status:** fixed in this repo's `CLAUDE.md`, "Repository layout" section,
2026-10-01 — now states the frontmatter (root-relative) and body-link
(file-relative) rules as two distinct conventions, matching `bin/lint-wiki`'s
actual behavior.

---

## 11. Verify Aggregate Claims Against Every Instance They Describe

### The rule

**Before writing any sentence that generalizes across multiple facts — "all N
are X," "every Y has been Z," "N of M are corroborated" — verify it against
each individual instance the generalization covers, not just the ones that
prompted it or come easily to mind.** A generalization drawn from a few clear
examples is exactly the shape of claim that's easiest to over-extend to a case
that doesn't actually fit. This isn't solvable by adding more lint rules —
this class of bug is semantic, not structural, and no automated check can
verify it without re-deriving the evidence itself. It's a discipline:
re-derive, don't infer, before asserting a pattern holds universally.

### Why this is fundamental, not a minor accuracy nit

A wiki whose summary sentences can't be trusted without independently
re-deriving the evidence behind them has lost the entire point of being a
second brain — the reader would have to re-verify everything the wiki tells
them anyway, which is exactly the manual overhead the pattern exists to
eliminate. A confidently false claim is worse than a broken link, not just as
bad — a broken link fails *loud* (click it, nothing happens, distrust it
immediately); a false generalization fails *silent*, reading identically
confident whether or not it's true, giving the reader no signal to
double-check at all.

### Why this got past every existing check

Traced against the blueprint directly:

- **The blueprint's Acceptance checklist**, "every durable claim has a usable
  citation" — satisfiable even by a false generalization, because a claim can
  individually have a citation while a *summary sentence about several
  claims* is untrue for one of them. Citation presence and generalization
  accuracy are different properties.
- **The blueprint's Stage 6, contradiction resolution** — not triggered by
  this class of bug. Nothing about it is a contradiction between sources;
  it's an omission — a generalization that was never checked against the
  specific case that breaks it.
- **The blueprint's Stage 7, compile and test** (broken links, orphans,
  staleness, secrets, formatting, regression tests) — entirely structural. A
  link that exists and resolves is valid by every structural check; the
  defect here is semantic, in the prose making the claim, not in anything a
  structural check inspects.

Distinct from [§6](#6-self-audit-against-a-rules-full-literal-scope) (applying
someone else's stated rule too narrowly in the moment) and from
[§9](#9-verification-tooling-needs-the-same-intent-vs-letter-audit-as-prose-rules)
(tooling checking a weaker property than it claims to) — this is a session's
own generated summary text never being checked against the individual facts
it purports to summarize.

### Where this fits in the blueprint

Add to Stage 7 ("compile and test") or the Acceptance checklist directly: *any
sentence asserting a pattern across multiple durable claims (a count, an
"all/every" statement, a corroboration-rate claim) must be checked against
each instance it covers before publication, not inferred from a
representative sample.* This is a distinct requirement from "every claim has
a citation" and should be stated as such, not assumed to be covered by it.

---

### Build notes (dummy-program-specific — exclude from merge)

Caught while adding inline citations to a Risks table (an unrelated formatting
task). The table's intro sentence claimed all 4 risks were corroborated by
dated Slack posts from their owning function. Re-deriving each risk's specific
evidence for the citation work turned up no Slack message anywhere in the
capture matching one risk's raised date — the claim was false for 1 of 4, and
had been sitting in the wiki, unnoticed, since the Version 0 build. The three
that *were* corroborated each explicitly said "raising this as a risk" in
Slack; the one that wasn't had simply never been checked individually.

The owner's own framing on discovering this: *"it is fundamental that the
wiki can be trusted to be correct... as soon as that trust is lost, it ceases
to be valuable."*

**Status:** incorporated into this repo's `CLAUDE.md`, "Self-review habits"
section, 2026-10-01 (fourth bullet). The false claim itself corrected the
same day — see `wiki/projects/flexpay-au.md`'s Risks section.

---

## 12. Mechanical Checks for the Two Sub-Categories of §11 That Are Actually Checkable

### The rule

§11 identified three failure sub-categories, not one: fabricated/inaccurate
direct quotes, relative-date language conflated with absolute dates, and
paraphrases overclaiming precision the source doesn't support. Only the first
two are mechanically checkable at all — the third requires understanding what
a paraphrase *implies* versus what the source *establishes*, which is a
judgment call no deterministic script can make. Build lint checks for the
first two rather than relying on §11's discipline alone:

- **A verbatim-quote check** — extracts quoted text from a durable page's
  body and confirms it's a literal substring somewhere in that page's cited
  sources. Catches a fabricated quote with certainty; can't catch an unquoted
  paraphrase, since there's nothing to string-match.
- **A relative-date-language check** — flags any source a page cites whose
  content contains relative-date words (day names, "tomorrow,"
  "this/next/last week/month") as worth a second look. Can't verify the
  nearby claim is *wrong*, only that it's citing something where getting it
  wrong is easy — genuinely heuristic, expect false positives on messages
  where the relative language isn't actually load-bearing for any claim drawn
  from them.

### Why this matters

Auditing every citation by hand against §11's discipline catches real bugs,
but proves unreliable on its own — a manual re-check of "just the citations
touched in this session" can miss an identical, uncorrected instance of the
same bug living on a completely different page nobody thought to re-examine,
found only once wiki-wide tooling exists and actually runs against every
page. Matches [§9](#9-verification-tooling-needs-the-same-intent-vs-letter-audit-as-prose-rules)'s
own point: tooling beats vigilance because it doesn't get tired on the tenth
item the way a person re-checking by hand does.

### Where this fits in the blueprint

Add both checks to the build's lint/verification tooling (Stage 7-equivalent),
as warnings rather than hard errors — both are heuristic, not certain, and
will produce some false positives that are cheap to review and dismiss. Note
explicitly in the tooling's own documentation that a third failure category
(paraphrase overclaiming precision) exists and is *not* covered by either
check — so it doesn't read as solved once the two mechanical checks are in
place.

---

### Build notes (dummy-program-specific — exclude from merge)

Run against this repo's own wiki, these two checks found: one exact duplicate
of an already-fixed date-conflation bug on a second page nobody had thought to
re-check; one further imprecise paraphrase ("since" implying an unevidenced
start date); two pages missing a citation for a Notion-status claim they were
making; and, resolving a false-negative in the first regression test, a
*third* instance of a misquote living inside a `sources/**` capture file's own
analytical commentary — see the "Post-build corrections" entry in
`wiki/log.md` for the full list and how that last one was handled given
`sources/**`'s normal immutability.

**Status:** both checks added to this repo's `bin/lint-wiki`, 2026-10-01.
Regression-tested: a directly-injected fabricated quote and a reintroduced
directory-link-style bug (see §9) both now produce the expected lint failure;
restoring the file afterward produces a clean diff. No CLAUDE.md change —
same reasoning as §9, this is tooling closing a gap the existing rule already
described, not a new prose rule.

---

## 13. Frontmatter Must Be a Complete Source Manifest, Not a Subset

*Placement note: this belongs thematically with §2's citation-completeness
group, not at the end — appended here rather than inserted-and-renumbered, to
avoid the cross-reference risk a full renumbering carries. (The previous
renumbering pass on this file did in fact miss a stale reference in
`wiki/log.md` pointing at old section numbers — fixed in a separate commit,
not recorded in this addendum itself.) Worth relocating in a future
consolidated reorganization pass.*

### The rule

**A durable page's frontmatter `sources:` list must be a complete manifest of
every source that page's own body cites or relies on — not a representative
subset, and not satisfied by the same source appearing only on a different,
cross-referenced page.** If page A states a fact directly and defers *further*
detail to page B ("see B's page for the full account"), A's own frontmatter
still needs an entry for whatever A itself states — A pointing at B doesn't
make A's own manifest accurate.

### Why this matters

A frontmatter source list exists so a reader (or a session) can audit what a
page relies on at a glance, without reading the whole body first. If the body
cites something inline that never makes it into frontmatter, the manifest
silently under-reports what the page actually depends on — and this is
especially easy to miss when a page shares subject matter with another page
that *does* carry the fuller citation, since it's tempting to treat the
citation as "covered" once it exists anywhere in the wiki rather than
specifically on the page making the claim.

### Where this fits in the blueprint

Add to the schema/instruction file's frontmatter/citation rules: the
`sources:` field is a *complete* manifest for that specific page, not a
best-effort subset — verify it by checking the field against the page's own
body, not by confirming the citation exists somewhere in the wiki.

### Illustrative example (generic, not tied to any specific programme)

A project page's status table states a specific progress figure, drawn from a
particular message, in its body text — but the page's frontmatter only lists
the tracker database as a source. The message that's actually being relied on
for the figure is never added to frontmatter, even though the body directly
quotes it.

---

### Build notes (dummy-program-specific — exclude from merge)

Found four real instances of this while doing other work, never in a
dedicated sweep for it: the Milestones table's newly-added inline Slack
citations were never added to `flexpay-au.md`'s own frontmatter after the
citation rewrite; the Risks table had the same gap; and `people/ben-okafor.md`
and `people/grace-lindqvist.md` each stated a Notion-status claim in their
body without the corresponding Notion citation in their own frontmatter (the
project page had it, they didn't).

**Status:** the four found instances were fixed at the time. The *rule
itself* was never written down until now — flagged as an outstanding item
across two separate conversation checkpoints before actually being added.

---

## 14. Reference a Non-Durable Item by Its Smallest Containing Heading

*Placement note: this belongs thematically with §3's anchor-navigation group
— appended here rather than inserted-and-renumbered, same reasoning as §13.*

### The rule

**When a durable page needs to reference one specific item that lives inside
a table or list on another page — and that item doesn't warrant becoming its
own durable page — link to the smallest existing heading that contains it,
not to an unrelated but nearby entity as a substitute, and not by inventing a
new per-item anchor.** A table row can't hold its own Markdown heading (see
[§3](#3-anchor-navigation-heading-as-slug-not-a-id-tags) — headings are the
only anchor mechanism proven to actually work), so there's no way to link
*precisely* to one row. The resolution is to link at the *section* level
(e.g. the enclosing `## Milestones` heading) — accurate about where to look,
even without row-level precision — rather than either fabricating anchor
infrastructure a table can't structurally support, or substituting a
different, only-tangentially-related entity that merely happens to have a
real page nearby.

### Why this matters

Not every tracked entity deserves its own durable page — granular items
(individual milestones, tasks, tickets) are usually better kept as rows in a
table on a project page, to avoid duplicating an external tracker's full
detail into the wiki. But other durable pages sometimes need to reference
*one specific* such item precisely — e.g. a decision page whose gate depends
on one milestone's completion. Without a stated rule, the natural failure
mode is picking whatever *does* have a working link nearby as a stand-in,
even when it's the wrong thing — which produces a misleading picture of what
actually depends on what (visible directly in a tool like Obsidian's graph
view, where the substitute entity ends up looking connected to something it
isn't really about).

### Where this fits in the blueprint

Add to the schema/instruction file's cross-reference guidance: referencing a
granular, non-durable item (a table row, a tracker entry) should link to the
smallest existing heading that contains it, never to an unrelated entity
picked only because it has a working anchor. Pair this with the
heading-as-slug anchor rule ([§3](#3-anchor-navigation-heading-as-slug-not-a-id-tags))
so both the "how to anchor a section" and "how to reference something inside
one" rules sit together.

### Illustrative example (generic, not tied to any specific programme)

A decision page states its rollout is gated on a specific milestone's
completion. That milestone is one row in a status table on a different page,
with no anchor of its own. Rather than linking to a different, textually
adjacent decision that happens to have its own page, the decision links to
the table's enclosing section heading on the project page instead.

---

### Build notes (dummy-program-specific — exclude from merge)

The literal case: `d4-gtm-spend-gate.md`'s gate depends on milestone M08's
completion, but M08 has no anchor of its own — it's one row in
`flexpay-au.md`'s Milestones table. It originally linked to `d3-sydney-pilot.md`
(the decision that established the Sydney-pilot concept) as a stand-in, since
D3 had a real page and M08 didn't — which made Obsidian's graph show D4
connected to D3 directly, misrepresenting what D4 actually depends on (M08's
completion, not D3's existence). Resolved by linking both D3's and D4's M08
mentions to `../projects/flexpay-au.md#milestones` (the existing section
heading) instead.

**Status:** the specific D3/D4 fix was made at the time this was discovered.
The rule itself was never written down as its own addendum entry until now.

---

## Log (dummy-program-specific — exclude from merge)

Section numbers in every entry below refer to this file's **current**
numbering (post-reorganization, see the final entry), not necessarily the
number a section had at the moment each entry was written — updated for
consistency so the log stays a useful cross-reference against the file as it
exists today, not a puzzle requiring a historical numbering key.

- **2026-10-01** — File created, consolidating `source-addressability-addendum.md`
  and `live-link-citation-completeness.md` (content folded into §1, §2, §3, and
  §10, unchanged in substance) into this single running file, per the owner's
  request. §6 and §7 added as new entries at the same time.
- **2026-10-01 (follow-up)** — §1, §2, §3, §6, §7, and §10 marked with
  incorporation status against this repo's `CLAUDE.md` (all now incorporated
  except §10, which was also fixed at the same time). §8 added, surfaced from
  noticing §10 itself sat flagged-but-unactioned across several turns even
  after permission to edit CLAUDE.md was already established.
- **2026-10-01 (follow-up 2)** — New subsection added under §2, after the owner
  caught a Notion citation link (M07) that 404'd. Root cause: two Notion MCP tools
  return disagreeing `url` fields for the same page, and the wrong one was trusted
  for all 10 milestone-row citations. Distinguished explicitly from §3 (that's
  about viewer navigation behavior for links internal to the wiki; this is about
  external URL correctness, unrelated to which app reads the wiki). All 10 URLs in
  `wiki/sources/notion/2026-10-01.md` corrected and HTTP-verified. CLAUDE.md's
  Notion bullet and a new connector-URL-verification paragraph added the same day.
- **2026-10-01 (follow-up 3)** — §9 added, after the owner spotted an unresolved
  node in Obsidian's graph view traced to a directory link (`../people/`) in
  `wiki/projects/flexpay-au.md` that `bin/lint-wiki` had never flagged.
  `check_link_targets` tightened from `os.path.exists` to `os.path.isfile` for
  both body links and frontmatter citations. No CLAUDE.md change — this was a
  tooling gap, not a prose-rule gap.
- **2026-10-01 (follow-up 4)** — §11 added, after discovering `flexpay-au.md`'s
  Risks table falsely claimed all 4 risks were Slack-corroborated when R1 had no
  matching Slack message at all. Traced against the blueprint directly: the
  Acceptance checklist's "every claim has a citation" was satisfied by R1 anyway,
  since it never checked whether a *summary sentence about several claims* held
  for each one. Rule added to CLAUDE.md's "Self-review habits" (fourth bullet);
  the false claim corrected in the same commit as the Risks table citation work.
- **2026-10-01 (follow-up 5)** — §12 added: built `bin/lint-wiki` checks for the
  two mechanically-checkable sub-categories of §11 (verbatim quotes, relative-date
  language). Running them found a second, uncorrected copy of the M04 bug on
  `people/maya-chen.md`, a similar imprecise paraphrase on the same page, two
  pages missing a Notion citation, and a third copy of the D4 misquote inside a
  `sources/**` file's own commentary. All corrected; the `sources/**` edit is a
  scoped, explicitly-logged exception to normal immutability (see
  `wiki/log.md`'s "Post-build corrections" entry), authorized for this
  active-build-phase exercise specifically, not a general practice.
- **2026-10-01 (follow-up 6)** — §4 and §5 added, from a full-session review
  of outstanding threads that hadn't been circled back to. §4: inline citation
  link text must label which lane it points to (Slack/Notion/Drive) — fixed in
  the Milestones/Risks tables when first raised, never written down as a rule
  or applied elsewhere; `d2-rules-based-credit-model.md`'s four unlabeled
  channel-name links flagged as not yet retroactively fixed. §5: cited URLs
  must render as actual hyperlinks, never bare text — prompted directly by the
  owner receiving one as plain text mid-conversation. Both incorporated into
  CLAUDE.md's "Live-link citations" section the same day.
- **2026-10-01 (follow-up 7)** — Whole-file restructure: every section split
  into a portable core (rule, rationale, "Where this fits in the blueprint",
  a genericized illustrative example where needed) and a trailing "Build
  notes (dummy-program-specific — exclude from merge)" subsection carrying
  the FlexPay AU specifics and incorporation status. Prompted by the owner
  noting that "Status" lines and FlexPay-specific illustrations would be
  meaningless or confusing once this file is actually merged into a v2
  blueprint intended for use with zero dummy-program context. Section
  numbering and titles were deliberately left unchanged in this pass.
- **2026-10-01 (follow-up 8)** — Second structural pass, after the owner asked
  for a critical review of merge-readiness rather than a confirmation.
  Findings: (1) the section then-titled "Known Gap: CLAUDE.md's Link-Path
  Wording vs. Actual Lint Behavior" was the only section title naming a
  specific tool-file rather than a portable principle — the blueprint's own
  convention is `AGENTS.md` *or equivalent*, confirmed against the blueprint
  text directly, not assumed — retitled to "Schema-Doc Wording Must Match What
  Its Own Lint Tooling Enforces" (now §10). (2) the file's organizing
  principle was chronological discovery order, appropriate for a build log but
  not for content meant to merge into a reference document — reorganized into
  two thematic groups (source/citation mechanics, §1–§5; self-review and
  verification habits, §6–§12), with this Log preserving the original
  discovery order and now-corrected cross-references. (3) the file intro
  itself hadn't been labeled "exclude from merge" despite being entirely about
  this file's own maintenance — labeled, and a note added distinguishing that
  Claude Code was the tool used throughout while the blueprint itself remains
  tool-agnostic (`AGENTS.md` *or equivalent*). Two of §1's specific blueprint
  references (exact section names, and a verbatim quote of deliverable #2's
  current wording) were checked directly against `ai-second-brain-blueprint.md`
  rather than trusted from an earlier session that predates this conversation
  — both confirmed accurate.
- **2026-10-01 (follow-up 9)** — §13 added, the first of four items identified
  in a full-conversation audit of outstanding threads that had been flagged but
  never actually resolved. Appended rather than inserted into its natural
  thematic position (alongside §2) to avoid another renumbering pass so soon
  after the last one. Rule added to CLAUDE.md's "Page structure and citation
  rules" section the same day.
- **2026-10-01 (follow-up 10)** — §14 added, the second of the four
  audit-identified items: the D3/D4/M08 lesson (link to the smallest
  containing heading for a non-durable, table-row item rather than
  substituting an unrelated entity with a working anchor) had been resolved in
  the wiki itself at the time but never written up as its own rule. Rule
  added to CLAUDE.md's "Page structure and citation rules" section the same
  day, right after §13's.

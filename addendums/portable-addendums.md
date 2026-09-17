# Second-Brain Blueprint Addendums (portable core)

Fourteen gaps found while building a wiki off the second-brain blueprint,
written to merge into a v2 blueprint or straight into a fresh instruction file
(`AGENTS.md`, `CLAUDE.md`, or equivalent — the blueprint is tool-agnostic).
Each entry below is a rule, why it matters, and where it plugs into the
blueprint — nothing else. It carries no build-specific history, no example
tied to any one programme's data, and no incorporation status, so it applies
unchanged to a first-time build with no context of where these were found.

For the discovery story behind each rule — what surfaced it, when it was
fixed, and how it was tracked — see
[build-history-addendums.md](build-history-addendums.md), the fuller working
file this was distilled from. That file is this build's own audit trail;
this one is the reusable output of it.

## Contents

**Source & citation mechanics**

1. [Source Addressability](#1-source-addressability)
2. [Live-Link Citation Completeness](#2-live-link-citation-completeness)
3. [Frontmatter Must Be a Complete Source Manifest](#3-frontmatter-must-be-a-complete-source-manifest)
4. [Anchor Navigation: Heading-as-Slug, Not `<a id>` Tags](#4-anchor-navigation-heading-as-slug-not-a-id-tags)
5. [Reference a Non-Durable Item by Its Smallest Containing Heading](#5-reference-a-non-durable-item-by-its-smallest-containing-heading)
6. [Label Which Lane an Inline Citation Points To](#6-label-which-lane-an-inline-citation-points-to)
7. [Render Cited URLs as Hyperlinks, Not Plain Text](#7-render-cited-urls-as-hyperlinks-not-plain-text)

**Self-review & verification habits**

8. [Self-Audit Against a Rule's Full Literal Scope](#8-self-audit-against-a-rules-full-literal-scope)
9. [Flag Unverified Claims About External Tool Behavior](#9-flag-unverified-claims-about-external-tool-behavior)
10. [Track Deferred Items](#10-track-deferred-items)
11. [Verification Tooling Needs the Same Intent-vs-Letter Audit as Prose Rules](#11-verification-tooling-needs-the-same-intent-vs-letter-audit-as-prose-rules)
12. [Schema-Doc Wording Must Match What Its Own Lint Tooling Enforces](#12-schema-doc-wording-must-match-what-its-own-lint-tooling-enforces)
13. [Verify Aggregate Claims Against Every Instance They Describe](#13-verify-aggregate-claims-against-every-instance-they-describe)
14. [Mechanical Checks for the Two Sub-Categories of §13 That Are Actually Checkable](#14-mechanical-checks-for-the-two-sub-categories-of-13-that-are-actually-checkable)

---

## 1. Source Addressability

**Rule:** Every source lane gets a resolvable root identifier recorded in the
schema file, not just a name — and any lane whose contents can grow gets a
live re-enumeration instruction anchored to that root, not a hardcoded list
of what it currently contains. Concretely, for each lane: record the stable
ID/address (channel ID, page/database ID, folder ID — whatever the
connector's own addressing scheme is), plus a direct link where the
connector's UI supports one. If the lane has a container-with-children shape
(a parent page with child pages, a folder with files), anchor to the
container's ID and instruct: *re-enumerate the container's current contents
at the start of every refresh's capture step — never rely on a remembered
list.* State currently-known contents as an illustrative, explicitly
non-exhaustive snapshot. Any per-item evidence-quality caveat (e.g. "this
connector doesn't expose real per-row history") should be phrased generically
enough to apply to an item discovered later by the live enumeration, not
hardcoded to only the items named at build time.

**Why:** A name isn't a resolvable address — a fresh session has to re-search
for something named only in prose and hope the match is unambiguous, and one
workspace tends to accumulate near-duplicate names over time. A named list
also goes stale the moment the source grows: a child page added later isn't
in scope until a human notices and hand-edits the instruction file, which is
exactly the manual upkeep a second brain exists to eliminate.

**Where this fits in the blueprint:**
- **"Schema and instruction layer"** — add resolvable source identifiers and,
  for growable sources, a live-enumeration instruction, to what the schema
  should define.
- **"Required deliverables"** — the canonical instruction file should
  explicitly cover source identifiers and traversal, not just ingest, query,
  refresh, lint, citations, contradictions, privacy, and page conventions.
- **"Non-negotiable behaviors"** — add: never hardcode a static list of child
  pages/files/channels for a source whose contents can grow; anchor to a
  stable root ID and re-enumerate live at each refresh.
- Distinct from the existing "link to the original system when permitted"
  rule — that's about citing captured *evidence* back to its origin; this is
  about the schema file being able to *relocate its own sources* without a
  human re-supplying URLs each time. Keep both.

**Template for the schema file's source-scope section:**
```
- **{Lane}** — anchored at {container type} `{stable ID}` ({direct link if the
  connector supports one}). At the start of every refresh's capture step,
  re-{list/fetch/enumerate} this {container} fresh and treat whatever it currently
  contains as in scope — never rely on a remembered list. As of {date}, that's
  {known children/items}, but this is illustrative, not exhaustive: something added
  later is picked up automatically by the next refresh's live enumeration, with no
  edit to this file required.
```

---

## 2. Live-Link Citation Completeness

**Rule:** Every entity a refresh names in a capture file — including the
live-enumeration listing of what a container search returned, not just
quoted facts pulled from it afterward — must be a real hyperlink to its own
live URL, not a bare ID in backticks. Keep the ID alongside the link if
useful, not instead of it. A URL-shaped field returned by a connector is not
automatically a working link: cross-check when more than one tool call
returns a URL-labeled field for the same object and they disagree; verify
resolution directly where practical (a fetch, an HTTP request); where
verification is inconclusive (an auth-walled platform redirecting every
request to the same login page), fall back to asking the human to confirm
one representative link rather than guessing. Do this once, at first
integration of a source lane — then record the confirmed-working URL
template in the schema file itself, the same way a chat platform's permalink
formula would be spelled out.

**Why:** A "record a live link next to the quoted text" rule is easy to
satisfy for individual cited facts while missing the capture step's own
live-enumeration listing, since it isn't literally "quoted text" — a narrow
reading skips it, and IDs end up as bare backtick text even when a working
link was already available in the same tool result. Separately, a link that
*is* present can still be wrong: different tool calls against the same
connector can return disagreeing `url`-labeled fields for the same object —
one correct, one malformed — and citations built on the wrong one look
identical in markdown but silently fail to resolve.

**Example** — before (not clickable): `1. **Some Document Name** (Doc,
\`abc123def456...\`)`. After (clickable, ID kept for reference): `1.
**[Some Document Name](https://.../abc123def456.../edit)** (Doc, id
\`abc123def456...\`)`.

**Where this fits in the blueprint:** the schema/instruction file's citation
rule must explicitly cover a refresh's live-enumeration listing, not only
facts quoted from a source afterward. Add: *before trusting any URL-shaped
field a connector returns, verify it actually resolves — a field named "url"
isn't proof it's correct, and different tool calls against the same
connector can disagree.*

---

## 3. Frontmatter Must Be a Complete Source Manifest

**Rule:** A durable page's frontmatter `sources:` list must be a complete
manifest of every source that page's own body cites or relies on — not a
representative subset, and not satisfied by the same source appearing only
on a different, cross-referenced page. If page A states a fact directly and
defers *further* detail to page B, A's own frontmatter still needs an entry
for whatever A itself states — A pointing at B doesn't make A's own manifest
accurate.

**Why:** The frontmatter source list exists so a reader can audit what a
page relies on at a glance, without reading the whole body first. It's
especially easy to under-report when a page shares subject matter with
another page that *does* carry the fuller citation — tempting to treat a
citation as "covered" once it exists anywhere in the wiki, rather than
specifically on the page making the claim.

**Example** (generic): a project page's status table states a specific
progress figure, drawn from a particular message, in its body text — but the
page's frontmatter only lists the tracker database as a source. The message
actually being relied on for the figure is never added to frontmatter, even
though the body directly quotes it.

**Where this fits in the blueprint:** add to the schema/instruction file's
frontmatter/citation rules — the `sources:` field is a *complete* manifest
for that specific page, not a best-effort subset, verified by checking the
field against the page's own body, not by confirming the citation exists
somewhere in the wiki.

---

## 4. Anchor Navigation: Heading-as-Slug, Not `<a id>` Tags

**Rule:** Every per-section citation anchor inside a capture file must be
the section's own Markdown heading (`### the-anchor-id`) — never a separate
`<a id="...">` tag next to a differently-worded heading. Put the
human-readable label as a bold line immediately below the heading, not in
the heading text itself. Use lowercase kebab-case for the anchor id — that
form survives essentially any heading-slugification algorithm unchanged, so
it stays stable across renderers.

**Why:** A bare `<a id="anchor-id"></a>` placed before a heading —
```
<a id="some-anchor-id"></a>
### 2026-08-14 — Some Meeting
```
— opens the right *file* in tools like Obsidian and VS Code, but lands at
the top, not at the tagged section. `<a id>` fragment-scrolling is native
*browser* behavior: it works when a tool renders markdown to real HTML in an
actual browser tab (e.g. GitHub's web view), but Obsidian and VS Code use
their own internal link routers, which resolve a link's `#fragment` against
a **heading's own auto-slugified text**, not an arbitrary `id` sitting next
to it — a behavior shared by most markdown-aware apps with in-app
navigation, which makes heading-as-slug the *broader*-compatibility choice,
not a narrower one. The fix — make the heading itself the anchor string —
stays plain CommonMark, so it doesn't reintroduce vendor-specific syntax:
```
### some-anchor-id
**2026-08-14 — Some Meeting.**
```
This was only established by directly testing in real tools, not by
reasoning about the CommonMark spec alone (see [§9](#9-flag-unverified-claims-about-external-tool-behavior)).

**Where this fits in the blueprint:** add to the schema/instruction file's
citation-anchor guidance — per-section citation anchors must be the
section's own heading, lowercase kebab-case, never a separate `<a id>` tag
next to a differently-worded heading.

---

## 5. Reference a Non-Durable Item by Its Smallest Containing Heading

**Rule:** When a durable page needs to reference one specific item that
lives inside a table or list on another page — and that item doesn't
warrant becoming its own durable page — link to the smallest existing
heading that contains it, not to an unrelated but nearby entity as a
substitute, and not by inventing a new per-item anchor. A table row can't
hold its own Markdown heading (see [§4](#4-anchor-navigation-heading-as-slug-not-a-id-tags) —
headings are the only anchor mechanism proven to work), so link at the
*section* level (e.g. the enclosing `## Milestones` heading) instead.

**Why:** Not every tracked entity deserves its own durable page — granular
items (individual milestones, tasks, tickets) are usually better kept as
table rows on a project page, to avoid duplicating an external tracker's
full detail into the wiki. But other durable pages sometimes need to
reference *one specific* such item precisely — e.g. a decision page whose
gate depends on one milestone's completion. Without a stated rule, the
natural failure mode is picking whatever *does* have a working link nearby
as a stand-in, even when it's the wrong thing — producing a misleading
picture of what actually depends on what (visible directly in a tool like
Obsidian's graph view, where the substitute entity ends up looking connected
to something it isn't really about).

**Example** (generic): a decision page states its rollout is gated on a
specific milestone's completion. That milestone is one row in a status table
on a different page, with no anchor of its own. Rather than linking to a
different, textually adjacent decision that happens to have its own page,
the decision links to the table's enclosing section heading on the project
page instead.

**Where this fits in the blueprint:** add to the schema/instruction file's
cross-reference guidance — referencing a granular, non-durable item should
link to the smallest existing heading that contains it, never to an
unrelated entity picked only because it has a working anchor. Pair with §4
so "how to anchor a section" and "how to reference something inside one" sit
together.

---

## 6. Label Which Lane an Inline Citation Points To

**Rule:** A citation's visible link text must make clear which lane it
points to — Slack, chat tool, ticketing system, shared drive, whatever the
source actually is — not just that it's a link at all. `[Slack
2026-08-14](url)` or `([Notion](url))`, not a bare date or a bare channel
name like `[2026-08-14](url)` or `([finance-team](url))`. Applies anywhere a
citation is inlined into prose or a table cell.

**Why:** A citation rule that only requires a link to *exist and resolve*
doesn't also guarantee the link is self-describing — those are different
properties, and a wiki can satisfy the first while silently failing the
second, since nothing about a working-but-unlabeled link looks broken.

**Example** (generic): a decision page cites four messages as corroboration,
using each channel's name as the link text: `(#finance)`, `(#legal)`.
Nothing in the link text itself says these came from a chat tool at all — a
reader has to infer that from a sentence elsewhere on the page.

**Where this fits in the blueprint:** add to the schema/instruction file's
citation-format guidance — citation link text must self-identify its source
lane. Pair with an explicit example of the required format and a
counter-example of the failure, so it's unambiguous at build time.

---

## 7. Render Cited URLs as Hyperlinks, Not Plain Text

**Rule:** Any cited URL, in chat or in wiki content, is rendered as an
actual markdown hyperlink — `[label](url)` — never as bare/plain text.

**Why:** A citation rule that says to "include the live link along with the
fact" without also saying the link has to actually *be* a link is satisfied,
in its narrowest reading, by a URL presented as plain text — the reader
still has to copy-paste it, exactly the friction live-link citations exist
to remove.

**Where this fits in the blueprint:** add explicitly to the citation rule —
a cited URL is always rendered as a markdown hyperlink, never bare text, in
both wiki content and in a chat response synthesizing from it.

---

## 8. Self-Audit Against a Rule's Full Literal Scope

**Rule (habit):** after applying a rule to the task at hand, take one
additional pass asking "does this rule's evident *purpose* cover anything
else this file/page/output also contains, even if the rule's literal
wording doesn't name it explicitly?" Applies to any rule with an implicit
scope — citation completeness, frontmatter requirements, contradiction
handling, staleness checks.

**Why:** When a rule is stated with an implicit scope, it's easy to satisfy
it for the specific case at hand while missing other cases the rule's
*intent* clearly covers but its *literal wording* doesn't name. Cheap to
catch immediately after writing something, expensive to catch later — it
surfaces as a bug report, or never surfaces at all.

**Where this fits in the blueprint:** add as a stated review habit alongside
the schema's citation/contradiction rules — applying a rule correctly to the
immediate case isn't the same as checking whether its purpose extends
further than its literal wording within the same output.

---

## 9. Flag Unverified Claims About External Tool Behavior

**Rule (habit):** when a design choice depends on how a specific external
tool, connector, or renderer behaves — and that behavior hasn't been
directly observed (a tool call, a test, or the owner confirming it) — say so
explicitly as an assumption, not a settled fact. Where practical, propose a
small, reversible test before rolling the assumption out broadly. Anything
verifiable in-repo (does a file exist, does a script exit 0, does lint pass)
should just be checked directly, not hedged.

**Why:** An agent has no way to open a specific third-party app and observe
how it behaves — that's a fact about specific software establishable only by
testing it or having a human confirm it, not by reasoning about a spec. A
plausible, spec-compliant design can still be wrong if it rests on an
untested assumption about how a particular tool's internals actually work.

**Where this fits in the blueprint:** add as a stated review habit — before
asserting how a specific external tool will render, navigate, or resolve
something, distinguish "verified by testing" from "inferred from general
principles" explicitly, and propose the cheapest test that would confirm or
disconfirm the assumption before committing to it broadly.

---

## 10. Track Deferred Items

**Rule (habit):** before declaring any piece of work "done" — a refresh, a
requested fix, a chat response — scan for outstanding flagged/deferred items
from earlier in the same session (or, for a refresh, from the log's open
judgment items) and check whether anything just discovered or just permitted
resolves one of them. If so, close the loop explicitly rather than leaving
it to the owner to notice the connection themselves.

**Why:** Correctly deferring something — logging a genuine contradiction as
a judgment item, holding off an edit pending the owner's authorization — is
not the same as resolving it. Two concrete failure shapes: (1) a blocking
constraint quietly lifts (permission is later granted for a *different*
edit) but nothing re-checks the earlier, still-open item; (2) new evidence
resolves an old open item, but nothing connects the two, so the owner is
left seeing "unresolved — needs your input" long after it's actually been
settled.

**Where this fits in the blueprint:** add as a stated review habit, paired
with the contradiction-resolution protocol — a judgment item logged as
unresolved needs periodic re-checking against new evidence and newly-granted
permissions, not just a one-time log entry.

---

## 11. Verification Tooling Needs the Same Intent-vs-Letter Audit as Prose Rules

**Rule:** when writing or reviewing a structural/lint check, verify it
actually enforces the property it claims to enforce — not a weaker,
easier-to-satisfy proxy for it. For a link-integrity check: verify the
target is a *file* (`os.path.isfile`), not merely that *some path* exists
(`os.path.exists`, also true for directories). General version: whenever a
check's implementation is more permissive than the plain-English description
of what it's supposed to guarantee, that gap is exactly where bugs will
silently pass through — worse than a missing check, since a passing check
creates false confidence the property actually holds. This is the tooling
counterpart to [§8](#8-self-audit-against-a-rules-full-literal-scope): §8's
fix is a habit to repeat every time; this one's fix is a one-time code
change that then holds for every future case with no repeated vigilance.

**Why:** A structural check can satisfy the *letter* of its stated purpose
("does this path exist") while missing the actual *intent* ("does this link
resolve to a page a reader can open"). A result that technically passes is
worse than an obviously-missing check, because nothing signals attention is
needed — the automated safety net looks like it's working.

**Where this fits in the blueprint:** any lint/verification tooling a build
relies on should get this scrutiny when first written or extended — read
each check's implementation next to its own stated purpose and ask whether
the code actually verifies that purpose, or something weaker that happens to
overlap with it most of the time.

---

## 12. Schema-Doc Wording Must Match What Its Own Lint Tooling Enforces

**Rule:** when a schema/instruction file states a path or format
convention, and that convention is also enforced by lint tooling, the two
must agree — and if the tooling implements two different rules for two
different cases (e.g. frontmatter citations resolved one way, body links
resolved another), the prose must describe both distinctly, not collapse
them into one blended description.

**Why:** The prose is what a human or future session reads and follows; the
tooling is what actually enforces correctness. If they drift apart, content
that follows the prose fails lint, and content that passes lint doesn't
necessarily match the documented convention — a build that happens to follow
the tooling's actual behavior still passes lint while silently contradicting
its own documentation, misleading the next session that trusts the written
rule over the code.

**Where this fits in the blueprint:** whenever a schema file states a
structural convention that lint tooling also checks, verify the two agree by
testing, not by assuming the prose was written correctly — the same
intent-vs-letter audit [§11](#11-verification-tooling-needs-the-same-intent-vs-letter-audit-as-prose-rules)
recommends for tooling applies symmetrically to the prose describing it.

---

## 13. Verify Aggregate Claims Against Every Instance They Describe

**Rule:** before writing any sentence that generalizes across multiple facts
— "all N are X," "every Y has been Z," "N of M are corroborated" — verify it
against each individual instance the generalization covers, not just the
ones that prompted it or come easily to mind. This isn't solvable by adding
more lint rules — the bug is semantic, not structural, and no automated
check can verify it without re-deriving the evidence itself. It's a
discipline: re-derive, don't infer, before asserting a pattern holds
universally.

**Why:** A wiki whose summary sentences can't be trusted without
independently re-deriving the evidence behind them has lost the point of
being a second brain. A confidently false generalization is worse than a
broken link: a broken link fails *loud* (click it, nothing happens); a false
generalization fails *silent*, reading identically confident whether or not
it's true, giving the reader no signal to double-check at all. It also slips
past every existing safeguard for a specific reason: "every claim has a
citation" is satisfiable even by a false generalization, since a claim can
individually have a citation while a *summary sentence about several claims*
is untrue for one of them — citation presence and generalization accuracy
are different properties. Contradiction resolution isn't triggered either,
since nothing about this is a contradiction between sources — it's an
omission, a generalization never checked against the specific case that
breaks it. And structural checks (broken links, orphans, staleness, secrets,
formatting) don't catch it because the defect is in the prose making the
claim, not in anything a structural check inspects.

**Where this fits in the blueprint:** add to the compile-and-test stage or
the acceptance checklist directly — any sentence asserting a pattern across
multiple durable claims (a count, an "all/every" statement, a
corroboration-rate claim) must be checked against each instance it covers
before publication, not inferred from a representative sample. State this as
a distinct requirement from "every claim has a citation," not assumed to be
covered by it.

---

## 14. Mechanical Checks for the Two Sub-Categories of §13 That Are Actually Checkable

**Rule:** §13 covers three failure sub-categories, not one: fabricated or
inaccurate direct quotes, relative-date language conflated with absolute
dates, and paraphrases overclaiming precision the source doesn't support.
Only the first two are mechanically checkable — the third requires
understanding what a paraphrase *implies* versus what the source
*establishes*, a judgment call no deterministic script can make. Build lint
checks for the first two rather than relying on §13's discipline alone:

- **A verbatim-quote check** — extracts quoted text from a durable page's
  body and confirms it's a literal substring somewhere in that page's cited
  sources. Catches a fabricated quote with certainty; can't catch an
  unquoted paraphrase, since there's nothing to string-match.
- **A relative-date-language check** — flags any cited source whose content
  contains relative-date words (day names, "tomorrow," "this/next/last
  week/month") as worth a second look. Can't verify a nearby claim is
  *wrong*, only that it's citing something where getting it wrong is easy —
  genuinely heuristic, expect false positives where the relative language
  isn't actually load-bearing for any claim drawn from it.

**Why:** Auditing every citation by hand against §13's discipline catches
real bugs but is unreliable alone — a manual re-check of "just the citations
touched in this session" can miss an identical, uncorrected instance of the
same bug on a completely different page, found only once wiki-wide tooling
exists and runs against every page. Tooling beats vigilance because it
doesn't get tired on the tenth item the way a person re-checking by hand
does.

**Where this fits in the blueprint:** add both checks to the build's
lint/verification tooling, as warnings rather than hard errors — both are
heuristic and will produce false positives that are cheap to review and
dismiss. Note explicitly in the tooling's own documentation that a third
failure category (paraphrase overclaiming precision) exists and is *not*
covered by either check, so it doesn't read as solved once the two
mechanical checks are in place.

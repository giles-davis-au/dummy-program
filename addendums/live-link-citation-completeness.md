# Addendum: Live-Link Citation Completeness

Addendum to [ai-second-brain-blueprint.md](../ai-second-brain-blueprint.md) and to
[CLAUDE.md](../CLAUDE.md)'s "Live-link citations" section. **Maintained by the
owner (Giles Davis)** — Claude Code should read this file (and any others added to
`addendums/`) before a refresh, alongside CLAUDE.md, but should not write to it. See
CLAUDE.md's "What the agent may edit."

## What this corrects

CLAUDE.md's Live-link citations section already required a real, clickable link
"next to the quoted text, at capture time" for every fact pulled from Slack,
Notion, or Google Drive. In practice, during the 2026-10-01 Version 0 build, this
got applied inconsistently: quoted facts got proper links, but the capture step's
own **live-enumeration listing** — the "here's what I found when I re-enumerated
the Notion parent page / Drive folder" step that CLAUDE.md's refresh workflow
requires at the start of capture — did not. Google Drive file IDs and a Notion page
ID were recorded as bare text in backticks (e.g.
`` `16gr13nLMHj4EH_cLYkX2rLlUDkYScFk_cBwAsPlk8ig` ``) instead of as hyperlinks, so
there was no click-through at that point in the file — even though a working link
(the `viewUrl` / page URL) had already been fetched and was sitting right there in
the tool result.

## The rule (now also in CLAUDE.md, "Live-link citations")

Every entity a refresh names in a capture file — including the live-enumeration
listing of what Notion/Drive returned, not just quoted facts pulled from it
afterward — must be a real hyperlink to its own live URL (`viewUrl` / page URL), not
a bare ID in backticks. If an ID is worth keeping for reference (a Drive file ID, a
Notion page ID), keep it, but alongside the link, not instead of it.

### Example

Before (not clickable):
> 1. **FlexPay AU — Weekly Programme Meeting Notes** (Doc, `16gr13nLMHj4EH_cLYkX2rLlUDkYScFk_cBwAsPlk8ig`)

After (clickable, ID kept for reference):
> 1. **[FlexPay AU — Weekly Programme Meeting Notes](https://docs.google.com/document/d/16gr13nLMHj4EH_cLYkX2rLlUDkYScFk_cBwAsPlk8ig/edit)** (Doc, id `16gr13nLMHj4EH_cLYkX2rLlUDkYScFk_cBwAsPlk8ig`)

## Follow-up: the per-section anchor mechanism didn't actually work

The fix above made every capture-file entry a real hyperlink. But the *internal*
per-section anchors this whole scheme depends on — so a citation could deep-link
into one specific dated section of a multi-entry capture file, not just the file as
a whole — turned out not to work once tested in the owner's actual daily tools.

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

## Known related gap — not yet fixed, flagged for the owner

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
would write root-relative links that then fail lint. Worth clarifying in CLAUDE.md
directly; left as a known gap rather than fixed here since it's a genuine
correction to CLAUDE.md's own wording, not an addendum-level nuance.

## Log

- **2026-10-01** — Corrected in
  [wiki/sources/gdrive/2026-10-01.md](../wiki/sources/gdrive/2026-10-01.md) and
  [wiki/sources/notion/2026-10-01.md](../wiki/sources/notion/2026-10-01.md) (both
  files' "Live enumeration result" sections). Rule added to CLAUDE.md's "Live-link
  citations" section. This addendum file created to record the correction and give
  a place to log future refinements of the same kind.
- **2026-10-01 (follow-up)** — Discovered the `<a id="...">` anchor mechanism did
  not actually enable jump-to-section navigation in Obsidian or VS Code (landed on
  the right file, never the right section) — confirmed by the owner testing both
  apps. Replaced every per-section anchor across all three capture files
  ([wiki/sources/slack/2026-10-01.md](../wiki/sources/slack/2026-10-01.md),
  [wiki/sources/notion/2026-10-01.md](../wiki/sources/notion/2026-10-01.md),
  [wiki/sources/gdrive/2026-10-01.md](../wiki/sources/gdrive/2026-10-01.md), 53
  anchors total) with the heading-as-slug pattern above. No citation links
  elsewhere in the wiki needed to change, since the fragment strings themselves
  were unchanged — only the capture files' own heading formatting was.

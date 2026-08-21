"""Shared helpers for the FlexPay AU wiki scripts. Stdlib only, no dependencies."""
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WIKI_ROOT = os.path.join(ROOT, "wiki")
DURABLE_DIRS = ["projects", "people", "decisions"]

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.DOTALL)
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
LOG_ASOF_RE = re.compile(r"^##\s*Refresh\s*[—-]\s*as-of\s+(\d{4}-\d{2}-\d{2})", re.MULTILINE)
SOURCE_HEADING_RE = re.compile(r"^### (\S+)\s*$", re.MULTILINE)


def vault_rel(path):
    """Path relative to wiki/ (the knowledge-content root) — used for anything
    written into wiki content itself (current-state.*, entity-index.json), so it
    stays correct regardless of where the repo lives on disk or what tool reads it."""
    return os.path.relpath(path, WIKI_ROOT)


def repo_rel(path):
    """Path relative to the repo root — used for diagnostics printed at the terminal
    (lint-wiki, retrieve), since those are read from the repo root, not from inside
    the vault."""
    return os.path.relpath(path, ROOT)


def durable_pages():
    """Yield absolute paths to every .md file under the durable page directories."""
    for d in DURABLE_DIRS:
        dpath = os.path.join(WIKI_ROOT, d)
        if not os.path.isdir(dpath):
            continue
        for name in sorted(os.listdir(dpath)):
            if name.endswith(".md"):
                yield os.path.join(dpath, name)


def parse_page(path):
    """Return (meta_dict, body_str) for a page. meta values are str or list[str]."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    fm_text, body = m.group(1), m.group(2)
    meta = {}
    current_list_key = None
    for line in fm_text.split("\n"):
        if not line.strip():
            continue
        list_item = re.match(r"^\s*-\s+(.*)$", line)
        if list_item and current_list_key:
            meta.setdefault(current_list_key, []).append(list_item.group(1).strip())
            continue
        kv = re.match(r"^(\w[\w-]*):\s*(.*)$", line)
        if kv:
            key, val = kv.group(1), kv.group(2).strip()
            if val == "":
                meta[key] = []
                current_list_key = key
            else:
                meta[key] = val
                current_list_key = None
    return meta, body


def extract_links(body):
    return LINK_RE.findall(body)


def extract_title(body):
    for line in body.split("\n"):
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return None


def extract_summary(body):
    lines = body.split("\n")
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("**Summary:**"):
            parts = [stripped[len("**Summary:**"):].strip()]
            for cont in lines[i + 1:]:
                if not cont.strip():
                    break
                parts.append(cont.strip())
            return " ".join(parts)
    return None


def read_source_anchor_block(target):
    """Given a citation like 'sources/slack/2026-10-01.md#some-anchor', return the
    text of that anchor's section (from its '### anchor' heading up to the next
    '### ' heading or end of file). Returns None if the file, the anchor, or the
    '#anchor' part itself is missing -- callers that need the whole-file text
    should read the file directly instead."""
    if "#" not in target:
        return None
    file_part, anchor = target.split("#", 1)
    resolved = os.path.normpath(os.path.join(WIKI_ROOT, file_part))
    if not os.path.isfile(resolved):
        return None
    with open(resolved, encoding="utf-8") as f:
        text = f.read()
    headings = list(SOURCE_HEADING_RE.finditer(text))
    for i, m in enumerate(headings):
        if m.group(1) == anchor:
            start = m.end()
            end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
            return text[start:end]
    return None


def log_path():
    return os.path.join(WIKI_ROOT, "log.md")


def latest_asof():
    """Return the most recent as-of cursor recorded in log.md, or None."""
    p = log_path()
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8") as f:
        text = f.read()
    matches = LOG_ASOF_RE.findall(text)
    return matches[-1] if matches else None


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

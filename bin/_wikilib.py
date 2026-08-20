"""Shared helpers for the FlexPay AU wiki scripts. Stdlib only, no dependencies."""
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DURABLE_DIRS = ["projects", "people", "decisions"]

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.DOTALL)
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
LOG_ASOF_RE = re.compile(r"^##\s*Refresh\s*[—-]\s*as-of\s+(\d{4}-\d{2}-\d{2})", re.MULTILINE)


def rel(path):
    return os.path.relpath(path, ROOT)


def durable_pages():
    """Yield absolute paths to every .md file under the durable page directories."""
    for d in DURABLE_DIRS:
        dpath = os.path.join(ROOT, d)
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


def log_path():
    return os.path.join(ROOT, "log.md")


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

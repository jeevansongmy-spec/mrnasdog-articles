#!/usr/bin/env python3
"""
MrNasdog article syndication pipeline.

One command fans an article out to all distribution channels:
  GitHub (this public repo)  ·  Dev.to  ·  Telegram (@mrnasdog)

Each channel is best-effort and independent: if one fails, the others still
go, and the failure is logged so it can be retried later (articles are
evergreen, so a delayed re-send is fine). State is tracked in
.pipeline-state.json so re-running UPDATES instead of duplicating.

Usage:
  python3 syndicate.py growth/the-quiet-strategy.md
  python3 syndicate.py crypto/*.md
  python3 syndicate.py --dry-run growth/the-quiet-strategy.md   # show plan, send nothing
  python3 syndicate.py --devto-draft growth/foo.md              # Dev.to as unpublished draft
  python3 syndicate.py --only telegram growth/foo.md            # one channel only
  python3 syndicate.py --force growth/foo.md                    # re-send even if already posted

Credentials are read from ~/.claude-creds/mrnasdog.env (never committed):
  DEVTO_API_KEY, TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL
GitHub uses the local `git` + `gh` auth already on the machine.

Article markdown front matter (between --- fences):
  title:         "The Quiet Strategy"          (required)
  description:   "one-line summary"            (required — used by Dev.to + Telegram)
  canonical_url: "https://mrnasdoggrowth.com/thinking/the-quiet-strategy"  (required)
  tags:          ["ai", "strategy"]            (optional — Dev.to tags, max 4)
  published:     true                          (optional, default true)
The site (crypto|growth) is inferred from the folder.
"""

import json
import os
import re
import ssl
import subprocess
import sys
import urllib.request
import urllib.error

# macOS system Python often lacks a usable CA bundle for urllib; prefer certifi.
try:
    import certifi
    _SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except Exception:
    _SSL_CTX = ssl.create_default_context()

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
STATE_PATH = os.path.join(REPO_DIR, ".pipeline-state.json")
CREDS_PATH = os.path.expanduser("~/.claude-creds/mrnasdog.env")
CHANNELS = ("github", "devto", "telegram")


# ── helpers ───────────────────────────────────────────────────────────────
def load_creds():
    creds = {}
    if not os.path.exists(CREDS_PATH):
        return creds
    with open(CREDS_PATH) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            creds[k.strip()] = v.strip().strip('"').strip("'")
    return creds


def load_state():
    if os.path.exists(STATE_PATH):
        with open(STATE_PATH) as f:
            return json.load(f)
    return {}


def save_state(state):
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=2, sort_keys=True)
        f.write("\n")


def parse_article(path):
    with open(path) as f:
        raw = f.read()
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", raw, re.S)
    if not m:
        raise ValueError(f"{path}: no front matter found")
    fm_block, body = m.group(1), m.group(2).strip()
    fm = {}
    for line in fm_block.splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key, val = key.strip(), val.strip()
        if val.startswith("[") and val.endswith("]"):
            items = re.findall(r'"([^"]*)"|\'([^\']*)\'|([^,\[\]\s][^,\[\]]*)', val)
            fm[key] = [next(s for s in t if s).strip() for t in items if any(t)]
        else:
            fm[key] = val.strip('"').strip("'")
    slug = os.path.splitext(os.path.basename(path))[0]
    site = "crypto" if os.path.basename(os.path.dirname(os.path.abspath(path))) == "crypto" else "growth"
    for req in ("title", "description", "canonical_url"):
        if not fm.get(req):
            raise ValueError(f"{path}: missing required front-matter field '{req}'")
    published = str(fm.get("published", "true")).lower() != "false"
    tags = fm.get("tags") or []
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(",") if t.strip()]
    # Dev.to tags: lowercase alphanumeric, max 4
    devto_tags = [re.sub(r"[^a-z0-9]", "", t.lower()) for t in tags]
    devto_tags = [t for t in devto_tags if t][:4]
    return {
        "path": os.path.abspath(path), "slug": slug, "site": site,
        "title": fm["title"], "description": fm["description"],
        "canonical_url": fm["canonical_url"], "tags": tags,
        "devto_tags": devto_tags, "published": published, "body": body,
    }


def http(method, url, headers=None, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    headers = dict(headers or {})
    # A real User-Agent is required — Dev.to's Cloudflare 403s the default urllib UA.
    headers.setdefault("User-Agent", "MrNasdog-Pipeline/1.0")
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30, context=_SSL_CTX) as r:
            txt = r.read().decode()
            return r.status, (json.loads(txt) if txt else {})
    except urllib.error.HTTPError as e:
        txt = e.read().decode()
        try:
            return e.code, json.loads(txt)
        except Exception:
            return e.code, {"error": txt[:300]}


# ── channels ──────────────────────────────────────────────────────────────
def push_github(art, state, creds, dry):
    """The article file lives in this public repo; commit + push it."""
    rel = os.path.relpath(art["path"], REPO_DIR)
    if dry:
        return f"would commit + push {rel}"
    subprocess.run(["git", "-C", REPO_DIR, "add", rel], check=True)
    changed = subprocess.run(
        ["git", "-C", REPO_DIR, "diff", "--cached", "--quiet"]
    ).returncode != 0
    if changed:
        subprocess.run(
            ["git", "-C", REPO_DIR, "commit", "-q", "-m",
             f"publish: {art['site']}/{art['slug']}"], check=True)
    subprocess.run(["git", "-C", REPO_DIR, "push", "-q"], check=True)
    url = f"https://github.com/jeevansongmy-spec/mrnasdog-articles/blob/main/{rel}"
    state["github_url"] = url
    return ("committed + pushed" if changed else "already current") + f" → {url}"


def push_devto(art, state, creds, dry, draft):
    key = creds.get("DEVTO_API_KEY")
    if not key:
        raise RuntimeError("DEVTO_API_KEY missing from creds")
    body = {
        "article": {
            "title": art["title"], "body_markdown": art["body"],
            "published": (not draft) and art["published"],
            "canonical_url": art["canonical_url"],
            "description": art["description"], "tags": art["devto_tags"],
        }
    }
    existing = state.get("devto_id")
    if dry:
        return f"would {'update #' + str(existing) if existing else 'create'} (published={body['article']['published']})"
    headers = {"api-key": key, "Content-Type": "application/json"}
    if existing:
        status, resp = http("PUT", f"https://dev.to/api/articles/{existing}", headers, body)
        action = "updated"
    else:
        status, resp = http("POST", "https://dev.to/api/articles", headers, body)
        action = "created"
    if status not in (200, 201):
        raise RuntimeError(f"HTTP {status}: {resp}")
    state["devto_id"] = resp.get("id", existing)
    state["devto_url"] = resp.get("url", state.get("devto_url"))
    return f"{action} → {state.get('devto_url')} (published={body['article']['published']})"


def push_telegram(art, state, creds, dry, force):
    tok = creds.get("TELEGRAM_BOT_TOKEN")
    chan = creds.get("TELEGRAM_CHANNEL", "@mrnasdog")
    if not tok:
        raise RuntimeError("TELEGRAM_BOT_TOKEN missing from creds")
    if state.get("telegram_message_id") and not force:
        return f"skipped (already posted, msg {state['telegram_message_id']}; use --force to repost)"
    hashtags = " ".join("#" + t for t in art["devto_tags"][:3])
    text = (
        f"<b>{_esc(art['title'])}</b>\n\n"
        f"{_esc(art['description'])}\n\n"
        f"🔗 <a href=\"{art['canonical_url']}\">Read the full article</a>"
        + (f"\n\n{_esc(hashtags)}" if hashtags else "")
    )
    if dry:
        return f"would post to {chan}:\n      " + text.replace("\n", "\n      ")
    status, resp = http(
        "POST", f"https://api.telegram.org/bot{tok}/sendMessage",
        {"Content-Type": "application/json"},
        {"chat_id": chan, "text": text, "parse_mode": "HTML",
         "disable_web_page_preview": False},
    )
    if not resp.get("ok"):
        raise RuntimeError(f"HTTP {status}: {resp}")
    state["telegram_message_id"] = resp["result"]["message_id"]
    return f"posted to {chan} (msg {state['telegram_message_id']})"


def _esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ── driver ────────────────────────────────────────────────────────────────
def main(argv):
    dry = "--dry-run" in argv
    draft = "--devto-draft" in argv
    force = "--force" in argv
    only = None
    if "--only" in argv:
        i = argv.index("--only")
        only = argv[i + 1]
        del argv[i:i + 2]
    files = [a for a in argv[1:] if not a.startswith("--")]
    if not files:
        print(__doc__)
        return 1
    channels = (only,) if only else CHANNELS
    creds, all_state = load_creds(), load_state()
    rc = 0
    for path in files:
        art = parse_article(path)
        st = all_state.setdefault(art["slug"], {"site": art["site"]})
        print(f"\n=== {art['site']}/{art['slug']} — \"{art['title']}\""
              f"{'  [DRY RUN]' if dry else ''} ===")
        print(f"    canonical: {art['canonical_url']}")
        for ch in channels:
            try:
                if ch == "github":
                    msg = push_github(art, st, creds, dry)
                elif ch == "devto":
                    msg = push_devto(art, st, creds, dry, draft)
                elif ch == "telegram":
                    msg = push_telegram(art, st, creds, dry, force)
                else:
                    raise RuntimeError(f"unknown channel {ch}")
                print(f"  ✅ {ch:9} {msg}")
            except Exception as e:
                rc = 1
                print(f"  ❌ {ch:9} FAILED: {e}")
        if not dry:
            save_state(all_state)
    print("\nDone." if rc == 0 else "\nDone with errors (see ❌ above; rerun to retry those channels).")
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv))

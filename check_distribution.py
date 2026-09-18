#!/usr/bin/env python3
"""
Distribution check — is every public MrNasdog page mirrored, and is every mirror current?

WHY (Sep 18 2026): the release steps lived in four documents and nothing checked
them. Five coin articles went stale on GitHub + Dev.to after a hub rebuild, six
analysis articles and Case Study 001 were never mirrored, and nobody noticed for
weeks. A reminder in a doc cannot fix that; a check that fails loudly can.

WHAT COUNTS AS "PUBLIC": the live sitemap (https://mrnasdog.com/sitemap.xml) —
the same list Google and Bing are given — narrowed by distribution-policy.json
(eligible page types, pages left out on purpose). Nothing is maintained by hand,
so a new page shows up here the day it enters the sitemap, with or without a
Markdown mirror. A page with no mirror is a RED row, never a silent gap.

PER PAGE, it checks:
  origin     the live page answers 200 and declares itself canonical
  mirror     a Markdown file in crypto/ or growth/ carries that canonical_url
  fresh      the mirror is not older than the page (JSON-LD dateModified, else
             sitemap lastmod, compared with the mirror's last git commit)
  github     the public repo holds exactly the local file (blob sha)
  devto      the Dev.to article (by stored id) matches title/description/
             canonical/body of the local file
  telegram   INFORMATIONAL only — edit-in-place notice board, never a blocker

Read-only: no credentials, no sends. Adapted from Codex/Astra's audit
(ChatGPT Astra/experiments/distribution-audit-2026-09-18/audit_distribution.py).

USAGE
  python3 check_distribution.py                 # full check, write reports/
  python3 check_distribution.py --scope atom,dot  # print just these (still writes all)
Exit 0 = every required channel current · 2 = gaps · 3 = check incomplete.
"""
import argparse
import concurrent.futures
import hashlib
import html
import json
import os
import re
import ssl
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

try:
    import certifi
    CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    CTX = ssl.create_default_context()

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://mrnasdog.com"
REPO = "jeevansongmy-spec/mrnasdog-articles"
UA = {"User-Agent": "MrNasdog-DistributionCheck/1.0"}

sys.path.insert(0, HERE)
sys.dont_write_bytecode = True
from syndicate import parse_article  # noqa: E402  (pure function, no side effects)


def get(url, as_json=False):
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), context=CTX, timeout=40) as r:
                text = r.read().decode()
                return r.status, (json.loads(text) if as_json else text)
        except urllib.error.HTTPError as e:
            if e.code in (429, 502, 503, 504) and attempt < 3:
                time.sleep(min(float(e.headers.get("Retry-After") or 5), 30))
                continue
            return e.code, None
        except Exception:
            if attempt < 3:
                time.sleep(3)
                continue
            return None, None
    return None, None


def norm(s):
    return re.sub(r"\s+", " ", str(s or "")).strip()


def norm_body(s):
    return norm(re.sub(r"(?m)^```plaintext\s*$", "```", str(s or "")))


def blob_sha(path):
    data = open(path, "rb").read()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def last_commit_date(path):
    out = subprocess.run(["git", "-C", HERE, "log", "-1", "--format=%cs", "--", path],
                         capture_output=True, text=True).stdout.strip()
    return out or None


def plain(v):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", v))).strip()


# ── inventory ─────────────────────────────────────────────────────────────
def inventory(policy):
    status, xml = get(f"{SITE}/sitemap.xml")
    if status != 200:
        raise SystemExit(f"sitemap unreachable (HTTP {status})")
    pats = [re.compile(p) for p in policy["eligible_path_patterns"]]
    rows = []
    blocks = re.findall(r"<url>(.*?)</url>", xml, re.S)
    # Pages with no real date get the sitemap's BUILD time as lastmod (the same
    # instant as "/"). That says nothing about the page, so it is ignored.
    home = re.search(r"<lastmod>([^<]+)</lastmod>", blocks[0]) if blocks else None
    build_ts = home.group(1) if home else None
    for block in blocks:
        loc = re.search(r"<loc>([^<]+)</loc>", block).group(1).strip()
        lastmod = (re.search(r"<lastmod>([^<]+)</lastmod>", block) or [None, None])[1]
        if lastmod == build_ts:
            lastmod = None
        path = loc.replace(SITE, "") or "/"
        if not any(p.match(path) for p in pats):
            continue
        if path.endswith("/inflation"):
            kind = "coin"
        elif path.startswith("/research/"):
            kind = "methodology"
        else:
            kind = "case-study" if path.startswith("/case-studies/") else "analysis"
        slug = path.split("/")[2]
        row = {"kind": kind, "slug": slug, "path": path, "url": SITE + path,
               "sitemap_lastmod": lastmod[:10] if lastmod else None}
        if path in policy["excluded"]:
            continue  # left out on purpose — not shown, not counted
        rows.append(row)
    return rows


# ── evidence ──────────────────────────────────────────────────────────────
def fetch_origin(row):
    status, text = get(row["url"])
    text = text or ""
    canon = re.search(r'<link[^>]*rel="canonical"[^>]*href="([^"]+)"', text)
    title = re.search(r"<title>(.*?)</title>", text, re.S)
    mod = re.findall(r'"dateModified"\s*:\s*"([^"]+)"', text)
    return row["url"], {"status": status, "canonical": html.unescape(canon.group(1)) if canon else None,
                        "title": html.unescape(title.group(1)).strip() if title else None,
                        "date_modified": max(m[:10] for m in mod) if mod else None}


def collect(rows, state):
    ev = {"checked_at": datetime.now(timezone.utc).isoformat()}
    s, tree = get(f"https://api.github.com/repos/{REPO}/git/trees/main?recursive=1", as_json=True)
    ev["github_ok"] = s == 200
    ev["github"] = {x["path"]: x.get("sha") for x in (tree or {}).get("tree", [])}
    ids = sorted({v["devto_id"] for v in state.values() if v.get("devto_id")})

    def dev(i):
        st, data = get(f"https://dev.to/api/articles/{i}", as_json=True)
        time.sleep(0.4)
        return str(i), {"status": st, "data": data}
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        ev["devto"] = dict(pool.map(dev, ids))
    # Telegram public channel archive (informational)
    ev["telegram"], before, pages_ok = {}, None, True
    for _ in range(25):
        st, text = get("https://t.me/s/mrnasdog" + (f"?before={before}" if before else ""))
        if st != 200:
            pages_ok = False
            break
        chunks = re.split(r'data-post="mrnasdog/(\d+)"', text or "")
        seen = []
        for k in range(1, len(chunks), 2):
            mid, chunk = chunks[k], chunks[k + 1]
            body = re.search(r'<div class="tgme_widget_message_text[^>]*>(.*?)</div>', chunk, re.S)
            if body:
                ev["telegram"][mid] = {"text": plain(body.group(1)), "links": re.findall(r'href="([^"]+)"', body.group(1))}
            seen.append(int(mid))
        if not seen or min(seen) <= 1 or min(seen) == before:
            break
        before = min(seen)
    ev["telegram_ok"] = pages_ok
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        ev["origin"] = dict(pool.map(fetch_origin, rows))
    return ev


# ── assessment ────────────────────────────────────────────────────────────
def assess(rows, articles, state, ev, policy):
    by_canon = {}
    for a in articles:
        by_canon.setdefault(a["canonical_url"].rstrip("/"), []).append(a)
    out = []
    for row in rows:
        r = dict(row, issues=[])
        o = ev["origin"].get(row["url"], {})
        r["title"] = o.get("title")
        r["page_date"] = o.get("date_modified") or row.get("sitemap_lastmod")
        if o.get("status") != 200:
            r["issues"].append(f"origin HTTP {o.get('status')}")
        elif (o.get("canonical") or "").rstrip("/") != row["url"]:
            r["issues"].append("origin canonical differs")
        mirrors = by_canon.get(row["url"], [])
        if not mirrors:
            r.update(mirror=None, github="missing", devto="missing", telegram="none", fresh=None)
            r["issues"].append("no mirror — write the Markdown and syndicate")
            out.append(r)
            continue
        if len(mirrors) > 1:
            r["issues"].append("several mirrors share this canonical: " + ", ".join(os.path.relpath(m["path"], HERE) for m in mirrors))
        a = mirrors[0]
        rel = os.path.relpath(a["path"], HERE)
        r["mirror"] = rel
        r["mirror_date"] = last_commit_date(rel)
        # freshness: the mirror must not be older than the page
        r["fresh"] = not (r["page_date"] and r["mirror_date"] and r["mirror_date"] < r["page_date"])
        if not r["fresh"]:
            r["issues"].append(f"mirror older than page ({r['mirror_date']} < {r['page_date']})")
        # github
        if not ev["github_ok"]:
            r["github"] = "unchecked"
        else:
            r["github"] = "current" if ev["github"].get(rel) == blob_sha(a["path"]) else "differs"
            if r["github"] != "current":
                r["issues"].append("github copy differs from local file (commit + push)")
        # dev.to
        st = state.get(a["slug"], {})
        r["devto_id"] = st.get("devto_id")
        d = ev["devto"].get(str(st.get("devto_id")), {})
        data = d.get("data") or {}
        devto_off = row["path"] in policy.get("devto_unpublished_on_purpose", {}) or not a["published"]
        if devto_off:
            r["devto"] = "off on purpose"
        elif not st.get("devto_id"):
            r["devto"] = "missing"
            r["issues"].append("not on Dev.to")
        elif d.get("status") != 200:
            r["devto"] = "unchecked" if d.get("status") in (None, 429, 500, 502, 503) else f"HTTP {d.get('status')}"
            if r["devto"] != "unchecked":
                r["issues"].append(f"Dev.to {r['devto']}")
        else:
            bad = [k for k, v in (("title", a["title"]), ("description", a["description"]),
                                  ("canonical_url", a["canonical_url"])) if norm(v) != norm(data.get(k))]
            if norm_body(a["body"]) != norm_body(data.get("body_markdown")):
                bad.append("body")
            r["devto"] = "current" if not bad else "differs: " + ",".join(bad)
            r["devto_url"] = data.get("url")
            r["devto_edited"] = (data.get("edited_at") or data.get("published_at") or "")[:10] or None
            if bad:
                r["issues"].append("Dev.to differs from local file (" + ",".join(bad) + ")")
        # telegram (informational)
        mid = st.get("telegram_message_id")
        m = ev["telegram"].get(str(mid)) if mid else None
        if not mid:
            r["telegram"] = "none"
        elif not m:
            r["telegram"] = "unchecked" if not ev["telegram_ok"] else "not found"
        else:
            r["telegram"] = "current" if norm(a["title"]) in m["text"] and a["canonical_url"] in m["links"] else "old text"
        r["telegram_id"] = mid
        out.append(r)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--scope", help="comma-separated slugs to print (report still covers everything)")
    ap.add_argument("--out", default=os.path.join(HERE, "reports"))
    args = ap.parse_args()
    policy = json.load(open(os.path.join(HERE, "distribution-policy.json")))
    state = json.load(open(os.path.join(HERE, ".pipeline-state.json")))
    articles = [parse_article(os.path.join(HERE, f, n)) for f in ("crypto", "growth")
                for n in sorted(os.listdir(os.path.join(HERE, f))) if n.endswith(".md")]
    rows = inventory(policy)
    ev = collect(rows, state)
    res = assess(rows, articles, state, ev, policy)
    canon_set = {r["url"] for r in res} | set(policy["excluded"])
    orphans = sorted(os.path.relpath(a["path"], HERE) for a in articles
                     if a["canonical_url"].startswith(SITE) and a["canonical_url"].rstrip("/") not in {SITE + p for p in policy["excluded"]} | canon_set)
    incomplete = not ev["github_ok"] or any(r.get("devto") == "unchecked" for r in res)
    gaps = [r for r in res if r["issues"]]
    summary = {
        "checked_at": ev["checked_at"], "pages": len(res), "ok": len(res) - len(gaps), "gaps": len(gaps),
        "by_kind": {k: {"pages": sum(1 for r in res if r["kind"] == k),
                        "gaps": sum(1 for r in res if r["kind"] == k and r["issues"])}
                    for k in ("coin", "methodology", "analysis", "case-study")},
        "check_incomplete": incomplete,
        "orphan_mirrors": orphans,
        "excluded_on_purpose": policy["excluded"],
    }
    os.makedirs(args.out, exist_ok=True)
    report = {"summary": summary, "rows": sorted(res, key=lambda r: (not r["issues"], r["kind"], r["slug"]))}
    with open(os.path.join(args.out, "distribution.json"), "w") as f:
        json.dump(report, f, indent=1, ensure_ascii=False)
        f.write("\n")
    scope = set(args.scope.split(",")) if args.scope else None
    show = [r for r in report["rows"] if (r["slug"] in scope if scope else r["issues"])]
    print(json.dumps(summary, indent=1, ensure_ascii=False))
    for r in show:
        print(f"{'✅' if not r['issues'] else '❌'} {r['kind']:10} {r['slug']:34} github={r.get('github')} devto={r.get('devto')} tg={r.get('telegram')}  {'; '.join(r['issues'])}")
    return 3 if incomplete else (2 if gaps else 0)


if __name__ == "__main__":
    raise SystemExit(main())

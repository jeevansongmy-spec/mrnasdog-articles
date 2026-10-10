#!/usr/bin/env python3
"""
mirror_coin_hubs.py — Coin Hub Pipeline v2 (his OK Oct 11 2026): every live coin has TWO GitHub files.
  crypto/<slug>-coin-research.md     the MAIN one — the whole public coin page (§0.45–§0.49), canonical → /research/<slug>
  crypto/<slug>-pressure-framework.md the §0.46 inflation analysis (unchanged job), with a link to the main page on top
The coin file is the live text version https://mrnasdog.com/research/<slug>.md, written by the SAME converter as the page
(mrnasdog/lib/coin-public.ts) — so its numbers always match, and its words already drift per coin (his rule: not robotic).

  python3 mirror_coin_hubs.py [--coins arb,xrp,…] [--all-changed] [--dry-run] [--no-telegram]

  --coins        only these slugs (the nightly run: tonight's rebuilt coins)
  (default)      every live coin (lib/live-coin-list.json) — the 4-day refresh; only CHANGED files are committed
Per run: write files → guards (members-only text, canonical, H1) → ONE git commit + push → per-file GitHub receipts in
.pipeline-state.json → ONE Telegram receipt post (his proof a send went out). Never one post per coin.
"""
import hashlib, json, os, re, subprocess, sys, urllib.request
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://mrnasdog.com"
LIVE = os.path.expanduser("~/Documents/claude-code/mrnasdog/lib/live-coin-list.json")
sys.path.insert(0, HERE)
import syndicate  # noqa: E402  (creds, state, http helpers)

# members-only §0.47 values must never leave the site (handover-ecosystem-detail: the gated-score leak, Aug 31 2026)
PAID = re.compile(r"narrative [0-9.]+/3|business model [0-9.]+/2|spiral [0-9.]+/2", re.I)
Q_START, Q_END = "<!-- questions:start -->", "<!-- questions:end -->"
MAIN_MARK = "<!-- main-page -->"
# the line at the top of each §0.46 file — several shapes, picked per coin (not robotic)
MAIN_LINES = [
    "**Main page:** the full {sym} coin page — signal, price drivers and the buy/sell questions → [{host}]({url})",
    "➜ Start with the {name} coin page for the short answer (should you buy {sym}?) and its price drivers: [{host}]({url})",
    "This is the long supply read. For the signal, the price drivers and the questions people ask about {name}, see [{host}]({url}).",
    "Looking for the buy-or-sell answer? It is on the {sym} coin page, with demand and price drivers: [{host}]({url})",
    "The {name} coin page has the score, the price drivers and every question answered — [{host}]({url}). Below: supply, line by line.",
]


def hsh(s):
    h = 2166136261
    for ch in s:
        h = ((h ^ ord(ch)) * 16777619) & 0xFFFFFFFF
    return h


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "MrNasdog-mirror/1.0"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.status, r.read().decode("utf-8", "replace")


def git_differs(rel):
    """new or modified compared with the last commit"""
    out = subprocess.run(["git", "-C", HERE, "status", "--porcelain", "--", rel], capture_output=True, text=True).stdout
    return bool(out.strip())


def plain(md):
    return re.sub(r"\s+", " ", re.sub(r"[*_`#>\[\]]|\(https?://[^)]+\)", "", md)).strip()


def hub_file(slug, sym, name):
    status, md = get(f"{SITE}/research/{slug}.md")
    if status != 200 or not md.startswith("# "):
        raise RuntimeError(f"text version not ready (HTTP {status})")
    if PAID.search(md):
        raise RuntimeError("members-only value found — not sent")
    title = md.split("\n", 1)[0][2:].strip()
    paras = [p for p in md.split("\n\n")[1:] if p.strip() and not p.startswith(("*", "-", "#", "|"))]
    desc = plain(paras[0])[:240] if paras else title
    fm = "\n".join([
        "---",
        f"title:         {json.dumps(title, ensure_ascii=False)}",
        f"description:   {json.dumps(desc, ensure_ascii=False)}",
        f"canonical_url: \"{SITE}/research/{slug}\"",
        "content_type:  \"coin_hub\"",
        f"tags:          {json.dumps(['crypto', sym.lower(), re.sub(r'[^a-z0-9]', '', name.lower())[:20] or sym.lower(), 'should-i-buy'])}",
        "published:     true",
        "---",
        "",
    ])
    return fm + md


def fix_inflation_file(path, slug, sym, name):
    """§0.46 file: take the old question block out (it lives in the coin file now) and put the main-page line on top."""
    raw = open(path).read()
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", raw, re.S)
    if not m:
        return False
    fm, body = m.group(1), m.group(2)
    if Q_START in body:  # undo mirror_questions.py (Oct 10 2026): block out, the old H1 back
        body = re.sub(re.escape(Q_START) + r".*?" + re.escape(Q_END) + r"\n*", "", body, count=1, flags=re.S)
        part1 = re.search(r"^## Part 1 · Supply: (.*)$", body, re.M)
        if part1:
            old = part1.group(1).strip()
            body = re.sub(r"^# .*$\n*", "", body, count=1, flags=re.M)
            body = body.replace(part1.group(0), f"# {old}", 1)
            fm = re.sub(r"^title:.*$", lambda _: "title:         " + json.dumps(old, ensure_ascii=False), fm, count=1, flags=re.M)
    url = f"{SITE}/research/{slug}"
    line = MAIN_LINES[hsh(slug) % len(MAIN_LINES)].format(sym=sym, name=name, url=url, host=url.replace("https://", ""))
    block = f"{MAIN_MARK}\n{line}\n"
    if MAIN_MARK in body:
        body = re.sub(re.escape(MAIN_MARK) + r"\n[^\n]*\n", lambda _: block, body, count=1)
    else:
        orig = re.search(r"^(\*Originally published at .*\*|> Originally published at .*)$", body, re.M)
        h1 = re.search(r"^# .*$", body, re.M)
        at = orig.end() if orig else (h1.end() if h1 else 0)
        body = body[:at] + "\n\n" + block + "\n" + body[at:].lstrip("\n")
    new = f"---\n{fm}\n---\n{body}"
    if new != raw:
        open(path, "w").write(new)
        return True
    return False


def main(argv):
    dry = "--dry-run" in argv
    tele = "--no-telegram" not in argv
    live = json.load(open(LIVE))["live"]
    meta = {}
    src = open(os.path.expanduser("~/Documents/claude-code/mrnasdog/lib/pressure-dashboard.ts")).read()
    for slug, sym, name in re.findall(r'slug: "([a-z0-9-]+)", symbol: "([A-Za-z0-9]+)", name: "([^"]+)"', src):
        meta[slug] = (sym, name)
    slugs = [c["slug"] for c in live]
    if "--coins" in argv:
        want = [x.strip().lower() for x in argv[argv.index("--coins") + 1].split(",")]
        slugs = [s for s in slugs if s in want]
    changed, failed = [], []
    for slug in slugs:
        sym, name = meta.get(slug, (slug.upper(), slug))
        rel_hub = f"crypto/{slug}-coin-research.md"
        try:
            text = hub_file(slug, sym, name)
            p = os.path.join(HERE, rel_hub)
            if not os.path.exists(p) or open(p).read() != text:
                if not dry:
                    open(p, "w").write(text)
            if dry or git_differs(rel_hub):  # compared with git, so a crashed earlier run is picked up too
                changed.append(rel_hub)
        except Exception as e:
            failed.append(f"{slug}: {e}")
            continue
        inf = os.path.join(HERE, f"crypto/{slug}-pressure-framework.md")
        if os.path.exists(inf) and not dry:
            fix_inflation_file(inf, slug, sym, name)
            if git_differs(f"crypto/{slug}-pressure-framework.md"):
                changed.append(f"crypto/{slug}-pressure-framework.md")
    print(f"{len(slugs)} coins · {len(changed)} files changed · {len(failed)} failed")
    for f in failed:
        print("  ❌", f)
    if dry or not changed:
        return 1 if failed else 0

    # ONE commit + push for the whole batch (never one per file)
    subprocess.run(["git", "-C", HERE, "add", "--", *changed], check=True)
    n_hubs = sum(1 for c in changed if c.endswith("-coin-research.md"))
    msg = f"coin hubs: {n_hubs} coin pages + {len(changed) - n_hubs} §0.46 links ({datetime.now(timezone.utc).strftime('%Y-%m-%d')})"
    subprocess.run(["git", "-C", HERE, "commit", "-q", "-m", msg, "--", *changed], check=True)
    if subprocess.run(["git", "-C", HERE, "push", "-q"]).returncode != 0:
        subprocess.run(["git", "-C", HERE, "pull", "-q", "--rebase", "--autostash"], check=True)
        subprocess.run(["git", "-C", HERE, "push", "-q"], check=True)
    print(f"✅ github  one commit: {msg}")

    # receipts per file (check_distribution reads GitHub itself; this is the record)
    state = syndicate.load_state()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    for rel in changed:
        st = state.setdefault(os.path.splitext(os.path.basename(rel))[0], {"site": "mrnasdog.com"})
        st["github_url"] = f"https://github.com/jeevansongmy-spec/mrnasdog-articles/blob/main/{rel}"
        st.setdefault("receipts", {})["github"] = {"at": now, "sha256": hashlib.sha256(open(os.path.join(HERE, rel), "rb").read()).hexdigest()[:16], "ok": True, "note": "batch commit"}
    syndicate.save_state(state)

    if tele and n_hubs:
        creds = syndicate.load_creds()
        tok, chan = creds.get("TELEGRAM_BOT_TOKEN"), creds.get("TELEGRAM_CHANNEL", "@mrnasdog")
        hubs = [c.split("/")[1].replace("-coin-research.md", "") for c in changed if c.endswith("-coin-research.md")]
        names = ", ".join(meta.get(s, (s.upper(),))[0] for s in hubs[:40]) + (f" + {len(hubs) - 40} more" if len(hubs) > 40 else "")
        text = (f"<b>Coin pages updated: {len(hubs)}</b>\n\n{syndicate._esc(names)}\n\n"
                f"Should you buy, sell or wait? Each page answers it by supply and demand, with price drivers and the questions people ask.\n\n"
                f"🔗 <a href=\"{SITE}/coins\">All coins</a> · <a href=\"https://jeevansongmy-spec.github.io/mrnasdog-articles/\">GitHub copies</a>")
        status, resp = syndicate.http("POST", f"https://api.telegram.org/bot{tok}/sendMessage", {"Content-Type": "application/json"},
                                      {"chat_id": chan, "text": text, "parse_mode": "HTML", "disable_web_page_preview": True})
        print("✅ telegram one receipt post" if resp.get("ok") else f"⚠️ telegram: {status} {str(resp)[:150]}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

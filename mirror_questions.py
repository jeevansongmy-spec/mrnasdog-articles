#!/usr/bin/env python3
"""
mirror_questions.py — SEO plan v5 (his approval Oct 10 2026): a coin's GitHub mirror carries the same buy/sell questions
as its coin page. For each named crypto/<x>-pressure-framework.md it:
  1. reads the LIVE coin page https://mrnasdog.com/research/<slug> (FAQPage JSON-LD = the Question Engine answers, built
     from the page data, so they are dated and differ on every coin — never typed by hand here),
  2. sets the title (front matter + H1) to the coin's own buy question + "Supply, Demand and Price Drivers (<Month YYYY>)",
  3. puts the answers (Part 2 demand + Part 3 price drivers, with the supply numbers) between the markers below, ONE
     disclaimer line at the end, and keeps the old supply analysis as "Part 1 · Supply".
Idempotent: a second run only refreshes the block and title. The nightly coin run regenerates mirrors from the
/inflation page — run this on those files BEFORE syndicate.py (docs/handover-coin-page-routine.md step 8).

  python3 mirror_questions.py crypto/xrp-pressure-framework.md [more files…]   (then syndicate.py the same files)
"""
import html, json, re, sys, urllib.request

START, END = "<!-- questions:start -->", "<!-- questions:end -->"
NOTE = "Every answer here applies basic economic theory — the law of supply and demand — to this coin's data. It is not financial advice."
SKIP = ("How does MrNasdog judge", "alerts cover?")  # shared help items, not coin answers
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
SHORT = [m[:3] for m in MONTHS]


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "mrnasdog-mirror/1.0"})
    return urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")


def faq(page):
    for block in re.findall(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', page, re.S):
        try:
            data = json.loads(block)
        except ValueError:
            continue
        for d in data if isinstance(data, list) else [data]:
            if d.get("@type") == "FAQPage":
                return [(html.unescape(e["name"]), html.unescape(e["acceptedAnswer"]["text"])) for e in d["mainEntity"]]
    return []


def build(path):
    raw = open(path).read()
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", raw, re.S)
    if not m:
        raise ValueError(f"{path}: no front matter")
    fm, body = m.group(1), m.group(2)
    canon = re.search(r'^canonical_url:\s*"?([^"\n]+)"?', fm, re.M).group(1).strip()
    cm = re.match(r"https://mrnasdog\.com/research/([^/]+)/inflation/?$", canon)
    if not cm:
        raise ValueError(f"{path}: canonical {canon} is not a coin inflation page")
    coin_url = f"https://mrnasdog.com/research/{cm.group(1)}"
    items = [(q, a) for q, a in faq(fetch(coin_url)) if not any(s in q for s in SKIP)]
    if len(items) < 4:
        raise ValueError(f"{path}: only {len(items)} answers on {coin_url} — page not on the Question Engine yet")
    dated = re.search(r"\((%s) (\d{1,2}) (\d{4})" % "|".join(SHORT), " ".join(a for _, a in items))
    if not dated:
        raise ValueError(f"{path}: no dated answer on {coin_url}")
    mon, day, year = dated.groups()
    title = f"{items[0][0]} Supply, Demand and Price Drivers ({MONTHS[SHORT.index(mon)]} {year})"

    lines = [START, "",
             f"Updated {mon} {day} {year} from the live page: [{coin_url.replace('https://', '')}]({coin_url}).", "",
             "## The buy and sell questions: supply, demand and price drivers", ""]
    for q, a in items:
        a = a.replace(NOTE, "").replace(NOTE.split(" It is")[0], "").strip()
        a = re.sub(r"(?<=[.)]) (?:• ?)?([▲▼]) ", r"\n- \1 ", re.sub(r"(?<=[.)]) • ?", "\n- ", a))  # driver list → bullets
        lines += [f"### {q}", "", a, ""]
    lines += [f"*{NOTE}*", "", END]
    block = "\n".join(lines)

    if START in body:  # refresh
        body = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, body, count=1, flags=re.S)
        body = re.sub(r"^# .*$", lambda _: f"# {title}", body, count=1, flags=re.M)
    else:  # first time: new H1 + block, the old H1 becomes Part 1
        h1 = re.search(r"^# (.*)$", body, re.M)
        if not h1:
            raise ValueError(f"{path}: no H1")
        body = body[:h1.start()] + f"# {title}\n\n{block}\n\n## Part 1 · Supply: {h1.group(1)}" + body[h1.end():]
    fm = re.sub(r"^title:.*$", lambda _: "title: " + json.dumps(title, ensure_ascii=False), fm, count=1, flags=re.M)
    open(path, "w").write(f"---\n{fm}\n---\n{body}")
    return title, len(items)


if __name__ == "__main__":
    files = sys.argv[1:]
    if not files:
        print(__doc__)
        sys.exit(1)
    rc = 0
    for f in files:
        try:
            t, n = build(f)
            print(f"ok  {f}: {n} answers · {t}")
        except Exception as e:  # one bad page never stops the rest
            print(f"ERR {f}: {e}")
            rc = 1
    sys.exit(rc)

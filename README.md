# MrNasdog — Articles

Public mirror + syndication source for articles by **MrNasdog** (Zhiyi Song).

Every article here is a copy whose **canonical link points back to the original**
on [mrnasdog.com](https://mrnasdog.com) (crypto research) or
[mrnasdoggrowth.com](https://mrnasdoggrowth.com) (thinking & growth). The original
site is always the source of truth; this repo is a distribution surface.

## Layout
- `crypto/` — articles originating on mrnasdog.com
- `growth/` — articles originating on mrnasdoggrowth.com
- `syndicate.py` — the one-command syndication pipeline
- `.pipeline-state.json` — per-article publish state (Dev.to id, Telegram msg id)

## Pipeline
One command fans an article out to **GitHub (this repo) + Dev.to + Telegram (@mrnasdog)**:

```bash
python3 syndicate.py growth/the-quiet-strategy.md          # publish everywhere
python3 syndicate.py --dry-run growth/the-quiet-strategy.md # preview, send nothing
```

Each channel is best-effort and independent — if one fails the others still go,
and re-running updates instead of duplicating. Credentials come from
`~/.claude-creds/mrnasdog.env` (Dev.to key, Telegram bot token) and the local
GitHub auth; **no secrets live in this repo.**

See the front-matter contract at the top of `syndicate.py`.

---
title: "Your AI Coin Watcher: One Copy-Paste, Then It Checks Every Day"
description: "Members can plug my crypto supply research into their own AI. Copy one instruction from your profile, paste it into Claude or ChatGPT, and it checks your coins every morning — telling you only when a number actually moves."
canonical_url: "https://mrnasdog.com/analysis/ai-coin-watcher"
tags: ["api", "ai", "crypto", "webdev"]
published: true
---

> Originally published at **[mrnasdog.com/analysis/ai-coin-watcher](https://mrnasdog.com/analysis/ai-coin-watcher)** by MrNasdog.

I opened my research to your own AI. Copy one instruction from your profile, paste it into Claude or ChatGPT, and it watches your coins every morning.

## What this is

Every coin I research has one number I care about most: **how much new supply is coming in the next 90 days.** When that number moves, something real happened — an unlock, a burn, an emission change, a governance vote.

Until now you had two ways to hear about it: visit the coin page, or wait for a [coin alert](https://mrnasdog.com/analysis/coin-alerts) email. Both work. Both are me talking to you on my schedule.

This is the third way, and it's different: **your own AI can now read my numbers directly.** You give it one instruction once. Every morning it checks your coins, and if something moved, it goes and finds out why — then hands you a short briefing in your own chat.

**You don't need to be a developer.** There is no code to write. It is one button and one paste.

## How to set it up (about 30 seconds)

1. **Step 1** — log in and open your [Profile](https://mrnasdog.com/profile). Find the card called **"Your AI coin watcher"**.
2. **Step 2** — under **Your setup**, type the coins you want watched (`btc, eth, sol` — as many as you like), and press **Generate my API key** once.
3. **Step 3** — press the big amber **"Copy my daily watcher instruction"** button, and paste it into your AI.

**Claude** — paste it into the Claude desktop app and say *"run this as a daily scheduled task every morning."*

**ChatGPT** — paste it into a new *scheduled Task*, set to daily.

That's the whole setup. Change your coin list later? Just re-copy the instruction and paste it in again.

## What you get back

**On a quiet day — almost every day — one line:**

```
No changes in your coins today.
```

**On a day something moved**, your AI takes the new number, goes and searches the news itself, and writes you the reason:

> **SUI — next 90 days: 4.1% → 5.6%**
>
> A scheduled investor unlock lands next month, adding tokens the earlier read didn't cover. Staking rewards are unchanged, so the whole move is the unlock. Worth checking whether the market has already priced it in.
>
> *Example only — a shape, not a real reading.*

The important part is what it **doesn't** send. **Silence means nothing moved.** No daily digest of nothing, no dashboard to check, no habit to build.

## Who gets it

| Tier | What you get |
|---|---|
| Free | Every number stays readable on the coin pages — and free coin-alert emails |
| Member | A key, and the watcher — 100 checks a day |
| Founding Member | A key, and the watcher — 100 checks a day |

The pages stay open to everyone — that never changes. The key is the members-only part. [See the plans →](https://mrnasdog.com/membership)

## If you write code

The watcher is just a friendly wrapper around a plain JSON API. If you'd rather call it yourself, it's in the same card under **"For developers"**:

- `GET /api/v1/inflation` — every coin I research. Narrow it with `?coins=sol,trx` or `?changed_within=1d`.
- `GET /api/v1/inflation/{coin}` — one coin.
- Auth with `Authorization: Bearer <key>`. 100 calls a day. A watcher needs one.
- **My promise on v1:** I will add fields, never rename or remove them. Anything you build today keeps working.

## Two honest notes

**This is a beta,** and I'm calling it one on purpose. I use it myself every morning — that's how it got built — but you're early, and early things have rough edges. If yours behaves strangely, tell me and I'll fix it.

**Your key is private.** It sits inside the instruction you copy, so paste that into your own AI and nowhere else — not a public chat, not a shared document. If it ever gets out, press **Regenerate** in your profile and the old key dies instantly.

And the number itself is **my researched reading, not a live market feed** — it moves when I find something that changes the supply outlook. Your AI tells you *that it moved*; the coin page tells you *what I think about it*.

---

*My own research and opinion. Not financial advice.*

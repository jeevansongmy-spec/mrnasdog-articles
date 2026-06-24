---
title: "CC Inflation Analysis · June 2026 · Mint still ahead of the burn"
description: "A MrNasdog Pressure Framework read of Canton Coin (CC): a ~1.59B / 90D minting reward vs a ~785M fee burn. Framework +2.1% net, matching the supply monitor; uncapped burn-and-mint, no vesting."
canonical_url: "https://mrnasdog.com/research/cc/inflation"
tags: ["crypto", "cc", "canton", "rwa"]
published: true
---

> Originally published at **[mrnasdog.com/research/cc/inflation](https://mrnasdog.com/research/cc/inflation)** by MrNasdog.

Canton Coin is an **uncapped burn-and-mint token**: the Canton Network mints about **1.59B CC** over 90 days to reward network activity, while transaction fees burn roughly **785M CC** back out. The mint still outruns the burn, so the framework reads about **+2.1% net** — matching our supply monitor's **+2.11%** read of the same window. Canton Coin is **structurally inflationary on the active float** for now, with the burn rising toward the mint as institutional usage scales.

## The verdict, in one paragraph

For the 90-day window ending June 25 2026, the MrNasdog Pressure Framework reads **CC at +2.1% net** on the forward view, driven by a minting reward that out-issues the fee burn. The gross mint runs near **1.59B CC** over 90 days against a fee burn of about **785M CC**, leaving roughly **+805M CC** of net new supply on a **~38.9B** circulating base. Our independent supply monitor reads the same window at **+2.11%**, a gap of just **0.04 percentage points** — well inside tolerance, so no monitor-gap flag ships and the primary read is confirmed. Canton Coin is **structurally inflationary on the active float**, at a low-single-digit pace that the burn is steadily eating into.

## Sell pressure: where new CC comes from

Sell #1 — protocol inflation — is the whole sell side, at about **1.59B CC** over the next 90 days. The Canton Network mints fresh CC in discrete rounds roughly every ten minutes and pays it to the participants who do real work: application providers, who now take about **62%** of the reward pool, and Super Validators, who take around **20%** and decline gradually toward mid-2029. The minting follows a front-loaded curve issuing close to **100B CC** over its first ten years before settling to a flat ~2.5B a year. Two 2026 changes already trimmed the mint: a **mid-January 2026 halving** (around block 78,840) cut issuance per round in half and dropped the Super Validator share from 48% to 20%, and **CIP-0096** set validator liveness rewards to **zero on Apr 30 2026**, so node uptime no longer mints CC — only real usage does. This is a minting reward, not a sale: every coin is issued in exchange for measured activity.

Sell #2 — vesting unlocks — is **zero**, and structurally so. Canton Coin had a fair launch with no pre-mine, no venture token allocation and no team or seed schedule, so there is no cliff to unlock and nothing waiting to vest. Sell #3 — Foundation and unscheduled unlocks — is also zero: because there was no token sale, there is no foundation stockpile to release; supply enters only through the minting reward, and there is no dated discretionary release in the window. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate or court distribution applies to Canton Coin.

## Buy pressure: where new CC goes

Buy #2 — protocol fee burn — is the only active offset, at about **785M CC** over 90 days. Every fee on Canton's Global Synchronizer is paid in CC and permanently burned, so usage directly destroys supply. The burn is accelerating: more than **1B CC** has been burned cumulatively, the burned value crossed a **$417M** milestone in April 2026, and the recent run-rate near **$1M of fees a day** implies roughly 785M CC destroyed over a 90-day window. That burn is real and rising, but it still trails the mint, so it slows dilution rather than reversing it.

Buy #1 — programmatic buyback — is **zero**: there is no treasury buying CC on the open market, because the model removes supply through the fee burn instead. Buy #3 — Foundation buy — is zero, with no discretionary open-market buying. Buy #4 — new long-term lock — is also zero: a new Super Validator locking option (**CIP-0105**, approved Mar 2 2026) lets validators voluntarily lock earned rewards to keep their governance weight, but it is voluntary and carries no fixed escrow quantum, so the framework books no new long-term lock in the window. The entire buy side is the fee burn.

## Foundation and overhang

Canton Coin has no classic overhang to track — there is no pre-mine, no investor token allocation, and no foundation treasury funded by a sale, so there is no stockpile that could dump on the market. The institutional names attached to Canton — Goldman Sachs, HSBC, BNY Mellon, Tradeweb, Nasdaq — backed the company Digital Asset in equity rounds, not CC token allocations, so they create no token unlock overhang. The only continuous supply force is the minting reward itself, which is paid out for activity rather than held in reserve, and the new voluntary SV locking under CIP-0105 actually pulls some earned CC out of immediate circulation rather than adding to it. Because the token is fully earned into circulation, the framework books no discretionary release beyond protocol inflation and watches the burn reports and minting schedule on a roughly bi-weekly walk. If a future disclosure reveals a controlled balance that begins to release, that outflow would enter Sell #3 at the next refresh — but as of this window there is nothing of that kind to surface.

## How CC compares to other uncapped burn-and-mint chains

CC belongs to the class of **uncapped burn-and-mint tokens** — the same structural family as Ethereum after EIP-1559 or Solana, where new issuance and a usage-driven burn pull in opposite directions and net supply tracks activity. Unlike a hard-capped, halving-model coin, Canton Coin has no ceiling; unlike a pure inflation chain, it pairs the mint with a fee burn that scales with real network use. The result is a supply curve that bends toward equilibrium: the mint is front-loaded and steps down over a decade toward a flat ~2.5B a year, while the burn climbs with institutional throughput.

The contrast worth drawing is with fixed-supply tokens and with chains that have already crossed into net-deflationary. Canton Coin is neither yet: it is still early in its emission schedule, so the mint dominates and net supply grows at a low-single-digit pace. The bullish structural case is that the burn is designed to catch the mint as usage compounds — and the 2026 changes push that way, since the January halving and the end of validator liveness rewards both shrink the mint while the fee burn keeps climbing. At the point the two cross, CC would flip from mildly inflationary to roughly flat or net-deflationary. For an inflation lens today, though, CC reads as steadily, mildly inflationary, with the burn acting as a partial brake rather than a full offset.

## What to watch in the next 90 days

Watch the daily burn run-rate — the single number that decides whether net inflation keeps easing toward equilibrium; a sustained move above the recent ~$1M-a-day pace would close the gap with the mint quickly. Watch the next minting step-down as the front-loaded curve ages and the full effect of the April 30 2026 end of validator liveness rewards feeds through. Watch how much earned CC Super Validators lock under CIP-0105, since voluntary locking quietly removes coins from the active float. Watch institutional adoption announcements, since every new settlement flow on Canton burns CC directly. And expect the framework to re-run its realized-vs-forward end-check at each refresh against the supply monitor, which now carries a usable Canton Coin history.

## Summary

Canton Coin is an uncapped burn-and-mint utility token whose supply grows on a front-loaded minting schedule and shrinks through a usage-driven fee burn. The network mints about 1.59B CC over 90 days to reward activity, while fees burn roughly 785M CC back out, leaving the framework at about +2.1% net on a ~38.9B base — in line with the supply monitor's +2.11% read. There is no vesting, no foundation stockpile and no buyback — the entire buy side is the fee burn, and the entire sell side is the minting reward. CC stays mildly inflationary on the active float for now, with a January halving, the end of validator liveness rewards, and a rising fee burn all pushing it toward the equilibrium the model is built for.

---

*MrNasdog Pressure Framework analysis of Canton Coin (CC), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 25, 2026.*

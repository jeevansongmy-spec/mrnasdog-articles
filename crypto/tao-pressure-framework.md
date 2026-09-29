---
title: "TAO Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description: "TAO supply is growing: 324K TAO of block rewards plus a one-time 172K mint, less 6.8K recycled, gives +4.31% in 90 days and about +2.77% next. 21M cap."
canonical_url: "https://mrnasdog.com/research/tao/inflation"
tags: ["crypto", "tao", "bittensor", "ai"]
published: true
---

> Originally published at **[mrnasdog.com/research/tao/inflation](https://mrnasdog.com/research/tao/inflation)** by MrNasdog.

# TAO Inflation Analysis · September 2026 · Supply growing · projected to keep growing

Bittensor's TAO supply is growing. In the 90 days to Sep 29 2026 the Bittensor chain created **495,691 TAO** — **323,690 TAO** of ordinary block rewards plus a one-time mint of **172,001 TAO** on Sep 15 2026 — and recycled **6,834 TAO** back out of supply, for a net rise of **+4.31%**. With the one-time mint gone, the next 90 days point to about **+2.77%**. TAO is capped at 21M and halves by issued supply, but only about 54% of that cap is mined, so the block reward still dominates.

## The verdict, in one paragraph

The MrNasdog Pressure Framework reads TAO at **+4.31%** net supply growth over the last 90 days and **+2.77%** for the next 90 days, measured on a circulating base of **11.34M TAO**. Our monitor reads **+18.14%**, a gap of **13.83 percentage points**, so the ⚠ monitor-gap note ships on the coin page. The gap is not new TAO: the public supply figure the monitor divides sat at about 9.60M TAO — the chain's own count on Aug 5 2025 — until Sep 14 2026, then jumped about 1.75M TAO in one day on Sep 15 2026 to catch up with coins issued long before this window. On the chain itself, issued supply rose from 11.07M to 11.56M TAO between Jul 1 and Sep 29 2026, which is exactly our ledger. TAO is a steadily inflating, Bitcoin-shaped supply with one unusual quarter: a one-time mint on top of the halved block reward.

## Sell pressure: where new TAO comes from

Protocol inflation is the main source. Every Bittensor block, roughly every 12 seconds, mints **0.5 TAO** and sends it into the subnets, where it rewards miners, validators and stakers. The chain produced 647,379 blocks in the window, so block rewards created **323,690 TAO**, about 3,600 a day. The reward was halved from 1 TAO to 0.5 TAO in December 2025 when issued supply passed 10.5M TAO, and the next halving waits until 15.75M TAO have been issued — about 4.19M TAO away, years from now. The next 90 days therefore run at the same pace: another **323,690 TAO**.

The second source is a one-time event. On Sep 15 2026 a Bittensor network upgrade minted **172,001 TAO** in a single block into the root staking pool. For months, stakers on root had been credited rewards on paper without the matching TAO being moved into the pool, so the pool held less than it owed and exits could stall. The upgrade minted the missing TAO to close that hole. It runs only once and cannot repeat, so it counts in the last 90 days and adds nothing to the next.

Vesting unlocks are zero. TAO had a fair launch in 2021 with no presale, no team share and no investor share, so there is no vesting schedule and no cliff. Foundation and unscheduled unlocks are also zero: there is no foundation reserve to release, only a small Opentensor Foundation wallet. Nothing is locked long-term and no bankruptcy estate holds TAO.

## Buy pressure: where new TAO goes

Bittensor has no burn address and no buyback. Instead it recycles: transaction fees, the cost of registering on a subnet and the leftovers of closed subnets are taken out of issued supply and returned to the pool of TAO not yet mined. That removed **6,834 TAO** this window, about 76 a day, and much of it arrived in lumps when subnets closed. Transaction fees only began to be recycled on Aug 12 2026; since then the pace has been about **9,311 TAO** per 90 days, which is the figure the next 90 days use. A later upgrade on Sep 18 2026 halved transaction fees, but the ten days since are too short to show a new pace. Recycled TAO is not destroyed forever — it can be mined again later — so its real effect is to push the next halving a little further out.

The other buy rows are zero. No programmatic buyback buys TAO; some subnets buy back their own subnet tokens, which is a different asset. No foundation buys TAO for the project. And staking is not a lock: about 7.45M TAO is staked, but staked TAO still counts as circulating and can be withdrawn, so a bigger stake removes nothing from the float.

## Foundation and overhang

TAO has no team-held reserve, so the overhang is small and mostly made of protocol balances that already count as circulating. The Opentensor Foundation's own wallet held about **625 TAO** at the end of the window, up from about 524. Subnet owners have about **31,444 TAO** locked as the price of their subnet slots, and the subnets' trading pools hold about **7.45M TAO** that anyone selling a subnet token can draw out. All of these are read from the chain on every rebuild. Because every one of them already sits inside the circulating count, moving them adds no new supply — but if the Foundation wallet's balance falls between refreshes, that outflow enters the Foundation row at the next refresh.

## How TAO compares to other capped, halving chains

TAO is often called the Bitcoin of AI, and its supply design earns the comparison: a 21M cap, no premine, and a block reward that halves. The difference is the trigger. Bitcoin halves on a block count, every 210,000 blocks, and now pays 3.125 BTC per block, about 0.8% of its supply a year. TAO halves on issued supply, and because Bittensor recycles fees and registration costs back into unmined supply, each recycled coin delays the next TAO halving. Bitcoin has no such loop — its fees go to miners and nothing returns to the unmined pool.

The stage matters too. Bitcoin has mined about 95.7% of its cap, so its inflation is already low. TAO has mined only about 54% of its cap, and after one halving it still adds roughly 2.8% of supply per 90 days — closer to an early-stage Bitcoin than today's. Against uncapped chains like Ethereum, which pay stakers in new coins and burn part of every fee, TAO has a hard ceiling but no burn: its recycling is a delay, not a destruction.

TAO also differs in where new coins land. On Bitcoin, new BTC goes straight to miners. On Bittensor, new TAO flows into subnet pools and rewards, and participants are often paid in subnet tokens first, so how fast new TAO reaches the open market depends on how much of it is swapped out of those pools.

## What to watch in the next 90 days

First, the pace of recycling after the Sep 18 2026 fee cut: if lower fees slow it, the buy side shrinks and net growth edges up. Second, the runtime upgrades proposed on Sep 24 2026 and Sep 25 2026, still waiting for approval — none of them changes the block reward, but each is read for supply effects when it goes live. Third, the gamma-token proposal made on Sep 28 2026, which would let subnets turn part of their emissions into usage credits; it is only an idea for now and moves no TAO. Fourth, the public supply figure itself: it now lags the chain by about 223K TAO, including the Sep 15 2026 mint, and a catch-up would move the monitor again without any new TAO. The next halving is not a watch item this quarter — at today's pace it is more than three years away.

## Summary

TAO's supply grew **+4.31%** in the 90 days to Sep 29 2026: **323,690 TAO** of block rewards at 0.5 TAO a block, plus a one-time **172,001 TAO** mint on Sep 15 2026 to back root stakers, less **6,834 TAO** recycled. Without the one-time mint, the next 90 days point to about **+2.77%**. Bittensor has no vesting, no treasury and no burn, so the halved block reward is the whole story, and the main risk is that new TAO keeps arriving faster than recycling takes it back. The ceiling is the 21M cap, with the next halving set by issued supply at 15.75M TAO.

---

*MrNasdog Pressure Framework analysis of TAO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

---
title: "DOGE Inflation Analysis · July 2026 · Supply growing, projected to keep growing"
description: "Supply growing, projected to keep growing: Dogecoin mined 1.23B DOGE in 90 days at 10,000 per block, with no burn or buyback. Framework +0.79% net, monitor +0.79%."
canonical_url: "https://mrnasdog.com/research/doge/inflation"
tags: ["crypto", "doge", "dogecoin", "proof-of-work"]
published: true
---

> Originally published at **[mrnasdog.com/research/doge/inflation](https://mrnasdog.com/research/doge/inflation)** by MrNasdog.

Dogecoin mints exactly **10,000 DOGE per block** and produced **122,673 blocks** in the last 90 days, adding **1.23B DOGE** to supply. There is no Dogecoin buyback, no Dogecoin fee burn and no vesting escrow, so every newly mined DOGE is net new supply. The Pressure Framework reads Dogecoin at **+0.79%** net over 90 days, against our supply monitor at **+0.79%** — the two agree almost exactly.

## The verdict, in one paragraph

For the 90-day window ending July 19 2026, the MrNasdog Pressure Framework reads **DOGE at +0.79% net**, driven entirely by the Dogecoin block reward, with nothing on the buy side to offset it. Our supply monitor reads the realised 90-day change at **+0.79%** — a gap of **0.00 percentage points**, comfortably inside tolerance, so no monitor-gap chip ships on the Dogecoin overview. That agreement is not luck: this build derives Dogecoin issuance from the **observed** block count on chain rather than the nominal one-block-per-minute target, and real Dogecoin block times run a little slow — **1,363 blocks a day** against a nominal 1,440. Dogecoin is **structurally inflationary at a low, steady, fully predictable pace**: roughly 5 billion new DOGE a year, forever, on a circulating base that keeps growing underneath it.

## Sell pressure: where new DOGE comes from

Sell #1, protocol inflation, is the whole Dogecoin story, at **1.23B DOGE** over 90 days. Dogecoin pays a fixed block reward of **10,000 DOGE** to the miner of every block, and the Dogecoin network targets one block per minute. Over the window from April 20 2026 to July 19 2026 the chain actually produced **122,673 blocks**, which is **13.6M DOGE a day** and about **5B DOGE a year**. Crucially, this Dogecoin block reward **never halves**. Unlike a capped halving-model coin, Dogecoin fixed its subsidy at a flat 10,000 per block at block 600,000 and has issued at that pace ever since, so the last 90 days and the next 90 days mint the same amount. Dogecoin is merge-mined with Litecoin, which secures the chain but does not change the subsidy by a single coin.

Sell #2, vesting unlocks, is **zero**. Dogecoin launched in December 2013 as a fair launch with no presale, no investor round and no team allocation, so no Dogecoin vesting schedule exists and no cliff can hit the market — and as a UTXO chain without a smart-contract layer, Dogecoin has no way to hold a vesting escrow even if someone wanted one. Sell #3, Foundation and unscheduled unlocks, is also **zero** for this window, though it is no longer empty of watch items: a listed company that built an **Official Dogecoin Treasury** now holds **463.1M DOGE** and has said it is winding the position down. Its balance was unchanged across the entire 90-day window, so the framework books no release. Sell #4, long-term locked or bankruptcy, is **zero**, because no bankruptcy estate or court-ordered distribution applies to Dogecoin.

## Buy pressure: where new DOGE goes

Every Dogecoin buy-side row is **zero**, and that emptiness is the defining feature of Dogecoin supply. Buy #1, programmatic buyback, is zero: Dogecoin earns no protocol revenue and has no mechanism that spends money buying DOGE off the open market. Buy #2, protocol fee burn, is zero: Dogecoin transaction fees are paid to miners as part of the block reward, never destroyed, so the Dogecoin network burns nothing — there is no burn in Dogecoin consensus at all. Buy #3, Foundation buy, is zero; the Dogecoin Foundation runs a small reserve of about **10M DOGE** but announced no open-market buying in the window, and the large corporate treasury that once accumulated DOGE has reversed course into selling. Buy #4, new long-term lock, is zero: proof-of-work Dogecoin has no staking contract to lock into and no new escrow was announced. With nothing on the buy side, the gross Dogecoin mint and the net Dogecoin supply change are the same number.

## Foundation and overhang

Dogecoin has no unlock overhang in the usual sense, because no team cliff, investor schedule or treasury allocation ever existed to create one. What the framework does track are identified group-controlled holdings that could reach the market. The largest is a listed company's **463.1M DOGE** treasury, disclosed at that exact figure on both March 31 2026 and June 2 2026 in its regulated filings — unchanged through the whole window, but explicitly slated for disposition after the company abandoned its Dogecoin treasury strategy and terminated its asset-management agreements. Those coins sit with third-party custodians rather than a published address, so the framework monitors them through regulated filings rather than on-chain. Two smaller listed holders carry about **70.5M DOGE** and **21.7M DOGE**, and the Dogecoin Foundation reserve holds about **10M DOGE**. None of these entities can mint a single new DOGE. If any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How DOGE compares to other proof-of-work chains

Dogecoin belongs to a small class: **uncapped proof-of-work chains with a flat, non-halving emission**. A halving-model chain cuts its block reward on a fixed schedule, so its inflation rate steps down and its supply approaches a hard ceiling. Dogecoin has neither a ceiling nor a halving — it adds the same 10,000 DOGE per block indefinitely. The one thing that does fall over time is the Dogecoin inflation **rate**, because a fixed 5-billion-a-year mint is divided by a circulating base that grows every year, so a constant coin count becomes a shrinking percentage. That makes Dogecoin structurally closer to a tail-emission privacy coin than to a capped halving coin, even though it is merge-mined alongside one of the largest halving-model chains.

The sharper contrast is with chains that pair issuance against a burn or a buyback. A base-fee burn can push a chain net deflationary in busy periods; a programmatic buyback funded by protocol revenue can do the same. Dogecoin does neither, so its net supply change equals its gross mint with no brake whatsoever. That gives Dogecoin one of the cleanest inflation reads in the entire framework: exactly one source of new supply, fully predictable from the block reward, and nothing pulling in the other direction. Being predictable is not the same as being benign — a chain with no offsetting mechanism has no way to absorb a demand shock through its supply side.

## What to watch in the next 90 days

Watch the disposition of the **463.1M DOGE** corporate treasury: the company has stated no binding agreement exists, so the next regulated filing is the trigger, and any realised sale moves Sell #3 off zero for the first time. Watch the Dogecoin block reward itself — a Dogecoin Core proposal to cut the reward from 10,000 to 1,000 DOGE per block, opened **Jan 26 2025**, is closed and was never adopted; any change would require a coordinated Dogecoin hard fork, and until one activates the 10,000-per-block pace holds. Watch Dogecoin block times, since the gap between the observed **1,363 blocks a day** and the nominal 1,440 is what separates a correct issuance read from an overstated one. And watch for any new Dogecoin burn, buyback or lock mechanism: there is none today, and introducing one would be the only structural change capable of altering this coin's one-directional supply math.

## Summary

Dogecoin is an uncapped proof-of-work chain whose supply grows by a fixed, non-halving block reward of 10,000 DOGE. The chain minted **1.23B DOGE** across the last 90 days — 122,673 blocks, about 13.6M a day — while the Dogecoin buy side is completely empty: no buyback, no fee burn, no vesting, no treasury buying. That puts the Pressure Framework at **+0.79% net**, matching our supply monitor at **+0.79%** almost exactly. The key risk is not the mint, which is predictable to the block: it is the **463.1M DOGE** corporate treasury now marked for disposal, sitting above a market with no structural bid. Dogecoin has no cap and no ceiling — only a fixed coin count per day whose percentage weight slowly thins as the base grows.

---

*MrNasdog Pressure Framework analysis of Dogecoin (DOGE), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 19, 2026.*

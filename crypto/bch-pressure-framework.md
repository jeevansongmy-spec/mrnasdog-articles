---
title:         "BCH Inflation Analysis · September 2026 · Mixed flows, supply roughly steady"
description:   "Mixed flows, supply roughly steady: Bitcoin Cash mined 40,381.25 BCH over 12,922 blocks in 90 days, with no buyback and no burn. Net +0.201%, monitor +0.221%."
canonical_url: "https://mrnasdog.com/research/bch/inflation"
tags:          ["crypto", "bch", "bitcoincash", "payments"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/bch/inflation](https://mrnasdog.com/research/bch/inflation)*

# BCH Inflation Analysis · September 2026 · Mixed flows, supply roughly steady

Bitcoin Cash (BCH) adds new supply in exactly one way — the proof-of-work block reward of **3.125 BCH** — and takes nothing back: there is no BCH buyback, no BCH fee burn and no staking lock. Counting every block the Bitcoin Cash chain actually produced in the last 90 days gives **12,922 blocks** and **40,381.25 BCH** of new coins, so the MrNasdog Pressure Framework reads BCH at **+0.201% net** against a supply-monitor reading of **+0.221%** — a gap of **0.02 percentage points**, which is agreement. BCH is mildly inflationary under a hard **21M cap**, with about **0.91M BCH** left to mine.

## The verdict, in one paragraph

For the 90-day window ending **Sep 13 2026**, the Pressure Framework reads **BCH at +0.201% net**: **40,381.25 BCH** of mining issuance on the sell side against **zero** on the buy side, divided by **20.09M BCH** circulating. The independent supply monitor reads the realised 90-day change at **+0.221%**. The gap is **0.02 percentage points**, far inside the framework's half-point tolerance, so BCH ships with **no data-conflict flag**. The forward column also reads **+0.201%**, because the Bitcoin Cash block reward stays at 3.125 BCH until the next halving, around **Apr 2028**, and the next 90 days are projected at the block pace the chain just measured. The label for BCH is **capped proof-of-work, mining-only supply**: one sell row, no buy rows, and a small, steady rise toward a fixed ceiling.

## Sell pressure: where new BCH comes from

Sell #1, protocol inflation, is **~40.4K BCH**, and it is the only non-zero row on the Bitcoin Cash ledger. Bitcoin Cash inherited Bitcoin's monetary rules when it split in **Aug 2017**: a fixed subsidy per block that halves every 210,000 blocks, now **3.125 BCH**. Because that reward is paid per block rather than per unit of time, the framework counts blocks instead of assuming the ten-minute target. Between height **955,377** and height **968,298** the chain produced **12,922 blocks**, one every **601.75 seconds** on average — slightly slower than target, so a calendar estimate of 144 blocks a day would have overstated BCH issuance by **118.75 BCH**. Every one of those blocks was read, not sampled: together they created **40,381.25 BCH**, one satoshi short of the full schedule because a single miner under-claimed its reward. Transaction fees add nothing to supply; they are existing BCH paid to miners inside the same reward.

Sell #2, vesting unlocks, is **zero**. Bitcoin Cash began as a copy of the Bitcoin ledger, so every BCH was either inherited at the split or mined since; there was no premine, no token sale and no team or investor allocation, and therefore no BCH vesting schedule exists. Sell #3, foundation and unscheduled unlocks, is **zero**: there is no Bitcoin Cash foundation treasury, no DAO wallet and no diversion of the block reward to developers — a 2020 plan to fund development that way was rejected and never switched on. Sell #4, long-term locked or bankruptcy supply, is **zero**, although it carries the one live watch item. The Mt. Gox estate still holds an undisclosed amount of BCH, and its trustee has until **Oct 31 2026** to finish repaying creditors. Those BCH are already counted as circulating, so paying them out moves existing coins between wallets rather than creating new supply.

## Buy pressure: where new BCH goes

Nowhere — and on Bitcoin Cash that is a structural fact rather than a quiet quarter. Buy #1, programmatic buyback, is **zero**: the Bitcoin Cash protocol earns no revenue of its own and has no treasury to spend. Buy #2, protocol fee burn, is **zero**, and it was checked on both surfaces that could show a burn. The supply surface rose by exactly the mined amount across the window and never fell, and every block paid its fees to the miner in full. The unspendable-address surface was read separately: the two well-known keyless Bitcoin Cash addresses took in **0.001 BCH** of stray sends across the whole window, against **40,381.25 BCH** mined — too small to book. Buy #3, foundation buying, is **zero** because no project entity exists to buy; a Nasdaq-listed company is building a BCH treasury, but it is a third party buying on the open market with no disclosed size, so its coins were already in the float. Buy #4, new long-term locks, is **zero**: proof-of-work has no staking, and no new BCH lockup with a stated size appeared.

## Foundation and overhang

Bitcoin Cash has no team-controlled overhang to enumerate. With no allocation ever made, no foundation, DAO or team wallet holds BCH that could be released, and the published circulating figure sits within one update cycle of total BCH mined — the difference between the two is exactly **103 blocks** of reward, which is timing, not a locked bucket. Exchange custody wallets and large unlabelled holders are excluded by rule, because those BCH belong to depositors or to no identified group. The one balance tracked on the page is the Mt. Gox bankruptcy estate's BCH, whose remaining size the trustee has not disclosed; the last Bitcoin Cash repayment notice was dated **Mar 27 2025**, and it is re-checked against the trustee's own announcements on every refresh. If that estate's BCH moves to market between refreshes, the outflow enters Sell #4 at the next refresh.

## How BCH compares to other capped proof-of-work coins

BCH belongs to the halving-model class: a hard cap, a block reward that steps down on a fixed block count, and no burn. Against Bitcoin, the mechanism is identical — same cap, same halving heights, same **3.125** reward per block — so the two supplies grow at almost the same rate, and the difference between them is how many blocks each chain happens to produce. Against Litecoin, another capped proof-of-work chain, the shape is the same with different constants. Against a tail-emission or fixed-reward coin such as Dogecoin, which issues a flat amount forever with no cap, BCH inflation keeps halving toward zero, so the direction of travel is toward scarcity rather than toward a permanent drip.

Against uncapped proof-of-stake Layer 1s that mint validator rewards and offset part of it with a fee burn, BCH has neither side of that trade: nothing is minted beyond the schedule, and nothing is burned. The Bitcoin Cash fee economy is very small — about **23.36 BCH** of fees across the whole window, roughly **$58 a day**, or about **0.0005%** of its market capitalisation a year — so a fee burn would remove almost nothing even if one existed. That is also why the block count matters so much here: the BCH block reward is almost entirely new coins, so issuance is close to a pure function of how many blocks arrive.

## What to watch in the next 90 days

First, the Mt. Gox repayment deadline on **Oct 31 2026**: a BCH distribution would not change the BCH inflation reading, because those coins already circulate, but any move of estate BCH toward exchanges is tracked under Sell #4. Second, the BCH block pace: the chain ran **601.75 seconds** a block this window, and because Bitcoin Cash shares its mining hardware with Bitcoin, a sustained shift in hash power would move the next reading of Sell #1 by a few hundred BCH. Third, the **Nov 15 2026** lock-in date that the Bitcoin Cash research forum cites for the May 2027 upgrade: the candidate changes discussed there are scripting features, and a faster-blocks proposal is still unfinished — if block timing ever changes, issuance per block is re-measured from scratch. Fourth, the halving itself sits far outside the window, around **Apr 2028**, when the reward falls to **1.5625 BCH**.

## Summary

The MrNasdog Pressure Framework reads Bitcoin Cash at **+0.201% net** over the trailing 90 days and **+0.201%** over the next 90, with the supply monitor at **+0.221%** and no data conflict. The structural mechanism is capped proof-of-work: **40,381.25 BCH** of block rewards across **12,922 measured blocks**, and zero on every buy row because Bitcoin Cash has no buyback, no fee burn, no treasury and no staking. The key risk is not hidden supply but the absence of any offset — nothing on the Bitcoin Cash chain takes a coin back, so the float can only grow until the reward reaches zero. The ceiling is the **21M BCH** cap, about **96%** already mined, with the next halving around **Apr 2028**.

*MrNasdog Pressure Framework analysis of BCH, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 13 2026.*

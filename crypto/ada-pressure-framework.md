---
title:         "ADA Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description:   "Cardano adds ~365M ADA per 90 days — 115M from the capped reserve plus 270M voted out of its on-chain treasury, with no burn and no buyback. Framework reads +0.98% net."
canonical_url: "https://mrnasdog.com/research/ada/inflation"
tags:          ["crypto", "ada", "cardano", "layer1"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/ada/inflation](https://mrnasdog.com/research/ada/inflation)*

# ADA Inflation Analysis · August 2026 · Supply growing, projected to keep growing

Over the last 90 days about **365.3M ADA** reached the tradable float on Cardano — **115.3M** released from the Cardano protocol reserve and a much larger **269.6M** paid out of the on-chain Cardano treasury by approved governance actions, against only **19.6M** handed back. The MrNasdog Pressure Framework reads ADA at **+0.98%** net for the window and **+0.62%** forward; our independent supply monitor reads **+0.93%**, a gap of **0.05 percentage points**. Cardano is hard-capped at 45 billion ADA and mints nothing above it — but the cap is a ceiling, not a brake, and the treasury is now the bigger of Cardano's two taps.

## The verdict, in one paragraph

For the 90-day window ending **Aug 17 2026**, the Pressure Framework reads **Cardano at +0.98% net** on the last-90-day view and **+0.62%** on the forward view. Our supply monitor independently reads the realised change at **+0.93%**, putting the gap at **0.05 percentage points** — well inside tolerance, so there is **no monitor-gap flag** on this build. The two readings agree because they measure the same quantity from opposite ends: the framework adds up the on-chain flows into the ADA float, and the monitor measures the float itself. Total sell pressure was **384.9M ADA** against **19.6M** of buy pressure. The label that fits Cardano is **structurally inflationary on a hard cap** — the 45 billion ADA ceiling is real and permanent, but a 6.19 billion ADA reserve and a 1.45 billion ADA treasury still sit outside the float, and both are draining into it.

## Sell pressure: where new ADA comes from

Cardano has exactly one source of genuinely new ADA, and it is not a miner or a validator minting blocks. Every five days — one Cardano epoch — a fixed fraction of the remaining protocol reserve is moved into a reward pot together with that epoch's transaction fees. One fifth of the pot is taken by the Cardano treasury and the rest is paid to stake pools and delegators. Because the fraction is applied to a shrinking balance, the release decays automatically. Read directly on-chain across the window, the reserve gave up **182.7M ADA**, but **67.4M** of that was absorbed by the treasury and never touched the market, so **Sell #1, protocol inflation, is 115.3M ADA** — the portion that actually reached the ADA float.

**Sell #2, vesting unlocks, is zero**, and permanently so. Cardano's public sale and the three founding-organisation allocations finished releasing in 2019; there is no cliff, no vesting contract, and no locked tranche left anywhere in ADA's cap table. That makes ADA unusual among large layer-1 tokens, most of which still carry a multi-year unlock calendar.

The dominant row is **Sell #3, foundation and unscheduled unlocks, at 269.6M ADA** — and none of it is an unlock in the usual sense. It is the Cardano treasury spending its own balance. Twenty-five treasury-withdrawal governance actions were enacted inside the window, the largest a single **131.5M ADA** development batch on **May 29 2026**, followed by **32.9M** on **Jun 13 2026**, **23.0M** on **Jun 23 2026** and **32.9M** on **Jul 28 2026**. Treasury ADA sits outside the circulating figure until a vote releases it, so each enacted withdrawal is a real, dated addition to the float. **Sell #4, long-term locked or bankruptcy, is zero**: no estate or court-supervised trustee distributes ADA on a schedule.

## Buy pressure: where new ADA goes

Cardano offers the buy side almost nothing, and the reason is structural rather than circumstantial. **Buy #1, programmatic buyback, is zero**. A 2026 funding model has been publicly floated in which the Cardano treasury would take equity-like stakes in ecosystem projects and recycle returns into open-market ADA purchases, but nothing is deployed and no purchase has been observed on-chain, so the row stays at zero and is watched.

**Buy #2, protocol fee burn, is zero** because Cardano destroys nothing. Every transaction fee is pooled each epoch and recycled into the same reward pot — one fifth to the treasury, the rest to stakers. There is no burn address, no base-fee destruction, no equivalent of the mechanism that lets several competing chains offset their own issuance. **Buy #3, foundation buy, is zero** as well; the founding foundation's most recent published accounts move the other way, with ADA falling to about half of its reserves while bitcoin and cash rose.

**Buy #4, new long-term lock, is zero**, and this is the point most often misread about Cardano. ADA staking is non-custodial and non-locking: delegated ADA never leaves the owner's wallet, there is no bonding period and no unbonding queue, so the roughly two-thirds of ADA that is delegated removes nothing at all from the sellable float. The only genuine offset is a coin-specific fifth row — **19.6M ADA returned to the Cardano treasury**, nearly all of it in a single transfer on **Jun 28 2026**. That ADA leaves the float, but a future spending vote can release it again, so it is a pause rather than a burn.

## Foundation and overhang

Two team-controlled overhangs sit behind the ADA float. The first and largest is the **on-chain Cardano treasury, holding 1,453.7M ADA** as of **Aug 17 2026**. It is not a multisig or a custodial wallet — it is a protocol-level pot that only moves when a treasury-withdrawal governance action is ratified, and it is refreshed from the chain on every rebuild. It is also the most active overhang on this page, having released 269.6M ADA in 90 days. The second is the founding **Cardano Foundation's own reserves**, where the latest published financial report puts ADA at about half of roughly $361M in total assets; no per-wallet address is published, so it is tracked through the foundation's own disclosures rather than on-chain, and it is booked at zero until a sale is evidenced.

The 6,186.4M ADA protocol reserve is deliberately not listed as an overhang: it is released mechanically by consensus rules rather than by anyone's discretion, and it is already booked continuously in Sell #1. There is no buyback accumulation wallet, no bankruptcy residual, and no unscheduled-unlock pool. If either tracked overhang's balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How ADA compares to other capped layer-1 chains

ADA belongs to the small family of layer-1 coins with a genuine protocol-encoded cap, and the closest structural analogue is a halving chain: both replace discretionary issuance with a decaying release curve, and both promise that the ceiling is arithmetic rather than policy. The difference is where the undistributed supply lives. On a halving chain the unissued coins exist only as future block subsidy — nobody holds them, nobody can vote them out early. On Cardano the unissued supply is a real, readable reserve balance of **6,186.4M ADA** plus a treasury balance of **1,453.7M ADA**, and the treasury half can be moved to market by a vote rather than by the passage of time. That is why ADA's realised float growth is lumpy where a halving chain's is smooth.

Against uncapped continuous-emission proof-of-stake chains, Cardano looks better on the long horizon and no better in the short one. An uncapped chain can outrun ADA on annual issuance percentage, but it can also cut its own rate by governance; Cardano cannot mint above 45 billion ADA under any vote, which is a harder guarantee than any inflation parameter. Against chains that run a fee burn, though, Cardano is plainly weaker: a burn chain has a live counterweight that scales with usage, while Cardano recycles every fee back into the reward pot and the treasury, so higher network activity does not reduce ADA supply at all. And unlike an exchange token running a quarterly buyback out of revenue, Cardano has no revenue-funded bid under the coin — the proposed treasury-funded buyback would be the first, and it is not live.

## What to watch in the next 90 days

First, the **120.0M ADA** open-market liquidity withdrawal approved by ADA holders was ratified on-chain and enacts at the epoch boundary on **Aug 17 2026** — it is already the single largest item in the forward ledger and is the reason the next-90-day reading is **+0.62%** rather than lower. Second, the 300M ADA net-change limit that caps annual treasury spending **expired unratified on Aug 2 2026** with 337.4M already enacted for the cycle; a replacement limit has been floated at 500M ADA and whether it passes decides how large Sell #3 can be next quarter. Third, two further spending votes worth **4.3M ADA** close on **Sep 16 2026** and are not counted in this ledger until ratified. Fourth, the proposed treasury-funded ADA buyback: the first observed on-chain purchase would move Buy #1 off zero for the first time. Fifth, the Cardano Foundation's next financial disclosure, which is the only visibility into whether it is still rotating out of ADA.

## Summary

Cardano is a hard-capped proof-of-stake chain whose supply is still growing steadily: **+0.98%** of the ADA float over the last 90 days and **+0.62%** projected forward, against a monitor reading of **+0.93%**. The structural mechanism is a decaying protocol reserve that released **115.3M ADA** to market plus an on-chain treasury that voted out a larger **269.6M**, with no fee burn, no buyback and no locking staking to absorb any of it. The key risk is that the treasury half is discretionary rather than mechanical — a single ratified governance action added 131.5M ADA to the float in one epoch, and the spending limit meant to cap that behaviour has lapsed. The ceiling is the one thing that does not move: no ADA is ever created above 45 billion, and roughly 7.6 billion of that remains outside the float, in a reserve that drains by rule and a treasury that drains by vote.

---

*MrNasdog Pressure Framework analysis of ADA, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 17 2026.*

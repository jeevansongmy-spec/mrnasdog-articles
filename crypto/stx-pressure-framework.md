---
title:         "STX Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description:   "A Jul 30 2026 upgrade lifted the Stacks miner reward to 1,500 STX a block for six months, with no burn or buyback. Framework +0.63% rising to +1.22%, monitor +0.674%."
canonical_url: "https://mrnasdog.com/research/stx/inflation"
tags:          ["crypto", "stx", "stacks", "bitcoin"]
published:     true
---

*Originally published at [mrnasdog.com/research/stx/inflation](https://mrnasdog.com/research/stx/inflation)*

Stacks has one supply engine — the miner reward — and no brake. Reading the chain directly, supply grew about **11.66M STX** over the last 90 days, and a **Jul 30 2026** upgrade (PoX-5) reversed an earlier reward cut and added a temporary boost, lifting the reward to **1,500 STX** per Bitcoin block for roughly six months. That step nearly **doubled** the pace, projecting to about **22.7M STX** next quarter, while there is **no buyback and no burn** to remove any of it. The Pressure Framework reads **+0.63% net** last 90 days, rising to **+1.22%** next, and our supply monitor agrees at **+0.674%** — a gap of only **0.05 percentage points**.

## The verdict, in one paragraph

For the 90-day window ending Aug 2 2026, the Pressure Framework reads **STX at +0.63% net** over the trailing window, projected to **+1.22%** for the next. Sell pressure is **11.66M STX** of realised miner issuance, buy pressure is **zero**, against a circulating base of **1.855B STX**. Our supply monitor reads **+0.674%** for the trailing window, a gap of only **0.05 percentage points**, so **no monitor-gap chip** ships — the on-chain supply delta and the monitor agree. The forward number is higher than the trailing one for a specific, documented reason: the PoX-5 upgrade on **Jul 30 2026** restored the Stacks coinbase from 500 back to 1,000 STX per Bitcoin block and added a temporary **+500** boost, so the reward now runs at **1,500 STX** per block for the first bonding period. STX is best characterised as **structurally inflationary with no offset** — a predictable, schedule-driven drift that just accelerated.

## Sell pressure: where new STX comes from

Sell #1, protocol inflation, is **11.66M STX** realised, and it is the entire sell side. Stacks mints new STX as the miner coinbase, paid once per tenure. A tenure is anchored to a Bitcoin block, but miners **miss** some tenures — several Bitcoin blocks in the window anchor no Stacks block at all — so the real pace runs below one reward per Bitcoin block, at a measured tenure rate around **0.86**. Reading total supply at both ends of the window gives the honest figure: **1.855B STX** now against about **1.844B** ninety days ago, a rise of **11.66M STX**. The important detail is the mid-window change: on **Jul 30 2026** the PoX-5 upgrade lifted the reward, and the measured per-block issuance stepped from about **842** to about **1,749 STX** per Bitcoin block. Because that boosted reward lasts roughly six months, it covers the whole next quarter, which is why the forward projection is about **22.7M STX** rather than a repeat of the trailing figure.

The remaining sell rows are all **zero**. Sell #2, vesting unlocks, is zero because the 2017-2019 Blockstack token-sale vesting expired years ago — the chain now reports every STX as unlocked, and no founder or investor cliff falls in the window. Sell #3, foundation and unscheduled unlocks, is zero as a realised figure: no discretionary open-market sale was observed, though there are tracked overhangs, covered below. Sell #4, long-term locked or bankruptcy, is zero because there is no Stacks estate, no trustee and no court-ordered STX distribution.

## Buy pressure: where new STX goes

Every buy row is **zero**, and that is the defining fact about STX supply. Buy #1, programmatic buyback, is zero because Stacks runs no buyback — nothing removed STX during the window. Buy #2, protocol fee burn, is zero because Stacks has no burn: transaction fees are paid to miners rather than destroyed, so network activity does not shrink the supply the way an EIP-1559-style base-fee burn would. Buy #3, foundation buy, is zero because no Stacks Foundation open-market purchase has been disclosed. Buy #4, new long-term lock, is zero because both PoX stacking and the newly launched Bitcoin Bonds are yield custody, not supply locks — stacked STX earns Bitcoin rewards while still counting as circulating. With nothing on the buy side, the miner reward runs unopposed, and the Jul 30 boost lands directly on the net figure.

## Foundation and overhang

Stacks has one notable tracked overhang: the SIP-031 endowment. The endowment contract still holds about **55.86M STX**, released at roughly **4.17M STX** a month to the endowment wallet over a two-year vesting. The crucial nuance is that this STX was minted back at the endowment's activation — 100M immediately and 100M into the contract — so it already sits inside total supply. A release moves it from the contract to the wallet rather than creating new coins, which is why it does not enter Sell #1 as new issuance. The second piece is the Stacks Foundation operational treasury. Both are re-read on every rebuild, and if a discretionary balance falls between refreshes — the endowment wallet or the Foundation actually selling into the market — that outflow enters Sell #3 at the next refresh. Neither showed a discretionary sale in the trailing year, which is why Sell #3 is zero rather than a projected number.

## How STX compares to other uncapped-emission Bitcoin L2s

The first comparison is cap versus no cap. Bitcoin itself is the hard-cap archetype: a fixed 21M supply and a halving schedule that only ever slows issuance. Stacks is the opposite — there is no hard cap, only a long tail-emission curve that drifts toward roughly **2.318B STX** by 2050. That makes STX structurally inflationary in a way its settlement layer is not, and the Jul 30 upgrade is a reminder that the emission schedule is a governance variable, not a fixed constant: a proposal just moved the reward the other way, up rather than down.

The second comparison is burn versus no burn. Fee-burning smart-contract platforms and the exchange tokens with quarterly buybacks have a real mechanism pulling supply back down, and on a busy day they can print net-negative supply. Stacks has neither — fees go to miners and there is no protocol burn — so it sits firmly in the pure-emission camp, where the only thing that can offset new supply is a future governance decision to add a burn or a buyback. Nothing like that exists today.

The third comparison is what the market data shows, and here STX is unusually clean. Many tokens carry a large divergence between the chain and their published circulating figure; STX does not. The widely-quoted circulating supply, about **1.855B STX**, tracks the chain closely, and our supply monitor's trailing read of **+0.674%** lands within a rounding step of the framework's **+0.63%**. The honest measure and the market-data measure point at the same thing: supply is drifting up, and just started drifting up faster.

## What to watch in the next 90 days

First, the reward boost itself: the **1,500 STX** per block rate runs for the first bonding period — about six months, into **Jan 2027** — then reverts to **1,000 STX** per block, which will ease the pace but keep supply growing. Second, whether the measured tenure rate holds near **0.86** or miners capture more tenures, which would lift realised issuance toward the theoretical ceiling. Third, whether the SIP-031 endowment wallet or the Foundation begins visibly selling into the market — that flow enters Sell #3 the moment it appears on-chain. Fourth, any governance proposal to add a burn or a buyback, the only thing on this ledger that could turn the buy side non-zero. Fifth, the rollout of Bitcoin Bonds, expected from late **Aug 2026** — a demand story for STX stacking, but not a change to the supply ledger.

## Summary

The Pressure Framework reads STX at **+0.63% net** over the last 90 days and projects **+1.22%** for the next. The structure is simple: the miner coinbase mints new STX every tenure, the PoX-5 upgrade on **Jul 30 2026** lifted that reward to **1,500 STX** per Bitcoin block for about six months, and there is **no buyback and no burn** to remove any of it, so supply drifts steadily upward and just accelerated. The key risk is the absence of any offset — STX is inflationary by schedule until governance adds a brake — and the only ceiling is the soft tail-emission curve toward roughly **2.318B STX** by 2050. The market-data supply feed and the on-chain read agree here, so the framework and our monitor tell the same story within a rounding step.

*MrNasdog Pressure Framework analysis of STX, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 2 2026.*

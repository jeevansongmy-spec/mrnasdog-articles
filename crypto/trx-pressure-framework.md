---
title:         "TRX Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "TRX is mildly inflationary: TRON minted 352M TRX in block rewards against a 229M TRX fee burn, +0.13% net over 90 days and the same next. No cap, no vesting."
canonical_url: "https://mrnasdog.com/research/trx/inflation"
tags:          ["crypto", "trx", "tron", "payments"]
published:     true
---

# TRX Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

*Originally published at [mrnasdog.com/research/trx/inflation](https://mrnasdog.com/research/trx/inflation).*

The MrNasdog Pressure Framework reads TRX as **mildly inflationary**: TRON minted **352.39M TRX** in block and voter rewards over the last 90 days and burned **229.12M TRX** in fees, so supply grew **+0.13%**, and the next 90 days project the same **+0.13%**. The mint is fixed at **136 TRX per block** by an on-chain governance vote, while the burn depends on how many people pay fees instead of staking. TRX has no supply cap, no vesting left and no buyback, so the fee burn is the only brake on new supply.

## The verdict, in one paragraph

Over the trailing 90 days (Jul 1 to Sep 28 2026) the TRON supply ledger nets to **+0.13%** of the **94.97B TRX** circulating: **123.27M TRX** more was created than destroyed. The monitor, which reads supply day by day, shows **+0.12%** over its own 90-day window. The gap is **0.01 percentage points**, far inside the 0.5-point line, so no warning chip is needed and the two readings agree. The forward 90 days hold the same **+0.13%**, because no vote in the window changed the block reward or the fee price. TRX is a **slowly inflating fee-burn chain**: the burn cancels about two-thirds of new coins, and the last third reaches the market.

## Sell pressure: where new TRX comes from

Protocol inflation is the whole sell side. Every TRON block pays **8 TRX** to the Super Representative that produced it and **128 TRX** to the pool shared by the voters behind the 127 elected and standby producers — **136 TRX** in all. The chain made **2,591,095 blocks** in the window, a little under one every three seconds, which comes to **352,388,920 TRX**, about **3.92M TRX a day**. The reward was cut to 8 + 128 by an on-chain vote in June 2025, down from 16 + 160, and it has not changed since. The only vote passed inside this window, in late August 2026, added newer smart-contract features and left the reward alone.

Vesting unlocks are **zero**. The 2017 token sale, the team share and the TRON Foundation share all finished unlocking by January 2020, no unlock tracker lists a TRX schedule, and circulating supply sits within **1.11M TRX** of total supply, so there is no locked bucket left to open.

Foundation and unscheduled unlocks are **zero**. With only 1.11M TRX outside the circulating count, any project wallet bigger than that is already counted as circulating, and a sale from it would move coins that are already in the market. Long-term locks and bankruptcy releases are also **zero**: TRON has no estate, no court-run distribution and no unwinding lock.

## Buy pressure: where new TRX goes

The fee burn is the whole buy side. On TRON, every fee paid in TRX — bandwidth, energy for smart contracts, new-account and memo fees — is destroyed rather than paid to producers. Over the window the burn came to **229,116,867 TRX**, about **2.55M TRX a day**, and a random check of 300 blocks spread across the 90 days read the same total within 1.4%. Much of that burn is the energy cost of stablecoin transfers, which makes TRON's burn a measure of how many people pay to move dollars on the chain.

The burn is getting smaller. It ran at **2.69M TRX a day** in July and **2.34M TRX a day** over the last 30 days, with no fee change behind the drop. One reason sits in how TRON works: users who stake TRX receive free energy and bandwidth and pay no fee, and about **45.62B TRX** — 48% of supply — is staked. The energy price has stayed at 100 sun since August 2025, when a vote cut it from 210 sun and roughly halved what each transfer burns.

Programmatic buyback is **zero**: the protocol buys nothing back. A listed company close to the project keeps buying small amounts of TRX on the open market, but those coins move from one circulating wallet to another and leave nothing off the float. Foundation buys are **zero** — the buyback-and-burn programmes announced in the TRON ecosystem this year are for other tokens, not TRX. New long-term locks are **zero** too: staked TRX stays inside the circulating count, so more staking changes nothing in the supply count.

## Foundation and overhang

TRON has almost no overhang in the supply sense. The non-circulating remainder is about **1.11M TRX**, with no published schedule; it is checked at every rebuild. No wallet on the chain carries a public TRON Foundation or TRON DAO label, and any such wallet would already be inside the circulating count. The largest identified group holding is a listed company close to the project, which reported about **715.8M TRX** after a purchase on Sep 23 2026 and stakes most of it; a staked TRX fund that listed on Sep 9 2026 also holds TRX. Both bought their coins on the open market. If any of these balances falls between rebuilds, the outflow enters Sell #3 at the next refresh — but because they sit inside the float, a sale would show up as market selling, not as new supply.

## How TRX compares to other smart-contract Layer 1s

TRX sits in the same family as Ethereum: an uncapped proof-of-stake chain that mints new coins to the people who secure it and burns part of every fee. The difference is in the size of each side. TRON's mint is a fixed amount per block, set by a vote of block producers, rather than a curve that grows with the amount staked. And TRON's burn is much larger relative to its mint — about two-thirds of new TRX is burned — because the chain carries a heavy load of paid stablecoin transfers.

Against hard-capped chains such as Bitcoin, TRX has no halving and no ceiling; the 136 TRX per block runs until a new vote changes it. Against chains where fees go to validators instead of a burn, TRX gives every fee back to all holders by destroying it. Against exchange-chain coins with scheduled buyback burns, TRX has nothing timed or discretionary — its burn is automatic and continuous, and it rises and falls with how much people use TRON.

TRON was net deflationary in mid-2025, when the energy price was 210 sun. Since the energy price cut in August 2025, the burn has fallen below the mint, and the net now leans to growth. A chain like this can swing between shrinking and growing on usage alone, without any change to its rules.

## What to watch in the next 90 days

First, the burn rate: it has fallen from about 2.69M TRX a day in July to about 2.12M TRX a day over the last week, and if it keeps falling the next 90 days will print above +0.13%.

Second, the fee proposals: an open community proposal would cut the account-permission fee from 100 TRX to 7 TRX and the multi-signature fee from 1 TRX to 0.1 TRX; it has no on-chain vote date yet, and it would trim the burn only a little.

Third, any vote on the block reward or the energy price — either one moves the whole ledger at once, and none is scheduled as of Sep 29 2026.

Fourth, the stake: more TRX staked means more free energy and fewer fees burned, so a rise in the 45.62B TRX staked would lower the burn.

## Summary

TRX is mildly inflationary: TRON mints **352.39M TRX** per 90 days at a fixed 136 TRX per block and burns **229.12M TRX** in fees, for net supply growth of **+0.13%** over the last 90 days and the same projected for the next 90. The mint is set by an on-chain vote and the burn by how much people pay to use the chain, with no vesting, no unlocks and no buyback on either side. The key risk for the reading is a burn that keeps shrinking as more users stake instead of paying fees. TRX has no supply cap; its supply keeps growing unless usage lifts the burn above the mint again or a vote changes the reward.

*MrNasdog Pressure Framework analysis of TRX, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

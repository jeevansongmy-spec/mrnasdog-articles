---
title:         "XTZ Inflation Analysis · October 2026 · Supply growing · projected to keep growing"
description:   "XTZ supply is growing: Tezos paid bakers 8.12M new XTZ in 90 days while burns removed 63K, a +0.73% net rise, about +0.74% next. No cap, no vesting."
canonical_url: "https://mrnasdog.com/research/tezos/inflation"
tags:          ["crypto", "xtz", "tezos", "layer1"]
published:     true
---

Originally published at [XTZ Inflation Analysis · October 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/tezos/inflation).

# XTZ Inflation Analysis · October 2026 · Supply growing · projected to keep growing

Tezos (XTZ) supply is growing at a steady, moderate pace. Between Jul 11 and Oct 9 2026 the Tezos protocol created **8.12M XTZ** in baker rewards and old 2017 sale claims added **15,159 XTZ**, while storage burns, the exchange burn and lost rollup bonds destroyed **62,772 XTZ**. Net, circulating XTZ rose **+0.73%** in 90 days, the monitor reads **+0.74%**, and we expect about **+0.74%** again in the next 90 days. Tezos has no supply cap; the only brake is adaptive issuance, which pays less as more XTZ is staked.

## The verdict, in one paragraph

Over the last 90 days the MrNasdog Pressure Framework measures Tezos supply growth of **+0.73%**, against a monitor reading of **+0.74%**. The gap is **0.006 percentage points**, well inside our 0.5-point tolerance, so no warning chip is needed: two independent ways of counting XTZ agree almost to the coin. Almost all of the growth is new XTZ paid to bakers and stakers; the burns on the other side remove less than one coin in a hundred of what is created. The cite-able label for Tezos today is **steady staking inflation on an uncapped proof-of-stake chain**.

## Sell pressure: where new XTZ comes from

The first and by far the largest source is protocol inflation: **8,117,661 XTZ** created in 90 days, about 90,200 XTZ a day. Tezos pays bakers, the validators who propose and attest blocks, in freshly minted XTZ, and since 2024 it sets the rate with adaptive issuance. The rule is simple: when a larger share of XTZ is staked, the yearly rate falls, and when staking drops, the rate rises to pull people back in. About **31%** of supply is staked today and the Tezos protocol quotes a yearly issuance rate near **3.1%**. The protocol's own schedule for the next two days pays slightly less per block than the 90-day average, but we keep the measured rate for the forecast.

A second Tezos subsidy, the payment the chain makes to its built-in liquidity-baking exchange, is switched off. Bakers vote on it in every block, and their vote has kept it off since **Jun 2 2026**, so it added nothing this window.

Vesting unlocks are **zero**. The founders' and the Tezos Foundation's launch shares vested monthly over four years and finished in 2022, so no locked team supply remains on a calendar.

The Foundation and unscheduled unlocks row holds the one small XTZ stream that does enter the float from outside it: claims from the 2017 Tezos fundraiser. About **19.97M XTZ** from that sale has never been claimed, and those coins are not counted as circulating until someone claims them. In this window four claims brought in **15,159 XTZ**; over the past year 13 claims brought in 93,003 XTZ, at least one every quarter, so we expect about **23,251 XTZ** in the next 90 days.

Long-term locks and bankruptcy releases are **zero**: no court estate, trustee or long lock is paying XTZ out.

## Buy pressure: where new XTZ goes

There is **no programmatic buyback**. Transaction fees on Tezos go to the bakers who include the transaction; no contract or treasury uses them to buy XTZ on the market.

The protocol fee burn comes to **32,772 XTZ** and has two parts. Every time a user stores new data on Tezos, such as a new contract or a bigger contract state, a storage fee is destroyed: **22,775 XTZ** this window. And the liquidity-baking exchange sends 0.1% of every trade to an address no one can spend from: **9,997 XTZ**. We counted every one of those 6,799 transfers and they match the change in that address to the last unit.

A Foundation buy is **zero**: no announcement or on-chain flow shows the Tezos Foundation buying XTZ. A new long-term lock is also **zero**. Staking on Tezos is real and slashable, and stakers now earn three times what plain delegators earn, but staked XTZ still counts as circulating, so more staking does not shrink the float. It only pulls the issuance rate down.

One extra line appears this time: lost rollup bonds, **30,000 XTZ**. Operators of the Etherlink rollup lock a 10,000 XTZ bond when they post results. Between **Aug 15 and Aug 18 2026** six bonds were lost in disputes; half of each went to the winner and the other half was destroyed. This was a one-off, so the forecast books none of it again.

## Foundation and overhang

The Tezos Foundation is the one tracked team holder. Its labelled wallets hold about **63.66M XTZ**: four Foundation bakers with 33.24M and ten delegator wallets with 30.42M. On **Oct 6 2026** four of those delegator wallets sent about 19.9M XTZ out, and by **Oct 7 2026** two brand-new wallets held **30.00M XTZ** between them, each delegating to a Foundation baker and staking 6.68M. That looks like a reshuffle of the Foundation's own stake, not a sale. Its last report put its XTZ at about $76M on Dec 31 2025, or roughly 146M XTZ at that day's price, which includes loans and exchange liquidity we cannot see wallet by wallet.

All of the Foundation's XTZ already counts as circulating, so moving or selling it adds no new supply in our ledger; we read these wallets on the chain at every rebuild. The overhang that can add supply is the **19.97M XTZ** of unclaimed 2017 sale coins. If any of these balances falls between rebuilds, the outflow enters the Foundation and unscheduled unlocks row at the next rebuild.

## How XTZ compares to other proof-of-stake Layer 1s

Tezos sits in the uncapped proof-of-stake group with Ethereum and Cosmos-style chains: there is no maximum supply, and validators are paid in new coins forever. What sets Tezos apart is the feedback loop. Many proof-of-stake chains either fix the reward rate or step it down on a calendar; Tezos ties it to the staked share, so the rate drifts down as staking grows and would rise if stakers left. At **+0.73%** a quarter, Tezos runs well above Ethereum's recent pace but below the young chains still paying out large launch allocations.

The burn side is where Tezos looks weakest next to Ethereum. Ethereum destroys a slice of every transaction fee; Tezos only destroys storage fees and a sliver of exchange trades, so its burn covers about **0.4%** of new issuance. Compared with exchange tokens that run monthly buybacks, Tezos has no buyer of last resort at all. Compared with halving coins such as Bitcoin, it has no cap and no scheduled cut, only the slow pull of adaptive issuance.

## What to watch in the next 90 days

First, the Tezos protocol proposal period that runs from **Oct 7 to Oct 21 2026**. No proposal has been submitted yet. The next upgrade, Protocol V, is expected to switch on built-in liquid staking; if it is proposed now, the vote would take about 70 days and could activate near the end of this window.

Second, the staked share. It stayed near 31% this window; a rise pushes the issuance rate down, and a drop would push it back up. Third, the liquidity-baking vote: if bakers switch the exchange subsidy back on, it would add about 0.5 XTZ a block, roughly 650K XTZ a quarter. Fourth, the Foundation's new staking wallets and its next activity report, which would show whether the Oct 6 2026 moves were only a reshuffle.

## Summary

Tezos (XTZ) supply grew **+0.73%** in the 90 days to Oct 9 2026, and the MrNasdog Pressure Framework expects about **+0.74%** in the next 90 days. Nearly all of it is baker pay set by adaptive issuance, about 8.1M XTZ a quarter, while storage burns, the exchange burn and lost rollup bonds removed under 1% of that. Nothing vests and there is no buyback; the main risk is that staking falls and the issuance rate rises. There is no supply cap, so the only ceiling on XTZ inflation is how much of it people choose to stake.

*MrNasdog Pressure Framework analysis of XTZ, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 9 2026.*

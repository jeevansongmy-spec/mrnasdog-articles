---
title:         "DOT Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description:   "Polkadot minted 13.78M DOT in 90 days under its 2.1B cap and burned none: fees now feed a governance pool. Framework +0.81% net, monitor +0.85%, gap 0.04pp."
canonical_url: "https://mrnasdog.com/research/dot/inflation"
tags:          ["crypto", "dot", "polkadot", "layer1"]
published:     true
---

> Originally published at **[mrnasdog.com/research/dot/inflation](https://mrnasdog.com/research/dot/inflation)** by MrNasdog.

Polkadot adds new DOT every minute and destroys almost none of it, so the Pressure Framework reads DOT at **+0.81%** over the trailing 90 days and **+0.81%** over the next 90. The whole reading is issuance: **13.78M DOT** minted in the window on a time-based curve, while every burn path that used to offset it now feeds a governance-run pool instead. Sell pressure is **13.78M DOT**, buy pressure is **0**, and the ceiling is a voted hard cap of **2,100M DOT** that the curve approaches but never crosses.

## The verdict, in one paragraph

Against a circulating base of **1,702.8M DOT**, the framework books **13.78M DOT** of sell pressure and **0** of buy pressure over the trailing 90 days — a net of **+0.81%** — and projects **+0.81%** for the next 90 days, because the Polkadot issuance curve does not step down again until **Mar 2028**. The inflation monitor reads **+0.85%** for the same window, a gap of **0.04 percentage points**, which is inside the framework's 0.5pp tolerance, so the overview ships without a monitor-gap warning. The label for DOT is a **capped, steadily inflating staking chain with its burns switched off**: supply grows slowly and in one direction only.

## Sell pressure: where new DOT comes from

Sell #1, protocol inflation, is **13.78M DOT**, and it is the entire sell side. Since the Asset Hub migration of November 2025, Polkadot balances, staking and issuance live on Asset Hub, and Asset Hub keeps the one count of DOT in existence — including the DOT sitting on the relay chain and other system chains, which it tracks through a checking account rather than counting twice. That count rose from **1,689.0M** to **1,702.8M DOT** across the window. The mechanism is a mint that drips new DOT at most once a minute, sized by elapsed time rather than by blocks, on the curve set by the vote that capped DOT at 2.1B: each year the chain issues **13.14%** of the remaining room under the cap, re-measured every two years. Today that is **55.9M DOT** a year, about **153K DOT** a day. Adding up the drip schedule sub-window by sub-window reproduces the measured rise to within about 1,300 DOT. On **Jun 29 2026**, Referendum 1909 changed who receives each drip — stakers fell from 85% to **45.2%**, a new validator self-stake reward took **22.6%**, and the Dynamic Allocation Pool buffer rose from 15% to **32.2%** — but it did not change how much is minted, so the forward projection is not re-based.

Sell #2, vesting unlocks, is **0**. Polkadot has no team or investor unlock calendar left. What sits in the Polkadot vesting module today are private grants between holders, and in this window they ran in both directions: **2.45M DOT** was released from older grants while **7.89M DOT** was locked into new two-year grants, most of it in a single batch on **Sep 1 2026**. The last parachain slot deposits were returned in July. Every one of those coins was already inside the circulating figure the framework divides by, so neither the releases nor the new locks change the tradable float, and the framework books neither.

Sell #3, foundation and unscheduled unlocks, is **0**: the two pots with a spender both grew rather than shrank. Sell #4, long-term locked or bankruptcy, is **0** as well — DOT has no bankruptcy estate, no trustee and no court-ordered distribution.

## Buy pressure: where new DOT goes

Buy #1, programmatic buyback, is **0**. Polkadot runs no programme that spends treasury money buying DOT, and no referendum in the window created one.

Buy #2, protocol fee burn, is also **0**, and this is where Polkadot changed most. The Polkadot treasury stopped burning its unspent funds in **Mar 2026** when the Dynamic Allocation Pool went live, and since a runtime upgrade in early **Jun 2026** transaction fees, validator slashes and smart-contract burns on Asset Hub all route into that pool instead of being destroyed. The framework read both places a burn could show, at both ends of the window. The count of DOT in existence rose at every reading. The keyless burn address now proposed in Wish for Change 1939 received **2.1 DOT**. One real burn survives — coretime sales revenue is still destroyed on the relay chain — but the cross-chain accounting puts it at a few thousand DOT at most, too small to show on a base of 1,702.8M and not provable to the coin, so it is not booked.

Buy #3, foundation buy, is **0**: the treasury and the pool grew from issuance and fees arriving on their own, not from market purchases. Buy #4, new long-term lock, is **0**. Staking does not qualify, because Polkadot nominators can now unbond in one to two days, and the new two-year vesting grants were already circulating DOT.

## Foundation and overhang

Two Polkadot pots are tracked. The on-chain treasury held **24.31M DOT** at the end of the window against **23.44M DOT** at the start. The Dynamic Allocation Pool buffer, which now receives **32.2%** of every mint plus all fees and slashes, climbed from **0.11M** to **4.22M DOT**. Both balances are read from the chain at every rebuild, and together they close to within one DOT against the chain's own tally of inactive supply. Neither pot has a release calendar; OpenGov decides every outflow. The nearest candidate is Referendum 1944, still in its decision period, which would seed a DOT/dotUSD trading pool with treasury DOT worth about $1.5M. If the treasury's or the pool's balance falls between refreshes, that outflow enters Sell #3 at the next refresh.

## How DOT compares to other capped staking chains

DOT now sits between two families. Like Bitcoin, Polkadot has a hard ceiling and a stepped schedule that shrinks issuance over time; unlike Bitcoin, the steps are measured against the remaining room under the cap rather than halving a block reward, and the new supply pays stakers and a governance pool rather than miners. Against an uncapped continuous-emission proof-of-stake chain, where issuance is a policy that can be voted higher, DOT is stricter: its curve converges on 2.1B and the next change is already dated to Mar 2028.

Where DOT differs from the fee-burning chains is the buy side. An EIP-1559-style chain destroys part of every fee, so heavy usage can push its reading flat or negative. Polkadot chose the opposite in 2026: instead of burning fees, it keeps them in a pool that governance spends. That makes the DOT reading easy to forecast — it is almost exactly the issuance curve — but it also means network activity no longer offsets any of it.

## What to watch in the next 90 days

First, the issuance curve itself: absent a vote, it mints about 153K DOT a day until Mar 2028, so the next reading should land near +0.81% again. Second, Referendum 1944 on dotUSD, which would move treasury DOT into a trading pool if it passes. Third, Wish for Change 1939, which would confirm a keyless burn address and give Wish for Change 1926 — burning all DOT paid for future JAMKB sales — a destination; any DOT that reaches it lands in Buy #2. Fourth, the Dynamic Allocation Pool's later phases, which would move coretime revenue into the pool and could end the last surviving burn. Fifth, the pool buffer at 4.22M DOT and the treasury at 24.31M DOT, the only balances on Polkadot with a spender rather than a schedule.

## Summary

The MrNasdog Pressure Framework reads DOT at **+0.81%** over the trailing 90 days and **+0.81%** projected forward: supply growing, projected to keep growing. The structural mechanism is issuance with nothing offsetting it — Polkadot minted **13.78M DOT** in the window on a time-based curve, and since 2026 its fees, slashes and treasury surplus are kept in a governance pool rather than burned. The key risk is that usage cannot reduce this number, and the two growing pots, 24.31M DOT in the treasury and 4.22M DOT in the pool, are spent by vote rather than by schedule. The ceiling is the comfort: a hard cap of 2,100M DOT, approached along a curve that steps down again in Mar 2028.

*MrNasdog Pressure Framework analysis of DOT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 15 2026.*

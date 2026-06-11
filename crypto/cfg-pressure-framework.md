---
title: "CFG Inflation Analysis · June 2026 · Supply growing, projected to keep growing"
description: "A MrNasdog Pressure Framework read of Centrifuge (CFG): 3% inflation accrues to Treasury off-market, small incentive vest reaches market. Framework reads +1.68%; monitor −34.1% is migration accounting (⚠)."
canonical_url: "https://mrnasdog.com/research/cfg/inflation"
tags: ["crypto", "cfg", "centrifuge", "rwa"]
published: true
---

> Originally published at **[mrnasdog.com/research/cfg/inflation](https://mrnasdog.com/research/cfg/inflation)** by MrNasdog.

Centrifuge's CFG migrated to a single Ethereum-native token in 2025; its 3% annual inflation accrues to the Treasury off-market, leaving only a small ecosystem-incentive vest reaching circulation. The Pressure Framework reads **+1.68% net** inflation against a monitor reading of **−34.14%** — the large negative is migration accounting, not a sell, so a ⚠ chip ships.

## The verdict, in one paragraph

For the 90-day window the framework reads **CFG at +1.68% net** inflation — the only supply reaching the market is a small CP149 ecosystem-incentive vest. The inflation monitor reads **−34.14%** over the same window, a gap of **35.82 percentage points** that triggers a ⚠ data-conflict chip. The deep walk resolves it: the −197M the monitor saw is the May 20 2025 migration to the Ethereum-native CFG (a 1:1 swap) dropping un-migrated legacy CFG and WCFG from the circulating count — an accounting reclassification, not a market sell. CFG is mildly inflationary on live flows.

## Sell pressure: where new CFG comes from

**Protocol inflation** is booked at zero to market: Centrifuge mints 3% annually, but per the token docs that inflation accrues to the Centrifuge Treasury — it is new supply, yet it is parked off-market rather than distributed to circulation, so it adds no market sell pressure (it is tracked instead as a growing overhang). **Vesting unlocks** booked **~6.4M CFG**: the CP149 ecosystem-incentive tokens (100M vesting linearly through April 2029) enter circulation at roughly 6.4M per 90 days — the only scheduled supply reaching the market in the window. **Foundation and unscheduled unlocks** are zero: the Treasury and the ~45% of total supply still unreleased are tracked overhangs with no observed discretionary deploy. **Bankruptcy** is zero.

## Buy pressure: where new CFG goes

The buy ledger is empty. **Programmatic buyback** is zero — there is no revenue-funded buyback. **Protocol fee burn** is zero: Centrifuge's RWA pool fees accrue to liquidity providers and pool operators, not back to the CFG token. **Foundation buy** is zero — no accumulation programme. **New long-term lock** is zero — validator self-bonds are operational with a short unbond, not a long-term lock with an announced quantum.

## Foundation and overhang

Two overhangs are tracked. First, the **Centrifuge Treasury**, which accrues the 3% annual inflation (~20.9M CFG/yr) — new supply that is parked rather than sold, so it grows as a claim on the float without currently pressuring it. Second, the **~317M CFG still unreleased** (697.16M total minus ~380.6M circulating), spanning team, incentive and ecosystem buckets on a partial schedule (the CP149 line runs through April 2029). Both are walked bi-weekly. If either balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How CFG compares to other RWA tokens

Centrifuge is one of the oldest real-world-asset protocols, and CFG's supply mechanics now resemble a continuous-inflation Layer 1 more than a fixed-cap token: 3% a year, uncapped, with the new supply directed to the Treasury. Against ONDO — its closest RWA sibling in coverage — CFG is the opposite shape: ONDO has no inflation and releases supply in annual cliffs, while CFG inflates continuously but parks the mint. Against an RWA Layer 1 like MANTRA's OM (8% staking inflation paid to stakers), CFG's 3% is lower and, crucially, does not hit the market because it accrues to the Treasury rather than being distributed.

The mechanism that defines CFG this window is the migration. The 2025 move from the Substrate-native chain plus an Ethereum WCFG wrapper to a single Ethereum-native CFG (1:1 swap) is why the aggregator's circulating count fell ~34% — it dropped legacy tokens that had not yet swapped. That is a one-time reclassification, not a recurring flow, which is exactly why the framework keeps its live read (+1.68%) and ships the gap as a ⚠ chip rather than adopting the monitor's number.

The Treasury-accrual distinction is the crux of CFG's reading, so it is worth stating plainly. A token can inflate its total supply without adding market sell pressure if the new units are minted to a treasury that does not sell them — and that is exactly Centrifuge's design: the 3% goes to the Treasury, not to stakers' wallets or the open market. The framework therefore books that inflation at zero to market and tracks the Treasury as a growing overhang instead. This is the honest middle ground between counting the full 3% as a sell (it is not hitting the market) and ignoring it entirely (it is a real, growing claim on the float the Treasury could one day deploy).

## What to watch in the next 90 days

Three things move the reading. First, the **Centrifuge Treasury** — a deployment of accrued inflation to the market would convert the parked overhang into real Sell #3. Second, the **CP149 incentive vest** — it runs through April 2029 at ~6.4M/90D, the steady baseline. Third, the **migration tail** — as the last legacy CFG/WCFG swaps complete, the aggregator's circulating count should stabilise and the ⚠ gap should close on its own.

## Summary

CFG is a migrated, Ethereum-native RWA token with a 3% annual inflation that accrues to the Treasury off-market, leaving only a ~6.4M/90D ecosystem-incentive vest reaching circulation — so the framework reads **+1.68% net** against a monitor reading of **−34.14%**, a 35.82-point gap carrying a ⚠ chip. The negative monitor figure is the 2025 migration reclassification, not a sell. The key variable is whether the Treasury ever deploys its accrued inflation to the market.

---

*MrNasdog Pressure Framework analysis of CFG, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 12, 2026.*

---
title: "CFG Inflation Analysis · June 2026 · Supply growing, projected to keep growing"
description: "A MrNasdog Pressure Framework read of Centrifuge (CFG): 3% inflation + CP149 incentives accrue to Treasury off-market, team vest reaches market. Framework reads +1.58%; monitor −34.1% is migration accounting (⚠)."
canonical_url: "https://mrnasdog.com/research/cfg/inflation"
tags: ["crypto", "cfg", "centrifuge", "rwa"]
published: true
---

> Originally published at **[mrnasdog.com/research/cfg/inflation](https://mrnasdog.com/research/cfg/inflation)** by MrNasdog.

Centrifuge's CFG migrated to a single Ethereum-native token in 2025. Its 3% annual inflation and its CP149 incentive vest both accrue to the Centrifuge Treasury off-market, leaving only team and other-stakeholder vesting reaching circulation. The Pressure Framework reads **+1.58% net** inflation against a monitor reading of **−34.07%** — the large negative is migration accounting, not a sell, so a ⚠ chip ships.

## The verdict, in one paragraph

For the 90-day window the framework reads **CFG at +1.58% net** inflation — the only supply reaching the market is the team and other-stakeholder vesting, about **~6.0M CFG**. The inflation monitor reads **−34.07%** over the same window, a gap of **35.65 percentage points** that triggers a ⚠ data-conflict chip. The deep walk resolves it: the ~196.6M the monitor saw fall is the migration to the Ethereum-native CFG — the 1:1 swap opened May 20 2025 and the legacy window closed Nov 30 2025, and as it completed the aggregator dropped un-migrated legacy CFG and WCFG from the circulating count. That is an accounting reclassification, not a market sell. CFG is mildly inflationary on live flows.

## Sell pressure: where new CFG comes from

**Protocol inflation** is booked at zero to market. Centrifuge mints 3% of total supply a year (~20.9M CFG), but per the token docs that inflation accrues to the Centrifuge Treasury — it is new supply, yet it is parked off-market rather than distributed to circulation, so it adds no market sell pressure and is tracked instead as a growing overhang. **Vesting unlocks** are booked at **~6.0M CFG**: the team allocation (12% of supply, vesting through May 2030) and the other-stakeholder allocations (through March 2028) vest linearly to their recipients and reach circulation at roughly 6.0M per 90 days. The CP149 incentive tokens — 100M vesting through April 2029 — vest into the Treasury, so they stay off-market and are excluded here. **Foundation and unscheduled unlocks** are zero: the Treasury (accruing the 3% inflation plus the CP149 incentives) and the ecosystem allocation are tracked overhangs with no observed discretionary deploy to market. **Bankruptcy** is zero — no estate distributes CFG.

## Buy pressure: where new CFG goes

The buy ledger is empty. **Programmatic buyback** is zero — there is no revenue-funded buyback, only governance discussion of fee-sharing and value-accrual ideas that are not yet live on-chain. **Protocol fee burn** is zero: Centrifuge's RWA pool fees accrue to liquidity providers and pool operators, not back to the CFG token. **Foundation buy** is zero — the Foundation receives inflation, it does not buy CFG on the market. **New long-term lock** is zero — there is no newly-deployed lockup contract with an announced quantum.

## Foundation and overhang

Two overhangs are tracked. First, the **Centrifuge Treasury**, which accrues the 3% annual inflation (~20.9M CFG/yr) plus the 100M CP149 incentive vest through April 2029 — new supply that is parked rather than sold, so it grows as a claim on the float without currently pressuring it. Second, the **ecosystem allocation** (~14.3% of total supply) and the broader unreleased buckets behind the 54.6% released figure. Both are walked bi-weekly. If either balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How CFG compares to other RWA tokens

Centrifuge is one of the oldest real-world-asset protocols, and CFG's supply mechanics now resemble a continuous-inflation Layer 1 more than a fixed-cap token: 3% a year, uncapped, with the new supply directed to the Treasury. Against ONDO — its closest RWA sibling in coverage — CFG is the opposite shape: ONDO has no protocol inflation and releases supply in annual cliffs, while CFG inflates continuously but parks the mint. Against an RWA Layer 1 like MANTRA's OM (staking inflation paid to stakers), CFG's 3% is both lower and structurally different: it does not hit the market because it accrues to the Treasury rather than being distributed to stakers' wallets.

The mechanism that defines CFG this window is the migration. The 2025 move from the Substrate-native chain plus an Ethereum WCFG wrapper to a single Ethereum-native CFG (1:1 swap) is why the aggregator's circulating count fell about 34% — it dropped legacy tokens that had not yet swapped before the November 30 2025 deadline. That is a one-time reclassification, not a recurring flow, which is exactly why the framework keeps its live read (+1.58%) and ships the gap as a ⚠ chip rather than adopting the monitor's number.

The Treasury-accrual distinction is the crux of CFG's reading, so it is worth stating plainly. A token can inflate its total supply without adding market sell pressure if the new units are minted to a treasury that does not sell them — and that is exactly Centrifuge's design: both the 3% inflation and the CP149 incentive vest go to the Treasury, not to stakers' wallets or the open market. The framework therefore books that inflation at zero to market and tracks the Treasury as a growing overhang instead.

## What to watch in the next 90 days

Three things move the reading. First, the **Centrifuge Treasury** — a deployment of accrued inflation or incentives to the market would convert the parked overhang into real Sell #3. Second, the **team and other-stakeholder vesting** — running at ~6.0M/90D, the steady baseline (team through May 2030, other stakeholders through March 2028). Third, the **migration tail** — with the legacy swap window closed November 30 2025, the aggregator's circulating count should stabilise and the ⚠ gap should narrow on its own.

## Summary

CFG is a migrated, Ethereum-native RWA token whose 3% annual inflation and CP149 incentive vest both accrue to the Treasury off-market, leaving only a ~6.0M/90D team and other-stakeholder vest reaching circulation — so the framework reads **+1.58% net** against a monitor reading of **−34.07%**, a 35.65-point gap carrying a ⚠ chip. The negative monitor figure is the 2025 migration reclassification, not a sell. The key variable is whether the Treasury ever deploys its accrued inflation to the market.

---

*MrNasdog Pressure Framework analysis of CFG, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 26, 2026.*

---
title: "CFG Inflation Analysis · July 2026 · Supply growing, projected to keep growing"
description: "A MrNasdog Pressure Framework read of Centrifuge (CFG): 3% inflation + CP149 incentives accrue to Treasury off-market, team vest reaches market. Framework reads +2.89%; monitor −34.0% is a June 2026 circulating reclassification (⚠)."
canonical_url: "https://mrnasdog.com/research/cfg/inflation"
tags: ["crypto", "cfg", "centrifuge", "rwa"]
published: true
---

> Originally published at **[mrnasdog.com/research/cfg/inflation](https://mrnasdog.com/research/cfg/inflation)** by MrNasdog.

Centrifuge's CFG is now a single Ethereum-native token, and its 3% annual inflation and CP149 incentive vest both accrue to the Centrifuge Treasury off-market — leaving only team and other-stakeholder vesting reaching circulation. The Pressure Framework reads **+2.89% net** inflation against a monitor reading of **−34.0%**. The large negative is a circulating-supply reclassification, not a sell, so a ⚠ chip ships.

## The verdict, in one paragraph

For the 90-day window the framework reads **CFG at +2.89% net** inflation — the only supply reaching the market is the team and other-stakeholder vesting, about **~11.0M CFG** against a circulating base of **~380.4M**. The inflation monitor reads **−34.0%** over the same window, a gap of **36.9 percentage points** that triggers a ⚠ data-conflict chip. The deep walk resolves it: the roughly 197M CFG the monitor saw fall was a circulating-supply reclassification by the market data trackers that landed between June 4 and June 14 2026, aligning the count to the ~54.6% released figure the token docs report, while other trackers still show ~577M. On-chain total supply held at 697.16M, so no burn or sell occurred. CFG is mildly inflationary on live flows.

## Sell pressure: where new CFG comes from

**Protocol inflation** is booked at zero to market. Centrifuge mints 3% of total supply a year (~20.9M CFG), but per the token docs that inflation accrues to the Centrifuge Treasury — it is new supply, yet it is parked off-market rather than distributed to circulation, so it adds no market sell pressure and is tracked instead as a growing overhang. **Vesting unlocks** are booked at **~11.0M CFG**: the team allocation (12% of supply, vesting through May 2030) and the other-stakeholder allocation (~8.6% of supply, vesting through March 2028) release linearly to their recipients and reach circulation at roughly 11.0M per 90 days. The CP149 incentive tokens — 100M vesting through April 2029 — vest into the Treasury, so they stay off-market and are excluded here. **Foundation and unscheduled unlocks** are zero: the Treasury (accruing the 3% inflation plus the CP149 incentives) and the ecosystem allocation are tracked overhangs with no observed discretionary deploy to market. **Bankruptcy** is zero — no estate distributes CFG.

## Buy pressure: where new CFG goes

The buy ledger is empty. **Programmatic buyback** is zero — there is no revenue-funded buyback. Governance restructuring CP171 commits CFG as the single mechanism through which ecosystem value accrues and defers a value-accrual analysis to the coming quarters, but nothing is live on-chain. **Protocol fee burn** is zero: Centrifuge's RWA pool fees accrue to liquidity providers and pool operators, not back to the CFG token. **Foundation buy** is zero — the Foundation receives inflation, it does not buy CFG on the market. **New long-term lock** is zero — there is no newly-deployed lockup contract with an announced quantum.

## Foundation and overhang

Two overhangs are tracked. First, the **Centrifuge Treasury**, which accrues the 3% annual inflation (~20.9M CFG/yr) plus the 100M CP149 incentive vest through April 2029 — new supply that is parked rather than sold, so it grows as a claim on the float without currently pressuring it. Second, the **ecosystem allocation** (~14.3% of total supply) and the broader unreleased buckets behind the 54.6% released figure. Both are walked bi-weekly. If either balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How CFG compares to other RWA tokens

Centrifuge is one of the oldest real-world-asset protocols, and CFG's supply mechanics now resemble a continuous-inflation Layer 1 more than a fixed-cap token: 3% a year, uncapped, with the new supply directed to the Treasury. Against ONDO — its closest RWA sibling in coverage — CFG is the opposite shape: ONDO has no protocol inflation and releases supply in annual cliffs, while CFG inflates continuously but parks the mint. Against an RWA Layer 1 like MANTRA's OM (staking inflation paid to stakers), CFG's 3% is both lower and different in kind: it does not hit the market because it accrues to the Treasury rather than being distributed to stakers' wallets.

The mechanism that defines CFG this window is a reporting change, not a flow. In 2025 Centrifuge moved from a Substrate-native chain plus an Ethereum WCFG wrapper to a single Ethereum-native CFG via the CP149 migration (1:1 swap). The tracked circulating count for the migrated token then fell roughly 34% — but the drop landed in June 2026, not at the November 2025 swap deadline, and it aligned the count to the ~380.4M released figure the token docs report while other trackers still read ~577M. Because on-chain total supply held at 697.16M, that is a one-time circulating reclassification, not a recurring flow — which is exactly why the framework keeps its live read (+2.89%) and ships the gap as a ⚠ chip rather than adopting the monitor's number.

The Treasury-accrual distinction is the crux of CFG's reading, so it is worth stating plainly. A token can inflate its total supply without adding market sell pressure if the new units are minted to a treasury that does not sell them — and that is exactly Centrifuge's design: both the 3% inflation and the CP149 incentive vest go to the Treasury, not to stakers' wallets or the open market. The framework therefore books that inflation at zero to market and tracks the Treasury as a growing overhang instead. This is the honest middle ground between two wrong readings: counting the full mint as a sell (it is not hitting the market) and ignoring it entirely (it is a real, growing claim on the float that the Treasury could one day deploy).

## What to watch in the next 90 days

Three things move the reading. First, the **Centrifuge Treasury** — a deployment of accrued inflation or incentives to the market would convert the parked overhang into real Sell #3, and CP171's promised value-accrual analysis is where any such decision would surface. Second, the **team and other-stakeholder vesting** — running at ~11.0M/90D, the steady baseline (team through May 2030, other stakeholders through March 2028). Third, the **reclassification tail** — with the ~197M circulating cut now in the monitor's trailing window, the aggregator's reading should stabilise and the ⚠ gap should roll off on its own by around October 2026.

## Summary

CFG is a migrated, Ethereum-native RWA token whose 3% annual inflation and CP149 incentive vest both accrue to the Treasury off-market, leaving only a ~11.0M/90D team and other-stakeholder vest reaching circulation — so the framework reads **+2.89% net** against a monitor reading of **−34.0%**, a 36.9-point gap carrying a ⚠ chip. The negative monitor figure is a June 2026 circulating reclassification, not a sell; on-chain supply held at 697.16M. The key variable is whether the Treasury ever deploys its accrued inflation to the market.

---

*MrNasdog Pressure Framework analysis of CFG, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 6 2026.*

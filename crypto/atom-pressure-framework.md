---
title: "ATOM Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description: "Supply growing: ATOM reads +3.07% over 90 days. Cosmos Hub minted 16.30M ATOM at a real 12.65% rate against a 10% setting and burned only 1.6K from slashing."
canonical_url: "https://mrnasdog.com/research/atom/inflation"
tags: ["crypto", "atom", "cosmos", "staking"]
published: true
---

*Originally published at [https://mrnasdog.com/research/atom/inflation](https://mrnasdog.com/research/atom/inflation)*

# ATOM Inflation Analysis · September 2026 · Supply growing, projected to keep growing

Cosmos Hub adds new ATOM every block and destroys almost none, so the Pressure Framework reads ATOM at **+3.07%** over the trailing 90 days and **+3.17%** over the next 90. The mechanism is the staking mint: its setting sits at a **10%** ceiling, but because Cosmos Hub produces blocks faster than that setting assumes, the real rate is **12.65%** a year. Sell pressure is **16.30M ATOM**, buy pressure is **1.6K ATOM** of slashing burns, and ATOM has no supply cap at all.

## The verdict, in one paragraph

Against a circulating base of **530.76M ATOM**, the framework books **16.30M ATOM** of sell pressure and **1.6K ATOM** of buy pressure over the trailing 90 days — a net of **+3.07%** — and projects **+3.17%** for the next 90 days at the same settings. The inflation monitor reads **+3.01%** for the same window, a gap of **0.06 percentage points**, well inside the framework's 0.5pp tolerance, so no monitor-gap warning ships on the overview page. The label for ATOM is an **uncapped staking chain whose mint runs above its own setting**: new supply goes to stakers every block, and nothing on Cosmos Hub takes a meaningful amount back out.

## Sell pressure: where new ATOM comes from

Almost all of it comes from Sell #1, protocol inflation, at **16.30M ATOM**. Cosmos Hub's mint module pays new ATOM to validators and stakers in every block. Its annual rate floats between a **7%** floor and a **10%** ceiling depending on how much ATOM is staked against a **67%** goal. Staking has stayed below that goal — **63.17%** at the end of the window — so the rate has sat pinned at the **10%** ceiling the whole time. The mint parameters read identically at both ends of the window, and no governance proposal changed them.

The twist is how the **10%** is paid. Cosmos Hub does not pay per day; it pays per block, dividing the yearly amount by a fixed assumption of **4.36M** blocks a year. The chain actually made **1,360,268** blocks in these 90 days — a block every **5.72** seconds, or about **5.52M** a year. Nothing in the protocol adjusts for that, so every extra block is extra ATOM, and the real issuance rate is **12.65%** a year. The count of ATOM in existence rose from **514.48M** to **530.78M** across the window, which matches the per-block mint to within the slashing burns described below. At the same settings, the next 90 days add about **16.82M ATOM**, slightly more than the last 90 because the mint compounds off a larger base.

Sell #2, vesting unlocks, is **0**: the ATOM distributed at launch finished unlocking long ago and no release calendar remains. Sell #3, Foundation and unscheduled unlocks, is **0**, because no foundation release happened on a schedule or with a disclosed date inside the window; the pools that could release are covered under overhang below. Sell #4, long-term locked or bankruptcy, is **0**: Cosmos Hub has no bankruptcy estate and no court-ordered distribution.

## Buy pressure: where new ATOM goes

Buy #1, programmatic buyback, is **0**. Cosmos Hub has never run a buyback. Cosmos Labs has a tokenomics redesign in research with Gauntlet, aimed at tying ATOM to fee revenue, but it has not reached an on-chain vote. Coverage from August 2026 claiming ATOM had already switched to buybacks and burns is not supported by the chain: no such proposal exists, and the mint still runs at its ceiling.

Buy #2, protocol fee burn, is **0**. Transaction fees on Cosmos Hub go to stakers, and the base fee collected by the fee market is parked in its own account rather than destroyed — that account grew from **56.8K** to **60.2K ATOM**. Governance deposits were not burned either. Two spam proposals were overwhelmingly vetoed in July 2026, but a deposit is only burned when the vote also reaches quorum, and neither did, so both deposits were refunded; the supply shows no drop at either closing block.

The only ATOM actually destroyed is Buy #5, slashing burn, at **1.6K ATOM**. When a validator misses too many blocks, Cosmos Hub takes a small cut of its staked ATOM and burns it. That happened on **7** separate days in the window; the largest was on **Sep 2 2026**, when **7** validators lost **335 ATOM** in a single block. The framework assumes the same pace for the next 90 days. Buy #3, Foundation buy, is **0**: no entity bought ATOM on the market. Buy #4, new long-term lock, is **0**. Staked ATOM rose from **322.17M** to **335.27M**, but staked ATOM can unbond in 21 days and is already inside the circulating count, so it is not a lock.

## Foundation and overhang

Three pools of already-existing ATOM could reach the market by decision rather than by schedule. The largest is the Interchain Foundation treasury, which reported **14.93M ATOM** on **Jun 30 2026**, down from **15.23M** at the end of February; the foundation sells assets from time to time to fund its budget, and its holdings are refreshed from its monthly treasury report. The second is the Cosmos Hub community pool, controlled by on-chain governance, which grew from **10.45M** to **11.33M ATOM** over the window. That rise came from its **2%** share of staking rewards and fees plus **555.4K ATOM** sent back to the pool by a multisig on **Sep 10 2026**; the only spend that passed in the window paid out a stablecoin, not ATOM. The third is the fee-market account holding **60.2K ATOM** of parked base fees, which no decision has yet given a destination. The community pool and the fee-market account are read from the chain at every rebuild. If any of these balances falls between refreshes, that outflow enters Sell #3 at the next refresh.

## How ATOM compares to other proof-of-stake chains

ATOM sits in the uncapped, continuous-emission class of proof-of-stake chains, where staking rewards are paid in new coins and no ceiling exists on total supply. Within that class, ATOM is on the high end. Its staking-linked rate range of 7% to 10% is set by governance rather than written into a fixed schedule, and in practice it pays more than the top of that range because the mint counts blocks, not time. Chains that pay rewards per unit of time, or that re-scale their block assumption when block times change, do not carry that extra issuance.

Against a halving-model chain like Bitcoin the difference is structural. Bitcoin's issuance is capped and falls on a known clock, so its 90-day reading is a fraction of a percent and shrinking. ATOM's issuance is uncapped and responds to staking behaviour: if staking rose above the 67% goal, the rate would start to drift down toward the 7% floor, and if staking falls it stays pinned at the ceiling. There is no date on which ATOM issuance halves.

Against burn-heavy tokens — exchange tokens with quarterly buybacks, or chains that destroy part of every transaction fee — ATOM has no offset at scale. Its only removal is validator slashing, **1.6K ATOM** against **16.30M** minted, about one ATOM destroyed for every ten thousand created. For a burn to change this reading, Cosmos Hub would need a new fee-linked mechanism approved by governance, which is exactly what the tokenomics research is exploring.

## What to watch in the next 90 days

First, the Cosmos Labs tokenomics Phase 2 report with Gauntlet, which the Hub team says is almost finished; any proposal to cut the ceiling or change how the mint is paid would change the forward reading, and a vote passing mid-window would re-base the projection. Second, the staking ratio at **63.17%**: about **20.3M** more ATOM would need to be staked to reach the 67% goal and start pulling the rate below the ceiling. Third, the community pool at **11.33M ATOM**, where proposal #1054 closes its vote on **Sep 17 2026** and pays a stablecoin, not ATOM — any later proposal spending pool ATOM would add to Sell #3. Fourth, the Interchain Foundation's next monthly treasury report, to see whether its **14.93M ATOM** keeps falling. Fifth, block times: if blocks speed up further, issuance rises further above the **10%** setting.

## Summary

The MrNasdog Pressure Framework reads ATOM at **+3.07%** over the trailing 90 days and **+3.17%** projected forward: supply growing, projected to keep growing. The structural mechanism is Cosmos Hub's staking mint, pinned at its **10%** ceiling but paying a real **12.65%** a year because it counts blocks rather than time, which produced **16.30M ATOM** in 90 days against only **1.6K ATOM** destroyed by slashing. The key risk is that nothing on the chain offsets it — no buyback, no fee burn, no lock — while **14.93M ATOM** at the Interchain Foundation and **11.33M ATOM** in the community pool sit on no release schedule. ATOM has no supply cap; the only ceiling is a governance setting that a vote can change.

*MrNasdog Pressure Framework analysis of ATOM, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 15 2026.*

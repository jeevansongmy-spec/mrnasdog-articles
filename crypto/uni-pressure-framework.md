---
title: "UNI Inflation Analysis · July 2026 · Effectively Flat"
description: "UNI's UNIfication fee switch burned ~4.09M UNI / 90D against a ~5M growth-budget vest, with no protocol mint ever. Framework reads +0.15% net on the 1B genesis supply."
canonical_url: "https://mrnasdog.com/research/uni/inflation"
tags: ["crypto", "uni", "uniswap", "defi"]
published: true
---

*Originally published at [mrnasdog.com/research/uni/inflation](https://mrnasdog.com/research/uni/inflation)*

# UNI Inflation Analysis · July 2026 · Effectively Flat

Uniswap has never minted new UNI — the contract's 2% minter has never been called. The only fresh supply is the **20M UNI / year growth budget** (~5M this window). Against it, the UNIfication fee switch burned **~4.09M UNI**, verified on-chain. Framework reading: **+0.15% net** — supply on the float is effectively flat, slightly inflationary, on a 1B genesis supply.

## The verdict, in one paragraph

For the 90-day window ending July 6 2026, the framework reads **UNI at +0.15% net** — the growth-budget vesting adds about **5M UNI** to the float while the UNIfication fee-switch burn removes **~4.09M UNI**, leaving the two almost cancelling. The inflation monitor reads **−1.87%** over the same window, a gap of **2.02 percentage points** that triggers a monitor-gap flag. The gap is not a burn the framework missed: the monitor tracks circulating-supply classification, which fell partly from the on-chain burn and mostly from a governance vote on June 1 2026 that returned 12.5M previously-delegated UNI into the DAO treasury — a custody move, not market absorption. The framework keeps its net-flow read. UNI in mid-2026 is best characterised as a structurally-flat supply with a live, revenue-funded burn now large enough to neutralise its only new-supply stream.

## Sell pressure: where new UNI comes from

Sell #1 (protocol inflation) is **zero**. The UNI contract carries a minter that became unlockable in September 2024 and can issue up to 2% of supply per year, but governance has never called it — the on-chain total supply still reads its **1B genesis figure**, so no new UNI has ever been minted. The framework counts only what actually fires, not what the contract permits.

Sell #2 (vesting unlocks) is the only non-zero sell row at about **5M UNI**. The original four-year team, investor, advisor, airdrop and liquidity-mining vesting all finished in 2024, and every unlock tracker now shows UNI fully unlocked. The single live schedule today is the **20M UNI / year growth budget** created under UNIfication, paid quarterly from the DAO treasury through a vesting contract since January 1 2026 — roughly 5M UNI enters the active float in this window. Sell #3 (Foundation and unscheduled unlocks) is zero: the DAO governance treasury holds about **272M UNI**, but the only treasury movement in the window was the 12.5M delegated-token return on June 1 2026, which flowed into the treasury, not out to market. Sell #4 (long-term locked or bankruptcy) is zero — UNI has no bankruptcy estate.

## Buy pressure: where the UNI goes

Buy #2 (protocol fee burn) is the load-bearing buy row at **~4.09M UNI**. The **UNIfication fee switch**, live since December 2025, collects a share of v2, v3 and Unichain swap-fee revenue into a vault contract called TokenJar. That value can only be claimed by burning an equal value of UNI through a second contract, Firepit, which sends the UNI to the dead address. Reading the dead address directly on-chain, its UNI balance grew from about 102.7M to 106.8M over the window — a **~4.09M UNI burn** — with the burn pace peaking at a single-day record near 134,000 UNI in early June 2026.

The other buy rows are zero. Buy #1 (programmatic buyback) is zero because there is no separate buyback wallet — the fee switch routes value straight into the burn path rather than accumulating UNI. Buy #3 (Foundation buy) is zero; the Uniswap Foundation does not buy UNI on the open market. Buy #4 (new long-term lock) is zero — the deflationary force here is the burn, not a fresh supply lock.

## Foundation and overhang

The single largest team-controlled overhang is the **Uniswap DAO governance treasury**, holding about **272.1M UNI** in the on-chain Timelock as of July 6 2026 — the bulk of all non-circulating UNI. The June 1 2026 vote that returned 12.5M previously-delegated UNI to this Timelock added to it rather than releasing supply. The treasury funds the 20M-per-year growth budget already counted in Sell #2; outside that schedule, deploys require an on-chain governance vote and there is no published per-firing calendar. The framework tracks this balance on every refresh: if the treasury's UNI balance falls between refreshes through a discretionary market deploy, that outflow enters Sell #3 at the next refresh.

## How UNI compares to other DEX governance tokens

Most DEX governance tokens are structurally inflationary: SushiSwap's SUSHI, PancakeSwap's CAKE and dYdX's DYDX all fund liquidity-mining or staking rewards with continuous emission, so new supply outpaces any removal. UNI is now the opposite case in mechanism — it never mints, and it runs a revenue-funded burn. The closest structural analogue is Curve's veCRV model, which separates locked long-term holders from the market float, but Curve still emits fresh CRV every block while UNI's only new supply is a fixed, already-minted treasury budget.

Against fixed-cap DeFi protocols with fee-funded buyback — Aave's AAVE buyback, MakerDAO's MKR smart-burn — UNI sits in similar territory: a fixed denominator with protocol revenue eating into the float. The difference is mechanism design. UNI's burn is paired one-for-one with fee claims through Firepit, so the burn scales directly with how much fee revenue users want to extract, and it flows only as fast as swap volume generates claimable fees. That makes UNI's deflation contingent on usage rather than scheduled — closer to a base-fee burn than to a fixed buyback budget.

## What to watch in the next 90 days

First, **Uniswap swap volume** — the Firepit burn scales with fee revenue, so a sustained volume rise would push UNI net-deflationary while a slump would let the growth-budget vest dominate. Second, the next **growth-budget quarterly vest around Oct 1 2026**, which adds roughly 5M UNI to the float. Third, further **fee-expansion governance votes** extending the burn to v4, UniswapX or additional L2 and L1 pools — each one would lift the burn pace. Fourth, any DAO vote to **activate the 2% minter** or to deploy the ~272M treasury to market, either of which would change the sell side immediately.

## Summary

UNI is a 1B genesis-supply, fully-unlocked, DAO-governed token whose supply is now effectively flat: no protocol mint has ever fired, the only fresh supply is a ~5M-per-quarter treasury growth budget, and the UNIfication fee switch burns UNI from swap-fee revenue at a comparable pace — ~4.09M this window, confirmed on-chain. The framework reads +0.15% net; the monitor reads −1.87%, a gap driven by circulating-supply reclassification after 12.5M delegated UNI returned to the treasury, not by a missed flow. The key risk is swap volume, which sets the burn pace; the ceiling is the 1B genesis supply with no new mint; the swing factor is whether the DAO ever turns on the dormant 2% minter.

*MrNasdog Pressure Framework analysis of Uniswap (UNI), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 6, 2026.*

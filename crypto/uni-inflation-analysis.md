---
title: "Uniswap (UNI) Inflation Analysis: Fee-Switch Burn Turned It Deflationary"
description: "A MrNasdog Pressure Framework read of Uniswap (UNI): the post-vesting 2% perpetual mint (3M / 90D) is overwhelmed by the UNIfication fee-switch burn (~15M / 90D). Framework reads −1.93% net on a 1B hard cap. Net deflationary by design."
canonical_url: "https://mrnasdog.com/research/uni/inflation"
tags: ["crypto", "uniswap", "defi", "dex"]
published: true
---

> Originally published at **[mrnasdog.com/research/uni/inflation](https://mrnasdog.com/research/uni/inflation)** by MrNasdog.

Uniswap mints about 3M UNI every 90 days under post-vesting perpetual inflation. The UNIfication fee switch burns ~15M UNI over the same window from swap-fee revenue. Framework reading: **−1.93% net** on a 1B hard cap. UNI is currently a deflationary asset.

## The verdict, in one paragraph

For the 90-day window ending June 10 2026, the framework reads **UNI at −1.93% net inflation** — the 2% perpetual community-treasury mint (~3M UNI) is overwhelmed by the UNIfication fee-switch burn (~15M UNI) at current Uniswap volumes. The aggregator monitor reads **−1.89%**, well inside the framework's 0.5-percentage-point tolerance. The two readings agree. Uniswap in mid-2026 is, in supply-pressure terms, the cleanest deflationary case in DeFi: revenue-funded burn against a fixed cap.

## Sell pressure: where new UNI comes from

Uniswap has exactly one source of new supply now that the original 4-year vesting completed in 2024: the **post-vesting 2% annual perpetual inflation**, which mints into the community treasury. On a base of ~622M circulating UNI, that translates to roughly **3M new UNI every 90 days**. The mint is technically a Sell #1 row under the Pressure Framework's 8-row ledger, but it's a slow, predictable one.

Every other sell-side row is zero. Sell #2 (vesting unlocks) closed when the original team / investor / advisor / airdrop / LP-staking buckets all completed their 4-year linear schedule by September 2024. Sell #3 (Foundation + unscheduled unlocks) is zero — the Uniswap DAO controls the community treasury, but no observed in-window discretionary deploy went to market beyond the 2% mint already counted in Sell #1. Sell #4 (bankruptcy estate) is zero; there is no bankruptcy estate.

## Buy pressure: where the UNI goes

The **UNIfication proposal** activated November 10 2025 and rewired Uniswap's tokenomics. A share of v3 and v4 swap fees now converts UNI from the market via an on-chain mechanism and burns the purchased tokens. This replaces the long-debated "fee switch" with a structural buyback-and-burn instead of a separate treasury accumulation. Over the trailing 90 days, the observed burn pace runs roughly **15M UNI**, driven by DEX volume across the v3 and v4 pools.

The burn flow is large enough that the other buy-side rows are effectively immaterial. Buy #1 (programmatic buyback) is captured by the UNIfication burn — there's no separate buyback wallet accumulating UNI; the protocol burns directly. Buy #3 (Foundation buy) is zero — the Uniswap Foundation does not accumulate UNI on the open market. Buy #4 (new long-term lock) is zero — staking exists for governance but holds already-circulating tokens rather than locking fresh supply.

## Foundation and overhang

The Uniswap community treasury holds 43% of the original allocation, all of which has now passed vesting. This is the single largest team-controlled overhang on the chain. The DAO controls it via on-chain governance vote, and treasury deploys typically fund ecosystem grants and contributor compensation rather than open-market sells. There's no published per-firing schedule beyond the 2% perpetual mint that's already accounted for in Sell #1. If the DAO ever votes for a discretionary large-scale market deploy outside the 2% mint cadence, that's the watch line and it would flip the framework reading immediately.

## How UNI compares to other DEX governance tokens

Among DEX governance tokens, UNI's post-UNIfication structure is unusual. Most competitors — SushiSwap's SUSHI, PancakeSwap's CAKE, dYdX's DYDX — operate with continuous emission funding liquidity-mining programs, so their tokens are structurally inflationary while UNI is now structurally deflationary. The closest structural analogue is Curve's veCRV model, which locks long-term holders and creates a similar locked-stake-vs-market-float distinction — but Curve still mints fresh CRV continuously, while UNI's mint is capped at 2% perpetually with a much larger burn flowing the other way.

Against fixed-cap DeFi protocols more broadly — Aave's AAVE, MakerDAO's MKR — UNI now occupies similar territory: a fixed denominator with revenue-funded buyback eating into the float. The difference is volume. Uniswap's swap volumes are an order of magnitude larger than Aave's lending fees or MakerDAO's stability fees, so UNI's buyback flow is correspondingly larger. A direct revenue-to-burn comparison across these three reveals UNI as the most deflationary by absolute UNI-equivalent value at current market rates.

## What to watch in the next 90 days

Three things move the framework reading materially. First, **Uniswap swap volume** — the burn pace tracks directly with v3 and v4 fee accrual. A sustained 50%+ drop in DEX volume would compress the burn enough to flip UNI back toward neutral. Second, **DAO governance votes** that adjust the UNIfication parameters (e.g. changing the share of fees that go to burn vs treasury). Third, the perpetual **2% community-treasury mint** trajectory — if the DAO ever votes to increase or decrease that rate, Sell #1 changes immediately. None of these are currently signalled.

## Summary

UNI is a 1B-cap, fully-unlocked, DAO-governed token that just turned structurally deflationary thanks to the UNIfication fee switch. Post-vesting 2% perpetual mint is dwarfed by ~15M of 90-day burn from swap-fee revenue. The framework reads −1.93% net; the aggregator agrees within tolerance. The structural risk is DEX volume; the structural ceiling is the 1B cap, and the structural floor is whatever the DAO decides about future mint policy. For now, UNI sits among the cleanest deflationary cases in DeFi.

---

*MrNasdog Pressure Framework analysis of Uniswap (UNI), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 10, 2026.*

---
title: "INJ Inflation Analysis · July 2026 · The weekly burn now edges out the staking mint"
description: "A MrNasdog Pressure Framework read of Injective (INJ): ~1M / 90D of staking inflation vs a ~1.15M weekly burn auction and buyback. Framework −0.15% net; monitor −0.17% — mildly deflationary."
canonical_url: "https://mrnasdog.com/research/inj/inflation"
tags: ["crypto", "inj", "injective", "staking", "burn-auction"]
published: true
---

> Originally published at **[mrnasdog.com/research/inj/inflation](https://mrnasdog.com/research/inj/inflation)** by MrNasdog.

Injective mints about **1M INJ** over 90 days to pay stakers, on the INJ 3.0 dynamic supply schedule, while a weekly burn auction and monthly Community BuyBack destroy roughly **1.15M** back out. The burn now just outpaces the mint, so the Pressure Framework reads about **−0.15% net** — mildly deflationary. Our supply monitor reads a near-identical **−0.17%**, so the two agree with no monitor gap.

## The verdict, in one paragraph

For the 90-day window ending July 4 2026, the MrNasdog Pressure Framework reads **INJ at −0.15% net** on the forward view: a low staking mint that is now slightly out-burned by Injective's fee-funded buy-and-burn. Our supply monitor reads the realized last-90-day change at **−0.17%** — the on-chain float shrank from about 100.14M to 99.97M INJ — versus the framework's **−0.15%** read for the same window, a gap of just **0.02 percentage points**. That is well inside tolerance, so **no monitor-gap chip** ships. Both sides are derived independently — the staking mint from the protocol rate, the burn from the auction and buyback rhythm — and they happen to nearly cancel. INJ is best characterised as **mildly deflationary by structural buyback**: the burn is doing the work, not the mint.

## Sell pressure: where new INJ comes from

Sell #1 — protocol inflation — is the only source of new INJ, at about **1M INJ** over the next 90 days. Injective mints INJ every block to reward stakers under the INJ 3.0 dynamic supply model, where the inflation rate floats inside a band whose bounds are being pulled down toward roughly a **4%** floor and **7%** ceiling as the schedule matures. Because a large share of supply — around **58%** — is staked and the rate targets a high staked ratio, the effective mint runs low, and the freshly minted INJ paid to stakers is overwhelmingly re-bonded rather than sold.

Sell #2 — vesting unlocks — is **zero**: every original team, seed, private-sale and ecosystem allocation has finished vesting, so INJ is effectively fully circulating — about 99.97M of a 100M total — and no cliff hits the market. Sell #3 — Foundation and unscheduled unlocks — is also zero as a flow; there is no remaining scheduled unlock pool. Sell #4 — long-term locked or bankruptcy — is zero.

## Buy pressure: where new INJ goes

Buy #1 — programmatic buyback — is the dominant force on INJ, at about **1M INJ** burned over 90 days. Every week Injective runs a burn auction: roughly **60%** of the fees earned across the network's apps are pooled, bidders compete for that basket by offering INJ, and the winning INJ bid is permanently burned. Because the destination is a burn, those coins are destroyed for good. Buy #2 — protocol fee burn — adds about **0.15M INJ** more: a monthly Community BuyBack round buys and burns INJ funded by protocol revenue, with recent rounds growing from about **37K** to **55K INJ** and a June 2026 round setting a record after IIP-617, the Supply Squeeze, raised the deflation rate. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero as protocol mechanisms, though a public-company treasury did open a large INJ position and stake it in this window, a third-party purchase the framework notes but does not book as a protocol flow.

## Foundation and overhang

INJ has no classic unlock overhang — the token has been fully distributed, with no team, seed or ecosystem cliff left to release. The only structural source of new supply is the staking inflation itself, paid continuously to validators and delegators, and the large majority of it re-bonds into staking rather than reaching the float. There is no buyback accumulation wallet to track, because Injective's buying is paired directly with a burn rather than pooled in a treasury. The framework books no discretionary release beyond protocol inflation and re-checks the burn auction, the monthly buyback rounds and chain emission on a roughly bi-weekly walk; if a treasury or staking balance falls faster than the schedule, the outflow enters Sell #3 at the next refresh.

## How INJ compares to other uncapped proof-of-stake chains

INJ belongs to the class of **uncapped Cosmos-SDK proof-of-stake L1s with dynamic staking inflation** — closer to a continuous-emission chain than to a hard-capped, halving-model coin. Unlike a fixed-supply token, INJ has no ceiling; unlike a pure inflation chain, it pairs the staking mint with a fee-funded burn large enough to flip the net negative. The dynamic rate is the shared Cosmos feature: inflation floats between a floor and a cap based on the bonded ratio, and INJ's Supply Squeeze upgrades keep pulling those bounds down over time.

The contrast worth drawing is with exchange tokens that burn on a quarterly schedule to shrink supply. INJ does the same thing continuously, through a weekly auction rather than a quarterly event, and at a scale that now slightly exceeds its own mint. That puts INJ in the small group of proof-of-stake chains that are actually net-deflationary on the active float — the burn is the larger of the two forces. Whether that holds depends on fee revenue: the burn scales with on-chain activity, so a quieter market would let the mint edge back ahead.

## What to watch in the next 90 days

Watch the monthly Community BuyBack rounds — the next ones land around **Jul 13 2026**, **Aug 13 2026** and **Sep 13 2026**, and their growing size is a direct read on whether the burn keeps pace with the mint. Watch weekly burn-auction revenue, which scales with fee activity after the Vulcan mainnet upgrade — a busier network burns more INJ. Watch the bonded ratio: because inflation is dynamic, more staking pushes the mint rate down and less staking lifts it. And note any governance vote that lowers the inflation bounds further under the Supply Squeeze schedule.

## Summary

INJ is an uncapped proof-of-stake finance chain whose supply both mints and burns at once. The chain mints about 1M INJ over 90 days to stakers under the INJ 3.0 dynamic model, while a weekly burn auction and monthly Community BuyBack destroy roughly 1.15M back out, leaving the framework at about −0.15% net — mildly deflationary. Our supply monitor reads −0.17% realized, essentially agreeing, so no monitor gap ships. The key risk is fee revenue: the burn is the larger force only as long as on-chain activity keeps funding it, and a quieter market would let the staking mint edge back ahead.

*MrNasdog Pressure Framework analysis of Injective (INJ), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 4, 2026.*

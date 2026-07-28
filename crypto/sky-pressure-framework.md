---
title:         "SKY Inflation Analysis · July 2026 · Mixed flows, supply roughly steady"
description:   "Sky's capped 23.46B token added ~419M SKY of staking rewards over 90 days against ~324M bought and burned. Framework +0.41% net, monitor +0.55%, within tolerance."
canonical_url: "https://mrnasdog.com/research/sky/inflation"
tags:          ["crypto", "sky", "makerdao", "defi"]
published:     true
---

*Originally published at [mrnasdog.com/research/sky/inflation](https://mrnasdog.com/research/sky/inflation)*

Sky, the former MakerDAO, runs its SKY governance token under a fixed ceiling of about **23.46B** — no block reward, no open-ended mint. Over the last 90 days the only new float was a SKY staking-reward stream of roughly **419M SKY**, and against it the Smart Burn Engine bought and permanently burned about **324M SKY**. The framework reads **+0.41% net** versus our supply monitor at **+0.55%** — a gap of only **0.15 percentage points**, well inside tolerance, so no monitor-gap chip. SKY is a capped token whose inflation is a reward payout almost fully cancelled by a revenue-funded burn.

## The verdict, in one paragraph

For the 90-day window ending Jul 28 2026, the Pressure Framework reads **SKY at +0.41% net**. Sell pressure totals **419M SKY**, buy pressure **324M SKY**, against a circulating base of **23.38B SKY**. Our supply monitor reads the realised circulating change at **+0.55%**, a gap of just **0.15 percentage points**, which is inside the 0.5-point tolerance and ships no chip. The two readings agree because they measure the same thing from different ends: the reward schedule minus the burn is **+95M SKY** over 90 days, and the monitor sees the circulating figure rise by **+129M** — a 34M difference on a 23.4B base. SKY is best characterised as a **capped token whose inflation is a staking-reward payout, nearly fully offset by a buy-and-burn engine**.

## Sell pressure: where new SKY comes from

Sell #1, protocol inflation, is **419M SKY**, and it is the only meaningful source of new float on the token. Sky has no proof-of-work subsidy and no uncapped mint; the SKY supply sits under a fixed ceiling of about **23.46B**, of which **23.38B** is already circulating. What produces new float is the SKY staking-reward programme, which pays SKY to SKY stakers — the SKY-to-SKY reward system that replaced the older SKY-to-USDS rewards in November 2025. A rewards-normalization in early 2026 set the distribution at about **838M SKY over 180 days**, a cut of roughly 162M versus the prior schedule, which works out to **419M SKY** across this window. A monthly settlement executed on **Jul 20 2026** re-topped that buffer on the same track rather than changing the rate, so the forward row holds at 419M.

Sell #2, vesting unlocks, is **zero**, and the reason is a subtlety worth stating plainly. The MKR-to-SKY upgrade converts each MKR into **24,000 SKY**, and roughly **19%** of MKR is still unconverted — a 2% late-upgrade penalty has applied since December 2025 and rises over time. But the SKY reserved for that unconverted MKR is already minted and already inside the circulating figure, held by the converter contract. A conversion moves those coins from the converter to a holder without creating anything new, so it re-labels existing supply rather than adding to it; booking it as sell pressure would double-count. Sell #3, Foundation and unscheduled unlocks, is **zero** — the reward buffer and the converter reserve are protocol-controlled, but nothing moved out of them beyond the scheduled rewards. Sell #4, long-term locked or bankruptcy, is zero: there is no Sky estate, trustee or court-ordered distribution.

## Buy pressure: where new SKY goes

Buy #1, the programmatic buyback, is the mechanism that defines SKY, and unlike most buybacks it genuinely removes supply. The **Smart Burn Engine** spends protocol surplus, denominated in the USDS stablecoin, buying SKY on the open SKY/USDS market and then **permanently burning** what it buys. This matters for the framework: the purchased SKY is destroyed, not deposited into a liquidity pool and not accumulated in a treasury, so there is no buy-and-hold overhang that a supply monitor would keep counting as circulating. At the recent pace of about **3.6M SKY a day** the engine burned roughly **324M SKY** over the window, and it has removed more than **1.8B SKY** since the program began, funded by a protocol that reports rising revenue into 2026.

The other three buy rows are **zero**. Buy #2, protocol fee burn, is zero because Sky has no separate base-fee burn — the only SKY leaving supply is the Smart Burn Engine already counted in Buy #1, which is the thing doing the burning. Buy #3, Foundation buy, is zero because the protocol's only market buying is that same engine; no separate ecosystem entity has disclosed an open-market SKY purchase. Buy #4, new long-term lock, is zero: SKY staking has a short unstake path, so staked SKY stays effectively liquid rather than being removed from float, and no fixed-term lockup contract was deployed in the window.

## Foundation and overhang

Two protocol-controlled pools are tracked. The first is the **SKY staking-rewards buffer**, the source of Sell #1; it is replenished by monthly governance settlements — the most recent on **Jul 20 2026** — and it pays out on the published 838M-per-180-day schedule, so its release is scheduled rather than discretionary. The second is the **MKR-to-SKY converter reserve**, which holds the SKY still owed to the roughly 19% of MKR that has not upgraded; those coins are already inside the circulating figure, so their movement is a reclassification, not a release. Neither pool sold into the market outside the scheduled reward stream during the window. Each is re-read every rebuild, and if either balance falls between refreshes in a way that is not the scheduled reward, the outflow enters Sell #3 at the next refresh.

## How SKY compares to other capped governance tokens

The comparison that matters is emission versus burn under a hard ceiling. Many DeFi governance tokens still mint through liquidity-mining or staking curves, so their sell side scales with usage and has no natural end. SKY is capped near **23.46B** and pays its staking rewards out of a pre-funded buffer rather than by minting fresh supply above the cap, so its worst case is bounded — the reward stream is a reclassification of already-counted coins, not new issuance stacked on top.

The second comparison is burn versus buy-and-hold. Exchange tokens that run quarterly buybacks often keep the purchased supply in a treasury or a liquidity pool, where it remains re-deployable and still counts as circulating — which is why those buybacks and a supply monitor structurally disagree. Sky does the opposite: the **Smart Burn Engine** destroys what it buys, so the reduction is irreversible and shows up cleanly in every supply feed. That is why SKY's framework net and our monitor land within **0.15 points** of each other, where a buy-and-hold token would show a persistent gap. The trade-off is that the burn is funded by protocol revenue and therefore discretionary in size — if revenue falls, the offset shrinks and the token drifts more clearly positive.

## What to watch in the next 90 days

First, the burn pace: the Smart Burn Engine's daily buy is funded by USDS surplus, so any drop in protocol revenue would shrink the roughly **324M/90d** offset and tip the net more clearly positive. Second, the next monthly rewards settlement — the **Jul 20 2026** normalization held the 838M-per-180-day rate, but a future settlement could cut it, which would lower Sell #1 directly. Third, the MKR-to-SKY conversion, where about 19% of MKR is still unconverted under a rising late penalty; the conversions themselves are supply-neutral, but a wave of upgraders selling freshly received SKY would show up as real market pressure the framework does not currently book. Fourth, any governance move on the Smart Burn Engine's spend rate. Fifth, the Sky treasury restructuring that followed the Genesis Capital wind-down, in case it redirects surplus away from the burn.

## Summary

Sky is a capped governance token, so its inflation is not an emission in the usual sense but a reward payout: the SKY staking programme released about 419M SKY over 90 days on a fixed 838M-per-180-day schedule. Against that, the Smart Burn Engine bought and permanently burned roughly 324M SKY, about 3.6M a day, funded by protocol revenue. That leaves the framework at +0.41% net, close to flat, with our supply monitor at +0.55% — a 0.15-point gap that needs no explanation because both sides are measuring the same small drift. The key risk is that the burn is discretionary in size and depends on revenue holding up; the key structural fact is that the whole system operates under a fixed ~23.46B ceiling that governance cannot lift without redeploying the token.

*MrNasdog Pressure Framework analysis of Sky (SKY), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 28 2026.*

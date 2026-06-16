---
title: "FLR Inflation Analysis · June 2026 · Lower mint, bigger burn, supply still creeping up"
description: "A MrNasdog Pressure Framework read of Flare (FLR): ~632M / 90D of protocol inflation at the new 3% rate vs a ~62M fee burn. Framework +0.7% net; monitor +0.25%, the gap a gross-vs-float wedge."
canonical_url: "https://mrnasdog.com/research/flr/inflation"
tags: ["crypto", "flr", "flare", "inflation"]
published: true
---

> Originally published at **[mrnasdog.com/research/flr/inflation](https://mrnasdog.com/research/flr/inflation)** by MrNasdog.

Flare mints about **632M FLR** over the next 90 days as staking and oracle rewards, now that a governance vote cut the yearly inflation rate from **5% to 3%**. A new 20x gas-fee burn plus burned unclaimed rewards remove roughly **62M** back out, so the Pressure Framework reads about **+0.7% net**. Our supply monitor reads only **+0.25%** — a gap that comes from reward FLR re-staking, sitting unclaimed, or being burned rather than reaching the open market.

## The verdict, in one paragraph

For the 90-day window ending June 16 2026, the MrNasdog Pressure Framework reads **FLR at +0.7% net** on the forward view, driven by protocol inflation that out-issues the new fee burn. Our supply monitor reads the realized last-90-day change at **+0.25%**, versus the framework's **+1.05%** gross-mint read for the same window — a gap of about **0.8 percentage points** that ships a **⚠ monitor-gap chip**. The gap is structural: most of Flare's minted reward FLR is re-staked, held unclaimed in temporary pools, or burned if left unclaimed past its window, so on-chain float grows far slower than the gross mint. FLR is **structurally inflationary on the active float**, but at a low and falling single-digit pace.

## Sell pressure: where new FLR comes from

Sell #1 — protocol inflation — is the whole story, at about **632M FLR** over the next 90 days. Flare mints new FLR as rewards for FTSO oracle delegation, FLR staking, and FAssets participation, and the issuance is calculated on already-distributed FLR rather than on total supply. The FIP.16 governance proposal, accepted on **April 24 2026** with 98.06% support, cut the annual inflation rate from **5% to 3%** — a 40% reduction — with the emissions change taking effect around mid-May. The prior 90-day window straddled that cut and ran higher, near 904M, which is why the realized last-quarter mint was larger than the forward view.

Sell #2 — vesting unlocks — is **zero**: Flare's 36-month FlareDrop distribution, which paid out 24.2B FLR, finished on **January 30 2026**, before this window opened, so no scheduled distribution cliff reaches the market. Sell #3 — Foundation and unscheduled unlocks — is also zero, with no dated discretionary treasury or escrow release pending. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate or court distribution applies to FLR.

## Buy pressure: where new FLR goes

Buy #2 — protocol fee burn — is the active offset, at about **62M FLR** over 90 days. The same FIP.16 vote raised Flare's base gas fee 20x, a change going live around **end of June 2026**, and unclaimed inflation rewards are burned after their claim window expires. Together these lift the projected annual burn from roughly **7.5M every six months toward about 300M a year** at current activity. Buy #1 — programmatic buyback — is zero for now: Flare set up the FIRE revenue entity to buy and burn FLR on the open market, but it has no defined in-window quantum yet, so the framework carries it at zero and monitors it. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero.

## Foundation and overhang

FLR has no classic unlock overhang — the airdrop distribution is finished and the token is broadly distributed. What it does have is two structural pools tied to the reward system: temporary unearned-reward pools, funded by protocol penalties, where a fraction is recycled into core-protocol incentives and the rest is burned; and the reward stream itself, where any inflation reward left unclaimed past its window is burned rather than added to float. These are not a stockpile waiting to dump — they are exactly why realized float grows slower than the gross mint. The framework books no discretionary release beyond protocol inflation and re-checks the reward, burn, and chain emission figures on a roughly bi-weekly walk; if a treasury balance falls faster than the schedule, the outflow enters Sell #3 at the next refresh.

## How FLR compares to other uncapped proof-of-stake chains

FLR belongs to the class of **uncapped proof-of-stake L1s with a capped annual issuance** — closer to a continuous-emission chain than to a hard-capped, halving-model coin. Unlike a fixed-supply token, FLR has no ceiling; but because issuance is a percentage of already-distributed supply with a hard annual cap, the effective inflation rate falls over time and now sits at 3% gross. Unlike a pure inflation chain, FLR pairs the mint with a fee burn and burns of unclaimed rewards, so net dilution runs below the headline rate.

The contrast worth drawing is with chains that have flipped net-deflationary through aggressive fee burns. Flare's 20x gas-fee burn is a real brake, but at current activity it offsets only about a tenth of the gross mint, so it slows dilution rather than reversing it. For an inflation lens, that means FLR reads as mildly and decreasingly inflationary: the rate cut and the bigger burn both push net dilution down, while the FIRE buy-and-burn is a wildcard that could tighten supply further once it is funded and active.

## What to watch in the next 90 days

Watch the base-gas-fee burn going live around **June 30 2026** — the 20x increase is the single change that decides how much of the mint the burn can absorb. Watch the FIRE entity, since once it starts buying and burning FLR on the open market it would add a second, discretionary buy-side offset the framework currently carries at zero. Watch realized network activity, because both the gas-fee burn and FIRE revenue scale with usage, so a busier chain burns more. And expect the framework to keep reading above our supply monitor for as long as reward FLR re-stakes or sits unclaimed rather than reaching the float — that gap is structural, not a new unlock.

## Summary

FLR is an uncapped proof-of-stake token whose supply grows from staking and oracle rewards at a rate that a governance vote just cut from 5% to 3%. The chain mints about 632M FLR over the next 90 days, while a new 20x gas-fee burn plus burned unclaimed rewards remove roughly 62M, leaving the framework at about +0.7% net. Our supply monitor reads +0.25% realized, with the gap explained by reward FLR re-staking, sitting unclaimed, or being burned instead of reaching the open market. FLR stays mildly inflationary on the active float, with both the rate cut and the bigger burn pulling net dilution down.

*MrNasdog Pressure Framework analysis of Flare (FLR), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 16, 2026.*

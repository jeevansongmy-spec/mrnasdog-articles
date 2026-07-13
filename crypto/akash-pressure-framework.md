---
title: "AKT Inflation Analysis · July 2026 · A lower mint, still ahead of the burn"
description: "A MrNasdog Pressure Framework read of Akash Network (AKT): ~2.9M / 90D of staking inflation at a lowered 4% rate vs a ~1.0M usage burn. Framework +0.65% net; monitor +11.1%, the gap a supply reclassification."
canonical_url: "https://mrnasdog.com/research/akt/inflation"
tags: ["crypto", "akt", "akash-network", "depin"]
published: true
---

> Originally published at **[mrnasdog.com/research/akt/inflation](https://mrnasdog.com/research/akt/inflation)** by MrNasdog.

Akash Network now mints about **2.9M AKT** over 90 days as Cosmos-style staking rewards — down after governance cut the inflation ceiling to **4%** — while a usage-linked Burn-Mint Equilibrium burns roughly **1.0M** back out. New supply still edges ahead of the burn, so the Pressure Framework reads about **+0.65% net**. Our supply monitor reads **+11.1%** — a gap that comes from a circulating-supply reclassification, not from new issuance.

## The verdict, in one paragraph

For the 90-day window around July 14 2026, the MrNasdog Pressure Framework reads **AKT at +0.65% net** on the forward view — protocol inflation still out-issues the usage burn, but by far less than it used to. Our supply monitor reads the realized last-90-day change at **+11.1%**, versus the framework's **+0.65%** emission read for the same window — a gap of about **10.4 percentage points** that ships a **⚠ monitor-gap chip**. The gap is not new mint: the live on-chain mint runs at a **4%** yearly rate, producing only about **2.9M AKT** a quarter, and the burn removes ~**1.0M**, so the chain's own total supply grows only ~1.6M in 90 days. The monitor's much larger jump is a supply-classification catch-up — already-minted, previously-non-circulating AKT being re-tagged as freely tradable. AKT is **mildly inflationary**, and less so than before the inflation cut.

## Sell pressure: where new AKT comes from

Sell #1 — protocol inflation — is the whole story, at about **2.9M AKT** over the next 90 days. Akash Network is a Cosmos-SDK chain, so AKT is minted every block as staking rewards on a schedule that flexes with the bonded ratio. Governance recently lowered the mint band to a **4%** ceiling and a **3%** floor — down from the old 8% cap — and the live mint module currently sits at the **4%** top. Because roughly **82%** of AKT is staked, well above the 67% target, the rate is drifting toward the 3% floor over time. A community-pool tax routes half of each mint to community-directed spending, but every coin in that mint is freshly issued AKT, so it counts once, here.

Sell #2 — vesting unlocks — is **zero**: every original team, investor and seed allocation finished vesting back in March 2023, so AKT is fully unlocked and no cliff hits the market. The often-quoted "unlocks running into 2030" refer to ongoing block-reward emission, which is already captured in Sell #1, not a separate vesting overhang. Sell #3 — Foundation and unscheduled unlocks — is also zero as a flow; the community pool accrues continuously from the block reward and is governance-controlled, and no dated discretionary release to the open market was found in the window. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate or court distribution applies to AKT.

## Buy pressure: where new AKT goes

Buy #2 — the protocol burn — is the only active offset, at about **1.0M AKT** over 90 days. Since the Burn-Mint Equilibrium upgrade went live on **March 23 2026**, every dollar of compute spend burns AKT to mint a non-transferable compute credit; at settlement that credit is burned and AKT is re-minted to providers. The net burn has roughly doubled since launch — from about **6,000 AKT** a day in the first week to about **11,000 AKT** a day now — which works out to ~**1.0M** a quarter, and it scales directly with demand, so a busier quarter burns more. Buy #1 — programmatic buyback — is carried at zero: there is no revenue-funded treasury buyback running separately from the usage burn. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero, with no discretionary open-market buying or new escrow announced in the window.

## Foundation and overhang

AKT has no classic unlock overhang — the token is fully distributed and the vesting schedule physically expired in 2023. What it does have is one structural, continuous allocation inside the block reward itself: a community pool that receives half of every block's mint under the community-pool tax. That pool is not a stockpile waiting to dump; it is governance-controlled and spent on grants and ecosystem work over time — it even seeded the burn vault with 300,000 AKT. The framework books no discretionary release beyond protocol inflation and re-checks the community-pool balance and the burn pace on a roughly bi-weekly walk; if the pool's balance falls to the open market faster than grants explain, that outflow enters Sell #3 at the next refresh.

## How AKT compares to other uncapped staking chains

AKT belongs to the class of **Cosmos-SDK staking chains with a bonded-ratio emission curve** — closer to a continuous-emission proof-of-stake L1 than to a hard-capped, halving-model coin. Like Cosmos Hub's ATOM, AKT mints new supply each block to pay stakers, with the rate flexing around a target bonded ratio rather than following a fixed halving. Its recent inflation cut to a 4% ceiling puts it on the lower end of that class — many Cosmos chains still mint in the high single digits or low teens. It does carry a stated maximum supply of 388.5M, but that ceiling is distant — circulating sits near 292M — so the cap is not a near-term brake the way a fully-emitted hard cap would be.

The contrast worth drawing is with exchange tokens that burn aggressively enough to go net-deflationary, or with fixed-supply coins that issue nothing at all. AKT's Burn-Mint Equilibrium is a genuine demand-linked burn, which is unusual for a Cosmos chain — and with the mint now lower, the burn covers a larger share of issuance than it did at launch. But at current adoption it still offsets only about a third of the mint, so it slows dilution rather than reversing it. For an inflation lens specifically, AKT reads as mildly inflationary: the staking emission is the dominant force, the usage burn is a growing partial brake, and the network would need compute demand an order of magnitude higher to tip net-deflationary.

## What to watch in the next 90 days

Watch the Burn-Mint Equilibrium burn pace — the ~11,000 AKT daily run-rate is the single number that decides whether net inflation keeps easing, since the burn scales with compute spend. Watch compute revenue, because that is what funds the burn; a strong AI-demand quarter lifts it. Note that with ~82% of AKT staked the live mint rate is drifting from the 4% ceiling toward the 3% floor, which slowly lowers Sell #1 on its own. Track any further governance move on the inflation band, since a future vote could lower it again. And expect the framework to keep reading far below our supply monitor for as long as the monitor is absorbing a one-time circulating-supply reclassification — that gap is classification, not a new unlock.

## Summary

AKT is a Cosmos-SDK staking token whose supply grows on a bonded-ratio emission curve. After a governance cut to a 4% ceiling, the chain now mints about 2.9M AKT over 90 days, while a usage-linked Burn-Mint Equilibrium burns roughly 1.0M back out, leaving the framework at about +0.65% net — mildly inflationary, and less so than before. Our supply monitor reads +11.1% realized, with the gap explained by a circulating-supply reclassification rather than new issuance. The demand-linked burn slows dilution rather than reversing it, and a distant 388.5M cap is not a near-term constraint.

*MrNasdog Pressure Framework analysis of Akash Network (AKT), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 14, 2026.*

---
title: "AKT Inflation Analysis · June 2026 · Staking emission still ahead of the burn"
description: "A MrNasdog Pressure Framework read of Akash Network (AKT): ~6.4M / 90D of staking inflation vs a ~0.5M usage burn. Framework +2% net; monitor +11.6%, the gap a supply reclassification."
canonical_url: "https://mrnasdog.com/research/akt/inflation"
tags: ["crypto", "akt", "akash-network", "depin"]
published: true
---

> Originally published at **[mrnasdog.com/research/akt/inflation](https://mrnasdog.com/research/akt/inflation)** by MrNasdog.

Akash Network mints about **6.4M AKT** over 90 days as Cosmos-style staking rewards, while a usage-linked Burn-Mint Equilibrium burns roughly **0.5M** back out. New supply stays well ahead of the burn, so the Pressure Framework reads about **+2.0% net**. Our supply monitor reads **+11.6%** — a gap that comes from a circulating-supply reclassification, not from new issuance.

## The verdict, in one paragraph

For the 90-day window ending June 30 2026, the MrNasdog Pressure Framework reads **AKT at +2.0% net** on the forward view, driven by protocol inflation that far out-issues the usage burn. Our supply monitor reads the realized last-90-day change at **+11.6%**, versus the framework's **+2.0%** emission read for the same window — a gap of about **9.6 percentage points** that ships a **⚠ monitor-gap chip**. The gap is not new mint: staking emission at the current **8.9%** yearly rate produces only about **6.4M AKT** a quarter, so the monitor's much larger jump is a supply-classification catch-up — already-minted, previously-non-circulating AKT being re-tagged as freely tradable. AKT is **structurally inflationary**, at a mid-single-digit annual pace.

## Sell pressure: where new AKT comes from

Sell #1 — protocol inflation — is the whole story, at about **6.4M AKT** over the next 90 days. Akash Network is a Cosmos-SDK chain, so AKT is minted every block as staking rewards on a declining schedule that trends toward a target bonded ratio; the realized rate sits near **8.9%** a year, just above the **8%** nominal cap set by governance, with a **4%** floor underneath it. A **50%** community-pool tax routes half of each mint to community-directed spending, but every coin in that mint is freshly issued AKT, so it counts once, here.

Sell #2 — vesting unlocks — is **zero**: every original team, investor and seed allocation finished vesting back in March 2023, so AKT is fully unlocked and no cliff hits the market. The often-quoted "unlocks running into 2030" refer to ongoing block-reward emission, already captured in Sell #1, not a separate vesting overhang. Sell #3 — Foundation and unscheduled unlocks — is also zero as a flow; the community pool accrues continuously from the block reward and is governance-controlled, and no dated discretionary release to the open market was found. Sell #4 — long-term locked or bankruptcy — is zero.

## Buy pressure: where new AKT goes

Buy #2 — the protocol burn — is the only active offset, at about **0.5M AKT** over 90 days. Since the Burn-Mint Equilibrium upgrade went live on **March 23 2026**, every dollar of compute spend burns AKT to mint a non-transferable compute credit; at settlement that credit is burned and AKT is re-minted to providers. At today's usage the net burn runs near **6,000 AKT** a day — about **0.5M** a quarter — and scales directly with demand, so a busier quarter burns more. Buy #1 — programmatic buyback — is carried at zero: there is no revenue-funded treasury buyback running separately from the usage burn. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero.

## Foundation and overhang

AKT has no classic unlock overhang — the token is fully distributed and the vesting schedule physically expired in 2023. What it does have is one structural, continuous allocation inside the block reward itself: a community pool that receives half of every block's mint under the 50% community-pool tax. That pool is not a stockpile waiting to dump; it is governance-controlled and spent on grants and ecosystem work over time. The framework books no discretionary release beyond protocol inflation and re-checks the community-pool balance and the burn pace on a roughly bi-weekly walk; if the pool's balance falls to the open market faster than grants explain, that outflow enters Sell #3 at the next refresh.

## How AKT compares to other uncapped staking chains

AKT belongs to the class of **Cosmos-SDK staking chains with a bonded-ratio emission curve** — closer to a continuous-emission proof-of-stake L1 than to a hard-capped, halving-model coin. Like Cosmos Hub's ATOM, AKT mints new supply each block to pay stakers, with the rate flexing around a target bonded ratio rather than following a fixed halving. It does carry a stated maximum supply of 388.5M, but that ceiling is distant — circulating sits near 292M — so the cap is not a near-term brake the way a fully-emitted hard cap would be.

The contrast worth drawing is with exchange tokens that burn aggressively enough to go net-deflationary, or with fixed-supply coins that issue nothing at all. AKT's Burn-Mint Equilibrium is a genuine demand-linked burn, which is unusual for a Cosmos chain — but at current adoption it offsets only a small fraction of the mint, so it slows dilution rather than reversing it. For an inflation lens specifically, AKT reads as steadily inflationary: the staking emission is the dominant force, and the usage burn is a partial brake that grows only as compute demand grows.

## What to watch in the next 90 days

Watch the Burn-Mint Equilibrium burn pace — the ~6,000 AKT daily run-rate is the single number that decides whether net inflation eases, since the burn scales with compute spend. Watch compute revenue, because that is what funds the burn; a strong AI-demand quarter lifts it. Note any governance move on the inflation parameters, since the realized rate runs just above the 8% cap and a future vote could lower it toward the 4% floor. Track the AEP-79 shared-security migration discussion, which could change how staking emission is paid if Akash moves to a shared-security model. And expect the framework to keep reading far below our supply monitor for as long as the monitor is absorbing a one-time circulating-supply reclassification — that gap is classification, not a new unlock.

## Summary

AKT is a Cosmos-SDK staking token whose supply grows on a bonded-ratio emission curve. The chain mints about 6.4M AKT over 90 days at the current 8.9% rate, while a usage-linked Burn-Mint Equilibrium burns roughly 0.5M back out, leaving the framework at about +2.0% net. Our supply monitor reads +11.6% realized, with the gap explained by a circulating-supply reclassification rather than new issuance. AKT stays structurally inflationary, with the demand-linked burn slowing dilution rather than reversing it — and a distant 388.5M cap that is not a near-term constraint.

*MrNasdog Pressure Framework analysis of Akash Network (AKT), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 30, 2026.*

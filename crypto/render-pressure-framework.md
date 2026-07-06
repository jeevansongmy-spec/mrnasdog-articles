---
title: "RENDER Inflation Analysis · July 2026 · The burn sits level with the mint"
description: "A MrNasdog Pressure Framework read of Render Network (RENDER): ~0.36M/90D of released emissions vs a ~0.36M job burn under burn-mint equilibrium. Framework ~flat net; monitor +0.03%; biased deflationary as Salad ramps."
canonical_url: "https://mrnasdog.com/research/render/inflation"
tags: ["crypto", "render", "render-network", "solana"]
published: true
---

> Originally published at **[mrnasdog.com/research/render/inflation](https://mrnasdog.com/research/render/inflation)** by MrNasdog.

**TL;DR.** Render Network runs on a burn-mint equilibrium: about **0.36M RENDER** reaches the market over 90 days as node-operator rewards and grants, while roughly **0.36M** is burned as customers pay for render and AI-compute jobs. The two nearly cancel, so the framework reads about **flat** net. Our supply monitor agrees, reading **+0.03%** realized over the last 90 days — essentially no change — with a newly integrated compute subnet biasing the balance toward deflation from here.

## The verdict, in one paragraph

For the 90-day window ending July 6 2026, the MrNasdog Pressure Framework reads **RENDER at roughly 0.00% net**. The reason is structural: Render Network is built around a **Burn-Mint Equilibrium**, where RENDER is burned to pay for work and new RENDER is minted to reward the operators who do it. When usage and emissions are balanced, those two flows roughly offset and net supply barely moves. Our supply monitor reads the realized last-90-day change at **+0.03%** — three hundredths of a percentage point, within the framework's flat reading, so no gap chip is needed. RENDER is, on the active float, **about as close to supply-neutral as a working token gets**, and the newly approved Salad subnet is engineered to tip that balance gently deflationary as it ramps.

## Sell pressure: where new RENDER comes from

Sell #1 — protocol inflation — is the only active source, and it is smaller than it first looks. Render Network mints new RENDER as rewards to GPU node operators and as artist and AI grants, on a governed, declining schedule paid out epoch by epoch, roughly weekly. The current year (Year 3 of the Burn-Mint Equilibrium, set by governance proposal RNP-022) authorizes about **5.9M RENDER** across node rewards, grants, and operations — split roughly 1.5M node rewards, 1.5M grants, and 2.9M operations, and the emission steps down each year from 9.1M in Year 1 and 5.9M in Year 2. But only the node-reward and grant slice that is **actually released** reaches the open market — about **0.36M over 90 days**. The large operations bucket stays locked by the Foundation and does not enter circulating supply until it is spent, so the framework counts the released amount, not the full authorized ceiling.

Sell #2 — vesting unlocks — is **zero**: the original RNDR token sale and team allocations finished vesting long ago, and no dated cliff falls inside this window. Sell #3 — Foundation and unscheduled unlocks — is also zero as a flow; there is no public evidence of a discretionary Foundation release in the window, and the locked operations emissions are tracked but not projected forward until they actually move. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate or court distribution applies to RENDER.

## Buy pressure: where RENDER is removed

Buy #2 — protocol fee burn — is the whole offset, at about **0.36M RENDER** over 90 days. Every render or AI-compute job is paid in RENDER, and 95% of that spend is burned the moment the work completes — destroyed permanently, not parked in a treasury, with 5% kept by the Foundation. Job burns grew sharply through 2025, up roughly **279%** year over year, and cumulative burns crossed **1.22M** coins and kept climbing, with a recent epoch alone burning about 20.5K RENDER. At the current pace the burn runs level with the released mint, which is exactly what a burn-mint equilibrium is designed to do when usage is healthy — and rising usage tips it toward net deflation.

Buy #1 — programmatic buyback — is zero: RENDER has no open-market buyback, because its supply offset is the job burn rather than a treasury buying coins back. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero, with no discretionary open-market buying or new escrow announced in the window.

## Foundation and overhang

RENDER's main overhang is not a vesting cliff — it is the **Foundation-locked operations emissions**, the roughly 2.9M slice of the 5.9M yearly authorization. These coins are minted on paper but held back, released only as the Foundation spends on operations, research and growth, and they do not count as circulating until they move. That is why the framework books Sell #1 at the released amount rather than the full 5.9M: counting the locked bucket as market supply would overstate dilution. A new subnet integration, **RNP-023** — approved **April 8 2026** to bring the Salad Network onto RENDER — pulls a portion of monthly operations emissions forward to fund subnet rewards, but it keeps the overall emissions cap unchanged, so the overhang ceiling is the same. The framework re-checks the monthly Foundation reports on a regular walk; if that locked balance starts falling faster than usage explains, the outflow enters Sell #3 at the next refresh.

## How RENDER compares to other burn-mint tokens

RENDER belongs to the class of **burn-mint utility tokens** — supply rises with emissions and falls with usage, and net inflation depends on which side is winning. Unlike a hard-capped, halving-model coin, RENDER has no fixed scarcity floor in the short run; unlike a pure inflation chain, it has a real demand-driven sink that can fully offset the mint. The result is a token whose net supply tracks how much work the network is actually doing: heavy usage burns more than is minted and the supply shrinks, while quiet periods let the mint edge ahead.

Right now the two sides sit almost exactly in balance — the healthiest state for this design, because the network is busy enough that job burns roughly match the rewards paid to keep operators online. The emissions schedule is also declining over time, stepping down each year and halving further out, so the mint side has a built-in downward drift. The newly approved **RNP-023**, which brings the Salad Network — **60,000** or more daily-active consumer GPUs in 180-plus countries — onto RENDER as a third subnet, is deliberately structured so its burns exceed its mints from day one, pushing RENDER further toward deflation as that usage ramps. For an inflation lens, RENDER reads as **supply-neutral today and structurally biased toward deflation** as long as usage holds up.

## What to watch in the next 90 days

Watch the monthly burn figures — the single number that decides whether RENDER tips deflationary or inflationary is how much compute the network sells, because that is what gets burned. Watch the ramp of the RNP-023 Salad subnet, integrating 60,000-plus consumer GPUs; its burns are engineered to outpace its mints, so a strong ramp would deepen the deflationary lean. Watch the released emissions in the monthly Foundation reports, since a faster draw on the locked operations bucket would add supply the framework would move into Sell #3. Note that the current emissions year runs through **December 19 2026**, after which a Year-4 governance proposal would set the next step-down — none has been filed yet. And expect net supply to keep hovering near flat for as long as job burns and released rewards stay matched — the balance is the design, not a coincidence.

## Summary

RENDER is a burn-mint utility token on Solana whose supply rises with operator rewards and falls with job burns. About 0.36M RENDER reaches the market over 90 days as released emissions, while roughly 0.36M is burned paying for render and AI jobs, leaving the framework at about flat net. Our supply monitor reads +0.03% realized — essentially the same, so no gap chip is needed. RENDER stays close to supply-neutral on the active float, with a declining emissions schedule, rising usage, and the newly approved Salad subnet all nudging it further toward the deflationary side over time.

---

*MrNasdog Pressure Framework analysis of Render Network (RENDER), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 6, 2026.*

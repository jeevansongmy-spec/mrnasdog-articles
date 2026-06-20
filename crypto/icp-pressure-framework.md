---
title:         "ICP Inflation Analysis · June 2026 · Supply growing, but the burn is closing the gap"
description:   "Supply still grows, but the burn is closing in: the Internet Computer mints ~11.8M ICP/90d vs a ~7.6M cycles burn. Framework reads +0.8% net (monitor +0.75%)."
canonical_url: "https://mrnasdog.com/research/icp/inflation"
tags:          ["crypto", "icp", "internet-computer", "layer1"]
published:     true
---

*Originally published at [mrnasdog.com/research/icp/inflation](https://mrnasdog.com/research/icp/inflation)*

The Internet Computer mints about **11.8M ICP** over 90 days for node-provider and governance voting rewards, while converting ICP to cycles for compute burns roughly **7.6M** back out. New supply still leads the burn, so the framework reads about **+0.8%** net. Our supply monitor reads **+0.75%** over the same window — the two agree, because ICP is fully unlocked and total supply equals circulating supply.

## The verdict, in one paragraph

For the 90-day window ending June 16 2026, the MrNasdog Pressure Framework reads **ICP at +0.8% net** on the forward view, driven by reward minting that still out-issues the cycles burn. Our supply monitor reads the realized last-90-day change at **+0.75%**, versus the framework's **+0.74%** read for the same window — a gap of about **0.01 percentage points**, well inside tolerance, so no monitor-gap chip is needed. Because ICP carries no locked overhang and its total supply equals its circulating supply, the framework's mint-minus-burn math lands almost exactly on the monitor's realized number. ICP is **mildly inflationary and trending toward balance**, with a deliberate plan to push the burn past the mint.

## Sell pressure: where new ICP comes from

Sell #1 — protocol inflation — is the whole sell side, at about **11.8M ICP** over the next 90 days. New ICP is minted to pay two reward streams: node-provider rewards for the machines that run the network, and governance voting rewards for ICP staked in neurons. Under the Mission70 plan published in January 2026, the gross minting rate is being cut step by step from roughly **9.72%** a year toward about **5.42%** a year by January 2027, so this stream is easing across the window rather than holding flat. Both reward types are newly issued supply, so they count once, here.

Sell #2 — vesting unlocks — is **zero** as a separate flow: genesis allocations release on a long linear schedule with no cliff in this window, and the reward maturity that unlocks from neurons is re-minted ICP already captured in protocol inflation above. Sell #3 — Foundation and unscheduled unlocks — is also zero; the Foundation's holdings sit in long-dissolve-delay neurons and there is no dated discretionary release pending. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate or court distribution applies to ICP.

## Buy pressure: where new ICP goes

Buy #2 — protocol fee burn — is the active offset, at about **7.6M ICP** over 90 days. ICP is burned whenever it is converted to cycles, the gas that developers spend on compute, storage and bandwidth, so every canister running on the network quietly removes supply. This burn is usage-driven and has been climbing — the early-2026 burn rate ran roughly double the late-2025 average — which is exactly the lever Mission70 is trying to amplify. Buy #1 — programmatic buyback — is carried at zero for now: the new cloud-engine model routes **20%** of compute revenue into buying and burning ICP, but it is still rolling out and not yet quantified on-chain in this window. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero, with no discretionary open-market buying or new escrow announced beyond ordinary neuron staking.

## Foundation and overhang

ICP has no classic unlock overhang in the trader's sense — total supply equals circulating supply, so there is no locked bucket waiting to flood the float. The DFINITY Foundation does hold a meaningful ICP position, but it is staked in neurons with long dissolve delays, which means it cannot be sold quickly and earns voting rewards rather than sitting idle. The framework books no discretionary release beyond protocol inflation and re-checks the reward minting and cycles burn on a roughly bi-weekly walk; if a Foundation neuron began dissolving and its balance fell between refreshes, that outflow would enter Sell #3 at the next refresh.

## How ICP compares to other uncapped proof-of-stake chains

ICP belongs to the class of **uncapped layer-1s that pair reward minting with a usage-driven burn** — structurally closer to a fee-burning smart-contract chain than to a hard-capped, halving-model coin. Unlike a fixed-supply token, ICP has no ceiling; unlike a pure inflation chain, it destroys ICP every time the network is used for compute. The result is a tug-of-war: minting adds supply for security and governance, while the cycles burn subtracts it in proportion to real demand.

The contrast worth drawing is with chains where the burn is large enough to flip net-deflationary during heavy usage. ICP is not there yet — the mint still leads the burn — but Mission70 is explicitly engineered to close that gap, both by cutting reward minting and by adding the cloud-engine buy-and-burn. For an inflation lens specifically, that means ICP reads as mildly inflationary today, with a credible, mechanism-based path toward flat or deflationary if compute demand keeps rising while issuance falls.

## What to watch in the next 90 days

Watch the cycles burn rate — it is the single number that decides whether ICP drifts toward flat, and it scales directly with network usage. Watch the Mission70 minting cuts as they take effect, since each step lowers the reward issuance that feeds Sell #1. Watch the cloud-engine buy-and-burn rollout; once 20% of compute revenue is reliably buying and burning ICP on-chain, Buy #1 stops being zero and the buy side grows. And watch any change in the Foundation's neuron position, which is the only large holding that could add a discretionary sell flow if it began dissolving.

## Summary

ICP is an uncapped layer-1 whose supply grows when reward minting outpaces the cycles burn. The network mints about 11.8M ICP over 90 days for node-provider and voting rewards, while converting ICP to cycles for compute burns roughly 7.6M back out, leaving the framework at about +0.8% net. Our supply monitor reads +0.75% realized — the two agree almost exactly because ICP is fully unlocked. The key risk is that minting stays ahead of the burn, and the key opportunity is Mission70, which is cutting issuance and scaling the burn toward a deflationary flip.

---

*MrNasdog Pressure Framework analysis of Internet Computer (ICP), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 16, 2026.*

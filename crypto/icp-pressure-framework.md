---
title: "ICP Inflation Analysis · July 2026 · Supply growing, but the mint is easing"
description: "A MrNasdog Pressure Framework read of Internet Computer (ICP): ~3.8M / 90D of reward minting vs a ~0.2M cycles burn. Framework +0.6% net; monitor +0.54%, and on-chain supply confirms it."
canonical_url: "https://mrnasdog.com/research/icp/inflation"
tags: ["crypto", "icp", "internet-computer", "compute"]
published: true
---

> Originally published at **[mrnasdog.com/research/icp/inflation](https://mrnasdog.com/research/icp/inflation)** by MrNasdog.

The Internet Computer mints about **3.8M ICP** over 90 days to reward node operators and governance voters, while compute demand burns roughly **0.2M ICP** back out. New supply stays well ahead of the burn, so the Pressure Framework reads about **+0.6% net**. Our supply monitor reads **+0.54%** — the two agree, and the on-chain total supply confirms it, rising from 550.7M to 554.3M over the window.

## The verdict, in one paragraph

For the 90-day window ending July 4 2026, the MrNasdog Pressure Framework reads **ICP at +0.6% net**, driven by protocol minting that far out-issues the cycle burn. Our supply monitor reads the realized last-90-day change at **+0.54%**, versus the framework's **+0.64%** read for the same window — a gap of about **0.1 percentage points**, inside tolerance, so no data-conflict chip is shipped. The two readings agree because ICP's net is directly observable: total supply is minted ICP minus burned ICP, and it rose **+3.57M** on-chain across the window. ICP is **structurally inflationary but decelerating** — new coins still exceed burned coins, but the Mission70 upgrade is stepping the mint rate down through 2026.

## Sell pressure: where new ICP comes from

Sell #1 — protocol inflation — is the whole story, at about **3.8M ICP** over the next 90 days. The Internet Computer mints new ICP for two purposes: to pay **node providers** who operate the machines hosting the network, and to reward **governance voters** who stake ICP in NNS neurons. Node-provider rewards ran about **2.4M ICP** across three monthly reward events in the window, and disbursed voting-reward maturity added roughly **1.4M ICP** more. The Mission70 upgrade, approved by NNS governance in April 2026, is cutting the annual minting rate from **9.72%** toward the low-single digits by early 2027, so this row eases quarter over quarter.

Sell #2 — vesting unlocks — is **zero**: the original seed allocation vested on a four-year schedule that finished in 2025, so no team, seed or investor cliff hits the market. Sell #3 — Foundation and unscheduled unlocks — is also zero as a flow; the foundation and team hold their ICP inside staked NNS neurons that already count as circulating, and no dated discretionary release is pending. Sell #4 — long-term locked or bankruptcy — is zero.

## Buy pressure: where new ICP goes

Buy #2 — protocol fee burn — is the only active offset, at about **0.2M ICP** over 90 days. Every computation, byte of storage, and unit of bandwidth on the Internet Computer is paid in **cycles**, and ICP is destroyed when it is converted into cycles — a real, on-chain deflationary sink. At the current usage the cycle burn ran roughly **0.2M ICP** over the window, far below the mint. Buy #1 — programmatic buyback — is zero, because the protocol runs no open-market buyback of ICP. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero.

## Foundation and overhang

ICP has no classic unlock overhang — the four-year genesis vesting completed in 2025, and the token is fully distributed. The DFINITY foundation, the team, and early backers hold their ICP inside **staked NNS neurons**, which the supply count already treats as circulating rather than as locked reserve. These neurons earn voting rewards and can in principle be dissolved on their configured delay, but there is no dated cliff and no announced sale program. The framework books no discretionary release beyond protocol minting and re-checks the reward events and cycle burn on a roughly bi-weekly walk; if a foundation neuron balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How ICP compares to other uncapped compute chains

ICP belongs to the class of **uncapped, continuous-emission L1s that pair minting with a usage-driven burn** — structurally closer to a fee-burning smart-contract chain than to a hard-capped, halving-model coin. Unlike a fixed-supply token, ICP has no ceiling and mints continuously to secure the network; unlike a pure inflation chain, it destroys ICP whenever compute is paid for. The distinctive feature is that both sides are directly measurable on-chain, so net supply change is observed rather than estimated.

The contrast worth drawing is with chains whose fee burn is large enough to flip net-deflationary in busy periods. ICP's cycle burn is real but small today — under a tenth of the gross mint — so it slows dilution rather than reversing it. What makes ICP unusual is that the mint side, not the burn side, is the lever being pulled: the Mission70 upgrade is cutting issuance directly, so net inflation trends down through 2026 even without a bigger burn. For an inflation lens, ICP reads as mildly inflationary and decelerating.

## What to watch in the next 90 days

Watch the Mission70 rate step-downs — the single biggest lever on ICP's net inflation is the minting schedule, and each scheduled cut lowers Sell #1 again. Watch the cycle burn rate, since heavier compute demand raises the burn and narrows net inflation from the other side. Watch node-provider reward events, which post monthly and set most of the mint. And watch for any change to how staked neurons are counted, though none is pending. If the mint keeps easing and the burn holds, ICP's net could approach flat later in 2026.

## Summary

ICP is an uncapped compute-network token whose supply is minted for node operators and voters and burned when converted into cycles for compute. The network mints about 3.8M ICP over 90 days while the cycle burn removes roughly 0.2M, leaving the framework at about +0.6% net — matched by our supply monitor at +0.54% and by the on-chain total supply, which rose +3.57M over the window. ICP stays mildly inflationary, with the burn far below the mint, but the Mission70 upgrade is stepping the mint rate down, so the trend points toward slower growth.

*MrNasdog Pressure Framework analysis of Internet Computer (ICP), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 4, 2026.*

---
title: "KAIA Inflation Analysis · June 2026 · The fee burn now cancels the mint"
description: "A MrNasdog Pressure Framework read of Kaia (KAIA): ~74.6M / 90D block-reward mint vs an ~80M on-chain fee burn. Framework −0.09% net; monitor agrees at −0.09%, no gap."
canonical_url: "https://mrnasdog.com/research/kaia/inflation"
tags: ["crypto", "kaia", "klaytn", "fee-burn"]
published: true
---

> Originally published at **[mrnasdog.com/research/kaia/inflation](https://mrnasdog.com/research/kaia/inflation)** by MrNasdog.

Kaia mints about **74.6M KAIA** over 90 days at a fixed **9.6** per block, while an on-chain fee burn removes roughly **80M** over the same window. The burn runs just ahead of the mint, so the Pressure Framework reads about **−0.09% net** — supply essentially flat, edging down. Our supply monitor reads the same realized **−0.09%**, so the two agree and no gap chip is needed.

## The verdict, in one paragraph

For the 90-day window ending June 16 2026, the MrNasdog Pressure Framework reads **KAIA at −0.09% net** on the forward view, as an on-chain fee burn of roughly **80M KAIA** slightly out-paces a fixed block-reward mint of about **74.6M KAIA**. Our supply monitor reads the realized last-90-day change at **−0.09%** as well — the two numbers line up, the gap is **0.00 percentage points**, and the page ships **no monitor-gap chip**. KAIA is best described as a **roughly flat, burn-balanced proof-of-stake chain**: new issuance is real and continuous, but the fee burn now matches it, so net dilution is essentially nil.

## Sell pressure: where new KAIA comes from

Sell #1 — protocol inflation — is the whole story, at about **74.6M KAIA** over the next 90 days. Kaia is an uncapped proof-of-stake EVM chain that mints a fixed **9.6 KAIA** per block at roughly one-second block times, which works out to about **300M KAIA** a year, or near **5.2%** nominal issuance. That mint is split across validators and stakers, the Kaia Ecosystem Fund and the Kaia Infrastructure Fund — but all three slices are newly issued supply, so they count once, here.

Sell #2 — vesting unlocks — is **zero**: roughly 100% of KAIA total supply already circulates, and the original merger reserves were destroyed through scheduled treasury burns before this window, so no team, seed or reserve cliff hits the market. Sell #3 — Foundation and unscheduled unlocks — is also zero as a flow; the Ecosystem and Infrastructure funds are fed continuously inside the block reward already counted in Sell #1. Sell #4 — long-term locked or bankruptcy — is zero.

## Buy pressure: where new KAIA goes

Buy #2 — protocol fee burn — is the only active offset, and it is a big one, at about **80M KAIA** over 90 days. Since the Kore hardfork, Kaia burns most of every block's gas fee on-chain, tracked directly in the chain's own supply accounting as burnt fees plus dead-address burns. Across the window that burn ran just ahead of the **9.6**-per-block mint, so the chain's net total supply actually edged down rather than up. Buy #1 — programmatic buyback — is zero: Kaia manages supply through fee burning, not open-market buybacks. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero.

## Foundation and overhang

KAIA has no classic unlock overhang — the token is fully distributed, and the merger-era reserves were already removed through the KIP-103 and KIP-160 treasury rebalances that burned the surplus rather than releasing it. What remains are two structural, continuous allocations inside the block reward itself: the Ecosystem Fund and the Infrastructure Fund, each receiving a fixed quarter of every block's mint. These are not a stockpile waiting to dump; they are already counted as new issuance in Sell #1. The framework books no discretionary release beyond protocol inflation and re-checks the on-chain burn and emission on a roughly bi-weekly walk; if a fund balance falls faster than the schedule, the outflow enters Sell #3 at the next refresh.

## How KAIA compares to other uncapped proof-of-stake chains

KAIA belongs to the class of **uncapped proof-of-stake L1s that pair a fixed block reward with a fee burn** — structurally the same shape as Ethereum after EIP-1559, rather than a hard-capped, halving-model coin. Unlike a fixed-supply token, KAIA has no ceiling; unlike a pure inflation chain, it burns most of its gas fees on-chain. The result is a net figure that hovers around zero and tips deflationary whenever network activity lifts the burn above the steady mint — which is exactly what the window shows.

The contrast worth drawing is with chains whose issuance always wins because they have no burn, and with exchange tokens that burn aggressively from revenue rather than from gas. KAIA sits in the middle: a constant **9.6**-per-block mint sets a fixed inflation floor, and a usage-linked burn claws it back. For an inflation lens, that means KAIA reads as essentially flat — the mint and the burn are close enough that net supply barely moves, and the balance can flip slightly deflationary in busier weeks.

## What to watch in the next 90 days

Watch on-chain network activity — because the burn is fee-driven, a busier chain burns more and pushes net supply further below zero, while a quiet stretch lets the fixed mint edge back ahead. Watch any governance proposal touching the 9.6-per-block reward, since the emission parameter is adjustable by governance and a change there moves Sell #1 directly. Watch for any new gas-abstraction rollout that lets users pay fees in stablecoins, which could thin the KAIA fee burn over time. And expect the framework to keep tracking our supply monitor closely for as long as the mint and burn stay this evenly matched — there is no unlock overhang to surprise the reading.

## Summary

KAIA is an uncapped proof-of-stake fuel token whose supply is held nearly flat by a fee burn that now cancels the block mint. The chain mints about 74.6M KAIA over 90 days at a fixed 9.6 per block, while an on-chain fee burn removes roughly 80M, leaving the framework at about −0.09% net. Our supply monitor reads the same −0.09% realized, so the two agree and no gap chip ships. The key risk is the reverse of today's balance: if activity falls, the fixed mint can edge back ahead of the burn, and because supply is uncapped there is no ceiling to stop slow dilution if that happens.

*MrNasdog Pressure Framework analysis of Kaia (KAIA), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 16, 2026.*

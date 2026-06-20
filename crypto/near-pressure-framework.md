---
title: "NEAR Inflation Analysis · June 2026 · Halved mint, with a fee buyback closing in"
description: "A MrNasdog Pressure Framework read of NEAR Protocol (NEAR): ~8M / 90D of halved 2.5% epoch issuance vs a fee-funded buyback-and-burn. Framework +0.4% net; monitor +0.74%, a small clean gap."
canonical_url: "https://mrnasdog.com/research/near/inflation"
tags: ["crypto", "near", "near-protocol", "proof-of-stake"]
published: true
---

> Originally published at **[mrnasdog.com/research/near/inflation](https://mrnasdog.com/research/near/inflation)** by MrNasdog.

NEAR Protocol mints about **8M NEAR** over 90 days at its new **2.5%** yearly maximum — half the old rate after the October 2025 halving upgrade — while a fee-funded buyback and a gas burn remove roughly **2.5M** back out. The mint still leads, so the Pressure Framework reads about **+0.4% net**. Our supply monitor reads **+0.74%** realized — a small gap, well inside tolerance, with no warning chip.

## The verdict, in one paragraph

For the 90-day window ending June 16 2026, the MrNasdog Pressure Framework reads **NEAR at +0.42% net** on the forward view, with protocol inflation still out-issuing the combined buyback-and-burn. Our supply monitor reads the realized last-90-day change at **+0.74%**, versus the framework's **+0.42%** read for the same window — a gap of about **0.3 percentage points**, inside the half-point tolerance, so **no monitor-gap chip ships**. The small residual is realized epoch issuance running near the 2.5% maximum while less than half the supply is staked. NEAR is now **mildly inflationary and trending toward neutral**: the October 2025 halving cut the mint in half, and a growing fee-funded buyback is steadily eating the rest.

## Sell pressure: where new NEAR comes from

Sell #1 — protocol inflation — is the whole story, at about **8M NEAR** over the next 90 days. NEAR Protocol mints new NEAR every epoch to reward validators, and the Halving Upgrade (Protocol Version 81), completed on mainnet October 30 2025, cut the maximum annual issuance from **5% to 2.5%**. At the new rate, 2.5% of the ~1.3B circulating supply over a quarter is roughly 8M NEAR, split **90% to validators** and **10% to the protocol treasury** — all newly issued, so it counts once, here.

Sell #2 — vesting unlocks — is **zero**: roughly 99% of all NEAR is already circulating and the token is fully unlocked, so no team, backer or treasury cliff hits the market in the window. Sell #3 — Foundation and unscheduled unlocks — is also zero as a flow, with no dated discretionary release of foundation or treasury NEAR pending. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate or court distribution applies to NEAR.

## Buy pressure: where new NEAR goes

Buy #1 — programmatic buyback — is the larger of two offsets, at about **2M NEAR** over 90 days. Since the NEAR Intents fee switch went live February 23 2026, 100% of the fees from cross-chain swaps are routed into buying NEAR on the open market for buyback-and-burn; about **2.1M NEAR** has been directed so far, and the framework counts the realized amount rather than the higher annualized run-rate. Buy #2 — protocol fee burn — adds roughly **0.5M NEAR** over 90 days: **70%** of every transaction's base-layer gas fee is burned on-chain and gone for good, a real EIP-1559-style sink that is small at current activity. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero, with no discretionary open-market buying or new escrow announced beyond the Intents buyback.

## Foundation and overhang

NEAR has no classic unlock overhang — the token is essentially fully distributed, with about 99% of supply already circulating. What it does have is one structural, continuous allocation inside the epoch reward itself: the 10% treasury slice of every block's mint, accruing to the protocol rather than to validators. This is not a stockpile waiting to dump; it is a fixed share of a now-halved issuance, monitored as it accrues. The framework books no discretionary release beyond protocol inflation and re-checks the treasury balance and the Intents buyback flow on a roughly bi-weekly walk; if the treasury balance falls faster than the schedule, the outflow enters Sell #3 at the next refresh.

## How NEAR compares to other uncapped proof-of-stake chains

NEAR belongs to the class of **uncapped proof-of-stake L1s with continuous epoch issuance** — closer to a continuous-emission chain than to a hard-capped, halving-model coin. Unlike a fixed-supply token, NEAR has no ceiling; unlike a pure inflation chain, it pairs the mint with both a gas burn and a fee-funded buyback. The October 2025 halving moved it decisively toward the lower-inflation end of that class: at 2.5% gross, NEAR now issues at half its historical pace, and the two burn sinks scale with on-chain and cross-chain activity rather than with a fixed schedule.

The closest structural analogue is Ethereum, which also pairs continuous staking issuance with an EIP-1559 base-fee burn and flips net-deflationary only when activity is high enough. NEAR adds a second lever Ethereum lacks: the Intents buyback, which converts cross-chain swap fees directly into open-market NEAR purchases. That gives NEAR two paths to neutrality — rising gas activity and rising Intents volume — so its net inflation should keep easing as either climbs. For an inflation lens, NEAR reads as mildly inflationary today but structurally biased downward, the opposite of a chain whose only force is a fixed mint.

## What to watch in the next 90 days

Watch the NEAR Intents fee volume — the buyback scales directly with it, and a sustained jump in cross-chain swap activity is the single fastest way the net rate falls toward zero. Watch the staking ratio: with less than half of supply staked, realized epoch issuance sits near the 2.5% maximum, so a higher stake share would not raise the mint but would change validator yields. Note the gas-burn trend, since 70% of base-layer fees burn and rise with on-chain usage. And expect the framework to keep reading slightly below our supply monitor while realized issuance runs near the cap — that gap is small and within tolerance, not a new unlock.

## Summary

NEAR is an uncapped proof-of-stake token whose supply grows on continuous epoch issuance, now halved to a 2.5% yearly maximum after the October 2025 upgrade. The chain mints about 8M NEAR over 90 days, while a fee-funded Intents buyback and a 70% gas burn remove roughly 2.5M back out, leaving the framework at about +0.4% net. Our supply monitor reads +0.74% realized, a gap of about 0.3 points that stays inside tolerance with no warning chip. NEAR stays mildly inflationary on the active float today, but with two activity-linked burn sinks pushing it toward neutral as usage grows.

*MrNasdog Pressure Framework analysis of NEAR Protocol (NEAR), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 16, 2026.*

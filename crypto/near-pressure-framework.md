---
title: "NEAR Inflation Analysis · July 2026 · A halved mint, lightly offset"
description: "A MrNasdog Pressure Framework read of NEAR Protocol (NEAR): ~8.0M / 90D of halved 2.5% epoch issuance vs a small fee-funded buyback and a 70% gas burn. Framework +0.52% net; monitor +0.41%, a clean gap."
canonical_url: "https://mrnasdog.com/research/near/inflation"
tags: ["crypto", "near", "near-protocol", "proof-of-stake"]
published: true
---

> Originally published at **[mrnasdog.com/research/near/inflation](https://mrnasdog.com/research/near/inflation)** by MrNasdog.

NEAR Protocol mints about **8.0M NEAR** over 90 days at its **2.5%** yearly rate — half the old rate after the October 2025 halving upgrade — while a fee-funded buyback and a gas burn remove only about **1.3M** back out. The mint clearly leads, so the Pressure Framework reads about **+0.52% net**. Our supply monitor reads **+0.41%** realized — a gap of just **0.11 percentage points**, well inside tolerance, with no warning chip.

## The verdict, in one paragraph

For the 90-day window ending July 6 2026, the MrNasdog Pressure Framework reads **NEAR at +0.52% net** on the forward view, with protocol inflation still out-issuing the combined buyback-and-burn by a wide margin. Our supply monitor reads the realized last-90-day change at **+0.41%**, versus the framework's **+0.52%** read for the same window — a gap of about **0.11 percentage points**, inside the half-point tolerance, so **no monitor-gap chip ships**. The small residual is 90-day supply-proxy noise plus the fact that bought-back NEAR is held rather than burned, so the monitor still counts it as circulating. NEAR is now **mildly inflationary and biased toward neutral**: the October 2025 halving cut the mint in half, and two activity-linked sinks chip at the rest.

## Sell pressure: where new NEAR comes from

Sell #1 — protocol inflation — is the whole story, at about **8.0M NEAR** over the next 90 days. NEAR Protocol mints new NEAR every epoch to reward validators, and the Halving Upgrade (Protocol Version 81), completed on mainnet October 30 2025, cut the maximum annual issuance from **5% to 2.5%**. At the new rate the chain issues roughly **32.5M NEAR a year**, or about 8.0M over a quarter, split **90% to validators** and **10% to the protocol treasury** — all newly issued, so it counts once, here.

Sell #2 — vesting unlocks — is **zero**: NEAR is fully unlocked, with total supply already equal to circulating, so no team, backer or treasury cliff hits the market in the window. Sell #3 — Foundation and unscheduled unlocks — is also zero as a flow, with no dated discretionary release of foundation or treasury NEAR pending; the 10% treasury slice of each epoch's mint accrues continuously inside Sell #1 rather than as a discrete dump. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate or court distribution applies to NEAR.

## Buy pressure: where new NEAR goes

Buy #1 — programmatic buyback — is the smaller of two offsets, at about **0.6M NEAR** over 90 days. Since the NEAR Intents fee switch went live February 23 2026, protocol revenue from cross-chain swaps is routed into buying NEAR on the open market; the framework counts the realized revenue-funded amount — the protocol's own revenue dashboard shows about **$387K over the trailing 30 days**, roughly **$1.2M a quarter** — not the far larger gross swap-volume headline. One important nuance: the repurchased NEAR is **held, staked or pulled from liquidity rather than burned immediately**, so it leaves the open-market float but still counts in supply — which is why the monitor and the framework read so closely together. Buy #2 — protocol fee burn — adds roughly **0.7M NEAR** over 90 days: **70%** of every transaction's base-layer gas fee is burned on-chain and gone for good, a real EIP-1559-style sink that is small at current activity. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero, with no discretionary open-market buying or new escrow announced beyond the Intents buyback.

## Foundation and overhang

NEAR has no classic unlock overhang — the token is fully distributed, with total supply equal to circulating. What it does have is one structural, continuous allocation inside the epoch reward itself: the **10% treasury slice** of every block's mint, accruing to the protocol rather than to validators. There is also the **Intents buyback wallet**, where revenue-funded NEAR purchases accumulate; because that NEAR is held rather than burned, it is a tracked balance, not a destroyed one. Neither is a stockpile waiting to dump — the treasury is a fixed share of a now-halved issuance, and the buyback hold is a sink. The framework re-checks the treasury balance and the Intents buyback flow on a roughly bi-weekly walk; if either balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How NEAR compares to other uncapped proof-of-stake chains

NEAR belongs to the class of **uncapped proof-of-stake L1s with continuous epoch issuance** — closer to a continuous-emission chain than to a hard-capped, halving-model coin. Unlike a fixed-supply token, NEAR has no ceiling; unlike a pure inflation chain, it pairs the mint with both a gas burn and a fee-funded buyback. The October 2025 halving moved it decisively toward the lower-inflation end of that class: at 2.5% gross, NEAR now issues at half its historical pace, and the two sinks scale with on-chain and cross-chain activity rather than with a fixed schedule.

The closest structural analogue is Ethereum, which also pairs continuous staking issuance with an EIP-1559 base-fee burn and flips net-deflationary only when activity is high enough. NEAR adds a second lever Ethereum lacks: the Intents buyback, which converts cross-chain swap fees directly into open-market NEAR purchases. The difference is that Ethereum's burn destroys the token outright, while NEAR's buyback so far **holds** the NEAR — so on a strict supply count the offset is real but the deflation only shows up as reduced float, not a falling total. For an inflation lens, NEAR reads as mildly inflationary today but structurally biased downward as either gas activity or Intents volume climbs.

## What to watch in the next 90 days

Watch the NEAR Intents fee volume — the buyback scales directly with it, and a sustained jump in cross-chain swap activity is the single fastest way the net rate falls toward zero; reporting puts the break-even for net deflation near **$177M in daily Intents volume** against a recent average closer to **$77M**. Watch whether the protocol starts **burning** the bought-back NEAR rather than holding it — a live governance debate, with a co-founder floating a fixed maximum-supply model — because that would convert the buyback into a true supply reduction the monitor can see. Watch the base-layer gas-burn trend, since 70% of gas fees burn and rise with on-chain usage. And note that no team, backer or foundation unlock is scheduled, so there is no cliff on the calendar to move the reading.

## Summary

NEAR is an uncapped proof-of-stake token whose supply grows on continuous epoch issuance, now halved to a 2.5% yearly rate after the October 2025 upgrade. The chain mints about 8.0M NEAR over 90 days, while a fee-funded Intents buyback and a 70% gas burn remove only about 1.3M back out, leaving the framework at about +0.52% net. Our supply monitor reads +0.41% realized, a gap of about 0.11 points that stays well inside tolerance with no warning chip. NEAR stays mildly inflationary on the active float today, with two activity-linked sinks pushing it toward neutral as usage grows — and a clearer path to deflation if the bought-back NEAR is ever burned instead of held.

---

*MrNasdog Pressure Framework analysis of NEAR Protocol (NEAR), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 6 2026.*

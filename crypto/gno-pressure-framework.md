---
title:         "GNO Inflation Analysis · July 2026 · Hard-capped and near flat"
description:   "Gnosis mints only ~0.008M GNO/90d in staking rewards that mostly re-stake, with no live burn. Framework reads +0.3% net (monitor +0.03%) — capped and quiet."
canonical_url: "https://mrnasdog.com/research/gno/inflation"
tags:          ["crypto", "gno", "gnosis", "staking"]
published:     true
---

*Originally published at [mrnasdog.com/research/gno/inflation](https://mrnasdog.com/research/gno/inflation)*

Gnosis is hard-capped at **3M GNO** with about **2.64M circulating**. Validator staking rewards mint only about **0.008M GNO** over 90 days, and most of it re-stakes rather than reaching the market, so the framework reads about **+0.3%** net. Our supply monitor reads only **+0.03%** — both point to a supply that is capped and barely moving.

## The verdict, in one paragraph

For the 90-day window ending July 4 2026, the MrNasdog Pressure Framework reads **GNO at +0.3% net**, just off flat. Sell pressure is a small validator staking emission; buy pressure is currently zero because the DAO's new redemption-burn has not fired yet. Our supply monitor reads the realized last-90-day change at **+0.03%**, versus the framework's **+0.30%** gross read — a gap of about **0.28 percentage points**, inside tolerance, so no monitor-gap chip ships. The small wedge is structural: GNO validator rewards are minted but must stay staked, so gross emission runs slightly ahead of the supply that actually reaches float. GNO is best characterised as **hard-capped and near flat** — a governance and staking token whose supply is being managed down toward its 3M ceiling.

## Sell pressure: where new GNO comes from

Sell #1 — protocol inflation — is the only non-zero source, at about **0.008M GNO** over the next 90 days. Gnosis Chain is proof-of-stake, and validators earn rewards in freshly minted GNO on a published curve that pays a higher rate when little is staked and decays toward **4%** a year as the staked base grows. At the current staked level that curve mints only a few thousand GNO a quarter, and because every validator must keep GNO staked, most of that reward re-stakes immediately rather than reaching the open market.

Sell #2 — vesting unlocks — is **zero**: there is no scheduled team, seed or investor cliff hitting the market, and the remaining non-circulating GNO sits in the DAO vesting contract that is being burned down toward the 3M cap, not released. Sell #3 — Foundation and unscheduled unlocks — is also zero as a flow; the roughly **0.36M** gap between circulating and the cap is treasury and vesting supply being reduced over time, and there is no dated discretionary release pending. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate or court distribution applies to GNO.

## Buy pressure: where new GNO goes

Buy #1 — programmatic buyback — is carried at **zero**, but it is the row to watch. GnosisDAO passed a pro-rata treasury redemption on **Jun 27 2026** that lets holders surrender GNO for a share of the roughly **$223M** treasury, and any GNO redeemed is **burned at the moment of redemption** — a genuine deflationary sink. Because the mechanism runs a 30-day opt-in followed by a three-month claim window, no burn had executed inside this window as of July 4 2026, so the framework books it at zero and monitors it. Buy #2 — protocol fee burn — is zero because Gnosis Chain fees are paid and burned in xDAI, not GNO, so there is no GNO fee burn to count. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero, with no discretionary open-market GNO buying or new escrow announced in the window beyond the ongoing validator staking itself.

## Foundation and overhang

GNO's only meaningful overhang is the non-circulating supply held by GnosisDAO — roughly **0.36M GNO** between the 2.64M circulating and the 3M cap, sitting in the DAO treasury and the vesting contract. The important feature is direction: that reserve is being **burned down**, not distributed, as the DAO follows through on its multi-year mandate to cut the total from about 10M toward 3M. The redemption programme is the newest lever on that overhang, since redeemed GNO is destroyed rather than recycled. The framework tracks the treasury and vesting balances on a roughly bi-weekly walk; if either balance falls in a way that reaches the market rather than the burn address, the outflow enters Sell #3 at the next refresh.

## How GNO compares to other hard-capped staking tokens

GNO belongs to the class of **hard-capped proof-of-stake governance tokens** — closer to a fixed-supply asset than to an uncapped, continuously-inflating L1. Unlike a halving-model coin whose cap is enforced by a fixed subsidy schedule, GNO's 3M ceiling is enforced socially, by DAO burns that grind the total supply down over years. And unlike a high-emission staking chain, its validator rewards are small relative to the float and mostly re-stake, so the mint barely touches circulating supply.

The contrast worth drawing is with staking tokens that inflate to pay validators from fresh supply that reaches the market. GNO issues far less, and it pairs that issuance with an active supply-reduction programme — the vesting burns and now the redemption burns — that pushes in the opposite direction. For an inflation lens specifically, that means GNO reads as flat to very mildly inflationary today, with a real path to net-deflationary the moment the redemption burns begin to fire.

## What to watch in the next 90 days

Watch the treasury redemption claim window, expected to open around **Jul 27 2026** — the first GNO burned through it flips Buy #1 from zero to a real deflationary number. Watch the amount of GNO actually surrendered for redemption, since a large take-up would remove supply permanently. Watch the total GNO staked, because the staking curve mints more when more is staked, though the effect on float stays small. And watch GnosisDAO governance for any further vesting-contract burn, the mechanism that has been steering the total supply toward its 3M cap.

## Summary

GNO is a hard-capped proof-of-stake governance token with about 2.64M circulating against a 3M ceiling. Validator rewards mint only about 0.008M GNO over 90 days and mostly re-stake, so the framework reads about +0.3% net, near flat, and our supply monitor reads +0.03% realized. The key risk is upside for holders, not dilution: a DAO redemption that burns surrendered GNO passed on June 27 2026 and could turn the buy side deflationary once its claim window opens. Until then GNO stays capped and quiet — a supply being managed down toward its ceiling rather than expanded.

---

*MrNasdog Pressure Framework analysis of Gnosis (GNO), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 4, 2026.*

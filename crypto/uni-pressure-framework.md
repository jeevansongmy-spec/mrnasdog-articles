---
title: "UNI Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description: "UNI supply is roughly steady: Uniswap's fee burn destroyed 5.69M UNI in 90 days against a 5.00M UNI treasury growth budget. Net −0.13%, next 90 days +0.13%."
canonical_url: "https://mrnasdog.com/research/uni/inflation"
tags: ["crypto", "uni", "uniswap", "defi"]
published: true
---

Originally published at [https://mrnasdog.com/research/uni/inflation](https://mrnasdog.com/research/uni/inflation) by MrNasdog.

# UNI Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

UNI supply is roughly steady: over the last 90 days the Uniswap fee burn destroyed **5,692,001 UNI** and a DAO wallet returned **113,138 UNI** to the treasury, against a **5.00M UNI** growth budget paid out of that treasury — a net change of **−0.13%**. The next 90 days turn slightly the other way, to about **+0.13%**, because the next 5M UNI slice unlocks on Oct 1 2026 while, at today's higher UNI price, the same fees burn only about **4.22M UNI**. Total supply is still exactly 1 billion: the burn happens at a dead address, and the 2% yearly mint right has never been used.

## The verdict, in one paragraph

Across Jul 1 to Sep 29 2026, UNI supply that counts as circulating fell by **805,139 UNI**, or **−0.13%** of the **620.40M UNI** float. Our inflation monitor, which reads the same float from market data, measured **−0.10%** over its own 90 days — a gap of **0.03 percentage points**, well inside our half-point tolerance, so no warning chip is needed. For the next 90 days we project **+0.13%**: one scheduled 5M UNI release against a fee-funded burn of about 4.22M UNI. In one line, UNI is a **treasury-funded budget balanced by a fee-funded burn**, and which side wins each quarter depends on swap fees and the UNI price.

## Sell pressure: where new UNI comes from

Protocol inflation is **0**. The UNI token contract reported a total supply of exactly 1,000,000,000 UNI at both ends of the window, and no new UNI was minted. That reading is a real measurement, not a fixed number baked into the code: the supply figure lives in storage the mint function writes to. The mint right itself is alive — the Uniswap DAO treasury can mint up to 2% of supply a year, about 20M UNI, at most once every 365 days — but only after a full governance vote, and no such vote has been proposed.

Vesting unlocks are the whole sell side: **5.00M UNI**. Under the UNIfication plan passed in December 2025, the DAO pays Uniswap Labs a growth budget of 20M UNI a year, released as 5M UNI every quarter by a vesting contract that pulls the coins from the DAO treasury. The Jul 1 slice was paid on Jul 14 2026. The next slice unlocks on Oct 1 2026, so the next 90 days also carry **5.00M UNI**, and 25M UNI — five more quarters — is already approved. Because the treasury sits outside the circulating count, every slice is new supply for the market, even though the coins already exist.

Foundation and unscheduled unlocks are **0**: apart from the budget slice, not one UNI left the DAO treasury this window. Long-term locks and bankruptcy releases are also **0** — the founding team and investor vesting ended in 2024, and there is no estate or court schedule holding UNI.

## Buy pressure: where new UNI goes

The programmatic buyback is the big buy row: **5,692,001 UNI** destroyed in 90 days, across 2,433 burns. Since the UNIfication fee switch went live in December 2025, Uniswap protocol fees collect in a fee vault on each chain. Anyone can empty the vault, but only by destroying a fixed lot of UNI — 4,000 UNI on Ethereum. So traders buy UNI, burn it, and take the fees when the fees are worth more than the UNI. Fees earned on other chains end the same way: the UNI is sent back to Ethereum and burned there. Measured in dollars, the UNI burned matched the protocol's fee income for the same weeks to within a few percent.

The pace changed inside the window. Two governance votes executed on Jul 27 2026 switched on protocol fees for Uniswap v4 pools on seven chains and for Robinhood Chain. Before them the burn ran at about **40,900 UNI a day**; after them, about **72,500 UNI a day**, or roughly $407,000 of fees a day. Fees are earned in dollars, and the UNI price has more than doubled since July, so the same dollars now buy fewer UNI. At today's price of about $8.69, the post-vote fee rate burns about **4.22M UNI** in the next 90 days. If UNI stayed cheaper, or fees kept growing, the burn would be bigger.

The protocol fee burn row is **0** on its own: no swap fee is destroyed directly — fees go to liquidity providers and to the fee vault — and the UNI destroyed to empty that vault is counted once, above. The Foundation buy row carries **113,138 UNI**: on Jul 30 2026 a DAO-linked wallet sent reward UNI it had claimed, plus some it bought on the market, back into the treasury, which takes it out of circulation. It was a one-off, so the next 90 days count 0. New long-term locks are **0**: UNI has no staking contract, and delegating votes never moves the coins.

## Foundation and overhang

The one large team-controlled overhang is the Uniswap DAO treasury: **267.25M UNI**, which is exactly the part of supply not counted as circulating. 25M UNI of it is already committed to the growth budget; the rest can only move by governance vote. The Uniswap Labs budget wallet holds about **12.00M UNI** and the original 2020 airdrop contract still holds about **12.51M** unclaimed UNI, but both are already counted as circulating, so spending or claiming them adds nothing new. Bought-back UNI goes straight to the burn address, which now holds **112.35M UNI**, including the one-time 100M UNI treasury burn of December 2025 — so no buyback wallet builds up. We read these balances straight from the chain at every rebuild: if the treasury's balance falls between refreshes for anything other than the scheduled slice, that outflow enters Sell #3 at the next refresh.

## How UNI compares to other DEX governance tokens

Most DEX tokens fall into one of two designs. Emission tokens such as CAKE and AERO pay liquidity providers in newly minted coins every week and then try to claw some back with burns or locks; their sell side is protocol inflation, measured in percent of supply per quarter. UNI has no emissions at all: liquidity providers are paid only in swap fees, the mint right sits unused, and the only new supply is a fixed, quarterly treasury budget of 5M UNI — under 1% of the float a quarter.

On the buy side, UNI now looks more like fee-buyback tokens than like its old self. Until December 2025 no Uniswap fee touched UNI. Now a slice of every swap fee on most Uniswap chains ends as UNI bought and burned, with no treasury decision needed each time. The difference from a straight buyback is that the burn is set in dollars of fees, not in UNI, so a rising UNI price shrinks the number of coins burned, and a falling one grows it.

The result is a middle case: UNI supply is neither shrinking fast, like tokens that burn most of their revenue with no new supply, nor growing like emission-funded DEX tokens. The net sits within a fraction of a percent of zero, and it can tip either way from quarter to quarter.

## What to watch in the next 90 days

**Oct 1 2026** — the next 5M UNI growth-budget slice unlocks; it usually leaves the treasury within about two weeks. **Oct 3 2026** — the on-chain vote to switch on Uniswap fees on Arc, Circle's new chain, closes; if it passes, one more chain feeds the burn. A second vote to turn on v4 fees on five smaller chains has been announced but has no date yet. Watch the UNI price too: every dollar of fees burns fewer UNI when the price rises. And watch for any governance proposal to use the 2% mint right, which would add up to about 20M UNI; none exists today. The next budget slice after this one unlocks on Jan 1 2027, just outside this window.

## Summary

UNI supply is roughly steady: in the 90 days to Sep 29 2026 Uniswap's fee-funded burn destroyed 5.69M UNI while the DAO treasury released a 5.00M UNI growth budget, for a net of −0.13%, and we project about +0.13% for the next 90 days as the Oct 1 2026 slice meets a burn of about 4.22M UNI at today's price. The key risk to that reading is the 267.25M UNI DAO treasury and its unused 2% yearly mint right, both of which need a governance vote to move. Total supply is fixed at 1 billion unless that mint is used, and every burned UNI sits at a dead address for good.

*MrNasdog Pressure Framework analysis of UNI, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

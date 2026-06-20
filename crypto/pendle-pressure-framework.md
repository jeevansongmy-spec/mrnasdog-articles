---
title:         "PENDLE Inflation Analysis · June 2026 · Emissions cut to a low terminal rate"
description:   "Net ~+0.5%: Pendle's emissions cut to a terminal ~2%/yr rate (~0.84M/90d) with no supply sink. Monitor reads +2.6% on the old, higher pre-cut window."
canonical_url: "https://mrnasdog.com/research/pendle/inflation"
tags:          ["crypto", "pendle", "defi", "inflation"]
published:     true
---

*Originally published at [mrnasdog.com/research/pendle/inflation](https://mrnasdog.com/research/pendle/inflation)*

Pendle's weekly incentive emissions decayed for over a year and then switched to a terminal rate of about **2% a year** on circulating supply — roughly **0.84M PENDLE** over the next 90 days, with no buyback or burn that actually removes supply. The framework reads **~+0.5%** net forward. Our supply monitor reads the past quarter at **+2.6%**, because that window still carried the old, higher emissions before the cut.

## The verdict, in one paragraph

For the 90-day window beginning June 20 2026, the MrNasdog Pressure Framework reads **PENDLE at about +0.5% net** on the forward view, driven entirely by terminal incentive emissions with nothing on the buy side that removes supply. Our supply monitor reads the realized last-90-day change at **+2.6%** — but that window (March 22 to June 20 2026) captured the tail of the old decaying emission schedule and the cut still settling in, so it runs well above the forward rate. The framework's realized read for the same window agrees with the monitor at about **+2.6%**, so the gap is roughly **0 percentage points** and no monitor-gap chip ships. The drop from +2.6% realized to +0.5% forward is a documented regime change: weekly emissions decayed 1.1% per week until April 2026, then switched to the terminal 2%-per-annum rate, and the Algorithmic Incentive Model that went live January 29 2026 cut overall emissions roughly 30%. PENDLE reads as **cooling supply growth — newly low and stable.**

## Sell pressure: where new PENDLE comes from

Sell #1 — protocol inflation — is the entire flow, at about **0.84M PENDLE** over the next 90 days. Pendle's incentive emissions decayed by **1.1%** each week from September 2024, when the weekly mint was 216,076 PENDLE, until April 2026, and then switched to a terminal inflation rate of about **2% per annum** on circulating supply. On a circulating base near **171.0M**, that terminal rate is roughly **66K PENDLE a week** — a small, rule-based emission, not a discretionary release. The Algorithmic Incentive Model now routes that budget to pools by measured contribution rather than by manual votes.

Sell #2 — vesting unlocks — is **zero**: all team and investor tokens finished vesting in September 2024, so no scheduled cliff or linear founder unlock remains. Sell #3 — Foundation and unscheduled unlocks — is zero as a booked flow, but the Ecosystem Fund is a tracked overhang: it holds a large unallocated slice of supply with no published 90-day release rate, so it is monitored rather than booked. Sell #4 — long-term locked or bankruptcy — is zero, because there is no bankruptcy estate and no scheduled long-term protocol release tied to PENDLE.

## Buy pressure: where new PENDLE goes

Every buy-side row is **zero** for the supply lens, and the buyback is the row that surprises people. Buy #1 — programmatic buyback — directs up to **80%** of protocol revenue to buying PENDLE on the open market, but those bought-back tokens are **redistributed to active sPENDLE stakers** as rewards, not burned and not held in a treasury. Because the tokens flow straight back into circulating hands, the buyback removes **no** circulating supply — it is real market buy pressure on price, but not a supply sink, so the inflation framework books it at zero. Buy #2 — protocol fee burn — is zero, because there is no PENDLE burn; fee value is paid out, not used to destroy tokens. Buy #3 — Foundation buy — is zero, with no treasury purchase in the window. Buy #4 — new long-term lock — is zero as a booked figure: staking PENDLE into sPENDLE does pull it out of the float, but sPENDLE is now liquid — a 14-day exit, or instant for a 5% fee — and two-directional, with no announced net-new quantum, so the framework does not book it.

## Foundation and overhang

PENDLE has one live overhang worth naming and one structure worth understanding. The **Ecosystem Fund** holds a large unallocated portion of total supply and is excluded from circulating; it releases on building grants and incentive top-ups with no published 90-day rate, so it stays tracked rather than booked. The **sPENDLE staking contract** holds the staked PENDLE that is excluded from circulating supply — but because staking is now liquid and reversible within 14 days, that balance can move in either direction and is not a one-way lock. The framework books no discretionary release beyond terminal emissions; if the Ecosystem Fund's balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How PENDLE compares to other DeFi emission tokens

PENDLE belongs to the class of **vote-escrow / staking-reward DeFi tokens** with scheduled emissions — its closest analogue is Curve's CRV, which also mints incentives on a decaying schedule with no burn. The difference now is that PENDLE has reached its terminal floor: where CRV still emits tens of millions of tokens a quarter, PENDLE's terminal 2%-per-annum rate is under a million over 90 days, a far lighter dilution. The contrast with buyback-and-burn tokens is sharper still: those pair emissions with an active sink, so their net supply can shrink. PENDLE's buyback does not burn — it redistributes to stakers — so it lifts staker rewards and supports price without subtracting from supply.

This is a mechanism-based read, not a price-based one. On an inflation lens specifically, PENDLE reads as **low and stable**: the terminal emission is small, vesting is fully behind it, and the only thing that could reverse the picture is the Ecosystem Fund moving tokens out — which the framework watches but does not assume.

## What to watch in the next 90 days

Watch the realized supply curve flatten — the monitor's 90-day number should keep falling toward the terminal rate as the old high-emission window rolls off, confirming the cut on-chain. Watch Ecosystem Fund disbursements, since that fund is the one tracked balance that could add unbooked supply if it deploys. Watch protocol revenue, because it sets the size of the buyback that supports stakers — a revenue rebound lifts the buy pressure on price even though it removes no supply. And watch governance: any proposal to start burning a slice of the buyback, instead of redistributing all of it, would turn the buyback into a real supply sink and push the net read below zero.

## Summary

PENDLE's emissions have just dropped to a low terminal rate of about 2% a year, so only about 0.84M PENDLE reaches the market over the next 90 days, leaving the framework at about +0.5% net. Vesting is fully complete, and the revenue buyback redistributes PENDLE to stakers rather than burning it, so it removes no supply. Our monitor still reads +2.6% for the past quarter because that window carried the old, higher emissions before the cut — a documented regime change, not a data conflict. The one risk to watch is the Ecosystem Fund, the only tracked balance that could add unbooked supply.

---

*MrNasdog Pressure Framework analysis of Pendle (PENDLE), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 20, 2026.*

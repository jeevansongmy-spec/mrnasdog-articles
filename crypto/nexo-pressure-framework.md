---
title:         "NEXO Inflation Analysis · July 2026 · Fixed supply, buyback held not burned — net flat"
description:   "Net flat: a fixed 1B supply with no mint or vesting, and a revenue buyback held in a locked reserve, not burned. Framework reads 0% / 90D; monitor +0.07%."
canonical_url: "https://mrnasdog.com/research/nexo/inflation"
tags:          ["crypto", "nexo", "cefi", "exchange-token"]
published:     true
---

*Originally published at [mrnasdog.com/research/nexo/inflation](https://mrnasdog.com/research/nexo/inflation)*

**TL;DR.** NEXO is a fixed **1B** ERC-20 with no mint, no remaining vesting, and no burn, so no flow moves the supply either way — the framework reads **0% net** over the last 90 days and the next. Nexo runs a revenue buyback, but repurchased NEXO is parked in a locked reserve rather than burned, and those coins already count as circulating, so it removes no counted supply. Our supply monitor agrees at about **+0.07%** — a gap of just **0.07 percentage points**, well inside tolerance, so no warning chip ships.

## The verdict, in one paragraph

For the 90-day window ending July 13 2026, the MrNasdog Pressure Framework reads **NEXO at 0% net** — supply flat, with the forward view also flat at **0%**. There is no sell pressure: Nexo's NEXO token has no protocol inflation, no mint function, and no scheduled unlock. There is also no counted buy pressure, because the one active mechanism — a revenue buyback — parks its coins in a locked reserve rather than destroying them. Our supply monitor reads the realized last-90-day change at about **+0.07%**, a gap of only **0.07 percentage points** against the framework's **0%** — inside the 0.5-point tolerance, so **no monitor-gap chip** is shown. NEXO is a **fixed-supply exchange token with mixed flows and a supply that is roughly steady**: nothing added, nothing counted removed.

## Sell pressure: where new NEXO comes from

No new NEXO comes from anywhere. Sell #1 — protocol inflation — is **zero**: the on-chain totalSupply is fixed at exactly **1,000,000,000** NEXO, there is no mint function, and the supply has never grown. Sell #2 — vesting unlocks — is also **zero**: the entire 1B was issued back at the 2018 ICO and is already circulating, so there is no remaining vesting schedule and no future unlock to release into the market. This gives NEXO one of the cleaner supply profiles among top-100 assets, with circulating supply equal to fully diluted supply.

Sell #3 — Foundation and unscheduled unlocks — is **zero** as a flow, with no dated discretionary company release in the window. Sell #4 — long-term locked or bankruptcy — is **zero**, because Nexo is a solvent operating company with no bankruptcy estate or court-ordered distribution. Every sell row on the NEXO ledger is empty, and the on-chain supply confirms it: fixed at 1B, unchanged.

## Buy pressure: where new NEXO goes

Buy #1 — programmatic buyback — is the only active mechanism, and it is booked at **zero** for this window. Nexo runs a revenue-funded open-market buyback of NEXO; a **$50M** program was approved by governance in December 2025 and is described as active. The critical structural fact is what happens to the coins: repurchased NEXO is sent to the on-chain Investor Protection Reserve under a 12-month lock and **held, not burned**. Because those coins were already counted as circulating, moving them into the reserve removes no counted supply — unlike a buyback-and-burn, which permanently destroys coins. On-chain, the reserve balance has held at about **114.8M** NEXO unchanged across the trailing 12 months, so no new accumulation is booked in the last 90 days.

Buy #2 — protocol fee burn — is **zero**: NEXO is a utility token with no protocol-level fee or gas burn, so no coins are destroyed by transactions. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both **zero**, with no discretionary market buying outside the buyback program and no new escrow announced in the window.

## Foundation and overhang

NEXO does carry one clearly identified team-controlled overhang: the Investor Protection Reserve, an on-chain address holding about **114.8M** NEXO — roughly **11%** of supply — accumulated from years of past buybacks. That balance has not moved to the wei over the trailing year, and the reserve is refreshed on a roughly bi-weekly on-chain walk. Because the reserve is already inside the reported circulating count, it does not distort the inflation read today, but it is the one balance to watch: if the Investor Protection Reserve's balance falls between refreshes, that outflow would enter Sell #3 at the next refresh.

## How NEXO compares to other exchange tokens

NEXO belongs to the class of **exchange and CeFi platform tokens with a revenue-funded buyback**, but it sits at the softer end of that class on supply mechanics. The aggressive members of the class run a buyback-and-**burn**: they buy their token with platform profit and destroy it on-chain, so supply is fixed or capped and only ever shrinks. NEXO runs a buyback-and-**hold** instead — the repurchased coins go to a locked Investor Protection Reserve and are later recycled into interest payouts and strategic use, not burned. Mechanically, that means a burn-model exchange token reads deflationary while NEXO reads flat, even though both are buying their own token with revenue.

Against uncapped proof-of-stake L1s, NEXO looks very different again: those chains mint new coins every block, so their supply grows continuously and a burn only slows dilution. NEXO has no emission at all — its 1B supply is fully issued and fixed — so there is no dilution to fight in the first place. The trade-off is that, unlike a burn-model token, NEXO's buyback does not actively reduce the counted float; it parks it. For the inflation read that nets to the same place as a capped-but-flat token: steady supply, neither growing nor shrinking.

## What to watch in the next 90 days

Watch the Investor Protection Reserve address for any change from its long-standing ~114.8M NEXO balance — an inflow would mean buyback coins are being parked (still not a burn), while an outflow would enter Sell #3. Watch for any Nexo announcement that the buyback will switch from hold to burn, which is the single change that would turn the buy side deflationary. Watch governance for any new program that locks or releases NEXO. And keep an eye on the circulating-supply figure: with supply fixed at 1B on-chain, any move in the reported number is aggregator noise, not a real flow. No dated supply event is scheduled inside the window.

## Summary

NEXO is a fixed 1B exchange token with no mint, no remaining vesting, and no burn, so its supply neither grows nor shrinks — the framework reads 0% net over 90 days, matching our supply monitor at about +0.07%. Its one active mechanism, a revenue-funded buyback, parks repurchased NEXO in a locked Investor Protection Reserve rather than burning it, and those coins already count as circulating, so the buyback removes no counted supply. The key structural risk is the reserve overhang of about 114.8M NEXO, held off-market but already counted; the key upside would be a switch from buyback-and-hold to buyback-and-burn. As it stands, NEXO reads as a steady, fully-issued fixed-supply token.

---

*MrNasdog Pressure Framework analysis of Nexo (NEXO), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 13, 2026.*

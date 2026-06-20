---
title: "WBT Inflation Analysis · June 2026 · Capped supply, slowly burning down"
description: "A MrNasdog Pressure Framework read of WhiteBIT Coin (WBT): zero new minting under a 400M hard cap vs a weekly fee-funded buyback-burn. Framework −0.2% net; the −44% supply drop was a reporting change, not a burn."
canonical_url: "https://mrnasdog.com/research/wbt/inflation"
tags: ["crypto", "wbt", "whitebit", "exchange-token"]
published: true
---

> Originally published at **[mrnasdog.com/research/wbt/inflation](https://mrnasdog.com/research/wbt/inflation)** by MrNasdog.

WhiteBIT Coin is hard-capped at **400M** with no way to mint more, so protocol inflation is **zero**. A weekly buyback-burn funded by trading fees removes about **0.3M WBT** over 90 days, leaving the Pressure Framework at roughly **−0.2% net** — mildly deflationary. Our supply monitor reads a dramatic **−44.6%**, but that drop is a reporting reclassification, not coins being destroyed.

## The verdict, in one paragraph

For the 90-day window ending June 16 2026, the MrNasdog Pressure Framework reads **WBT at about −0.2% net** — a hard-capped exchange token with no new issuance and a small, steady buyback-burn that slowly trims the float. Our supply monitor reads the realized last-90-day change at **−44.6%**, a gap of roughly **44 percentage points** that ships a **⚠ monitor-gap chip**. The gap is not a burn: an external data feed stopped counting a large locked allocation as circulating, so the published float fell from about **213M** to **118M** with no coins actually destroyed. On the real on-chain picture, WBT is **structurally deflationary at a low, steady pace** — capped issuance plus a fee-funded burn.

## Sell pressure: where new WBT comes from

There is essentially none. Sell #1 — protocol inflation — is **zero**, because WBT is capped at 400M and no mechanism exists to create new coins; the supply can only fall as tokens burn. Sell #2 — vesting unlocks — is also **zero** in this window: the multi-year team lock finished releasing through 2025, and the large unlock dated **March 13 2026** fired just before the window opened on March 18, so no cliff reaches the market between then and June 16 2026.

Sell #3 — Foundation and unscheduled unlocks — is **zero** as a flow; there is no dated discretionary release in the window, though the non-circulating reserve (the gap between total and circulating supply) remains a tracked overhang. Sell #4 — long-term locked or bankruptcy — is **zero**, because no bankruptcy estate or court-ordered distribution applies to WBT.

## Buy pressure: where new WBT goes

Buy #1 — programmatic buyback — is the only active force, at about **0.3M WBT** over 90 days. WhiteBIT runs a weekly buyback funded by **33%** of trading fees plus a slice of other fees, buying WBT on the open market and burning it permanently; the stated pace removes roughly **0.08%** of supply per month, and the program has burned about **80M WBT** cumulatively against a long-term target of half the cap. Because the destination is a burn, those coins are gone for good and the buyback counts cleanly on the buy side.

Buy #2 — protocol fee burn — is carried at **zero**, because there is no separate base-fee burn distinct from the weekly buyback-burn already counted in Buy #1; counting it again would double the figure. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both **zero**, with no discretionary open-market buying or new escrow announced in the window.

## Foundation and overhang

WBT's circulating supply is about **118M** against a total of roughly **294M**, so close to **176M** sits in non-circulating reserve — the project's own allocations and undistributed buckets. That reserve is the tracked team-controlled overhang. There is no published schedule that releases it inside this window, and the most recent reclassification actually moved a large slice of it out of the circulating count rather than into the market. The framework books no discretionary release beyond the weekly burn and re-checks the burn reports and the circulating count on a roughly bi-weekly walk; if the reserve balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How WBT compares to other exchange tokens with buyback-burns

WBT belongs to the class of **hard-capped exchange tokens with a fee-funded buyback-burn** — the same structural family as the large centralized-exchange coins that recycle a share of trading revenue into open-market buys and burns. Unlike an uncapped proof-of-stake chain that mints new coins every block, WBT has no issuance at all; the only supply force is the burn. That puts it firmly on the deflationary side of the ledger, but gently: the weekly burn is small relative to the float, so supply trims rather than collapses.

The contrast worth drawing is with the headline supply number. A reader looking only at a data feed would see WBT's circulating supply fall by nearly half and conclude the burn is enormous. It is not — the drop is a classification change in how locked tokens are counted, not destruction. On a mechanism basis, WBT is a steady, low-rate deflationary token: capped issuance, a modest fee-funded burn, and a large reserve that has not been scheduled into the market.

## What to watch in the next 90 days

Watch the weekly burn reports — the buyback pace is funded by trading fees, so a busy quarter on the exchange lifts the burn and a quiet one slows it. Watch whether the circulating-supply count is revised again, since the last reclassification is what produced the headline supply drop and any further adjustment will move the reported float without any real burn. Watch the non-circulating reserve of roughly 176M for any dated release schedule, which would add the first real sell-side flow. And note that the framework will keep reading near flat-to-mildly-deflationary while issuance stays at zero and the burn stays small.

## Summary

WBT is a hard-capped exchange token with zero protocol inflation and a weekly fee-funded buyback-burn. With no minting and a burn of about 0.3M WBT over 90 days, the framework reads roughly −0.2% net — mildly deflationary. Our supply monitor reads −44.6%, but that is a circulating-supply reclassification, not a burn; no coins were destroyed in that move. The key structural fact is the cap plus the burn, and the key risk is the large non-circulating reserve, which could add sell pressure only if a release schedule is announced.

*MrNasdog Pressure Framework analysis of WhiteBIT Coin (WBT), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 16, 2026.*

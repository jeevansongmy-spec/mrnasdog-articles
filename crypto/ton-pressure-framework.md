---
title: "TON Inflation Analysis · June 2026 · Faster blocks meet a loud unlock calendar"
description: "A MrNasdog Pressure Framework read of Toncoin / Gram (TON): ~50M emission after Catchain 2.0 plus ~110M/90d of early-backer vesting. Framework +5.9% net; monitor +10.0%."
canonical_url: "https://mrnasdog.com/research/ton/inflation"
tags: ["crypto", "ton", "gram", "layer-1"]
published: true
---

> Originally published at **[mrnasdog.com/research/ton/inflation](https://mrnasdog.com/research/ton/inflation)** by MrNasdog.

The Open Network — whose coin was renamed **Toncoin to Gram** in June 2026 with no change to supply — now carries two real sell forces. An April speed upgrade lifted validator emission to roughly **50M TON** over 90 days, and the Believers Fund vesting unlock moves about **110M TON** from frozen to circulating in the same window. With no buyback to offset either, the framework reads about **+5.9%** net. Our supply monitor reads **+10.0%** — the gap is an aggregator-side reclassification, not an extra outflow.

## The verdict, in one paragraph

For the 90-day window opening June 28 2026, the MrNasdog Pressure Framework reads **TON at about +5.9% net** on the forward view, driven by a stepped-up validator emission plus the Believers Fund vesting unlock. Our supply monitor reads the realized last-90-day change at **+10.0%**, versus the framework's **+5.91%** read of on-chain emission plus the published unlock calendar — a gap of about **4.1 percentage points** that ships a **⚠ monitor-gap chip**. The monitor's extra rise is a supply-classification change on the data side: TON renamed to Gram and previously-frozen buckets were re-tagged as circulating faster than the per-cliff vesting calendar and the mint rate — not a flow the framework could trace on-chain. TON is **structurally inflationary on the float** right now, but the cause is a finite unlock plus a temporary emission step-up, not perpetual high issuance.

## Sell pressure: where new TON comes from

Sell #1 — protocol inflation — is no longer a rounding error, at about **50M TON** over the next 90 days. The Catchain 2.0 upgrade went live on **April 9 2026** and cut block time from roughly 2.5 seconds to about 400 milliseconds. Because the per-block reward was left unchanged — 1.7 TON on the masterchain, 1.0 TON on the basechain — producing far more blocks pushed annual emission from the old ~0.6% toward roughly **3.6%**. Live chain counters show about **570K TON** minted per day against a far smaller fee burn, which nets to roughly 50M over the window.

Sell #2 — vesting unlocks — is still the largest single force, at about **110M TON** over 90 days. The Believers Fund holds about **1.27B TON** from early backers and releases one thirty-sixth of itself — about **36.6M TON** — every month, from late 2025 through October 2028. Three of those monthly cliffs land inside this window: **July**, **August** and **September 2026**, summing to roughly 110M coins moving from frozen to tradable. Sell #3 — Foundation and unscheduled unlocks — is zero, because no dated discretionary release is scheduled outside that fund. Sell #4 — long-term locked or bankruptcy — is also zero as a flow, but it is not empty: about **1,081M TON** of early-miner wallets, frozen by a 2023 community vote, stay locked until roughly February 2027 and so contribute nothing in this window.

## Buy pressure: where new TON goes

There is no buy-side offset to speak of. Buy #1 — programmatic buyback — is zero: TON has no protocol mechanism that buys coins off the market. Buy #2 — protocol fee burn — is real but is already netted into the emission figure above, so it is carried at zero here to avoid double-counting; the network burns about half of each transaction fee, and that burn scales with activity, but it is far too small to absorb a 110M unlock plus a faster-block emission. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero, with no discretionary open-market buying or new escrow announced in the window. The result is a one-sided ledger: emission and the unlock add, and nothing structural removes.

## Foundation and overhang

TON's overhang is unusually large and well-documented. The biggest tracked block is the **1,081M TON** of frozen early-miner wallets — 171 genesis accounts that mined TON during the early proof-of-work phase and never transacted, suspended for 48 months by the February 2023 governance vote. That freeze lifts around **February 2027**, so it is a watch item for a future window, not this one. The second block is the Believers Fund itself: of its roughly 1.27B TON, about **1.1B** remains to release on the monthly schedule through October 2028. Both are surfaced as overhangs and re-checked on a roughly bi-weekly walk; if either balance falls faster than its published schedule, the outflow enters Sell #3 at the next refresh.

## How TON compares to other uncapped layer-1 chains

TON belongs to the class of **uncapped proof-of-stake L1s**, and after Catchain 2.0 its emission profile looks more conventional than it used to. Most uncapped chains carry their dilution in the emission curve itself — a steady few percent a year to validators. TON spent years near the bottom of that range at about 0.6% net, thanks to its fee burn; the faster-block upgrade has lifted that toward **3.6%**, putting it closer to the middle of the uncapped pack rather than the floor.

What still sets TON apart is that the bulk of its near-term dilution is front-loaded into a **finite vesting schedule** rather than spread across perpetual emission. A halving-model chain with a hard cap dilutes a known, shrinking amount forever; a high-emission L1 dilutes a steady amount forever; TON dilutes heavily but temporarily, as the Believers Fund and the frozen-miner blocks work through their calendars by 2027–2028. There is also a live governance lever: validators have been voting on whether to cut the per-block reward to claw the post-Catchain emission back down, so the emission half of the ledger could ease if that passes — unlike a chain whose inflation is fixed in protocol.

## What to watch in the next 90 days

Watch the three Believers Fund cliffs in **July**, **August** and **September 2026** — each adds about 36.6M TON, and together they remain the largest piece of the inflation story for the window. Watch the validator block-reward vote: if the masterchain reward is cut from 1.7 TON toward a lower level, the Sell #1 emission step-up partly reverses. Watch whether the data side keeps reading circulating supply well above the combined emission-plus-unlock pace; that wedge is what drives the monitor gap and would close once the post-rebrand reclassification settles. And keep the **February 2027** early-miner unfreeze on the calendar — it is the next large structural overhang after this fund.

## Summary

TON — now branded Gram — is an uncapped proof-of-stake L1 whose coin inflation stepped up after the April 2026 Catchain 2.0 speed upgrade, to roughly 3.6% a year, and whose near-term supply is further dominated by a finite vesting unlock. Validator emission adds about 50M TON over the next 90 days and the Believers Fund releases about 110M across three monthly cliffs, with no buyback to offset either, leaving the framework at about +5.9% net. Our supply monitor reads +10.0% realized, with the gap explained by an aggregator-side reclassification rather than a traceable outflow. The key risk is the combined unlock-plus-emission pace; the key relief is that the unlock is scheduled and finite and the emission step-up is up for a governance reversal — with the frozen early-miner block as the next overhang to watch in 2027.

*MrNasdog Pressure Framework analysis of Toncoin (TON / Gram), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 28, 2026.*

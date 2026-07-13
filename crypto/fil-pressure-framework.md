---
title: "FIL Inflation Analysis · July 2026 · Supply growing, projected to keep growing"
description: "A MrNasdog Pressure Framework read of Filecoin (FIL): ~5.6M/90d block-reward mint plus ~16.4M team and foundation vesting against a ~0.4M fee burn. Framework +2.71% net; monitor +3.24%."
canonical_url: "https://mrnasdog.com/research/fil/inflation"
tags: ["crypto", "fil", "filecoin", "storage"]
published: true
---

> Originally published at **[mrnasdog.com/research/fil/inflation](https://mrnasdog.com/research/fil/inflation)** by MrNasdog.

Filecoin adds roughly **22M FIL** to supply over 90 days — about **5.6M** from a decaying block-reward mint and about **16.4M** from six-year Protocol Labs and Filecoin Foundation vesting — against only a **~0.4M** fee-and-penalty burn and no buyback. The Pressure Framework reads about **+2.71%** net; our supply monitor reads **+3.24%**, a **+0.53pp** gap that trips a monitor-gap flag because network storage power is shrinking and releasing pledge collateral. FIL is **structurally inflationary on the active float** until its vesting completes on **Oct 15 2026**.

## The verdict, in one paragraph

For the 90-day window, the MrNasdog Pressure Framework reads **FIL at about +2.71% net** — new supply from a mint plus vesting, with almost nothing burned back. Our supply monitor reads the realized last-90-day circulating change at **+3.24%**, versus the framework's **+2.71%** — a gap of about **0.53 percentage points**, just over tolerance, so a monitor-gap chip is shown. The residual is not a data error: Filecoin's network quality-adjusted power fell roughly **15%** over the window, so terminating storage sectors are returning locked **pledge collateral** to the circulating float faster than the mint-plus-vesting rows alone imply. Both readings agree on the direction. FIL is **structurally inflationary on the active float**, at a mid-single-digit annualized pace, and the largest driver is vesting, not the mint.

## Sell pressure: where new FIL comes from

Sell #1 — protocol inflation — is the smaller force, at about **5.6M FIL** over the next 90 days. Filecoin mints new FIL every block as a storage-mining reward: on-chain the network mints roughly **62,000 FIL** a day, at about **4.33 FIL** per winning block across some five blocks an epoch. That block reward is decaying, because raw storage power sits far below the network baseline, so most of it now comes from the fixed simple-minting curve rather than baseline minting; 75% of each reward vests over 180 days rather than landing immediately.

Sell #2 — vesting unlocks — is the dominant driver, at about **16.4M FIL** over 90 days. Protocol Labs (**300M FIL**) and the Filecoin Foundation (**100M FIL**) each vest linearly over six years from the October 2020 network launch — **400M FIL** total, about **66.7M** a year — and that schedule is still running at full rate through this window before it concludes on **Oct 15 2026**. These tokens unlock into team custody, so they are new unlocked supply that does not immediately reach the trading float. The early SAFT investor tranches, which vested over six months to three years, all finished back in 2023. Sell #3 — Foundation and unscheduled unlocks — is zero as a separate flow, because the Foundation's release is already counted as scheduled vesting in Sell #2 and no discretionary sale beyond it is evident. Sell #4 — long-term locked or bankruptcy — is zero, since no bankruptcy estate applies to FIL.

## Buy pressure: where new FIL goes

There is very little buy pressure to report. Buy #1 — programmatic buyback — is **zero**: Filecoin runs no buyback, and there is no protocol or treasury mechanism buying FIL on the open market. Buy #2 — protocol fee burn — is about **0.4M FIL** over 90 days: gas fees, storage-fault penalties, and the newer FIP-0100 per-sector daily fee are all burned on-chain to the network burn account, lifting cumulative burn to roughly **42.5M FIL**. It is real, but a small fraction of the mint, because the base fee sits near its floor. Buy #3 — Foundation buy — is zero, with no discretionary open-market buying evident. Buy #4 — new long-term lock — is also zero: storage providers lock FIL as pledge collateral, but that collateral is currently **releasing, not growing**, as sectors terminate — a structural flow that adds float rather than removing it.

## Foundation and overhang

FIL's team-controlled overhang is defined by its vesting schedule and one idle reserve. Protocol Labs and the Filecoin Foundation still hold vesting FIL — roughly **17M** left — that releases linearly until **Oct 15 2026**, captured in Sell #2. Separately, a **300M FIL** mining reserve sits undistributed; a governance proposal to burn it outright (FIP-0093) has been stalled for over a year, and a newer proposal to do the same is still only in discussion — so the reserve is monitored, not booked as a flow. The framework re-checks the on-chain mint, the burn account, and the vesting schedule on a roughly bi-weekly walk; if the mining-reserve balance or a foundation wallet falls faster than the vesting schedule, that outflow enters Sell #3 at the next refresh.

## How FIL compares to other uncapped emission L1s

FIL belongs to the class of **uncapped, continuous-emission L1s** whose supply still carries a multi-year vesting overhang — closer to a young smart-contract chain than to a hard-capped, halving-model coin like Bitcoin. Unlike a fixed-supply token, FIL has no real ceiling — the **2B** figure is a nominal maximum, not a reached cap — and unlike an exchange token, it has no revenue-funded buyback to lean against dilution. What separates FIL from a pure inflation chain is that its heaviest supply pressure is **vesting, not the mint**, and that pressure has a known end date.

The contrast worth drawing is with chains that pair emission with a strong fee burn: an EIP-1559-style chain can drift net-deflationary when activity is high, because the burn scales with demand. Filecoin's burn is real but small after its fee redesign, so it does almost nothing to slow dilution. There is also a Filecoin-specific wrinkle absent from most L1s — pledge collateral. When the network is growing, providers lock large amounts of FIL and tighten the float; when it is shrinking, as now, that same collateral unwinds and **adds** to circulating supply, which is exactly why our monitor reads growth a touch faster than the mint-and-vesting rows alone.

## What to watch in the next 90 days

Watch the **Oct 15 2026** vesting completion — the single event that ends the largest structural sell force in FIL's history, though it falls just after this window closes. Watch the on-chain daily mint rate, near **62,000 FIL** a day, since a lower rate directly lowers Sell #1. Watch network storage power: it fell about **15%** over the last 90 days, and continued decline keeps releasing pledge collateral into the float. Watch the two mining-reserve burn proposals; either passing would cut nominal supply by **300M FIL** and reshape the tokenomics, but both remain unvoted. And watch the fee burn — near **0.4M FIL** a window today — which only matters if network activity rises sharply.

## Summary

FIL is an uncapped decentralized-storage token whose supply is still growing on two fronts: a decaying block-reward mint of about 5.6M FIL over 90 days and roughly 16.4M more from six-year Protocol Labs and Foundation vesting. With no buyback and only a ~0.4M FIL fee burn, almost nothing offsets that new supply, so the framework reads about +2.71% net — a touch below our monitor's +3.24%, the gap explained by pledge collateral unwinding as the network contracts. The key structural fact is the timeline: the six-year vesting that dominates today's sell pressure completes on Oct 15 2026, after which the smaller, decaying mint becomes the main driver of FIL inflation.

*MrNasdog Pressure Framework analysis of Filecoin (FIL), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 14, 2026.*

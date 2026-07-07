---
title: "FIL Inflation Analysis · July 2026 · Supply growing, with no burn to offset it"
description: "A MrNasdog Pressure Framework read of Filecoin (FIL): ~5.6M/90d block-reward mint plus ~21M of investor and foundation vesting, no buyback. Framework +3.3% net; monitor +3.44%."
canonical_url: "https://mrnasdog.com/research/fil/inflation"
tags: ["crypto", "fil", "filecoin", "storage"]
published: true
---

> Originally published at **[mrnasdog.com/research/fil/inflation](https://mrnasdog.com/research/fil/inflation)** by MrNasdog.

Filecoin adds roughly **27M FIL** to circulation over 90 days — about **5.6M** from a decaying block-reward mint and about **21M** from investor and foundation vesting — with essentially **no buyback or burn** to offset it. The Pressure Framework reads about **+3.3%** net, in line with our supply monitor's **+3.44%**. FIL is structurally inflationary until its six-year vesting completes on **Oct 15 2026**.

## The verdict, in one paragraph

For the 90-day window, the MrNasdog Pressure Framework reads **FIL at about +3.3% net**, driven almost entirely by new supply with nothing burning it back. Our supply monitor reads the realized last-90-day circulating change at **+3.44%**, versus the framework's **+3.34%** for the same window — a gap of only about **0.1 percentage points**, well inside tolerance, so no monitor-gap chip is shown. The two agree because the framework's breakdown — block-reward mint plus vesting release — reconstructs the observed circulating growth almost exactly. FIL is **structurally inflationary**, at a mid-single-digit annualized pace, and the single biggest driver is vesting, not the mint.

## Sell pressure: where new FIL comes from

Sell #1 — protocol inflation — is the smaller of the two forces, at about **5.6M FIL** over the next 90 days. Filecoin mints new FIL every block as a storage-mining reward: a fixed simple-minting floor plus baseline minting that scales with how close network storage power sits to its target. On-chain, the network minted roughly **62,000 FIL** in the latest 24 hours; that mint decays over time on a six-year half-life, and 75% of each miner's reward vests over 180 days rather than landing immediately.

Sell #2 — vesting unlocks — is the dominant driver, at about **21M FIL** over 90 days. Protocol Labs (**300M FIL**) and the Filecoin Foundation (**100M FIL**) both vest linearly over six years from the October 2020 network launch, which puts roughly **16M FIL** into circulation over this window; the 180-day vesting release of prior miner rewards adds the rest. The early SAFT investor allocations, which vested mostly over three years, have already run down. Sell #3 — Foundation and unscheduled unlocks — is zero as a separate flow, because the foundation's release is already counted as scheduled vesting in Sell #2, and no discretionary sale beyond it is evident. Sell #4 — long-term locked or bankruptcy — is zero, since no bankruptcy estate applies to FIL.

## Buy pressure: where new FIL goes

There is almost no buy pressure to report. Buy #1 — programmatic buyback — is **zero**: Filecoin runs no buyback, and there is no protocol or treasury mechanism buying FIL on the open market. Buy #2 — protocol fee burn — is carried at **zero**: the network does burn gas fees, but after the 2024 fee redesign the base-fee burn collapsed to only about **20 FIL a day**, an immaterial fraction of the mint. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero, with no discretionary open-market buying or new escrow announced in the window. The one large offsetting force on FIL supply is pledge collateral: storage providers lock FIL to run sectors — currently around **75M FIL** — but that is a structural lock, not a burn, so it does not enter the buy ledger.

## Foundation and overhang

FIL's team-controlled overhang is defined by its vesting schedule and one idle reserve. Protocol Labs and the Filecoin Foundation still hold vesting FIL that releases linearly until **Oct 15 2026**, captured in Sell #2. Separately, a **300M FIL** mining reserve sits undistributed; a governance proposal to burn it outright has been stalled for over a year with no vote, and a newer proposal to do the same is still only in discussion — so the reserve is monitored, not booked as a flow. The framework re-checks the on-chain mint and the vesting schedule on a roughly bi-weekly walk; if the mining-reserve balance or a foundation wallet falls faster than the vesting schedule, the outflow enters Sell #3 at the next refresh.

## How FIL compares to other uncapped storage and utility L1s

FIL belongs to the class of **uncapped, continuous-emission L1s** whose supply still carries a multi-year vesting overhang — closer to a young smart-contract chain than to a hard-capped, halving-model coin like Bitcoin. Unlike a fixed-supply token, FIL has no real ceiling (the 2B figure is nominal), and unlike an exchange token, it has no revenue-funded buyback to lean against dilution. What separates FIL from a pure inflation chain is that its heaviest supply pressure is **vesting, not the mint** — and that pressure has a known end date.

The contrast worth drawing is with chains that pair emission with a strong fee burn: those can drift net-deflationary when activity is high. Filecoin's burn is real but tiny after the fee redesign, so it does nothing to slow dilution. For an inflation lens specifically, FIL reads as clearly inflationary today, with the important nuance that the largest driver — six-year investor and foundation vesting — expires in October 2026, after which the mint alone (a much smaller, decaying number) becomes the main source of new supply.

## What to watch in the next 90 days

Watch the **Oct 15 2026** vesting completion — the single event that removes the largest structural sell force in FIL's history, though it falls just after this window closes. Watch the on-chain daily mint rate, near **62,000 FIL** a day, since a lower rate directly lowers Sell #1. Watch the two mining-reserve burn proposals; either passing would cut nominal supply by 300M FIL and reshape the tokenomics, but both remain unvoted. And watch pledge collateral: a rising lock absorbs FIL out of float even as the mint continues.

## Summary

FIL is an uncapped decentralized-storage token whose supply is still growing on two fronts: a decaying block-reward mint of about 5.6M FIL over 90 days and roughly 21M more from investor and foundation vesting. With no buyback and only a token gas burn, nothing offsets that new supply, so the framework reads about +3.3% net — in line with our supply monitor's +3.44%. The key structural fact is the timeline: the six-year vesting that dominates today's sell pressure completes on Oct 15 2026, after which the smaller, decaying mint becomes the main driver of FIL inflation.

---

*MrNasdog Pressure Framework analysis of Filecoin (FIL), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 4, 2026.*

---
title: "SUI Inflation Analysis · July 2026 · Supply growing on a steady monthly unlock"
description: "Sui adds ~66M SUI over the next 90 days (~59M vesting + ~7M subsidy) with no buyback or burn. Framework +1.6% net; monitor +2.47% — no data conflict."
canonical_url: "https://mrnasdog.com/research/sui/inflation"
tags: ["crypto", "sui", "layer1", "vesting"]
published: true
---

> Originally published at **[mrnasdog.com/research/sui/inflation](https://mrnasdog.com/research/sui/inflation)** by MrNasdog.

**TL;DR.** Sui Network releases about **66M SUI** over the next 90 days — roughly **59M** in vesting through three monthly unlock steps plus about **7M** in staking subsidies — and nothing buys it back. The MrNasdog Pressure Framework reads about **+1.6% net** to market. Our supply monitor reads **+2.47%** realized over the last 90 days, within a few hundredths of a point of the framework's own trailing read — so there is no data conflict on this build.

## The verdict, in one paragraph

For the forward 90-day window the MrNasdog Pressure Framework reads **SUI at about +1.63% net**, driven almost entirely by scheduled vesting that out-issues everything else. Our supply monitor reads the realized last-90-day change at **+2.47%**, versus the framework's **+2.44%** read for that same trailing window — a gap of just **0.03 percentage points**, comfortably inside tolerance, so this build ships **no monitor-gap chip**. The two readings agree because Sui Network publishes its own monthly circulation schedule, and the framework books that schedule directly: circulating supply steps up about **22M SUI** a month, no more and no less. SUI is **structurally inflationary on the active float**, at a low-single-digit pace, with the vesting calendar — not the protocol mint — as the dominant force.

## Sell pressure: where new SUI comes from

Sell #2 — vesting unlocks — is the dominant force, at about **59M SUI** over the next 90 days. Locked SUI releases in steady monthly steps rather than lumpy cliffs, and three of those steps land in this window: **Aug 1**, **Sep 1** and **Oct 1 2026**, each adding roughly **22M SUI** to circulating supply. The mix now leans toward the community reserve and the contributor allocations rather than early-investor tranches. It is worth flagging one discrepancy: some public unlock trackers list a large ~91M "cliff" on Aug 2 2026, but Sui's own circulation schedule shows August adding only about 22M net — the larger figure is a gross-unlock artifact, and the framework follows Sui's own net schedule. Most of the still-locked 10B hard cap unlocks on a published calendar that runs into 2030, including a large reserve that only begins after 2030.

Sell #1 — protocol inflation — adds only about **7M SUI** to the tradable float over the same 90 days. Sui pays a staking subsidy each epoch that is temporary by design and shrinks over time; three years into the schedule, the per-epoch subsidy has decayed to a fraction of its launch rate. Most of that subsidy is paid to stakers who re-stake rather than sell, so its real impact on float is smaller still, and it is already folded into Sui's published circulation figure. Sell #3 — Foundation and unscheduled unlocks — is zero beyond the scheduled steps already counted, with no dated off-calendar release pending. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate or court distribution applies to SUI.

## Buy pressure: where new SUI goes

There is no meaningful buy-side offset. Buy #1 — programmatic buyback — is **zero**: Sui runs no protocol or treasury program buying SUI off the market. Buy #2 — protocol fee burn — is also carried at zero: gas fees are paid to validators and storage fees flow into a perpetual storage fund rather than being burned. That storage fund mildly slows effective supply growth as the network grows, and the documentation frames it as a long-run drag, but no fixed quantum of SUI is destroyed in the window, so the framework does not estimate it. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero, with no discretionary open-market buying or new escrow announced. A large share of SUI is staked, but staking does not remove supply. With nothing absorbing the monthly unlock, the full sell-side flow reaches the net read.

## Foundation and overhang

SUI carries a real, dated overhang: roughly **59%** of the 10B hard cap is still locked, releasing on a published calendar through 2030 and beyond. The largest long-dated piece is a reserve of about **5.2B SUI** — over half the entire cap — that only begins releasing after 2030. The nearer-term overhang is the community reserve of roughly **1.07B SUI**, custodied by the Sui Foundation, which feeds the monthly steps alongside smaller contributor and labs-treasury slices. These are not a discretionary stockpile that can dump at will — they are pre-scheduled, so the framework books them in Sell #2 by date rather than as a Sell #3 surprise. The framework re-checks the circulation schedule and chain emission on a roughly bi-weekly walk; if a Foundation reserve balance falls faster than the published schedule, that excess outflow enters Sell #3 at the next refresh.

## How SUI compares to other capped vesting-heavy L1s

SUI belongs to the class of **hard-capped layer-1 tokens with a long multi-year vesting tail** — closer to a venture-backed L1 still working through its unlock schedule than to a fully-distributed, emission-only chain. Unlike an uncapped proof-of-stake chain whose supply grows forever on a fixed inflation curve, SUI has a fixed 10B ceiling and a declining staking subsidy; the dominant supply force is not the protocol mint but the calendar of contributor and reserve unlocks still in flight.

The contrast worth drawing is with chains that pair their emission with a real burn — fee-burn networks or exchange tokens with quarterly buybacks that can tilt net-deflationary. SUI has neither: gas goes to validators and storage fees pool rather than burn, so there is no offset against the monthly unlock. That makes SUI read as cleanly, persistently inflationary for as long as the unlock calendar runs — the supply curve is dominated by what is scheduled to unlock, not by any mechanism removing coins.

## What to watch in the next 90 days

Watch the three monthly unlock steps on **Aug 1**, **Sep 1** and **Oct 1 2026**, each about 22M SUI — together they are the whole of the net read, so any change to their size or timing moves the framework directly. Watch the published circulation schedule itself: if Sui Foundation adjusts the calendar or a reserve releases ahead of plan, the next refresh will re-book it. Watch the bucket mix at each step, since a larger community-reserve share can change how much is sold versus staked or held. And watch the staking ratio, because a higher share staked means more of both the subsidy and the unlocks stays off the market.

## Summary

SUI is a hard-capped layer-1 token whose supply is still climbing on a multi-year vesting calendar. Over the next 90 days the chain releases about 66M SUI — roughly 59M in vesting through three monthly steps plus a ~7M staking subsidy — and with no buyback and no quantified burn to offset them, the framework reads about +1.6% net to market. Our supply monitor reads +2.47% realized over the last 90 days, within a few hundredths of a point of the framework, so there is no data conflict. SUI stays low-single-digit inflationary on the active float, with the unlock schedule — not any burn — as the force that decides the read.

*MrNasdog Pressure Framework analysis of Sui (SUI), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 6 2026.*

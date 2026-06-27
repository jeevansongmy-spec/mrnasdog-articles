---
title: "SUI Inflation Analysis · June 2026 · Monthly unlocks keep supply growing"
description: "Sui releases ~145M SUI over the next 90 days in monthly vesting cliffs (incl. a ~91M August cliff) plus ~19M subsidy, with no buyback or burn. Framework +4% net; monitor +3.36%."
canonical_url: "https://mrnasdog.com/research/sui/inflation"
tags: ["crypto", "sui", "layer1", "vesting"]
published: true
---

> Originally published at **[mrnasdog.com/research/sui/inflation](https://mrnasdog.com/research/sui/inflation)** by MrNasdog.

**TL;DR.** Sui Network releases roughly **145M SUI** over the next 90 days through three monthly vesting cliffs — including a large **~91M** August unlock — plus about **19M** in staking subsidies, and nothing buys it back. The MrNasdog Pressure Framework reads about **+4% net** to market. Our supply monitor reads **+3.36%** realized over the last 90 days, an almost exact match — so there is no data conflict on this build.

## The verdict, in one paragraph

For the 90-day window the MrNasdog Pressure Framework reads **SUI at about +4.07% net** on the forward view, driven almost entirely by scheduled vesting cliffs that out-issue everything else. Our supply monitor reads the realized last-90-day change at **+3.36%**, versus the framework's **+3.26%** read for that same trailing window — a gap of just **0.1 percentage points**, comfortably inside tolerance, so this build ships **no monitor-gap chip**. The two readings agree because the framework now books the unlock cliffs at their observed, irregular sizes — the early-investor tranche finished in May 2026, so recent cliffs are smaller — rather than a flat monthly average. SUI is **structurally inflationary on the active float**, at a mid-single-digit pace, with the vesting calendar — not the protocol mint — as the dominant force.

## Sell pressure: where new SUI comes from

Sell #2 — vesting unlocks — is the dominant force, at about **145M SUI** over the next 90 days. Locked SUI releases in monthly cliffs whose sizes vary, and three of them land in this window: **Jul 1**, **Aug 2** and **Sep 1 2026**. The August cliff is the large one, at roughly **91M SUI** — about 0.91% of total supply — while the July and September cliffs are closer to **27M** each. With the early-investor Series B linear vest having finished in May 2026, the monthly mix now tilts toward the community reserve, early contributors and the labs treasury. Most of the still-locked 10B hard cap unlocks on a published schedule that runs into 2030, including a large reserve that only begins after 2030.

Sell #1 — protocol inflation — adds about **19M SUI** to the tradable float over the same 90 days. Sui pays a staking subsidy each epoch that is temporary by design and falls roughly 10% every quarter; three years into the schedule, the per-epoch subsidy has decayed to a fraction of its launch rate. Most of that subsidy is paid to stakers who re-stake rather than sell, so its real impact on float is smaller than the gross mint. Sell #3 — Foundation and unscheduled unlocks — is zero beyond the scheduled cliffs already counted. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate or court distribution applies to SUI.

## Buy pressure: where new SUI goes

There is no meaningful buy-side offset. Buy #1 — programmatic buyback — is **zero**: Sui runs no protocol or treasury program buying SUI off the market. Buy #2 — protocol fee burn — is also carried at zero: gas fees are paid to validators and storage fees flow into a perpetual storage fund rather than being burned. That storage fund mildly slows effective supply growth as the network grows, but no fixed quantum of SUI is destroyed in the window, so the framework does not estimate it. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero, with no discretionary open-market buying or new escrow announced. With nothing absorbing the monthly unlocks, the full sell-side flow reaches the net read.

## Foundation and overhang

SUI carries a real, dated overhang: roughly 60% of the 10B hard cap is still locked, releasing on a published calendar through 2030 and beyond. The largest in-window source is the community reserve, which feeds the monthly cliffs alongside smaller early-contributor and labs-treasury slices. These are not a discretionary stockpile that can dump at will — they are pre-scheduled, so the framework books them in Sell #2 by date rather than as a Sell #3 surprise. The staking subsidy is a separate, continuous allocation that shrinks each quarter and is largely re-staked. The framework re-checks the unlock calendar and chain emission on a roughly bi-weekly walk; if a reserve balance falls faster than the published schedule, that excess outflow enters Sell #3 at the next refresh.

## How SUI compares to other capped vesting-heavy L1s

SUI belongs to the class of **hard-capped layer-1 tokens with a long multi-year vesting tail** — closer to a venture-backed L1 still working through its unlock schedule than to a fully-distributed, emission-only chain. Unlike an uncapped proof-of-stake chain whose supply grows forever on a fixed curve, SUI has a fixed 10B ceiling and a declining staking subsidy; the dominant supply force is not the protocol mint but the calendar of investor, contributor and reserve unlocks still in flight.

The contrast worth drawing is with chains that pair their emission with a real burn — fee-burn networks or exchange tokens with quarterly buybacks that can tilt net-deflationary. SUI has neither: gas goes to validators and storage fees pool rather than burn, so there is no offset against the monthly cliffs. That makes SUI read as cleanly, persistently inflationary for as long as the unlock calendar runs — the supply curve is dominated by what is scheduled to unlock, not by any mechanism removing coins.

## What to watch in the next 90 days

Watch the August cliff on **Aug 2 2026** — at roughly 91M SUI it is several times the size of the July and September unlocks and the single biggest driver of the net read. Watch the smaller cliffs on **Jul 1** and **Sep 1 2026**, around 27M each, which set the baseline now that the Series B tranche has finished. Watch the bucket mix at each cliff: as the community reserve carries more of the load, the share that is staked or held rather than sold can shift, which is what moves realized float versus the gross unlock. And watch the staking ratio, since a higher share staked means more of both the subsidy and the unlocks stays off the market.

## Summary

SUI is a hard-capped layer-1 token whose supply is still climbing on a multi-year vesting calendar. Over the next 90 days the chain releases about 145M SUI through three monthly cliffs — led by a large ~91M August unlock — plus a ~19M staking subsidy, and with no buyback and no quantified burn to offset them, the framework reads about +4% net to market. Our supply monitor reads +3.36% realized over the last 90 days, within a tenth of a point of the framework, so there is no data conflict. SUI stays mid-single-digit inflationary on the active float, with the unlock schedule — not any burn — as the force that decides the read.

---

*MrNasdog Pressure Framework analysis of Sui (SUI), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jun 28 2026.*

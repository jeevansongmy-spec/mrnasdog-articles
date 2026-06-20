---
title: "XTZ Inflation Analysis · June 2026 · Quiet chain, issuance cooled to a crawl"
description: "A MrNasdog Pressure Framework read of Tezos (XTZ): ~9.8M / 90D of Adaptive Issuance staking rewards, no buyback or burn offset. Framework +0.9% net; monitor +0.90%, a clean match."
canonical_url: "https://mrnasdog.com/research/tezos/inflation"
tags: ["crypto", "xtz", "tezos", "proof-of-stake"]
published: true
---

> Originally published at **[mrnasdog.com/research/tezos/inflation](https://mrnasdog.com/research/tezos/inflation)** by MrNasdog.

Tezos mints about **9.8M XTZ** into circulation over 90 days under Adaptive Issuance, with no buyback and no meaningful fee-burn offset, so the Pressure Framework reads about **+0.9% net**. Our supply monitor reads the realized last-90-day change at **+0.90%** — an almost exact match, because the framework books issuance straight off the same on-chain supply growth the monitor measures. XTZ is a quiet, slowly-inflating proof-of-stake chain.

## The verdict, in one paragraph

For the 90-day window ending June 16 2026, the MrNasdog Pressure Framework reads **XTZ at +0.9% net** on the forward view, driven entirely by Adaptive Issuance staking rewards with no offset on the buy side. Our supply monitor reads the realized last-90-day change at **+0.90%**, versus the framework's **+0.89%** read for the same window — a gap of about **0.01 percentage points**, comfortably inside tolerance, so **no monitor-gap chip** ships. The two agree because both observe Tezos's on-chain circulating supply directly: it grew from about 1,078.5M to 1,088.2M over the window. XTZ is **mildly inflationary on a falling curve**, the cleanest possible read.

## Sell pressure: where new XTZ comes from

Sell #1 — protocol inflation — is the entire story, at about **9.8M XTZ** reaching circulation over the next 90 days. Tezos is a Liquid Proof-of-Stake chain, and new XTZ is minted each cycle as baker and staker rewards under **Adaptive Issuance**, the mechanism introduced in the Paris upgrade in 2024. Adaptive Issuance lets the yearly rate float between **0.05% and 5%**, recomputing every cycle to nudge the staked-supply ratio toward a **50% target**. With staking participation high, the nominal rate has cooled toward the low single digits, and net supply reaching the float now runs near **0.9% per 90 days**.

Sell #2 — vesting unlocks — is **zero**: Tezos raised its funds in its 2017 launch, and the original team and Foundation allocations are fully distributed, so there is no investor cliff or unlock schedule hitting the market. Sell #3 — Foundation and unscheduled unlocks — is also zero as a flow; the Tezos Foundation funds grants over time, but there is no dated bulk release in this window. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate or court distribution applies to XTZ.

## Buy pressure: where new XTZ goes

There is no buy-side offset on XTZ. Buy #1 — programmatic buyback — is **zero**: Tezos runs no program that buys XTZ on the open market. Buy #2 — protocol fee burn — is carried at **zero** as well: Tezos does burn XTZ for storage and allocation costs, where execution and storage fees are destroyed rather than paid to bakers, but the amount is small and not separately published, and it is already netted into the observed circulating growth in Sell #1, so booking it again would double-count. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero, with no discretionary open-market buying or new escrow announced in the window.

## Foundation and overhang

The Tezos Foundation holds a treasury used to fund grants, development and ecosystem programs, but it is not a scheduled unlock overhang — there is no cliff that mechanically converts a locked balance into float on a known date. Spending is discretionary and spread over years, so it does not register as a dated supply event. The framework books no Foundation release beyond protocol inflation and re-checks the on-chain supply and Foundation activity on a roughly bi-weekly walk; if the Foundation's balance falls faster than its grant pace between refreshes, the outflow enters Sell #3 at the next refresh. For now, the only mover is Adaptive Issuance itself, which is exactly why the framework and the monitor agree so closely.

## How XTZ compares to other uncapped proof-of-stake chains

XTZ belongs to the class of **uncapped proof-of-stake L1s with a self-adjusting issuance rate** — closer to a continuous-emission chain than to a hard-capped, halving-model coin like Bitcoin. What sets Tezos apart inside that class is Adaptive Issuance: instead of a fixed schedule, the mint responds to how much of the supply is staked, falling as participation rises. That makes XTZ structurally inflationary but on a **downward-trending curve**, rather than a flat perpetual rate.

Compared with chains that pair emission with an aggressive burn — exchange tokens that buy and burn, or fee-burning smart-contract platforms that can flip net-deflationary in busy periods — Tezos has no real burn brake. Its storage burn is tiny relative to issuance, so net supply growth tracks the mint almost one-for-one. The result is a clean, predictable read: XTZ inflates at a low, falling rate, with nothing on the buy side strong enough to reverse it. For an inflation lens, that makes it one of the quieter, more legible supply stories among the major proof-of-stake L1s.

## What to watch in the next 90 days

Watch the staked-supply ratio — Adaptive Issuance lowers the mint as staking rises toward and past the 50% target, so a higher staking rate quietly pushes net inflation down further. Watch on-chain circulating supply, which is the single number that decides the net reading, since there is no unlock or buyback to surprise it. Watch for any Tezos protocol upgrade that changes issuance parameters, as governance can adjust the curve. And watch Foundation activity, the one discretionary lever that would enter Sell #3 if a large balance moved on a dated event.

## Summary

XTZ is an uncapped proof-of-stake coin whose supply grows under Adaptive Issuance, a rate that self-adjusts toward a 50% staking target and has cooled to the low single digits. Tezos mints about 9.8M XTZ into circulation over 90 days, with no buyback and no meaningful fee-burn offset, leaving the framework at about +0.9% net. Our supply monitor reads +0.90% realized over the same window — an almost exact match, because both measure the same on-chain supply growth. XTZ stays mildly inflationary on a falling curve, the cleanest read in the framework.

*MrNasdog Pressure Framework analysis of Tezos (XTZ), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 16, 2026.*

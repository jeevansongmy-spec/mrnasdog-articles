---
title: "KAS Inflation Analysis · June 2026 · Supply growing, but the mint shrinks every month"
description: "A MrNasdog Pressure Framework read of Kaspa (KAS): ~148M / 90D of fair-launch proof-of-work mining, an empty buy ledger, and a mint that decays each month. Framework +0.54% net; monitor +0.64%, a near-exact match."
canonical_url: "https://mrnasdog.com/research/kas/inflation"
tags: ["crypto", "kas", "kaspa", "proof-of-work"]
published: true
---

> Originally published at **[mrnasdog.com/research/kas/inflation](https://mrnasdog.com/research/kas/inflation)** by MrNasdog.

Kaspa mines about **148M KAS** over the next 90 days on a fair-launch proof-of-work schedule whose reward halves smoothly every month, and there is no buyback, burn or foundation buying to offset it. So the Pressure Framework reads about **+0.54% net** on the forward view, down from **+0.64%** last quarter. Our supply monitor reads **+0.64%** for the same trailing window — a match to within **0.01 percentage points**, with no ⚠ gap.

## The verdict, in one paragraph

For the 90-day window ending June 22 2026, the MrNasdog Pressure Framework reads **KAS at +0.54% net** on the forward view, driven entirely by proof-of-work mining emission with no offset on the buy side. Our supply monitor reads the realized last-90-day change at **+0.64%**, matching the framework's own **+0.64%** read for that trailing window almost exactly — a gap of about **0.01 percentage points**, well inside tolerance, so no **⚠ monitor-gap chip** ships. The match is structural: Kaspa's only supply event is mining, every mined coin reaches circulation, and that is precisely what the monitor measures. KAS is a **quiet, mildly inflationary fair-launch chain** whose issuance shrinks each month.

## Sell pressure: where new KAS comes from

Sell #1 — protocol inflation — is the entire story, at about **176M KAS** mined over the last 90 days and about **148M KAS** projected over the next 90. Kaspa is a pure proof-of-work BlockDAG: new KAS is created each block and paid directly to miners, with no dev tax and no allocation skimmed off the top. The reward follows a **chromatic** emission schedule — instead of a single annual halving, the block reward is cut smoothly every month by a factor of (1/2)^(1/12), so issuance falls a little each month rather than in one step. That is why the forward 90-day figure sits below the trailing one, and why it keeps drifting down quarter after quarter.

Sell #2 — vesting unlocks — is **zero**: Kaspa launched fair in November 2021 with no premine, no ICO, no venture allocation and no team tokens, so nothing was ever locked and no cliff can reach the market. Sell #3 — Foundation and unscheduled unlocks — is also **zero**, because there is no foundation treasury or insider stash to release; every coin in circulation was mined in the open. Sell #4 — long-term locked or bankruptcy — is **zero**, with no bankruptcy estate or court-ordered distribution attached to KAS.

## Buy pressure: where new KAS goes

The buy ledger is **empty**. Buy #1 — programmatic buyback — is **zero**: Kaspa has no protocol buyback, and the handful of third-party promos that call themselves KAS buyback-burns are not part of the chain, so the framework does not count them. Buy #2 — protocol fee burn — is **zero**: transaction fees on Kaspa are tiny and paid to miners, not burned, so nothing is removed from supply there. Buy #3 — Foundation buy — is **zero**, because there is no foundation or treasury to buy KAS on the open market. Buy #4 — new long-term lock — is **zero**, with no staking cap, escrow or multi-year lockup announced in the window. With nothing on the buy side, net inflation simply equals gross mining emission.

## Foundation and overhang

Kaspa has no overhang in the usual sense — there is no foundation wallet, no investor cliff and no unlock calendar, because the chain was never funded by a token sale. Development is paid for by community donations and by a small operation that mines KAS alongside everyone else rather than holding a pre-allocated reserve. That means there is no balance the framework needs to watch for a sudden release: the only source of new KAS is the block reward itself, already captured in Sell #1. If a large identified treasury ever began distributing — which the fair-launch design does not create — that outflow would enter Sell #3 at the next refresh; today there is nothing to track.

## How KAS compares to other proof-of-work chains

KAS belongs to the class of **hard-capped proof-of-work coins** — the same family as Bitcoin and Litecoin, where a fixed asymptotic cap (about 28.7 billion KAS) and a halving schedule define the monetary policy. The difference is the shape of the halving. Bitcoin steps its reward down once every four years, producing a sharp discontinuity at each halving; Kaspa spreads the same reduction across twelve monthly steps, so the curve is smooth and issuance declines a little every month. The Crescendo upgrade in May 2025 raised the chain to ten blocks per second while cutting the per-block reward by the same factor, leaving the KAS-per-second emission rate unchanged — a throughput change, not a monetary one.

Against uncapped proof-of-stake L1s, which mint perpetually to reward stakers, KAS is structurally tighter: emission is already past roughly 96% of the cap and shrinks each month, so dilution is low and falling rather than open-ended. And unlike exchange tokens that burn or buy back to go net-deflationary, Kaspa has no offsetting mechanism at all — the inflation lens is simply the mining curve, with no burn to read against it. For now that leaves KAS mildly inflationary, with the rate trending toward zero as the cap approaches.

## What to watch in the next 90 days

Watch the monthly step-downs in the block reward — each month the chromatic schedule shaves a little more off issuance, so the forward mint keeps easing without any announcement needed. Watch the share of the cap already mined; as KAS nears the ~28.7B asymptote, the inflation rate compresses further toward zero. Watch for any protocol proposal that would add a fee burn or change emission, though none is on the table — Kaspa has no central governance to enact one. And expect the framework and our supply monitor to keep agreeing closely, because mining is the only supply event and both measure the same realized coins.

## Summary

KAS is a fair-launch, hard-capped proof-of-work coin whose supply grows only through mining on a smoothly decaying schedule. The chain mined about 176M KAS over the last 90 days and will mine about 148M over the next 90, with no buyback, burn or foundation buying to offset it, leaving the framework at about +0.54% net forward. Our supply monitor reads +0.64% realized for the trailing window, matching the framework to within a hundredth of a point, so no gap chip ships. The key risk is simply continued mild dilution — but it is the lowest-discretion supply profile in the framework, with the mint shrinking month over month as the cap approaches.

*MrNasdog Pressure Framework analysis of Kaspa (KAS), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 22, 2026.*

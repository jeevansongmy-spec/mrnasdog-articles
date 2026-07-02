---
title: "JTO Inflation Analysis · June 2026 · Vesting with nothing to absorb it yet"
description: "No protocol mint, no live burn: JTO grows ~48.9M/90d through daily vesting with nothing to absorb it. Framework reads +10% net (monitor +7.69% — a gross-vest-vs-float gap)."
canonical_url: "https://mrnasdog.com/research/jto/inflation"
tags: ["crypto", "jito", "solana", "jto"]
published: true
---

> Originally published at **[mrnasdog.com/research/jto/inflation](https://mrnasdog.com/research/jto/inflation)** by MrNasdog.

Jito's governance token has no protocol mint and no active burn — its supply grows purely through a daily vesting unlock, about **48.9M JTO** over 90 days. With nothing on the buy side to absorb it, the Pressure Framework reads roughly **+10%** net. Our supply monitor reads **+7.69%** realized; the gap is vested coins landing in treasury and ecosystem pools rather than the open-market float.

## The verdict, in one paragraph

For the 90-day window ending June 30 2026, the MrNasdog Pressure Framework reads **JTO at about +10% net**, driven entirely by vesting unlocks of Jito. Our supply monitor reads the realized last-90-day circulating change at **+7.69%**, versus the framework's **+9.99%** gross-vest read for the same window — a gap of about **2.3 percentage points** that ships a **⚠ monitor-gap chip**. The gap is structural: the framework counts the gross daily vest of JTO (about **48.9M**), while the monitor counts realized float (about **34.95M**), and the roughly 14M difference is vested coins routed into DAO-treasury, ecosystem and community pools that are not yet open-market float. JTO is **structurally inflationary through vesting, with no offset**.

## Sell pressure: where new JTO comes from

Sell #1 — protocol inflation — is **zero** for JTO. Jito is a Solana liquid-staking and MEV protocol, and JTO is its governance token, not a chain's staking coin. Solana staking yields are paid in SOL, so no protocol mint ever issues new JTO. Every new JTO that enters the market comes from one place: the vesting schedule.

Sell #2 — vesting unlocks — is the entire flow, at about **48.9M JTO** over the next 90 days, roughly **543K JTO per day** on a smooth daily release. The unlocks come from the original 1B JTO allocation: **Core Contributors (24.5%)** on a three-year vest after a one-year cliff that ended December 7 2024, **Investors (16.21%)** on their multi-year schedule, and **Ecosystem Development (25%)** on a 48-month linear vest, with the long **Community Growth (34.29%)** pool releasing over roughly six years. Sell #3 — Foundation and unscheduled unlocks — is zero as a flow: the remaining locked portions of those same allocations are tracked overhangs that release only on their linear schedules, with no dated discretionary deployment. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate or court distribution applies to JTO.

## Buy pressure: where new JTO goes

The buy ledger is empty, and that is the crux of JTO's reading. Buy #1 — programmatic buyback — is zero in this window: the **JTX** consumer trading app plans to direct **80%** of its revenue to open-market JTO buybacks, but it launches in **July 2026** and is not buying yet, so the framework counts no buyback until it is executing on-chain. Buy #2 — protocol fee burn — is zero, and this is the important one: Jito generates real revenue from MEV and liquid staking, but that revenue **accrues to stakers and the DAO treasury**, not to a recurring JTO burn. A one-time **9.7M JTO** burn earlier in 2026 fell before this window and is not a standing mechanism. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero, with no discretionary buying or new escrow announced in the window.

## Foundation and overhang

JTO's overhang is the unreleased remainder of its four allocations: **Community Growth, Ecosystem Development, Core Contributors and Investors**, all on multi-year linear schedules running into and beyond 2026. Because the schedules are long — up to about six years for the community and ecosystem pools — supply keeps growing at a vesting-driven pace, smoothly rather than via cliffs. Part of each day's vest lands in DAO-treasury and ecosystem buckets that are not yet open-market float, which is exactly why realized supply grows slower than the gross unlock. The framework books no discretionary release beyond the daily vest and re-checks the unlock schedule and the JTX buyback status on a roughly bi-weekly walk; if a treasury balance falls faster than the schedule, the outflow enters Sell #3 at the next refresh.

## How JTO compares to other vesting-driven governance tokens

JTO belongs to the class of **vesting-driven governance tokens with no buy-side offset** — closer to a 2023-2024 governance launch on a long unlock calendar than to a fee-burn chain coin or a buyback-and-burn exchange token. Its supply curve is set by the unlock schedule, not by protocol emission, and unlike a hard-capped halving coin there is no fixed scarcity force pushing the other way. The result is a fairly clean function of the vesting calendar: positive, smooth, and persistent for as long as the multi-year schedules run.

The contrast worth drawing is with tokens that capture their own revenue in supply terms. An exchange token that burns quarterly, or a protocol that buys back and burns, turns revenue into a deflationary force; Jito today routes its MEV and staking revenue to stakers and the DAO instead, so JTO's value accrual is governance-mediated, not supply-mediated. For an inflation lens specifically, that means JTO reads as steadily inflationary while the vest runs — the revenue is real, but it does not yet show up as a buy-side offset. The JTX buyback, once live, would be the first mechanism to change that.

## What to watch in the next 90 days

Watch the **JTX launch in July 2026** — once the app ships and its 80%-of-revenue buyback begins executing on-chain, it becomes the first real buy-side offset to the vest, and the framework will start counting it in Buy #1. Watch the daily vesting pace, near **543K JTO per day**, which is smooth but shifts in mix as the Core Contributor three-year vest and the longer community and ecosystem schedules progress. Watch any DAO governance proposal that would route treasury revenue into a JTO buyback or burn. And expect the framework to keep reading above our supply monitor for as long as vested coins land in treasury and ecosystem pools rather than the open-market float — that gap is structural, not a new unlock.

## Summary

JTO is a vesting-driven governance token with no buy-side offset yet. A daily vesting unlock releases about 48.9M JTO over 90 days from its community, ecosystem, contributor and investor allocations, and because MEV and staking revenue accrue to stakers and the DAO rather than to a buyback or burn, nothing absorbs it. The framework reads about +10% net; our supply monitor reads +7.69% realized, with the gap explained by vested coins landing in treasury and ecosystem pools instead of the open float. JTO stays steadily inflationary while the multi-year vest runs — until the JTX revenue buyback goes live and adds the first offset.

---

*MrNasdog Pressure Framework analysis of Jito (JTO), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 30, 2026.*

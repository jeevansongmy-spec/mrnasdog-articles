---
title: "JTO Inflation Analysis · June 2026 · Vesting with nothing to absorb it"
description: "No emission, no burn: JTO grows ~37M/90d through linear vesting with nothing to absorb it. Framework reads +7.6% net (monitor +8.2% — a denominator convention)."
canonical_url: "https://mrnasdog.com/research/jto/inflation"
tags: ["crypto", "jito", "solana", "jto"]
published: true
---

> Originally published at **[mrnasdog.com/research/jto/inflation](https://mrnasdog.com/research/jto/inflation)** by MrNasdog.

Jito's governance token has no protocol emission and no burn — its supply grows purely through linear vesting, about **37M JTO** over 90 days. With nothing on the buy side to absorb it, the framework reads roughly **+7.6%** net. The monitor reads **+8.2%**; the small gap is a denominator convention, not a supply disagreement.

## The verdict, in one paragraph

For the 90-day window ending June 14 2026, the MrNasdog Pressure Framework reads **JTO at +7.6% net**, driven entirely by linear vesting. The inflation monitor reads **+8.2%** — a gap of **0.6 percentage points** that ships a **⚠ monitor-gap chip**. The two see the same ~37M of unlocks; the framework divides that flow by current circulating (485M → +7.6%) while the monitor divides by the 90-day-ago base (448M → +8.2%), so the gap is purely the **denominator convention** on a fast-growing supply. JTO is **structurally inflationary through vesting, with no offset**.

## Sell pressure: where new JTO comes from

Sell #1 — protocol inflation — is zero. JTO is a governance token; it is not the staking unit of a chain and pays no protocol emission. New JTO enters only through vesting.

Sell #2 — vesting unlocks — is the entire flow, at about **37M JTO** over 90 days. The unlocks come from four allocations on multi-year schedules: **Community Growth (34%)** and **Ecosystem Development (25%)** on roughly six-year linear schedules, **Core Contributors (24.5%)** on a three-year vest after a one-year cliff, and **Investors (16%)**. Sell #3 — Foundation and unscheduled unlocks — is zero as a flow: the remaining locked portions of those same allocations are tracked overhangs, releasing only on their linear schedules with no discretionary deployment. Sell #4 — long-term locked or bankruptcy — is zero.

## Buy pressure: where new JTO goes

The buy ledger is empty, and that is the crux of JTO's reading. Buy #1 — programmatic buyback — is zero; there is no JTO buyback. Buy #2 — protocol fee burn — is zero, and this is the important one: Jito generates real revenue from MEV and liquid staking, but that revenue **accrues to stakers and the DAO treasury**, not to buying back or burning JTO. So the token earns the protocol's economics indirectly through governance, but there is no mechanism that removes JTO from supply to offset the vesting. Buy #3 — Foundation buy — is zero. Buy #4 — new long-term lock — is zero.

## Foundation and overhang

JTO's overhang is the unreleased remainder of its four allocations: **Community Growth, Ecosystem Development, Core Contributors and Investors**, all on multi-year linear schedules. Because the schedules are long (up to ~6 years for the community and ecosystem pools), the supply will keep growing at a vesting-driven pace for years, but in a smooth, predictable way rather than via cliffs. The framework books no discretionary release beyond the linear vest and monitors the pools on a roughly bi-weekly walk; if a balance falls faster than the schedule, the outflow enters Sell #3 at the next refresh.

## How JTO compares to other vesting-driven governance tokens

JTO belongs to the class of **vesting-driven governance tokens with no buy-side offset**. Like many 2023–2024 governance launches, its supply curve is set by an unlock schedule rather than by protocol emission, and — unlike a fee-burn token or a revenue-buyback token — nothing on the protocol side reduces supply. That makes its inflation reading a fairly clean function of the vesting calendar: positive, smooth, and persistent for as long as the multi-year schedules run.

The contrast worth drawing is with tokens that capture their own revenue in supply terms. An exchange token that burns quarterly, or a protocol that buys back and burns, turns revenue into a deflationary force; JTO routes its MEV and staking revenue to stakers and the DAO instead, so the token's value accrual is governance-mediated, not supply-mediated. For an inflation lens specifically, that means JTO reads as steadily inflationary while the vest runs — the revenue is real but does not show up as a buy-side offset.

## What to watch in the next 90 days

Watch the vesting pace — the ~37M / 90-day rate is smooth, but the mix shifts as the Core Contributor three-year vest and the longer community and ecosystem schedules progress. Watch any governance proposal that would route DAO revenue into a JTO buyback or burn, which would add the buy-side offset the token currently lacks and change the reading materially. And note that the framework number will read slightly below the monitor for as long as the supply is growing fast, because the two use different denominators — that gap is convention, not a new unlock.

## Summary

JTO is a vesting-driven governance token with no buy-side offset. Linear vesting releases about 37M JTO over 90 days from its community, ecosystem, contributor and investor allocations, and because MEV and staking revenue accrue to stakers and the DAO rather than to a buyback or burn, nothing absorbs it. The framework reads +7.6% net; the monitor reads +8.2%, with the 0.6-point gap explained entirely by the current-vs-90-day-ago denominator convention. JTO stays steadily inflationary while the multi-year vest runs, unless governance later adds a buyback.

---

*MrNasdog Pressure Framework analysis of Jito (JTO), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 14, 2026.*

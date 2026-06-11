---
title: "OM Inflation Analysis · June 2026 · Supply growing, projected to keep growing"
description: "A MrNasdog Pressure Framework read of MANTRA (OM): fixed 8% staking inflation ~104M / 90D, empty buy ledger. Framework reads +2.00%; monitor +8.4% includes the Mar 2026 redenomination (⚠)."
canonical_url: "https://mrnasdog.com/research/om/inflation"
tags: ["crypto", "om", "mantra", "rwa"]
published: true
---

> Originally published at **[mrnasdog.com/research/om/inflation](https://mrnasdog.com/research/om/inflation)** by MrNasdog.

MANTRA's OM is the staking token of an uncapped RWA Layer 1 with a fixed 8% annual inflation. The Pressure Framework reads **+2.00% net** inflation from that staking emission (~104M / 90D) against a monitor reading of **+8.41%** — the larger figure includes the March 2026 redenomination, a one-time mint rather than recurring market supply.

## The verdict, in one paragraph

For the 90-day window the framework reads **OM at +2.00% net** inflation, booking the recurring 8% staking emission. The inflation monitor reads **+8.41%** over the same window — a gap of **6.41 percentage points** that triggers a ⚠ data-conflict chip. The deep walk explains it: the recurring flow is the fixed 8% annual inflation (~103.7M OM / 90D), and the remaining ~298M of the +402M the monitor observed is the March 3 2026 redenomination (OM → MANTRA, a 1:4 split) minting new units natively on MANTRA Chain — a one-time structural reclassification, not recurring supply. OM is structurally inflationary on continuous staking emission.

## Sell pressure: where new OM comes from

**Protocol inflation** booked **~104M OM**: MANTRA Chain runs a governance-fixed 8% annual inflation (Proposals 17-18), split 60% to staking rewards and 40% to the MANTRA Chain Association — roughly 103.7M OM of new emission per 90 days, the recurring supply flow. **Vesting unlocks** are zero this window: the next scheduled unlock (~21.2M) lands June 19 2026, inside the next 90-day window, so it is surfaced in the Upcoming strip rather than booked here, and the March 2026 redenomination was a one-time reclassification, not a market unlock. **Foundation and unscheduled unlocks** are zero as a booked figure, with the Association and the remaining locked allocation enumerated below. **Bankruptcy** is zero.

## Buy pressure: where new OM goes

The buy ledger is empty. **Programmatic buyback** is zero — staking rewards are paid from new emission, not from purchasing OM. **Protocol fee burn** is zero: periodic protocol-revenue burns have been discussed but no quantified in-window burn exists. **Foundation buy** is zero — the Association is a net recipient of inflation, not a market buyer. **New long-term lock** is zero — bonded staking is operational with a ~21-day unbond, not a long-term lock with an announced quantum.

## Foundation and overhang

Two overhangs are tracked. The **MANTRA Chain Association** receives 40% of the 8% inflation (~166M OM/yr) into a treasury whose deployment cadence is not published — a growing claim on the float. The **~479M OM still locked** on the vesting schedule is the second, releasing on a partial schedule whose next step is the June 19 2026 unlock (~21.2M). Both are walked bi-weekly. If either balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How OM compares to other RWA Layer 1s

OM is an uncapped, continuously-emitting RWA Layer 1 — mechanically closer to a Cosmos staking chain than to a fixed-cap governance token. Against Cosmos Hub's ATOM, the model is familiar (staking inflation paid to bonded holders), though OM's 8% is fixed by governance rather than floating on a bonded-ratio band. Against its RWA peers in coverage, OM is the only one whose supply pressure is protocol emission rather than vesting: ONDO is fixed-cap with cliff vesting, PLUME is fixed-cap with continuous vesting, and CFG inflates but parks the mint in its Treasury — whereas OM's 8% is distributed to stakers and the Association, so it reaches the float.

The mechanism that complicates OM this window is the redenomination. The March 3 2026 1:4 split (OM → MANTRA) minted new units natively on MANTRA Chain, which inflated the aggregator's supply count by a one-time amount unrelated to the recurring staking flow. The framework keeps its live read on the 8% emission (+2.00%) and ships the gap as a ⚠ chip rather than adopting the monitor's +8.41%, because a one-time redenomination is not recurring market supply.

The redenomination is worth one more sentence because it is the kind of event that routinely breaks supply trackers. A 1:4 split that natively mints new units changes the token count without changing any holder's economic stake — it is a units conversion, like a stock split, not a distribution. An aggregator that reads the post-split token count as a supply increase will report a large jump that has nothing to do with sell pressure, which is exactly what happened here. The framework separates the two and books only the recurring emission, which is why the page reads +2.00% and flags the rest as a ⚠ reclassification rather than adopting the headline figure.

## What to watch in the next 90 days

Three things move the reading. First, the **June 19 2026 unlock** (~21.2M OM) lands inside the next window and books into Sell #2. Second, the **8% inflation rate** — it is governance-set and reviewed at least annually, so a proposal to change it would shift the recurring baseline. Third, any **Association deployment** of its accrued 40% share — that would convert the parked overhang into real Sell #3.

## Summary

OM is the staking token of MANTRA, an uncapped RWA Layer 1, with a fixed 8% annual inflation (~104M OM / 90D) split between stakers and the Association — so the framework reads **+2.00% net** against a monitor reading of **+8.41%**, a 6.41-point gap carrying a ⚠ chip. The gap is the March 2026 redenomination, a one-time mint, not recurring supply. The key risks are the continuing 8% emission and the Association's growing, unscheduled treasury claim.

---

*MrNasdog Pressure Framework analysis of OM (MANTRA), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 12, 2026.*

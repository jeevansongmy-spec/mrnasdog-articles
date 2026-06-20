---
title:         "DCR Inflation Analysis · June 2026 · Supply growing, projected to keep growing"
description:   "Decred mints ~0.14M DCR per 90 days from a deterministic ~5.58 DCR block subsidy with no offsetting flow. Framework reads +0.83% net; decays 1% every ~21 days."
canonical_url: "https://mrnasdog.com/research/dcr/inflation"
tags:          ["crypto", "dcr", "decred", "pow"]
published:     true
---

*Originally published at [mrnasdog.com/research/dcr/inflation](https://mrnasdog.com/research/dcr/inflation)*

Decred (DCR) mints about **0.14M DCR** every 90 days from a deterministic hybrid PoW/PoS block subsidy of ~5.58 DCR, with nothing offsetting it. Framework reading: **+0.83% net** on a ~17.48M circulating base against a ~21M hard cap — about 83% issued, with the subsidy decaying 1% every ~21 days toward a final block in 2120.

## The verdict, in one paragraph

For the 90-day window ending June 20 2026, the framework reads **DCR at +0.83% net inflation** — pure block-subsidy issuance, no offsetting flow. The aggregator monitor reads **+0.83%**, a gap of essentially **0.00 percentage points** — one of the cleanest agreements in the catalog, so no warning chip. Decred is a structurally inflationary but mathematically predictable chain: a decade of hybrid proof-of-work and proof-of-stake emission, decaying smoothly, slowly approaching its hard cap.

## Sell pressure: where new DCR comes from

One source only. Sell #1 (protocol inflation) booked **~0.14M DCR**: Decred's block subsidy pays **~5.58 DCR** per block at roughly 5-minute blocks — about 288 blocks and 1,606 DCR per day, or 145,000 DCR per 90 days. The subsidy is fully deterministic: it began at 31.19582664 DCR at the Feb 2016 genesis and reduces by a factor of 100/101 every **6,144 blocks** (~21 days), so two small step-downs land inside any 90-day window and the run-rate eases slightly. Every block's subsidy splits 1% to PoW miners, 89% to staker votes, and 10% to the on-chain Treasury — but all three slices are new issuance, so Sell #1 captures the whole subsidy. Sell #2 (vesting unlocks) is **0** forever: the 1.68M DCR premine (8% of supply, split 4% dev fund and 4% airdrop) was fully distributed at launch, with no investor cohort and no vesting schedule. Sell #3 (Foundation and unscheduled unlocks) is **0** as new supply, with the on-chain Treasury enumerated as the only team-controlled overhang. Sell #4 (bankruptcy) is **0**.

The arithmetic is worth showing because Decred allows it cleanly. The chain targets a 5-minute block, so a day holds ~288 blocks. At **~5.58 DCR** each, that is ~1,606 DCR daily — ~145,000 DCR across 90 days, or 0.83% of the 17.48M circulating base. The monitor measured **+0.83%** over the same window from the supply data alone, independently of this derivation. When a protocol's entire supply policy is a single decaying subsidy and the observed chain matches the formula to a hundredth of a percent, the framework has nothing left to investigate — and that is exactly the appeal of a deterministic emission asset.

## Buy pressure: where new DCR goes

The buy ledger is structurally empty. Buy #1 (programmatic buyback) is **0**: Decred has no protocol buyback — its Treasury funds development through DAO votes, not market buys. Buy #2 (protocol fee burn) is **0**: transaction fees flow to PoW miners and PoS voters as part of the reward, so nothing is destroyed. Buy #3 (Foundation buy) is **0**; no accumulation programme buys DCR from the market. Buy #4 (new long-term lock) is **0** on a net basis: PoS staking locks DCR in time-locked tickets, but tickets continuously mature and the DCR they hold is already counted as circulating — staking churns the float rather than removing it. New supply enters; nothing structurally leaves.

## Foundation and overhang

Decred has one team/DAO-controlled overhang: the **on-chain Treasury**, currently around **786K–867K DCR**, fed by the 10% slice of every block subsidy that is already counted inside Sell #1. The Treasury is governed by Politeia, Decred's on-chain proposal-and-vote system, and in Q1 2026 the community passed DCP-0013, which caps spending at **4% of the balance per month** with a minimum floor near 10,800 DCR. Crucially, Treasury outflows are development funding, not new issuance — they move already-issued DCR from a protocol wallet into the hands of contributors, so they do not change the supply total. If the Treasury's balance falls between refreshes through approved spending, that outflow enters Sell #3 at the next refresh as a tracked float change, not as fresh inflation.

## How DCR compares to other capped-supply hybrid chains

Among hard-cap emission chains, Decred sits between Bitcoin's step-halving model and a continuous-decay curve. Bitcoin cuts its reward in half every four years; Decred instead trims 1% every ~21 days, producing a smooth geometric decay rather than abrupt cliffs. The result is a much steadier issuance schedule with no halving-day shocks — the rate just keeps easing, block after block, toward a final subsidy around September 2120. At ~0.83% per 90 days, Decred's pace is modestly higher than Bitcoin's post-2024 ~0.2% and Litecoin's ~0.42%, reflecting that DCR is ~83% issued versus their higher mined fractions.

What sets Decred apart from pure-PoW peers is the hybrid model and the Treasury. Where Bitcoin and Litecoin route the entire subsidy to miners, Decred splits it — 1% PoW, 89% staker votes, 10% Treasury — which folds a self-funding development budget directly into issuance instead of relying on an external foundation. That makes Decred structurally different from exchange tokens that buy back and burn: DCR has no revenue dependence, no discretionary burn, and no governance lever that can vote emission higher. The supply curve is coded, and the only discretion in the system is how the already-issued Treasury slice gets spent.

It is also worth naming what Decred does not have, because the absences are structural in this framework: no investor vesting cliff left from any era, no opaque foundation treasury off-chain, no buyback that could shrink in a weak quarter, and no governance process that could raise the subsidy. The one watch line — Treasury spending — moves float, not supply.

## What to watch in the next 90 days

Genuinely little on the supply side. The block subsidy will step down by 1% roughly four times across the window, easing the run-rate slightly below the headline figure — the framework reading stays near **+0.83%**. The structural watch lines are governance items, not supply events: any new Politeia proposal that draws down the **Treasury** under the DCP-0013 4% monthly cap (a float change, tracked in Sell #3), and any consensus proposal touching the subsidy split or schedule. None changing the issuance curve is currently pending. Hashrate and ticket-pool swings can wobble block timing by a few percent, which is noise at this scale.

## Summary

Decred is a hybrid PoW/PoS, hard-cap chain emitting **~0.14M DCR per 90 days** from a ~5.58 DCR block subsidy that decays 1% every ~21 days, with an empty buy ledger and a single on-chain Treasury overhang that spends rather than issues. The framework reads **+0.83% net**; the monitor agrees to within a hundredth of a point. The trajectory is fully coded: ~83% of the ~21M cap is issued, the subsidy keeps stepping down toward 2120, and nothing discretionary can move the supply curve. DCR is one of the most predictable inflation profiles in coverage — mildly inflationary, by design, and easing.

---

*MrNasdog Pressure Framework analysis of DCR, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 20, 2026.*

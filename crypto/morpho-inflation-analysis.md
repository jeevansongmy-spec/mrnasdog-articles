---
title: "Morpho (MORPHO) Inflation Analysis: A Multi-Cohort Vesting Unlock With No Offset"
description: "A MrNasdog Pressure Framework read of Morpho (MORPHO): multi-cohort vesting unlock adds ~96M MORPHO / 90D with no offsetting buyback. Framework reads +14.87%, aggregator +17.49%. Material net inflation on a 1B fixed cap."
canonical_url: "https://mrnasdog.com/research/morpho/inflation"
tags: ["crypto", "morpho", "defi", "lending"]
published: true
---

> Originally published at **[mrnasdog.com/research/morpho/inflation](https://mrnasdog.com/research/morpho/inflation)** by MrNasdog.

Morpho is in the middle of a multi-cohort vesting unlock that adds roughly 96M MORPHO every 90 days from Founders, Strategic Partners, and Contributor schedules. Nothing offsets it — the fee switch is not active, and there's no buyback. Framework reading: **+14.87% net** on a 1B fixed cap.

## The verdict, in one paragraph

For the 90-day window ending June 10 2026, the framework reads **MORPHO at +14.87% net inflation** — heavy unlock pressure from the active cohort schedules with no offsetting flow. The aggregator monitor reads **+17.49%**, a 2.62-percentage-point gap above the framework reading. The gap is explained by the monitor's denominator convention (it divides by the 90-day-ago supply, not the current supply) plus the discretionary deployment buckets held by Morpho Labs and the Morpho Association, which the framework does not enumerate without on-chain confirmation. The two readings agree on direction: MORPHO is experiencing meaningful supply growth.

## Sell pressure: where new MORPHO comes from

MORPHO has a 1 billion fixed cap minted at genesis (June 24 2022 legacy contract). The mint function is no longer callable, so Sell #1 — protocol inflation — is permanently zero. Every token that will ever exist already exists; the supply pressure comes from the **vesting schedule** releasing pre-minted tokens into circulation, which sits in Sell #2.

Three cohorts are actively vesting through the window. **Founders** (15.2% allocation, 152M MORPHO total) are on a 2-year linear schedule running through May 17 2028, after a unanimous relock in May 2025. **Strategic Partners Cohort 3** (6.7% allocation, 67M MORPHO) is on a 2-year linear from late November 2025 through November 2027. **Contributors** (5.8% allocation, 58M MORPHO) continues on its multi-year linear schedule. Combined, the three streams release roughly 96M MORPHO over 90 days at current pace.

Sell #3 — the discretionary buckets — is where the framework reads conservative against the monitor. The Morpho DAO Treasury holds 354M MORPHO; Morpho Association holds ~63M; Morpho Labs holds ~58M. These buckets can be deployed to market at the DAO's or the entity's discretion. MIP 131 (a 150M MORPHO grant proposal for the Strategic Support Program 2026-2030) was under governance discussion through May 2026 but had not executed. The framework does not enumerate Sell #3 without a confirmed on-chain transaction or a ratified governance proposal — so this row sits at zero, with a watching flag for the next refresh. The Apollo cooperation agreement from February 2026 (authorising up to 90M MORPHO over 48 months) sits in the same category: authorised but not enumerated as in-window flow.

## Buy pressure: where the MORPHO goes

The buy ledger is empty. **The Morpho Blue fee switch is not active** as of June 2026 — the infrastructure exists at the smart-contract level (capped at 25% of borrower interest), but the legal and tax work required for activation had not completed at the time of the most recent governance disclosure. When and if it activates, it could fund a DAO-side accumulator. Buy #2 (fee burn) is zero — MORPHO is a governance token with no burn mechanism. Buy #3 (Foundation buy) is zero — the Morpho Association is the issuer, not an accumulator. Buy #4 (new long-term lock) is zero — there is no veMORPHO or comparable lock mechanism.

The structural absence of a buy-side flow is the load-bearing reason MORPHO reads as inflationary right now. Once the cohort vesting completes in 2027-2028, sell pressure compresses naturally. Until then, the framework reading is dominated by the unlock cadence.

## Foundation and overhang

The Morpho DAO Treasury (35.4% of supply, 354M MORPHO) is the single largest team-controlled overhang in the protocol. The DAO controls it via governance vote, requiring a 500K MORPHO proposal threshold. MIP 131's 150M MORPHO Strategic Support Program is the watch item — if it ratifies and deploys, Sell #3 activates immediately. The Apollo cooperation agreement is a separate watch line: 90M MORPHO authorised over four years, no confirmed delivery in window, but if Apollo begins taking delivery from the Morpho Association at material pace, Buy #3 might activate on the demand side.

## How MORPHO compares to other DeFi governance tokens

Among DeFi lending governance tokens, MORPHO sits at one extreme of the inflation spectrum. Aave (AAVE) and Maker (now Sky / SKY) are both at or very near full supply, with no meaningful active vesting. Their inflation reads come from emission programs or buyback flows. Compound (COMP) finished its early vesting years ago and shows essentially flat supply. Morpho launched its token only in November 2024 with 11.2% circulating at TGE, and the multi-cohort unlock is now in full swing. MORPHO is the highest-inflation lending governance token in coverage today, by a meaningful margin.

The structural reason is the long-tail vesting design — Founders and Strategic Partners chose multi-year linear schedules with cliff structures, so the supply expansion compounds over time rather than firing in a single event. This trades short-term sell-pressure spikes (like ENA's cliff events or DYDX's scheduled unlocks) for a longer plateau of moderate sell pressure.

## What to watch in the next 90 days

Three things move the framework reading. First, **MIP 131 ratification** — if the 150M strategic support proposal passes governance, Sell #3 activates and the inflation reading jumps materially. Second, the **Apollo cooperation agreement** — any confirmed delivery tranche would mean Apollo is acquiring MORPHO directly, potentially via OTC from Morpho Association, which could either show up as Buy #3 (if classified as accumulation) or as additional Sell #3 (if Morpho Association deploys to fund the OTC). Third, the **fee switch** — activation announcements would change the buy-side reading immediately, and the legal/tax timeline remains the gating factor.

## Summary

MORPHO is in the middle of a multi-year cohort unlock and has no active offsetting flow. The framework reads +14.87% net for the trailing 90 days; the aggregator monitor reads +17.49%, with the 2.62-percentage-point gap explained by denominator convention plus undeployed discretionary buckets. The buy ledger is structurally empty pending fee-switch activation. The single most important watch line is MIP 131 ratification, which could materially change the reading. Until the cohort schedules complete in 2027-2028, MORPHO sits among the most inflationary lending governance tokens in coverage.

---

*MrNasdog Pressure Framework analysis of Morpho (MORPHO), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 10, 2026.*

---
title: "AAVE Inflation Analysis · July 2026 · Buyback edges out emission, supply roughly steady"
description: "A MrNasdog Pressure Framework read of Aave (AAVE): a fixed 16M cap with no mint, a ~0.026M/90d revenue buyback held in reserve just outweighing a ~0.014M safety-module emission. Framework −0.08%; monitor +0.28%."
canonical_url: "https://mrnasdog.com/research/aave/inflation"
tags: ["crypto", "aave", "defi", "buyback"]
published: true
---

> Originally published at **[mrnasdog.com/research/aave/inflation](https://mrnasdog.com/research/aave/inflation)** by MrNasdog.

AAVE is hard-capped at **16M** with no mint function, so there is no protocol inflation. The only new float is the Ecosystem Reserve streaming about **0.014M AAVE** to Safety Module stakers over the next 90 days, while a revenue-funded buyback takes roughly **0.026M AAVE** off the market and holds it — a net of about **−0.08%**. Our supply monitor reads **+0.28%** over the last 90 days, a gap of about **0.32 percentage points**, inside tolerance.

## The verdict, in one paragraph

For the 90-day window ending July 8 2026, the MrNasdog Pressure Framework reads **AAVE at about −0.08% net** on the forward view — the buyback slightly outweighing the Safety Module emission on a capped supply. Our supply monitor reads the realized last-90-day change at **+0.28%**, versus the framework's **−0.04%** read for the same window — a gap of about **0.32 percentage points**, inside the 0.5-point tolerance, so no monitor-gap chip is raised. The two agree because the bought-back AAVE is held in the DAO Collector, which the monitor's upstream still counts as circulating; that leaves realized circulating drifting only slightly up from the reserve emission, close to the framework's near-flat read. AAVE is **capped and roughly steady**, tilting a touch deflationary on the active float.

## Sell pressure: where new AAVE comes from

Sell #1 — protocol inflation — is **zero**. AAVE is hard-capped at **16M** and has no mint function; the 2020 LEND-to-AAVE migration minted 13M and 3M went to the Ecosystem Reserve, and nothing new is issued. Sell #2 — vesting unlocks — is also **zero**: the migration is long finished and every original team, seed and investor allocation has fully vested, so no cliff reaches the market.

Sell #3 — Foundation and unscheduled unlocks — is the only live sell row, at about **0.014M AAVE** over the next 90 days. This is the legacy Safety Module: the Ecosystem Reserve streams AAVE to stkAAVE stakers as rewards, and governance cut that rate from roughly **220 AAVE** a day to about **150 AAVE** a day — a 2.75% staking-APR target — in an ARFC that closed June 26 2026. It is a release of already-minted reserve supply into the float, not new issuance. Sell #4 — long-term locked or bankruptcy — is **zero**, because no bankruptcy estate or court distribution applies to AAVE.

## Buy pressure: where new AAVE goes

Buy #1 — programmatic buyback — is the offsetting force, at about **0.026M AAVE** over 90 days, or roughly **292 AAVE** a day bought on the open market. Under Aavenomics, the buyback was made permanent in 2025, had its budget trimmed from **$50M** to **$30M** a year in March 2026, and became automatic and non-discretionary as "Aavenomics 3.0" on June 27 2026, funded by protocol and GHO revenue. We book the buyback at its actual reported pace rather than the full budget ceiling, because revenue is running below the cap. The bought AAVE is held in the DAO Collector — accumulated, not burned — so it removes float but does not destroy supply.

The other buy rows are **zero**. Buy #2 — protocol fee burn — is zero: AAVE has no fee-burn mechanism, and revenue funds the buyback instead of destroying tokens, though governance has floated an optional future burn. Buy #3 — Foundation buy — is zero as a separate line, because the DAO's open-market buying is the programmatic buyback already in Buy #1. Buy #4 — new long-term lock — is zero, with no new multi-year lock or escrow announced in the window.

## Foundation and overhang

About **0.82M AAVE** sits outside the circulating float, held across the DAO's Ecosystem Reserve and the Collector. The Ecosystem Reserve is the source of the Safety Module emission and holds the deployable AAVE that governance can direct; the Collector is where protocol revenue and the bought-back AAVE accumulate. Both are on-chain, DAO-controlled, and tracked as team-controlled overhangs. The framework books no discretionary release from them beyond the documented Safety Module stream, and re-checks the emission rate and the reserve balances on a roughly bi-weekly walk. If either the Ecosystem Reserve or the Collector balance falls between refreshes, that outflow enters Sell #3 at the next refresh.

## How AAVE compares to other capped DeFi tokens

AAVE belongs to the class of **hard-capped tokens with a revenue-funded buyback** — closer in mechanism to an exchange token like BNB or OKB than to an uncapped emission L1. Where an uncapped chain mints new supply continuously and a fee-burn chain like Ethereum destroys a slice of every transaction, AAVE does neither: its 16M cap means no mint, and it has no burn. The supply-side lever it does share with exchange tokens is the buyback — protocol revenue used to buy the token back off the market.

The key mechanism difference is what happens to the bought token. An exchange token that runs a buyback-and-**burn** permanently retires the supply it buys, so each buyback shrinks the cap-relative float for good. Aave runs a buyback-and-**hold**: the AAVE it buys accumulates in the DAO Collector rather than being destroyed, so it leaves the active float but could, in principle, be redirected by governance later. That is why AAVE reads as roughly steady rather than firmly deflationary — the reserve emission adds a little float, the buyback removes a little more, and the net lands close to flat. For an inflation lens specifically, AAVE is one of the calmest profiles in DeFi: capped, no mint, no scheduled unlocks, and a buyback that just tips the balance to the deflationary side.

## What to watch in the next 90 days

Watch the Aavenomics 3.0 routing decision — the DAO has said the split of bought-back AAVE between the treasury, the Safety Module, and any burn will be finalized at the next quarterly community call; a decision to burn would flip the buyback from hold to permanent removal. Watch the buyback pace itself: it is funded by protocol and GHO revenue, and borrow-fee revenue was down about 25% from its peak, so the roughly 292 AAVE a day can rise or fall with revenue. Watch the Safety Module emission holding near 150 AAVE a day after the June 26 2026 cut, and the Umbrella migration, which could wind down legacy stkAAVE rewards and end the AAVE emission entirely. And watch for any governance move to enable an AAVE burn, which would be the first mechanism to shrink the capped supply outright.

## Summary

AAVE is a hard-capped DeFi governance token on Ethereum with no mint, no scheduled unlocks, and no fee burn. The only new float is a Safety Module emission of about 0.014M AAVE over 90 days from the Ecosystem Reserve, and a revenue-funded buyback of about 0.026M AAVE just outweighs it — leaving the framework at roughly −0.08% net, in line with the monitor's +0.28% realized read within 0.32 points. The bought AAVE is held rather than burned, so the profile is roughly steady with a slight deflationary tilt. The main thing that could change the reading is a governance decision to burn the buyback stack, which would turn a capped-but-flat supply into a shrinking one.

---

*MrNasdog Pressure Framework analysis of Aave (AAVE), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 8 2026.*

---
title: "Hyperliquid (HYPE) Inflation Analysis: The Buyback Is Bigger Than the Unlock"
description: "A MrNasdog Pressure Framework read of Hyperliquid (HYPE): Assistance Fund buys ~2.95M HYPE / 90D from platform fees, 3× the team-vault claim rate. Framework reads −0.876% net. Structurally deflationary by design."
canonical_url: "https://mrnasdog.com/research/hype/inflation"
tags: ["crypto", "hyperliquid", "defi", "perpetuals"]
published: true
---

> Originally published at **[mrnasdog.com/research/hype/inflation](https://mrnasdog.com/research/hype/inflation)** by MrNasdog.

Hyperliquid's Assistance Fund buys ~2.95M HYPE every 90 days from platform fee revenue, three times the team-vault claim rate. Framework reading: **−0.876% net** on a 1B protocol-immutable cap. The buyback is bigger than the unlock — by design.

## The verdict, in one paragraph

For the 90-day window ending June 10 2026, the framework reads **HYPE at −0.876% net inflation** — a structurally deflationary read driven by the Assistance Fund accumulating HYPE faster than the Core Contributors cohort claims it. The aggregator monitor reads **−6.63%**, a 5.75-percentage-point gap below the framework reading. The gap is explained by a documented aggregator re-baseline event: the upstream CG circulating field reclassified roughly 14M HYPE from circulating to non-circulating during Q1 2026, then another 13.85M in May. On-chain flow accounts for ~1.95M of the 15.8M circulating decrease; the remaining 13.85M is the re-classification. Framework reading holds primary; monitor headline carries the additional reclassification noise.

## Sell pressure: where new HYPE comes from

HYPE has a 1B protocol-immutable cap, and the cap is meaningful: there is no validator-issuance inflation. Gas fees on Hyperliquid pay validators directly out of fee revenue, and staking rewards come from a separate pre-funded pool rather than new mint. Sell #1 (protocol inflation) is permanently zero.

Sell #2 — vesting unlocks — is the only active sell-side flow. The **Core Contributors cohort** claims HYPE from the vesting pool at an actual on-chain rate of roughly 330K HYPE per month, against an authorized ceiling of ~9.92M per month. The framework counts actual behaviour, not the ceiling, so this row sits at ~1.0M HYPE per 90 days. This is the load-bearing convention for HYPE: the team could claim much more, but they don't, and the framework reads the actual rather than the potential.

Sell #3 — Foundation discretion + unscheduled — is zero with full enumeration of the four team-controlled overhangs: Future Emissions ~414.7M HYPE (governance-gated behind a 2-year minimum vote — even if voted today, cannot release in this 90-day window), Vault contract ~241.6M (Core Contributors vesting pool; only the ~1.0M/90d in Sell #2 flows out), Hyper Foundation safe ~60M (discretionary holder, slow grant deployment), and the Assistance Fund itself ~44.6M (only accumulates, no outflow observed). Sell #4 (bankruptcy estate) is zero.

## Buy pressure: the Assistance Fund

The dominant buy flow is the **Assistance Fund**. The AF accumulates roughly 67% of platform fees, converted on-market to HYPE via Hyperliquid's own order book. The verified daily accrual rate is steady at ~32,723 HYPE per day = ~2.95M HYPE per 90 days. The AF only accumulates; there is no observed outflow from the wallet, so every HYPE bought is effectively removed from market float.

This is the load-bearing structural fact about HYPE's tokenomics: the buyback is roughly 3× the team's actual claim rate. As long as Hyperliquid's platform fee revenue continues, the AF accumulates faster than the vesting pool releases. Buy #2 (fee burn) is zero — the trace ~1,676 HYPE in null/dead addresses is rounding noise from genesis distribution. Buy #3 (Foundation buy) is zero; all Foundation-led buy activity flows through the AF. Buy #4 (new long-term lock) is zero; staking unbond is ~7 days (operational, not long-term).

## Foundation and overhang

The four team-controlled overhangs are tracked but not in the active ledger. The most consequential is **Future Emissions ~414.7M** — gated behind a 2-year governance vote, this is the upside risk to a future inflation reading. If Hyperliquid governance ever votes to release Future Emissions, the framework reading would shift materially. The Vault contract ~241.6M is where Core Contributors continue to claim from; the 240M+ remainder is structural overhang, not active flow. The Hyper Foundation safe ~60M is a slow grant-deployment holder; no observed firings in window. The Assistance Fund's own ~44.6M balance is the cumulative buyback inventory.

## How HYPE compares to other revenue-driven tokens

Among revenue-driven governance tokens, HYPE's design is unusually aggressive in routing platform fees back into the token. Roughly 67% of fees flow to the AF for HYPE buybacks, compared to Jupiter's 50% to Litterbox or Sky's variable rate Smart Burn Engine deploy. The AF doesn't burn — it accumulates — which means the buyback inventory continues to grow indefinitely as long as Hyperliquid platform usage continues.

The closest structural analogue is BNB's quarterly burn (revenue-funded, but BNB burns rather than holds). Differences from HYPE: BNB burns at quarter end (lumpy), HYPE accumulates daily (continuous); BNB removes from circulation permanently, HYPE could theoretically deploy the AF in a crisis (the "Assistance" framing). Both designs achieve net-deflationary supply trajectory; HYPE's is more aggressive per dollar of revenue.

## What to watch in the next 90 days

Three things move the framework reading. First, **Hyperliquid platform fee revenue** — the AF accrual rate tracks directly with platform usage. A sustained drop in trading volume would compress the buyback pace. Second, the **Future Emissions governance vote** — there is no signal of imminent governance action, but any movement on this would be the single most consequential event for HYPE's inflation reading. Third, watch for any **AF deployment** — the fund's purpose includes acting as a backstop in case of market dislocation. If the AF ever distributes accumulated HYPE rather than holding it, the framework's buy reading changes.

## Summary

HYPE is a 1B fixed-cap token with no protocol-issuance inflation, a slow team-vesting claim, and a revenue-funded buyback (Assistance Fund) that runs 3× the vesting claim rate. The framework reads −0.876% net for the trailing 90 days — structurally deflationary. The aggregator monitor reads −6.63%, with the additional 5.75-percentage-point gap explained by documented CG re-baseline reclassification (the monitor headline is more deflationary than on-chain flow). HYPE in mid-2026 is the cleanest example in coverage of a "buyback bigger than unlock" structure that comes directly from platform revenue.

---

*MrNasdog Pressure Framework analysis of Hyperliquid (HYPE), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 10, 2026.*

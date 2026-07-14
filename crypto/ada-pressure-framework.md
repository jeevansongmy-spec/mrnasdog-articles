---
title:         "ADA Inflation Analysis · July 2026 · The reserve drips, and now the treasury spends"
description:   "Cardano adds ~326M ADA/90d — a ~185M reserve drip plus a ~141M treasury spend-down — with no burn or buyback. Framework reads +0.87% net (monitor +0.88% — they agree)."
canonical_url: "https://mrnasdog.com/research/ada/inflation"
tags:          ["crypto", "ada", "cardano", "inflation"]
published:     true
---

*Originally published at [mrnasdog.com/research/ada/inflation](https://mrnasdog.com/research/ada/inflation)*

**TL;DR.** Over the last 90 days about **326M ADA** reached the tradable float on Cardano — roughly **185M** from the fixed reserve and another **141M** as the on-chain treasury spent down its 2026 budget, with no burn or buyback anywhere to offset it. The framework reads about **+0.87%** net, and our supply monitor agrees at **+0.88%**. ADA is capped at 45 billion, but it is far from fully circulating, so the protocol keeps moving coins to market every epoch.

## The verdict, in one paragraph

For the 90-day window ending Jul 14 2026, the MrNasdog Pressure Framework reads **Cardano at +0.87% net** on the last-90-day view and **+0.73%** forward. Our supply monitor reads the realized last-90-day change at **+0.88%** — the tradable float grew from about **36,955M to 37,281M ADA**, a rise of roughly **326M** — putting the gap at just **0.005 percentage points**, so there is **no monitor-gap chip**. The float grew for two on-chain reasons this window: the reserve released about **185M ADA** of new supply, and the Cardano treasury balance fell about **141M** as approved budget proposals disbursed. ADA is therefore **mildly, structurally inflationary** — supply is growing on two fronts, and it is projected to keep growing at a low, gently declining pace.

## Sell pressure: where new ADA comes from

Sell #1 — protocol inflation — is about **185M ADA** over the last 90 days, easing to roughly **183M** forward. This needs a careful read, because ADA is capped at 45 billion and no new coins are minted above that ceiling. Instead, new supply is **released from a fixed reserve** set aside at genesis. Every 5-day epoch, the Cardano protocol moves **0.3%** of whatever remains in the reserve into a reward pot; **20%** of that pot goes to the treasury and the rest is paid as staking rewards, and both shares leave the reserve into counted supply. On-chain, the reserve fell from about **6,432M to 6,246M ADA** across the window — a drawdown of **185M** — and because the release is a fixed share of a shrinking reserve, the rate is **disinflationary** by design, with a reserve half-life of roughly four to five years.

Sell #3 — Foundation and unscheduled unlocks — is the new figure this window, at about **141M ADA**. The Cardano on-chain treasury, which now holds around **1.47B ADA**, is being spent down: its balance fell about 141M over 90 days as the **2026 Intersect budget** process disbursed approved proposals. A treasury can only fall through governance treasury-withdrawals, so this decline is previously-locked ADA moving into the float — real sell pressure the framework now books. Forward, that flow is projected lower, near **90M**, because the on-chain pace is already decelerating and a **350M-ADA net-change limit** caps how much treasury ADA can leave through mid-2027. Sell #2 — vesting unlocks — is **zero**: the 2017 public sale, the founding organisations and the Cardano Foundation finished distributing their allocations years ago. Sell #4 — long-term locked or bankruptcy — is zero, with no estate or court distribution in play for ADA.

## Buy pressure: where new ADA goes

This is the short half of the ledger: **nothing**. Buy #1 — programmatic buyback — is zero, because Cardano runs no buyback; neither the protocol nor the treasury buys ADA on the open market. Buy #2 — protocol fee burn — is also zero, and this is the detail people most often get wrong about Cardano. Cardano does **not burn transaction fees**. Fees are collected into a pot and recycled to stakers and the treasury, so they circulate rather than disappear. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero, with no discretionary open-market buying or new escrow announced in the window, and staking on Cardano is **non-locking**, so delegated ADA stays liquid. With no burn and no buyback anywhere on the network, nothing pulls supply back, so both the reserve drip and the treasury payout land net positive.

## Foundation and overhang

ADA has no classic unlock overhang — the early Cardano allocations are fully distributed. The pool that matters is the **on-chain treasury**, which receives 20% of every epoch's reward pot and holds on the order of **1.47B ADA**. Unlike a static reserve, it is now an **active** source of float: it fell about 141M over the last 90 days as the 2026 budget disbursed, and that outflow is exactly what Sell #3 tracks. The treasury can only be spent through **Voltaire-era governance** — each proposal ratified by delegate representatives (DReps) and bounded by the **2026-27 Net Change Limit** of 350M ADA. Two live examples frame the pace: a **7.8M ADA** Cardano Summit budget that failed its 66.67% vote in June 2026, and an approved **3.3M ADA** EMURGO event grant that disburses around October 2026. The overhang is tracked on-chain via the treasury balance and re-checked each build; if that balance falls further between refreshes, the additional outflow enters Sell #3 at the next refresh.

## How ADA compares to other capped proof-of-stake chains

ADA sits in an unusual middle ground: Cardano is **hard-capped like Bitcoin** but emits like a **proof-of-stake reward chain**. The cap means there is a hard ceiling and no open-ended mint, which feels like a fixed-supply token. But because most of the supply was reserved rather than pre-circulated, the protocol still releases coins every epoch — so for an inflation lens, ADA reads as mildly inflationary today, not flat. The difference from an uncapped staking chain is direction: ADA's reserve issuance only goes down, because it is a shrinking percentage of a shrinking reserve, where an uncapped chain can hold a flat or even rising emission.

What sets Cardano apart from most reward chains is the second source of float: a large, governed **on-chain treasury** that is now actively spending. Many proof-of-stake networks let treasury or foundation reserves sit idle; Cardano's Voltaire budget process has turned it into a live outflow, so the float grows from both reserve emission and treasury deployment at once. And unlike chains that pair issuance with a fee burn — where busy periods can flip them net-deflationary — Cardano has **no burn brake**: fees recycle instead of burning, so every coin the reserve or treasury releases lands as net new float.

## What to watch in the next 90 days

Watch the on-chain treasury balance — with the 2026 budget disbursing, its month-to-month decline is now the swing factor in ADA's sell pressure, and it feeds Sell #3 directly. Watch the Intersect governance queue for further large treasury-withdrawal proposals clearing the 67% approval bar, and watch the **350M-ADA Net Change Limit** (running through Jul 3 2027) that caps how fast the treasury can drain. Watch the reserve release rate — at 0.3% of the remaining reserve per epoch, it only eases from here. And note there is still no burn or buyback proposal in play for Cardano; for an inflation read, that absence is what keeps ADA net positive rather than flat.

## Summary

ADA is a hard-capped proof-of-stake token that still adds supply on two fronts: a fixed reserve that drips about 185M ADA over 90 days, and an on-chain treasury now spending down roughly 141M as its 2026 budget disburses. Nothing on the network burns ADA back out, leaving the framework at about +0.87% net — and our supply monitor reads +0.88% realized, effectively the same number. ADA stays mildly inflationary, with both flows gently easing as the Cardano reserve shrinks toward the 45 billion cap and the treasury drain runs into its net-change limit.

---

*MrNasdog Pressure Framework analysis of Cardano (ADA), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 14 2026.*

---
title:         "ADA Inflation Analysis · July 2026 · A capped coin that still drips supply"
description:   "Cardano releases ~380M ADA/90d from a fixed reserve into staking and treasury, with no burn. Framework reads +1.0% net (monitor +1.03% — they agree)."
canonical_url: "https://mrnasdog.com/research/ada/inflation"
tags:          ["crypto", "ada", "cardano", "inflation"]
published:     true
---

*Originally published at [mrnasdog.com/research/ada/inflation](https://mrnasdog.com/research/ada/inflation)*

**TL;DR.** Cardano releases about **380M ADA** over 90 days from a fixed reserve into staking rewards and the treasury, while nothing on the network burns ADA back out. So the framework reads about **+1.0%** net — and our supply monitor agrees, at **+1.03%**. The reserve drip is the whole story, and it slowly fades as the reserve shrinks toward the 45 billion cap.

## The verdict, in one paragraph

For the 90-day window ending Jul 6 2026, the MrNasdog Pressure Framework reads **ADA at +1.02% net** on the last-90-day view and **+1.01%** forward, driven entirely by reserve-funded staking and treasury emission with no offsetting burn. Our supply monitor reads the realized last-90-day change at **+1.03%** (about **380M ADA** of new supply), within **0.01 percentage points** of the framework, so there is **no monitor-gap chip**. Cardano has a **45 billion hard cap** and is not minted above it — but it is far from fully circulating, so the protocol keeps moving coins out of reserve every epoch. ADA is therefore **mildly, structurally inflationary**: supply is growing, and it is projected to keep growing at a low-single-digit pace that gently declines over time.

## Sell pressure: where new ADA comes from

Sell #1 — protocol inflation — is the entire story, at about **380M ADA** over the next 90 days. This needs a careful read, because ADA is capped at 45 billion and no new coins are minted above that ceiling. Instead, new circulating supply is **released from a fixed reserve** that was set aside at genesis. Every 5-day epoch, the Cardano protocol moves **0.3%** of whatever remains in the reserve into a reward pot. That pot is then split: **20%** goes to the treasury and the rest is paid out as staking rewards, and both shares leave the reserve into counted supply. About 18 epochs fall in a 90-day window, and the reserve currently holds roughly **7.5 billion ADA** — the gap between the ~37.3 billion already counted and the 45 billion cap — so the window releases around 380M ADA of new float.

Because the release is a fixed share of a shrinking reserve, the rate is **disinflationary** by design: each year the reserve is smaller, so each year the drip is smaller too. The Cardano reserve has a half-life of roughly four to five years. Sell #2 — vesting unlocks — is **zero**: the 2017 public sale, the founding organisations and the Cardano Foundation finished distributing their allocations years ago, so no cliff hits the market. Sell #3 — Foundation and unscheduled unlocks — is also zero as a flow; treasury spending now runs through Voltaire-era community governance, and a **June 2026** proposal to fund the Cardano Summit fell short of the two-thirds threshold a treasury withdrawal needs and never executed. Sell #4 — long-term locked or bankruptcy — is zero, with no estate or court distribution in play for ADA.

## Buy pressure: where new ADA goes

This is the short half of the ledger: **nothing**. Buy #1 — programmatic buyback — is zero, because Cardano runs no buyback program; neither the protocol nor the treasury buys ADA on the open market. Buy #2 — protocol fee burn — is also zero, and this is the detail people most often get wrong about Cardano. Cardano does **not burn transaction fees**. Fees are collected into a pot and recycled to stakers and the treasury, so they circulate rather than disappear. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero, with no discretionary open-market buying or new escrow announced in the window, and staking on Cardano is non-locking, so delegated ADA stays liquid. With no burn and no buyback anywhere on the network, there is no force pulling supply back, so the reserve drip lands net positive.

## Foundation and overhang

ADA has no classic unlock overhang — the early Cardano allocations are fully distributed. The one pool worth naming is the **on-chain treasury**, which receives 20% of every epoch's reward pot and now holds on the order of **1.7 billion ADA**. That treasury is not a stockpile waiting to dump: it can only be spent through community governance votes, each proposal ratified by delegate representatives and bounded by a Net Change Limit proposed at **350M ADA** for the cycle. Critically, treasury ADA is already counted supply — spending it is a reclassification, not new issuance. Two live examples this window: a **7.8M ADA** Summit budget vote that failed the 66.67% threshold, and an approved **3.3M ADA** EMURGO event grant that moves existing treasury ADA. The framework books no discretionary treasury outflow beyond the reserve emission already counted in Sell #1, and re-checks the governance queue on a roughly bi-weekly walk; if an approved proposal pushes a large ADA sum to market, that outflow would enter Sell #3 at the next refresh.

## How ADA compares to other capped proof-of-stake chains

ADA sits in an unusual middle ground: Cardano is **hard-capped like Bitcoin** but emits like a **proof-of-stake reward chain**. The cap means there is a hard ceiling and no open-ended mint, which feels like a fixed-supply token. But because most of the supply was reserved rather than pre-circulated, the protocol still releases coins every epoch — so for an inflation lens, ADA reads as mildly inflationary today, not flat. The key difference from an uncapped staking chain is direction: ADA's issuance only goes down, because it is a shrinking percentage of a shrinking reserve, where an uncapped chain can hold a flat or even rising emission.

The contrast worth drawing is with chains that pair issuance with a fee burn. Some proof-of-stake networks burn enough base fees to offset or even reverse their staking emission, which can flip them net-deflationary in busy periods. Cardano has no such brake — fees recycle instead of burning — so every coin the reserve releases lands as net new float. That makes ADA cleaner to read than a burn-and-mint chain: there is one force, the reserve drip, and it is always positive and always slowly fading.

## What to watch in the next 90 days

Watch the reserve release rate — at 0.3% of the remaining reserve per epoch, the single number that matters is how fast the reserve depletes, and it only eases from here. Watch the treasury governance queue at Intersect: an approved, large ADA proposal that actually pushes coins to market would be the one thing that lifts sell pressure beyond the reserve drip, and it would enter Sell #3. The 2026 Net Change Limit, proposed at 350M ADA, caps how much treasury ADA can leave in the cycle. Watch staking participation, since the more ADA is staked and re-staked, the slower fresh rewards reach the open float. And note that there is still no burn or buyback proposal in play for Cardano — for an inflation read, that absence is what keeps ADA mildly positive rather than flat.

## Summary

ADA is a hard-capped proof-of-stake token that still drips new supply from a fixed reserve. Cardano releases about 380M ADA over 90 days into staking rewards and the treasury, while nothing on the network burns ADA back out, leaving the framework at about +1.0% net. Our supply monitor reads +1.03% realized — effectively the same number, because the reserve drip is exactly what it measures, so there is no monitor gap. ADA stays mildly inflationary, with issuance gently fading year over year as the Cardano reserve shrinks toward the 45 billion cap.

---

*MrNasdog Pressure Framework analysis of Cardano (ADA), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 6 2026.*

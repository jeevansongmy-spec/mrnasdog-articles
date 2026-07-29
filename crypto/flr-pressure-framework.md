---
title: "FLR Inflation Analysis · July 2026 · Supply growing, but FIP.16 cuts the pace nearly in half"
description: "A MrNasdog Pressure Framework read of Flare (FLR): protocol inflation ~1.07B/90D, now cut to 3% (~640M forward) vs a new base-fee burn (~74M). Framework +0.65% net; monitor +1.20% last-90d."
canonical_url: "https://mrnasdog.com/research/flr/inflation"
tags: ["crypto", "flr", "flare", "oracles"]
published: true
---

> Originally published at **[mrnasdog.com/research/flr/inflation](https://mrnasdog.com/research/flr/inflation)** by MrNasdog.

Flare protocol inflation minted about **1.07B FLR** over the last 90 days, a roughly 5% annual pace, but the **FIP.16** tokenomics reform has cut the rate to **3%** and switched on a raised base-fee burn, so the next 90 days project to about **640M** minted against roughly **74M** burned. The Pressure Framework reads FLR at about **+0.65% net going forward**, down from the **+1.20%** the last 90 days ran at, which matches our supply monitor almost exactly — so no monitor-gap flag is raised.

## The verdict, in one paragraph

For the 90-day window beginning July 30 2026, the MrNasdog Pressure Framework reads **FLR at about +0.65% net** on the forward view — about **640M FLR** minted by the newly reduced 3% protocol inflation against roughly **74M FLR** destroyed by the raised base-fee burn. Over the last 90 days the framework reads **+1.20%**, and our supply monitor reads the realized change at **+1.20%** too — a gap of about **0.0 percentage points**, so no monitor-gap chip. The two agree because both capture the same fact: Flare's inflation is allocated a year at a time, so realized minting stayed at the pre-committed ~5% pace right across the window even though FIP.16 passed inside it — the cut lands on the forward number, not the last one. The one-line read: **an uncapped, capped-inflation chain whose supply is still growing but whose issuance was just cut nearly in half**.

## Sell pressure: where new FLR comes from

Sell #1 — protocol inflation — is effectively the entire sell side, at about **1.07B FLR** minted over the last 90 days and about **640M** projected for the next. Flare issues new FLR on a capped yearly schedule and pays it to FLR stakers, price-feed delegators and FAssets data agents. The FIP.16 reform approved on **April 24 2026** cut the annual inflation rate from **5% to 3%** and the yearly issuance cap from 5B to 3B FLR. Because that annual allocation is committed and paid out across reward epochs, realized minting held near the old 5% pace for the whole trailing window — which is why the last 90 days minted about 1.07B — while the forward window sits fully at the lower 3% rate, hence the step down to about 640M. There is no maximum supply, so this is genuine new issuance rather than a scheduled unlock.

Every other sell row is **zero**. Sell #2 — vesting unlocks — is zero because the three-year FlareDrop distribution that had been moving previously-locked FLR into circulation, together with a multi-year 2.1B backer-token burn, both finished on schedule on **January 30 2026**, and early-backer vesting ran out over the same quarter. Sell #3 — Foundation and unscheduled unlocks — is zero: the Flare Foundation and its investment fund hold a large non-voting allocation, but no dated discretionary release fell in the window. Sell #4 — long-term locked or bankruptcy — is zero, because no estate or court-ordered distribution applies to FLR.

## Buy pressure: where new FLR goes

Buy #2 — the protocol fee burn — is the active offset, at about **25M FLR** over the last 90 days and roughly **74M** projected for the next. Flare burns the base fee on every transaction, and FIP.16 raised that base fee about **20×**, from 25 to 500 gwei, so at current activity the burn scales toward about **300M FLR** a year — up from a negligible ~7.5M before. The catch on the last-90-day number is timing: the fee-burn hard fork executed in **late June 2026**, so the higher rate ran only about five of the trailing thirteen weeks, removing about 25M; the forward window carries the full-quarter pace of roughly 74M.

The other buy rows are **zero**. Buy #1 — a programmatic buyback — is carried at zero, but it is the row to watch: FIP.16 created **FIRE**, the Flare Income Reinvestment Entity, whose mandate explicitly includes buying FLR on the open market and burning it, funded by data-connector fees, FAssets and Flare Smart Account fees, and captured MEV. FIRE is newly live with no observed on-chain buyback quantum yet, so it removes nothing from supply for now. Buy #3 — Foundation buy — is zero, with no discretionary open-market buying observed outside the burn. Buy #4 — new long-term lock — is zero: FIP.16 reweighted staking rewards to favor locking, 5× the delegation rate as of **July 20 2026**, but staking is continuous and no new dated multi-year lock or escrow was announced.

## Foundation and overhang

FLR's overhang picture got simpler in 2026. The multi-year FlareDrop that released locked FLR every month is finished, so the largest scheduled source of new float is gone. The remaining team-controlled overhang is the **Flare Foundation and Flare VC Fund** holdings — a non-voting allocation on the order of **a fifth of supply**, part of the roughly **19.3B FLR** gap between the 106.26B total supply and the 86.96B circulating — with no published release schedule. The rest of that gap is the undistributed reward reserve, which enters circulation only through the capped inflation schedule counted in Sell #1, not as a discretionary cliff. The framework books no discretionary release beyond that inflation and re-checks the schedule, the fee burn and any FIRE activity on a roughly bi-weekly walk; if a Foundation balance falls faster than the schedule, that outflow enters Sell #3 at the next refresh.

## How FLR compares to other uncapped proof-of-stake chains

FLR belongs to the class of **uncapped, capped-inflation proof-of-stake Layer-1s** — coins with no hard supply ceiling but a bounded annual issuance that shrinks the effective rate over time. Unlike a halving-model coin such as BTC with a fixed maximum, FLR has no ceiling; unlike an uncapped continuous-emission chain with no brake, its yearly mint is capped and now falling, and it pairs the mint with a fee burn that scales with network use. That last feature makes FLR a close structural cousin of post-Merge **Ethereum**: issuance to secure the chain, an EIP-1559-style base-fee burn to claw some of it back, and a net rate that moves with activity rather than sitting at a fixed number.

The contrast worth drawing is with chains that burn aggressively enough to go net-deflationary. FLR's fee burn is real and newly meaningful — on the order of a tenth of the gross mint at current activity — so it slows dilution rather than reversing it. For an inflation lens specifically, that leaves FLR mildly inflationary with a clear cooling trend: the 3% mint is the dominant force, the base-fee burn is a growing brake, and FIRE is a second brake that could tighten if its buyback-and-burn mandate ever fires. Compared with an exchange token that runs a fixed quarterly buyback, FLR's deflationary pressure is usage-driven and still emerging rather than scheduled and proven.

## What to watch in the next 90 days

Watch the **base-fee burn** as activity moves — the ~74M-per-quarter pace assumes current throughput, so a busier Flare burns more and a quiet one burns less. Watch **FIRE**: the first time it routes captured revenue or MEV into an on-chain buyback-and-burn, the published amount moves Buy #1 off zero and tightens the net rate. Watch the **3% inflation** now that it applies to the whole forward window — realized minting should step down from the ~1.07B last quarter toward ~640M as the next annual allocation reflects the lower rate. Watch the **FAssets** program, live at v1.3 since **May 14 2026**, since FAssets fees are a FIRE revenue source. And expect the framework to keep tracking close to our supply monitor now that the FlareDrop distribution has ended and the biggest one-off float source is gone.

## Summary

FLR is the native coin of Flare, an uncapped, capped-inflation data-and-oracle chain whose supply grows on a bounded yearly schedule. The FIP.16 reform cut the mint from 5% to 3% and switched on a 20× base-fee burn: realized issuance was about 1.07B FLR last quarter but projects to about 640M going forward, against roughly 74M burned, leaving the framework at about +0.65% net — down from +1.20% over the last 90 days, which our supply monitor confirms at +1.20% with essentially no gap. There is no vesting, no bankruptcy overhang and no proven buyback yet; the key risk-and-opportunity is FIRE, whose open-market buyback-and-burn mandate is live but unfired. With the three-year FlareDrop finished, FLR stays mildly inflationary but on a clearly cooling path — the smaller mint leading, the fee burn slowing it.

---

*MrNasdog Pressure Framework analysis of Flare (FLR), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 30 2026.*

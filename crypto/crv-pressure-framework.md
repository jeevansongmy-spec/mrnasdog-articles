---
title: "CRV Inflation Analysis · July 2026 · Supply growing, projected to keep growing"
description: "A MrNasdog Pressure Framework read of Curve DAO (CRV): ~28.5M / 90D of decaying gauge emission with no buyback and no burn. Framework +1.86% net; monitor +2.48%, gap +0.62pp."
canonical_url: "https://mrnasdog.com/research/crv/inflation"
tags: ["crypto", "crv", "curve", "defi"]
published: true
---

> Originally published at **[mrnasdog.com/research/crv/inflation](https://mrnasdog.com/research/crv/inflation)** by MrNasdog.

Curve mints about **28.5M CRV** over 90 days to liquidity gauges on a fixed schedule that decays about 16% a year, while the buy side is **zero** — no buyback, no burn. The framework reads about **+1.86%** net; our supply monitor reads **+2.48%**, a **+0.62pp** gap that trips a warning chip because already-allocated gauge CRV is being reclassified into the circulating count faster than the mint alone. CRV is **structurally inflationary on a hard cap** of **3.03B**, with the pace easing as the mint steps down.

## The verdict, in one paragraph

For the 90-day window, the MrNasdog Pressure Framework reads **CRV at about +1.86% net** on the trailing view and about **+1.66%** on the forward view, driven entirely by Curve's gauge emission with no offsetting buy pressure. Our supply monitor reads the realized last-90-day circulating change at **+2.48%**, versus the framework's **+1.86%** on-chain mint for the same window — a gap of about **0.62 percentage points**, just over tolerance, so this build ships a **monitor-gap chip**. The residual is not a data error: the on-chain mint is deterministic at a fixed rate, and the monitor's circulating base grew faster because already-allocated gauge CRV is being claimed and reclassified from non-circulating to circulating — not new issuance beyond the fixed schedule. Both readings agree on direction. CRV is **structurally inflationary on a hard cap**: supply grows, but only from a fixed, decaying mint, and there is no burn to reverse it.

## Sell pressure: where new CRV comes from

Sell #1 — protocol inflation — is the entire story, at about **28.5M CRV** over the last 90 days. Curve mints new CRV every second and routes it to liquidity providers through its gauge system, on a fixed, permissionless schedule that steps down each year. On-chain the CRV token contract runs at a constant **3.66 CRV a second**, or about **316,600 CRV a day** — roughly **115.5M CRV a year** in the current mining epoch, which began on **Aug 12 2025**. The next step-down lands on **Aug 12 2026**, inside the coming window, which pulls the forward 90-day mint down to about **25.4M CRV** as the rate drops another ~16%.

Sell #2 — vesting unlocks — is **zero**: every original team, investor, employee and early-liquidity allocation finished vesting on **Aug 12 2024**, so CRV is fully unlocked and no cliff hits the market. All new supply now comes only from the gauge emission. Sell #3 — Foundation and unscheduled unlocks — is also zero as a flow; the DAO's governance-controlled community reserve, about **151M CRV** or 5% of the max supply, has no published 90-day release rate and showed no distribution event this window. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate or court distribution applies to CRV.

## Buy pressure: where new CRV goes

The buy side is the unusual part of CRV: it is **completely empty**. Buy #1 — programmatic buyback — is **zero**, because Curve runs no CRV buyback; protocol fees are paid to vote-locked holders in the crvUSD stablecoin rather than used to repurchase CRV on the open market. Buy #2 — protocol fee burn — is **zero**: Curve does not burn CRV, building value through fee-sharing with lockers instead of scarcity. Buy #3 — Foundation buy — is zero, with no discretionary open-market buying by the project or DAO. Buy #4 — new long-term lock — is also zero: vote-escrow locking does remove CRV from the active float, and about **45%** of circulating CRV is vote-locked, but locked CRV is still circulating supply and the locking is voluntary and roughly steady, so no fixed quantum is booked. With nothing on the buy side, the gross mint is the net mint.

## Foundation and overhang

CRV has no classic unlock overhang — the token is fully distributed and all founder, investor and employee vesting ended in **Aug 2024**. What remains is one DAO-controlled structure worth tracking: the **community reserve**, about **151M CRV** or 5% of the hard cap, held under governance control with no published 90-day release rate. It is watched but not booked as a flow, because there was no observed distribution event in the window. The framework re-checks the on-chain emission rate and this reserve on a roughly bi-weekly walk; if the community reserve's balance falls between refreshes, that outflow enters Sell #3 at the next refresh.

## How CRV compares to other capped emission tokens

CRV belongs to the class of **hard-capped tokens with a decaying emission schedule** — structurally closer to a halving-model coin than to an uncapped proof-of-stake chain. Like Bitcoin, CRV has a fixed ceiling — **3.03B** — and a mint that steps down on a fixed calendar; unlike Bitcoin's four-year halving, CRV's cut is annual and smaller, about 16% every August. The result is a long, gentle glide toward the cap rather than sharp halving cliffs, and CRV sits at about **50.7%** of its cap today.

Where CRV diverges sharply is the buy side. Exchange tokens and many DeFi peers pair emission with a buyback-and-burn that can flip them net-deflationary; CRV pointedly does not. Its model directs fees to vote-locked holders in a stablecoin, so there is no repurchase and no burn to offset the mint. For an inflation lens specifically, that means CRV reads as steadily, mildly inflationary with no brake — the only thing slowing dilution is the decaying schedule itself, not any active removal of supply. That is the cleanest way to characterise CRV: a capped, decaying mint with an empty buy side.

## What to watch in the next 90 days

Watch **Aug 12 2026** — the programmed annual emission cut, which lowers the daily mint about 16% and is the single dated event that moves the framework read this window. Watch the DAO's community reserve for any large disbursement, since it is the one tracked overhang that could add to Sell #3. Watch the governance forum for any new proposal touching supply — a buyback, a burn, or a treasury deployment would all change the buy side, which is currently empty; the 2026 shift to a scrutiny-based fee model changes how crvUSD fees are routed, not CRV supply. And expect the framework to keep reading a little below our monitor for as long as already-allocated gauge CRV is being claimed into the circulating count — a classification catch-up, not a new unlock.

## Summary

CRV is a hard-capped governance token whose supply grows only from a fixed gauge-emission schedule that decays about 16% each August. Curve mints about 28.5M CRV over the last 90 days, easing to about 25.4M next quarter after the Aug 12 2026 step-down, while the buy side stays at zero — no buyback, no burn. That leaves the framework at about +1.86% net, a touch below our monitor's +2.48%, the +0.62pp gap explained by already-allocated gauge CRV being reclassified into circulating rather than any new issuance. CRV stays mildly inflationary with no brake but a hard 3.03B ceiling, and the pace eases as the mint decays.

---

*MrNasdog Pressure Framework analysis of Curve DAO (CRV), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 14 2026.*

---
title: "CRV Inflation Analysis · June 2026 · Capped mint, easing, with nothing to burn it back"
description: "A MrNasdog Pressure Framework read of Curve DAO (CRV): ~28.4M / 90D of decaying gauge emission with no buyback and no burn. Framework +1.9% net; monitor +2.27%, gap 0.4 points."
canonical_url: "https://mrnasdog.com/research/crv/inflation"
tags: ["crypto", "crv", "curve", "defi"]
published: true
---

> Originally published at **[mrnasdog.com/research/crv/inflation](https://mrnasdog.com/research/crv/inflation)** by MrNasdog.

Curve mints about **28.4M CRV** over 90 days to liquidity providers on a schedule that decays about 16% a year, while the buy side is **zero** — no buyback, no burn. That leaves the framework at about **+1.9%** net, and our supply monitor agrees at **+2.27%**, a gap of just **0.4 points**. CRV is structurally inflationary but capped at **3.03B**, with the pace easing as the mint decays.

## The verdict, in one paragraph

For the 90-day window ending June 30 2026, the MrNasdog Pressure Framework reads **CRV at +1.9% net** on the trailing view and about **+1.7%** on the forward view, driven entirely by gauge emission with no offsetting buy pressure. Our supply monitor reads the realized last-90-day change at **+2.27%**, versus the framework's **+1.86%** emission read for the same window — a gap of about **0.4 percentage points**, inside tolerance, so this build ships **no monitor-gap chip**. The small residual is the DAO community fund's slow multi-year grant vesting, which has no published 90-day rate and is tracked rather than booked. CRV is **structurally inflationary on a hard cap**: supply grows, but only from a fixed, decaying mint, and there is no burn to reverse it.

## Sell pressure: where new CRV comes from

Sell #1 — protocol inflation — is the entire story, at about **28.4M CRV** over the last 90 days. Curve mints new CRV every block and routes it to liquidity providers through its gauge system, on a fixed, permissionless schedule that steps down roughly **16%** each August. The current epoch (live since August 12 2025) runs at about **115.5M CRV a year**, or roughly **316K CRV a day**. The next step-down lands on **August 12 2026** — inside the coming window — which pulls the forward 90-day total down to about **26.1M CRV** as the rate drops another ~16%.

Sell #2 — vesting unlocks — is **zero**: every original team, investor, employee and early-liquidity allocation finished vesting on August 12 2024, so CRV is fully unlocked and no cliff hits the market. All new supply now comes only from the emission schedule. Sell #3 — Foundation and unscheduled unlocks — is also zero as a flow; the DAO community fund (~24M CRV) releases on multi-year grant contracts with no published 90-day rate, and the DAO treasury that takes 10% of revenue is a holding structure, not a CRV-issuing pool. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate or court distribution applies to CRV.

## Buy pressure: where new CRV goes

The buy side is the unusual part of CRV: it is **completely empty**. Buy #1 — programmatic buyback — is **zero**, because Curve runs no CRV buyback; protocol fees are paid to vote-locked holders in a stablecoin rather than used to repurchase CRV on the open market. Buy #2 — protocol fee burn — is **zero**: Curve deliberately does not burn CRV, building value through fee-sharing with lockers instead of scarcity. Buy #3 — Foundation buy — is zero, with no discretionary open-market buying by the project or DAO. Buy #4 — new long-term lock — is also zero: vote-escrow locking does remove CRV from the active float, but locked CRV is still circulating supply and the locking is voluntary and continuous, so no fixed quantum is booked. With nothing on the buy side, the gross mint is the net mint.

## Foundation and overhang

CRV has no classic unlock overhang — the token is fully distributed and all founder, investor and employee vesting ended in August 2024. What remains is two DAO-controlled structures. The first is the **community fund**, roughly **24M CRV** still to release on multi-year, linear grant contracts; it has no published 90-day rate, so it is watched but not booked as a flow, and it is the most likely source of the small residual above our emission math. The second is the **DAO treasury**, established in mid-2025, which accrues 10% of protocol revenue as a reserve rather than issuing CRV. Both are re-checked on a roughly bi-weekly walk; if either balance falls faster than expected between refreshes, the outflow enters Sell #3 at the next refresh.

## How CRV compares to other capped emission tokens

CRV belongs to the class of **hard-capped tokens with a decaying emission schedule** — structurally closer to a halving-model coin than to an uncapped proof-of-stake chain. Like Bitcoin, CRV has a fixed ceiling (**3.03B**) and a mint that steps down on a fixed calendar; unlike Bitcoin's four-year halving, CRV's cut is annual and smaller, about 16% every August. The result is a long, gentle glide toward the cap rather than sharp halving cliffs.

Where CRV diverges sharply is the buy side. Exchange tokens and many DeFi peers pair emission with a buyback-and-burn that can flip them net-deflationary; CRV pointedly does not. Its model directs fees to vote-locked holders in a stablecoin, so there is no repurchase and no burn to offset the mint. For an inflation lens specifically, that means CRV reads as steadily, mildly inflationary with no brake — the only thing slowing dilution is the decaying schedule itself, not any active removal of supply. That is the cleanest way to characterise CRV: a capped, decaying mint with an empty buy side.

## What to watch in the next 90 days

Watch **August 12 2026** — the programmed Epoch 6 emission cut, which lowers the daily mint about 16% and is the single dated event that moves the framework read this window. Watch the DAO community fund for any large grant disbursement, since its multi-year release is the one tracked overhang that could add to Sell #3. Watch the governance forum for any new proposal touching supply — a buyback, a burn, or a treasury deployment would all change the buy side, which is currently empty. And expect the framework to keep reading slightly below our supply monitor for as long as the community fund drips out faster than the gross mint alone — a small gap, not a new unlock.

## Summary

CRV is a hard-capped governance token whose supply grows only from a fixed gauge-emission schedule that decays about 16% each August. Curve mints about 28.4M CRV over the last 90 days, easing to about 26.1M next quarter after the August 12 2026 step-down, while the buy side stays at zero — no buyback, no burn. That leaves the framework at about +1.9% net, with our supply monitor close behind at +2.27%, a 0.4-point gap that ships no chip. CRV stays mildly inflationary with no brake but a hard 3.03B ceiling, and the pace eases as the mint decays.

*MrNasdog Pressure Framework analysis of Curve DAO (CRV), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 30, 2026.*

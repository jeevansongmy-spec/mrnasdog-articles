---
title: "KAIA Inflation Analysis · July 2026 · A fixed mint the burn can't catch"
description: "A MrNasdog Pressure Framework read of Kaia (KAIA): a fixed 9.6-per-block mint (~74.65M / 90D) vs a ~0.2M gas-fee burn. Framework +1.27% net; monitor +0.09%, the gap a gross-vs-float wedge."
canonical_url: "https://mrnasdog.com/research/kaia/inflation"
tags: ["crypto", "kaia", "klaytn", "layer-1"]
published: true
---

> Originally published at **[mrnasdog.com/research/kaia/inflation](https://mrnasdog.com/research/kaia/inflation)** by MrNasdog.

Kaia mints a fixed **9.6 KAIA** per block — about **74.65M KAIA** over 90 days — while an on-chain gas-fee burn removes only about **0.2M**. New supply runs far ahead of the burn, so the Pressure Framework reads about **+1.27% net**. Our supply monitor reads only **+0.09%** — a gap that comes from newly minted KAIA landing in the KEF and KIF ecosystem funds and re-staked validator rewards, which sit outside the freely-traded float.

## The verdict, in one paragraph

For the 90-day window ending July 5 2026, the MrNasdog Pressure Framework reads **KAIA at +1.27% net** on the forward view, driven by a fixed block-reward mint that dwarfs the chain's tiny gas-fee burn. Our supply monitor reads the realized circulating change at **+0.09%**, a gap of about **1.2 percentage points** that ships a **⚠ monitor-gap chip**. The gap is structural, not an error: Kaia's on-chain total supply genuinely grew **+1.18%** over the window as it minted **~74.65M KAIA**, but roughly 69M of that lands in the Kaia Ecosystem Fund (KEF), the Kaia Infrastructure Fund (KIF) and re-staked validator rewards — buckets classified outside the circulating float the monitor measures. KAIA is **structurally inflationary on total supply**, at a low-single-digit pace, even while its traded float looks flat.

## Sell pressure: where new KAIA comes from

Sell #1 — protocol inflation — is the whole story, at about **74.65M KAIA** over the next 90 days. Kaia mints a fixed **9.6 KAIA** on every block at roughly one-second block times, which on-chain minting counters confirm to the coin: the network's **totalMinted** figure rose by exactly 74,649,600 KAIA across the window. That works out to about **300M KAIA a year**, or a nominal **5.2%**. The mint is split 50% to validators and stakers, 25% to the Kaia Ecosystem Fund and 25% to the Kaia Infrastructure Fund — but all three slices are newly issued supply, so they count once, here.

Sell #2 — vesting unlocks — is **zero**: nearly all KAIA is already circulating, and the old Klaytn and Finschia merger reserves were permanently destroyed in one-time on-chain burns before this window, so no team, seed or treasury cliff hits the market. Sell #3 — Foundation and unscheduled unlocks — is also zero as a discrete flow; the ecosystem and infrastructure funds are fed continuously inside the block reward already booked in Sell #1. Sell #4 — long-term locked or bankruptcy — is zero.

## Buy pressure: where new KAIA goes

Buy #1 — programmatic buyback — is **zero**: Kaia runs no open-market buyback; supply is managed by an on-chain burn, not by purchases. Buy #2 — protocol fee burn — is the only active offset, and it is small: the network permanently burns half of each block's gas base fee, plus a smaller MEV-auction and business burn, but activity is light, so the on-chain **burntFee** counter shows only about **0.2M KAIA** removed over 90 days. A new rule from the mid-2026 GP-21 governance reform also burns any unearned validator Contribution Reward, which adds a slow deflationary trickle. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero.

## Foundation and overhang

KAIA has no classic unlock overhang — the token is essentially fully distributed. What it does have is two structural, continuous allocations inside the block reward itself: the Kaia Ecosystem Fund (KEF) and the Kaia Infrastructure Fund (KIF), each receiving a fixed 25% of every block's mint. These are not a stockpile waiting to dump on a cliff date; they accrue block by block and largely stay parked or re-staked, which is exactly why the traded float grows far slower than the gross mint. The framework books no discretionary release beyond protocol inflation and re-checks the on-chain supply counters on a roughly bi-weekly walk; if a KEF or KIF balance falls faster than the schedule, the outflow enters Sell #3 at the next refresh.

## How KAIA compares to other uncapped proof-of-stake chains

KAIA belongs to the class of **uncapped proof-of-stake L1s with a fixed per-block reward** — closer to a continuous-emission chain than to a hard-capped, halving-model coin. Unlike a fixed-supply token, KAIA has no ceiling; unlike a chain with an aggressive revenue burn, its gas-fee burn is tiny relative to the mint. The result is steady, low-single-digit growth in total supply, with the burn acting as a rounding error rather than a brake.

The sharper contrast is with exchange tokens or fee-heavy L1s that burn enough to go net-deflationary. Kaia's burn is real but modest — a fraction of a percent of the gross mint — so it barely dents dilution. What makes KAIA distinctive is the wide split between total supply and float: because half of every block reward flows into the KEF and KIF foundation funds, the coin's traded float can look almost flat even as its total supply compounds at roughly 5% a year. For an inflation lens, that means KAIA reads as steadily inflationary on the metric that matters for long-run dilution — total supply — even when a float-based monitor reads flat.

## What to watch in the next 90 days

Watch the on-chain **totalMinted** and **burntFee** counters — the fixed 9.6-per-block mint against a ~0.2M quarterly burn is the pair that sets the reading, and only a big jump in network activity would grow the burn enough to matter. Watch the GP-21 tokenomics reform, live since the May 19–Jun 2 2026 vote, as its unearned-Contribution-Reward burn ramps and its permissionless validator rollout lands later in 2026. Watch for any Kaia Governance Process vote that changes the 9.6-per-block reward, since the rate is governance-adjustable and was raised from 6.4 to 9.6 in the past. And expect the framework to keep reading well above our supply monitor for as long as new KAIA lands in the KEF and KIF funds rather than the traded float.

## Summary

KAIA is an uncapped proof-of-stake coin from the Klaytn + Finschia merger whose supply grows on a fixed 9.6-per-block reward. The chain mints about 74.65M KAIA over 90 days at a ~5.2% nominal rate, while an on-chain gas-fee burn removes only about 0.2M, leaving the framework at about +1.27% net. Our supply monitor reads +0.09% on the circulating float, with the gap explained by newly minted KAIA landing in the KEF and KIF ecosystem funds and re-staked rewards rather than reaching the market. KAIA stays mildly but persistently inflationary on total supply, with the tiny burn nowhere near enough to reverse it.

*MrNasdog Pressure Framework analysis of Kaia (KAIA), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 5, 2026.*

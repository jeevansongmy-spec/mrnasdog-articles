---
title: "APT Inflation Analysis · July 2026 · Supply growing, projected to keep growing"
description: "A MrNasdog Pressure Framework read of Aptos (APT): ~13.31M staking emission plus ~22.62M monthly vesting per 90D, no buyback. Framework +4.2% net; monitor +4.85% (0.66pp gap)."
canonical_url: "https://mrnasdog.com/research/apt/inflation"
tags: ["crypto", "apt", "aptos", "layer1"]
published: true
---

> Originally published at **[mrnasdog.com/research/apt/inflation](https://mrnasdog.com/research/apt/inflation)** by MrNasdog.

Aptos mints about **13.31M APT** of staking rewards and unlocks another **22.62M APT** of monthly vesting over the next 90 days, against a gas-fee burn of only about **0.70M APT** and no buyback. That leaves the Pressure Framework at roughly **+4.2%** net new supply forward. Our supply monitor reads the realized last-90-day change at **+4.85%**; the framework's gross on-chain read of the same trailing window is higher at **+5.51%**, a gap of about **0.66 percentage points** that ships a monitor-gap note. APT is structurally inflationary, with staking emission and the vesting calendar both pushing supply up.

## The verdict, in one paragraph

For the 90-day window ending July 13 2026, the MrNasdog Pressure Framework reads **APT at about +4.2% net** on the forward view, driven by 7% staking emission plus two monthly vesting unlocks, with almost no buy-side offset. Our supply monitor reads the realized last-90-day change at **+4.85%**, while the framework's own gross read of that trailing window — three vesting cliffs plus the staking mint, net of a small burn — is **+5.51%**, a gap of about **0.66 percentage points**, over the half-point tolerance, so a **monitor-gap chip ships**. The deep walk traced the gap to classification: the framework counts the gross staking mint and the full unlock schedule, roughly **47M APT** over the trailing 90 days, while the monitor's **+38.5M** tracks classified circulating supply, which excludes rewards accruing to the Foundation's permanently locked-and-staked 210M and to re-locked stake. The on-chain staking config confirms a live **7%** annual rate — not the widely-reported 2.6% cut, which is approved but not yet executed. APT is **structurally inflationary on both emission and unlocks**.

## Sell pressure: where new APT comes from

Sell #1 — protocol inflation — is about **13.31M APT** over the next 90 days. Aptos mints staking rewards every two-hour epoch; the on-chain staking config reports a per-epoch rate that annualizes to **7.0%** on the roughly **770.7M APT** staked, or about 53.99M APT a year. Note the widely-reported cut of the staking rate from 5.19% to **2.6%** is an approved-but-unexecuted proposal — the live per-epoch rate still yields 7%, and observed total-supply growth of about **54M APT** a year, from a 1.00B genesis in October 2022 to roughly 1.206B now, confirms it. New APT is paid to validators and delegators.

Sell #2 — vesting unlocks — adds about **22.62M APT**. Aptos releases a monthly cliff of roughly **11.31M APT** to early investors, core contributors, the community and the foundation on the 12th of each month, so two firings — August 12 and September 12 2026 — fall inside this window; the final unlock lands on October 12 2026, one day past the 90-day mark, after which the vesting flow stops. Sell #3 — Foundation and unscheduled unlocks — is **zero** as a flow: the Foundation permanently locked and staked 210M APT in the 2026 overhaul, but those coins were already non-circulating, so the lock removes float rather than adding it. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate applies to APT and staked APT carries only a 14-day unlock period.

## Buy pressure: where new APT goes

The buy side is nearly empty. Buy #1 — programmatic buyback — is **zero**: Aptos runs no buyback contract or treasury buying APT off the market, and staking rewards are paid from new emission rather than purchases. Buy #2 — protocol fee burn — is small but real at about **0.70M APT** over 90 days: the 2026 overhaul now burns **100%** of gas fees, roughly 235K APT a month recently, and the burn grows with network usage — but at today's fee levels it offsets only a small fraction of the mint and unlocks. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero; the 210M APT Foundation lock executed before this window, so it is not a new in-window offset. With the burn immaterial, nearly the full gross emission and unlock flow reaches net.

## Foundation and overhang

The headline overhang is the **210M APT** the Foundation permanently locked and staked — about 18% of circulating supply — which is now removed from the float and can never be sold or distributed, so it counts as a reduction in the overhang rather than a future seller. Beyond that, the remaining early-investor, core-contributor, community and foundation allocations are the live overhang, releasing on the monthly cliff that feeds Sell #2 through October 2026. Circulating supply is about **844.5M APT** of a roughly 1.206B minted total, so a large locked balance still exists, but most of it is on the published vesting calendar. The framework re-checks the on-chain staking config, the validator set and the unlock calendar on a roughly bi-weekly walk; if a treasury wallet or vesting contract releases faster than the published schedule, the extra outflow enters Sell #3 at the next refresh.

## How APT compares to other uncapped proof-of-stake chains

APT belongs to the class of **high-emission proof-of-stake L1s** still working through a multi-year vesting tail — closer to a young, heavily-vesting chain than to a hard-capped, halving-model coin like Bitcoin. Its 7% staking rate sits at the higher end of the class, above the low-single-digit emission of many newer L1s and above the roughly 3.8% adaptive rate of a peer like Tezos, and it stacks on top of monthly unlocks that are larger still. Unlike a chain that pairs issuance with an EIP-1559-style base-fee burn big enough to flip net-deflationary, Aptos burns only a token amount today, so the mint and unlocks flow through almost undiluted.

The contrast worth drawing is with the direction Aptos is trying to go. The 2026 tokenomics overhaul added a **2.1B** hard cap, a 100% gas-fee burn and a proposed staking cut to 2.6%, aiming to convert APT from a bootstrap-inflation token into a usage-driven, potentially deflationary one as activity scales. For now that is a forward-looking case: the cap is far above the current supply, the burn is immaterial, and the rate cut is not yet live on-chain. So for this 90-day window APT reads as clearly inflationary — the staking mint and the vesting calendar dominate, and the framework reads growth on both the trailing and forward views.

## What to watch in the next 90 days

Watch the two monthly unlocks on August 12 and September 12 2026 — each adds about 11.31M APT and together are the biggest swing factor for the reading. Watch the final vesting cliff on October 12 2026, which ends the four-year investor and core-contributor cycle; after it, the monthly unlock flow stops and APT's inflation profile drops sharply. Watch whether the approved staking cut to 2.6% is actually executed on-chain — the single change that would roughly halve Sell #1. And watch the gas-fee burn: if Aptos volume grows enough to make the burn material, Buy #2 could finally start offsetting emission in a meaningful way.

## Summary

APT is a high-emission proof-of-stake token whose near-term supply growth comes from both 7% staking inflation and a monthly vesting calendar. Over the next 90 days Aptos mints about 13.31M APT of staking rewards and unlocks roughly 22.62M more, with only a ~0.70M gas burn and no buyback to offset it, leaving the framework at about +4.2% net. Our supply monitor reads +4.85% realized over the trailing 90 days, versus the framework's gross +5.51% for that window, a 0.66-point gap traced to classified-circulating accounting, so the framework keeps its on-chain read and flags the gap. The key risk is the vesting schedule and a live 7% mint; the key relief is the October 2026 unlock cliff and the approved but not-yet-executed staking cut, both of which point to lower supply growth ahead.

*MrNasdog Pressure Framework analysis of Aptos (APT), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 13 2026.*

---
title: "SUI Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description: "SUI supply is growing: staking payouts and monthly unlocks added 53.15M SUI in 90 days, nothing burned — +1.30% net, +1.53% projected for the next 90 days."
canonical_url: "https://mrnasdog.com/research/sui/inflation"
tags: ["crypto", "sui", "layer1", "vesting"]
published: true
---

> Originally published at **[mrnasdog.com/research/sui/inflation](https://mrnasdog.com/research/sui/inflation)** by MrNasdog.

# SUI Inflation Analysis · September 2026 · Supply growing · projected to keep growing

The MrNasdog Pressure Framework reads **SUI** as a coin whose market supply is growing: **53.15M SUI** entered the float in the last 90 days and none left it, a net of **+1.30%** of the **4.10B SUI** in circulation. The flow comes from two places — staking payouts drawn from a fund set aside at launch, and unlocks on the 1st of every month — while Sui burns nothing. The next 90 days read **+1.53%**, because three monthly unlocks fall inside the window instead of two. All **10B SUI** already exist, so the growth is locked supply reaching the market, not new coins being minted.

## The verdict, in one paragraph

Over the 90 days to Sep 29 2026 the SUI float grew by **+1.30%**, and the framework projects **+1.53%** for the 90 days to Dec 28 2026. Our supply monitor, which reads the market-wide circulating count, measured **+1.29%** over its own 90 days — a gap of **0.004 percentage points**, well inside the half-point tolerance, so no warning chip is shown. The two readings agree because the circulating count for SUI is built from the project's own release plan, and our ledger walks the same plan, month by month, next to the staking payouts read on-chain. In one line: **SUI is a fixed-cap coin in a steady, scheduled release, with no burn to offset it**.

## Sell pressure: where new SUI comes from

The first and largest source is the **stake subsidy**. Sui set aside a fund at launch to top up staking rewards, and it pays out once per 24-hour epoch. In the window it paid **25.89M SUI**: 313,811 SUI a day until Jul 17 2026, then 282,430 SUI a day after a planned 10% cut. The fund's balance fell from 258.89M to 233.00M SUI over the same epochs — exactly the sum of the payouts, to the last unit. The cuts come every 90 epochs, and the next one lands on **Oct 15 2026**, taking the daily payout to 254,187 SUI. That leaves about **23.30M SUI** of staking payouts in the next 90 days.

The second source is the **vesting unlock** for early contributors, released on the 1st of each month. August 1 released 7.65M SUI and September 1 released 7.46M, for **15.12M SUI** in the window. The next three tranches are 7.19M on Oct 1, 7.08M on Nov 1 and 6.90M on Dec 1 2026 — about **21.17M SUI**. The Series A and Series B investor rounds finished their monthly releases in May 2026, which is why the total monthly unlock dropped from about 52M to about 22M SUI (staking payouts included) in June.

The third source is the **Foundation and Mysten Labs**. On the same monthly dates the Sui Foundation's community reserve receives about 4.00M SUI and the Mysten Labs treasury about 2.07M — **12.14M SUI** over August and September, and **18.21M SUI** over the next three months. These are team-held buckets on a published plan, so they count when they open, whatever the holder does next. There is no long-term lock or bankruptcy estate releasing SUI: a listed company holds about 105M SUI it bought from the Foundation under a two-year transfer limit that runs from mid-2025 into 2027, and none of it can move inside the next 90 days.

## Buy pressure: where new SUI goes

Nothing takes SUI off the market for good. The Sui Foundation does run a **daily buyback**, paid for with the interest earned on stablecoins held on the network: about **712K SUI** for about $538K over the window. But the Foundation does not burn or keep those coins. It hands them back out to apps, validators and partners, so they leave the market and return to it, and the framework books **0**. Even if every bought coin were destroyed, the buyback would cover only about two and a half days of staking payouts.

Sui has **no fee burn**. Computation fees — about 235K SUI in 90 days — are paid to stakers each epoch. Storage fees go into a storage fund that pays most of them back when data is deleted; that fund grew by only about 188K SUI in the window, and total supply stayed at exactly 10B. There is no Foundation purchase to hold coins off the market, and staking does not remove SUI from the float: about **7.01B SUI** is staked, more than the whole circulating count because locked coins can stake too, and that stake fell by about 221M SUI over the window. The buy side totals **0** in both windows.

## Foundation and overhang

About **5.90B SUI** — 59% of the 10B total — is not yet in the float, and all of it is team, Foundation or protocol controlled. About **686M SUI** is still due on the published plan between now and May 2030, released each month on the 1st: the contributor, reserve and Mysten Labs tranches plus the staking payouts. Of that, **233.0M SUI** sits in the staking fund, which pays out every day on a falling rate. The largest block, about **5.22B SUI**, has no published release date after May 2030; the project says the pace will follow how the Foundation deploys its allocation for builders and the ecosystem.

We re-read the staking fund from the chain at every rebuild, and the monthly plan and the Foundation's buyback records on a walk every two weeks. If any of these balances falls faster than the plan between refreshes, the extra outflow enters Sell #3 at the next refresh. The buyback destination holds almost nothing by design, since the coins are passed on as they are bought.

## How SUI compares to other Move-based Layer 1s

SUI and Aptos (APT) share the Move language and a similar origin, but their supply models differ at the root. **SUI has a hard cap**: all 10B coins were created at launch, and staking rewards are paid from a pre-funded pot. Aptos mints new APT for staking rewards with no fixed cap, and burns gas fees against it. So SUI's supply growth is set by a release plan that ends, while APT's depends on an open-ended reward rate minus a fee burn.

Against the larger smart-contract chains, SUI is unusual for having **no burn at all**. Ethereum and Solana both destroy part of every fee, which sets a floor under their net issuance when the network is busy. Sui instead sends computation fees to stakers and parks storage fees in a refundable fund, and it cut its gas price roughly five times in April 2026 and made supported stablecoin transfers free in May 2026. Usage therefore does little to shrink SUI's supply; the release plan decides it.

The trade-off is visibility. A capped, pre-minted coin like SUI will never be diluted past 10B, but 59% of that cap is still locked, and the pace of the largest block is left to the Foundation. That makes SUI's supply easier to forecast than an uncapped chain's over the next few months, and harder to forecast after 2030.

## What to watch in the next 90 days

**Oct 1 2026**: the monthly unlock of about 13.26M SUI — 7.19M to early contributors, 4.00M to the community reserve and 2.07M to Mysten Labs. **Oct 15 2026**: the next 10% cut to the staking payout, to 254,187 SUI a day. **Nov 1 2026** and **Dec 1 2026**: unlocks of about 13.15M and 12.97M SUI. Also on the watch line: any change to the Foundation's buyback, which today recycles coins instead of removing them, and any Foundation sale of locked SUI to treasury companies, which would move coins outside the published plan.

## Summary

SUI's float grew **+1.30%** in the last 90 days and is projected to grow **+1.53%** in the next 90, from daily staking payouts and monthly unlocks, with nothing burned and a Foundation buyback that hands its coins back out. The supply is capped at 10B and every coin already exists, so the growth is locked supply reaching the market on a published plan. The key risk is the 5.22B SUI with no published release date after May 2030; the ceiling is the 10B cap itself.

---

*MrNasdog Pressure Framework analysis of SUI, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

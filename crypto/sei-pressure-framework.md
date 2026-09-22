---
title:         "SEI Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "Supply growing: SEI reads +4.99% over 90 days. Sei minted 42.9M for stakers and team and investor unlocks released 293.3M, with no fee burn and no buyback."
canonical_url: "https://mrnasdog.com/research/sei/inflation"
tags:           ["crypto", "sei", "cosmos", "layer1"]
published:     true
---

Originally published at [SEI Inflation Analysis · September 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/sei/inflation).

# SEI Inflation Analysis · September 2026 · Supply growing · projected to keep growing

SEI supply is growing and is projected to keep growing: the MrNasdog Pressure Framework reads Sei at **+4.99%** over the last 90 days and **+4.96%** over the next 90. Two taps feed it — a staking mint paid every day that created **42.9M SEI**, and monthly team and investor unlocks that released **293.3M SEI** — while nothing is burned or bought back, so buy pressure is **0**. SEI has a hard cap of **10,000M**, but **2,489.3M SEI** already created still sits outside the counted float, and **777.3M** is yet to be minted.

## The verdict, in one paragraph

Against a circulating base of **6,733.3M SEI**, the framework books **336.2M SEI** of sell pressure and **0** of buy pressure over the trailing 90 days — a net of **+4.99%** — and **334.1M SEI**, or **+4.96%**, for the next 90 days. The inflation monitor reads **+0.11%** for the same window, a gap of **4.89 percentage points**, well over the 0.5-point tolerance, so the overview carries a monitor-gap warning. The gap has one cause: the float figure the monitor divides by has sat at **6,733.3M SEI** since **Feb 2026** and has not taken a single step since, while the Sei chain kept minting every day and the team vesting contracts kept paying every month. The monitor cannot see flows its own figure never records. The label for SEI is **a capped chain still paying out its launch allocations**: about a twentieth of the float added every quarter, with nothing taken back.

## Sell pressure: where new SEI comes from

Sell #1, protocol inflation, is **42.9M SEI**. Sei's mint module creates SEI on a fixed yearly plan and pays it to validators and stakers, with no community tax held back. The plan is set by calendar date, not by block: it paid **494,505 SEI a day** until **Aug 14 2026**, then stepped down to **453,297 SEI a day** from **Aug 15 2026**, when the yearly amount fell from 180M to 165M SEI. The forward column uses the new rate only, which is why it is lower: **40.8M SEI**. These are brand-new coins that did not exist before, so every one is new tradable supply. The Sei chain confirms it: total SEI rose from **9,212.3M** on **Aug 30 2026** to **9,222.7M** on **Sep 22 2026**, exactly 23 days of mint to the last decimal.

Sell #2, vesting unlocks, is **293.3M SEI**, and it has two parts. The first is the Sei team allocation, which does not sit in ordinary wallets: it is held in two on-chain vesting contracts that stake the locked coins and release a fixed slice on the 15th of each month — **22.2M** from one and **20M** from the other, **42.2M SEI** in all. The framework read these contracts directly rather than trusting a calendar. They paid out on **Jul 16**, **Aug 17** and **Sep 16 2026**, and each payment moved on through a project account to team wallets, so **126.7M SEI** left the lock and reached spendable hands. The second part is the private-sale investors, who receive **55.6M SEI** a month on the same calendar. Their coins are not held in any readable contract, so the published schedule stands: **166.7M SEI** over the window. Every one of these tranches came after the counted float stopped moving, so each one crosses from outside that float into it, and counts once.

Sell #3, Foundation and unscheduled unlocks, is **0**. The Sei Foundation's own vesting contract has finished and is empty, and its last payout left on **Jun 17 2026**, before this window. Sell #4, long-term locked or bankruptcy, is **0**: SEI has no bankruptcy estate, trustee or court-ordered distribution.

## Buy pressure: where new SEI goes

Nowhere. Buy #1, programmatic buyback, is **0** — Sei runs no programme that spends project money buying SEI, and none was announced in the window. Buy #2, protocol fee burn, is also **0**, and this is by design: Sei's EVM charges a base fee but does not destroy it, so gas goes to validators and stakers. The framework checked both places a burn could show. Total SEI rose by exactly the mint, so nothing was subtracted, and the two EVM dead addresses held the same **1,571 SEI** at both reads. No governance vote in the window was rejected, so no deposit was burned either.

Buy #3, Foundation buy, is **0**: the only SEI flowing into project accounts was staking income earned by the vesting contracts, which is already counted in the mint. Buy #4, new long-term lock, is **0**. About **4,162.6M SEI** is staked, but staked SEI is already treated as tradable supply, and the 21-day unbonding wait is a delay, not a lock.

## Foundation and overhang

The largest overhang on SEI is the team allocation still inside its two vesting contracts: **945.1M SEI**, all of it staked, releasing **42.2M** a month. One contract finishes on **Aug 15 2027**; the other was stretched to **Aug 15 2029**. Both are read on-chain at every rebuild. The second item is the private-sale remainder, about **611.1M SEI**, released at **55.6M** a month until Aug 2027 under an off-chain lockup that no contract shows. The third is the ecosystem reserve: its vesting contract emptied in Aug 2025, and the reserve now sits in ordinary project wallets with no public label. One tracker lists a small monthly "strategic" slice from it; no movement was seen, so it is watched rather than booked. The fourth is the **777.3M SEI** not yet minted, which enters through the mint on a falling plan to Aug 14 2033. If any of these balances falls between refreshes by more than its schedule explains, that outflow enters Sell #3 at the next refresh.

## How SEI compares to other capped proof-of-stake chains

SEI sits between two familiar shapes. Like an uncapped Cosmos chain, Sei pays stakers with newly minted coins — but unlike them, its mint is a fixed amount per day that falls each year and stops for good in 2033, so the SEI cap is a real number in the code rather than a policy. On the mint alone, Sei adds about **0.6%** of its float a quarter, which is mild for a staking chain.

The larger force is the launch calendar. Three years after launch, Sei still releases team and investor coins every month, and those unlocks are about seven times the size of the mint. That makes SEI read much more like a young token working through its vesting than like a mature capped chain such as Bitcoin, where the only new supply is a shrinking block reward. And unlike exchange-chain tokens that burn fees or buy back supply, Sei has no removal mechanism at all, so there is nothing to offset either tap.

## What to watch in the next 90 days

First, the monthly unlocks on **Oct 15**, **Nov 15** and **Dec 15 2026**, about **97.8M SEI** each across team and investors; the team contracts' payouts will be read on-chain. Second, the mint, which should run at **453,297 SEI**until Aug 14 2027. Third, Sei governance: the window's votes covered network upgrades, cross-chain transfer settings and consensus timing, none of them supply-changing, but a vote could add a burn or change the mint. Fourth, the ecosystem reserve wallets, the one pool with a spender rather than a schedule. Fifth, the float figure the monitor divides by — if it starts moving again, the monitor gap should close on its own.

## Summary

The MrNasdog Pressure Framework reads SEI at **+4.99%** over the trailing 90 days and **+4.96%** projected forward: supply growing, projected to keep growing. The mechanism is two taps and no drain — a staking mint of about 0.45M SEI a day and monthly team and investor unlocks of about 97.8M SEI, against zero burn and zero buyback. The key risk is that the unlocks run on a fixed calendar until 2027 for investors and 2029 for part of the team, with **945.1M SEI** still in the team contracts. The ceiling is the **10,000M SEI** cap, which the mint reaches only in 2033.

MrNasdog Pressure Framework analysis of SEI, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 23 2026.

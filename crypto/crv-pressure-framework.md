---
title: "CRV Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description: "CRV supply is growing: 26.4M CRV of gauge emissions and 15.4M from ended veCRV locks gave +2.64% in 90 days, +1.93% next after the Aug 2026 cut. No buyback."
canonical_url: "https://mrnasdog.com/research/crv/inflation"
tags: ["crypto", "crv", "curve", "defi"]
published: true
---

Originally published at [CRV Inflation Analysis · September 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/crv/inflation).

# CRV Inflation Analysis · September 2026 · Supply growing · projected to keep growing

The MrNasdog Pressure Framework reads Curve DAO's CRV at **+2.64%** net over the last 90 days and **+1.93%** over the next 90: gauge emissions created **26.36M CRV** and ended veCRV locks returned **15.45M CRV** to the market, while new locks took in only **1.33M CRV** and nothing was bought back or burned by the protocol. The structural mechanism is a fixed emission schedule that pays Curve liquidity providers in new CRV every second and steps down once a year, the last cut landing on **Aug 12 2026**. The cap is **3.03B CRV**, and the one lever that can slow supply growth is locking: when more CRV leaves locks than enters them, the float grows faster than emissions alone.

## The verdict, in one paragraph

Over the 90 days to Sep 29 2026, the circulating CRV supply grew by **41.39M CRV**, or **+2.64%** of the **1.57B CRV** in circulation. The inflation monitor, which reads the same classified supply, shows **+2.80%** over its own 90-day window, a gap of **0.16 percentage points** — inside the tolerance, so no data-conflict flag is raised. For the next 90 days the framework projects **+1.93%**: the lower Epoch 6 emission rate adds about **23.96M CRV**, and about **7.48M CRV** is expected to come out of ended locks. CRV is a steadily inflationary DeFi governance token whose float grows from emissions and from locks unwinding, with no buyer on the other side.

## Sell pressure: where new CRV comes from

Protocol inflation is the largest row. Curve's token contract releases CRV at a fixed rate per second to the liquidity gauges, and the CRV is minted when liquidity providers claim it. In the last 90 days **26,359,613 CRV** were minted this way. The rate is set by the contract's yearly epochs: on Aug 12 2026 Epoch 6 began and the rate fell from about **3.66 CRV a second** to about **3.08 CRV a second**, a cut of about 15.9% that brings yearly emissions to about **97.2M CRV**. Because that cut fell inside the window, the forward figure uses the new rate only: **23.96M CRV** over the next 90 days. The next cut arrives in August 2027.

Vesting unlocks are small. The founding team, investor and employee allocations finished vesting years ago. The only vesting contract still holding coins is the one for Curve's first liquidity providers, fully vested since Aug 13 2021, which holds **10.30M CRV** nobody has claimed yet. Holders claimed **926,472 CRV** from it in the window, **706,795 CRV** of that in a single claim; the forward figure counts only the steady small claims, about **0.22M CRV**.

The Foundation and unscheduled row is zero. Curve's DAO treasury and community multisig hold CRV that is already counted as circulating, so moving or spending it adds nothing new, and the community-fund escrow that sits outside circulation did not move.

The long-term lock row is the second engine. About **841M CRV** is locked in veCRV for voting power and fee income and is not counted as circulating. When a lock ends and the owner withdraws, the coins return to the float: **15,447,927 CRV** came out in 90 days. Only **1.48M CRV** of locks are due to end in the next 90 days, but **14.29M CRV** of locks have already ended and still wait to be withdrawn. At this window's pace of withdrawals from that pile, the framework expects about **7.48M CRV** to come out next. There is no bankruptcy estate.

## Buy pressure: where new CRV goes

There is no programmatic buyback. Curve's trading and lending fees are paid to veCRV holders in crvUSD, Curve's own dollar coin, and no contract or treasury uses them to buy CRV. There is no protocol fee burn either: the dead address held the same **169.86 CRV** at both ends of the window. No Foundation or DAO wallet bought CRV.

New locks are the only real buy-side row. Holders locked or topped up **1,327,218 CRV** in veCRV during the window, which takes those coins out of circulation; the framework projects the same pace forward. That is less than a tenth of what came out of locks, so the locked pile shrank by **14.12M CRV**. A last small row counts coins lost for good: users sent **12,710 CRV** straight to the CRV token's own address, where nothing can move them, and burned **59.8 CRV** themselves.

## Foundation and overhang

Three balances sit outside circulation and could enter it. The largest is the veCRV lock pile, about **841M CRV**, of which **14.29M CRV** is already free to withdraw and **12.87M CRV** more is scheduled to unlock over the next 12 months; the lock contract is read on-chain at every rebuild. The second is the early liquidity-provider vesting contract with **10.30M CRV** fully claimable at any time. The third is the community-fund escrow with **0.85M CRV**, static all window. There is also a pool of about **10.2M CRV** of emissions already earned by gauges but not yet claimed, which counts in protocol inflation only when it is minted.

Inside circulation, the DAO treasury holds **5.73M CRV** and the community multisig **1.52M CRV**; the multisig sent **6.3M CRV** to the treasury in the window, and the treasury paid **568,181 CRV** into a one-year stream for the new crvUSD and Llamalend risk team, approved on Sep 2 2026. Those moves do not change the count. If the balance of either escrow falls between refreshes, the outflow enters the ledger at the next refresh.

## How CRV compares to other vote-escrow DeFi tokens

CRV created the vote-escrow model that many DeFi tokens copied: lock the token for up to four years, get voting power over where emissions go, and share the fees. The model's supply effect depends on two flows rather than one. Emissions always add coins; locks remove them only while more CRV goes in than comes out. In this window the lock pile was a net seller, so CRV's float grew by about **1.6 times** its emissions.

Balancer's BAL uses the same shape — a gauge emission that steps down by the same factor each year and a vote-escrow lock — so the two tokens face the same question: whether lockers keep relocking. Aerodrome's AERO differs in one important way: part of its protocol income buys AERO on the market and locks it, which gives it a buyer that CRV does not have. Curve instead pays its fees out in crvUSD, which rewards lockers but never touches the CRV supply.

Against uncapped proof-of-stake coins, CRV's emission is shrinking by design and ends at a hard cap of **3.03B CRV**, with about **2.42B CRV** created so far. The long-run risk is not the schedule but the locks: **826.5M CRV** of unexpired veCRV will all come due within four years unless its owners extend.

## What to watch in the next 90 days

First, the withdrawal pace from the **14.29M CRV** of ended locks: if holders empty it faster than this window, the forward **+1.93%** rises; if they relock, it falls. Second, the weekly lock calendar, which releases about **1.48M CRV** in total by Dec 28 2026, never more than about 0.31M in one week. Third, any Curve DAO vote touching emissions, the fee split or a buyback — none was on the vote list as of Sep 29 2026. Fourth, the early-LP vesting contract, where one large claim like the **706,795 CRV** seen this window would add a lump to the float.

## Summary

The MrNasdog Pressure Framework reads CRV as supply growing and projected to keep growing: **+2.64%** over the last 90 days and **+1.93%** over the next 90, against a monitor reading of **+2.80%**. The mechanism is Curve's fixed gauge emission, now about **97.2M CRV** a year after the Aug 12 2026 cut, plus CRV coming out of ended veCRV locks faster than new locks absorb it. The key risk is the lock pile of about 841M CRV, since nothing in the protocol buys CRV back. The ceiling is the 3.03B CRV cap, reached slowly as the emission rate keeps stepping down each August.

*MrNasdog Pressure Framework analysis of CRV, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

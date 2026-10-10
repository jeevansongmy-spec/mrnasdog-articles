---
title: "CRV Inflation Analysis · October 2026 · Supply growing · projected to keep growing"
description: "CRV supply is growing: 25.9M CRV of gauge emissions and 11.8M back from ended veCRV locks gave +2.37% in 90 days, about +1.84% next. No buyback, no burn."
canonical_url: "https://mrnasdog.com/research/crv/inflation"
tags: ["crypto", "crv", "curve", "defi"]
published: true
---
Originally published at [CRV Inflation Analysis · October 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/crv/inflation).

# CRV Inflation Analysis · October 2026 · Supply growing · projected to keep growing

<!-- main-page -->
The Curve DAO coin page has the score, the price drivers and every question answered — [mrnasdog.com/research/crv](https://mrnasdog.com/research/crv). Below: supply, line by line.

**CRV**, the governance and reward token of **Curve Finance**, is inflationary: over the 90 days to Oct 7 2026 the circulating supply grew by a net **+2.37%**, and the framework projects about **+1.84%** for the next 90 days. Two flows drive it: **25.90M CRV** of new gauge emissions and **11.79M CRV** coming back out of ended vote-escrow locks, against only **1.38M CRV** of new locks. Curve has no buyback and no fee burn, and the yearly emission cut on Aug 12 2026 slows the printing but does not stop it.

## The verdict, in one paragraph

Our primary read puts CRV at **+2.37%** net new circulating supply over the last 90 days: **38.61M CRV** entered the float and **1.39M CRV** left it, measured on **1.57B CRV** in circulation. The inflation monitor reads **+2.67%** for the same stretch, a gap of **0.30** percentage points, inside our 0.5-point tolerance, so no warning chip is shown; most of that gap is simply that the monitor divides by the smaller supply of 90 days ago. Looking ahead, the lower emission rate and a thinner lock calendar bring the projection down to about **+1.84%**. The one-line label: **a DeFi token that still prints steadily and whose locks keep leaking back**.

## Sell pressure: where new CRV comes from

Protocol inflation is the biggest source. The CRV token releases a fixed number of coins every second to the liquidity pools that win the weekly gauge vote, and the coins are minted when liquidity providers claim them. In the window, **25.90M CRV** was minted this way; the minted total matches the change in total supply to the coin once the 63 CRV burned by hand is added back. The rate drops by the fourth root of two every August, and the sixth cut landed on Aug 12 2026, taking it from 3.66 to **3.08 CRV a second**. At the new rate the next 90 days bring about **23.96M CRV**, and the next cut is not due until Aug 2027.

Vesting unlocks are almost over for CRV. The team, investor and employee schedules from the 2020 launch ended between Aug 2022 and Aug 2024. What remains is one old pot for the earliest Curve liquidity providers: fully vested since Aug 2021, but never claimed by some of them. **917.5K CRV** left it in this window, most of it in a single claim of 706.8K, and about **10.29M CRV** is still inside. The three quarters before saw only about 21K to 29K CRV each, so the forward figure is that steady pace, about **24.3K CRV**.

Foundation and unscheduled unlocks book zero. Curve DAO grants, such as the Swiss Stake development grant voted on Apr 12 2026 and the one-year 568K CRV stream to a risk adviser that started in September, are paid from wallets that already count as circulating, so they move coins inside the float rather than adding new ones.

The long-term locked row is the second big source. About **840.6M CRV** sits in veCRV, the vote-escrow contract, and that pile is outside the float. When a lock ends and the holder withdraws, the CRV returns to the market: **11.79M CRV** came out in 90 days. The contract keeps a public calendar of when locks end. It shows just **1.81M CRV** of locks ending in the next 90 days, plus **14.02M CRV** that already ended but was never withdrawn; at this window's pace about **6.28M CRV** should come out next. There is no bankruptcy estate or trustee holding CRV.

## Buy pressure: where new CRV goes

There is no programmatic buyback. Curve pays half of its trading fees, and a share of its crvUSD lending interest, to veCRV holders every week, in crvUSD rather than in CRV, so the fee machine rewards lockers without ever buying CRV on the market.

There is no protocol fee burn either: no part of any Curve fee destroys CRV. The only coins destroyed in the window were accidents, tracked as row 5: **12.7K CRV** sent by mistake to the token's own contract address, where it can never move, and 63 CRV burned by hand, together about **12.8K CRV**. We expect none next, because accidents do not follow a schedule.

No Foundation buy happened: no DAO vote or treasury flow bought CRV in the window. The only real buyer on the supply side is the new long-term lock. Holders locked **1.38M CRV** of fresh coins into veCRV for up to four years, to earn the weekly fee payouts and to steer where emissions go. That takes the coins out of the float, and we project the same amount for the next 90 days. It is small next to the 11.79M that came out of ended locks, so the vote-escrow pile shrank by about 10.42M CRV in the window.

## Foundation and overhang

Curve has no single foundation wallet, but several team-controlled piles are worth watching. The Curve DAO treasury holds about **5.73M CRV**, filled during the window by 6.3M CRV from a team multisig, which itself still holds about **1.52M CRV**; both sit inside the float, so their spending adds nothing new. An old DAO reserve contract outside the float holds **845K CRV** and did not move. The unclaimed early-provider pot holds about **10.29M CRV**, and the vote-escrow contract holds the 840.6M CRV described above, with 14.02M of it already free to withdraw. On top of that, about 10.3M CRV has been earned by pools but not yet claimed, and it joins the float as it is minted. We read each of these balances on-chain at every rebuild; if any of them falls between refreshes, the outflow enters the Foundation and unscheduled unlocks row at the next refresh.

## How CRV compares to other vote-escrow DeFi tokens

CRV invented the vote-escrow model that many DeFi tokens later copied: lock the token for up to four years, get voting power over emissions and a share of fees. The model works as a sink while locks grow, but CRV is now in the other phase: more coins leave old locks than enter new ones, so the lock pile that once soaked up emissions is now adding to supply. Most later copies share the same shape: continuous emissions directed by gauge votes, with fees paid to lockers rather than spent on buybacks.

Against exchange tokens that route fees into buy-and-burn programmes, CRV has no mechanical buyer at all: its fees are paid out in a dollar coin, which makes locking attractive but never removes CRV from supply. Against fixed-supply governance tokens, CRV keeps a slowly falling emission schedule with a hard cap of about 3.03B CRV; 2.42B has been minted so far, so the printing still has years to run.

The mechanism that sets CRV apart is the yearly step-down: every August the emission rate falls by about 16%, so the new-coin flow shrinks on a fixed calendar instead of by governance choice. That makes the emission side easy to forecast. The lock side is the harder part, because it depends on whether holders keep re-locking.

## What to watch in the next 90 days

First, the weekly lock calendar: the biggest single week is Dec 31 2026, when about 385K CRV of locks end, and every week of withdrawals from the 14.02M already-ended pile adds to supply. Second, the size of new veCRV locks: if fee payouts rise and fresh locking picks up, the buy side could grow past its current 1.38M CRV. Third, Curve DAO votes on grants and on gauges; the vote that ended emissions for old pools, executed on Oct 6 2026, moves rewards around but does not change the total rate. Fourth, the early-provider pot: another large claim like the 706.8K CRV one in this window would lift the vesting row again.

## Summary

Curve DAO's CRV is a growing-supply token: **+2.37%** net in the last 90 days and about **+1.84%** projected next, with the monitor at **+2.67%** and no conflict flagged. The structure is steady gauge emissions, now **3.08 CRV a second** after the Aug 12 2026 cut, plus coins returning from ended veCRV locks, with no buyback and no burn to offset them. The key risk is that the 840.6M CRV lock pile keeps shrinking faster than new locks arrive. The ceiling is the hard cap of about 3.03B CRV and the fixed yearly step-down that slows emissions every August.

*MrNasdog Pressure Framework analysis of CRV, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 8 2026.*

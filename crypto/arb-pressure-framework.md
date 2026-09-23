---
title:         "ARB Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "ARB supply grew 6.30% in 90 days as team, investor and Foundation unlocks and a 230M ARB DAO grant hit the market. Next 90 days: +4.73%. See the full ledger."
canonical_url: "https://mrnasdog.com/research/arb/inflation"
tags:          ["crypto", "arb", "arbitrum", "layer-2"]
published:     true
---

Originally published at [ARB Inflation Analysis · September 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/arb/inflation).

# ARB Inflation Analysis · September 2026 · Supply growing · projected to keep growing

ARB supply is growing and is projected to keep growing, even though Arbitrum has not minted a single new ARB since launch. The Pressure Framework reads ARB at **+6.30%** over the last 90 days and **+4.73%** over the next 90, against a monitor reading of **+6.52%**. Every point of it is existing ARB moving into the market: **556.8M ARB** of sell pressure from monthly team and investor unlocks, the Arbitrum Foundation's own vest and a **230M ARB** DAO grant, set against **129.2M ARB** of unspent grant money that went back to the DAO treasury. The supply ceiling is **10,000M ARB**, and the DAO can raise it by 2% a year only by vote.

## The verdict, in one paragraph

Against a circulating base of **6,785.6M ARB**, the framework books **556.8M ARB** of sell pressure and **129.2M ARB** of buy pressure over the trailing 90 days, a net of **+6.30%**. For the next 90 days it projects **321.0M ARB** of sell pressure and nothing on the buy side, a net of **+4.73%**. The inflation monitor reads **+6.52%** for the same window, a gap of **0.21 percentage points**. That is inside the framework's 0.5-point tolerance, so the overview page carries no warning chip. The label for ARB: **a non-minting governance token whose float grows on unlock calendars and DAO votes**.

## Sell pressure: where new ARB comes from

It does not come from minting. Sell #1, protocol inflation, is **0**. The ARB token on Arbitrum One has been minted exactly once, **10,000M ARB** at launch in March 2023, and a full scan of the token's history finds no second mint. Total supply read **9,999,998,977.63** at the start of the window and **9,999,998,977.61** at the end; the only change was **0.02 ARB** that a holder burned. There is one real caveat. The token contract gives the Arbitrum DAO a right to mint up to **2%** of supply once a year, about **200M ARB**. That right has been open since **Mar 15 2024**and has never been used; the contract's next-mint date has not moved since launch. A DAO vote could use it, so this row is watched, not closed.

Sell #2, vesting unlocks, is **326.84M ARB** and comes from two schedules. The first is the team, adviser and investor calendar: one quarter of those allocations unlocked on Mar 16 2024, and the rest unlocks in 36 equal monthly tranches of about **92.65M ARB** on the 16th of each month until **Mar 16 2027**. Three tranches landed in this window, on Jul 16, Aug 16 and Sep 16 2026, for **277.94M ARB**. These coins are held with custodians rather than in a vesting contract, so the published calendar is the measure. The second is the Arbitrum Foundation's vesting wallet, which holds the Foundation's 700M ARB budget and releases it in a straight line until **Apr 17 2027**. It paid **48.90M ARB**into the Foundation's operating wallet in four monthly releases, and its balance fell by exactly that amount.

Sell #3, Foundation and unscheduled unlocks, is **230.00M ARB**. On **Jun 28 2026** the Arbitrum DAO treasury paid 230M ARB to the Arbitrum Foundation, the ARB part of the Foundation's 2027 operating budget that token holders approved in an on-chain vote closing **Jun 25 2026**. The DAO treasury sits outside the circulating count, and the Foundation's operating wallet sits inside it, so this grant is new supply reaching the market. It was the treasury's only ARB payment in the window. Sell #4, long-term locked or bankruptcy, is **0**: ARB has no bankruptcy estate, no trustee and no court-ordered distribution.

## Buy pressure: where new ARB goes

Buy #1, programmatic buyback, is **0**. The Arbitrum DAO runs no buyback. Offchain Labs, the company that builds Arbitrum, has said since Mar 2025 that it buys ARB for its own treasury, but it names no wallet and no amount, and coins held by a company already count as float, so that buying moves nothing out of the market. A bond-funded buyback idea was discussed on the governance forum and never reached a vote.

Buy #2, protocol fee burn, is **0**, and on ARB it cannot be anything else today: gas on Arbitrum is paid in ETH, not ARB, so there is no fee stream to burn. Both burn paths were still read at both ends of the window. The dead address held **1,533 ARB** on both dates, and total supply fell by just **0.02 ARB**. Buy #3, Foundation buy, is **0**: the Foundation operating wallet grew from **85.2M** to **324.1M ARB**, but every coin came from the DAO grant and the Foundation's own vest, not from the market. Buy #4, new long-term lock, is **0**; the ARB staking contract the DAO approved held **0 ARB** at both ends of the window.

The one real removal sits in Buy #5, unspent grants returned to the treasury, at **129.18M ARB**. Holders voted in June 2026 to wind down the DAO's gaming fund and take back its unused ARB. The fund returned **86.18M ARB** on **Jul 7 2026** and **43.00M ARB** on **Jul 21 2026**. Those coins had counted as circulating while the fund held them; back in the treasury, they are outside the count again. About **14.5M ARB** more was promised and has not arrived, so the framework books nothing for it going forward.

## Foundation and overhang

The overhang on ARB is large and almost all of it is readable on chain. The biggest item is the **Arbitrum DAO treasury**, at **2,556.1M ARB**, down from **2,657.0M** at the start of the window. It has no release calendar; ARB leaves it only when holders vote a payment, and in the last twelve months that happened once. The second is the **team and investor calendar**, with about **555.9M ARB** still to unlock in six tranches through Mar 16 2027. The third is the **Foundation vesting wallet**, at **105.9M ARB**, which empties by Apr 17 2027. The fourth is the **Foundation operating wallet**, at **324.1M ARB**. It already counts as float, so it adds nothing when it moves, but it has sent **10M ARB** to the same custody address every month, which is the likeliest path from Foundation spending to the market.

The treasury, the vesting wallet and the operating wallet are read from the chain at every rebuild; the calendar is checked against the published schedule. If the DAO treasury or the Foundation vesting wallet falls between refreshes by more than the schedule and the voted payments explain, that outflow enters Sell #3 at the next refresh.

## How ARB compares to other layer-2 governance tokens

ARB sits in the class of layer-2 governance tokens: tokens that do not pay for gas, have no fee burn, and carry a large DAO treasury plus a team and investor vest. The closest comparison is Optimism's OP, whose token also leaves room for governance to mint and whose treasury also pays grants into circulation. Both look the same on the supply chart: flat total supply, rising float. The difference is timing. ARB's team and investor vest ends on **Mar 16 2027**, so the steady monthly unlock has six tranches left, and after that the float grows only by DAO vote and the Foundation's last few months of vesting.

Against capped proof-of-work chains, the contrast is in where supply comes from. Bitcoin mints on every block on a fixed clock; ARB mints nothing, yet its float grew faster in this window than any halving-model chain's, because ARB's supply was created in full on day one and is released on a calendar. Against exchange tokens that buy back and burn, ARB has no removal mechanism tied to usage at all. Arbitrum earns fees and license income in ETH and stablecoins, but none of it is turned into ARB purchases. Without a vote to change that, the only thing that takes ARB out of the float is a program handing unspent money back.

## What to watch in the next 90 days

First, the three team and investor tranches on **Oct 16 2026**, **Nov 16 2026** and **Dec 16 2026**, about **92.65M ARB** each, which make up most of the **+4.73%** forecast. Second, the Foundation vesting wallet, which should release about **43.09M ARB** by **Dec 22 2026** on its straight-line schedule. Third, Arbitrum DAO votes: no ARB payment from the treasury is on the ballot today, but any new grant program paid in ARB would land in Sell #3 the day it executes. Fourth, the last **14.5M ARB** the gaming fund still owes the treasury; if it arrives, it lowers the reading. Fifth, the DAO's 2% mint right, which has sat unused since Mar 15 2024; any vote to use it would add up to about **200M ARB** at once.

## Summary

The MrNasdog Pressure Framework reads ARB at **+6.30%** over the trailing 90 days and **+4.73%** projected forward: supply growing, projected to keep growing. Arbitrum mints no new ARB; the growth comes from a team and investor calendar releasing about **92.65M ARB** a month until Mar 2027, the Foundation's vest, and DAO votes that pay ARB out of a **2,556.1M ARB** treasury. The key risk is that the treasury is far larger than anything left on the calendar, and only votes decide when it moves. The ceiling is **10,000M ARB**, and the DAO's 2% yearly mint right has never been used.

MrNasdog Pressure Framework analysis of ARB, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 23 2026.

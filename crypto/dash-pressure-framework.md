---
title:         "DASH Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description:   "Dash created 82.5K DASH in 90 days and 33.5K came back out of the Platform credit pool, against 19.8K deposited and 39 burned. Framework +0.75%, monitor +0.59%."
canonical_url: "https://mrnasdog.com/research/dash/inflation"
tags:          ["crypto", "dash", "masternode", "proofofwork"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/dash/inflation](https://mrnasdog.com/research/dash/inflation)*

# DASH Inflation Analysis · September 2026 · Supply growing, projected to keep growing

The MrNasdog Pressure Framework reads DASH at **+0.75%** over the trailing 90 days and **+0.72%** over the next 90: supply growing, projected to keep growing. Dash is a proof-of-work chain whose block reward still creates new DASH for miners, masternodes and a voted monthly treasury, and a second flow now runs beside it — DASH coming back out of the Dash Platform credit pool. Sell pressure is **115.9K DASH**, buy pressure is **19.8K DASH**, and the constraint is the block reward itself, which drops by one fourteenth every **210,240** blocks and last dropped on **Aug 16 2026**.

## The verdict, in one paragraph

Against a circulating base of **12.83M DASH**, the framework books **115.9K DASH** of sell pressure and **19.8K DASH** of buy pressure over the trailing 90 days — a net of **+0.75%**— and projects **+0.72%** for the next 90 days, slightly lower because the full window now runs at the reduced block reward. The inflation monitor reads **+0.59%** for the same window, a gap of **0.16 percentage points**, which is inside the framework's 0.5pp tolerance, so the overview ships with no monitor-gap warning. The label for DASH is a **low, shrinking-emission payment chain with a Platform bridge that leaks back into the float**: the inflation is real but small, and it steps down once a year on a clock written into the code.

## Sell pressure: where new DASH comes from

Most of it comes from the block reward. Sell #1, protocol inflation, is **82.46K DASH**. Every Dash block creates new coins: 20% go to the miner, 60% to masternodes, and 20% is held back for the treasury. Of the masternode share, 37.5% is not paid as spendable DASH at all — it goes straight into the Dash Platform credit pool, where it cannot be spent until an evonode withdraws it. So in these 90 days miners and masternodes received **61.14K DASH** they could spend, and three monthly treasury blocks paid **21.32K DASH** to the proposals that won the masternode vote. The treasury budget that nobody voted for is never created; the three treasury blocks left about **215 DASH** of budget unpaid, and those coins simply do not exist.

Two measurement details matter. First, the 12th block-reward reduction landed inside the window: the block at height 2,522,880 still paid the old reward, and from the next block on **Aug 16 2026** the reward was exactly thirteen fourteenths of it. The forward estimate therefore uses the new, lower reward for the whole next window. Second, Dash blocks did not arrive on their 2.5-minute target. The chain produced **49,334** blocks in 90 days, one every **157.6 seconds**, and because Dash pays per block rather than per unit of time, a slower chain simply creates fewer coins. The forward estimate uses that measured pace, not the target.

Sell #2, vesting unlocks, is 0: Dash launched in 2014 with no sale, no investor tranche and no team allocation, so there is no vesting schedule. Sell #3, Foundation and unscheduled unlocks, is 0, because the treasury is created only when it pays, so there is no held pool waiting to be released. Sell #4, long-term locked or bankruptcy, is 0 — no estate or court distribution is attached to DASH.

The second source is Sell #5, Platform credit withdrawals, at **33.48K DASH**. The credit pool that receives part of every masternode reward sits outside circulating supply. When evonode operators withdraw their Platform earnings as normal DASH, those coins cross back into the spendable float. **2,029** withdrawals did so in this window, and the pace rose every month — **19.15K DASH** of it arrived after **Aug 21 2026** alone.

## Buy pressure: where new DASH goes

Buy #1, programmatic buyback, is 0. Dash has never run a buyback: transaction fees go to the block finder, and the treasury pays proposals instead of buying DASH. Buy #2, protocol fee burn, is a tiny **39 DASH**. Dash burns no transaction fees; the only coins it destroys are the **1 DASH** fee paid to submit a treasury proposal, and **39** proposals were submitted in these 90 days. Buy #3, Foundation buy, is 0 — the development team is paid by the treasury and does not buy on the market.

Buy #4, new long-term lock, is 0 even though Dash locks a great deal of DASH. Running a masternode needs **1,000 DASH** of collateral and an evonode **4,000 DASH**, about **4.02M DASH** across **2,976** nodes today. That collateral stays counted as circulating, so a node opening or closing moves nothing in this reading. The real removal is Buy #5, Platform credit deposits, at **19.81K DASH**: users turned DASH into Platform credits **1,156** times to pay for usernames, apps and private transfers, and those coins left the spendable float for the credit pool. The pool grew from **26.08K** to **36.34K DASH** across the window, and the deposits, withdrawals and block-reward inflow add up to that change within a fraction of one DASH.

## Foundation and overhang

Dash has an unusually small team overhang, because its treasury is a flow, not a stock. The budget is about **6,828 DASH** per monthly cycle and is created only for passed proposals, so there is no treasury wallet whose balance could be dumped. The core development team is funded from that budget in DASH; it holds no published reserve, and none was enumerable on chain this session, so it is watched through the proposal record. Two larger items are watched every rebuild. The Platform credit pool held **36.34K DASH** at the end of the window, readable from every block, and its outflows are already booked in Sell #5. Masternode and evonode collateral of **4.02M DASH** is the biggest locked-by-choice balance on the chain, but it is already inside circulating supply. If the credit pool falls between refreshes by more than the withdrawals booked here, or if a team wallet is identified and its balance falls, that outflow enters the sell side at the next refresh.

## How DASH compares to other proof-of-work chains

DASH sits between Bitcoin and the tail-emission privacy coins. Like Bitcoin, Dash has a falling issuance clock, but where Bitcoin halves every four years, Dash trims its block reward by one fourteenth every year, so the curve is smoother and the cuts are smaller. A mid-cycle Bitcoin reads close to **+0.2%** a quarter; Dash reads more because its reward is still a larger share of its supply. Unlike tail-emission chains such as Monero, Dash's reward keeps shrinking and approaches a cap near 18.9M rather than a permanent floor.

Two things make Dash different from almost every other proof-of-work chain. First, a fixed fifth of issuance is a treasury that only exists if masternodes vote to spend it, so part of the inflation is decided each month rather than printed automatically. Second, the Dash Platform credit pool works like a bridge to a second chain: coins go in as credits and come out as DASH. Neither side is a burn. Chains that burn fees, such as Ethereum, can offset issuance with usage; Dash has no fee burn, so its only meaningful buy-side lever is people choosing to hold value on Platform.

## What to watch in the next 90 days

First, the treasury block expected around **Sep 20 2026**, which has **6,810 DASH** allocated to passing proposals, followed by two more around **Oct 21 2026** and **Nov 20 2026**. Second, the Platform credit pool: withdrawals tripled from the first month of the window to the last, and if that pace holds the sell side rises; if deposits keep climbing with Platform use, the buy side does. Third, the block pace — at **157.6 seconds** a block the fourth treasury block of the cycle lands just after this window, but a faster chain would pull it in. Fourth, governance: no proposal to change the 20/60/20 split, the treasury or the reward schedule is on the ballot. The next reward reduction is about a year away, near **Sep 2027**.

## Summary

The MrNasdog Pressure Framework reads DASH at **+0.75%** over the trailing 90 days and **+0.72%** projected forward: supply growing, projected to keep growing. The mechanism is a proof-of-work block reward split between miners, masternodes and a voted treasury, plus DASH withdrawn from the Dash Platform credit pool, against deposits into that pool and a **39 DASH** burn of proposal fees. The key risk is the Platform bridge, whose withdrawals rose every month of the window and are the one part of the sell side not fixed by code. The ceiling is the reward clock: it cuts issuance by one fourteenth every year, most recently on **Aug 16 2026**, and no vote is on the table to change it.

*MrNasdog Pressure Framework analysis of DASH, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 18 2026.*

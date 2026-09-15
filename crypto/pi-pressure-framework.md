---
title: "PI Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description: "Pi Network mints no PI, yet 399.7M of migrated mining rewards and 81.9M from Core Team and Foundation wallets reached the market in 90 days. Net +4.30%."
canonical_url: "https://mrnasdog.com/research/pi/inflation"
tags: ["crypto", "pi", "pinetwork", "layer1"]
published: true
---

> Originally published at **[mrnasdog.com/research/pi/inflation](https://mrnasdog.com/research/pi/inflation)** by MrNasdog.

# PI Inflation Analysis · September 2026 · Supply growing, projected to keep growing

Pi Network mints no new PI — all 100,000M PI were created when the chain launched — and yet the Pressure Framework reads PI at **+4.30%** over the trailing 90 days and **+4.30%** over the next 90. Supply reaches the market two measured ways, both out of wallets the Pi Core Team set up at launch: mined rewards migrating to pioneers (**399.7M PI**) and Core Team and Foundation wallets sending Pi to exchanges (**81.9M**). Buy pressure is **0**: Pi Network has no burn and no buyback, and **86% of the 100,000M** still sits in those wallets.

## The verdict, in one paragraph

Against a circulating base of **11,193M PI**, the framework books **481.6M PI** of sell pressure and **0** of buy pressure over the trailing 90 days — a net of **+4.30%** — and projects **+4.30%** for the next 90 days at the same pace. The inflation monitor reads **+3.67%** for the same window, a gap of **0.63 percentage points**, which is over the framework's 0.5pp tolerance and ships with a monitor-gap warning on the overview page. The gap is fully explained, and this time the monitor is the lower number. The circulating figure the monitor tracks is migrated mining rewards and nothing else, so it cannot see Pi leaving Core Team and Foundation wallets for exchanges (**0.73pp**); it also picks up **0.03pp** less migration on its dates and reads **0.13pp** higher because it divides by the 90-day-old supply. The label for PI is a **fully pre-minted coin being handed out from team-controlled wallets**: nothing is created, but roughly five million PI a day still reach the market.

## Sell pressure: where new PI comes from

It does not come from minting. The Pi Network ledger counts **100,000M PI** in existence at both ends of the window. Every one of them was created on **Dec 31 2020** in two transfers: 20,000M to the Pi Core Team, spread over 10,000 wallets of 2,000,001 PI each, and 80,000M to a community account that later split into a **65,000M** mining pool, a **10,000M** Foundation reserve and a **5,000M** liquidity fund. The Pi whitepaper sets that 65/10/5/20 split.

**Sell #1, protocol inflation, is 399.7M PI**, and it is Pi mining. Pioneers mine Pi in the phone app for years before they can move it. After they pass identity checks, the mining pool pays those rewards out on the main chain. On chain the path is plain: the pool sent a **500M PI** top-up to a payout wallet on **Sep 8 2026**, that wallet funds an operator in 50M steps, and the operator creates one claimable payment per pioneer. Those payments added up to **399.7M PI** inside the window. Pi Network's own supply feed moved by the same amount, to within 0.56%. Migration comes in batches, not on a calendar, and the Core Team sets the pace.

**Sell #2, vesting unlocks, is 0.** Pi Network has no investor vesting, but it has lockups: pioneers lock Pi for two weeks to three years to mine faster, and part of each migration arrives locked. Locked Pi is already counted in the **11,193M PI** circulating figure. When a lockup ends, Pi moves from locked to unlocked inside that figure, and nothing new is added. Locked Pi fell from **6,221.1M** to **6,149.6M** over the window, and that is still 0 for this row. The locked part of each new migration is counted once, in Sell #1.

**Sell #3, Foundation and unscheduled unlocks, is 81.9M PI**, and it is the row most write-ups miss. The 10,001 Core Team wallets sent Pi out on **Jul 7 2026**, **Aug 6 2026** and **Sep 3 2026**, about once a month, through small one-use wallets; **17.9M PI** of it reached exchange deposit accounts inside the window. A wallet funded only by the liquidity fund, refilled with **50M PI** on **Sep 3 2026**, sends a few thousand PI to an exchange every few minutes: **58.1M PI** in the window. A Foundation wallet sent **6.0M PI** more the same way. **Sell #4, long-term locked or bankruptcy, is 0**: PI has no bankruptcy estate and no trustee.

## Buy pressure: where new PI goes

Nowhere. **Buy #1, programmatic buyback, is 0**. The Pi Core Team runs no buyback and has publicly rejected community calls for a buy-and-burn. **Buy #2, protocol fee burn, is 0.** Pi Network has no burn address and no burn programme. The ledger's coin count did not fall. Transaction fees do leave wallets: **1.93M PI** moved into the protocol fee pool in the window, where no wallet can spend it. But the coin count did not drop, and an upgrade could release that pool, so the framework does not call it a burn. **Buy #3, Foundation buy, is 0**: no Core Team, Foundation or liquidity wallet read in the window received Pi from outside its own group. **Buy #4, new long-term lock, is 0**: locked Pi is already counted in circulating supply, so a new lock takes nothing out of it.

## Foundation and overhang

The overhang on PI is huge, and almost none of it has a published calendar. The mining pool holds **48,648.9M PI**, a second mining wallet **4,669.0M**, and the payout wallet **454.2M**. The Core Team's 10,001 wallets hold **17,775.9M PI**, down from 20,000M at launch, with **31.6M** more sitting in the small wallets their monthly releases pass through. The Foundation reserve and its sub-wallets hold **9,955.3M PI**. The liquidity fund holds **4,898.6M PI**, including **26.6M** still waiting in the wallet that feeds an exchange. Every balance was read on chain this session and is read again at each rebuild. Pi Network ties these pots to migration: the team, Foundation and liquidity shares may be released only as fast as mined Pi migrates, which puts the allowance released so far, mining included, at **17,220.2M PI**.

The trigger sentence applies to all of them: if the mining pool, the Core Team wallets, the Foundation reserve or the liquidity fund falls between refreshes by more than migration explains, that outflow enters Sell #3 at the next refresh.

## How PI compares to other pre-minted, team-distributed coins

PI belongs with coins whose whole supply was created on day one and is released by an operator. It does not fit with mined chains. A halving chain like Bitcoin mints on every block at a rate code fixes; its 90-day reading is a fraction of a percent and falls on a known date. Pi Network mines nothing on chain. Its "mining" is a payout from a pool, and the Core Team decides how fast that payout runs. On the issuance axis PI looks strict. On the release axis it is one of the least predictable coins we track.

It is closest in shape to a newly launched token working through team and investor unlocks. There are two differences. Pi Network's release has no dated cliffs, so there is no single day to watch. And the biggest holder of undistributed supply also runs the chain, the identity checks and the payout wallets. On a typical vesting token, a contract enforces the unlock dates. On Pi Network, a team decision does.

Compared with exchange tokens that run buybacks and burns, PI has neither side of that mechanism. Those tokens can read negative, because usage pays for coins to be removed. For PI to read flat, something would have to take about **481.6M PI** off the market every 90 days — about **4.3% of circulating supply** — and Pi Network has nothing built to do that today.

## What to watch in the next 90 days

First, **Protocol 27**, scheduled for mainnet on **Sep 15 2026** and brings liquidity pools and a trading venue to Pi Network: if the liquidity fund seeds those pools, its **4,898.6M PI** balance starts to move. Second, the Core Team's monthly release, seen on **Jul 7**, **Aug 6** and **Sep 3 2026**; if the pattern holds, the next ones land in early October, November and December. Third, the liquidity-fund wallet feeding an exchange, which has **26.6M PI** left at its current pace and will need another refill. Fourth, migration batches out of the mining pool, which ran at about **399.7M PI** a quarter; the payout wallet got **500M PI** on **Sep 8 2026**. Fifth, a change in how the circulating figure is defined: today it counts locked Pi, and if it ever dropped the **6,149.6M** locked, lockup expiries would start to count as new supply.

## Summary

The MrNasdog Pressure Framework reads PI at **+4.30%** over the trailing 90 days and **+4.30%** projected forward: supply growing, projected to keep growing. Pi Network mints nothing. The float grows because wallets set up by the Core Team hand out Pi that already exists: **399.7M PI** of migrated mining rewards and **81.9M** sent to exchanges from Core Team and Foundation wallets. The key risk is that the pace is a team decision, not a schedule, and more than **80,000M PI** is still undistributed. The only ceiling is the **100,000M PI** made at launch, and no burn or buyback works against the release.

---

*MrNasdog Pressure Framework analysis of PI, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 15 2026.*

---
title:         "M Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description:   "MemeCore mints 30 M every block and burns almost nothing: +1.47% net over 90 days. A 925.93M reserve payout on Aug 19 2026 went to a treasury that has not sold."
canonical_url: "https://mrnasdog.com/research/memecore/inflation"
tags:          ["crypto", "memecore", "layer1", "meme"]
published:     true
---

> Originally published at **[mrnasdog.com/research/memecore/inflation](https://mrnasdog.com/research/memecore/inflation)** by MrNasdog.

# M Inflation Analysis · September 2026 · Supply growing, projected to keep growing

M, the native coin of the MemeCore chain, grows by a fixed block reward: every MemeCore block mints **30 M**, which added **33.33M M** over the last 90 days, while the only burn — the MemeCore base fee — removed about **584 M**. The largest event of the window was not issuance: on **Aug 19 2026** a MemeCore reserve contract paid out **925.93M M** to a Nasdaq-listed treasury company, and that treasury wallet has never sent a transaction, so the MrNasdog Pressure Framework counts those coins as held, not sold. That gives MemeCore **+1.47% net** over the last 90 days and **+1.47%** over the next 90, against a supply-monitor reading of **+73.44%** — a **71.98 percentage point** gap that comes entirely from how that one transfer is counted. M supply keeps climbing toward a **10B** cap.

## The verdict, in one paragraph

For the 90-day window ending **Sep 13 2026**, the Pressure Framework reads **M at +1.47% net**: the MemeCore block reward added **33.33M M** and the base-fee burn took back about **584 M**, against a circulating supply of **2.27B M**. The independent supply monitor reads the same window at **+73.44%**. The gap is **71.98 percentage points**, far past the half-point tolerance, so M ships with a **data-conflict flag**. A full walk found the cause: the monitor's supply rose by about **962M**, which is issuance plus the **925.93M M** reserve payout almost exactly, and measured on the monitor's own base the two readings sit a fifth of a point apart. The monitor counts the payout as new float; the framework counts it as coins that changed hands inside the MemeCore circle and have not reached the market. Even if those coins were booked as sold, the next-90-day reading would not change, because the payout has no schedule to repeat. The label for M is **steadily inflationary by block reward**.

## Sell pressure: where new M comes from

Sell #1, protocol inflation, is **33.33M M**. The MemeCore client pays a flat **30 M** into the staking reward contract with every block, a rate set by the hard fork at block **2,300,000** that cut the reward from **112.5 M**. That rate was read directly on-chain at 150 random blocks inside the window and every one credited exactly 30. MemeCore produced **1,110,856** blocks at **7.00 seconds** each, right on its target, so there is no timing correction to make. The same rate carries into the next 90 days; only another hard fork can change it.

Sell #2, vesting unlocks, is **zero**. A public unlock model schedules monthly MemeCore tranches of about **56.11M M**, three of which fell inside the window. None of them happened on-chain: the contracts that hold the unissued allocations kept identical balances across those dates, and the circulating count never stepped on them. Tokens that vest on paper but never leave the contract cannot be sold, so the framework books the realised figure, not the calendar.

Sell #3, foundation and unscheduled unlocks, is also **zero**, and this is the row that decides the page. Seven MemeCore reserve contracts hold **3.14B M**, and that total matches the gap between total and circulating supply to within **0.05M**, so no locked reserve is missing from the list. Six did not move. The largest paid out **925.93M M** on **Aug 19 2026**; the coins crossed the bridge to BNB Chain, where **925,925,926 M** landed in the treasury wallet of ZeroStack, a Nasdaq-listed company, in exchange for its shares. The company's filing names the contributors as MemeCore principals, appoints one as president and bars staking the coins. That treasury wallet has never sent a single transaction. The coins changed custody; they did not reach the market. Sell #4, long-term locked or bankruptcy supply, is **zero**: no estate or trustee schedule exists.

## Buy pressure: where new M goes

Buy #2, the protocol fee burn, is about **584 M** over 90 days. MemeCore destroys the base fee on every transaction: in single-transaction blocks the sender is debited and no address is credited. The amount is tiny because the MemeCore chain runs about **14,000** transactions a day at a very low fee, so the burn offsets less than a hundredth of one percent of issuance. The dead and zero addresses did not move at all. Buy #1, programmatic buyback, is **zero**: no MemeCore contract buys M back. Buy #3, foundation buy, is **zero**: on **Jul 2 2026** the MemeCore foundation approved a treasury buyback of at least **$10M**, but withheld the wallet, the timing and the method, and no tracked reserve grew this window, so there is no dated amount to book. Buy #4, new long-term locks, is **zero**: no new MemeCore lock with a stated size appeared, and the treasury company agreed not to stake.

## Foundation and overhang

The MemeCore overhang is large and on-chain. The reserve that made the August payout still holds **724.07M M**; the other six reserve contracts hold **700M**, **650M**, **600M**, **317.32M**, **100M** and **50M M**. Together that is **3.14B M**, more than the whole circulating supply of **2.27B**, and none of it runs on a schedule the chain enforces. Inside the counted float sit the ZeroStack treasury at **925.93M M** and team-origin wallets at **244.55M** and **90M M**, all unchanged across the window. The foundation's buyback wallet has no published address. Every contract is re-read each rebuild: if any of these balances falls and the coins reach a market, the outflow enters Sell #3 at the next refresh.

## How M compares to other memecoin chains

Most memecoins are single tokens with a fixed or tail supply: an ERC-20 memecoin with no mint function cannot add supply at all, and a proof-of-work memecoin such as Dogecoin adds a fixed number of coins per block with no cap. MemeCore sits between them and behaves more like a proof-of-stake Layer 1. M has a **10B** hard cap, but only **5.41B** exists today, and the rest is minted as validator and delegator rewards at **30 M** a block — about **135M M** a year — so the float grows on a schedule rather than staying fixed.

Against fee-burning Layer 1s, the difference is the size of the burn. A busy chain can burn enough base fees to cancel much of its issuance; MemeCore burns about **584 M** a quarter against **33.33M** minted, because network fees run near **0.0001%** of M's market value a year. The bigger structural feature is the reserve: **3.14B M** held in team-side contracts is larger than the float itself, which puts MemeCore closer to a young venture-backed Layer 1 than to a fully distributed memecoin. The August payout shows how that overhang can move in one day without touching the market.

## What to watch in the next 90 days

First, the ZeroStack treasury wallet: the company says its MemeCore holding will fund ecosystem work, and any transfer out of that wallet that reaches an exchange would be the first real sale of the August coins. Second, ZeroStack's shareholder vote on the pre-funded warrants, which decides how much of the company the MemeCore principals end up owning. Third, the next modelled MemeCore unlock tranches around **Oct 2 2026**, **Nov 2 2026** and **Dec 2 2026**, about **56.11M M** each, which have not moved on-chain so far. Fourth, the foundation buyback: a published wallet or a dated purchase would turn Buy #3 from zero into a real number. Fifth, any MemeCore hard fork that changes the **30 M** block reward.

## Summary

The MrNasdog Pressure Framework reads MemeCore's M at **+1.47% net** over the trailing 90 days and **+1.47%** over the next 90, driven by a fixed **30 M** block reward with almost nothing burned against it. The August 2026 payout of **925.93M M** to a Nasdaq-listed treasury is counted as held, because the receiving wallet has never moved a coin, and that choice is the whole of the gap to the supply monitor. The key risk is the overhang: **3.14B M** in reserve contracts plus a **925.93M** corporate treasury, none of it on an enforced schedule. The ceiling is the **10B** cap, with about **4.59B M** still to be minted.

---

*MrNasdog Pressure Framework analysis of M, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 13 2026.*

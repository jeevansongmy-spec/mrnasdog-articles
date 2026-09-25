---
title:         "HYPE Inflation Analysis · September 2026 · Mixed flows, supply roughly steady"
description:   "HYPE supply is roughly steady at −0.04% over 90 days and next: a 1.98M HYPE fee buyback plus burns just outweigh 2.17M of team, staking and foundation supply."
canonical_url: "https://mrnasdog.com/research/hype/inflation"
tags:          ["crypto", "hype", "hyperliquid", "defi"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/hype/inflation](https://mrnasdog.com/research/hype/inflation)*

# HYPE Inflation Analysis · September 2026 · Mixed flows, supply roughly steady

HYPE, the coin of the Hyperliquid perpetual-futures exchange and its own chain, is in near balance: over the last 90 days **2.17M HYPE** of new supply reached the market — team vault releases, staking rewards and foundation payments — while the Hyperliquid Assistance Fund buyback and the HYPE fee burns took **2.25M HYPE** back out. The MrNasdog Pressure Framework reads that as **−0.04% net** over the last 90 days and the same over the next 90, against a supply-monitor reading of **−0.02%** — a gap of **0.02 percentage points**. HYPE sits under a fixed **1,000M** cap, but **411.29M** of it is an unissued reserve that keeps paying stakers, so the buyback has to keep running just to hold supply level.

## The verdict, in one paragraph

For the 90-day window ending **Sep 25 2026**, the Pressure Framework reads **HYPE at −0.04% net**: **2,169,905 HYPE** entered the float and **2,254,130 HYPE** left it, on a counted circulating supply of **222.45M**. The independent supply monitor reads the realised 90-day change at **−0.02%**. The gap is **0.02 percentage points**, far inside the framework's half-point tolerance, so HYPE ships with **no data-conflict flag** — with the caveat that the monitor divides by a circulating figure that has not been updated since early June, so the agreement is weaker evidence than it looks. The forward column also reads **−0.04%**: the same rows run at the same pace, and a new reserve-yield buyback due **Oct 3 2026** is not counted until it pays. The label for HYPE is **buyback-balanced**: a capped token whose fee-funded buyback now just outweighs the new coins its reserve and team vault release.

## Sell pressure: where new HYPE comes from

HYPE supply grows from three places, and the largest is the core contributors' vault. It was given **238M HYPE** at launch, and its published calendar allows roughly **9.92M HYPE** a month — about **29.75M** across this window. The vault took almost none of that. Read from its own ledger, it sent out **452,000 HYPE** on **Jul 7 2026**, **433,024** on **Aug 6** and **433,419** on **Sep 6**, each spread across about ten outside wallets. That is Sell #2, vesting unlocks, at **1.32M HYPE** — the released amount, not the scheduled one, because tokens that vest but never leave the vault are not on the market. The vault still holds **241.42M HYPE**, all staked, which is more than the whole counted float, so every coin it sends out is genuinely new supply.

Sell #1, protocol inflation, is the HYPE staking reward. Hyperliquid pays stakers out of a reserve set aside at launch and never issued, so the **1,000M** cap never moves but every reward still adds coins to the market. About **2.42M HYPE** left that reserve over the window, a pace checked three ways — the reserve read at several dates, the published reward curve, and two live readings minutes apart. Most of it went to the team vault, the Hyper Foundation and the grants wallet, which are outside the float and are counted only when they send coins out, leaving **0.75M HYPE** paid to ordinary stakers. The rate eases as more HYPE is staked. Sell #3, foundation and unscheduled unlocks, is **0.10M HYPE**: the Hyper Foundation sent **50,000** on **Aug 4** and **50,000** on **Aug 31 2026**, and the community grants wallet made small payments of **3,501**. Sell #4, long-term locked or bankruptcy supply, is **zero**: no estate or trustee holds HYPE, and the listed companies and funds that hold it bought on the open market.

## Buy pressure: where new HYPE goes

Buy #1, the programmatic buyback, is the Hyperliquid Assistance Fund, and it is the biggest line on the page. Most Hyperliquid trading fees flow to it automatically, and it buys HYPE on the open market around the clock, holding the coins at a system address that has never had a private key. Its balance rose from **45.50M** to **47.48M HYPE** — **1.98M HYPE** bought in 90 days, with not a single coin sent out. The count was checked against the fund's own trade log, where every buy since early September adds up to the balance change exactly, and against an outside read of the fees it received. The headline that nearly all fees go to the buyback is the gross figure; measured, about **78%** of fees reached it over the last 30 days. Validators voted in **Dec 2025**, with **85%** support, to treat this balance as burned, so the HYPE it buys leaves the float for good unless the chain's own code is changed.

Buy #2, the protocol fee burn, runs on two separate surfaces. On the trading layer, HYPE paid for faster order handling, for launching new markets and on some spot trades is destroyed, and HYPE total supply fell by **236,756** across the window. On HyperEVM, the smart-contract side, gas is burned as well — **35,350 HYPE**. Paired readings seconds apart showed one moving while the other stood still, so they are two burns, not one seen twice, and together they come to **0.27M HYPE**. Buy #3, foundation buying, is **zero**: the foundation only sent coins out. Buy #4, new long-term locks, is **zero**: launching a market or a stablecoin needs a **500,000 HYPE** bond, but that bond sits in ordinary staking, which is already counted as circulating. A fifth row, the reserve-yield buyback, is held at **zero** until it first pays.

## Foundation and overhang

HYPE carries the largest overhang of any line on the page, and it is almost all in two places. The first is the unissued reserve of **411.29M HYPE**, which drains at about **27,000 HYPE** a day into staking. The second is the core contributors' vault at **241.42M HYPE**: its calendar lets it release close to **10M HYPE** a month, and for the last three months it has used under a twentieth of that. The Hyper Foundation holds **60.49M HYPE**, almost all staked, with **50,000** already unstaked and waiting; the community grants wallet holds **2.97M**, with **106,500** unstaked; and the foundation's own validators have kept about **0.37M** of commission. The Assistance Fund's **47.48M HYPE** is tracked too, though validators have voted never to release it. Every one of these balances is read from the chain on each refresh. If any of them falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How HYPE compares to other exchange and perpetual-futures tokens

HYPE sits between two familiar designs. Like an uncapped proof-of-stake Layer 1, it pays stakers with new coins, and on its own that would make supply grow every year. Unlike most of them, the exchange underneath earns enough to fight back: Hyperliquid collected about **$76M** of fees over the last 30 days, a pace near **$930M** a year against a market value of about **$20.5B** — roughly **4.5%** a year. BNB Chain, one of the busiest fee-burning chains, collects fees near **0.2%** of its value a year, and a typical proof-of-stake chain collects far less than that while its issuance runs on. HYPE also differs from fixed-cap proof-of-work coins, whose supply only rises toward the cap: HYPE's cap is fixed too, but the buyback can pull the float down.

Against exchange tokens that burn from a reserve, the difference is funding. A reserve burn destroys coins the project already held, with no bid on the order book. The HYPE buyback is paid in cash from trading fees and buys in the open market, so it supports price as it removes supply — the float shrinks only when trading is busy enough. And against perpetual-exchange tokens that route fees to a treasury, the Assistance Fund is the rarer case: its coins cannot be spent, so they never become a future overhang. The trade-off is plain — HYPE's supply balance depends on trading volume and the HYPE price, both of which move.

## What to watch in the next 90 days

First, **Oct 3 2026**: the first payment of the new reserve-yield buyback, in which about **90%** of the yield on the USDC reserves used on Hyperliquid is sent to the Assistance Fund every 30 days; once it lands on-chain its size becomes known and it will be counted. Second, the team vault releases due **Oct 6**, **Nov 6** and **Dec 6 2026**: booked at about **0.44M HYPE** each, as they have run, against a calendar of **9.92M** each — a vault that took its full calendar even once would flip the reading to clearly inflationary. Third, the **50,000** the foundation and the **106,500** the grants wallet have already unstaked, which would enter Sell #3 when they are sent out. Fourth, the pace of trading fees, since a quieter quarter or a higher HYPE price means the buyback removes fewer coins.

## Summary

The MrNasdog Pressure Framework reads HYPE at **−0.04% net** over the trailing 90 days and **−0.04%** over the next 90: **2.17M HYPE** of new supply from the team vault, staking and the foundation, against **2.25M HYPE** taken out by the fee-funded Assistance Fund buyback and the HYPE fee burns. The structural mechanism is a capped token with an unissued staking reserve, balanced by a buyback that trading fees fund with about **$59M** a month. The key risk is the core contributors' vault, which is allowed to release more than twenty times what it has been taking each month. The ceiling is the **1,000M HYPE** cap, which cannot rise; whether supply grows or shrinks beneath it depends on the buyback keeping pace with the reserve and the vault.

---

*MrNasdog Pressure Framework analysis of HYPE, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 25 2026.*

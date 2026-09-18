---
title:         "LAB Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description:   "Supply growing: LAB cannot be minted, yet 151.27M LAB left team wallets in 90 days, +19.50% net, with monthly unlocks due Oct 14, Nov 14 and Dec 14 2026."
canonical_url: "https://mrnasdog.com/research/lab/inflation"
tags:          ["crypto", "lab", "labterminal", "tokenomics"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/lab/inflation](https://mrnasdog.com/research/lab/inflation)*

# LAB Inflation Analysis · September 2026 · Supply growing, projected to keep growing

LAB, the token of the LAB Terminal multi-chain trading app on BNB Chain, cannot be minted — the LAB contract carries no mint path — so every new LAB in the market comes out of LAB Terminal team wallets. Over the 90 days to **Sep 18 2026**, **151.27M LAB** left team control against about **204 LAB** destroyed from the float, so the MrNasdog Pressure Framework reads LAB at **+19.50% net**, and **+19.82%** for the next 90 days as LAB vesting contracts release on **Oct 14**, **Nov 14** and **Dec 14 2026**. The supply monitor reads **+147.39%** — a **127.89-point** gap, because the counted LAB float jumped on **Aug 13 2026** while **341.73M** of those coins still sit in team wallets and locks. LAB total supply is **989,999,803** and can only fall.

## The verdict, in one paragraph

For the 90-day window ending **Sep 18 2026**, the Pressure Framework reads **LAB at +19.50% net** against a circulating base of **775.54M LAB**: **151.27M LAB** reached wallets outside the team, and the buy side removed almost nothing. The supply monitor reads the same 90 days at **+147.39%**, a gap of **127.89 percentage points**, far past the half-point tolerance, so LAB ships with a **data-conflict flag**. The flag is explained rather than unresolved: the monitor divides a classifier step of **462.18M** by the old, smaller float, and that step counts coins as circulating that the chain shows are still held by the team. The forward column reads **+19.82%**. The label for LAB is **a monthly team-unlock token**: no issuance, no working burn, and a float that grows every month on the 14th.

## Sell pressure: where new LAB comes from

Sell #1, protocol inflation, is **zero** and stays zero. The LAB contract on BNB Smart Chain was read byte by byte: it exposes the standard transfer functions plus burn, with no mint, no owner and no upgrade path, and the only change LAB total supply has ever made is a fall from **1,000,000,000** to **989,999,803**. LAB Terminal cannot print a new LAB.

Sell #2, vesting unlocks, is **107.02M LAB**, and it is measured off the wallets, not the calendar. At the window open, five LAB Terminal team multisigs held **687.46M LAB** — exactly the part of LAB supply the counted float left out. Three of them emptied on **Jul 28** and **Jul 29 2026**, but that LAB did not go to market: it went to one team wallet that funded LAB vesting contracts and LAB claim lockers, and it is the admin of those contracts. From there, **86.04M LAB** was claimed by outside wallets and a second team multisig paid **20.98M LAB** in two monthly batches. The releases bunch on the 14th: **54.23M LAB** on **Aug 13–14** and **49.66M LAB** on **Sep 13–14**. Sell #3, foundation and unscheduled unlocks, is **44.25M LAB**: the same team wallet also paid LAB directly to outside wallets in uneven amounts, including **13.04M LAB** on **Sep 7 2026**. Sell #4, long-term locked or bankruptcy supply, is **zero**: no estate or court-run distribution holds LAB. Every team balance in this analysis was read at both window ends, and the team group closes to the unit: **687.46M** in, **526.19M** still held, the difference fully explained by coins that left.

## Buy pressure: where new LAB goes

Almost nowhere. The headline event is the LAB burn of **10M LAB** on **Jul 9 2026**, which cut LAB total supply for real. But those LAB came from a team multisig that had held the same coins since launch and has never received a single LAB since, so the burn destroyed coins that were never in the float and removed **zero** from circulation. Ordinary wallets burned about **204 LAB**, which is the whole Buy #5 row. Buy #1, the programmatic buyback, is booked at **zero**: LAB Terminal reports buying about **3.1M LAB** this window from trading fees, and it lists the **10M LAB** burn as a purchase too, but no matching buy or holding wallet could be found on chain, no bought LAB was destroyed, and the destination is not disclosed. Buy #2, a fee burn, is **zero** because LAB is a token, not a chain, and the app's fees are paid in the coins people trade. Buy #3, foundation buying, is **zero**. Buy #4, new long-term locks, is **zero**: nothing new was locked with a stated size this window — no new lockup contract and no announced amount.

## Foundation and overhang

LAB Terminal still controls **526.19M LAB** across the team group, all readable on chain and re-read on every refresh. The largest single pieces are a team multisig at **108.00M LAB** that has not moved since launch and another at **76.46M LAB** whose only moves were the burn and a transfer to the team wallet; together they are the part the counted float still leaves out. The team wallet that runs the LAB vesting contracts holds **61.50M LAB** with no schedule. The second team multisig holds **41.97M LAB**, four more monthly batches of **10.49M**. The LAB vesting contracts and claim lockers hold the rest, including **25.46M LAB** already vested but not yet claimed. One more wallet is watched but not booked: a **133.0M LAB** holder that emptied on **Jul 13–15 2026** was already counted as circulating, so its sale moved coins between holders rather than adding supply. If any of these team balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How LAB compares to other trading-platform tokens

LAB belongs to the platform-token class: a token attached to a trading product rather than to a chain. The strongest members of that class pair a fixed or shrinking supply with a fee-funded burn that visibly takes coins off the market, so the float falls on a schedule. LAB has the fixed supply — there is no mint — but not the working burn: the only large LAB burn destroyed team coins that were never tradable, and the reported buyback cannot be traced on chain. That leaves the vesting schedule as the only force moving LAB supply, and it moves one way.

Against chain tokens, the contrast is the source of new coins. A proof-of-stake chain issues new coins to validators every block; LAB issues nothing, so LAB inflation is really distribution — coins minted at launch leaving team custody. That makes the LAB sell side lumpy rather than smooth: most of it lands on one day a month. The trading app underneath does earn real fees, about **$648K** across this window, but those fees are paid in the coins people trade, so the LAB float gains no automatic buyer from them.

## What to watch in the next 90 days

First, the monthly LAB unlocks: the LAB vesting contracts release **28.30M LAB** on **Oct 14 2026** and **28.21M LAB** each on **Nov 14** and **Dec 14 2026**, and together with the claim lockers and the multisig batches each month adds about **42.8M LAB**. Second, the team wallet at **61.50M LAB**: it paid **44.25M LAB** straight out this window on no fixed dates, and any repeat adds to Sell #3. Third, the unclaimed backlog of **25.46M LAB**, which can reach the market the day its owners claim it. Fourth, the reported buyback: if LAB Terminal publishes the wallet it buys into, or starts burning what it buys, the buy side would finally register.

## Summary

The MrNasdog Pressure Framework reads LAB at **+19.50% net** over the trailing 90 days and **+19.82%** over the next 90. LAB cannot be minted, so the whole sell side is LAB Terminal team coins leaving custody — **151.27M LAB** this window, most of it on the 14th of each month — while the buy side is close to zero because the **10M LAB** burn used coins that were never tradable. The key risk is size: the team group still holds **526.19M LAB**, more than two thirds of the counted float, with **153.75M** scheduled out by **Dec 14 2026**. The ceiling is the **989,999,803 LAB** in existence, and every LAB still in team hands is supply that has not reached the market yet.

*MrNasdog Pressure Framework analysis of LAB, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 18 2026.*

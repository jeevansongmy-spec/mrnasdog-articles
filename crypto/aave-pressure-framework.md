---
title:         "AAVE Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "AAVE supply is roughly steady at +0.12% over 90 days: no mint, 19.2K AAVE paid from one DAO reserve to stakers and grants, and a buyback paused since April."
canonical_url: "https://mrnasdog.com/research/aave/inflation"
tags:                    ["crypto", "aave", "defi", "tokenomics"]
published:     true
---

Originally published at [AAVE Inflation Analysis · September 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/aave/inflation).

# AAVE Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

AAVE supply is roughly steady: the Pressure Framework reads **+0.12%** over the last 90 days and **+0.14%** for the next 90. Aave mints no new AAVE; the only supply that reaches the market is paid out of one DAO reserve, **19.2K AAVE** of staking rewards and grant streams, while buy pressure is **0** because the AAVE buyback has been paused since Apr 19 2026. The ceiling is a fixed **16M AAVE**, and the monitor's **+1.71%** is a one-time recount, not new supply.

## The verdict, in one paragraph

Against a circulating base of **15.43M AAVE**, the framework books **19.2K AAVE** of sell pressure and **0** of buy pressure over the trailing 90 days, a net of **+0.12%**, and projects **+0.14%** for the next 90 days. The inflation monitor reads **+1.71%** for the same window, a gap of **1.58 percentage points**. That is over the framework's 0.5-point tolerance, so the overview carries a monitor-gap warning. The gap is explained: between Jul 11 and Jul 19 2026 the monitor's circulating count jumped by about **236K AAVE** in one step, while on chain the total supply stayed at 16M and the DAO buyback wallet, which holds about that amount, did not move. No release was found to match it, so the framework keeps its own reading. The label for AAVE is **a fixed-supply governance token with one slow, DAO-controlled leak**.

## Sell pressure: where new AAVE comes from

It does not come from minting. The AAVE token on Ethereum has a total supply of **16M AAVE**, and it read exactly that at both ends of the window. The number sits in writable storage rather than being hard-coded, so a mint would have shown up, and the live token code has no mint function. The token can still be upgraded by an Aave DAO vote, so the framework treats the fixed supply as checked, not permanent.

What reaches the market comes from the Aave **Ecosystem Reserve**, which held **571.1K AAVE** at the end of the window. It is the only AAVE left out of the circulating count; the 16M total minus the circulating figure equals its balance to within one coin. Every coin it pays out therefore becomes new tradable supply. Sell #1, protocol inflation, is **14.8K AAVE**: staking rewards claimed by Safety Module stakers. The reward rate is **150 AAVE a day**, read on chain at both ends, and claims ran a little above it as stakers collected older rewards. Stakers can only claim while the DAO has approved enough AAVE for the reward contract, and a top-up vote sized at about 30.6K AAVE is pending, so the framework expects about the same next quarter.

Sell #2, vesting unlocks, is **4.4K AAVE**. Three payment streams run out of the same reserve in straight lines: **75K AAVE** to Aave Labs over four years to Apr 12 2030 under the Aave Will Win framework, and **5K AAVE** a year each to LlamaRisk and TokenLogic, two DAO service providers. The streams earn about **7.1K AAVE** per 90 days; recipients drew 4.4K in the window, and the TokenLogic stream has not been drawn at all yet, so the forward figure uses the full 7.1K. Sell #3, Foundation and unscheduled unlocks, is **0**: no DAO wallet released AAVE outside these two paths. Sell #4, long-term locked or bankruptcy, is **0**: AAVE has no bankruptcy estate.

## Buy pressure: where new AAVE goes

Nowhere, this window. Buy #1, programmatic buyback, is **0**. The Aave DAO buyback was paused on Apr 19 2026, the day after a bridge exploit hit Aave markets, and no buyback ran in these 90 days. An automatic buyback, called Aavenomics 3.0, was announced in late June 2026, but it has not gone live: the Ecosystem Reserve received no AAVE at all in the window, and holders were still asking the DAO for news on Sep 20 2026. Even a restart would not count by itself. The **240.5K AAVE** bought before the pause sits in the DAO buyback wallet, which is already counted as circulating, so coins parked there remove nothing. Only AAVE sent back to the reserve or destroyed would register.

Buy #2, protocol fee burn, is **0**. AAVE has no burn, and both burn checks agree: total supply stayed at 16M and the dead address gained less than 0.04 AAVE. Buy #3, Foundation buy, is **0**: the DAO bought no AAVE on the market, and its buyback wallet held the same balance at both ends. Buy #4, new long-term lock, is **0**. Staked AAVE in the Safety Module rose from **2.16M** to **2.49M**, but staked AAVE is counted as circulating and can leave after a two-day wait, so staking removes nothing from this reading.

## Foundation and overhang

The main overhang is the Ecosystem Reserve itself, at **571.1K AAVE**, down from **590.3K** at the start of the window. About **78.1K AAVE** of it is already owed on the three payment streams, and roughly 55K AAVE of staking rewards had been earned but not yet claimed in late August. It is read on chain at every rebuild. The second item is the DAO buyback wallet, at **240.5K AAVE**, flat across the window; it is already inside the float, so a sale would reach the market without changing the supply count, which is exactly why it is watched. The DAO treasury holds a further **6.6K AAVE**, and an old claim contract holds **7.5K AAVE** that did not move. If any of these balances falls between refreshes by more than the rewards and streams explain, that outflow enters Sell #3 at the next refresh.

## How AAVE compares to other fixed-supply DeFi governance tokens

AAVE belongs to the class of DeFi governance tokens that were fully minted at launch and never mint again. That is a different shape from a proof-of-work coin like Bitcoin, which still issues on every block on a shrinking schedule, and from uncapped proof-of-stake chains that pay stakers with fresh issuance of several percent a year. AAVE pays its stakers too, but from a fixed, pre-minted reserve, so its effective issuance is set by DAO votes and ends when the reserve runs down.

Against tokens that run buyback-and-burn programmes, such as exchange tokens with quarterly burns or perpetual-exchange tokens that route fees into burns, AAVE currently has no removal at all. Its buyback, when it ran, parked coins in a DAO wallet rather than destroying them, so even at full speed it would not shrink supply unless the coins leave the circulating float. That is the main mechanism gap between AAVE and the tokens whose readings turn negative.

Against tokens with large vesting cliffs, AAVE is quiet. There are no investor or team cliffs; the only scheduled releases are small grant streams that total about 7.1K AAVE a quarter. The result is a low, smooth reading that DAO votes, not calendars, can move.

## What to watch in the next 90 days

First, the Safety Module allowance top-up: once executed, it lets stakers claim up to about **30.6K AAVE**, including part of the unclaimed backlog, which could lift Sell #1 above 150 a day for a while. Second, Aavenomics 3.0: if the automatic buyback goes live, watch where the bought AAVE goes, because only coins sent to the Ecosystem Reserve or burned would count as buy pressure. Third, any vote to change the **150 AAVE a day** staking reward rate. Fourth, the three payment streams, which run to Apr 12 2030, May 27 2027 and Jun 27 2027. Fifth, the DAO buyback wallet at **240.5K AAVE**, which has a spender and no schedule. The forward window runs to Dec 22 2026.

## Summary

The MrNasdog Pressure Framework reads AAVE at **+0.12%** over the trailing 90 days and **+0.14%** projected forward: mixed flows, supply roughly steady. Aave mints no AAVE; the only new tradable supply is **19.2K AAVE** a quarter paid out of the DAO's Ecosystem Reserve as staking rewards and grant streams, with nothing removed because the buyback has been paused since Apr 19 2026 and parks its coins inside the float. The key risk is DAO discretion: votes set the reward rate, the streams and whether the 240.5K AAVE buyback stack is ever sold. The ceiling is firm in practice: a fixed **16M AAVE**, with only 571.1K still outside the float.

MrNasdog Pressure Framework analysis of AAVE, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 23 2026.

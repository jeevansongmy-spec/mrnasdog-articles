---
title:         "AAVE Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description:   "AAVE supply is roughly steady: +0.14% over 90 days, +0.15% next. No mint, no burn; the DAO reserve paid 21.9K AAVE to stakers and grants, buyback paused."
canonical_url: "https://mrnasdog.com/research/aave/inflation"
tags:                    ["crypto", "aave", "defi", "tokenomics"]
published:     true
---

Originally published at [AAVE Inflation Analysis · October 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/aave/inflation).

# AAVE Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

AAVE supply is roughly steady: over the 90 days to Oct 2 2026, **21,897 AAVE** left the Aave DAO's Ecosystem Reserve and entered the market, and nothing was taken back out, for net growth of **+0.14%** of the **15.44M AAVE** in circulation, with about **+0.15%** expected in the next 90 days. AAVE is not minted: the 16M AAVE cap is fully issued, and every new coin on the market comes out of one DAO reserve that still holds about **565,072 AAVE**. The AAVE buyback has been paused since Apr 19 2026, and there is no burn yet.

## The verdict, in one paragraph

The MrNasdog Pressure Framework reads AAVE at **+0.14%** net supply growth over the last 90 days (**21,897 AAVE** released, **0 AAVE** removed) and **+0.15%** for the next 90 days. The inflation monitor reads **+1.69%** for the same window, a gap of **1.55 percentage points**, which is above the 0.5-point line, so a monitor-gap note ships on the coin page. Almost all of that gap is one recount: on Jul 19 2026 the circulating figure the monitor reads rose by about **236K AAVE** in a single day while no matching coins moved on-chain, which fits the DAO buyback wallet's flat **240.5K AAVE** being counted as circulating. AAVE is a fully issued governance token with a slow reserve drip and a paused buyback.

## Sell pressure: where new AAVE comes from

The first and largest source is staking pay. Aave pays AAVE stakers in the Safety Module **150 AAVE a day**, and those rewards come out of the Ecosystem Reserve rather than from new minting. Over the 90 days, stakers claimed **16,009 AAVE**: 14,689 AAVE from the main staking pool and 1,320 AAVE from older staking pools that no longer earn rewards but still held unclaimed ones. Because claims also clear a backlog of older rewards, they ran a little above the 13,500 AAVE that 150 a day adds up to. In September 2026 the Aave DAO raised the reserve's spending limit for these claims, and about 37,900 AAVE of older staking rewards remain unpaid, so the claim rate could stay above the daily emission for a while.

The second source is vesting streams from the same reserve. In April 2026 the Aave DAO approved a grant of **75,000 AAVE** to Aave Labs, the main developer, paid as a straight-line stream over four years, which is about **4,623 AAVE** every 90 days until Apr 2030. Two DAO service providers each receive **5,000 AAVE** a year in the same way. In the last 90 days the payees actually drew **5,888 AAVE**; the next 90 days count all three streams in full, about **7,089 AAVE**, even though one provider has not drawn any of its stream yet.

The other two sell rows are zero. No foundation or team wallet outside circulation released AAVE beyond the streams, and the reserve has no published plan for the rest of its balance. There is no bankruptcy estate, trustee or long lock paying out AAVE, and the old contract that swapped LEND into AAVE has been closed.

## Buy pressure: where new AAVE goes

Nothing was removed from the AAVE float in the last 90 days, so every buy row is zero. The AAVE buyback, which ran from April 2025 and bought more than 205,000 AAVE in its first ten months, was paused on Apr 19 2026 after a bridge exploit pushed bad collateral into Aave's lending markets. The DAO buyback wallet held exactly **240,502 AAVE** at both ends of the window, and the Ecosystem Reserve received nothing. Bought AAVE has so far been parked inside circulation, so even a restarted buyback only removes supply if the coins are burned or locked outside the float.

AAVE has no protocol fee burn. On Sep 29 2026 Aave's founder said a burn is being considered for the next AAVE token plan, alongside an automatic buyback announced in June 2026, but there is no vote, size or start date, and on-chain the dead addresses gained only 0.04 AAVE. No team or foundation bought AAVE into a locked wallet. Staking grew from **2.24M AAVE** to **2.49M AAVE**, but staked AAVE still counts as circulating and can leave after a short cooldown, so it takes nothing off the market.

## Foundation and overhang

The one AAVE overhang outside circulation is the Aave DAO Ecosystem Reserve, which held **565,072 AAVE** on Oct 2 2026. About 74,607 AAVE of it is already promised to the three streams; the rest, roughly 490,000 AAVE, has no release schedule and is spent only by DAO vote. Inside circulation, the DAO buyback wallet holds a flat 240,502 AAVE lent out to earn interest, the DAO treasury holds 6,591 AAVE, an old claims contract holds 7,512 AAVE, and the Aave Labs stream wallet holds 8,680 AAVE it has not sold. We read every one of these balances on-chain at each rebuild. If the reserve's balance falls faster than the staking claims and streams explain between refreshes, the extra outflow enters Sell #3 at the next refresh; and if the buyback wallet is sold, that selling shows up as market supply even though the coins were already counted.

## How AAVE compares to other DeFi governance tokens

Among DeFi governance tokens, AAVE sits at the slow end. Tokens that still mint new supply for liquidity rewards, such as CRV, read close to **+1.9%** for the next 90 days on our ledgers, and tokens still working through investor and team vesting, such as MORPHO, read around **+7%**. AAVE has no mint at all: its 16M cap was fully issued long ago, so its only new supply is what the DAO chooses to pay out of the reserve, and that payout is small next to the float.

The difference shows up on the buy side. Tokens whose protocols turn fees into buybacks that leave the float, such as LDO on our ledgers, can shrink their supply, while AAVE's fees currently fund the DAO treasury and none of them remove coins. Until a burn or an outside-the-float lock exists, AAVE cannot go below zero, however much the Aave protocol earns. A paused, park-in-the-float buyback and a fixed cap make AAVE look more like a slow-release treasury token than a buy-and-burn token.

## What to watch in the next 90 days

First, the Aavenomics 3.0 proposal: if the automatic buyback goes live and the bought AAVE is burned, Buy #1 or Buy #2 turns non-zero and AAVE could flip from mild growth to shrinking. Second, the next Safety Module allowance update, due about every quarter, which decides how much of the roughly 37,900 AAVE backlog of staking rewards can be claimed. Third, any vote that changes the 150 AAVE daily staking rate, which has been cut several times since 2025. Fourth, the Umbrella reward period ending Dec 2 2026; those rewards are paid in other tokens, but a move to pay in AAVE would add to Sell #1. Fifth, any large payment out of the Ecosystem Reserve beyond the three streams.

## Summary

AAVE supply grew **+0.14%** in the 90 days to Oct 2 2026 and is projected near **+0.15%** for the next 90 days: a mixed, roughly steady picture. The mechanism is simple: AAVE is fully issued at 16M, and new coins reach the market only as staking pay and grant streams from the Aave DAO Ecosystem Reserve, while the AAVE buyback is paused and there is no burn. The key risk is the reserve's unscheduled 490,000 AAVE, which the DAO can spend by vote; the ceiling is that the reserve holds only **565,072 AAVE**, about 3.7% of circulation, so AAVE supply cannot grow much beyond it.

*MrNasdog Pressure Framework analysis of AAVE, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 2 2026.*

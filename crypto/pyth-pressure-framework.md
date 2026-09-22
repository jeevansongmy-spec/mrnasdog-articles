---
title:         "PYTH Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "PYTH supply is roughly steady: 0.00% net over 90 days and next. No mint is possible, the last 2,125M cliff is May 2027, and DAO buybacks stay in the float."
canonical_url: "https://mrnasdog.com/research/pyth/inflation"
tags:                    ["crypto", "pyth", "solana", "oracle"]
published:     true
---

Originally published at [PYTH Inflation Analysis · September 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/pyth/inflation).

# PYTH Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

PYTH supply is roughly steady: the Pressure Framework reads Pyth Network at **0.00%** over the last 90 days and **0.00%** for the next 90, against **−0.14%** on the inflation monitor. Sell pressure is **0** because no PYTH can be minted and no vesting cliff falls in either window; buy pressure is **0** because the DAO's monthly buyback parks PYTH in a treasury that is already counted as circulating. The one constraint that matters is the calendar: the fourth and final cliff of **2,125M PYTH** is due in **May 2027**.

## The verdict, in one paragraph

Against a circulating base of **7,874.96M PYTH**, the framework books **0** of sell pressure and **0** of buy pressure over the trailing 90 days, a net of **0.00%**, and projects **0.00%** for the next 90 days. The inflation monitor reads **−0.14%** for the trailing window, a gap of **0.14 percentage points**, which is inside the framework's 0.5pp tolerance, so the overview ships with no monitor-gap warning. The monitor's small negative reading comes from a single high supply estimate at the start of its window; the circulating count itself sat still all quarter. The label for PYTH is **a capped oracle token in the quiet stretch between two vesting cliffs**.

## Sell pressure: where new PYTH comes from

Not from minting. Sell #1, protocol inflation, is **0**, and it is 0 for good. The PYTH token lives on Solana, and its mint authority reads empty on-chain. On Solana an empty mint authority cannot be restored by anyone, including a DAO vote, so the **10,000M PYTH** ceiling is final. Pyth Network used to pay Oracle Integrity Staking rewards to publishers and delegators, but a DAO vote paused them earlier in 2026 and the leftover reward pool, **0.85M PYTH**, went back to the DAO treasury on **Jul 23 2026**. Those rewards were always paid from existing coins, never from new ones.

Sell #2, vesting unlocks, is **0** in both windows. Pyth Network launched with 15% of supply free and 85% locked, released in four equal yearly cliffs of **2,125M PYTH** at 6, 18, 30 and 42 months after launch. The third cliff landed in **May 2026**, a month before this window opened on **Jun 24 2026**. The fourth and last lands in **May 2027**, well after the next window closes on **Dec 21 2026**. The chain confirms the schedule to the decimal: total PYTH on-chain is **9,999.96M**, and subtracting the circulating count leaves exactly **2,125M**, which is one cliff and nothing else. A proposal in March 2026 to delay the May 2026 cliff never became policy; the cliff fired on time.

Sell #3, Foundation and unscheduled unlocks, is **0**. Every unlocked PYTH is already inside the circulating count, so when a Pyth Network wallet pays out grants or moves coins to an exchange, nothing new reaches the float; the coins were counted the day their cliff fired. Sell #4, long-term locked or bankruptcy, is **0**: there is no bankruptcy estate, trustee or court-ordered distribution attached to PYTH.

## Buy pressure: where new PYTH goes

Buy #1, programmatic buyback, is **0**, and this is the row most worth explaining, because the buyback is real. Since December 2025 the Pyth DAO has sent one third of its non-PYTH treasury each month to the Pythian Council, which buys PYTH on the open market and returns it. In this window **3.62M PYTH** came back to the treasury in three rounds, on **Jul 6 2026**, **Aug 3 2026** and **Sep 2 2026**, matching the DAO's own reports to the sixth decimal. The problem is where it lands. The DAO treasury is not part of the locked 2,125M, so it is already counted as circulating; buying from an exchange into it moves coins from one circulating wallet to another. The PYTH is held, not burned and not locked, so the float does not shrink.

Buy #2, protocol fee burn, is **0**. Pyth Network has no fee burn. Holders do destroy small amounts of PYTH when they clean up wallets, and in the token's whole life that adds up to about **39,845 PYTH**, far too little to show at this scale. Buy #3, Foundation buy, is **0**: beyond the buyback, the treasury received **15.34M PYTH** of revenue share paid in PYTH by Douro Labs, the Pyth Pro operator, plus the returned reward pool, and both are transfers inside the float. Buy #4, new long-term lock, is **0**: governance staking stays open and withdrawable, and staked PYTH is already inside the circulating count.

## Foundation and overhang

The overhang on PYTH is dominated by one item: the final vesting tranche of **2,125M PYTH**, due in **May 2027**. It is scheduled, not discretionary, and it is read from the chain at every rebuild. The second item is the Pyth DAO treasury, which held **38.5M PYTH** on **Sep 22 2026**, up from **18.7M** at the start of the window on buyback credits, revenue paid in PYTH and the returned reward pool. The third is Douro Labs' payout wallet at **15.1M PYTH**, and the fourth is **1.4M PYTH** sitting in the Pythian Council wallet partway through the September buying round. Finally, two large accounts that received most of the May 2026 release still hold **1,064M PYTH** and have not moved since late May. All of these are refreshed from the chain at every rebuild. Because everything except the final tranche is already counted as circulating, none of it can add to the float when it moves; if the final tranche's locked balance ever falls before its date, that outflow enters Sell #3 at the next refresh.

## How PYTH compares to other capped governance tokens

PYTH sits in the class of hard-capped tokens that stopped issuing entirely. That is stricter than a halving-model chain like Bitcoin, which still mints on every block at a slowly falling rate, and far stricter than a proof-of-stake chain paying staking rewards out of fresh issuance. On the issuance axis PYTH reads a flat zero, and a vote cannot change that.

What PYTH shares with most venture-backed tokens is a cliff calendar. Tokens that vest in large yearly cliffs read near zero between cliffs and then jump on the release date; PYTH's May 2026 cliff alone added more than a third to its circulating count. A continuous linear vest spreads the same supply across every day instead. PYTH's pattern means the calm of this quarter says little about May 2027.

The buyback is the other comparison worth making. Exchange tokens that buy back and burn remove coins from existence, and their readings go negative. Pyth Network's programme buys and holds in a DAO treasury that stays inside the circulating count, so in supply terms it is a transfer, not a removal. The DAO's own forum has discussed partial burns; until one is adopted and executed, the buyback supports demand without shrinking the float.

## What to watch in the next 90 days

First, the Pyth Strategic Reserve V2 idea posted on **Sep 9 2026**, which would send the DAO's full revenue share into PYTH purchases; it changes the buying pace, not the treasury destination, so it moves this page only if it adds a burn or a lock. Second, the tenth buying round, approved in **September 2026** and already partly executed. Third, any proposal to burn part of the reserve, which is the one change that would turn Buy #1 on. Fourth, any vote to move the final cliff; it would not affect this window but would reset the May 2027 date. Fifth, the DAO treasury balance at **38.5M PYTH**, which is the pot with a spender rather than a schedule.

## Summary

The MrNasdog Pressure Framework reads PYTH at **0.00%** over the trailing 90 days and **0.00%** projected forward: mixed flows, supply roughly steady. Pyth Network cannot mint new PYTH, no vesting cliff falls between **Jun 24 2026** and **Dec 21 2026**, and the DAO's monthly buyback keeps PYTH in a treasury that already counts as circulating. The key risk is the final cliff of **2,125M PYTH** in **May 2027**, about 27% of today's float. The ceiling is permanent at **10,000M PYTH**, and supply can only shrink from here.

MrNasdog Pressure Framework analysis of PYTH, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 22 2026.

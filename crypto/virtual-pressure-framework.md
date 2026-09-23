---
title:         "VIRTUAL Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "VIRTUAL supply grows 0.29% over 90 days as the last 2024 lockup releases 1.92M tokens. The 1B cap is fully minted, nothing burns, and the treasury sits still."
canonical_url: "https://mrnasdog.com/research/virtual/inflation"
tags:          ["crypto", "virtual", "virtuals", "aiagents"]
published:     true
---

Originally published at [VIRTUAL Inflation Analysis · September 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/virtual/inflation).

# VIRTUAL Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

VIRTUAL supply is roughly steady: the Pressure Framework reads Virtuals Protocol at **+0.29%** over the last 90 days and **+0.05%** over the next 90, against an inflation monitor reading of **+0.22%**. The only VIRTUAL reaching the market is **1.917M VIRTUAL** withdrawn from one 2024 vesting lockup, with **0** bought back or burned. The cap is a hard **1,000M VIRTUAL**, fully minted, and the role that could mint more belongs to an empty address.

## The verdict, in one paragraph

Against a circulating base of **658.4M VIRTUAL**, the framework books **1.917M VIRTUAL** of sell pressure and **0** of buy pressure over the trailing 90 days, a net of **+0.29%**, and **0.360M VIRTUAL** of sell pressure for the next 90 days, a net of **+0.05%**. The inflation monitor reads **+0.22%** for the same window, a gap of **0.07 percentage points**. That is inside the framework's 0.5-point tolerance, so the overview carries no warning. Both readings see the same thing: one vesting lockup draining into the market. The label for VIRTUAL is **a capped, fully minted token with one small lockup left to unwind**.

## Sell pressure: where new VIRTUAL comes from

It does not come from minting. Sell #1, protocol inflation, is **0**, and it is tagged permanent. The VIRTUAL contract on Ethereum caps supply at **1,000M VIRTUAL**, and all of it was minted in Dec 2023. Its only mint function answers to an owner role that was handed to the empty address, so no one can ever call it. When we test-called that mint function, the contract refused with its own permission error. When we swapped in a test value for the stored total, the supply reading changed with it, which shows the flat 1,000M VIRTUAL at both ends of the window is a real reading, not a number fixed in the code. The copies of VIRTUAL on Base, Solana and Robinhood Chain are bridged stand-ins for coins held on Ethereum. The Base copy is backed one for one by the bridge's balance on Ethereum, and the Solana copy by a lock pool on Base, so none of them adds supply.

The whole supply story is Sell #2, vesting unlocks, at **1.917M VIRTUAL**. Most unlock trackers list VIRTUAL as fully unlocked, and for the original allocation that is true. But in Apr and May 2024 a group of holders placed **36.19M VIRTUAL** into a streaming lockup contract, in 19 separate streams running up to two years. That contract sits outside the counted float: circulating supply equals 1,000M minus the treasury multisig minus this lockup, to the last coin. So its coins count the moment holders withdraw them. Its balance fell from **2.28M VIRTUAL** on Jun 25 2026 to **0.36M VIRTUAL** on Sep 23 2026. Most of that came in August, when four streams holding 3.5M VIRTUAL between them reached their end dates. Every transfer in and out of the contract adds up exactly to its current balance.

Sell #3, Foundation and unscheduled unlocks, is **0**: the ecosystem treasury did not move a single coin in the window. Sell #4, long-term locked or bankruptcy, is **0** as well. VIRTUAL has no bankruptcy estate, no trustee and no court-ordered distribution.

## Buy pressure: where new VIRTUAL goes

Nowhere, this window. Buy #1, programmatic buyback, is **0**. Virtuals Protocol is known for a buyback-and-burn, but it buys back and burns each AI agent's own token, one layer down, not VIRTUAL. The VIRTUAL spent on those buybacks lands in agent trading pools, which already count as circulating, so it removes nothing from this reading.

Buy #2, protocol fee burn, is also **0**, and here the contract settles it. The VIRTUAL contract has no burn function at all, so total supply can never fall. We still read both places a burn could appear, at both ends of the window. Total supply stayed at exactly **1,000M VIRTUAL**. The burn addresses on Ethereum and Base gained less than one VIRTUAL between them. The Base copy's supply did fall by about **0.47M VIRTUAL**, but the bridge's balance on Ethereum fell by the same amount: that was coins bridging home, a move, not a burn.

Buy #3, Foundation buy, is **0**: the treasury multisig held the same balance on both dates. The protocol keeps 30% of the 1% agent trading fee, but that income collects in wallets already counted as circulating, so it is not a purchase. Buy #4, new long-term lock, is **0**. VIRTUAL locked for voting power already counts as circulating, and the main voting-lock contract shrank anyway, from **22.27M** to **21.60M VIRTUAL**.

## Foundation and overhang

The overhang on VIRTUAL is one very large pot and one very small one. The large pot is the ecosystem treasury: **340.65M VIRTUAL**, 35% of the cap less early spending, in one multisig on Ethereum. It has not sent a coin anywhere since May 2024. Its rules allow the DAO to release up to 10% a year, only with a vote. Two voted items point at it, and neither has drawn a coin from the multisig: a 1% sniper-defense and yield fund, and a team grant of up to 6% that streams only if VIRTUAL reaches $10, $20 and $40, far above today's price. The small pot is what remains in the 2024 lockup: **0.36M VIRTUAL**, all of it free to claim by Oct 24 2026. Both balances are read from the chain at every rebuild. If the treasury's balance, or the lockup's beyond its own schedule, falls between refreshes, that outflow enters Sell #3 at the next refresh.

## How VIRTUAL compares to other capped launchpad tokens

VIRTUAL belongs to the strictest supply class: a hard cap that is already fully minted, with the minting role given up for good. That is stricter than a halving chain like Bitcoin, which still mints on every block, and stricter than staking tokens whose inflation rate is set by a governance vote. On the issuance side, VIRTUAL cannot inflate at all.

What it does share with younger launchpad tokens is a large treasury outside the float. At **340.65M VIRTUAL**, it is more than half the size of the whole circulating supply. Most launchpad tokens release team and treasury coins on a fixed calendar. VIRTUAL's treasury has no calendar, only a yearly ceiling and a vote, so its risk is a decision, not a date. For two years that decision has been to spend nothing.

The other comparison is to exchange-style tokens that burn their own supply with revenue. Those tokens can read deflationary when usage is high. VIRTUAL collects real fees, but the burn happens one layer down, in agent tokens, so VIRTUAL's own supply takes none of that benefit. Its route to a negative reading would need a new decision to buy back VIRTUAL itself.

## What to watch in the next 90 days

First, the lockup's last two streams end on **Oct 22 2026** and **Oct 24 2026**, after which all **0.36M VIRTUAL** left can be withdrawn and this row goes to zero for good. Second, the staker bonus announced for **Sep 30 2026**: if its VIRTUAL comes from the treasury multisig, it is new sell pressure, and its size and source are not yet published. Third, the treasury multisig itself, at **340.65M VIRTUAL**; any vote that spends from it shows up here at the next refresh. Fourth, any governance move to buy back VIRTUAL itself rather than agent tokens, which is the one event that could flip this reading negative.

## Summary

The MrNasdog Pressure Framework reads VIRTUAL at **+0.29%** over the trailing 90 days and **+0.05%** projected forward: mixed flows, supply roughly steady. Virtuals Protocol mints nothing and burns nothing; the only supply reaching the market is the tail of one 2024 vesting lockup, **1.917M VIRTUAL** last quarter and at most **0.360M VIRTUAL** next. The key risk is the **340.65M VIRTUAL** treasury, which can release up to 10% a year with a vote. The ceiling is firm: **1,000M VIRTUAL**, fully minted, with no one able to mint more.

MrNasdog Pressure Framework analysis of VIRTUAL, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 23 2026.

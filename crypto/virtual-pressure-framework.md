---
title:         "VIRTUAL Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description:   "VIRTUAL supply is roughly steady: a 2024 lockup released 1.62M VIRTUAL for +0.25% net in 90 days, +0.04% next. Capped 1B, no burn, 340.65M treasury unmoved."
canonical_url: "https://mrnasdog.com/research/virtual/inflation"
tags:          ["crypto", "virtual", "virtuals", "aiagents"]
published:     true
---

Originally published at [VIRTUAL Inflation Analysis · October 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/virtual/inflation).

# VIRTUAL Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

**VIRTUAL**, the base coin of **Virtuals Protocol**, added about **0.25%** to its circulating supply in the last 90 days, and we expect only about **0.04%** in the next 90. The whole sell side is one old 2024 lockup paying out its last streams: **1.62M VIRTUAL** left it in the window and **295,279 VIRTUAL** is all that remains, free by **Oct 24 2026**. No new VIRTUAL can be minted — supply is capped at 1B and all 1B already exist — and nothing buys back or burns VIRTUAL, so the buy side is **0**.

## The verdict, in one paragraph

Over the 90 days from Jul 9 2026 to Oct 7 2026, sell pressure on VIRTUAL was **1.62M VIRTUAL** and buy pressure was **0**, a net of **+0.25%** on a circulating supply of **658.39M VIRTUAL**. For the next 90 days the ledger shows **+0.04%**, because the lockup that did all the releasing has only **295K VIRTUAL** left. Our inflation monitor could not be read on Oct 8 2026; the same supply series rebuilt from public market data reads **+0.15%**, a gap of **0.10 percentage points** — well inside our 0.5-point tolerance, so no warning chip is shown. The series reads a little lower only because its count of circulating VIRTUAL stopped moving after Aug 28 2026, while another 665,929 VIRTUAL left the lockup after that day. In one line: **a capped coin at the very end of its last lockup, with a large treasury that has not moved**.

## Sell pressure: where new VIRTUAL comes from

**Protocol inflation is 0.** The VIRTUAL token contract on Ethereum caps supply at 1,000,000,000, and all 1B already exist (the project began as PathDAO and took its new name in late 2023). The owner key has been given up, and when we tested a new mint from the owner address the contract refused it with its own cap error. There are no staking rewards paid in new coins and no emission programme. The copies of VIRTUAL on Base, Solana, Robinhood Chain and Arc are bridged from that one Ethereum supply, so they add nothing.

**Vesting unlocks were 1.62M VIRTUAL.** In 2024 a set of wallets put 36.19M VIRTUAL into 19 time-locked streams in one lockup contract. Most of those streams have already finished. In this window 23 claims and refunds took **1,619,934 VIRTUAL** out of the lockup; its balance fell from 1.92M to 295,279, and the payments we counted add up to that drop exactly. What is left sits in four streams: two that are still running and end on Oct 22 2026 and Oct 24 2026, and two that have already finished but were never claimed. We book the whole **295,279 VIRTUAL** for the next 90 days as the most that can come out; after Oct 24 2026 this row is empty.

**Foundation and unscheduled unlocks were 0.** The ecosystem treasury holds **340.65M VIRTUAL** in a 4-of-6 multisig and has not sent a single coin since May 2024. Some unlock trackers draw a monthly release of 2.92M VIRTUAL from it, but that is a paper model of the 10%-a-year spending cap, and the wallet did not move. **Long-term locked or bankruptcy is 0**: Virtuals Protocol never raised an outside funding round, and no estate or trustee holds VIRTUAL.

## Buy pressure: where new VIRTUAL goes

**Programmatic buyback is 0.** Virtuals Protocol does run buybacks, but they buy and burn agent tokens, not VIRTUAL. The 1% trading tax on agent tokens is split between the agent creator and the protocol, and the protocol's share lands in wallets that already count as circulating, so it removes nothing.

**Protocol fee burn is 0.** The VIRTUAL contract has no burn function. Total supply read exactly 1B at both ends of the window, the dead address on Ethereum held the same 1,498 VIRTUAL, and the copy on Base gained less than one coin. **Foundation buy is 0**: no treasury or team purchase of VIRTUAL was announced or seen on-chain, and the holder proposals asking for a VIRTUAL buyback expired in Dec 2025 without passing.

**New long-term lock is 0.** Holders can lock VIRTUAL as veVIRTUAL for voting power, points and a new staker bonus. The staking contract held 22.48M VIRTUAL at the start of the window and **21.56M VIRTUAL** at the end. Locked VIRTUAL still counts as circulating, so the lock takes nothing out of the float, and the small drop added nothing to it either.

## Foundation and overhang

Two balances sit outside the circulating count, and together they explain it to the coin: the ecosystem treasury multisig with **340.65M VIRTUAL**, and the 2024 lockup with **295,279 VIRTUAL**. The treasury is the big one — about a third of all VIRTUAL. Its rules allow at most 10% a year to be spent, and only after a veVIRTUAL vote. Governance has already approved a staff grant of up to 6% of supply, but it pays out only if VIRTUAL reaches $10, $20 and $40, far above today's price, and a 1% fund for launch defence. We read the treasury and the lockup on-chain at every rebuild. If the treasury's balance falls between refreshes, the outflow enters Sell #3 at the next refresh; the lockup is tracked in Sell #2 until it is empty.

Other wallets the team runs — the staking contract, the fee wallets on Base and the bridge escrows — already count as circulating, so a move from them changes nothing in this ledger.

## How VIRTUAL compares to other launchpad and AI-agent tokens

Most launchpad tokens either print new coins to reward users or spend platform fees buying their own coin back. VIRTUAL does neither. Its supply is a hard cap that is already fully minted, so the only way supply reaches the market is from wallets that were set aside at the start — and in Virtuals Protocol's case that is almost entirely one treasury that has been still for over two years. Fee buybacks exist, but they point at the agent tokens built on the platform, so they support those coins rather than VIRTUAL itself.

That makes VIRTUAL closer to a capped token with a large reserve than to a fee-burning chain coin like ETH or a buyback token. Day to day the float barely grows: once the 2024 lockup empties in October 2026, the next-90-day reading falls to zero unless the treasury moves. The risk is not slow dilution; it is one large, vote-gated pile of **340.65M VIRTUAL** that could be released in bigger steps — up to 10% of it in a year.

## What to watch in the next 90 days

**Oct 22 2026 and Oct 24 2026:** the last two lockup streams end, and all of the remaining 295,279 VIRTUAL can be claimed; after that the vesting row is empty.

**The staker bonus that began Sep 30 2026:** veVIRTUAL holders get extra VIRTUAL by stake age; the source of those coins has not been published, and it only becomes new supply if it is paid from the treasury multisig.

**The vote that closes Oct 8 2026:** a holder proposal offers veVIRTUAL stakers a one-time early unstake. Staked coins already count as circulating, so it would not change this ledger, but it could free up to 21.56M VIRTUAL to trade.

**Any treasury vote:** a governance proposal to spend from the 340.65M treasury is the one event that could move this reading by more than a fraction of a percent.

## Summary

VIRTUAL, the base coin of Virtuals Protocol, grew its circulating supply by about **0.25%** in the last 90 days, all of it from the last streams of a 2024 lockup, and we expect about **0.04%** in the next 90 as that lockup runs dry on Oct 24 2026. No new VIRTUAL can be minted, and nothing burns or buys it back. The key risk is the **340.65M VIRTUAL** treasury, untouched since May 2024 but able to release up to 10% a year after a holder vote. Until that wallet moves, VIRTUAL is a capped coin with almost no new supply reaching the market.

---

*MrNasdog Pressure Framework analysis of VIRTUAL, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 8 2026.*

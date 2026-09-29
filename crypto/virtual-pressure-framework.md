---
title:         "VIRTUAL Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "VIRTUAL supply is roughly steady: a 2024 lockup released 1.90M VIRTUAL for +0.29% net in 90 days, +0.05% next. Capped 1B, no burn, 340.65M treasury unmoved."
canonical_url: "https://mrnasdog.com/research/virtual/inflation"
tags:          ["crypto", "virtual", "virtuals", "aiagents"]
published:     true
---

Originally published at [VIRTUAL Inflation Analysis · September 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/virtual/inflation).

# VIRTUAL Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

The MrNasdog Pressure Framework reads VIRTUAL at **+0.29% net** over the trailing 90 days and **+0.05%** over the next 90. The only new supply is an old 2024 lockup on Ethereum that paid out **1,901,514 VIRTUAL** in the window and now holds just **360,201 VIRTUAL**, all claimable by Oct 24 2026. VIRTUAL has a hard cap of **1B** that is already fully minted, no burn and no buyback of its own, so the one real risk sits in the **340.65M VIRTUAL** ecosystem treasury — a multisig that has not moved a coin since May 13 2024.

## The verdict, in one paragraph

Over the 90 days from Jul 1 2026 to Sep 29 2026, VIRTUAL supply that the market can trade grew by **1.90M VIRTUAL**, or **+0.29%** of the **658.39M** circulating. Nothing came off the market. The monitor, which tracks the circulating count day by day, reads **+0.24%** for the same stretch, a gap of **0.05 percentage points** — well inside our half-point tolerance, so no warning chip is shown. For the next 90 days the Virtuals Protocol ledger falls to **+0.05%**, because the 2024 lockup is nearly empty. VIRTUAL is a fixed-supply coin whose float is almost settled: quiet today, with one large treasury in reserve.

## Sell pressure: where new VIRTUAL comes from

Protocol inflation is **0** and will stay there. All 1,000,000,000 VIRTUAL were created on Ethereum in December 2023. The token contract has a hard cap of 1B, that cap is already reached, and the owner key was given up, so a new mint fails with the contract's own cap error. The contract also has no burn function, which means the supply can never drop below the cap and reopen room for minting. The VIRTUAL on Base, Solana, Robinhood Chain and Arc are bridge copies: each one exists only because the same coin is locked in a bridge on Ethereum or Base, so Virtuals Protocol supply is counted once, on Ethereum.

Vesting unlocks are the one live row, at **1.90M VIRTUAL**. A lockup contract set up in 2024 holds streams for early partners and contributors, and those coins sit outside the circulating count until someone claims them. Holders claimed 23 times in the window, most heavily in August, taking out **1,901,514 VIRTUAL**. We read the contract balance at both ends of the window and it fell by exactly that amount. Only **360,201 VIRTUAL** remain: two streams finish on Oct 22 2026 and Oct 24 2026, and the rest has already vested but is not claimed yet. So the next 90 days carry at most **0.36M VIRTUAL** from this source. Unlock trackers list VIRTUAL as fully unlocked; the chain shows this small tail still running.

Foundation and unscheduled unlocks are **0**: the ecosystem treasury did not send a single coin in the window. Long-term locked coins and bankruptcy releases are also **0** — there is no estate, and the coins locked for voting are already part of the circulating count.

## Buy pressure: where new VIRTUAL goes

All four buy rows are **0**. Virtuals Protocol does run buybacks, but they buy and burn agent tokens, not VIRTUAL. Every agent token pays a 1% trading fee; 70% goes to the agent's creator and 30% to the Virtuals treasury wallets, which are already counted as circulating, so that flow does not take VIRTUAL off the market. There is no protocol fee burn: total supply read exactly 1B at both ends of the window, and the dead addresses hold about 1,500 VIRTUAL, unchanged apart from 0.18 sent by hand. No team wallet bought VIRTUAL, and the treasury multisig stayed still.

Staking does not remove coins either. Holders can lock VIRTUAL for up to two years to get veVIRTUAL, which gives voting power and a share of new agent-token airdrops. Those locked coins stay in the circulating count, and the lock actually shrank this window, from **22.56M** to **21.58M VIRTUAL**. So a new long-term lock books **0**.

## Foundation and overhang

The overhang that matters is the ecosystem treasury: a multisig on Ethereum holding **340,652,950 VIRTUAL**, about 34% of all VIRTUAL and outside the circulating count. It has made only seven transfers in its life, and the last coins left it on May 13 2024. Under the Virtuals Protocol whitepaper it may release no more than 10% a year for three years, and only after a holder vote. The governance portal shows no passed proposal in 2026, and the newest one, from March 2026, failed. One unlock tracker models this treasury as releasing about 2.9M VIRTUAL every month; the chain says it has not released anything, so we book what the chain shows.

The second overhang is the 2024 lockup's remaining **360,201 VIRTUAL**, which is on a known schedule and already in the next-90-day number. Inside the circulating count sit the protocol's fee wallet on Base (about 2.14M VIRTUAL), the voting lock (21.58M) and a second small lockup (about 91K); moving those adds nothing new. We read the treasury and the lockup straight from the chain at every rebuild. If the treasury's balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How VIRTUAL compares to other launchpad tokens

Most launchpad and app tokens still carry large team and investor vesting, so their supply grows by several percent a quarter as cliffs open. VIRTUAL is different: its public share was fully unlocked from the start, there was no venture round with a multi-year schedule, and the cap is already minted. That puts VIRTUAL closer to a fixed-supply coin than to a typical launchpad token — the float moves only when an old lockup or the treasury pays out.

The trade-off is on the buy side. Launchpads that send their fees into buying back their own token create steady buy pressure. Virtuals Protocol points its fee buybacks at the agent tokens built on it, so VIRTUAL gains demand from agent trading, since every agent trades against VIRTUAL, but not a direct buyer. Against uncapped chain tokens that pay validators in new coins, VIRTUAL has no issuance at all; against exchange tokens with quarterly burns, it has no burn. Its supply story comes down to one question: when, and how fast, the treasury is spent.

## What to watch in the next 90 days

First, the VIRTUAL staker bonus that starts on Sep 30 2026: veVIRTUAL holders get extra VIRTUAL based on how long they have staked, but neither the size nor the source is public yet — if it is paid from the treasury multisig, it becomes new supply. Second, the last two streams of the 2024 lockup end on Oct 22 2026 and Oct 24 2026, after which that row falls to zero. Third, any holder vote to deploy the ecosystem treasury; even one year at the 10% cap would add up to 35M VIRTUAL, far more than anything in today's ledger. Fourth, any change to where the 1% agent trading fee goes — a switch to buying VIRTUAL itself would create the coin's first real buy row.

## Summary

VIRTUAL, the base token of Virtuals Protocol, has a hard-capped and fully minted supply of 1B, with no issuance, no burn and no buyback of its own. The only new supply in the last 90 days was **1.90M VIRTUAL** from a 2024 lockup, a **+0.29%** net that falls to **+0.05%** next as that lockup empties by Oct 24 2026. The key risk is the **340.65M VIRTUAL** ecosystem treasury, which is capped at 10% a year and needs a holder vote, and which has not moved since May 2024. Until that treasury is spent, VIRTUAL supply is roughly steady.

---

*MrNasdog Pressure Framework analysis of VIRTUAL, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

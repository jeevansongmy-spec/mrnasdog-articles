---
title:         "VIRTUAL Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description:   "VIRTUAL is roughly steady: fixed 1B cap, no minting, 1.55M out of an old lockup gives +0.24% in 90 days, at most +0.04% next. 340.65M treasury unmoved."
canonical_url: "https://mrnasdog.com/research/virtual/inflation"
tags:          ["crypto", "virtual", "virtuals", "aiagents"]
published:     true
---
Originally published at [VIRTUAL Inflation Analysis · October 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/virtual/inflation).

# VIRTUAL Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

<!-- main-page -->
This is the long supply read. For the signal, the price drivers and the questions people ask about Virtuals Protocol, see [mrnasdog.com/research/virtual](https://mrnasdog.com/research/virtual).

VIRTUAL, the base coin of the Virtuals Protocol AI-agent launchpad, is close to flat: supply in the market grew about **+0.24%** in the last 90 days and can grow at most **+0.04%** in the next 90. No new VIRTUAL is minted — the contract caps supply at **1B** and the mint key was given up — so the only new float came from an old lockup that released **1,549,376 VIRTUAL**, against **0** bought back, burned or newly locked. The real question for VIRTUAL is the treasury: **340.65M VIRTUAL**, about a third of all coins, that has not moved since May 2024.

## The verdict, in one paragraph

Our ledger reads a net **+0.24%** for VIRTUAL over the 90 days to Oct 18 2026 (**1.55M VIRTUAL** of new float on **658.39M** circulating), and a ceiling of **+0.04%** for the next 90 days. Our monitor could not be read on this check, so we ran the same check on the same market data instead: it shows **+0.13%**, a gap of about **0.10** percentage points, inside our 0.5-point limit, so no warning chip is shown. The market figure reads lower because its count of the lockup stopped updating at the end of August 2026 while about 666,000 more VIRTUAL was paid out after that. In one line: VIRTUAL is a fixed-supply coin with a quiet float and a large treasury that has stayed still.

## Sell pressure: where new VIRTUAL comes from

Protocol inflation is **0**. All 1B VIRTUAL were created when the coin moved over from its older PathDAO token in December 2023. The Ethereum contract has a hard cap of exactly 1B, and the owner role that could call mint was renounced. We tested this on the live contract: a mint call from an outside wallet is refused because it is not the owner, and even a call from the empty owner address is refused because it would break the cap. The VIRTUAL coins on Base, Solana, Robinhood Chain and Arc are bridged copies backed by coins locked on Ethereum, so they add nothing new.

Vesting unlocks are the one live sell row: **~1.55M VIRTUAL**. A lockup contract created in 2024 that sits outside the circulating count started the window with 1,844,656 VIRTUAL and ended it with 295,279. We matched that drop, to the last coin, against all 19 claims and refunds it sent in the window. What is left sits in four streams that are all claimable by **Oct 24 2026**, so the next 90 days can add at most **~295K VIRTUAL**, and then the lockup is empty. Two of those streams ended in August and September and have still not been claimed, so the real figure may come in lower.

Foundation and unscheduled unlocks are **0**. The treasury multisig on Ethereum held 340,652,950 VIRTUAL at both ends of the window, and its full history shows the last coins left it on May 13 2024. Some unlock trackers show 2.9M VIRTUAL coming out of a Foundation pool on the 28th of every month, but the wallet did not move on Jul 28, Aug 28 or Sep 28 2026, so we do not count it. Long-term locked or bankruptcy supply is also **0**: VIRTUAL never raised money from investors, so there are no investor lockups, and no estate or court holds any.

## Buy pressure: where new VIRTUAL goes

Programmatic buyback is **0**. Every agent token on Virtuals trades with a 1% tax that is swapped into VIRTUAL and split between the agent creator and protocol wallets. That swap does buy VIRTUAL in the market, but the coins land in wallets that already count as circulating, so they only change hands. The buyback and burn programs on the platform target agent tokens, not VIRTUAL, and holder proposals in December 2025 asking for a revenue buyback did not pass.

The protocol fee burn is **0**: the VIRTUAL contract has no burn function, total supply read exactly 1B at both ends, and the dead address on Base gained only a quarter of a coin. Foundation buys are **0** — no treasury purchase was announced or seen on-chain. New long-term locks are **0** too. Holders can lock VIRTUAL for up to two years to vote and earn agent-token airdrops, but the lock shrank from 22.37M to 21.49M VIRTUAL in the window, and locked coins still count as circulating anyway.

## Foundation and overhang

The overhang that matters is the treasury multisig: **340.65M VIRTUAL**, which we read on-chain at every check. The project's rules let it release no more than 10% of the treasury share a year, and only after a holder vote. Only three proposals have ever passed, all in July 2025: setting up the Virtuals Foundation, a 1% fund to defend agent launches against snipers, and a grant of up to 6% of supply to the core team that starts only if VIRTUAL holds $10, then $20, then $40, for 30 days. At about $0.63 today none of those price steps is close.

The second overhang is the lockup contract, now down to 295,279 VIRTUAL and due to be empty after Oct 24 2026. The protocol's fee wallets and the vote-lock are already inside the float, so they are not overhang. If the treasury or the lockup balance falls between our checks, the outflow goes into the sell side at the next check.

## How VIRTUAL compares to other AI-agent and launchpad tokens

VIRTUAL sits in the fixed-cap group. Bittensor (TAO) pays new coins to miners and validators every block on a halving schedule, so its supply grows by design. Other AI tokens pay stakers in new coins. VIRTUAL has neither: no emission and no staking pay in VIRTUAL, so its float grows only when locked or treasury coins are released.

Against other launchpads the difference is on the buy side. Some launchpad tokens, such as Pump.fun's PUMP, spend platform revenue on buying their own coin back. On Virtuals, trading fees are paid out in VIRTUAL to creators and the protocol, so the buying is real but the coins stay in the market. That means VIRTUAL has no built-in buyer to offset a treasury release.

The closest match is a governance token with a big, voted treasury: a fixed cap, almost no new float today, and one large wallet whose release needs a vote. For VIRTUAL that wallet holds 34% of all coins, far more than the 0.03% that is still left in old lockups.

## What to watch in the next 90 days

**Oct 22 and Oct 24 2026**: the last two lockup streams finish, and after that the whole remaining 295,279 VIRTUAL can be claimed. Once it is claimed, the vesting row goes to zero.

**Oct 28, Nov 28 and Dec 28 2026**: the dates some trackers mark for a 2.9M VIRTUAL Foundation unlock. We will check the treasury multisig on each date. If it moves, the release goes into the sell side.

Any new treasury vote: a proposal to spend from the 340.65M VIRTUAL treasury, for agent rewards, grants or the launch-defense fund, would be the first real release since May 2024. The 10%-a-year limit would cap it at about 35M VIRTUAL a year.

Fee flows and any buyback: if Virtuals starts using fee income to buy VIRTUAL and lock or burn it, that would be the coin's first buy row.

## Summary

VIRTUAL is a fixed-supply coin: the contract caps it at 1B and no one can mint more, so supply in the market grew only **+0.24%** in the 90 days to Oct 18 2026, all of it from an old lockup that is almost empty, with at most **+0.04%** to come. Nothing buys back or burns VIRTUAL. The key risk is the **340.65M VIRTUAL** treasury, a third of all coins, which has not moved since May 2024 but can release up to about 35M VIRTUAL a year after a holder vote.

---

*MrNasdog Pressure Framework analysis of VIRTUAL, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 18 2026.*

---
title: "FLOKI Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description: "FLOKI supply is roughly steady: no new FLOKI can be made, and staking-exit burns plus a fee buyback removed 5.18B FLOKI in 90 days, −0.05% net, the same next."
canonical_url: "https://mrnasdog.com/research/floki/inflation"
tags: ["crypto", "floki", "tokenomics", "ethereum"]
published: true
---

Originally published at [FLOKI Inflation Analysis · September 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/floki/inflation).

# FLOKI Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

The MrNasdog Pressure Framework reads FLOKI at **−0.05% net** over the trailing 90 days and **−0.05%** over the next 90: no new FLOKI is created at all, and burns removed **5.18B FLOKI** from a float of **9.64T**. Almost all of that burn is the early-unstake penalty of the Floki staking program — **5.14B FLOKI** — with a fee-funded buyback adding **38.05M**. Floki supply is fixed by code on both Ethereum and BNB Chain, so FLOKI can only shrink, and it shrinks slowly.

## The verdict, in one paragraph

Over the 90 days to Sep 29 2026, the Floki ledger shows **0 FLOKI** of new supply and **5,178,671,821 FLOKI** burned, a net of **−0.0537%** of circulating supply, shown as **−0.05%**. Our inflation monitor, which reads the classified circulating figure day by day, shows **−0.0671%** over the same stretch. The gap is **0.013 percentage points**, well inside the half-point tolerance, so no warning chip is shown and the two readings agree. The next 90 days project the same **−0.05%**, because both burn streams ran through the whole window and nothing dated is due to change them. FLOKI is a fixed-supply token with a slow, usage-driven burn: a quiet, mildly deflationary float.

## Sell pressure: where new FLOKI comes from

Nowhere. Protocol inflation is **0** and always will be: the FLOKI token contract on each chain created 10 trillion FLOKI once, at launch, and its code has no mint function. We read the verified Floki source this session and walked every line that changes a balance — the one-time creation and the transfer function, which only moves coins and sends the 0.3% trading tax to the treasury. Ownership of both contracts sits with a dead address, so no one can change that code path. The same bytecode runs on Ethereum and on BNB Chain.

Vesting unlocks are **0**. Floki has no team or investor allocation on a release calendar, and no unlock tracker lists one. Foundation and unscheduled unlocks are also **0**: the Floki DAO treasury and the other team wallets are already inside the circulating count, so when they pay out or sell, coins move within the float rather than into it. Long-term locked supply and bankruptcy releases are **0** too. There is no estate, and the Floki staking pools, which hold about **956.07B FLOKI** on Ethereum and **735.33B FLOKI** on BNB Chain, are counted as circulating already, so unstaking adds nothing new.

## Buy pressure: where new FLOKI goes

Every FLOKI that leaves the float goes to the same place: the unspendable burn address on each chain. Its balance rose by **3,430,309,160 FLOKI** on Ethereum and **1,748,362,660 FLOKI** on BNB Chain across the window, and a sweep of every burn transfer in those 90 days added up to exactly the same totals, to the last unit.

The programmatic buyback removed **38.05M FLOKI**. The Floki token locker sends a quarter of every fee it earns to buy FLOKI on the market and burn it; the rest goes to the treasury. On Ethereum an automated run on Sep 21 2026 bought and burned most of the **23.48M** booked there; on BNB Chain runs on Aug 21, Aug 31, Sep 21 and Sep 27 burned **14.58M**. The old Floki trading bot, which used half its fees to buy and burn FLOKI, has been retired, and its new version charges no fee during testing, so it adds nothing to the forecast.

The protocol fee burn is **0**: the 0.3% trading tax funds the Floki treasury rather than a burn. The Foundation buy is **0**, since no treasury purchase for its own account showed up. A new long-term lock is **0** because new stakes stay inside the circulating count.

The largest row is the early-unstake burn at **5.14B FLOKI**. Floki staking locks coins for 3 to 48 months, and anyone who leaves early loses 5% to 20% of the stake to the burn address. That happened **193** times this window: **3.41B FLOKI** on Ethereum and **1.73B FLOKI** on BNB Chain. A handful of holders also burned **13,492 FLOKI** by hand; those one-offs are not projected forward.

## Foundation and overhang

The team-controlled FLOKI we track is all inside the float. The Floki DAO treasury holds about **22.41B FLOKI** on Ethereum, down from about **60.60B** 90 days ago, and about **74.69B FLOKI** on BNB Chain, up from about **20.06B**. A second Ethereum Safe run by the same five signers holds about **114.65B FLOKI**, down from about **164.65B**. The wallet set aside for the Floki ETP holds about **7.78B FLOKI** on Ethereum and **8.53B FLOKI** on BNB Chain, unchanged. The contracts that collect the trading tax hold well under 1M FLOKI each, and the locker's treasuries hold almost none. We read these balances on-chain at every rebuild and review the project's news every two weeks.

Because the circulating count already includes all of these wallets, a treasury sale changes who holds FLOKI, not how much FLOKI exists. If one of these balances falls between refreshes, we check where the coins went; only coins proven to enter the float from outside it would ever reach the sell side.

## How FLOKI compares to other meme coins

FLOKI sits with the fixed-supply meme coins, not with the ones that print new coins. Dogecoin adds a fixed number of new coins every block forever, so its supply grows every year no matter what holders do. Floki can never grow: its supply was fixed at launch on both chains, and the only open question is how fast it shrinks.

Among fixed-supply meme coins, the difference is what drives the burn. Some rely on a large one-time burn or a tax that burns on every trade. Floki burns through its own products: stakers who break their lock, and a slice of the fees its token locker earns. That ties the burn to how the Floki products are used, which makes it steady but small — about **0.05%** of supply every 90 days.

Floki also runs on two chains, Ethereum and BNB Chain, with a separate 10-trillion supply on each and a large share of each already burned. The float is simply everything not sitting at the two burn addresses, about **9.64T FLOKI**, so there is no hidden locked bucket waiting to be released.

## What to watch in the next 90 days

First, the replacement for the Floki trading bot: at its Sep 7 2026 update the team said the share of fees going to buy and burn FLOKI is still being decided, and a real fee on a busy bot could become a second burn stream. Second, the pace of early exits from Floki staking, which drives **99%** of the burn — a wave of exits would speed it up, a calm market would slow it. Third, the automated locker buyback runs, last seen on Sep 21 and Sep 27 2026. Fourth, the Floki DAO treasury, whose BNB Chain wallet grew by about **54.6B FLOKI** this window; its sales do not change supply, but its choices on burns would. Fifth, any Floki DAO vote on a new burn or on the ETP, where no date has been set.

## Summary

FLOKI cannot inflate: its code on Ethereum and BNB Chain has no way to create new coins, so Sell pressure is **0**. Burns from the Floki staking early-unstake penalty and a fee-funded buyback removed **5.18B FLOKI** in 90 days, a net of **−0.05%**, matching our monitor within **0.013 percentage points**. The main risk to the reading is how small the burn is: it depends on stakers leaving early, and the retired trading bot no longer adds to it. Supply is capped at what exists today, about **9.64T FLOKI**, and can only go down from here.

*MrNasdog Pressure Framework analysis of FLOKI, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

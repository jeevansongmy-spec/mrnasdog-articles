---
title:         "PENDLE Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "PENDLE supply grows +1.50% in 90 days with nothing minted: treasury wallets and expiring vote-locks released 2.60M PENDLE, and the buyback removed none."
canonical_url: "https://mrnasdog.com/research/pendle/inflation"
tags:                    ["crypto", "pendle", "defi", "inflation"]
published:     true
---

Originally published at [PENDLE Inflation Analysis · September 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/pendle/inflation).

# PENDLE Inflation Analysis · September 2026 · Supply growing · projected to keep growing

PENDLE supply is growing and is projected to keep growing, even though the Pendle token contract minted **0** PENDLE in the last 90 days. The Pressure Framework books **2.60M PENDLE** of sell pressure — treasury wallets paying for rewards and exchange sends, plus expiring vote-locks — against **0** of buy pressure, for **+1.50%** over the trailing 90 days and **+0.82%** projected forward, while the monitor reads **+2.04%**. The fee-funded buyback is real, but every bought PENDLE goes to stakers who are still counted as float, and behind all of it sits **9.51M PENDLE** of unclaimed emissions that one wallet can mint at any time.

## The verdict, in one paragraph

Against a circulating base of **173.59M PENDLE**, the framework books **2.60M PENDLE** of sell pressure and **0** of buy pressure over the trailing 90 days — a net of **+1.50%** — and projects **+0.82%** for the next 90 days as the vote-lock expiry calendar thins out. The inflation monitor reads **+2.04%** for the same window, a gap of **0.54 percentage points**, which is over the framework's 0.5pp tolerance and therefore ships with a monitor-gap warning on the overview page. The gap is fully explained: about **0.04pp** is base convention, because the monitor divides by the supply of 90 days ago, and about **0.52pp** comes from the monitor's two snapshot readings — its **Jun 24 2026** reading sits **0.69M PENDLE** below the same feed's own day-by-day series, and its **Sep 22 2026** reading **0.21M** above it. The label for PENDLE is **a non-minting token whose float grows from treasury spending and expiring locks**.

## Sell pressure: where new PENDLE comes from

Not from the mint. The PENDLE token contract read a total supply of **281.53M PENDLE** at both ends of the window, identical to the last unit, and its weekly emission counter did not advance. Pendle still pays liquidity rewards — shared out by an algorithmic reward model since January 2026 — but they are funded from the governance treasury rather than from new coins. That treasury sent **0.40M PENDLE on Jul 20 2026** and **0.50M PENDLE on Sep 13 2026** to the wallet that feeds the reward gauges and the reward distributor. The treasury sits outside the counted float, so those coins enter the market the moment they leave it: Sell #1, protocol inflation, is **0.90M PENDLE**, and the forward column assumes the same pace.

Sell #2, vesting unlocks, is **0**. Pendle's team, investor and advisor allocations finished vesting in September 2024, and no vesting calendar is left to release.

Sell #3, Foundation and unscheduled unlocks, is **0.79M PENDLE**. On **Sep 8 2026** the governance treasury sent **0.60M PENDLE** through a one-hop wallet to an exchange deposit wallet, the same route it used for another **0.60M** on **May 13 2026**. The team wallet sent **0.12M on Jun 25 2026** and **0.07M on Aug 26 2026** along the same kind of route. For the next 90 days the framework books one more team payment of about **0.07M PENDLE**; the treasury's exchange sends have come about four months apart, so the next one would land after this window.

Sell #4, long-term locked, is **0.91M PENDLE**, and it is the vePENDLE vote-lock unwinding. vePENDLE was replaced by liquid sPENDLE staking in January 2026, and it took **zero** new deposits in the window. As two-year locks reach their expiry, holders withdraw: **253** withdrawals returned the full **0.91M**, and the contract's own expiry schedule releases **0.45M PENDLE** in the next 90 days.

## Buy pressure: where new PENDLE goes

Buy #1, programmatic buyback, is **0** — and this is the row worth explaining, because the buyback genuinely runs. Pendle routes **80%** of its swap and yield fees into PENDLE purchases every two weeks. In the window the buyback contract bought **0.98M PENDLE** and passed **0.97M** into the sPENDLE staking contract, which pays it out to stakers. The question the framework asks is where those coins end up relative to the float, and the answer is inside it: rebuilding the non-circulating count wallet by wallet closes only when the staking contract is counted as circulating. PENDLE bought out of the market and handed to stakers who can leave in 14 days stays in the market, so the buyback removes nothing from this reading.

Buy #2, protocol fee burn, is **0**. The PENDLE token has a burn function, but its burn switch reads off at both ends of the window. The framework read both burn surfaces rather than trusting one: the dead address held **0.1 PENDLE** at both ends and the total supply did not move, so nothing was destroyed. Governance could turn burning on, but only after a 7-day delay.

Buy #3, Foundation buy, is **0**: the governance treasury, the team wallet, the ecosystem fund and the vote-lock received not a single PENDLE in the window. Buy #4, new long-term lock, is **0**. The old vote-lock took no deposits, and sPENDLE is liquid staking with a 14-day exit, counted as circulating, so it is not a lock that takes PENDLE off the market.

## Foundation and overhang

The largest overhang on PENDLE does not exist yet. The token contract accrues a weekly emission that only its designated rewards wallet can mint, and that wallet last claimed on **Mar 24 2025**, when **23.08M PENDLE** was minted in one call. Since then **9.51M PENDLE** of unclaimed emissions has built up, growing by about **1.43M**each quarter at the contract's terminal rate of roughly 2% a year. Claims have come in lumps, months apart, with no public schedule, so the framework watches it at every rebuild rather than booking it. A claim would add those coins to the float in a single step.

The rest is held in four wallets outside the float, each read on-chain at every rebuild: the vePENDLE vote-lock with **63.58M PENDLE**, of which about **2.0M** has already expired but not been withdrawn and the rest expires by **Mar 2 2028**; the governance treasury with **19.75M**; the ecosystem fund with **16.12M**, which did not move this window; and the team wallet with **7.77M**. The buyback contract passes coins straight through to stakers and holds almost nothing. If any of these balances falls between refreshes by more than the rows above account for, that outflow enters Sell #3 at the next refresh.

## How PENDLE compares to other DeFi governance tokens

PENDLE sits in a group of DeFi tokens whose supply chart looks flat while their tradable float keeps rising. A capped proof-of-work coin adds float only through new blocks; PENDLE adds float through wallets the project already holds. That is why a total supply that did not move by a single unit can still read **+1.50%**: the pressure comes from coins crossing from project-held and locked balances into circulation, not from creation.

The second comparison is the buyback. Some protocols send bought-back tokens to a dead address or to a treasury the market does not count, and their readings can go negative. Pendle pays its bought-back PENDLE to stakers, which rewards holders but leaves the coins in the float. A burn or a lock outside the float would turn the same **0.98M PENDLE** a quarter into real buy pressure; a payout to liquid stakers does not.

The third is the vote-escrow model. Classic two-year vote-locks pull supply out of the market for long stretches. Pendle has retired that design for liquid staking, so the vePENDLE balance can only fall from here, and every expiry is a small, dated release rather than a lock that renews itself.

## What to watch in the next 90 days

First, the dormant mint: any call to the emission function would add about **9.51M PENDLE** or more in one step, far larger than every other row. Second, vote-lock expiries, with the largest in the window on **Nov 12 2026** at about **0.21M PENDLE**, and larger dates on **Dec 24 2026** and **Dec 31 2026** just after it. Third, the governance treasury at **19.75M PENDLE**, which has been sending reward funding every few weeks and exchange transfers about every four months. Fourth, the buyback destination: if bought PENDLE were ever burned or locked outside the float instead of paid to stakers, Buy #1 would turn on. Fifth, the next team payment, expected around late October 2026.

## Summary

The MrNasdog Pressure Framework reads PENDLE at **+1.50%** over the trailing 90 days and **+0.82%** projected forward: supply growing, projected to keep growing. Pendle minted nothing and burned nothing, yet **2.60M PENDLE** reached the market from the governance treasury, the team wallet and expiring vePENDLE locks, while a buyback of **0.98M PENDLE** removed none because it pays liquid stakers. The key risk is the unclaimed emission of **9.51M PENDLE**, which one wallet can mint without a vote. There is no hard cap: total supply is **281.53M PENDLE** today and the contract keeps accruing about 2% a year until someone claims it.

MrNasdog Pressure Framework analysis of PENDLE, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 23 2026.

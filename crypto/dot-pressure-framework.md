---
title:         "DOT Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description:   "Polkadot minted 13.94M DOT in 90 days under its new 2.1B hard cap and destroyed nothing at all — framework reads +0.82% net, monitor +0.63%, gap 0.19pp."
canonical_url: "https://mrnasdog.com/research/dot/inflation"
tags:          ["crypto", "dot", "polkadot", "layer1"]
published:     true
---

> Originally published at **[mrnasdog.com/research/dot/inflation](https://mrnasdog.com/research/dot/inflation)** by MrNasdog.

Polkadot minted **13.94M DOT** over the last 90 days and destroyed **nothing at all**, a net **+0.82%** of the **1.70B** circulating supply, against our own monitor at **+0.63%** — a gap of **0.19** percentage points, well inside tolerance, so there is no data conflict to flag. Polkadot is now a hard-capped nominated-proof-of-stake network: a **Mar 2026** governance vote fixed a permanent ceiling of **2.1B DOT** and cut annual issuance **53.6%**, to a stepped curve that issues **13.14%** of the remaining gap every two years. The same round of votes switched every burn off, so DOT supply is slow, bounded and strictly one-directional.

## The verdict, in one paragraph

Over the 90 days to **Sep 4 2026** the Polkadot sell ledger totals **13.94M DOT** and the buy ledger is **zero**, for a net of **+0.82%** against a circulating supply of **1,701,217,240 DOT**. Our inflation monitor, measuring the same network from the opposite direction, reads **+0.63%**; the gap of **0.19** percentage points is inside the half-point tolerance, so no warning chip is shown. Getting that agreement required reading the right chain. Polkadot moved every DOT balance off its relay chain in **Nov 2025**, and the relay supply counter now holds just **241,007 DOT** — a residual worth **0.014%** of the real figure. A build that reads the historic relay key alone would report a Polkadot supply four orders of magnitude too small. Read correctly, DOT is **mildly inflationary on a capped float with no downward lever**.

## Sell pressure: where new DOT comes from

One mechanism supplies all of it. Polkadot has no mining, no halving and no unlock calendar; new DOT is minted by the protocol as a staking and network-security subsidy, and since **Mar 14 2026** the size of that subsidy has been a fixed annual quantum rather than a percentage of stake. The rule the network adopted issues **13.14%** of the distance still left to the **2.1B** ceiling, recalculated once every two years — the first step cut annual issuance from roughly **120M** DOT to about **56M**. Measured directly from the supply counter on Polkadot Asset Hub, the chain that now holds every DOT balance, issuance over the window was **13.94M DOT**, or about **3.32%** a year. That is Sell #1, and it is the entire sell side.

The pace is remarkably steady. Ten readings of the Polkadot supply counter across the window all land within **9 DOT** a day of **153,137** — the emission is time-indexed, paid per era rather than per block, so the chain running faster or slower changes nothing. That flat line is what makes the next-90-day figure of **13.79M DOT** a projection rather than a guess: the annual quantum does not move again until **Mar 2028**. A **Jul 3 2026** vote did re-cut how the mint is shared out — **45.2%** to staker rewards, **22.6%** to a validator self-stake incentive and **32.2%** parked in a buffer — and the per-era validator payout duly halved, but the supply counter never flinched. Distribution changed; issuance did not.

The other three sell rows are zero, and each for a structural reason. Vesting unlocks are zero because the Polkadot launch distribution is fully released — on-chain vesting schedules still exist across **1,054** accounts, but those coins were minted years ago and already sit inside the counted float, and the locked total rose across the window rather than draining. Foundation and unscheduled unlocks are zero because every identified protocol pool ended the window larger than it started. Long-term locked or bankruptcy is zero because Polkadot has never been through an insolvency and there is no estate to distribute.

## Buy pressure: where new DOT goes

Nowhere. All four Polkadot buy rows read **zero**, and this is the single most important fact about DOT supply today. Programmatic buyback is zero: Polkadot operates no buyback contract, no treasury market-purchase mandate, and no vote has proposed one. Foundation buy is zero: no Foundation or Labs entity has disclosed a DOT purchase programme, and the only identified pools on the chain are protocol accounts that received newly minted DOT rather than buying any. New long-term lock is zero: bonded DOT already sits inside the counted float, and after the **2026** staking reforms nominators are exempt from slashing with an exit measured in a day or two, so staking no longer resembles a lock at all.

Protocol fee burn is the row that changed, and it changed decisively. Polkadot used to destroy unspent treasury funds at the end of every spend period, and an earlier design burned coretime sales revenue outright. A **Mar 2026** referendum switched all of that off: treasury burns halted, and transaction fees, coretime sales revenue and slashed stake now route into a governance-controlled allocation pool instead of being destroyed. We checked both places a burn can possibly show up. The supply counter, read at both ends of the window and at eight points in between, only ever rose — no interval fell. The network unspendable address moved by **1.78 DOT** of dust in 90 days. Neither surface shows destruction, and the governance record explains why: on Polkadot in **2026**, DOT is not burned, it is reallocated.

## Foundation and overhang

Two protocol-controlled pools hold DOT with no fixed release date, and both were read directly at each end of the window. The on-chain Polkadot Treasury rose from **23.42M DOT** to **24.31M DOT**, spending through open governance but taking in more than it paid out. The new allocation buffer rose from almost nothing to **3.71M DOT**, filling once the **Jul 3 2026** vote began routing a **32.2%** share of issuance into it instead of paying it out to stakers. The two balances close cleanly against an independent measure of protocol-held DOT, with a residual of just **1.02 DOT** on a combined change of **4.61M** — the arithmetic is real, not asserted.

Beyond those, the Web3 Foundation genesis allocation has no published wallet set, so it can only be tracked through official disclosure rather than by reading a balance, and the legacy per-account vesting schedules described above sit in the same watch bucket. None of these carries a value in the ledger today, because capacity is not cadence. The trigger is simple: if the Polkadot Treasury balance or the allocation buffer falls between refreshes, that outflow enters Sell #3 at the next refresh. The buffer is the one to watch, because it is filling at roughly a third of every newly minted DOT and nothing in the current rules obliges governance to hold it.

## How DOT compares to other capped proof-of-stake chains

Polkadot now sits in an unusual structural slot: a hard-capped chain with a stepped, schedule-driven issuance curve, but no burn of any kind. Compare that to the halving-model chains, where a fixed cap is enforced by a block subsidy that halves on a fixed block count — those are block-indexed, so a chain running fast or slow shifts the emission date. Polkadot is time-indexed instead, a fixed annual quantum dripped per era, which is why its supply line is almost perfectly straight and why a projection out 90 days is reliable rather than approximate. Both designs end at a ceiling; only one of them tells you exactly what next quarter looks like.

Against the uncapped continuous-emission layer ones, DOT is the more disciplined structure on paper — a permanent **2.1B** ceiling versus an open-ended float — but the comparison flips on the buy side. Chains that pair issuance with a fee burn can and do run net deflationary in busy quarters, because usage removes coins. Polkadot removes nothing, by design and by governance choice: the burn was switched off in favour of reallocation, so no amount of network activity can pull DOT supply down. It is the mirror image of an exchange token with a quarterly buyback, where revenue converts directly into coins destroyed. DOT converts revenue into a governed balance instead, which is a policy lever rather than a supply sink.

The practical consequence is that Polkadot inflation is now a governance variable, not a market one. Two of the three numbers that decide DOT supply — the annual quantum and the allocation split — are set by vote, and the third, the **2.1B** cap, is also a vote that could in principle be revisited. That is a genuinely capped asset with a soft ceiling, and it prices differently from a capped asset with a hard one.

## What to watch in the next 90 days

First, the allocation buffer balance. It went from empty to **3.71M DOT** in a single quarter; the moment governance directs an outflow to the market, that outflow becomes real Polkadot sell pressure and enters Sell #3. Second, any follow-up to the **Jul 3 2026** budget vote — the split between staker rewards, validator incentive and buffer is now a routine governance parameter, and each re-cut changes who receives the mint even though it never changes its size. Third, the Phase 2 work on the allocation pool, which contemplates separate governed outflow tracks and a strategic reserve; that is the change that would give DOT a downward lever for the first time since **Mar 2026**.

Fourth, the DAO expression of support for burning the full DOT proceeds of any future ecosystem token sale — conditional, undated and without a quantum today, but the only live proposal anywhere in Polkadot governance that would actually destroy DOT. Fifth, the next issuance step itself, which lands on **Mar 14 2028** and will recompute the annual quantum as **13.14%** of whatever gap to **2.1B** remains — far outside this window, but it is the date that bounds every DOT supply projection until then.

## Summary

The MrNasdog Pressure Framework reads Polkadot as mildly inflationary and completely one-directional: **13.94M DOT** minted over 90 days, **zero** destroyed, a net of **+0.82%** of a **1.70B** circulating supply, projected at **+0.81%** for the next 90 days. The structural mechanism is a fixed annual issuance quantum under a permanent **2.1B** hard cap, cut **53.6%** in **Mar 2026** and unchanged until **Mar 2028**, which makes DOT supply unusually predictable. The key risk is that Polkadot has no burn at all — the treasury burn, the fee burn and the coretime revenue burn were all switched off in favour of a governed allocation pool, so nothing the network does can reduce DOT supply, and a growing pool of protocol-held DOT is now a governance decision away from becoming sell pressure. The ceiling is real; the floor is a vote.

---

*MrNasdog Pressure Framework analysis of DOT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 5 2026.*

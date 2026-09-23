---
title:         "MON Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "MON supply is growing: +3.33% in 90 days from block rewards and Foundation payouts, and +143.80% next as a 16.6B MON vesting cliff unlocks on Nov 24 2026."
canonical_url: "https://mrnasdog.com/research/monad/inflation"
tags:          ["crypto", "mon", "monad", "layer1"]
published:     true
---

Originally published at [MON Inflation Analysis · September 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/monad/inflation).

# MON Inflation Analysis · September 2026 · Supply growing · projected to keep growing

Monad's tradable MON supply is growing now and is set to more than double in the next 90 days. The Pressure Framework reads MON at **+3.33%** over the last 90 days — **425.0M MON** of sell pressure from block rewards and Foundation payouts against **31.3M MON** of base-fee burn — and at **+143.80%** for the next 90 days, because a one-year vesting cliff on** Nov 24 2026** unlocks **16,609.0M MON** for the team, investors and the Category Labs treasury. The monitor reads** +0.25%**. MON has no hard cap: 18 new MON are minted with every block.

## The verdict, in one paragraph

Against a circulating base of **11,825.2M MON**, the framework books **425.0M MON** of sell pressure and** 31.3M MON** of buy pressure over the trailing 90 days, a net of **+3.33%**, and projects **+143.80%** for the next 90 days. The inflation monitor reads **+0.25%** for the same window, a gap of **3.08 percentage points**. That is over the 0.5-point tolerance, so the overview ships with a monitor-gap warning. The gap has one clear cause: the monitor's supply figure is the Monad Foundation's public-float count as of **Mar 31 2026**, which has sat at 11,825.2M MON since mid-April and cannot register new block rewards or Foundation payouts. Its +0.25% is day-to-day price noise around that fixed number. MON is a young proof-of-stake chain with a small float and a large lock about to open.

## Sell pressure: where new MON comes from

Sell #1, protocol inflation, is **177.1M MON**. Every Monad block credits the staking system with new MON: exactly** 25 MON** per block until **Jul 23 2026**, and **18 MON** since, when the MIP-12 upgrade cut block time from 400 to 300 milliseconds and scaled the reward down with it. Across the window that minted **469.5M MON**. The Monad Foundation delegates **10,910.0M MON** through 20 staking wallets, and those wallets claimed and kept **292.3M MON** of the reward — the claims, the withdrawals and the wallet balances add up exactly — so only 177.1M MON reached independent stakers and node operators. At the current block rate the next 90 days mint about 462.2M MON, of which about** 182.3M MON** reaches the float.

Sell #2, vesting unlocks, is **0** for the last 90 days: the locked team and investor wallets did not move. It is** 16,609.0M MON** for the next 90. Monad's public mainnet launched on **Nov 24 2025**, and every team, investor and Category Labs treasury token was locked for one year. On **Nov 24 2026** investors receive 12/48 of their 19,683.2M MON (**4,920.8M**), the Category Labs treasury receives 12/48 of 3,952.8M MON (**988.2M**), and the team receives the vested portion the project puts at about 10.7% of initial supply (**10,700.0M**). That single day is larger than the entire 11,825.2M MON float. Monthly unlocks follow from Dec 24 2026, just outside this forecast, until late 2029.

Sell #3, Foundation and unscheduled unlocks, is **247.9M MON**. The Foundation's main wallet, holding** 17,136.1M MON** — more than the whole float, so it cannot be part of it — sent 250M MON to a set of payout wallets that pay recurring batches to outside wallets. Net of 30M MON that came back, 247.9M MON left the Foundation in the window; one of those payout wallets alone sent out 375.1M MON in the 90 days before, so the same run rate is projected forward. Sell #4, long-term locked or bankruptcy, is **0**: MON has no estate, trustee or court-ordered distribution.

## Buy pressure: where new MON goes

Buy #1, programmatic buyback, is **0**. The protocol has no buyback. Category Labs has said it may buy up to $80M of MON on the open market by the end of 2026, but it has not disclosed a single purchase, amount or wallet, so nothing is counted.

Buy #2, protocol fee burn, is **31.3M MON**. Monad charges each transaction its full gas limit, and the base part of that fee is destroyed; the block producer receives only the tip, which a direct balance read of producers confirms. Across 23,695 sampled blocks the burn averaged 1.19 MON per block before the upgrade and 1.37 MON after, and it has been rising as the chain gets busier. Small transfers to dead addresses add under 0.1M MON. The forward burn is about **35.1M MON**, which offsets less than a tenth of the new block rewards alone.

Buy #3, Foundation buy, is **0**. In Aug 2026 the Monad Foundation offered early investors up to $60M for their locked MON; nearly all declined, and any tokens it did buy stay locked on the original schedule, so no MON left the market. Buy #4, new long-term lock, is **0**: staked MON can be withdrawn after one epoch of a few hours, and locked tokens cannot be staked.

## Foundation and overhang

The overhang on MON is the largest thing about it. First, the locked team, investor and Category Labs buckets: about 50.6B MON at launch, sitting in quiet custody wallets that did not move in the window. After the Nov 24 2026 cliff roughly 34.0B MON remains to unlock monthly through late 2029. Second, the Foundation's ecosystem allocation, 38.2B MON at its last official count on Mar 31 2026: the 17,136.1M MON main wallet, the 10,910.0M MON staked through its 20 delegation wallets, and the rewards those wallets have claimed and kept. Third, the locked investor MON the Foundation bought in Aug 2026, which unlocks into Foundation hands; its size was never published.

Every one of these balances is read from the chain at each rebuild. The rule is simple: if the Foundation's main wallet, its staking wallets or the payout wallets lose more than the payouts already counted, that outflow enters Sell #3 at the next refresh.

## How MON compares to other proof-of-stake Layer 1 chains

On issuance alone, MON is moderate. Its 18 MON per block works out to about 1.9B MON a year, roughly 1.9% of total supply, which is lower than many staking chains that pay 5% or more to keep validators. Like Ethereum, Monad burns the base fee, but Monad's burn is still far smaller than its issuance, so it does not make supply shrink the way a busy Ethereum period can.

The real difference is the float. Most large chains launched years ago and have finished their insider vesting. MON launched in Nov 2025 with only about a tenth of its supply trading, and the Pressure Framework measures supply against that tradable float, not against the 100.7B total. That is why a one-year cliff that frees about 16.5% of total supply reads as more than 140% of the market. MON looks less like a mature proof-of-stake chain and more like a new token at the start of a four-year vest, with a large Foundation treasury paying out on top.

## What to watch in the next 90 days

First, **Nov 24 2026**: the one-year cliff releases 16,609.0M MON, and the investor and team custody wallets become spendable. Second, the Foundation payout wallets, which sent out 247.9M MON in the last 90 days; a faster pace raises the reading. Third, any Category Labs purchase under its $80M approval — the first disclosed buy with a wallet would count as buy pressure. Fourth, the base-fee burn, which is rising with activity but would need to grow many times over to offset block rewards. Fifth, **Dec 24 2026**, the first monthly unlock after the cliff, just past this forecast window.

## Summary

The MrNasdog Pressure Framework reads MON at **+3.33%** over the trailing 90 days and **+143.80%** projected forward: supply growing, projected to keep growing. Today the pressure comes from block rewards and Monad Foundation payouts, only partly offset by the base-fee burn. The key risk is the Nov 24 2026 cliff, which unlocks 16,609.0M MON — more than the whole current float — for the team, investors and Category Labs. There is no hard cap on MON; about 34.0B more locked MON follows monthly through late 2029.

MrNasdog Pressure Framework analysis of MON, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 23 2026.

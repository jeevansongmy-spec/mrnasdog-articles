---
title:         "CFX Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "CFX supply grows a steady 0.43% per 90 days: Conflux mints 22.70M CFX to miners and stakers while fee and storage burns remove 0.0073M. No cap, no buyback."
canonical_url: "https://mrnasdog.com/research/cfx/inflation"
tags:                    ["crypto", "cfx", "conflux", "layer1"]
published:     true
---

Originally published at [CFX Inflation Analysis · September 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/cfx/inflation).

# CFX Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

Conflux adds new CFX at a slow, steady pace: the MrNasdog Pressure Framework reads CFX at **+0.43%** over the trailing 90 days and **+0.43%** for the next 90. The whole reading comes from two protocol mints — a proof-of-work block reward for miners and staking interest paid in new coins — which created **22.70M CFX**, against fee and storage burns of just **0.0073M CFX**. Every launch lock has expired, there is no buyback, and Conflux has no supply cap: the pace is set by on-chain holder votes, and the vote now pending on a further miner-reward cut is far short of the turnout it needs.

## The verdict, in one paragraph

Against a circulating base of **5,241.4M CFX**, the framework books **22.70M CFX** of sell pressure and **0.0073M CFX** of buy pressure over the trailing 90 days — a net of **+0.43%** — and projects **+0.43%** for the next 90 days, because neither mint rate changed inside the window and no change is due to take effect. The inflation monitor reads **+0.51%** for the same window, a gap of **0.08 percentage points**, well inside the framework's 0.5-point tolerance, so the CFX overview ships with no monitor-gap warning. The label for CFX is **a low, steady emission chain**: new supply arrives on every block, in small amounts, and nothing on the buy side comes close to offsetting it.

## Sell pressure: where new CFX comes from

Sell #1, protocol inflation, is **22.70M CFX**, and it is the only row that is not zero. Conflux pays two groups in freshly created CFX. Miners earn a fixed reward on every block, which a holder vote halved on **Apr 7 2026** to about **0.40 CFX** a block; with Conflux producing roughly two blocks a second, that added **6.25M CFX** over the window. Stakers earn interest paid in new coins, at a rate that rises as more CFX is staked; that added **16.46M CFX**, more than twice the mining share. The chain's own count of CFX in existence rose from **5,791.8M** to **5,814.5M** across the 90 days, and a second, independent series of reward totals agrees with that rise to within about 0.04%. The pace held steady the whole way, including through the Conflux v3.1.0 network upgrade on **Aug 25 2026**, which changed no reward setting.

Sell #2, vesting unlocks, is **0**. The launch allocations — the team, early investors, the ecosystem and community funds — finished unlocking in 2024, and both locked buckets read zero on chain at both ends of the window. Sell #3, foundation and unscheduled unlocks, is also **0**, for a specific reason explained in the overhang section below: the coins the foundation moves are already counted as circulating. Sell #4, long-term locked or bankruptcy, is **0**; there is no bankruptcy estate or court-ordered payout attached to CFX.

## Buy pressure: where new CFX goes

Buy #1, programmatic buyback, is **0**. Conflux has no programme that spends money buying CFX on the market. The last large supply cut was a burn, not a purchase: in May 2025 the Conflux Foundation destroyed **76M CFX** it already held, after a community vote, and nothing like it happened in this window.

Buy #2, protocol fee burn, is **0.0073M CFX**, and it has two parts. Under the Conflux version of the base-fee design, part of every transaction's base fee is destroyed — **2,323 CFX** over 90 days. And when CFX is paid to reserve contract storage, part of it is converted into storage points and destroyed — **5,009 CFX**. Both burns come straight off the chain's count of CFX in existence. The address that holds past burns, now **573.0M CFX**, received nothing in the window, so no extra burn hides there. Put together, Conflux destroys about one coin for every 3,100 it creates.

Buy #3, foundation buy, is **0**: the foundation's fund contracts only paid coins out. Buy #4, new long-term lock, is **0** as well. Staked CFX grew from **901.0M** to **976.1M**, but staked CFX can be withdrawn and is already counted as circulating, so staking takes nothing off the float.

## Foundation and overhang

The Conflux overhang is large on paper. Four foundation fund contracts hold about **2,314M CFX** between them — close to half the circulating supply — and in this window they paid a net **71.2M CFX** to the foundation's operating wallet, roughly once a month, from where coins moved on into staking and to other accounts. The foundation also keeps a stake of roughly **500M CFX** placed in May 2025, whose rewards were set aside for at least two years. Their balances are read on chain at every rebuild.

None of this counts as new sell pressure, and that is deliberate. The circulating figure for CFX already includes every one of these wallets — the only CFX left out is the burned balance — so a foundation payout changes who holds the coins, not how many are out. The trigger still applies: if CFX ever moves from outside the counted float into it, or the counted float is redrawn to exclude these funds, that release enters Sell #3 at the next refresh.

## How CFX compares to other proof-of-work and proof-of-stake chains

CFX sits between two familiar models. Like Bitcoin, Conflux pays miners a block reward, but it has no halving clock and no hard cap; the reward changes only when holders vote, and the April 2026 vote cut it by half in one step. Like uncapped proof-of-stake Layer-1s, Conflux pays stakers interest in new coins, and on CFX that staking stream is now the larger mint by more than two to one. The result is an annual pace near **1.8%** of circulating supply — lower than most staking-led Layer-1s, higher than a late-cycle halving chain.

On the burn side, Conflux looks like Ethereum on paper — a base-fee burn plus a storage burn — but it lacks the transaction volume to make the burn matter. Ethereum-style chains can burn more than they mint in busy periods; Conflux burned about **0.03%** of what it minted in this window. And unlike exchange tokens that run scheduled buybacks, Conflux has no demand-linked removal at all, so its net reading tracks its mint almost exactly.

## What to watch in the next 90 days

First, the on-chain vote round that closes on **Oct 4 2026**. Its ballot leans toward cutting the miner reward again, but only about **16,667 CFX** of votes were cast against a minimum turnout of roughly **42.2M**, so under the chain's own rules the reward stays where it is. Second, the round now open, which takes effect around **Dec 3 2026**; so far it holds only votes to keep every setting unchanged, and a late wave of votes to cut would trim the last few weeks of this forecast. Third, the amount of CFX staked, which drives the staking interest and has been rising. Fourth, the four foundation fund contracts at about **2,314M CFX** and their monthly payouts. Fifth, the burn-holding address at **573.0M CFX**, which moves only when the foundation or holders choose to destroy coins.

## Summary

The MrNasdog Pressure Framework reads CFX at **+0.43%** over the trailing 90 days and **+0.43%** projected forward: mixed flows, supply roughly steady. Conflux creates new CFX on every block through a miner reward and staking interest — **22.70M CFX** a quarter — while its fee and storage burns remove only **0.0073M CFX**. The key risk is that CFX has no supply cap, so the pace depends entirely on holder votes and on how much CFX is staked; the key comfort is that every launch lock is gone and the pending vote to cut the miner reward again cannot pass on its current turnout.

MrNasdog Pressure Framework analysis of CFX, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 22 2026.

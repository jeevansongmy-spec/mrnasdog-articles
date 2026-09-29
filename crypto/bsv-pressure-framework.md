---
title: "BSV Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description: "BSV is mildly inflationary: mining issued 40,375 BSV in 90 days with no burn or buyback, +0.20% net, the same next. No vesting, no treasury, 21M hard cap."
canonical_url: "https://mrnasdog.com/research/bsv/inflation"
tags: ["crypto", "bsv", "bitcoin-sv", "proof-of-work"]
published: true
---

> Originally published at **[mrnasdog.com/research/bsv/inflation](https://mrnasdog.com/research/bsv/inflation)** by MrNasdog.

# BSV Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

Bitcoin SV (BSV) supply grows slowly and from one place only: mining. In the 90 days to Sep 29 2026, miners found **12,920 blocks** and each paid a reward of **3.125 BSV**, which added **40,375 BSV** to a circulating supply of **20.09M BSV** — a net **+0.20%**, with nothing burned or bought back. The next 90 days should look the same, because the next BSV halving does not arrive until block 1,050,000, around April 2028, and the 21M hard cap is already **95.7%** mined.

## The verdict, in one paragraph

The MrNasdog Pressure Framework reads BSV supply at **+0.20%** over the last 90 days and projects **+0.20%** for the next 90 days. Our inflation monitor, which reads supply changes independently, shows **+0.21%** for the same stretch. The gap between the two is **0.01 percentage points**, well inside our 0.5-point tolerance, so no warning flag is shown. The label for Bitcoin SV is simple: **a quiet, mining-only chain with a fixed schedule**. New BSV enters the market at a steady pace, and no mechanism on the Bitcoin SV network takes any of it back out.

## Sell pressure: where new BSV comes from

Protocol inflation is the only live row. Bitcoin SV is a proof-of-work chain, and every block pays its miner a fixed subsidy — **3.125 BSV** in the current halving era, which began at block 840,000 in 2024. We counted the blocks on-chain rather than assuming the ten-minute target: block 955,911 was the first of the window on Jul 1 2026 and block 968,830 the last on Sep 29 2026, so **12,920 blocks** landed, about 144 a day. The chain ran a little slow — each block took about 602 seconds on average — so the real figure of **40,375 BSV** sits just under what a round 144 blocks a day would give. We also checked the reward itself: every 20th block across the window paid its miner exactly 3.125 BSV plus that block's fees, with nothing left unclaimed.

Vesting unlocks are **0**, and they always will be. Bitcoin SV split from Bitcoin Cash in November 2018 and carries the same coin history back to Bitcoin's first block in 2009; there was no premine, no token sale and no team allocation, so there is nothing to vest. Foundation and unscheduled unlocks are also **0**: no project treasury holds BSV for later release. The long-term locked or bankruptcy row is **0** too. One bankruptcy estate is reported to hold about **142.8K BSV** from the 2018 split and plans to sell it for cash, but those coins already count as circulating, so a sale would move existing BSV between owners rather than add new BSV to the market.

## Buy pressure: where new BSV goes

Every buy row is **0**. There is no programmatic buyback: no contract, company or treasury buys BSV off the market on behalf of the network. There is no protocol fee burn: transaction fees on Bitcoin SV go to the miner who finds the block, on top of the subsidy, so fees add to what miners can sell rather than removing BSV. Across the window the average block in our sample carried only about 0.008 BSV in fees, tiny next to the 3.125 BSV reward.

We also read three well-known unspendable addresses, where coins sent are lost forever. Together they took in only **0.0057 BSV** in 90 days — far too small to count as a burn. There is no foundation buy, and no new long-term lock: BSV has no staking, because proof-of-work mining is secured by computing power, not by locked coins. So the Bitcoin SV buy side is empty by design, and the supply number is simply the block count times the reward.

## Foundation and overhang

Bitcoin SV has no team-controlled overhang that we can identify. The BSV Association supports development, but no treasury wallet holding BSV for release has been published, and no team wallet is tracked. The biggest named holder outside ordinary investors is the bankruptcy estate mentioned above, with about **142.8K BSV**; its creditor deadline is Oct 31 2026, and no sale date has been set. Almost all BSV already counts as circulating — only about **234 BSV** of total supply sits outside that count — so no large wallet can release coins that are not already in the market. We re-check these holders on every rebuild; if a team-controlled balance ever appears and starts to fall, that outflow enters the foundation and unscheduled unlocks row at the next refresh.

One Bitcoin SV feature is worth knowing. The network supports Digital Asset Recovery, a process where a valid court order can freeze coins and move them to their lawful owner. That changes who owns BSV, not how much exists, and we found no such order taking effect in this window.

## How BSV compares to other proof-of-work chains

BSV follows the same halving schedule as Bitcoin (BTC) and Bitcoin Cash (BCH): a 21M hard cap, a block reward that halves every 210,000 blocks, and the same 3.125 coin reward today. All three were one chain until 2017 and 2018, so the circulating supply and the yearly issuance rate of each sit close together, near 0.8% a year. What separates BSV is the block pace. Bitcoin SV miners found slightly fewer than 144 blocks a day in this window, so BSV issuance ran a touch under its nominal rate, while each chain's difficulty adjusts to its own hash power.

Against uncapped proof-of-stake chains, the difference is structural. A staking coin pays new coins to validators with no end date, and some offset part of it with a fee burn. BSV has neither a burn nor a tail: its issuance falls by half at each halving and stops near 21M. Against proof-of-work coins with a permanent tail emission, such as privacy coins that pay a fixed small reward forever, BSV issuance keeps shrinking toward zero instead. For a holder, the Bitcoin SV supply story is fully written in advance — the open question is demand, not supply.

## What to watch in the next 90 days

First, the block pace: if hash power leaves Bitcoin SV and blocks slow further, the next-90-day figure of **40,375 BSV** will come in a little lower, and a faster pace would push it a little higher. Second, the bankruptcy estate's creditor deadline on **Oct 31 2026**: a sale of its BSV would add selling in the market, although it would not add new coins. Third, the Teranode node software, now in public beta releases; a mainnet switch is not scheduled, and it changes capacity, not the block reward. Fourth, any court-ordered freeze under Digital Asset Recovery, which would move coins between owners without changing supply.

## Summary

Bitcoin SV is mildly and predictably inflationary: **40,375 BSV** of new mining rewards in 90 days against zero burn and zero buyback gives a net **+0.20%**, and the same is projected for the next 90 days. The mechanism is a fixed proof-of-work subsidy of 3.125 BSV per block, with no vesting, no treasury and no staking. The main supply-side risk is not new coins but existing ones changing hands, such as a bankruptcy estate selling about 142.8K BSV. The ceiling is the 21M hard cap, of which 95.7% is already mined, and the next halving near April 2028 cuts new supply in half again.

---

*MrNasdog Pressure Framework analysis of BSV, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

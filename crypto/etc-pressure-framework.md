---
title:         "ETC Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "Supply growing: ETC reads +0.63% over 90 days and +0.60% next. Mining is the only new supply, the block reward fell 20% on Jul 22 2026, and nothing is burned."
canonical_url: "https://mrnasdog.com/research/etc/inflation"
tags:          ["crypto", "etc", "ethereumclassic", "mining"]
published:     true
---

Originally published at [ETC Inflation Analysis · September 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/etc/inflation).

# ETC Inflation Analysis · September 2026 · Supply growing · projected to keep growing

Ethereum Classic (ETC) is mildly inflationary, and the only reason is mining. Over the 90 days to Sep 29 2026 the ECIP-1017 block reward created **998,747 ETC**, about **+0.63%** of the **158.32M ETC** in circulation, and nothing was burned, bought back or locked. The reward per block fell 20% on **Jul 22 2026**, so the next 90 days should bring about **942,243 ETC**, or **+0.60%** — and the whole supply is capped near 210.7M ETC by a schedule that cuts the reward every 5,000,000 blocks.

## The verdict, in one paragraph

The MrNasdog Pressure Framework reads ETC at **+0.63%** net supply growth over the last 90 days and **+0.60%** for the next 90 days. The inflation monitor reads **+1.23%**, a gap of **0.60 points**, which is above our 0.5-point line, so the Ethereum Classic page carries a monitor-gap note. We walked the gap and it is explained: the monitor's supply reading stood still near 156.5M ETC from early May until it caught up by about 932K ETC in one day on Jul 17 2026, so its starting figure sits too low. Our number is the chain's own mining reward, counted block by block, and it stays. In one line: Ethereum Classic is a **capped proof-of-work chain with falling, fully public issuance and no burn**.

## Sell pressure: where new ETC comes from

Protocol inflation is the whole sell side. Every Ethereum Classic block pays its miner a fixed reward in new ETC, and when a miner includes an uncle block — a valid block that lost the race — both the uncle's miner and the including miner get an extra 1/32 of the reward. The window ran from block 24,862,860 to block 25,436,595 (Jul 1 to Sep 29 2026). The first 137,140 blocks paid 2.048 ETC each; at block 25,000,001 on Jul 22 2026 the chain entered its sixth era and the reward fell to 1.6384 ETC for the remaining 436,595 blocks. We counted uncles on every block in the window: **23,707** of them, about one block in 24. Blocks plus uncles created **998,747 ETC**.

For the next 90 days we use the new reward only, because the cut happened inside the window. At the block time the chain has actually kept since Jul 22 2026, about 13.56 seconds, 90 days hold roughly 573,600 blocks. At 1.6384 ETC each, plus uncles at the recent rate, that is about **942,243 ETC**. The next cut, to 1.31072 ETC, comes at block 30,000,001, roughly two years away.

Vesting unlocks are **0**: Ethereum Classic has no vesting schedule at all. The coins created at the 2015 genesis were spendable from the first block, and there has never been a team or investor allocation that unlocks over time. Foundation and unscheduled unlocks are **0** because no foundation, company or DAO holds a reserve outside the float — total supply is only 348 ETC above circulating supply. Long-term locked or bankruptcy supply is **0**: there is no estate, trustee or unwinding lock releasing ETC.

## Buy pressure: where new ETC goes

Nothing takes ETC off the market. There is no programmatic buyback (**0**): Ethereum Classic has no protocol revenue that buys coins. There is no protocol fee burn (**0**): the chain never adopted a burned base fee, and every transaction fee goes to the miner. We read the two best-known burn addresses at both ends of the window; together they gained only about 1.1 ETC from ordinary sends, and those coins still count in the supply. There is no foundation buy (**0**), and no new long-term lock (**0**): ETC is mined, not staked, so no staking contract pulls coins out of the float.

The planned Olympia upgrade would add a base fee to Ethereum Classic, but it would send that fee to an on-chain treasury rather than destroy it. So even when it goes live, it would not add a burn to this ledger.

## Foundation and overhang

Ethereum Classic has no team-controlled overhang. Total supply sits only 348 ETC above circulating supply, so no wallet bigger than that can hold coins outside the float. The largest single holder we track is a US investment trust with about **10.85M ETC** at Jun 30 2026; it holds coins already counted as circulating, does not redeem shares, and slowly pays its fees in ETC, so it moves coins inside the float rather than adding new ones. The Olympia treasury does not exist yet. We check these holders on every rebuild, and if a reserve outside the float ever appears and its balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How ETC compares to other proof-of-work chains

Among proof-of-work coins, Ethereum Classic sits between Bitcoin and Monero. Like Bitcoin, ETC has a hard ceiling and a reward that steps down on a fixed block count; unlike Bitcoin's 50% halving every 210,000 blocks, ETC cuts 20% every 5,000,000 blocks, so each ETC cut is smaller and the issuance curve is flatter and longer. Monero goes the other way: after its main emission ended it pays a small fixed tail reward forever, so it has no cap at all.

Against Ethereum, the chain it split from in 2016, the gap is about the fee burn and the security model. Ethereum pays stakers in new coins and burns part of every fee; Ethereum Classic pays miners, burns nothing, and has no staking. That makes ETC's supply reading simpler: issuance is the whole story, and it is set by code and the block count, not by how much the network is used.

One more difference matters for the numbers. ETC pays a reward per block, not per unit of time, so if miners leave and blocks slow down, fewer ETC are created, and if blocks speed up, more are. Over this window blocks came about every 13.56 seconds, and our forward figure uses that pace.

## What to watch in the next 90 days

First, whether the Olympia upgrade gets a mainnet block number; it would add a base fee paid into a treasury, which changes who receives fees but not the number of ETC created. Second, the client dispute that began on Sep 14 2026, when a new node release was pushed and mining pools rolled back to the older version the next day; a split in the software could matter for the chain even though no coins were lost. Third, the block time: a big move in mining power would change how many blocks, and so how many ETC, fit into 90 days. Fourth, the uncle rate, now about 4.2% of blocks, which adds a little to issuance. The next community call is set for Oct 2 2026.

## Summary

Ethereum Classic (ETC) adds about **0.63%** to its supply every 90 days, all of it new coins paid to miners under the ECIP-1017 schedule, and nothing is burned, bought back or locked. The Jul 22 2026 reward cut lowers the next 90 days to about **+0.60%**. There is no vesting, no foundation reserve and no team overhang, so the main risk to this reading is a change in block time or a new upgrade rather than a hidden unlock. The supply is capped near 210.7M ETC, and each 5,000,000-block era cuts the reward by another 20%.

*MrNasdog Pressure Framework analysis of ETC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

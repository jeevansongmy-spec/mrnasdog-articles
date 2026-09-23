---
title:         "ETC Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "Supply growing: ETC reads +0.64% over 90 days and +0.60% next. Mining is the only new supply, the block reward fell 20% on Jul 22 2026, and nothing is burned."
canonical_url: "https://mrnasdog.com/research/etc/inflation"
tags:          ["crypto", "etc", "ethereumclassic", "mining"]
published:     true
---

Originally published at [ETC Inflation Analysis · September 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/etc/inflation).

# ETC Inflation Analysis · September 2026 · Supply growing · projected to keep growing

Ethereum Classic supply is growing and is projected to keep growing, but slowly and on a fixed clock. The Pressure Framework books **1.014M ETC** of new coins paid to miners and **0** removed, a net of **+0.64%** over the last 90 days and **+0.60%** projected for the next 90, while the monitor reads **+1.23%**. Proof-of-work mining is the only source of new ETC; there is no team, no vesting and no fee burn, and the ECIP-1017 schedule cut the block reward by 20% on **Jul 22 2026** on the way to a ceiling near **210.7M ETC**.

## The verdict, in one paragraph

Against a circulating base of **158.26M ETC**, the framework books **1.014M ETC** of sell pressure and **0** of buy pressure across the trailing 90 days, a net of **+0.64%**, and projects **+0.60%** for the next 90 days at the new, lower block reward. The inflation monitor reads **+1.23%** for the same window, a gap of **0.59 percentage points**, which is over the framework's tolerance, so the overview ships with a monitor-gap note. That gap is fully explained. About **0.42 points** comes from the monitor's starting supply: its supply reading stayed near **156.5M ETC** from late April until a one-day catch-up of about **932K ETC** on **Jul 17 2026**, so its Jun 25 figure sat about **660K ETC** below the chain. About **0.16 points** is its Sep 23 2026 reading running about **252K ETC** high, and **0.01 points** is its smaller divisor. The label for ETC is **a mined chain on a shrinking, fixed reward schedule**: supply grows every block, and every block adds less than it used to.

## Sell pressure: where new ETC comes from

All of it comes from mining. Sell #1, protocol inflation, is **1.014M ETC**, and it was measured block by block rather than estimated. The Ethereum Classic chain produced **573,654 blocks** between block **24,825,772** and block **25,399,425**, the first and last blocks of the window. The first **174,229** of them paid **2.048 ETC** each. At block **25,000,001**, mined on **Jul 22 2026**, the ECIP-1017 monetary policy stepped the reward down 20%, and the remaining **399,425** blocks paid **1.6384 ETC**. On top of that, **23,697** uncle blocks each earned a small bonus of one thirty-second of the reward for the uncle miner and the same again for the block that included it, adding about **2,605 ETC**. The reward step was confirmed from the chain's own balances on both sides of the boundary.

Because the reward changed inside the window, the forward number is not a copy of the trailing one. The next 90 days run entirely at **1.6384 ETC** per block. Ethereum Classic pays per block, not per unit of time, so block speed matters: since the cut, blocks have arrived every **13.56 seconds** on average, which gives about **573,339** blocks and **0.942M ETC** of new supply through **Dec 22 2026**. The next 20% cut comes at block **30,000,001**, about two years away, well outside this forecast.

Sell #2, vesting unlocks, is **0**. Ethereum Classic has no vesting schedule: its launch coins came from the original Ethereum sale and were spendable from the first block. Sell #3, foundation and unscheduled unlocks, is **0**, because no foundation, company or DAO holds a reserve of ETC outside the float. Sell #4, long-term locked or bankruptcy, is **0**: there is no estate, trustee or court-ordered distribution tied to ETC.

## Buy pressure: where new ETC goes

Nowhere. Buy #1, programmatic buyback, is **0**. No entity collects protocol income that could pay for one. Buy #2, protocol fee burn, is also **0**, and this is the row most worth explaining because Ethereum Classic is often assumed to behave like Ethereum. It does not. Ethereum Classic never adopted EIP-1559: its block headers carry no base-fee field and every transaction fee goes to the miner. The two common burn addresses were also read at both ends of the window: they picked up **1.1 ETC** between them, all in stray sends on **Aug 5 2026**. Those addresses are still counted inside circulating supply, so even that dust never left the float.

Buy #3, foundation buy, is **0**: no foundation or company bought ETC on the market. Buy #4, new long-term lock, is **0**. Ethereum Classic is mined, not staked, so no staking contract pulls coins out of circulation.

## Foundation and overhang

There is almost no overhang to track. About **158.26M ETC** circulate out of **158.26M ETC** in existence; the difference is only about **748 ETC**. No foundation treasury, team wallet, DAO treasury or buyback wallet holds coins outside the float, and there is no bankruptcy residual. The largest single holder of note is a US investment trust with about **10.85M ETC** at Jun 30 2026, but that is investor custody already counted as circulating, so its sales would move coins within the float.

The one thing to watch is proposed rather than live. The Olympia upgrade would add a base fee and send it to a new on-chain treasury instead of burning it. It is still a draft with no activation block. If it activates and that treasury, or any newly identified team-controlled wallet, sits outside the circulating count and its balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How ETC compares to other proof-of-work chains

ETC sits in the same family as Bitcoin and Litecoin: a proof-of-work chain with a hard supply ceiling reached by cutting the block reward on a fixed schedule. The difference is the shape of the cut. Bitcoin halves its reward every 210,000 blocks, so its issuance drops by half in one step about every four years. Ethereum Classic cuts by 20% every 5,000,000 blocks, about every two years, so its issuance declines in smaller, more frequent steps. Both are written into the protocol and cannot change without a hard fork.

Ethereum Classic's current reading of **+0.64%** a quarter is higher than a mid-cycle Bitcoin, which reads a fraction of that, because ETC is at an earlier point on its curve: about **75%** of its ceiling is issued, against well over 90% for Bitcoin. Unlike staking chains with open-ended emission set by governance, ETC has no lever on issuance, so its supply path is one of the most predictable in the market.

The sharpest contrast is with Ethereum itself. Ethereum burns part of every fee and can shrink when busy; Ethereum Classic burns nothing, so no amount of activity offsets its mining issuance.

## What to watch in the next 90 days

First, the block rate: at **1.6384 ETC** per block, faster blocks mean more new ETC, so a large change in mining power would move the forward number through **Dec 22 2026**. Second, the Olympia upgrade: the fee-market proposals were revised on **Sep 8 2026** but remain drafts with no activation block; if a block is set, the new treasury becomes a balance to track, though it destroys no coins. Third, the burn addresses, where any real burn programme would show first. Fourth, the US investment trust's holding of about **10.85M ETC**, the largest identified pool, which moves within the float. The next scheduled reward cut, at block **30,000,001**, falls outside this window.

## Summary

The MrNasdog Pressure Framework reads ETC at **+0.64%** over the trailing 90 days and **+0.60%** projected forward: supply growing, projected to keep growing. The only mechanism is proof-of-work mining, which paid **1.014M ETC** in the window and will pay about **0.942M ETC** in the next 90 days after the Jul 22 2026 reward cut. The key risk is that nothing offsets it: Ethereum Classic has no fee burn, no buyback and no staking lock. The comfort is the ceiling, near **210.7M ETC**, and a reward that keeps falling by 20% every 5,000,000 blocks.

MrNasdog Pressure Framework analysis of ETC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 23 2026.

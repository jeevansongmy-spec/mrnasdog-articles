---
title:         "OKB Inflation Analysis · September 2026 · Mixed flows, supply roughly steady"
description:   "Mixed flows, supply roughly steady: OKB's fixed 21M supply saw no mint, no vesting and no burn over 90 days. Framework 0.00% net; the supply monitor agrees."
canonical_url: "https://mrnasdog.com/research/okb/inflation"
tags:          ["crypto", "okb", "okx", "layer2"]
published:     true
---

# OKB Inflation Analysis · September 2026 · Mixed flows, supply roughly steady

*Originally published at [https://mrnasdog.com/research/okb/inflation](https://mrnasdog.com/research/okb/inflation)*

OKB, the gas token of X Layer, OKX's Ethereum layer-2 chain, has a fixed supply of **21M OKB**, and nothing was added to it or taken from it in the 90 days to **Sep 25 2026**: X Layer pays no block reward, OKB vesting ended in **2018**, and the only bridge onto X Layer destroys OKB on Ethereum before it creates any, and did not run this window. On the other side, OKX ended the quarterly OKB buyback-and-burn in **2025**, and X Layer keeps its **927.58 OKB** of gas fees rather than burning them. The MrNasdog Pressure Framework therefore reads OKB at **0.00% net** over the last 90 days and **0.00%** over the next 90, against a supply-monitor reading of **−0.03%** — a gap of **0.03 percentage points**, which is agreement, not conflict.

## The verdict, in one paragraph

For the 90-day window ending **Sep 25 2026**, the Pressure Framework reads **OKB at 0.00% net**: **zero** OKB added across all four sell rows and **zero** OKB removed across all four buy rows. The independent supply monitor reads the realised 90-day change at **−0.03%**, which is rounding noise around a constant **21M** count. The gap is **0.03 percentage points**, far inside the framework's half-point tolerance, so OKB ships with **no data-conflict flag**. The forward column also reads **0.00%**, because no OKB unlock, burn or mint is scheduled between now and **Dec 24 2026**. The label for OKB is a **fixed-supply gas token holding still**: the OKB supply was cut to 21M in 2025, and since then no mechanism has added to it or taken from it.

## Sell pressure: where new OKB comes from

Nowhere, this window, and that was measured rather than assumed. Sell #1, protocol inflation, is **zero**. X Layer runs on the OP Stack and pays its block producer out of gas fees, not newly minted OKB. New OKB can appear on X Layer only two ways, and both were read at both ends of the window. The first is the bridge from Ethereum: to bring OKB across, the Ethereum OKB must first be destroyed, and the ledger that tracks those deposits held **559,344.6** units at the start of the window and exactly the same at the end. The second is a built-in reserve that the chain's mint path draws from, and it held **zero** OKB at both ends. On Ethereum, the OKB contract's live code has no mint at all; its supply figure sits in ordinary contract storage, so a flat reading there is a real measurement, and it held at **429,064.58 OKB** for the whole window. It last moved on **Mar 6 2026**, when **9,476.66 OKB** were destroyed on the way to X Layer. One caution keeps this row honest: the Ethereum OKB contract can still be upgraded by a single owner key, so the absence of a mint is a fact about today's code, not a promise.

Sell #2, vesting unlocks, is **zero**: the OKB release schedule ended in 2018, and OKB circulating supply equals the full **21M**, so no locked bucket is left to open. Sell #3, foundation and unscheduled unlocks, is **zero**. OKX's own wallets hold most OKB — its latest reserve report shows **19.75M OKB** in exchange wallets against **19.72M** of customer and company balances — but every one of those coins already sits inside the 21M circulating count, so a move or a sale adds nothing new to the float. Sell #4, long-term locked or bankruptcy supply, is **zero**: there is no estate and no long-dated OKB lock. The two ledgers were also checked against double counting: the **429,064.58** OKB still on Ethereum can each reach X Layer only once, by being destroyed first, so OKB on Ethereum plus OKB on X Layer is one supply, counted once.

## Buy pressure: where new OKB goes

OKB used to have one of the best-known burns among exchange tokens, and it is gone. In August 2025 OKX destroyed **65,256,712 OKB** from past buybacks and treasury reserves in a single burn, fixed the OKB supply at 21M and ended the quarterly buyback-and-burn. OKX's last OKB burn report covers March to May 2025, and nothing has been bought back since, so Buy #1, programmatic buyback, is **zero**. Buy #2, the protocol fee burn, is also **zero**, because X Layer does not burn gas. Users paid **927.58 OKB** in gas fees this window; those OKB went into the chain's fee accounts, which grew from start to end, and the wallet those accounts pay out to never moved. A sample of three thousand blocks across the window put fees at **829 OKB**, and an independent chain-fee series agrees in dollars, so the fee flow is real, and none of it is destroyed.

Both burn surfaces were read on both chains. On Ethereum the OKB supply did not fall and the burn address held nothing. On X Layer the two burn addresses together received **0.47 OKB** over ninety days — users sending coins where no one can spend them, too small to register against a 21M supply. Buy #3, foundation buying, is **zero**: no OKB treasury programme exists. Buy #4, new long-term locks, is **zero**. OKX has said builders will stake OKB to open trading venues on X Layer, but that step is not open yet, no stake size or contract has been published, and staked OKB would stay inside the circulating count anyway.

## Foundation and overhang

The OKB overhang that matters is OKX itself. On X Layer the largest single OKB wallet is an OKX cold wallet holding **7.11M OKB**, and a group of OKX cold wallets of roughly **1M OKB** each sit behind it; four of them have not moved since June. OKX's reserve report counts **19.75M OKB** across its wallets but does not separate the company's own OKB from what it holds for customers, so OKX's own stake is opaque and is monitored through each new report. Because OKB circulating supply already equals total supply, none of these wallets sits outside the float, and the framework books a release from them as zero rather than as new supply. Two smaller balances are tracked on the chain itself: the X Layer fee accounts, which grew this window, and the wallet they pay out to, at **12,853 OKB** and never moved. Exchange custody held for depositors is excluded by rule. If any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How OKB compares to other exchange-linked chain tokens

OKB now sits in a small class: a large token with a fixed supply and no burn. BNB, its closest structural cousin, still destroys reserve BNB every quarter and burns part of every gas fee, so BNB supply falls on a schedule; OKB made its cut once, in 2025, and then switched both mechanisms off, so OKB supply stays level. Against an uncapped proof-of-stake Layer 1, which pays validators in newly minted coins, OKB has no mint side at all. Against a capped proof-of-work coin, which still issues a block subsidy until it reaches its cap, OKB is already at its ceiling of 21M and adds nothing.

Against other rollup gas tokens the difference is in where the fees go. X Layer is built on the OP Stack, where gas is collected into fee accounts rather than destroyed — unlike Ethereum mainnet, which burns the base fee. So X Layer activity moves OKB between wallets instead of removing it. The trade-off is plain: OKB has no dilution to fight and no burn to lean on, and its supply only changes if OKX changes the rules.

## What to watch in the next 90 days

First, the Ethereum OKB contract: it has no mint today, but a single owner key can upgrade it, so any change of its code is the one event that could reopen OKB issuance, and it is re-read on every rebuild. Second, the opening of venue staking on X Layer, still listed as upcoming on OKX's own roadmap for this quarter: it would lock OKB, but locked OKB stays inside the circulating count, so the framework would not book it unless the coins leave the float. Third, the protocol upgrades OKX has planned for X Layer in the fourth quarter of 2026: a change that began burning X Layer gas would open Buy #2, which is zero today. Fourth, the **429,064.58 OKB** still on Ethereum: each bridge to X Layer destroys it there and recreates it on X Layer, so it moves OKB between ledgers without changing the 21M.

## Summary

The MrNasdog Pressure Framework reads OKB at **0.00% net** over the trailing 90 days and **0.00%** over the next 90, with every sell row and every buy row at zero. The structural mechanism is a fixed 21M OKB supply on two ledgers, joined by a bridge that destroys OKB on Ethereum before it creates any on X Layer, with no block reward, no vesting and no burn left running. The key risk is control rather than code: the Ethereum OKB contract can still be upgraded by one owner key, and OKX holds most of the supply in wallets whose own share it does not publish. The ceiling is the **21M** cap itself — OKB supply already sits on it, and nothing currently moves it up or down.

---

*MrNasdog Pressure Framework analysis of OKB, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 25 2026.*

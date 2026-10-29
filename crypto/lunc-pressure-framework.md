---
title:         "LUNC Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description:   "LUNC inflation analysis: no new LUNC is minted and a 1.5% transfer tax burned 7.83B in 90 days. Supply in the market fell 0.24%, with 0.18% more projected."
canonical_url: "https://mrnasdog.com/research/lunc/inflation"
tags:          ["crypto", "lunc", "terraclassic", "tokenomics"]
published:     true
---
Originally published at [LUNC Inflation Analysis · October 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/lunc/inflation).

# LUNC Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

<!-- main-page -->
This is the long supply read. For the demand side, the price drivers and the questions people ask about Terra Classic, see [mrnasdog.com/research/lunc](https://mrnasdog.com/research/lunc).

Terra Classic (**LUNC**) is slightly deflationary: the LUNC supply in the market fell by a net **0.24%** in the 90 days to Oct 29 2026, and the same mechanisms point to a further **0.18%** fall in the next 90 days. Terra Classic mints no new LUNC at all, so every change comes from burning and locking: a **1.5%** on-chain transfer tax burned **7.83B LUNC**, Binance burned **966.42M LUNC** from its trading fees, against **534.92M LUNC** paid out of the community pool by vote. The ceiling on how fast LUNC can shrink is the tax itself: with **5.51T LUNC** circulating, even the higher tax removes well under one percent of supply each quarter.

## The verdict, in one paragraph

Over the 90 days from Jul 31 to Oct 29 2026, LUNC sell pressure came to **534.92M LUNC** and LUNC buy pressure to **13.58B LUNC**, a net change of **−0.24%** of the circulating supply. The next 90 days project **548.51M LUNC** of sell pressure against **10.36B LUNC** of buy pressure, or **−0.18%**. The inflation monitor, which follows the market-wide circulating count, reads **−0.23%** for the same 90 days, a gap of just **0.01 points**, so the coin page carries no warning note. The label that fits Terra Classic today: a zero-emission chain that shrinks slowly through its transfer-tax burn.

## Sell pressure: where new LUNC comes from

Protocol inflation is **0**. The Terra Classic mint module is set to a zero rate, with its minimum and maximum both at zero, and the old market swap that once printed LUNC whenever stablecoins were redeemed stays shut. Total LUNC supply went down on every single day of the window, from about 6.454T to 6.445T. Governance could in theory change those settings, so LUNC supply is not fixed by code, but no vote to do so exists.

Vesting unlocks are **0**. Terra Classic has no team or investor vesting calendar left; the allocations from the 2019 launch finished unlocking years ago, and the Terra Classic chain upgrade of Oct 26 2026 only made those old vesting accounts readable again, without releasing anything.

Foundation and unscheduled unlocks come to **534.92M LUNC**. Terra Classic has no foundation since Terraform Labs wound down; the community pool is the only shared treasury, and it pays out only after an on-chain vote. Two payments passed in the window: **281.85M LUNC** on Sep 4 2026 to keep the chain's links to other networks running, and **253.07M LUNC** on Oct 15 2026 for the finished Hyperlane bridge work. Because the community pool sits outside the circulating count, every LUNC it pays out is new supply in the market. Six such payments passed in the last twelve months, which points to about **548.51M LUNC** in the next 90 days, even though no spending vote is open today.

Long-term locked or bankruptcy supply is **0**. No court or bankruptcy estate is set to release LUNC. The old Terraform Labs wallets hold about **302.23M LUNC**, already counted as circulating, and moved less than half a million LUNC in these 90 days.

## Buy pressure: where new LUNC goes

Programmatic buyback is **0**: no Terra Classic contract or team buys LUNC back on the market. Every LUNC removal comes from burning or locking.

The protocol fee burn is the main engine at **7.83B LUNC**. Every on-chain transfer pays a tax, and since a vote passed on Aug 2 2026 that tax is **1.5%** instead of 0.5%, split 1.2% burned, 0.15% to the community pool and 0.15% to the staking-reward pool. Since the change, about **88.45M LUNC** a day has been destroyed. The burn per day did not triple with the tax, because people moved fewer coins once moving them cost more. At the post-change pace the LUNC burn tax destroys about **7.96B LUNC** in the next 90 days. Single large transfers matter: one transfer on Oct 23 2026 alone paid a burn of about 347M LUNC.

Foundation buy is **0**: there is no foundation, and the community pool fills from the tax, not from purchases.

New long-term lock adds **3.37B LUNC**. Staked LUNC is left out of the circulating count, so when holders stake more, coins leave the market. Net staking grew from 905.32B to 908.70B LUNC over the 90 days. Staking swings both ways, though: it fell by 4.65B LUNC in the last 30 days alone, so nothing is counted for the next 90 days.

The exchange fee burn adds **966.42M LUNC**. Binance burns half of the fees it earns on LUNC trading once a month, sending **275.65M LUNC** on Aug 1, **334.88M LUNC** on Sep 1 and **355.89M LUNC** on Oct 1 2026 to the Terra Classic burn address, where the chain destroys them in the same block. Three more batches, around Nov 1, Dec 1 and Jan 1, fall inside the next 90 days; at the recent pace they add up to about **966.42M LUNC**.

Community pool intake adds **1.41B LUNC**. One tenth of the transfer tax and part of validator pay flow into the community pool, which is outside the circulating count, so these LUNC leave the market until a vote spends them. About **1.44B LUNC** is expected to flow in over the next 90 days.

## Foundation and overhang

The largest pile that could reach the market is the stake itself: about **908.70B LUNC** is staked, and any of it can be withdrawn after a 21-day wait. Holders decide this one by one, with no schedule, and the stake is read from the chain at every rebuild. The community pool holds about **9.33B LUNC**; it pays only by vote, and a spending vote for 1.60B LUNC was rejected on Oct 1 2026. The staking-reward pool holds about **35.26B LUNC**, down from 39.44B LUNC 90 days earlier; it pays stakers a little every block, and those coins are already counted as circulating. The old Terraform Labs wallets hold about **302.23M LUNC**, and a fixed block of about **14.95B LUNC** is left out of the market-wide count without a named owner; it did not move in the window. If any of these balances falls between refreshes, the outflow enters the Foundation and unscheduled unlocks row at the next refresh.

## How LUNC compares to other burn-driven proof-of-stake chains

Most proof-of-stake chains pay their validators in brand-new coins and use a fee burn to win some of it back. Ethereum works this way: new ETH goes to validators every epoch and the fee burn removes only a small share of it, so ETH supply still grows. Terra Classic is the reverse case. LUNC has no issuance at all; validators and stakers are paid from the transfer tax, gas fees and a reward pool that already exists. That means LUNC never has new coins to absorb, and every burned LUNC is a straight cut.

The difference from exchange-chain tokens such as BNB is the source of the burn. BNB relies on large planned burns from its own treasury rules. LUNC relies on activity: the burn tax only fires when someone moves LUNC on chain, and the Binance batch only grows when LUNC trading on that exchange grows. Quiet markets mean a smaller LUNC burn, and the rise in the tax from 0.5% to 1.5% showed the trade-off, since the burn per day rose by about 2.3 times, not 3.

The other Terra Classic feature with no close match is scale. With about 5.51T LUNC circulating, burning 7.83B LUNC in a quarter is a real flow but a small share. Compared with capped coins such as bitcoin, LUNC has no hard limit, but in practice it behaves like a coin with a closed tap and a slow drain.

## What to watch in the next 90 days

**Nov 1 2026:** the next Binance monthly LUNC burn, for October trading fees, expected near the recent batches of about 322M LUNC; the Dec 1 2026 and Jan 1 2027 batches follow.

**Any new community pool vote:** none was open on Oct 29 2026, but six passed in the last year, and a large one would raise LUNC sell pressure in the quarter it pays.

**A pool ceiling plan:** a text vote to cap the community pool at 7B LUNC and send the rest to the staking-reward pool was rejected on Aug 21 2026. If it returns and passes, about 2.3B LUNC at today's balance would move back into the circulating count.

**Tax votes and the stake:** any vote that changes the 1.5% transfer tax or its 80/10/10 split moves the main LUNC burn directly, and a large wave of unstaking would release coins from the 908.70B LUNC stake after the 21-day wait.

## Summary

Terra Classic (LUNC) prints no new coins, so its supply in the market can only shrink or be refilled from pools that already exist. In the 90 days to Oct 29 2026 the net change was **−0.24%**, driven by a **1.5%** transfer-tax burn of 7.83B LUNC and monthly Binance fee burns, with **−0.18%** projected next. The main risks are a large spending vote from the 9.33B LUNC community pool and a wave of unstaking from the 908.70B LUNC stake. Because the burn depends on activity, the pace of LUNC deflation rises and falls with how much people actually use the chain.

*MrNasDog Pressure Framework analysis of LUNC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 29 2026.*

---
title:         "LUNC Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "LUNC supply roughly steady: −0.08% in 90 days, −0.17% next. No minting; a 1.5% burn tax and monthly exchange burns destroyed 7.4B LUNC as 3.0B left staking."
canonical_url: "https://mrnasdog.com/research/lunc/inflation"
tags:          ["crypto", "lunc", "terraclassic", "tokenomics"]
published:     true
---

Originally published at [LUNC Inflation Analysis · September 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/lunc/inflation).

# LUNC Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

Terra Classic mints no new LUNC, and its tradable float is shrinking slowly: the Pressure Framework reads LUNC at **−0.08%** over the last 90 days and **−0.17%** projected for the next 90, against a monitor reading of **+0.15%**. A transfer tax, tripled to 1.5% on **Aug 2 2026**, and Binance's monthly burn destroyed **7,442.4M LUNC**, while a net **2,998.3M LUNC** left the staked pool and became tradable. There is no supply cap; what keeps LUNC from growing is that emission is switched off and every taxed transfer destroys coins.

## The verdict, in one paragraph

Against a circulating base of **5,511,140.3M LUNC**, the framework books **2,998.3M LUNC** of sell pressure and **7,442.4M LUNC** of buy pressure over the trailing 90 days, a net of **−0.08%**, and projects **−0.17%** for the next 90 days. The inflation monitor reads **+0.15%** for the same window, a gap of **0.23 percentage points**, which is inside the framework's 0.5-point tolerance, so the overview carries no warning. The monitor's own supply series moves by billions of LUNC from one day to the next, so a gap of this size is expected. The label for LUNC is a **non-minting chain with a burn that now outruns its staking releases**: slightly deflationary on the float, and more so since the tax rise.

## Sell pressure: where new LUNC comes from

It does not come from minting. Terra Classic's emission settings read zero on every field: inflation rate, annual provisions, and both the upper and lower bounds. The count of LUNC in existence fell at every one of 91 reads across the window, from **6,455,620.8M** to **6,448,178.5M**, and the old market swap that once printed LUNC stays shut. Stakers on Terra Classic are paid from a reward pool filled by the transfer tax, not from new coins. So Sell #1, protocol inflation, is **0**. A governance vote could switch emission back on, so the row is watched rather than closed.

Sell #2, vesting unlocks, is **0**: Terra Classic has no team, investor or foundation release schedule. Sell #3, foundation and unscheduled unlocks, is **0** as well. The community pool paid out **291.7M LUNC** in two voted grants, on **Jul 1 2026** and **Sep 4 2026**, but those coins were already counted as circulating, so the grants moved them without adding any. Sell #4, long-term locked or bankruptcy, is **0**: the eight wallets left from Terraform Labs did not move.

The whole sell side is Sell #5, net unstaking, at **2,998.3M LUNC**. Terra Classic's circulating count leaves staked LUNC out, so a coin that leaves the staked pool joins the tradable float. Staked LUNC fell from **915,972.2M** to **912,973.9M** while the active validator set shrank from **103** to **87**. The flow is not one-way: staked LUNC fell **8,278.7M** before Aug 2 and rose **5,280.3M** after it. With no schedule behind it, the framework projects no staking release for the next 90 days.

## Buy pressure: where new LUNC goes

Into two burns. Buy #2, the protocol fee burn, is the larger at **6,227.5M LUNC**. Every taxed transfer on Terra Classic pays a tax, and 80% of it is destroyed. Governance proposal 12223 raised the tax from 0.5% to 1.5% at the block closing its vote on **Aug 2 2026**, so a taxed send now loses 1.2% instead of 0.4%. The burn rose from **36.2M** to **93.8M LUNC** a day, about two and a half times, which means taxed volume fell somewhat after the rise. Because the tax changed mid-window, the next 90 days use the rate since Aug 2: **8,442.9M LUNC**.

Buy #1, the programmatic buyback, is **1,214.8M LUNC**. Binance buys and burns LUNC once a month with half the trading fees from its LUNC pairs, and three burns landed in the window: **604.3M** on Jul 1, **275.6M** on Aug 1 and **334.9M** on Sep 1 2026. Terra Classic destroys anything sent to its burn account in the same block, so that account reads zero at both ends and the burn shows only as a fall in total supply. The framework reads that one surface and counts each coin once. The next three firings are counted at the latest size, **1,004.6M LUNC** in all.

Buy #3, foundation buy, is **0**: there is no foundation, and the community pool's growth from **8,284.1M** to **9,099.2M LUNC** is tax and reward income, not a purchase. Buy #4, new long-term lock, is **0**, because staking released coins over the window as a whole; that net release is already booked as Sell #5.

## Foundation and overhang

Terra Classic has no foundation and no team treasury; Terraform Labs was liquidated on **Jan 16 2026** and its duties passed to a wind-down trust. Three pots are watched. The community pool holds **9,099.2M LUNC** and pays out only by governance vote. The staking reward pool holds **36,861.4M LUNC** and drains a little every block to stakers, refilled by the tax. The eight wallets left from Terraform Labs hold **302.7M LUNC** plus **50.0M** staked; the court judgment says they must be burned or their keys destroyed, and the wind-down runs to **Dec 31 2026**.

All three are read on chain at every rebuild. The community pool and reward pool already count as circulating, so their payouts move coins within the float rather than adding to it. If the Terraform Labs wallets move, or any pot sends coins into the float from outside it between refreshes, that outflow enters Sell #3 at the next refresh.

## How LUNC compares to other non-minting and burn-driven chains

Most Cosmos-SDK chains pay stakers with new coins, at a staking-linked emission of several percent a year. Terra Classic uses the same software but has its emission set to zero, so LUNC pays stakers out of a pool the transfer tax refills. On the issuance axis it is stricter than a halving-model chain like Bitcoin, which still mints every block. Unlike Bitcoin, though, LUNC has no hard cap: supply falls because the settings say zero and the burn runs, and a vote could change either.

Against exchange tokens that run large quarterly buyback-and-burns, LUNC's burn is small relative to its supply. **7,442.4M LUNC** destroyed in 90 days sounds large, yet it is about **0.14%** of the float, because the float is over five trillion coins. The tax burn scales with usage, not with a treasury decision, so it is steadier than a discretionary buyback but cannot jump on demand.

The other lesson is the boundary. Because staked LUNC sits outside the circulating count, staking behaviour moves the float as much as the burn does. Over this window, net unstaking offset about **40%** of everything burned. On chains that count staked coins as circulating, the same flows would not show up at all.

## What to watch in the next 90 days

First, the Binance burns on **Oct 1 2026**, **Nov 1 2026** and **Dec 1 2026**, counted here at **334.9M LUNC**each; their size follows Binance's LUNC trading fees. Second, the tax burn, which runs near **93.8M LUNC** a day and moves with on-chain volume. Third, staking: a swing of a few billion LUNC into or out of the staked pool moves this reading as much as a month of burns. Fourth, the Terraform Labs wallets and their **Dec 31 2026** wind-down date. Fifth, governance: a security upgrade is set for **Sep 24 2026** and changes no supply rule, but any vote on the tax rate, the tax split or emission would.

## Summary

The MrNasdog Pressure Framework reads LUNC at **−0.08%** over the trailing 90 days and **−0.17%**projected forward: mixed flows, supply roughly steady, with a slow shrink. Terra Classic mints nothing; a 1.5% transfer tax and Binance's monthly burn destroyed **7,442.4M LUNC**, and net unstaking returned **2,998.3M LUNC** to the float. The key risk is staking, which can release billions in weeks with no schedule. There is no hard cap; the protection is emission set to zero and a burn tied to every taxed transfer, both of which a vote could change.

MrNasdog Pressure Framework analysis of LUNC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 23 2026.

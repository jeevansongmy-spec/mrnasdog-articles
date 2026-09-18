---
title:         "QNT Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "Mixed flows, supply roughly steady: QNT reads 0.00% over 90 days. No mint since Jun 25 2018, no burn, no buyback, but the 2018 mint switch was never turned off."
canonical_url: "https://mrnasdog.com/research/qnt/inflation"
tags:          ["crypto", "qnt", "quant", "interoperability"]
published:     true
---

> Originally published at **[mrnasdog.com/research/qnt/inflation](https://mrnasdog.com/research/qnt/inflation)** by MrNasdog.

# QNT Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

QNT supply did not move in the last 90 days: the MrNasdog Pressure Framework reads Quant's token at **0.00%** over the trailing 90 days and **0.00%** over the next 90, against an inflation monitor reading of **+0.09%**. Every QNT in existence was minted in a single five-hour window on **Jun 25 2018**, and there is no vesting, no emission, no burn and no buyback, so sell pressure is **0** and buy pressure is **0**. The constraint is not a hard cap in code: the 2018 sale contract behind the QNT mint function was parked rather than switched off, and its admin key could still create about **27.5M QNT** — a key that sent no transaction in this window.

## The verdict, in one paragraph

Against a circulating base of **14.54M QNT**, the framework books **0** of sell pressure and **0** of buy pressure over the trailing 90 days — a net of **0.00%** — and projects **0.00%** for the next 90 days, because nothing is scheduled to change. The inflation monitor reads **+0.09%** for the same window, a gap of **0.09 percentage points**, which sits inside the framework's 0.5pp tolerance, so the overview page ships without a monitor-gap warning. The monitor estimates supply from market data rather than from the chain, and a small wobble on a float that did not move is what that method produces. The label for QNT is a **finished distribution with a parked mint switch**: nothing is being added today, and the one thing that could add supply is a single admin key rather than a schedule.

## Sell pressure: where new QNT comes from

Nowhere, this window. Sell #1, protocol inflation, is **0**. QNT is a plain Ethereum ERC-20 token from 2018; Quant runs no chain of its own, so there is no validator reward and no emission schedule. The Pressure Framework did not trust the QNT contract's reported total for this, because that figure is a fixed number written into the contract at launch that no function ever updates — it would read the same whether coins were minted or not. Instead, every QNT mint ever recorded was replayed: **608 mints**, all on **Jun 25 2018**, and not one since. That count matches the 2018 sale contract's own sales counters to the last unit, and every one of the **751** investor slots in that contract has nothing left owed. The mint function itself is still live and answers only to the sale contract, whose admin key could reopen the sale; that key sent no transaction between **Jun 20 2026** and **Sep 18 2026**, so no mint could have happened. Because a mint is still possible, the row is watched, never closed.

Sell #2, vesting unlocks, is **0**: the whole QNT supply was handed out in 2018 with no vesting contract and no release calendar, and no unlock tracker lists a QNT schedule. Sell #3, Foundation and unscheduled unlocks, is **0**, with no public evidence of any release in the window. Sell #4, long-term locked or bankruptcy, is **0**: there is no bankruptcy estate, no trustee and no court-ordered distribution attached to QNT.

## Buy pressure: where new QNT goes

Also nowhere. Buy #1, programmatic buyback, is **0**. Quant bills Overledger licences in regular money, and no published programme turns that income into QNT purchases on the market. Buy #2, protocol fee burn, is **0**, and here the QNT contract is simple: it has no burn function at all. The framework still checked both places a burn could show up. The dead address held the same balance at both ends of the window. The QNT contract's own address works as a one-way sink, because it has no way to send tokens out; it received about **1.5 QNT** in the window from users who sent coins there by mistake. Those coins are gone for good, but at roughly one hundred-thousandth of a percent of the float they are far below what the ledger displays.

Buy #3, Foundation buy, is **0**: Quant publishes no wallet, and the four Overledger treasury contracts Quant published for licence payments held zero QNT at both ends of the window. Buy #4, new long-term lock, is **0**. Quant describes staking for its Trusted Node Program on the Fusion network, but no QNT staking contract was found on Ethereum among any contract holding **1,000 QNT** or more, and a stake of coins that already count as tradable would not remove supply from this reading anyway.

## Foundation and overhang

The overhang on QNT has three parts. The first and largest is the **parked mint switch**: the 2018 sale contract still has room to mint about **27.5M QNT**, nearly double the current supply, behind one admin key. It is read on chain at every rebuild. The second is a group of **three dormant wallets** holding **1.86M QNT** between them, linked on chain to the 2018 distribution — one is funded through the same chain of wallets that received the company's own allocation. None moved across the window. Because QNT's non-tradable bucket is only about **68K QNT**, these wallets already sit inside the tradable float, so a sale from them would move coins between holders rather than add new supply. The third is Quant's own company reserve of about **68K QNT**, which the company reports but which sits at no public address.

The Overledger licence treasury contracts are empty, and there is no buyback wallet and no bankruptcy estate. The trigger still applies to each item: if the mint switch is used, or any of these balances falls between refreshes in a way that moves coins into the tradable float, that outflow enters Sell #3 at the next refresh.

## How QNT compares to other fixed-supply tokens

QNT belongs to the class of fully distributed tokens: everything was created at launch, there is no emission and no vesting left, so the supply reading sits at a flat zero. That puts QNT alongside a mature capped coin like Bitcoin on the direction of travel, but the mechanism is different. Bitcoin still mints on every block on a known halving clock, so its reading is small but positive; QNT mints nothing at all. And unlike a young token working through a four-year team and investor vest, QNT has no unlock calendar waiting to push coins into the market.

The comparison that matters is the cap. Many fixed-supply ERC-20 tokens prove their ceiling by giving up the mint function in the contract. QNT did not: its mint function still exists behind the old sale contract, so the ceiling is a company commitment rather than a code guarantee. The published total of about **14.61M QNT** is also a company figure; the chain shows slightly more minted and never destroyed. On the other side, QNT has no burn engine like the exchange tokens that remove supply every quarter, so its reading cannot turn negative on its own.

## What to watch in the next 90 days

First, the mint switch: the 2018 sale contract's admin key is read at every rebuild, and any transaction from it — reopening the sale or recording a new presale entry — would be the first new QNT since **Jun 25 2018**. Second, Quant's Trusted Node Program staking: if a QNT staking contract goes live, the framework will check whether staked coins leave the tradable float. Third, the four Overledger treasury contracts, which have held zero; licence demand that actually locks QNT would show up there first. Fourth, the three dormant wallets holding **1.86M QNT**, which have not moved. Fifth, any Quant announcement of a buyback or burn, which the project has never had.

## Summary

The MrNasdog Pressure Framework reads QNT at **0.00%** over the trailing 90 days and **0.00%** projected forward: mixed flows, supply roughly steady. The structural reason is that Quant finished distributing QNT on **Jun 25 2018** and has no emission, vesting, burn or buyback. The key risk is the parked mint path — a 2018 sale contract that could still create about **27.5M QNT** behind one admin key, which stayed idle this window. The ceiling of about **14.61M QNT** is a company commitment, not a limit written into the token's code.

---

*MrNasdog Pressure Framework analysis of QNT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 18 2026.*

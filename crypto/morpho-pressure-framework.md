---
title:         "MORPHO Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description:   "Supply growing, projected to keep growing: MORPHO reads +5.87% per 90 days. Nothing minted or burned, but 26.97M unlocked and Morpho wallets paid out 13.48M."
canonical_url: "https://mrnasdog.com/research/morpho/inflation"
tags:          ["crypto", "morpho", "defi", "ethereum"]
published:     true
---

*Originally published at [mrnasdog.com/research/morpho/inflation](https://mrnasdog.com/research/morpho/inflation)*

# MORPHO Inflation Analysis · September 2026 · Supply growing, projected to keep growing

Morpho created no new MORPHO and burned none over the last 90 days — the count of MORPHO in existence was identical at both ends of the window — and yet the Pressure Framework reads MORPHO at **+5.87%** over the trailing 90 days and **+5.87%** over the next 90. Two mechanisms carry it: founder and strategic-partner lockups opening in a straight line to **May 17 2028**, and Morpho-run wallets paying out tokens they already hold. Sell pressure is **40.45M MORPHO**, buy pressure is **0**, and the 1,000M total is a policy rather than a hard limit, because the DAO multisig owns a mint function it has never used.

## The verdict, in one paragraph

Against a circulating base of **689.13M MORPHO**, the framework books **40.45M MORPHO** of sell pressure and **0** of buy pressure over the trailing 90 days — a net of **+5.87%** — and projects **+5.87%** for the next 90 days, because both lockups keep releasing at the same rate and the Morpho treasury wallets have paid out in every one of the last four quarters. The inflation monitor reads **+6.15%** for the same window, a gap of **0.28 percentage points**, inside the framework's 0.5pp tolerance, so the overview page ships with no monitor-gap warning. The label for MORPHO is a **fixed-count token whose float is still unlocking**: no coin is being printed, but a large share of the coins that exist are only now becoming tradable.

## Sell pressure: where new MORPHO comes from

It does not come from minting. Sell #1, protocol inflation, is **0**. MORPHO pays no block reward and no staking reward, and the total supply of the current MORPHO token read **999,999,999.80** at both ends of the window, with the older legacy token equally flat. That reading is a real measurement, not a hardcoded constant: the figure lives in the contract's writable storage and is not baked into its code. The row is watched rather than closed, because the MORPHO token is upgradeable and its owner, the Morpho DAO multisig, holds a mint function. Nothing has been minted with it.

The larger half of the story is Sell #2, vesting unlocks, at **26.97M MORPHO**. Morpho's founders hold **152M**, released in a straight line from **May 17 2026** to **May 17 2028**, which works out to **18.71M** per 90 days. Strategic Partners Cohort 3 holds **67M**, released in a straight line from **Nov 21 2025** to **Nov 21 2027**, or **8.26M** per 90 days. Neither lockup sits in a vesting contract; they are agreements, so the published calendar is what turns those coins tradable. Morpho also runs a wrapper that converts the old legacy MORPHO into the current token one-for-one, and any holder can use it at any time — so how much passes through the wrapper tells you nothing about when a lockup ends, and the framework does not read it as an unlock. About **166.5M MORPHO** is still locked under the two schedules.

Sell #3, Foundation and unscheduled unlocks, is **13.48M MORPHO**, and this row is measured, not scheduled. Across the Morpho Association, a second safe controlled by exactly the same signers, Morpho Labs, the Morpho DAO treasury and its reward wallets, the combined balance fell by 13.48M between Jun 17 2026 and Sep 15 2026, and every major wallet's transfers add up exactly to its balance change. The Morpho Association and its second safe sent out **9.89M** in grants and payments, and several recipients moved their MORPHO to exchanges within days. Morpho Labs sent **0.76M**. The Morpho DAO moved 6.00M into its rewards multisig, of which **2.84M** actually left the reward pipeline to users and partners. Sell #4, long-term locked or bankruptcy, is **0**: MORPHO has no bankruptcy estate, no trustee and no court-ordered distribution.

## Buy pressure: where new MORPHO goes

Nowhere. Buy #1, programmatic buyback, is **0**. The Morpho lending network earns interest fees, but the fee switch that would route a share of them toward MORPHO holders has never been activated, and no vote in the window proposed a buyback.

Buy #2, protocol fee burn, is **0**. MORPHO has no fee burn, and the framework checked both places a burn could appear rather than trusting one: the total supply did not fall on either token contract, and the dead address held the same **7.18 MORPHO** at both ends. Buy #3, Foundation buy, is **0**: every Morpho wallet was a net sender, and the one sizable inflow — 0.50M to the Morpho Association on Jun 30 2026 — returned from a wallet it had paid the day before. Buy #4, new long-term lock, is **0**. MORPHO has no staking lock. An agreement announced on Feb 13 2026 lets a large asset manager acquire up to 90M MORPHO over four years under trading restrictions, but no tranche, wallet or date has been disclosed, so there is nothing to count yet.

## Foundation and overhang

The overhang on MORPHO is large and almost entirely discretionary. The biggest item is the **Morpho DAO treasury at 304.0M MORPHO** — 290.4M still in legacy form on Ethereum, 0.6M in the current token and 13.0M on Base — which moves only by governance vote. In April 2026 that vote moved 150M to the Morpho Association under MIP 131, a grant for a 2026 to 2030 programme with no published year-by-year split. The **Morpho Association holds 103.8M** after this window's payouts, plus **42.0M** in its second safe. **Morpho Labs holds 11.5M**, and **7.7M** sits in reward wallets waiting to be claimed. On top of these, **166.5M** remains under the founder and Cohort 3 lockups. There is no buyback wallet to track, because there is no buyback.

Every wallet named here is read on chain at each rebuild, on both token contracts and on Base. The trigger is the same for all of them: if the DAO treasury, the Association, its second safe, Morpho Labs or the reward wallets fall between refreshes by more than the last reading, that outflow enters Sell #3 at the next refresh.

## How MORPHO compares to other DeFi governance tokens

MORPHO belongs to the class of DeFi governance tokens with a fixed issued supply and no revenue link to the token. On the issuance axis it is stricter than a continuous-emission layer-1 chain, which prints new coins every block to pay stakers, and stricter than the many DeFi tokens that mint a fresh reward budget each year. Morpho pays its incentives out of coins the DAO already holds, so rewards show up as treasury deployment, not as new supply.

On the float axis MORPHO looks like a token only a few years past launch. Roughly a third of the 1,000M is still outside the circulating count, and it sits in two places: lockups on a calendar and treasuries with a spender. That is the same shape as most venture-backed governance tokens, and it is why MORPHO reads above +5% while a mature fixed-supply coin with its vesting finished reads close to zero. Unlike cliff-based vests, both Morpho lockups release continuously, so there is no single unlock date — the pressure is smooth and steady rather than lumpy.

The sharper contrast is with lending and exchange tokens that already run a fee-funded buyback or burn. Those tokens offset their unlocks with a buy side that grows with usage. Morpho is one of the largest lending networks by deposits and has a fee switch built into its contracts, but it has never been turned on, so none of that activity reaches the MORPHO buy side. For the buy side to matter at today's size, it would need to remove on the order of 40M MORPHO every quarter.

## What to watch in the next 90 days

First, the two lockups, which keep releasing about **26.97M MORPHO** per 90 days with no break until **Nov 21 2027** for Cohort 3 and **May 17 2028** for the founders. Second, the Morpho Association and its second safe, which paid out 9.89M this window and still hold 145.8M between them from the MIP 131 grant and its own allocation. Third, the Morpho DAO treasury: MIP 134, put to vote on Sep 15 2026, would fund incentives on Arc at about $50,000 a month — small, but every new rewards programme is paid from this pot. Fourth, any fee switch proposal, the one change that could give MORPHO a buy side at all. Fifth, the Feb 13 2026 accumulation agreement: a first disclosed purchase or lock would be the first real candidate for Buy #4.

## Summary

The MrNasdog Pressure Framework reads MORPHO at **+5.87%** over the trailing 90 days and **+5.87%** projected forward: supply growing, projected to keep growing. The mechanism is not minting but release — **26.97M MORPHO** of founder and strategic-partner lockups opening on a straight line, plus **13.48M** paid out by Morpho-run wallets, against a buy side of **0**. The key risk is that both sources continue: the lockups run to May 17 2028 and the Morpho treasuries still hold more than 450M MORPHO between them. The ceiling is 1,000M MORPHO by policy, and the DAO multisig that owns the mint function has never used it.

MrNasdog Pressure Framework analysis of MORPHO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 15 2026.

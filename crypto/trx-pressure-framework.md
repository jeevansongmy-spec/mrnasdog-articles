---
title:         "TRX Inflation Analysis · September 2026 · Mixed flows, supply roughly steady"
description:   "Mixed flows, supply roughly steady: TRON minted 352.4M new TRX and burned 233.2M in fees over 90 days, so TRX reads +0.13% net, in line with the monitor."
canonical_url: "https://mrnasdog.com/research/trx/inflation"
tags:          ["crypto", "trx", "tron", "payments"]
published:     true
---

# TRX Inflation Analysis · September 2026 · Mixed flows, supply roughly steady

*Originally published at [mrnasdog.com/research/trx/inflation](https://mrnasdog.com/research/trx/inflation).*

TRX, the native coin of the TRON network, has no supply cap and no vesting left, so every new TRX comes from one place: the fixed **136 TRX** that TRON pays its Super Representatives for each block. Over the 90 days to **Sep 18 2026** that minted **352.4M TRX**, while the TRON fee burn destroyed **233.2M TRX** — about two-thirds of it. The MrNasdog Pressure Framework therefore reads TRX at **+0.13% net** over the last 90 days against a supply-monitor reading of **+0.13%** — a gap of **0.00 percentage points**, which is agreement, not conflict. TRX supply grows slowly and without limit; the only brake is how much TRON users pay in fees.

## The verdict, in one paragraph

For the 90-day window ending **Sep 18 2026**, the Pressure Framework reads **TRX at +0.13% net**: the sell side added **352,387,288 TRX** of new block rewards, and the buy side removed **233,226,077 TRX** through the TRON fee burn, leaving **119.2M TRX** of net new supply on a circulating base of **94.95B**. The independent supply monitor reads the realised 90-day change at **+0.13%**. The gap is **0.00 percentage points**, far inside the framework's half-point tolerance, so TRX ships with **no data-conflict flag**. The forward column also reads **+0.13%**, because neither the TRON block reward nor the TRON energy price changed inside the window. The label for TRX is **slowly inflationary, fee-burn offset**: an uncapped chain token whose issuance is fixed per block and whose float growth depends on how busy the chain is.

## Sell pressure: where new TRX comes from

Sell #1, protocol inflation, is the whole TRX sell side at **352.4M TRX**. TRON is a delegated proof-of-stake chain: 27 elected Super Representatives take turns producing blocks, and the protocol mints **136 TRX** for every block produced — **8 TRX** to the producer and **128 TRX** shared with the voters behind the Super Representatives. Both figures were read from TRON's own chain parameters this window; they were last changed by a Super Representative vote in **June 2025**, which cut them from 16 and 160. TRX issuance is counted per block, not per day, so the block count decides it: TRON produced **2,591,083 blocks** between Jun 20 2026 and Sep 18 2026, a measured **3.001 seconds** each, slightly slower than the three-second target, and nothing in the protocol makes up for missed blocks. The one TRON governance change that took effect inside the window, on **Aug 28 2026**, switched on new smart-contract features and left the TRX block reward untouched.

Sell #2, vesting unlocks, is **zero**: the 2017 TRX allocations finished releasing years ago, no unlock tracker carries a TRX schedule, and TRX circulating supply sits within **0.001%** of total supply. Sell #3, foundation and unscheduled unlocks, is **zero**, and here the arithmetic settles it rather than a promise: only about **721K TRX** sit outside the circulating count, so no foundation, team or DAO wallet can add new TRX to the market — anything such a wallet moves was already counted. Sell #4, long-term locked or bankruptcy supply, is **zero**: no estate distributes TRX on a schedule and no long-dated TRX lock is unwinding.

## Buy pressure: where new TRX goes

TRX goes to the fire. Buy #2, the protocol fee burn, removed **233.2M TRX** over the window, about **2.59M TRX a day**. Every TRON fee — bandwidth for simple transfers, energy for smart-contract calls, and small charges for new accounts and memos — is destroyed the moment it is paid rather than handed to block producers, and the chain keeps a running counter of everything burned. The TRX fee burn was read against total supply at both ends of the window, and then checked a second way, straight from the chain: a random sample of 390 blocks spread across the 90 days landed within **5%** of the booked figure. The TRON fee burn rises and falls through the day — blocks produced around midnight UTC burn roughly a third of what midday blocks burn — which is why only a sample spread across every hour gives an honest 90-day number. The burn eased late in the window, from about 2.72M TRX a day in the middle month to 2.42M in the last, with no fee change behind it, so the forward column keeps the trailing rate.

Buy #1, programmatic buyback, is **zero**: TRON has no buyback contract and no revenue share that purchases TRX. Buy #3, foundation buying, is **zero**. A Nasdaq-listed company does buy TRX every day and held about **709M TRX** by its Aug 13 2026 filing, but it is a separate buyer paying the market, and its coins stay inside the circulating count, so the purchases take nothing off the market. Buy #4, new long-term locks, is **zero**: TRX staking is real — it buys the right to use the chain and to vote for block producers — but nothing new was locked with a stated size, and staked TRX stays inside the circulating count.

## Foundation and overhang

TRX has almost no overhang in the sense the framework means: the non-circulating remainder is about **721K TRX**, or under **0.001%** of supply, and it is re-read on every refresh. No wallet among the largest TRX holders carries a TRON Foundation or TRON DAO label, and no foundation balance could be read this window; the largest TRX balances belong to exchange custody, which is excluded because those coins belong to depositors. The listed TRX treasury company is watched through its regulated filings and holds its coins inside the float. If the non-circulating remainder falls between refreshes and the TRX does not go to a burn, the outflow enters Sell #3 at the next refresh.

## How TRX compares to other uncapped proof-of-stake chains

TRX sits in the large class of chain tokens that pay validators in newly minted coins and lean on a fee burn to offset them. What sets TRON apart is that its TRX reward is a fixed number per block rather than a percentage of supply, so TRX issuance does not compound: about 1.43B TRX a year at the current pace, a shrinking share of a growing base. Chains that pay a set percentage of supply each year grow their issuance as they grow. Against a chain that mints nothing and pays validators from fees alone, TRX looks inflationary; against most staking chains, where the burn covers a small slice of new issuance, TRON's fee burn covering about **two-thirds** of TRX issuance is unusually strong.

Against hard-capped proof-of-work coins, TRX is a different design altogether: a capped chain's subsidy falls on a fixed schedule toward zero, while TRX issuance only changes when Super Representatives vote to change it — they raised it in Nov 2019 and cut it in Jun 2025. That makes the TRX sell side less predictable over years but very predictable over a quarter. The fee economy under TRX is large: TRON users burned roughly **$78M** of TRX over the window, about **1.0%** of a market capitalisation near **$31.8B** on an annual basis — well above the quiet chains the framework tracks. That fee economy is the only thing standing between TRX and a plain 1.5% a year inflation rate, and it is why TRX supply growth rises and falls with chain activity rather than with any schedule.

## What to watch in the next 90 days

First, the TRX burn rate: it slipped to about 2.42M TRX a day in the last month of the window, and a lasting drop toward 2M a day would push TRX net inflation toward **+0.2%** a quarter. Second, TRON governance: any Super Representative proposal that changes the block reward or the energy price moves both sides of the TRX ledger at once — the last reward cut was in June 2025 and the last energy-price cut on Aug 29 2025. Third, the staked TRX fund that opened on **Sep 9 2026** and the listed TRX treasury company's bid to become a Super Representative, announced on **Aug 13 2026**: both add TRX demand and stake, but neither removes TRX from the circulating count, so neither changes the framework reading. Fourth, the roughly 721K TRX outside the float: any outflow that does not end in a burn would open a Sell #3 row that has been zero all window.

## Summary

The MrNasdog Pressure Framework reads TRX at **+0.13% net** over the trailing 90 days and **+0.13%** over the next 90, in line with the supply monitor. The structural mechanism is a fixed **136 TRX** per-block reward to TRON's Super Representatives, **352.4M TRX** a quarter, offset by a TRON fee burn that destroyed **233.2M TRX** — two-thirds of it. The key risk is that the burn depends on how much TRON users pay in fees, so a quieter chain or a cheaper energy price lets more of the TRX issuance reach the market. There is no TRX supply cap: the ceiling on TRX inflation is set only by what Super Representatives vote to mint.

*MrNasdog Pressure Framework analysis of TRX, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 18 2026.*

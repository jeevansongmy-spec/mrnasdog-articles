---
title:         "XMR Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "XMR is mildly inflationary: a fixed 0.6 XMR tail emission minted 38,869 XMR in 90 days, +0.21% net, with no burn, no vesting and no cap. Same pace next."
canonical_url: "https://mrnasdog.com/research/xmr/inflation"
tags:          ["crypto", "xmr", "monero", "privacy"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/xmr/inflation](https://mrnasdog.com/research/xmr/inflation)*

# XMR Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

**Monero (XMR)** supply grows slowly and steadily: the MrNasdog Pressure Framework reads **+0.21%** net over the last 90 days and the same for the next 90. Every Monero block pays its miner a fixed **0.6 XMR** of tail emission, which came to **38,869 XMR** in 90 days, while **0 XMR** was burned, bought back or locked. There is no supply cap, no vesting and no team treasury, so the tail emission is the whole story, and the monitor agrees at **+0.21%**.

## The verdict, in one paragraph

Over the 90 days to **Sep 29 2026**, Monero minted **38,869 XMR** against a circulating supply of **18.81M XMR**, a net of **+0.21%**. Nothing on the buy side removed any XMR, so the net equals the new supply. The next 90 days project the same **+0.21%**, because the Monero block reward is flat and blocks keep arriving about every two minutes. The monitor, which measures supply from a separate market data feed, reads **+0.21%** as well (**+0.2134%** against our **+0.2066%**) — a gap of **0.01 percentage points**, well inside tolerance, so no warning chip is shown. In one line: **Monero is a quiet, flat-emission proof-of-work chain**, adding a small and shrinking share of new XMR each year.

## Sell pressure: where new XMR comes from

Protocol inflation is the only source of new XMR. Since May 2022, Monero has paid a tail emission of **0.6 XMR per block** with no end date. We counted every block in the window on the chain itself: **64,783 blocks** from Jul 1 2026 to Sep 29 2026, about 720 a day, one every 120 seconds on average. That would be 38,869.8 XMR at the full reward, but **4,736 blocks** were a little heavier than the free size limit and paid a slightly smaller reward, so **about 1 XMR** was never minted. Miners received **38,869 XMR** in total, about **432 XMR a day**. Monero also paid about 704 XMR of fees to miners, but fees are coins that already existed, so they add nothing to supply.

Vesting unlocks are **0**. Monero launched in April 2014 with no premine: no founder, investor or company allocation was ever created, so there is no vesting schedule and nothing waiting to unlock. The circulating count sits within **58 XMR** of total supply.

Foundation and unscheduled unlocks are **0**. Monero has no foundation treasury and no team wallet; the one group-held pot is the community General Fund, and every XMR in it already counts as circulating. Long-term locked or bankruptcy supply is also **0**: no estate, trustee or court payout holds XMR, and coins users locked with a custom unlock time, like fresh miner rewards that wait 60 blocks, are already in the circulating count.

## Buy pressure: where new XMR goes

Programmatic buyback is **0**. Monero has no company, no protocol revenue and no treasury budget, so nothing buys XMR back from the market.

Protocol fee burn is **0**. Monero does not burn fees. The **704 XMR** of fees paid in the window went to miners inside the block reward, and total supply rose by exactly the new coins minted — no more, no less. The small reward cut on heavy blocks is already netted out of the sell side, so it is not counted a second time here.

Foundation buy is **0**: no entity buys XMR for the project. New long-term lock is **0**: Monero is mined with RandomX proof of work, not staked, so there is no staking contract that could pull XMR out of the float. With all four buy rows at zero, the **+0.21%** sell side passes straight through to the net.

## Foundation and overhang

Monero has no foundation, no labs company and no investor wallets, so the overhang list is short. The one identified group-held pot is the **Monero General Fund**, which collects community donations and pays developers through the Community Crowdfunding System when a funded proposal is delivered. Its balance is not published and cannot be read on a private chain, so we treat it as opaque and re-check it by hand every two weeks. It does not change the ledger: total supply exceeds the circulating count by only **58 XMR**, so no wallet larger than that sits outside the float, and paying out the General Fund moves coins that are already counted. If the General Fund's balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How XMR compares to other proof-of-work chains

Monero sits between two families of proof-of-work coins. **Bitcoin** and **Zcash** use a halving model with a hard cap of 21M coins: the block reward is cut in half every four years, so issuance keeps shrinking toward zero and security must one day be paid for by fees alone. Monero followed a smooth decay curve until May 2022 and then switched to a permanent tail emission, choosing a small, never-ending reward over a hard cap. **Dogecoin** made the same choice with a flat reward per block, but at a much higher rate relative to its supply.

The Monero tail emission is fixed in XMR, not in percent. At about **157,600 XMR a year**, the annual rate is about **0.84%** today and falls a little every year as the supply grows, which is close to Bitcoin's rate today, will sit above it after Bitcoin's next halving in 2028, and stays far below most staking chains. Unlike Ethereum, Monero has no fee burn, so busy periods do not cut supply; unlike Zcash, no part of the block reward goes to a development fund. Every new XMR goes to the miner who found the block.

The other difference is privacy. Monero hides amounts and addresses, so wallet-level unlock tracking is impossible — but it is also unnecessary, because there was never a premine to track. Supply itself stays public: every block reward is visible, which is how we count the new XMR exactly.

## What to watch in the next 90 days

The FCMP++ and Carrot privacy upgrade runs a new test-network fork on **Oct 5 2026**; it changes no emission rule, and a mainnet date would be the signal that the upgrade is close. Block timing matters because the Monero reward is paid per block: if hashrate swings or a large pool mines selfishly, the block count can drift from 720 a day for a while before difficulty catches up. The block-size limit is worth watching too — if activity keeps rising, more blocks pay a slightly smaller reward, which trims new supply by a tiny amount. No proposal to change the 0.6 XMR tail emission is on the table as of **Sep 29 2026**; one would be the only thing able to move this reading by more than a rounding error before **Dec 28 2026**.

## Summary

Monero (XMR) is mildly and steadily inflationary: a fixed tail emission of 0.6 XMR per block minted **38,869 XMR** in 90 days, a net of **+0.21%** of circulating supply, with the same **+0.21%** projected for the next 90 days. Nothing is burned, bought back, staked or vested, and there is no team treasury, so the tail emission is the only supply force. The key risk to the reading is a change to the emission rule or a long shift in block timing, neither of which is scheduled. Monero has no supply cap by design, but its annual inflation rate of about **0.84%** keeps falling as supply grows.

*MrNasdog Pressure Framework analysis of XMR, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

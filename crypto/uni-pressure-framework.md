---
title: "UNI Inflation Analysis · October 2026 · Supply was growing · trend cooling"
description: "UNI supply grew +0.65% in 90 days: 10M UNI of treasury growth payouts against a 5.79M UNI fee-funded burn. About +0.06% projected next. No minting."
canonical_url: "https://mrnasdog.com/research/uni/inflation"
tags: ["crypto", "uni", "uniswap", "defi"]
published: true
---
Originally published at [https://mrnasdog.com/research/uni/inflation](https://mrnasdog.com/research/uni/inflation) by MrNasDog.

# UNI Inflation Analysis · October 2026 · Supply was growing · trend cooling

<!-- main-page -->
This is the long supply read. For the signal, the price drivers and the questions people ask about Uniswap, see [mrnasdog.com/research/uni](https://mrnasdog.com/research/uni).

UNI supply grew by **+0.65%** over the last 90 days and is projected to grow only about **+0.06%** over the next 90. The Uniswap DAO treasury paid out **10M UNI** of growth budget to Uniswap Labs, while the Uniswap fee switch paid people to burn **5,794,001 UNI** and a governance-linked wallet sent **113,138 UNI** back to the treasury. No new UNI was minted: total supply is still exactly 1B, of which 112.79M UNI now sit at the burn address.

## The verdict, in one paragraph

Our ledger reads **+0.65%** net UNI supply growth for the 90 days from Jul 14 to Oct 12 2026, and **+0.06%** for the next 90 days. The monitor reads **+0.64%** for the same kind of window, a gap of **0.01 percentage points**, well inside our 0.5-point tolerance, so no warning chip is shown. The window caught two quarterly payouts instead of the usual one, which is why it reads higher than the next 90 days, when one payout meets a fee burn of about the same size. In one line: UNI is a fee-burning DEX token whose treasury still pays out slightly more than the burn takes back.

## Sell pressure: where new UNI comes from

Protocol inflation was **0**. The UNI token has a mint function, and the Uniswap governance timelock is its minter: since Jan 1 2024 it may mint up to 2% of supply once a year, about 20M UNI. It has never done so, total supply read exactly 1,000,000,000 UNI at both ends of the window, and no vote proposes a mint. We checked that this total lives in contract storage that a mint would change, so the flat reading is a real one.

Vesting unlocks were **10M UNI**. The UNIfication vote of December 2025 set a growth budget of 20M UNI a year for Uniswap Labs, paid by a vesting contract that releases **5M UNI** each calendar quarter from the DAO treasury. The third-quarter tranche was claimed on Jul 14 2026 and the fourth on Oct 1 2026, both inside this window. The next tranche opens on Jan 1 2027, inside the next 90 days, so the forward figure is 5M UNI. The treasury has approved 20M UNI more for the contract, enough for four further quarters.

Foundation and unscheduled unlocks were **0**. Apart from the vesting payouts, nothing left the treasury in this window. Long-term locked or bankruptcy releases were also **0**: no estate or trustee holds UNI, and the team and investor vesting from the 2020 launch ended in 2024.

## Buy pressure: where new UNI goes

The programmatic buyback took **5,794,001 UNI** out of the market. Since the fee switch went live, a slice of Uniswap trading fees collects in vaults on 13 chains. Anyone can empty a vault, but only by destroying a fixed lot of 2,000 or 4,000 UNI, so the fees keep buying UNI and burning it. In this window about 2,500 such burns reached the Ethereum burn address, worth about **$32.4M** at the time, close to the protocol revenue reported for the same days. The pace rose after governance turned on fees for Uniswap v4 pools and Robinhood Chain on Jul 27 2026, and peaked in early September, when one week burned about 816,000 UNI.

Because each vault is emptied once its fees are worth the UNI lot, the number of coins burned depends on the UNI price. UNI roughly doubled in the window, to about $7.53, so the same dollars now burn fewer coins. At the fee pace since Jul 27 and today's price, we project about **4.63M UNI** burned in the next 90 days.

The protocol fee burn row is **0**, because the protocol never destroys its fees directly; the burn is counted once, as the buyback above. Foundation buys were **113,138 UNI**: on Jul 30 2026 a governance-linked wallet sent that amount back to the treasury, part of it bought in the market the day before. It has happened once and has no schedule, so the forward figure is 0. New long-term locks were **0**: UNI has no staking lock, and coins held for voting stay in the float.

## Foundation and overhang

The one overhang that matters is the Uniswap DAO treasury, the governance timelock, with **262.25M UNI**. It is the only balance counted outside the circulating supply, so every coin it pays out adds to the float. Of that balance, 20M UNI is already approved for the growth budget through the end of 2027; the rest has no release schedule and needs a governance vote to move. Inside the float sit the Uniswap Labs wallet that receives the budget (it passed on the full 19M UNI it received or held during the window), the original airdrop claim contract with about 12.5M unclaimed UNI, and the governance-linked wallet that returned coins in July. The treasury balance is read from the chain every day; if it falls between refreshes beyond the scheduled payouts, the outflow enters Sell #3 at the next refresh.

## How UNI compares to other DEX and DeFi governance tokens

Most exchange tokens that return fees to holders do it one of two ways: they buy their token and burn it, or they buy it and hold it in a treasury or fund. UNI uses the first way, with a twist: the protocol never trades itself. Searchers race to claim the fee vaults and pay with UNI that is destroyed, so the burn is as large as the fees allow and no treasury is left holding bought-back coins. Tokens that buy back into a fund keep those coins as a future overhang; UNI's burn removes them for good.

On the sell side, UNI is unusual among DeFi tokens because it pays no emissions to liquidity providers and runs no staking rewards. Tokens that reward farms or stakers mint new coins every day, which a burn must outrun before supply can shrink. UNI's only steady new supply is the 20M UNI a year growth budget, about 3.2% of circulating supply a year, against a fee burn that ran near 23M UNI a year at the pace of this window.

The hard limit is softer than a capped coin's. UNI started at 1B, will never exceed it unless governance votes to mint, and has already burned 112.79M. But the 2% yearly mint right means the cap is a policy choice, not a rule written in stone.

## What to watch in the next 90 days

**Jan 1 2027:** the next 5M UNI growth-budget tranche opens; we expect it to be claimed within two weeks, as the last four were.

**The burn pace:** weekly burns fell from about 816,000 UNI in early September to about 220,000 UNI in the week of Oct 5 2026 as fees cooled and the price stayed high. If that slower pace holds, the burn will fall short of the 4.63M UNI we project, and supply will grow faster than +0.06%.

**More fee votes:** fees on Arc went live on Oct 5 2026, and governance has more v4 pools and chains in the queue. Each new chain adds fee vaults that end in UNI burns.

**The mint right and the treasury:** any proposal to use the 2% mint, raise the growth budget or move treasury UNI outside the budget would change the sell side at once.

## Summary

UNI supply grew **+0.65%** in the 90 days to Oct 12 2026 and is projected near flat, about **+0.06%**, for the next 90 days. The structure is simple: the Uniswap DAO treasury pays a 5M UNI growth budget every quarter, and the fee switch burns UNI with every vault claimed, 5.79M UNI in this window. The key risk is the burn slowing while the payouts stay fixed, with 262.25M UNI in the treasury behind them. The ceiling is the original 1B UNI, which holds only as long as governance never uses its 2% yearly mint right.

---

*MrNasDog Pressure Framework analysis of UNI, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 12 2026.*

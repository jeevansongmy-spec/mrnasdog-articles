---
title:         "NEAR Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description:   "NEAR supply is growing: a 2.5% epoch mint added 7.98M NEAR in 90 days while the gas burn took back 61.6K, and fee buybacks are held, not burned. Net +0.61%."
canonical_url: "https://mrnasdog.com/research/near/inflation"
tags:          ["crypto", "near", "near-protocol", "layer1"]
published:     true
---

*Originally published at [mrnasdog.com/research/near/inflation](https://mrnasdog.com/research/near/inflation)*

NEAR, the native coin of NEAR Protocol, has no supply cap: NEAR Protocol mints new NEAR at every epoch at **2.5% a year**, the rate since the NEAR inflation halving of **Oct 30 2025**. Over the last 90 days that mint added **7.98M NEAR**, while the NEAR gas burn destroyed **61.6K NEAR** — less than 1% of what was minted. NEAR Intents swap fees also buy NEAR, but that NEAR is held in wallets that still count as circulating, so it takes nothing out of the float. The MrNasdog Pressure Framework reads NEAR at **+0.61% net** over 90 days against a supply-monitor reading of **+0.21%** — a gap of **0.39 percentage points**, inside tolerance. NEAR supply grows at close to its full mint rate.

## The verdict, in one paragraph

For the 90-day window ending **Sep 25 2026**, the Pressure Framework reads **NEAR at +0.61% net**: the sell side added **7.98M NEAR** and the buy side took back **61.6K NEAR**, on a circulating supply of **1.31B NEAR**. The independent supply monitor reads the 90-day change at **+0.21%**. The gap is **0.39 percentage points**, inside the framework's half-point tolerance, so NEAR ships with **no data-conflict flag**. The monitor's supply figure is derived from market value and price, and it swings by a few tenths of a percent from day to day on price rounding alone; NEAR total supply read straight off the chain rose **7.92M NEAR**, which is the framework's net to the coin. The forward column reads **+0.61%** again, because the mint is a fixed share of a supply that barely changes in 90 days. The label for NEAR is **steadily inflationary by design**: a proof-of-stake chain paying for its security with new coins, with a burn too small to offset them.

## Sell pressure: where new NEAR comes from

All new NEAR comes from the protocol itself. Sell #1, protocol inflation, is **7.98M NEAR** over 90 days. NEAR Protocol pays validators by minting NEAR at the start of each epoch, about every seven and a half hours, at a top rate of 2.5% of total supply a year. The figure here was read off total supply at all **293** epoch starts in the window rather than taken from the published rate, and it came to 99.6% of the full rate, because validators that miss blocks forfeit part of their reward and that part is never minted. NEAR blocks arrive every 0.61 seconds, well faster than the one-second pace the protocol constants assume, but the NEAR epoch reward is paid per unit of time rather than per block, so the faster chain adds no extra NEAR. About a tenth of every mint goes to the NEAR protocol treasury, which took in 802K NEAR this window and paid nothing out. The rate has not changed inside the window, so the forward figure, **8.03M NEAR**, is the same rate applied to today's supply.

Sell #2, vesting unlocks, is **zero**. The original NEAR team, backer and sale allocations have finished vesting, and every NEAR coin — including any still held in a lockup contract — is already inside the circulating count, so a release from a lockup moves coins that were counted all along. Sell #3, Foundation and unscheduled unlocks, is **zero** for the same reason: NEAR Foundation grants and payouts move coins that were already in the float, and adding them again would count them twice. Sell #4, long-term locked or bankruptcy supply, is **zero**: NEAR has no bankruptcy estate and no long-dated lock unwinding, and listed companies that hold NEAR bought it on the open market.

## Buy pressure: where new NEAR goes

Buy #2, the protocol fee burn, is **61.6K NEAR**. Every NEAR Protocol transaction pays gas, and 70% of that gas is destroyed as it is spent; the other 30% is credited to the smart contract that was called. The burn was measured as the difference between what the epoch mint created and how far NEAR total supply actually rose, and a random sample of 599 blocks across the window lands within 5% of it. That is about 684 NEAR a day. The NEAR House of Stake ratified **HSP-027** on **Jul 3 2026**, which ends the 30% contract share so that all of the gas is burned, but it ships with a protocol upgrade that has no mainnet date yet, so the forward column holds today's rate.

Buy #1, the programmatic buyback, is **zero** even though NEAR is being bought. Since early 2026 the fees from NEAR Intents, the cross-chain swap service built on NEAR Protocol, are used to buy NEAR, and the main NEAR buyback wallet grew by **1.32M NEAR** this window. Those coins are held, not burned, and the wallet is still part of the circulating count, so the purchase moves NEAR from sellers to a project wallet without taking any out of the float. The NEAR supply arithmetic confirms it: supply moved only by the mint and the gas burn. Buy #3, Foundation buying, is **zero**, and Buy #4, new long-term locks, is **zero**: about 42% of all NEAR is staked, and NEAR governance locks exist, but staked and locked NEAR stays inside the circulating count.

## Foundation and overhang

Four NEAR balances are tracked as overhangs. The NEAR protocol treasury holds **1.20M NEAR**, fed by its share of every mint, with no outflow in 90 days. The main NEAR buyback wallet holds **1.79M NEAR** and a second NEAR revenue wallet holds **1.78M NEAR**, both built from swap fees. The NEAR Foundation's own reserve is the largest and the least visible: its last public treasury report dates from 2023. A proposed NEAR Sovereign Fund of about **30M NEAR**, drawn from the protocol treasury and revenue, is still a forum discussion with no vote. The on-chain wallets are re-read on every refresh. Because every NEAR is already counted as circulating, none of these balances can add new supply when they are spent; what would change the reading is coins being destroyed, or a governance change to the mint.

## How NEAR compares to other proof-of-stake Layer 1 chains

NEAR belongs to the large class of uncapped proof-of-stake Layer 1 chains that pay validators in newly minted coins. What sets a chain in this class apart is how much of that mint its fee burn gives back. On NEAR the answer is very little: the gas burn returned under 1% of the mint this window, so NEAR supply grows at close to its full rate. Chains with a base-fee burn and heavy traffic can burn as much as they mint in busy periods; NEAR keeps gas cheap by design, so its burn stays small even when usage is high. At the measured pace, NEAR gas costs come to about 0.03% of supply a year, against a 2.5% mint.

Against chains with a fixed cap, NEAR is different again: a capped chain issues less every year until issuance stops, while NEAR mints a fixed share of a growing supply with no end date, so the number of new NEAR rises slowly year by year. Against exchange-linked tokens that burn what they buy, the NEAR Intents buyback is the notable contrast — it is real buying funded by real fees, but because the coins are kept rather than destroyed, it supports demand without shrinking supply. The halving of the NEAR mint from 5% to 2.5% in 2025 already moved NEAR toward the lower-issuance end of its class; turning held buybacks into burns, or cutting the mint again, are the two levers that could move it further.

## What to watch in the next 90 days

First, **HSP-027**: when the protocol upgrade that removes the 30% contract share of gas reaches NEAR mainnet, the NEAR gas burn rises by about 43%, which is still small next to the mint. Second, the NEAR Sovereign Fund discussion and the forum proposal of **Sep 12 2026** to move validator pay from new coins toward protocol revenue: either would change Sell #1, the largest line on the page, and only a ratified vote with a date moves the reading. Third, the NEAR buyback wallets: any decision to burn the held NEAR, rather than keep it, would open a real buy row for the first time. Fourth, the NEAR protocol treasury at **1.20M NEAR**: it has only taken in so far, and any spending plan would show there first.

## Summary

The MrNasdog Pressure Framework reads NEAR at **+0.61% net** over the trailing 90 days and **+0.61%** over the next 90. The structural mechanism is a 2.5% yearly epoch mint that pays NEAR Protocol validators by clock time, set against a gas burn of **61.6K NEAR** that gives back less than 1% of it; NEAR Intents fees buy NEAR, but the coins are held in wallets that stay in the float. The key risk is that nothing on the buy side is built to scale with the mint: the burn is small by design, and the fee-funded buying keeps its coins in the float, so until a governance change is dated the mint sets the pace alone. The ceiling is that NEAR has no supply cap, so without a change to the mint NEAR supply keeps growing at about 2.5% a year.

---

*MrNasdog Pressure Framework analysis of NEAR, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 25 2026.*

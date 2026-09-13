---
title:         "OKB Inflation Analysis · September 2026 · Mixed flows, supply roughly steady"
description:   "Mixed flows, supply roughly steady: OKB added and removed nothing over 90 days — no mint, no vesting, no burn. Framework 0.00% net; the supply monitor agrees."
canonical_url: "https://mrnasdog.com/research/okb/inflation"
tags:          ["crypto", "okb", "okx", "exchange"]
published:     true
---

# OKB Inflation Analysis · September 2026 · Mixed flows, supply roughly steady

*Originally published at [https://mrnasdog.com/research/okb/inflation](https://mrnasdog.com/research/okb/inflation)*

OKB, the gas token of OKX's X Layer chain, added nothing and removed nothing over the 90 days to **Sep 13 2026**. There is no OKB block reward, no vesting left, and no buyback or burn running since the 2025 programme ended, so the MrNasdog Pressure Framework reads OKB at **0.00% net** on a **21M** float, with **0.00%** projected next. The supply monitor reads **+0.0002%** — a gap of **0.0002 percentage points**, which is agreement. The flat OKB supply rests on code, not on a promise: the only bridge onto X Layer destroys OKB on Ethereum before it creates any.

## The verdict, in one paragraph

For the 90-day window ending **Sep 13 2026**, the Pressure Framework reads **OKB at 0.00% net**: all four OKB sell rows and all four OKB buy rows are zero. The independent supply monitor reads the realised change at **+0.0002%**, so the gap is **0.0002 percentage points**, far inside the half-point tolerance, and OKB ships with **no monitor-gap flag**. A flat reading on its own proves nothing, so the OKB write path was tested rather than assumed: the supply figure sits in storage the contract can change, the live code has no function that adds to it, and no bridge or upgrade event fired in the window. The label for OKB is **flat by construction, not by lock**: no mechanism adds OKB or removes it today, while the keys that could change the code still exist.

## Sell pressure: where new OKB comes from

Nowhere, this window. Sell #1, protocol inflation, is **zero**. X Layer is an OP-Stack layer-2 that pays its operator from gas fees, so there is no OKB block reward and no OKB staking emission. OKB lives on two ledgers — **429,064.58 OKB** still sits on Ethereum as the original token, and the rest is X Layer native gas — and the road between them runs one way. The Ethereum OKB contract's bridge function wipes the sender's balance and cuts the OKB total supply by the same amount; only then can the X Layer portal mint native OKB, and it can only do so by drawing down a fixed deposit-token balance created once at **559,344.6**. That balance splits into **429,064.58** still waiting and **130,280.02** already bridged, with nothing left over, and both halves were identical at the start and the end of the window. No OKB was bridged, so no OKB was minted on X Layer.

The Ethereum OKB total held the same value at both ends too, and it is a real reading rather than a fixed number: it lives in storage the contract writes, and the live OKB code carries sixteen functions, none of which can add supply. Sell #2, vesting unlocks, is **zero** and the one row marked permanent: the original OKB allocation finished vesting years ago and every OKB is unlocked. Sell #3, foundation and unscheduled unlocks, is **zero** — no identified OKX wallet sent OKB to market in the window. Sell #4 is **zero**: no estate or long-dated lock holds OKB.

## Buy pressure: where new OKB goes

Also nowhere. Buy #1, programmatic buyback, is **zero**. The quarterly OKB buyback-and-burn ended in **2025**; the last OKX burn report covers a period that closed in **May 2025**, and no programme has been announced since. The one-time burn of **65,256,712.097 OKB** that fixed the supply at 21 million was in August 2025, outside this window, and is not booked as a flow.

Buy #2, the protocol fee burn, is **zero**, and this is the OKB row most often misread. Every X Layer transaction pays gas in OKB, but that gas is not destroyed. It collects in the chain's fee accounts, which took in about **845 OKB** across the window, and those accounts pay out to a single wallet holding about **12.9K OKB** that has never sent a transaction. Parked coins can still be spent, so they stay in the float. Both burn surfaces were read at both ends: the Ethereum OKB total did not fall, and the X Layer dead addresses gained under half an OKB from stray user transfers, which is not a mechanism and rounds to nothing. Buy #3, foundation buy, is **zero**. Buy #4, new long-term lock, is **zero** for now: OKX's Exchange OS requires a builder to stake OKB before opening a trading venue, but no required amount and no staking contract address have been published, so nothing can be counted.

## Foundation and overhang

OKX burned its OKB reserves and past buyback holdings in August 2025, and it publishes no treasury address today, so the OKX treasury is tracked as opaque. What can be read on-chain is small and still: the X Layer fee-collection wallet at about **12.9K OKB**, flat across the window, and the chain's fee accounts at about **1.8K OKB**, still filling. The wallet OKX used to move its Ethereum OKB onto X Layer in 2025 now holds under one OKB. Exchange wallets holding customer OKB are excluded, because those coins belong to depositors. All of these are re-read on every rebuild. If the fee-collection wallet or any identified OKX wallet sends OKB toward the market between refreshes, that outflow enters Sell #3 at the next refresh.

## How OKB compares to other exchange-linked chain tokens

OKB now sits in an unusual spot among exchange tokens. BNB, the closest peer, also mints nothing, but it runs two burns — a quarterly reserve-funded burn and a slice of every block's gas — so BNB supply falls every quarter. OKB kept the zero-issuance half of that design and dropped the burn half: the quarterly OKB burn is gone and X Layer gas is parked rather than destroyed. The result is a supply that neither grows nor shrinks, which caps OKB's inflation reading at flat rather than deflationary.

Against capped proof-of-work coins the contrast is issuance: a hard-capped chain still pays a block subsidy until the cap is reached, so its supply rises every day, while OKB has no subsidy left to pay. Against other layer-2 chains, OKB differs in what the gas token is. Most OP-Stack layer-2s charge gas in ETH, which they neither mint nor burn; X Layer charges gas in its own token and mints it only against OKB destroyed on Ethereum, so bridging moves OKB between ledgers without changing the total. The trade-off is plain. With no burn, X Layer usage does not remove OKB from the market: its fee economy runs at roughly **$0.39M** a year against a market value near **$2.37B**, and none of it is destroyed.

## What to watch in the next 90 days

First, Exchange OS: open deployment was targeted for the third quarter, so by **Sep 30 2026** OKX may publish the staking contract and a required OKB stake, which would give Buy #4 its first measurable lock. Second, the X Layer fee-collection wallet at about **12.9K OKB**: its first outgoing transaction would open a Sell #3 row that has been zero all window. Third, the OKB token's upgrade key: a new implementation on the Ethereum contract could restore a mint or burn overnight, so the live code is re-read every rebuild. Fourth, any OKX announcement that starts burning X Layer gas, which would turn Buy #2 into the first non-zero OKB row since 2025.

## Summary

The MrNasdog Pressure Framework reads OKB at **0.00% net** over the trailing 90 days and **0.00%** over the next 90, with every sell and buy row at zero. The structural mechanism is a 21 million OKB supply with no block reward, no vesting and no burn, split between Ethereum and X Layer by a bridge that destroys before it mints. The key risk is that this is enforced by upgradeable code: the OKB contract's upgrade key and the X Layer portal's admin could change the rules, and X Layer gas fees are parked in a spendable wallet rather than burned. The ceiling is 21 million OKB, and nothing on the current calendar moves the total in either direction.

*MrNasdog Pressure Framework analysis of OKB, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 13 2026.*

---
title: "UNI Inflation Analysis · September 2026 · Mixed flows, supply roughly steady"
description: "Mixed flows, supply roughly steady: Uniswap burned 5.78M UNI from swap fees in 90 days against a 5.00M UNI treasury growth budget. Net −0.14%, next 90 days −0.27%."
canonical_url: "https://mrnasdog.com/research/uni/inflation"
tags: ["crypto", "uni", "uniswap", "defi"]
published: true
---

Originally published at [https://mrnasdog.com/research/uni/inflation](https://mrnasdog.com/research/uni/inflation) by MrNasdog.

# UNI Inflation Analysis · September 2026 · Mixed flows, supply roughly steady

Uniswap now destroys more UNI than its DAO pays out. Over the 90 days to **Sep 24 2026**, the Uniswap fee switch burned **5.78M UNI** and a multisig returned **0.11M UNI** to the DAO treasury, while the treasury released one **5.00M UNI** growth-budget slice — so the MrNasdog Pressure Framework reads UNI at **−0.14% net**, projects **−0.27%** for the next 90 days, and sits **0.14 percentage points** from the supply monitor's **+0.00%**. UNI has never been minted — the supply counter still reads exactly **1B** — but the 2% a year mint right is live, and the margin between burn and budget is thin.

## The verdict, in one paragraph

For the 90-day window ending **Sep 24 2026**, the Pressure Framework reads **UNI at −0.14% net**: **5.00M UNI** entered the float from the Uniswap DAO treasury and **5.90M UNI** left it, on a circulating supply of **620.66M UNI**. The independent supply monitor reads the same window at **+0.00%**, a gap of **0.14 percentage points**, inside the half-point tolerance, so UNI ships with **no data-conflict flag**. The ledger also closes on its own: the circulating float is exactly the genesis supply minus the burn address minus the DAO treasury, and that figure fell by **895,139 UNI** across the window — the same number the rows add up to. The forward column is deeper, at **−0.27%**, because two fee votes on **Jul 27 2026** lifted the UNI burn rate by about **63%**. The label for UNI today is **a fee-funded burn running just ahead of a fixed treasury budget**.

## Sell pressure: where new UNI comes from

Not from minting. Sell #1, protocol inflation, is **zero**. The UNI supply counter on Ethereum read exactly **1,000,000,000 UNI** at both ends of the window, and that counter is a live stored value rather than a number fixed in the code, so a mint would have moved it. The mint right itself is real: the Uniswap DAO treasury can mint up to **2% of supply a year**, and the waiting period ran out on **Jan 1 2024**. It has never been used, but it is one governance vote away, so the row stays watched rather than retired.

Sell #2, vesting unlocks, is where the sell side lives: **5.00M UNI**. The original four-year vesting for the Uniswap team and investors finished in **2024**. What vests now is the growth budget the UNIfication vote created for Uniswap Labs: **20M UNI** a year, paid by a UNI vesting contract in **5M UNI** slices each quarter, starting **Jan 1 2026**. The contract pulls each slice straight out of the DAO treasury, and the slices were withdrawn on **Jan 5**, **Apr 10** and **Jul 14 2026**. The July withdrawal was the treasury's only outflow in 90 days. The DAO has already approved **25M UNI** more, five further quarters, and the next slice unlocks on **Oct 1 2026**.

Sell #3, foundation and unscheduled unlocks, is **zero**. The DAO treasury is the only UNI balance kept out of the circulating count, so the only way new UNI reaches the market is by leaving it, and nothing left it this window except the growth-budget slice already booked in Sell #2. Sell #4, long-term locked or bankruptcy supply, is **zero**: Uniswap has no estate, no trustee schedule and no long lock unwinding.

## Buy pressure: where new UNI goes

Almost all of it goes to the burn address. Since the UNIfication vote in December 2025, part of every Uniswap swap fee collects in a protocol vault, and the only way to take those fees out is to buy UNI and destroy it, in fixed lots of **2,000 to 4,000 UNI**. Fees earned on other chains are handled the same way and the burned UNI is bridged back to the same Ethereum burn address. Buy #1, the programmatic buyback, came to **5.78M UNI** across **2,460** separate burns. Because the UNI token has no burn function, total supply never moves when UNI is burned; the burn address is the one place the flow shows, and it is counted once.

The rate changed inside the window, and the date is known. Two Uniswap governance proposals executed on **Jul 27 2026**: one switched on protocol fees for Uniswap v4 pools across seven chains, the other added v2 and v3 fees on Robinhood Chain. Before that date the UNI burn ran at about **45,500 UNI a day**; since then it has run at about **74,200 UNI a day**. The forward column uses the post-change rate, **6.68M UNI** over the next 90 days, and the trailing column stays as measured. Buy #2, the protocol fee burn, is **zero**, because nothing is burned per swap — the fee burn happens through that UNI purchase and is booked once, in Buy #1. Buy #3, foundation buying, is **0.11M UNI**: a multisig returned **113,138 UNI** to the DAO treasury on **Jul 30 2026**, which takes it out of circulation, and it has no schedule, so nothing is carried forward. Buy #4, new long-term locks, is **zero**: there is no UNI staking contract and delegated votes stay free to trade.

## Foundation and overhang

The overhang that matters is the Uniswap DAO treasury: **267.25M UNI**, about **43%** of circulating supply and the whole of the non-circulating bucket. **25M UNI** of it is already committed to the growth budget; the rest has no release schedule. It is read on the chain at every refresh. The growth-budget wallet that receives the quarterly slices holds **12.0M UNI** and moved about **2.0M UNI** out this window, but those coins were already counted as circulating, so those moves add nothing new. The unused **2%** a year mint right is tracked on the same schedule. If the treasury balance falls between refreshes and the UNI does not go to the vesting contract or the burn address, the outflow enters Sell #3 at the next refresh.

## How UNI compares to other DEX tokens

Many exchange tokens that return revenue do it with a buyback: the protocol buys its own token and parks it in a wallet it controls. That supports the price, but it builds a pile the protocol can later sell. Uniswap's design leaves no pile. Nobody at Uniswap buys UNI; outside traders buy it to claim the fee vault, and the UNI they bring is destroyed on arrival. The supply falls and there is no treasury of bought-back coins waiting to come back.

The trade-off is on the other side of the ledger. A token with no issuance and a fee burn, like a gas coin with a base-fee burn and no subsidy, can only shrink. UNI does have issuance: a fixed **20M UNI** a year growth budget and a mint right the DAO has not used. So UNI works like a tug-of-war between a fixed payout and a fee-driven burn. The burn is set in UNI per claim, so for the same dollar fees it destroys fewer UNI when the UNI price is high. A fixed schedule sets the payout side; trading volume and price set the burn side.

## What to watch in the next 90 days

First, the **Oct 1 2026** growth-budget slice: **5M UNI** leaves the DAO treasury once it is withdrawn, and it is already in the forward column. Second, the burn pace: the release needs about **55,600 UNI a day** of burning just to break even, against **74,200** since Jul 27 2026 — a slower market or a much higher UNI price could narrow that margin fast. Third, the second v4 fee vote, which is expected to cover the remaining five chains the first vote could not reach; it would add to the burn once it executes. Fourth, the DAO treasury at **267.25M UNI** and the 2% mint right — any use of either would open a sell row that is quiet today.

## Summary

The MrNasdog Pressure Framework reads Uniswap's UNI at **−0.14% net** over the last 90 days and **−0.27%** over the next 90: a fixed **5M UNI** quarterly growth-budget release from the DAO treasury against a fee-funded burn that destroyed **5.78M UNI** and has run faster since the **Jul 27 2026** fee votes. UNI has never been minted and total supply still reads **1B**, with **112.09M UNI** already at the burn address. The key risk is that the burn depends on trading volume and on the UNI price, while the release does not. The ceiling on new supply is the **267.25M UNI** treasury plus a **2%** a year mint right, neither of which has a schedule beyond the growth budget.

*MrNasdog Pressure Framework analysis of UNI, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 24 2026.*

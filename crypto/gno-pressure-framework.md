---
title:         "GNO Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "GNO supply is flat: 0.00% net over 90 days and 0.00% next. No GNO can be minted, and a July redemption of about 167K GNO stayed in the DAO treasury, not burned."
canonical_url: "https://mrnasdog.com/research/gno/inflation"
tags:          ["crypto", "gno", "gnosis", "dao"]
published:     true
---

Originally published at [GNO Inflation Analysis · September 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/gno/inflation).

# GNO Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

The MrNasdog Pressure Framework reads GNO at **0.00% net** over the trailing 90 days and **0.00%** over the next 90: **0 GNO** of new sell pressure against **0 GNO** of buy pressure, on a circulating supply of **2.64M GNO**. The GNO token has no function that can create coins, and the biggest supply story of the window — the GnosisDAO treasury redemption, which took in about **167,000 GNO** in July — moved coins from holders into a DAO treasury that is already counted as circulating, so it neither added to nor removed from the market. The monitor reads **−0.04%**, a gap of **0.04 points**.

      
## The verdict, in one paragraph

      
GNO's net supply change over the last 90 days is **0.00%**, and the projection for the next 90 days is also **0.00%**. The inflation monitor, which tracks the circulating count day by day, reads **−0.04%** over the same window. The gap between the two readings is **0.04 percentage points**, far inside the 0.5-point tolerance, so no data-conflict warning is shown. The monitor's small negative number is day-to-day noise around a circulating count that did not change. GNO is a **fixed-supply token with a flat float**: nothing was minted, nothing vested, nothing was burned, and the large treasury flows of the summer all stayed inside the market.

      
## Sell pressure: where new GNO comes from

      
Protocol inflation is **0 GNO**, and it cannot be anything else. The GNO token on Ethereum is a plain token: its code exposes only transfer, approval and balance functions, with no mint, no burn and no owner. Its on-chain total read **10M GNO** at both ends of the window. Of that, **3.15M GNO** sits at the zero address from past burns and **3.85M GNO** sits in a DAO vesting pot pledged to be burned, which leaves the 3M GNO supply the project targets. Gnosis Chain validators are paid in GNO, but those rewards come out of GNO that already exists, funded by GnosisDAO, not out of new coins. The GNO copy on Gnosis Chain grew by **46,852 GNO** in the window, exactly in step with the GNO locked in the bridge on Ethereum.

      
Vesting unlocks are **0 GNO**. The DAO's 8-year vesting pot, set up in November 2020, still holds **3.85M GNO** and did not release a single coin in the window. Its last move was the 3.15M GNO burn of Jan 30 2025, and GnosisDAO has committed to a 3M total supply, which means the rest is meant to be burned too. The pot runs until Nov 2028.

      
Foundation and unscheduled unlocks are **0 GNO**. The only pot of GNO that sits outside the circulating count is Gnosis Ltd's vesting contract, holding **360,411 GNO**. It is fully vested and did not move in the window; its last payout was 50,000 GNO on May 14 2025, more than a year ago, so there is no pattern to project forward.

      
Long-term locked or bankruptcy is **0 GNO**. There is no bankruptcy estate and no court-ordered payout. About **309,739 GNO** is staked with Gnosis Chain validators, but staked GNO is already inside the circulating count, so even the planned release of that stake adds nothing new.

      
## Buy pressure: where new GNO goes

      
Programmatic buyback is **0 GNO**. GnosisDAO bought about $1.46M of GNO on the open market between Apr 16 and May 8 2026, before this window, and has paused market buying while holders have a redemption route. Bought GNO lands in the DAO treasury, which the circulating count already includes.

      
Protocol fee burn is **0 GNO**. Gas on Gnosis Chain is paid in a stablecoin, not in GNO, so there is no fee burn. The zero-address balance stayed at **3,147,806 GNO** from the first day of the window to the last.

      
Foundation buy is **0 GNO**, and this is the row with the most activity behind it. Under the GnosisDAO redemption approved in June, holders could hand in GNO or staked GNO for a share of the DAO treasury between Jul 3 and Jul 17 2026. Holders handed in **111,074 GNO** and **48,261 staked GNO** (worth about 56,007 GNO), about **167,000 GNO** in all. On Jul 17 2026 every one of those coins was sent to the DAO's main safe, where they still sit. They were kept, not burned: the zero-address balance and the token total did not change. Because the DAO's safe is counted as circulating, the redemption moved coins from one part of the market to another and removed nothing.

      
New long-term lock is **0 GNO**. The Gnosis Chain staking contract shrank from **323,919 GNO** to **309,739 GNO** as validators left, and staking never takes GNO out of the circulating count in the first place.

      
## Foundation and overhang

      
Four GNO pots are tracked as team-controlled overhang. The first is Gnosis Ltd's vesting contract with **360,411 GNO**, fully vested and outside the circulating count — the one pot whose release would add new GNO to the market. The second is the DAO's 8-year vesting pot with **3.85M GNO**, outside even the 3M total and pledged to be burned. The third is the DAO's main safe, holding about **1.24M GNO** across Ethereum and Gnosis Chain plus **56,257 staked GNO**, most of it older treasury plus the July redemption intake. The fourth is a DAO liquidity wallet with about **115,039 GNO**. The last two are already counted as circulating, so a sale from them would move GNO within the market rather than add to it.

      
Every pot is re-read on the chain at each refresh. If the Gnosis Ltd vesting contract or the DAO vesting pot shrinks between refreshes and the coins are not burned, the outflow enters the foundation row at the next refresh. If the DAO burns the redeemed GNO, that burn enters the buy side.

      
## How GNO compares to other fixed-supply DAO tokens

      
GNO belongs to the group of fixed-supply governance tokens backed by a large treasury. Unlike an uncapped proof-of-stake coin such as ETH or SOL, where validators are paid in new coins every epoch, GNO has no issuance at all: Gnosis Chain pays its validators out of existing GNO, so the cost of security shows up as a treasury expense rather than a rising supply. The GnosisDAO proposal to turn Gnosis Chain into an Ethereum rollup describes that subsidy as a dilution of non-stakers of about 2.3% a year, but it is a transfer of existing GNO, not new supply.

      
Compared with exchange tokens that burn a share of revenue every quarter, GNO has no fee burn, because gas on its chain is paid in a stablecoin. Its supply only ever fell through one-off governance burns, such as the 3.15M GNO burn of January 2025. And compared with DAO tokens that run a buyback into a burn address, the GnosisDAO buyback and redemption both parked GNO in the treasury. That choice keeps GNO's float flat until the DAO decides to burn what it holds.

      
## What to watch in the next 90 days

      
First, the Gnosis Chain move onto Ethereum, approved by GnosisDAO in August, targets its first block around December 2026 or January 2027; at that point the validator set retires and about 350,000 staked GNO is freed. That GNO is already circulating, so it would not change the framework reading, but it could reach the market quickly. Second, any GnosisDAO vote to burn the roughly 167,000 GNO taken in through the redemption, or the 3.85M GNO left in the DAO vesting pot, would show up as buy pressure. Third, any payout from the Gnosis Ltd vesting contract, which holds 360,411 GNO, would be the only way new GNO enters the market. Fourth, GNO cashback for Gnosis Pay card users ends on Sep 30 2026, and the consumer card shuts on Dec 20 2026, which removes one steady source of GNO paid out to users.

      
## Summary

      
The MrNasdog Pressure Framework reads GNO at **0.00%** net supply change over the last 90 days and **0.00%** over the next 90 days, in line with the monitor's **−0.04%**. GNO cannot be minted, Gnosis Chain validators are paid from existing GNO, and the GnosisDAO treasury redemption of about 167,000 GNO stayed inside the circulating count because the DAO kept the coins rather than burning them. The key risk to the reading is a release from the 360,411 GNO Gnosis Ltd vesting contract, the only pot outside the circulating count; the key upside is a DAO decision to burn the GNO it holds. GNO's total supply is set at 3M by governance; its circulating count can rise only if those 360,411 GNO are paid out, and fall only through burns.

*MrNasdog Pressure Framework analysis of GNO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

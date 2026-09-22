---
title:         "GNO Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "GNO supply held flat over 90 days at 0.00%: a 167K GNO treasury redemption moved coins into the DAO, not to a burn. See the ledger, vesting and burn checks."
canonical_url: "https://mrnasdog.com/research/gno/inflation"
tags:                    ["crypto", "gno", "gnosis", "dao"]
published:     true
---

Originally published at [GNO Inflation Analysis · September 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/gno/inflation).

# GNO Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

GNO's tradable float did not move over the last 90 days, and the Pressure Framework reads it at **0.00%** over the trailing 90 days and **0.00%** for the next 90, against a monitor reading of **−0.11%**. The quarter's headline event, a GnosisDAO treasury redemption in which holders handed back about **167K GNO**, moved those coins into the DAO's own treasury rather than destroying them, and that treasury is already counted as circulating. Sell pressure is **0**, buy pressure is **0**, and the GNO token contract has no way to mint a new coin.

## The verdict, in one paragraph

Against a circulating base of **2.64M GNO**, the framework books **0** of sell pressure and **0** of buy pressure over the trailing 90 days, a net of **0.00%**, and projects **0.00%** for the next 90 days. The inflation monitor reads **−0.11%** for the same window, a gap of **0.11 percentage points**. That is inside the framework's 0.5-point tolerance, so the overview ships with no monitor-gap warning. The small monitor dip is day-to-day rounding in a supply figure that has in fact stayed at one number all quarter. The earlier reading of a shrinking float, built on the idea that the July redemption retired coins, does not survive a check of where the coins went. The label for GNO this quarter is **a capped token with a flat float**: large coin movements inside the DAO, no net change for the market.

## Sell pressure: where new GNO comes from

It does not come from minting. Sell #1, protocol inflation, is **0**, and it is one of the few rows on any page that can be called permanent. The GNO contract on Ethereum wrote its supply of **10M GNO** once, at launch, and carries only nine functions: transfers, approvals and read-only views. None of them can create a coin, and the stored supply figure sat at exactly **10M GNO** at both ends of the window. Of those 10M, about **3.15M GNO** were burned in January 2025 and **3.85M GNO** sit in a vesting contract committed to burning, which is why Gnosis describes its supply as 3M. The GNO that lives on Gnosis Chain is a bridged copy: it rose by **44,557 GNO** over the window while the GNO locked in the Ethereum-side bridge rose by the same amount, and the two match to within **232 GNO**, so nothing is counted twice. Gnosis Chain validators are paid in GNO, but those payments come out of a staking pot the DAO filled with existing GNO. They move coins from one counted wallet to another; they do not add any.

Sell #2, vesting unlocks, is **0**. GnosisDAO's eight-year vesting contract, started on **Nov 23 2020**, still holds **3.85M GNO**, of which roughly **1.68M GNO** has vested and could be withdrawn. Nothing was withdrawn: the balance did not change by a single unit across the 90 days. These coins sit outside the counted supply and the DAO has committed to burning them to reach its 3M target, so a withdrawal is not expected. Sell #3, Foundation and unscheduled unlocks, is **0**: the Gnosis Ltd vesting contract, the one pot the circulating figure leaves out, did not move. Sell #4, long-term locked or bankruptcy, is **0**. GNO has no bankruptcy estate and no court-ordered distribution.

## Buy pressure: where new GNO goes

Buy #1, programmatic buyback, is **0**. GnosisDAO's open-market GNO buying last ran from **Apr 16 to May 8 2026**, before this window opened, and has been paused since so that holders can use the redemption instead. Buy #2, protocol fee burn, is also **0**. Gas on Gnosis Chain is paid in xDAI, not GNO, so there is no fee burn to speak of. The framework still read both places a burn could appear, at both ends of the window: the zero address held **3.15M GNO** on both dates, the dead address did not move, and the count of GNO in existence held at **10M**. Nothing was destroyed.

Buy #3, Foundation buy, is **0**, and this is the row that needs the most care. Governance proposal GIP-151, passed on **Jun 26 2026**, let any holder hand GNO back to GnosisDAO for a share of the treasury. Between **Jul 3 and Jul 17 2026**, **92** holders sent in **111,074 GNO** and **48,261** staked GNO, about **167K GNO** in all. On **Jul 17 2026** every one of those coins was moved into the DAO's main treasury, where they still sit. The proposal calls them removed from circulation, but that is a label, not a location: the circulating figure the framework divides by already includes the DAO treasury, and nothing was burned. The coins moved from one counted wallet to another, so they take nothing off the market. Buy #4, new long-term lock, is **0**: GNO in the validator deposit contract fell from **330K** to **311K**, and staked GNO counts as circulating in any case.

## Foundation and overhang

GNO's overhang is large and almost entirely in GnosisDAO's hands. The DAO's main treasury holds **1.24M GNO** across Ethereum and Gnosis Chain, plus **56K** staked GNO, much of it from the redemption, and a DAO liquidity wallet holds another **111K GNO**. All of this is already inside the circulating figure, so selling it would not show up as new supply in this ledger, though it would reach the market. Outside the float sit two vesting contracts: the DAO's **3.85M GNO**, committed to burning, and Gnosis Ltd's **360,411 GNO**, fully vested since November 2025 and withdrawable at any time. Gnosis Ltd last withdrew **50K GNO** on **May 14 2025**, and before that in 2022 and 2021, so its releases are rare and unscheduled. Every one of these balances is readable on chain and refreshed at each rebuild. If either vesting contract's balance falls between refreshes, that outflow enters Sell #3, or Sell #2, at the next refresh.

## How GNO compares to other capped governance tokens

GNO sits in the strictest supply class: a token whose contract cannot mint at all. That is a harder promise than a halving chain like Bitcoin, which still issues new coins every block, and much harder than an uncapped proof-of-stake chain, where staking rewards are printed and the supply grows every year. On Gnosis Chain the staking rewards exist, but they are paid out of GNO the DAO already holds, so the cost falls on the treasury rather than on the supply count.

The redemption makes the most useful comparison. Exchange tokens that buy back and burn take coins out of existence, and their readings go negative. GnosisDAO did something that looks similar, swapping treasury assets for GNO, but kept the coins. That is closer to a company buying its own shares and holding them as treasury stock: the holder count shrinks, but the shares can be reissued. Until those coins are burned, a buy-and-hold treasury does not reduce the float the market can see.

The vesting picture also differs from most tokens. A typical project releases investor and team coins into the market over four years. GnosisDAO's largest vesting pot is instead scheduled for destruction, so its end state removes supply rather than adds it, and none of it is counted as circulating today.

## What to watch in the next 90 days

First, the **167K GNO** from the redemption: a vote to burn it would be the first real removal since January 2025, while a sale from the treasury would put it back into trading hands. Second, the move of Gnosis Chain onto Ethereum, approved as GIP-153 on **Aug 19 2026** and targeted for around the turn of the year: it ends the treasury-paid staking rewards and frees about **350K** staked GNO, which is already counted as circulating but could reach the market as validators exit. Third, Gnosis Ltd's **360,411 GNO** vesting pot, the only excluded balance that can be withdrawn at any time. Fourth, the DAO's **3.85M GNO** vesting contract, where any withdrawal not followed by a burn would count as new supply. The forward window runs to **Dec 21 2026**.

## Summary

The MrNasdog Pressure Framework reads GNO at **0.00%** over the trailing 90 days and **0.00%** projected forward: mixed flows, supply roughly steady. The GNO contract cannot mint, nothing was burned, and neither vesting contract released a coin. The July GIP-151 redemption moved about **167K GNO** into the GnosisDAO treasury, which is already counted as circulating, so it changed who holds GNO but not how much trades. The key risk is that the DAO's **1.24M GNO** treasury and the **350K** staked GNO due to unlock can both reach the market at the DAO's or validators' choosing, while the hard ceiling of **10M GNO** minus burns cannot be raised by anyone.

MrNasdog Pressure Framework analysis of GNO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 22 2026.

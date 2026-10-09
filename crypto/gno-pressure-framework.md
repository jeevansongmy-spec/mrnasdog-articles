---
title:         "GNO Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description:   "GNO supply is flat: 0.00% net over 90 days and 0.00% next. No GNO can be minted, and about 167K GNO from the July redemption stayed with the DAO, not burned."
canonical_url: "https://mrnasdog.com/research/gno/inflation"
tags:          ["crypto", "gno", "gnosis", "dao"]
published:     true
---

Originally published at [GNO Inflation Analysis · October 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/gno/inflation).

# GNO Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

**GNO supply was flat over the last 90 days and is set to stay flat for the next 90.** No new GNO can be created: the Ethereum token has no mint function, and the total is held at **3M GNO**, of which **2.64M** circulate. We count **0 GNO** of sell pressure and **0 GNO** of buy pressure, a net change of **0.00%**, against **−0.0004%** on our monitor. The one large flow of the window, about **167,081 GNO** handed back to GnosisDAO in the July treasury redemption, was kept by the DAO rather than burned, so it did not shrink the circulating count.

## The verdict, in one paragraph

Over the 90 days from Jul 11 2026 to Oct 9 2026, GNO's net supply change was **0.00%**, and our projection for the next 90 days is also **0.00%**. Our monitor, which tracks the market's circulating count day by day, reads **−0.0004%** for the same window. The gap is **0.00 percentage points**, far inside our 0.5-point tolerance, so no warning chip is shown. One caution sits under that agreement: the market's circulating figure for GNO has read the same number every day since early January 2026, so a flat monitor here proves less than it would for a coin whose count moves. We therefore checked the chain directly at both ends of the window, and it agrees. GNO is a fixed-supply coin with a quiet ledger: nothing was printed, nothing was burned.

## Sell pressure: where new GNO comes from

**Protocol inflation is 0 GNO.** The GNO token on Ethereum was created once, with 10M units, and its code has no way to add more: it holds only the standard transfer and approval functions. Its total read exactly 10M at both ends of the window. About 3.15M of those sit at the zero address after a burn in January 2025, and about 3.85M sit in the DAO's 8-year vesting contract, which GnosisDAO has pledged to burn as it vests. That leaves the 3M GNO everyone counts. Gnosis Chain stakers are paid in GNO, but those rewards come out of coins that already exist: the staking contract paid out **77,329 GNO** and took in **66,478 GNO** during the window, and its balance fell by exactly the difference. The GNO copy on Gnosis Chain grows only when GNO is locked on Ethereum; both sides rose by the same 38,860 GNO.

**Vesting unlocks are 0 GNO.** The DAO's vesting contract did not release a single coin this window, and its last release was the January 2025 burn. Because its coins are already left out of the 3M total, a future release only matters if the DAO stops burning it.

**Foundation and unscheduled unlocks are 0 GNO.** Gnosis Ltd's own vesting contract holds **360,411 GNO**, and it is the only GNO left out of the circulating count. It finished vesting in November 2025, so Gnosis Ltd can claim it at any time, but it last paid out 50,000 GNO on May 14 2025 and nothing left it this window.

**Long-term locked or bankruptcy supply is 0 GNO.** No court estate or trustee holds GNO. About 308,000 GNO is staked on Gnosis Chain, but staked GNO already counts as circulating.

## Buy pressure: where new GNO goes

**Programmatic buyback is 0 GNO.** GnosisDAO's treasury manager did buy GNO on the market this year, about $1.58M in the first quarter and $1.46M between Apr 16 and May 8 2026, then paused while the redemption ran. No buys were reported in this window, and bought GNO lands in the DAO's Safe, which the market already counts as circulating.

**Protocol fee burn is 0 GNO.** Gas on Gnosis Chain is paid in xDAI, so using the chain burns no GNO, and the burn addresses on Ethereum did not grow.

**Foundation buy is 0 GNO.** This is where the big story of the window sits. Under the one-time treasury redemption that GnosisDAO approved in June, holders could hand back GNO for a share of the treasury until Jul 17 2026. They returned **111,074 GNO** and **48,261 staked GNO**, about **167,081 GNO** in all. Every coin went to the DAO's main Safe and stayed there; none was burned. The DAO calls these coins removed from circulation, but the market's count still includes that Safe, so the circulating number did not fall.

**New long-term lock is 0 GNO.** A forum idea to lend the DAO's stablecoins against GNO locked for five years has not gone to a vote.

## Foundation and overhang

Two piles of GNO sit outside the market today. Gnosis Ltd's fully vested contract holds **360,411 GNO** that could be claimed any day without a vote. The DAO's 8-year vesting contract holds **3.85M GNO**, released over time until November 2028 and pledged for burning; if a release were kept instead of burned, it would be new supply. Inside the market count, the DAO holds its main Safe with about 832,000 GNO on Gnosis Chain, 414,000 GNO on Ethereum and 56,000 staked GNO, plus a liquidity wallet of about 115,000 GNO. We read every one of these balances from the chain at each rebuild. If any of them falls between rebuilds, the outflow enters the foundation row at the next refresh.

## How GNO compares to other DAO treasury tokens

GNO behaves less like a chain coin and more like a share in a large treasury. Most Layer 1 coins pay stakers with newly printed coins; Ethereum, for example, adds new ETH every day and burns only part of it back. Gnosis Chain also pays stakers in GNO, but the DAO funds those rewards from coins it already holds, so the supply stays fixed while the DAO's own pile slowly shrinks. GnosisDAO itself has said this costs non-stakers about 2.3% a year in dilution of their share of the treasury, even though the coin count never moves.

Compared with exchange tokens that buy back and burn on a schedule, GNO has no standing buyback and no burn tied to use. Its supply cuts came in large, voted steps instead: the 3M target, then a 3.15M burn in January 2025. The July 2026 redemption was a different kind of step: holders swapped GNO for treasury assets, but the DAO kept the coins rather than destroying them.

Against other governance tokens with big treasuries, GNO is unusual in how little is still locked. Only about 12% of the 3M sits outside the market count, all in one contract, while the DAO's much larger holdings are already counted as circulating. That makes GNO's supply easy to read: a move only matters if it burns coins or releases the one locked contract.

## What to watch in the next 90 days

**Ethereum rollup genesis, around the turn of the year.** GnosisDAO voted on Aug 19 2026 to move Gnosis Chain into the Ethereum Economic Zone. That ends the treasury-paid staking rewards and frees the staked GNO, but staked GNO already counts as circulating, so it adds nothing to our count.

**What the DAO does with the redeemed GNO.** About 167,081 GNO sits in the DAO's main Safe. A vote to burn it would take it out of the market for good and show up as buy pressure; selling it would not change the count.

**Gnosis Ltd's 360,411 GNO.** A claim from its vesting contract would be the one way new GNO reaches the market, and it would enter our foundation row in full.

**Whether buybacks restart.** The treasury manager paused buys for the redemption; its next quarterly report should say whether they resume.

## Summary

GNO is a fixed-supply coin: **3M GNO** in total, **2.64M** circulating, and no way to mint more. Over the last 90 days nothing was printed or burned, so net supply moved **0.00%**, in line with our monitor, and the next 90 days look the same. The largest flow, a redemption that returned about 167,081 GNO to GnosisDAO, stayed inside the market count because the coins were kept, not burned. The main risk to the supply is the 360,411 GNO in Gnosis Ltd's vesting contract, which can be claimed at any time; the main upside would be a DAO vote to burn the redeemed coins.

*MrNasdog Pressure Framework analysis of GNO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 9 2026.*

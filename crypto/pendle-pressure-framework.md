---
title:         "PENDLE Inflation Analysis · August 2026 · Mixed flows, supply roughly steady"
description:   "PENDLE mints nothing; a pre-minted reserve releases ~1.2M/90d and a fee-funded buyback removes ~1.14M to stakers. Framework +0.03% net; monitor +1.45%."
canonical_url: "https://mrnasdog.com/research/pendle/inflation"
tags:          ["crypto", "pendle", "defi", "inflation"]
published:     true
---

*Originally published at [mrnasdog.com/research/pendle/inflation](https://mrnasdog.com/research/pendle/inflation)*

Pendle (PENDLE) **has not minted a single token in over a year**: the ERC-20's total supply read exactly **281.53M** to the wei at both ends of the last 90 days. What looks like emission is a pre-minted incentive reserve draining — about **1.2M PENDLE** released over the window — and it is almost exactly offset by a fee-funded buyback that pulled about **1.14M PENDLE** off the market and gave it to stakers. The framework nets PENDLE at about **+0.03%** over the next 90 days. Our supply monitor reads the trailing 90 days at **+1.45%**, a gap that is a measurement artifact of buyback-and-hold, not new issuance.

## The verdict, in one paragraph

For the window opening Aug 2 2026, the MrNasdog Pressure Framework reads **PENDLE at about +0.03% net** supply change over the next 90 days — roughly **1.2M PENDLE** of incentive-reserve release against about **1.14M PENDLE** of buyback removal, on a circulating base of about **171.80M**. Our supply monitor reads the realized last-90-day change at **+1.45%**, a gap of about **1.41 percentage points**, so a monitor-gap warning does ship. The gap is expected and mechanical: Pendle's buyback removes PENDLE from the open market but delivers it to sPENDLE stakers, who the monitor's circulating source still counts as circulating, so the monitor cannot see the float sink and also picks up staking-side reclassification. On the on-chain reality — a flat total supply and a reserve that drains almost exactly as fast as the buyback absorbs — PENDLE is a **fixed-supply token whose float is roughly steady**.

## Sell pressure: where new PENDLE comes from

Sell #1 — protocol inflation — is about **1.2M PENDLE** over 90 days, but it is not a mint. Pendle's total supply read exactly **281.53M** at both ends of the window, so no new PENDLE was created. What the row measures is a transfer out of a pre-minted incentive reserve: the reserve wallet fell from **22.05M** to **20.85M**, releasing about **1.2M PENDLE** to reward distributors and the market. This is the token's so-called terminal emission, and it was cut hard — Pendle's Algorithmic Incentive Module reduced the underlying rate by about **71%**, so the reserve now drains slowly and the schedule points at a smaller number each quarter, never a larger one.

Sell #2 — vesting unlocks — is **zero**. Pendle's team, investor and advisor allocations are fully unlocked, and no cliff lands inside this window; every remaining non-circulating token sits in the incentive reserve behind Sell #1, not in a locked founder tranche. Sell #3 — Foundation and unscheduled unlocks — is also **zero** in booked value: the roughly **109.73M** of non-circulating PENDLE is the incentive-reserve multisig plus the ecosystem and liquidity-incentive distributor pools that fund the scheduled emission already counted in Sell #1, and there is no separate discretionary sale on top of that schedule. Sell #4 — long-term locked or bankruptcy — is **zero**, because no bankruptcy estate, trustee schedule or court-ordered distribution attaches to PENDLE.

## Buy pressure: where new PENDLE goes

Buy #1 — programmatic buyback — is the whole buy side, at about **1.14M PENDLE** over 90 days, and it is the mechanism that makes Pendle interesting. About **80% of protocol revenue** is used to buy PENDLE on the open market every two weeks, spread over the following week as an hourly time-weighted purchase, and the bought PENDLE is distributed to sPENDLE stakers. Summing every PENDLE transfer into the buyback contract over the window gives about **1.14M PENDLE** across **520** purchases — real fee revenue converted into real market buying. Because the tokens are handed out as staked sPENDLE, they are a genuine float sink even though staking is liquid with a 14-day exit.

Buy #2 — protocol fee burn — is **zero**: Pendle does not burn PENDLE. Fees are not destroyed, they are used to buy PENDLE for stakers, and the flat 281.53M total supply confirms nothing is sent to a burn address. Buy #3 — Foundation buy — is **zero**; no discretionary team or foundation buying was observed separate from the protocol buyback already counted. Buy #4 — new long-term lock — is deliberately **zero** to avoid double-counting: the PENDLE bought back is delivered to sPENDLE stakers, and that staking absorption is already inside Buy #1. Booking the same tokens again as a fresh lock would count them twice, and sPENDLE's 14-day-exit staking is not a multi-year lock in any case.

## Foundation and overhang

Pendle's standing overhang is the incentive reserve itself rather than a founder or investor treasury. Total supply is **281.53M** against about **171.80M** circulating, so roughly **109.73M PENDLE** is non-circulating. That splits into the **incentive-reserve multisig** holding about **20.85M**, refreshed by direct chain read, and the **ecosystem and liquidity-incentive distributor pools** holding about **89M**, which feed the scheduled terminal emission. None of this is a discretionary sell overhang in the usual sense — it is a published emission schedule that the framework already books through Sell #1, now running about 71% slower than before the Algorithmic Incentive Module. If the reserve multisig's balance falls faster between refreshes than the schedule implies, that extra outflow enters Sell #3 at the next refresh.

## How PENDLE compares to other fee-funded DeFi tokens

PENDLE belongs to the class of **DeFi protocol tokens that convert fee revenue into buy pressure** rather than into a burn. That places it between two extremes. On one side sit uncapped continuous-emission tokens and classic ve(3,3) DEX tokens, where fresh supply arrives every epoch forever and the only question is how fast dilution runs. On the other sit fee-burning platform tokens that permanently destroy supply out of revenue and reach genuinely negative net supply. Pendle sits in the middle by design: it stopped minting entirely, so its dilution problem already has a finish line, but instead of burning it recycles revenue into buybacks that are handed to stakers.

The important structural difference from a burn model is where the bought tokens go. A burn removes supply for good; Pendle's buyback moves supply from the open market into sPENDLE, where it stays counted as circulating and can return through the 14-day exit. That is exactly why our monitor reads **+1.45%** while the framework reads **+0.03%** — the monitor sees the reserve release enter circulation but cannot see the buyback take float back out, because staked PENDLE never leaves the circulating count. Measured on total supply, which has been flat at **281.53M** for over a year, PENDLE is neither inflationary nor deflationary. It is a capped, non-minting token whose emission is a reserve drain and whose buy side is a revenue-funded buyback of roughly equal size.

## What to watch in the next 90 days

Watch the **incentive-reserve multisig**: at about 20.85M and draining roughly 1.2M a quarter after the emission cut, its release rate is the single biggest driver of Sell #1, and a re-acceleration would be the first thing to push net supply up. Watch **protocol revenue**, because the buyback is 80% of it — if fees fall, the roughly 1.14M-per-quarter buy side shrinks and the reserve release stops being offset; if fees rise, the buyback can exceed the release and turn PENDLE net-deflationary on the float. Watch for any further **Algorithmic Incentive Module** adjustment, since a second cut would lower Sell #1 again. Watch the **sPENDLE staking rate**, now above 100M tokens staked, as it governs how much of each buyback is genuinely locked away. And watch total supply directly: any print above **281.53M** would be the first new PENDLE mint in over a year and would change the entire reading.

## Summary

Pendle is a fixed-supply, non-minting token: the PENDLE contract has read exactly 281.53M for over a year, so there is no issuance to dilute holders. Its only sell pressure is a pre-minted incentive reserve releasing about 1.2M PENDLE per 90 days — a rate just cut about 71% by the Algorithmic Incentive Module — and that is almost exactly cancelled by a fee-funded buyback that removed about 1.14M PENDLE to sPENDLE stakers over the same window, leaving the framework at roughly +0.03% net. The monitor's higher +1.45% is a measurement artifact: it counts the reserve release into circulation but cannot see the buyback take float back out, because staked PENDLE stays counted as circulating. The key variable from here is protocol revenue: it funds the buyback, so a strong revenue quarter can tip PENDLE net-deflationary while the reserve release keeps shrinking.

*MrNasdog Pressure Framework analysis of Pendle (PENDLE), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated August 2 2026.*

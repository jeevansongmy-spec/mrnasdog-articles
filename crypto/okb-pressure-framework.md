---
title: "OKB Inflation Analysis · July 2026 · Mixed flows, supply roughly steady"
description: "A MrNasdog Pressure Framework read of OKB: fixed at 21M with mint and burn removed from the token contract. Framework 0.00% net; the supply monitor agrees at +0.007%."
canonical_url: "https://mrnasdog.com/research/okb/inflation"
tags: ["crypto", "okb", "okx", "exchange-token"]
published: true
---

> Originally published at **[mrnasdog.com/research/okb/inflation](https://mrnasdog.com/research/okb/inflation)** by MrNasdog.

OKB, the OKX exchange token and the gas token of X Layer, sits at a fixed **21,000,000** supply, with both the mint and the burn functions removed from the OKB token contract in the August 2025 upgrade — nothing issues new OKB and nothing destroys it. The MrNasdog Pressure Framework therefore reads OKB at a flat **0.00% net** over the last 90 days and the next 90 days. Our independent supply monitor reads **+0.007%** across the same window, a gap of **0.007 percentage points** — agreement, not conflict.

## The verdict, in one paragraph

For the 90-day window ending **Jul 19 2026**, the Pressure Framework reads **OKB at 0.00% net**: every sell row and every buy row in the OKB ledger is zero, so the supply does not move in either direction. Our supply monitor reads the realized last-90-day change at **+0.007%** — a drift of about fifteen hundred OKB on a twenty-one million float, which is rounding noise in a circulating figure derived from market cap divided by price, not an actual issuance. The gap between the two readings is **0.007 percentage points**, far inside the framework's half-point tolerance, so OKB ships with **no monitor-gap flag**. The label for OKB is **capped but flat**: a hard-capped exchange token with no remaining issuance and, equally, no remaining burn.

## Sell pressure: where new OKB comes from

It does not come from anywhere. Sell #1, protocol inflation, is **zero**: the OKB token contract was upgraded on **Aug 18 2025** to strip out the mint function, so the implementation now running has no path to create a new OKB. That upgrade followed the **Aug 15 2025** burn of **65,256,712.097 OKB** drawn from historical repurchases and treasury reserves, which cut total supply by more than half and set it at exactly **21,000,000**. Sell #2, vesting unlocks, is **zero** because OKB is fully unlocked — its circulating supply equals its total supply equals its maximum supply, all three at 21M, and the original distribution schedule expired in 2018. There is no team, investor or treasury tranche still vesting.

Sell #3, Foundation and unscheduled unlocks, is **zero** as a flow. This is the row that usually carries an exchange token's real risk, and in OKB's case the reserve that would have populated it was itself the fuel for the 2025 burn — those tokens were destroyed, not parked. Every one of the remaining 21M OKB is counted as circulating, so there is no off-market bucket that could be released into the float. Sell #4, long-term locked or bankruptcy, is **zero**: OKB has no bankruptcy estate, no trustee schedule and no court-ordered distribution overhanging it. All four sell rows are structurally zero, and none of them can turn non-zero without a change to the token contract itself.

## Buy pressure: where new OKB goes

The buy side is empty for the mirror-image reason. Buy #1, programmatic buyback, is **zero**. OKX ran a quarterly buyback-and-burn for years, funded by a share of exchange trading fees, and the final report under that programme covered the quarter ending in May 2025. The August 2025 tokenomics upgrade retired it and removed the burn function alongside the mint function, so repurchased OKB can no longer be destroyed. Buy #2, protocol fee burn, is **zero**. X Layer, the Polygon-CDK zkEVM Layer 2 that OKX operates, uses OKB as its mandatory gas token — but those gas fees accrue to the network's sequencer and keep circulating. There is no base-fee burn on X Layer; gas consumption on this chain does not equal deflation.

Buy #3, Foundation buy, and Buy #4, new long-term lock, are both **zero**: no discretionary open-market accumulation is disclosed and no new multi-year escrow was announced in the window. The precision matters here. Even a large OKX repurchase today would not register as buy pressure in the inflation sense, because there is no longer a burn path — the tokens would simply move between wallets inside a fixed 21M supply, changing custody without changing the float.

## Foundation and overhang

OKB carries no identified team-controlled overhang in the supply sense. The reserve OKX accumulated across years of quarterly buybacks was consumed by the August 2025 burn, and after that burn the entire **21,000,000** supply is reported as circulating — there is no separate locked treasury bucket left to release. One structural detail worth noting: the OKB balance held on Ethereum is now only about **429.1K OKB**, because the Ethereum version of the token has been phased out in favour of OKB issued natively on X Layer; the cross-chain total is unchanged at 21M. The framework re-walks the token contract state and the circulating figure on each rebuild, and if any identified balance ever moved in a way that signalled a supply change, that outflow would enter Sell #3 at the next refresh. The one caveat the framework records is that the OKB token contract sits behind a proxy that still has a live owner — the mint and burn removal is the current implementation's behaviour rather than mathematically irreversible immutability, which is exactly why every OKB row is tagged as hand-checked rather than permanent.

## How OKB compares to other exchange tokens with hard caps

OKB now sits in a very small class: **exchange tokens with a fixed cap and no active supply mechanism at all**. The dominant exchange-token model is a recurring buyback-and-burn that grinds a larger float down over years — a genuinely deflationary token whose supply changes every quarter, and which the framework scores on the size of each burn. OKB took the opposite route. Instead of shrinking gradually, it executed one very large burn straight to a hard cap and then removed the ability to mint or burn at all. That makes OKB a fixed-supply token rather than a deflationary one: the supply is frozen, not falling, and the framework scores it accordingly rather than rewarding it for the historical burn.

The natural analogue is Bitcoin's hard cap, but the two arrive there differently. Bitcoin approaches 21M asymptotically through halvings stretched across a century, so it still prints a small positive inflation figure today; OKB is already at its permanent 21M with no issuance schedule left to run, so it prints exactly zero. Against uncapped continuous-emission Layer 1s, the contrast is sharper still — those chains fund security through perpetual staking issuance and read persistently positive, while OKB funds nothing through issuance because it has none. And against gas tokens with an EIP-1559-style base-fee burn, OKB differs on the mechanism that matters most: rising X Layer usage raises demand for OKB without removing a single token from supply.

## What to watch in the next 90 days

The single most important watch item is the OKB token contract itself: as long as the running implementation keeps mint and burn removed, the framework stays pinned at 0.00%, and because the proxy still has an owner, a future implementation change is the one event that could move any row. Second, watch OKX's announcements channel for any statement reintroducing a burn or buyback programme — the last entry under the old buy-back-burn schedule dates to Jun 23 2025, and a new one would be a tokenomics change rather than routine news. Third, watch X Layer throughput and gas revenue: growing usage strengthens the demand case for OKB but will not register on this ledger unless a burn is introduced. Fourth, watch for any disclosure of an OKX corporate OKB holding being segregated or locked, which would create a Sell #3 overhang where none exists today. Finally, expect the framework and the supply monitor to keep agreeing near flat, with the monitor oscillating by a few thousandths of a percent around exactly 21M.

## Summary

OKB is the OKX exchange token and the mandatory gas token of X Layer, with a supply fixed at **21,000,000** since the August 2025 burn of 65,256,712.097 OKB and the contract upgrade that removed both minting and burning. Nothing adds OKB and nothing removes it, so the MrNasdog Pressure Framework reads a flat **0.00% net** across both the trailing and forward 90-day windows, against a supply monitor reading of **+0.007%** — a 0.007 percentage-point gap that confirms rather than challenges the primary read. The structural fact is that OKB is capped but flat: it earns no credit for shrinking supply because its supply no longer shrinks. The key risk is not dilution but reversibility — the token contract remains behind an owned proxy, so the absence of a mint function is a maintained state rather than a mathematical guarantee.

---

*MrNasdog Pressure Framework analysis of OKB, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 19, 2026.*

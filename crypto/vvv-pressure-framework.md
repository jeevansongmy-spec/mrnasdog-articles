---
title:         "VVV Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "VVV supply is growing: team vesting of 1.23M and 666K new staking coins beat a 128.7K revenue burn: +3.08% net in 90 days, about +3.46% next despite cuts."
canonical_url: "https://mrnasdog.com/research/vvv/inflation"
tags:          ["crypto", "vvv", "venice", "ai"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/vvv/inflation](https://mrnasdog.com/research/vvv/inflation)*

# VVV Inflation Analysis · September 2026 · Supply growing · projected to keep growing

VVV, the token of the private AI app Venice on Base, is inflationary: over the last 90 days **2,006,244 VVV** reached the market against **519,319 VVV** taken off it, a net rise of **+3.08%** of the **48.25M** VVV in circulation. Team vesting is the biggest source and staking rewards the second, while Venice's revenue buy-and-burn removes far less. The next 90 days look similar, at about **+3.46%**, even after the staking emission is cut to 2M VVV a year on Oct 1 2026.

## The verdict, in one paragraph

For the 90 days to **Sep 29 2026**, the Pressure Framework reads VVV at **+3.08%** net: sell pressure of **2,006,244 VVV** against buy pressure of **519,319 VVV**, on a circulating supply of **48.25M VVV**. The inflation monitor reads **+2.37%** for almost the same window, a gap of **0.71 points**, which is over our 0.5-point line, so the page carries a ⚠ monitor gap chip. We traced the gap to one date: on **Aug 17 2026** the supply figure the monitor reads dropped by about 319,000 VVV when a team vesting contract holding exactly **319,458 VVV** was moved onto its locked list. No coins moved on-chain that day; added back, the monitor would read about **+3.05%**, close to ours. Our number stays. For the next 90 days we project **1,742,514 VVV** of sell pressure against **73,922 VVV** of buying, or **+3.46%**. VVV is inflationary on the active float: unlocks and emission outrun the burn.

## Sell pressure: where new VVV comes from

Protocol inflation added **666,444 VVV**. The VVV contract has one way to make new coins, a mint that only the staking contract can call, and that contract creates VVV every second at a rate Venice sets. The rate was cut from 4M a year to 3M on **Jul 1 2026** and to 2.5M on **Sep 1 2026**, both read directly on-chain. In total **702,956 VVV** were minted in the window; 666,444 went to stakers, who already count as circulating, and 36,512 went to the Venice treasury, which only counts once it is spent. On **Oct 1 2026** the rate falls again, to 2M VVV a year, so the next 90 days should add about **470,721 VVV** to stakers.

Vesting unlocks added **1,230,829 VVV**, the largest row. Venice's team allocation streams out of two on-chain vesting contracts second by second. The main one released **1,185,254 VVV** in 90 days and runs until **Jan 27 2027**, with about 1.53M VVV still to go; a smaller one released 45,574 VVV and holds about 0.30M across streams that end between 2027 and 2030. Holders withdraw almost as fast as the coins vest, so we count what actually left the contracts. The next 90 days should release about **1,192,655 VVV**.

Foundation and unscheduled unlocks added **108,971 VVV**. The biggest part is a monthly payment of about 26,000 VVV from the Venice treasury, seen on Aug 2, Aug 31 and Sep 29 2026, which totals **79,138 VVV** and is expected to keep going at the same pace. The liquidity wallet sent out 20,699 VVV and a second company wallet 9,134 VVV, both one-off. Long-term locked or bankruptcy supply added **0**: there is no estate, and the 1.5M VVV granted to the July 2026 funding round investors is locked until Jul 2027.

## Buy pressure: where new VVV goes

The programmatic buyback destroyed **128,732 VVV**. Venice spends part of its revenue buying VVV on the open market and sending it to a burn address. Every paid plan triggers a small burn, and since **Jul 17 2026** every API credit purchase does too ($5 of every $100): these small burns came to **61,828 VVV**. A monthly batch burned 23,178 VVV on Jul 9, 27,163 on Aug 7 and 16,563 on Sep 8, a further **66,904 VVV**. Because the burns are sized in dollars and VVV now trades above $27, the same spending buys fewer coins: we project about **73,922 VVV** for the next 90 days.

The protocol fee burn is **0**, because fees on Base are paid in ETH and VVV has no built-in fee burn. Foundation buying is **0**: Venice's buying goes into the burn, not onto its books. A new long-term lock is **0** as well: about 33.2M VVV is staked and 8.3M of it is locked to make DIEM, Venice's daily API-credit token, but staked coins still count as circulating. The fifth row, coins moved into company wallets, took **390,587 VVV** off the market: 275,001 into a second company wallet on Jul 28 and Aug 13 2026, and 115,586 into the liquidity wallet from pool work and open-market buys in July. These were one-off moves, so the next 90 days count none.

## Foundation and overhang

Venice controls a large pool of VVV that sits outside the circulating count. The main treasury holds **20.74M VVV** and also receives about 5% of every new emission; a second company wallet holds **8.63M VVV**; the liquidity wallet holds **1.57M VVV**; and the two team vesting contracts still hold **1.57M** and **0.30M VVV**. Together that is about 32.8M VVV, roughly two-thirds of today's float. Only the vesting contracts and the monthly treasury payment have a set pace; the rest has no published schedule. The July 2026 investors also hold a 1.5M VVV grant and warrants for up to 5M more, locked until Jul 2027. We read these wallets on-chain at every rebuild: if any of their balances fall between refreshes, the outflow enters Sell #3 at the next refresh.

## How VVV compares to other staking-reward app tokens

VVV sits between two common designs. Like many proof-of-stake chains, it pays stakers in new coins with no hard cap on supply, but unlike a chain whose rate is fixed in protocol code, Venice sets the VVV rate itself and has cut it again and again, from 14M a year at launch to 2M from Oct 1 2026. That makes VVV's emission low and falling, about 4% a year of the float, but also a company decision rather than a rule.

On the buy side, VVV looks like the app tokens that route revenue into buy-and-burn. The difference is size: VVV's burns are real and grow with Venice's sales, but in this window they removed about **7%** of what emission and vesting added. Tokens with a fee burn built into the chain destroy coins with every transaction; VVV only burns what the company chooses to spend. Until the team vesting ends in Jan 2027, VVV behaves like a young token still working through its unlock schedule, and the burn cannot keep up.

## What to watch in the next 90 days

The staking emission cut from 2.5M to 2M VVV a year on **Oct 1 2026** removes about 120,000 VVV from the next 90 days. The monthly revenue burn, which has landed around the 7th to 9th of each month, shows whether Venice's dollar budget rises with its revenue. The monthly treasury payment, last seen on **Sep 29 2026**, is due again in late October. The main team vesting stream keeps releasing about 12,700 VVV a day until it ends on **Jan 27 2027**, just after this window. Any further emission cut, or any large move out of the treasury or the second company wallet, would change this reading.

## Summary

VVV, the Venice Token on Base, grew its circulating supply by **+3.08%** over the last 90 days and is projected to grow about **+3.46%** over the next 90. Team vesting of about 1.2M VVV per quarter and staking rewards of about 0.5M per quarter outweigh a revenue buy-and-burn that removes well under 0.1M VVV per quarter at today's price. The main risk is the 32.8M VVV held by Venice outside the float, which has no schedule. The pressure should ease after the team vesting ends on Jan 27 2027, when staking emission of 2M VVV a year becomes the main source of new supply.

---

*MrNasdog Pressure Framework analysis of VVV, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

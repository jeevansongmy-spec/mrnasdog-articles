---
title: "CAKE Inflation Analysis · October 2026 · Supply shrinking · projected to keep shrinking"
description: "CAKE supply is shrinking: PancakeSwap's weekly fee buyback burned 7.23M CAKE against 2.36M added, net -1.53% over 90 days and about -1.17% expected next."
canonical_url: "https://mrnasdog.com/research/cake/inflation"
tags: ["crypto", "cake", "pancakeswap", "defi"]
published: true
---
> Originally published at **[mrnasdog.com/research/cake/inflation](https://mrnasdog.com/research/cake/inflation)** by MrNasdog.

<!-- main-page -->
This is the long supply read. For the signal, the price drivers and the questions people ask about PancakeSwap, see [mrnasdog.com/research/cake](https://mrnasdog.com/research/cake).

# CAKE Inflation Analysis · October 2026 · Supply shrinking · projected to keep shrinking

PancakeSwap's CAKE supply is shrinking. Over the 90 days to Oct 5 2026 the weekly fee buyback burned **7.23M CAKE**, while pool rewards and old staking locks added **2.36M CAKE**, so the float fell by a net **1.53%**. At today's price the same buyback dollars burn about **5.51M CAKE** in the next 90 days, for a projected **−1.17%**. The supply cap is **400M CAKE**, and today about **336M** exist.

## The verdict, in one paragraph

Our ledger reads CAKE at **−1.53%** net over the last 90 days and **−1.17%** projected for the next 90, on a circulating supply of **318.31M CAKE**. The inflation monitor reads **+2.55%**, a gap of **4.08 percentage points**, which is over our 0.5-point line, so the page carries a ⚠ monitor gap note. We walked the gap: the monitor's last read, on Oct 1 2026, landed in a burn week, when **11.99M CAKE** minted on Sep 30 2026 was still waiting to be burned on Oct 5 2026. Those coins never reached the market. Without them, the same supply series falls about **1.47%** from Jul 3 to Oct 1 2026, close to our number, and the rest is dates and price rounding. In one line: CAKE is a deflationary DEX token, shrunk by a revenue-funded buyback that is about three times larger than everything added.

## Sell pressure: where new CAKE comes from

The first source is the PancakeSwap emission. The MasterChef contracts mint new CAKE for every BNB Chain block, but almost all of it is sent straight back to the burn wallet the same week. Only a thin share is kept as rewards for special pools, and over these 90 days that kept emission was **1,612,146 CAKE**, about 17,900 a day. The posted schedule is a little higher, about 21,750 a day, because pool rewards nobody claims are burned too. Roughly half of the kept CAKE went to PancakeSwap's ecosystem wallet, which grew from **4.53M** to **5.49M CAKE**.

Vesting unlocks add **0**. CAKE never had team or investor vesting: every coin was born in the per-block mint, and that mint only ever paid the reward contracts and the burn wallet.

Foundation and unscheduled unlocks add **0**. The ecosystem wallet only received coins in this window, and those coins were already counted when they were minted, so spending them later would not add new supply.

The old staking locks added **747,572 CAKE**. PancakeSwap retired its vote-escrow lock in 2025, and holders are still taking their coins out of two old lock contracts, which fell from **19.35M** to **18.60M CAKE**. One lump of **575,065 CAKE** left between Aug 26 and Aug 28 2026; the rest is a slow weekly drip. We only project the drip, about **172,500 CAKE**, for the next 90 days, because lumps like August's have no schedule.

## Buy pressure: where new CAKE goes

The programmatic buyback is the main event. A share of PancakeSwap's trading fees buys CAKE on the open market, and every week those coins are burned at a dead address no one can spend from. In 13 weekly burns this window, the buyback destroyed **7,231,412 CAKE**, worth about **$13.7M** at the price of each week. The biggest week was mid-September, near 888,000 CAKE, when trading picked up. Because the buyback spends dollars, not a fixed number of coins, we project the next 90 days at today's price of about $2.49: the same dollars burn about **5.51M CAKE**.

The protocol fee burn from side products was small, **7,213 CAKE**, including 3 CAKE that holders burned themselves. After a June 2026 vote, most side-product fees now go to the PancakeSwap treasury instead of the burn, so this line should stay small.

Foundation buying adds **0**: no team wallet bought CAKE outside the weekly burn. New long-term locks add **0** too: long locks ended with the 2025 tokenomics change, and CAKE staked in pools today can leave at any time, so it still counts as circulating.

## Foundation and overhang

We track four piles that could reach the market. The ecosystem wallet, a multisig run by the team, holds about **5.49M CAKE** and only took coins in this window; its coins already count as circulating. The two old lock contracts still hold **18.60M CAKE** that belongs to holders who have not yet withdrawn; every coin that leaves them enters the market. The treasury that now receives side-product fees has no public address, so we follow it through governance posts and the monthly burn reports. Last, the cap leaves room for about **64M** more CAKE above today's supply, but there is no plan to mint into it. We read these balances on-chain at every rebuild. If any of them falls between rebuilds, the outflow enters the sell side at the next rebuild.

## How CAKE compares to other DEX tokens

Among exchange tokens, CAKE sits with the buy-and-burn group. Its burn is paid from real trading fees, in dollars, and it runs every week, so the shrink rate follows how much people trade on PancakeSwap. When volume and fees rose in September, the weekly burn rose with them; when trading cools, the burn shrinks, while the emission stays the same every block.

Many DEX tokens work the other way: they keep printing rewards for liquidity providers and use little or none of their fees to buy back. Those tokens grow their supply by design. Some others buy back but park the coins in a treasury wallet instead of burning them, which leaves a pile that can come back. CAKE's bought coins go to a dead address, which is the stronger version.

The trade-off is that CAKE's cap is a vote, not code. The 400M cap was set by a January 2026 vote and the mint function is still live, so the limit depends on governance staying disciplined.

## What to watch in the next 90 days

First, the weekly burns: each one shows whether trading fees can keep buying at the September pace now that CAKE costs almost twice what it did in July. Second, the monthly burn report for September, due in the first half of October 2026, which should confirm the mint and burn totals. Third, any new vote on emissions, the cap or fee splits; no proposal is open as of Oct 5 2026. Fourth, the old lock contracts: another lump like August's would raise the sell side. Fifth, the ecosystem wallet: if it starts paying out large amounts, we will see it on-chain.

## Summary

PancakeSwap's CAKE is shrinking: a weekly fee buyback burned **7.23M CAKE** in 90 days against **2.36M** added by pool rewards and old staking locks, for a net **−1.53%**, with about **−1.17%** projected next. The engine is real trading revenue spent on open-market buybacks that are sent to a dead address. The key risk is that the burn depends on trading fees and on the price: slower trading or a higher CAKE price means fewer coins burned, while the emission does not change. The ceiling is a 400M cap set by vote, about 64M above today's supply.

---

*MrNasdog Pressure Framework analysis of CAKE, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 5 2026.*

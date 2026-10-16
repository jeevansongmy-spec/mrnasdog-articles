---
title: "CAKE Inflation Analysis · October 2026 · Supply shrinking · projected to keep shrinking"
description: "CAKE supply is shrinking: PancakeSwap's weekly fee buyback burned 7.15M CAKE against 2.34M added, net -1.51% over 90 days and about -1.49% expected next."
canonical_url: "https://mrnasdog.com/research/cake/inflation"
tags: ["crypto", "cake", "pancakeswap", "defi"]
published: true
---
> Originally published at **[mrnasdog.com/research/cake/inflation](https://mrnasdog.com/research/cake/inflation)** by MrNasdog.

<!-- main-page -->
This is the long supply read. For the signal, the price drivers and the questions people ask about PancakeSwap, see [mrnasdog.com/research/cake](https://mrnasdog.com/research/cake).

# CAKE Inflation Analysis · October 2026 · Supply shrinking · projected to keep shrinking

CAKE supply is shrinking. Between Jul 18 and Oct 16 2026, the PancakeSwap fee buyback burned **7,153,053 CAKE**, while only **2,344,685 CAKE** reached the market from the farm mint and from old locks. That leaves a net change of **−1.51%** of circulating supply in 90 days and about **−1.49%** expected in the next 90 days, close to the monitor's **−1.32%**. The CAKE buyback is paid in dollars from swap fees, so its size moves with trading volume and the CAKE price, and a draft from Oct 14 2026 could change both sides of the CAKE ledger if it passes a vote.

## The verdict, in one paragraph

Our 90-day reading for CAKE is **−1.51%**: **7,160,266 CAKE** left the circulating supply through burns and **2,344,685 CAKE** entered it, against **317.95M CAKE** in circulation. The monitor reads **−1.32%** for a window that ends a week earlier, a gap of **0.19** percentage points. That is inside our 0.5-point tolerance, so no warning chip is needed and the two readings agree on the direction and roughly the size. For the next 90 days we expect about **−1.49%**. In one line: PancakeSwap is a fee-funded buyback-and-burn DEX token, deflationary because the weekly burn is about three times the new CAKE.

## Sell pressure: where new CAKE comes from

Protocol inflation is the farm mint. The CAKE contract mints 44 CAKE every block, but nearly all of it is burned straight back by the farm contracts: of **767.3M CAKE** minted in the window, only **1,612,264 CAKE** stayed in the market, about 17,900 a day. The setting would allow up to **21,741 CAKE** a day for farms, the lottery and an incentive fund, so the kept amount ran at about 82% of that ceiling. Close to **970,000 CAKE** of the kept mint went to the PancakeSwap team's ecosystem wallet, which is used for incentives and partner deals. With no vote on a new emission level, the next 90 days keep the same rate.

Vesting unlocks are zero. CAKE launched in 2020 as a farm token with no presale and no investor allocation, so there is no unlock calendar and no cliff to wait for.

Foundation and unscheduled unlocks are also zero. The ecosystem wallet only took coins in during the window and sent out just 1,000 CAKE in the last 30 days. It already counts as circulating, so a sale from it would move coins between holders and add no new CAKE.

The one live long-term-lock row is the slow emptying of the old CAKE lock contracts. PancakeSwap retired locking on Apr 23 2025, and holders who never collected are still taking their coins out. **732,421 CAKE** left the two old contracts in the window, and those coins were not counted as circulating while they sat there. One single withdrawal of **575,065 CAKE** between Aug 26 and Aug 28 2026 made up most of it. A lump like that has no pattern, so the next 90 days count only the slow drip, about **157,000 CAKE**.

## Buy pressure: where new CAKE goes

The programmatic buyback is the engine. Each week a share of swap fees from PancakeSwap v2, v3 and Infinity buys CAKE on the market and sends it to the burn address. Over 13 weekly batches the buyback burned **7,153,053 CAKE**, worth about **$14.0M** at the time; single weeks ranged from 316,000 to 888,000 CAKE, with the biggest weeks in early September when trading was busy. Because the buyback is a dollar amount, the same money buys fewer CAKE when the price rises: at **$2.16** on Oct 16 2026 it buys about **6.50M CAKE** in the next 90 days.

The protocol fee burn from side products is now small: **7,213 CAKE**. In a vote that closed on Jun 21 2026, holders agreed to send the fees of products other than the swap pools to the PancakeSwap treasury instead of burning them, and those products made up less than 2% of fees.

There was no foundation buy: nothing outside the weekly buyback shows the team or the treasury buying CAKE. New long-term locks are zero as well, because there is no lock to enter any more. The old lock contracts can only shrink.

## Foundation and overhang

The largest team-run wallet is the ecosystem wallet, a 3-of-7 multi-signature wallet that receives part of the CAKE farm mint. It held about **5.57M CAKE** on Oct 16 2026, up from 4.60M on Jul 18 2026, and we read its balance on-chain every day. It counts as circulating, so its coins are booked once, when they are minted. The PancakeSwap treasury, which collects side-product fees and stablecoin-pool fees, does not publish a CAKE balance, so we follow it through governance posts.

Holders, not the team, still have **15.83M CAKE** in the two retired lock contracts (5.19M and 10.64M). Every coin that leaves them enters the circulating supply, and we read both balances on-chain every day. The 400M cap that holders voted for in January 2026 leaves about **64.5M CAKE** of room above today's supply; the cap is a promise rather than a limit in the token code, and there is no plan to use the room. If any of these balances falls between refreshes, the outflow enters the sell side of the ledger at the next refresh.

## How CAKE compares to other DEX tokens

Among exchange tokens on decentralized exchanges, CAKE is one of the few that burns more than it prints, and it does so with real fees rather than a fixed burn calendar. Uniswap's UNI went the same direction only in early October 2026, when holders approved its fee switch and burned a large block of treasury UNI; CAKE has run a weekly buyback-and-burn since 2023 and reported 37 months in a row of net burns. The difference is that UNI has no farm mint to offset, while CAKE still prints new coins every block and must burn more than that just to shrink.

Vote-escrow DEX tokens, where holders lock coins for years to steer emissions, work the opposite way: the lock takes coins off the market, but weekly emissions are large and mostly go to lockers. PancakeSwap left that model in 2025. It retired locking, cut emissions from about 40,000 to 22,500 CAKE a day, and moved the value to the buyback. The cost of that switch shows up in our ledger as the old locks slowly emptying back into the market.

Compared with buyback tokens that keep the coins they buy in a treasury, the PancakeSwap buyback destroys every coin it buys, so no team wallet grows from it and no later sale can bring those coins back. That makes the CAKE buy side easy to check on-chain, but it also means the burn depends on swap volume: when trading slows, the weekly burn falls, and the CAKE farm mint does not.

## What to watch in the next 90 days

The Flip vote: the draft opened on Oct 14 2026 would give liquidity providers 88% of v3 and Infinity swap fees and cut new CAKE from 22,500 to 7,000 a day, but it would also stop the v3 and Infinity burns and leave v2 as the main burn source; if it passes, the team plans to roll it out from November 2026 to the end of January 2027.

The weekly burn report every Monday: the burn fell from about 888,000 CAKE in mid-September to about 500,000 in October, and a lower weekly figure is the first sign that the buy side is weakening.

The old lock contracts: another lump like the 575,065 CAKE withdrawal in late August 2026 would add to the sell side, and 15.83M CAKE could still come out.

The ecosystem wallet: it has been filling up, so a large transfer out of its 5.57M CAKE would be the first sign that the team is spending its share.

## Summary

CAKE, the PancakeSwap token, is deflationary: the weekly fee buyback burned **7,153,053 CAKE** in 90 days against **2,344,685 CAKE** of new and unlocked supply, a net **−1.51%**, with about **−1.49%** expected next. The mechanism is simple to check: PancakeSwap mints CAKE for farms every block and burns more than that each week with swap-fee money. The main risk is the Oct 14 2026 draft that would hand most v3 and Infinity fees to liquidity providers and stop their burns, together with any drop in trading volume. The 400M cap and the ongoing burns keep the supply pointing down for now.

---

*MrNasdog Pressure Framework analysis of CAKE, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 16 2026.*

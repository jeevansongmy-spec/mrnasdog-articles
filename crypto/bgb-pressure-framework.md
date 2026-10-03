---
title:         "BGB Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description:   "BGB supply is flat at 0.00% over 90 days. The contract cannot mint, and the 3.01M BGB Morph burn came from a locked treasury, so the 699.99M float did not move."
canonical_url: "https://mrnasdog.com/research/bgb/inflation"
tags:          ["crypto", "bgb", "bitget", "exchange"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/bgb/inflation](https://mrnasdog.com/research/bgb/inflation)*

# BGB Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

**BGB** (Bitget Token) has a flat float: the MrNasdog Pressure Framework counts **0 BGB** of sell pressure and **0 BGB** of buy pressure on the **699.99M BGB** in circulation, a net of **0.00%** over the last 90 days and **0.00%** projected for the next 90. The BGB contract on Ethereum cannot mint, and the quarterly Morph burn of **3.01M BGB** on Jul 14 2026 was paid out of the locked Morph Foundation treasury, not out of the float. The one real overhang is that treasury: **210.93M BGB**, allowed to release up to 2% of its original 220M a month but so far releasing nothing.

## The verdict, in one paragraph

Bitget Token's circulating supply did not change in the 90 days to Oct 3 2026: net **0.00%**, with **0.00%** expected for the next 90 days. The circulating count our monitor is built on also reads **+0.00%** over the same 90 days, so the gap is **0.00 percentage points** — well inside the 0.5-point line, and no warning chip is needed. Total supply did fall, from 913.93M to 910.92M BGB, because of the Jul 14 2026 burn, but every burned coin came from a pile that was never counted as circulating. The cite-able label for BGB today is a **fixed-mint exchange token with a treasury-funded burn**: real destruction, no change to the tradable float.

## Sell pressure: where new BGB comes from

**Protocol inflation is 0 BGB.** The BGB contract on Ethereum is a plain token contract that created all 2,000,000,000 BGB once, when it was deployed, and has no function to create more — no mint, no owner, no upgrade path. On the Morph network BGB is the gas token, but gas is paid with BGB that already exists: the 22.70M BGB on Morph match, to the last unit, the 22.70M BGB locked in the bridge on Ethereum.

**Vesting unlocks are 0 BGB.** Unlock trackers list Bitget Token as fully unlocked, and no investor or team cohort still has a vesting cliff. The only schedule left is the Morph Foundation treasury, which may release up to 2% of 220M BGB a month — about **4.4M BGB**, or roughly 13.2M in a 90-day window. The Morph Foundation calls that a ceiling, not an automatic payout, and the chain shows it has never been used: in the 13 months since the treasury was funded on Sep 4 2025, every coin that left it went to the burn address.

**Foundation and unscheduled unlocks are 0 BGB** this window, because the treasury sent nothing to the market. **Long-term locked or bankruptcy supply is 0 BGB**: no court estate or trustee holds BGB. The Sep 24 2026 hack at the Bitget exchange drained other assets from hot wallets; it did not create or release any BGB.

## Buy pressure: where new BGB goes

**The programmatic buyback is 0 BGB.** Bitget's old plan to spend part of its profit buying and burning BGB last fired in Jul 2025, when about 30M BGB were burned, and was replaced in Sep 2025 when Bitget handed 440M BGB to the Morph Foundation — 220M burned at once, 220M locked. Nobody buys BGB on the open market to burn it today.

**The protocol fee burn books 0 BGB on the float, even though it is real.** The Morph quarterly burn takes the network's fees for the quarter, divides by the average BGB price, and multiplies the result by a booster. For Apr–Jun 2026 that was $4,071 of fees at $1.92, times a booster of 1,420, which gave **3,010,400 BGB**, sent to the burn address on Jul 14 2026. We read the burn address and the treasury at both ends of the window: the burn address rose by exactly 3,010,400 BGB and the treasury fell by exactly the same amount. Since the treasury was never part of the circulating count, the float lost nothing.

**Foundation buying is 0 BGB**: the treasury has received nothing since its first deposit. **New long-term locks are 0 BGB**: Morph staking locks BGB for 90 days in a pool capped at 2M BGB, but staked coins still count as circulating, so staking does not shrink the float.

## Foundation and overhang

The Morph Foundation treasury is the one overhang that matters. It holds **210.93M BGB**, which is the whole gap between total supply (910.92M) and circulating supply (699.99M), to the unit. It started at 220M BGB on Sep 4 2025 and has paid out only to the burn address: 3.06M in Jan 2026, 3.00M in Apr 2026 and 3.01M in Jul 2026. Its rules let it release up to about 4.4M BGB a month for builders, liquidity and growth, so this is the coin's largest possible source of new float.

Outside the treasury, one wallet holds about 229.5M BGB and about 30 large multi-signature wallets hold between a few million and 54M each. All of them are already counted as circulating, so a transfer from them to an exchange moves supply within the float rather than adding to it — a market risk worth knowing, not a supply change. We re-read the treasury on every rebuild; if its balance falls between refreshes and the coins go anywhere but the burn address, the outflow enters Sell #3 at the next refresh.

## How BGB compares to other exchange tokens

Exchange tokens usually shrink supply through a buyback-and-burn paid from exchange profit. In that design, coins are bought from the market, so each burn takes coins out of the circulating float and the float shrinks quarter by quarter. BGB moved away from that design in Sep 2025. Its burn is now sized from fees on the Morph network and paid from a locked treasury, so total supply keeps falling while the tradable float does not.

Compared with exchange tokens whose burns come from market purchases, BGB looks weaker on the float: its burn removes nothing that a trader could have sold. Compared with exchange tokens that still mint rewards or carry large team unlocks, BGB looks stronger: there is no mint, no vesting cliff, and no unlock that has actually fired. The fixed 2B contract with no mint function puts BGB closer to hard-capped coins than to inflationary Layer 1 gas tokens, even though it now pays for gas on Morph.

The open question for BGB, unlike most exchange tokens, is the size of the burn itself. Morph fees for Apr–Jun 2026 were only $4,071, so the 3.01M BGB burn relied almost entirely on the 1,420 booster. If governance lowers the booster, the burn shrinks; if the treasury runs low after many quarters, the burn would have to come from somewhere else — and only a burn funded from the float would show up as buy pressure here.

## What to watch in the next 90 days

**The Q3 2026 Morph burn**, covering Jul 1 to Sep 30 2026, should land around mid-Oct 2026 if it follows the last three (Jan 23, Apr 9 and Jul 14 2026). We will check where it is paid from: from the treasury it books 0, from the float it becomes buy pressure.

**Any treasury release.** A first transfer from the Morph Foundation treasury to anywhere other than the burn address would be the first new BGB to reach the market, up to about 4.4M a month.

**Booster and governance votes.** A Morph vote that changes the booster or the governance factor changes the size of every later burn.

**The fallout from the Sep 24 2026 hack.** Bitget reopened withdrawals in steps from Sep 28 2026. Any sale of BGB from large in-float wallets would move price, but not the supply count.

## Summary

Bitget Token (BGB) has a flat circulating supply: **0.00%** over the last 90 days and **0.00%** expected over the next 90, against **+0.00%** on the monitor's circulating count. The BGB contract cannot mint, and the quarterly Morph burn — **3.01M BGB** on Jul 14 2026 — is paid from the locked Morph Foundation treasury, so it cuts total supply without touching the float. The key risk is that treasury: **210.93M BGB** that may release up to 4.4M a month, though it has released none so far. The ceiling on BGB supply is fixed at the 2B ever minted, less the 1.09B BGB already burned.

*MrNasdog Pressure Framework analysis of BGB, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 3 2026.*

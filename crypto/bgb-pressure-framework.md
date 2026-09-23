---
title:         "BGB Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "BGB supply is flat at 0.00% over 90 days. The quarterly burn is real, but it draws on a locked Morph Foundation reserve, so the 700.0M BGB float does not move."
canonical_url: "https://mrnasdog.com/research/bgb/inflation"
tags:          ["crypto", "bgb", "bitget", "exchange"]
published:     true
---

Originally published at [BGB Inflation Analysis · September 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/bgb/inflation).

# BGB Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

BGB's tradable supply is flat: the Pressure Framework reads Bitget Token at **0.00%** over the last 90 days and **0.00%** for the next 90, against a monitor reading of **+0.29%**. The quarterly burn is real — **3.01M BGB** was destroyed on **Jul 14 2026** — but every burned coin came out of the locked Morph Foundation reserve, never from the market, so sell pressure is **0** and buy pressure is **0**. The BGB contract on Ethereum has no mint function, so the **2,000M** ever created is a hard ceiling.

## The verdict, in one paragraph

Against a circulating base of **700.0M BGB**, the framework books **0** of sell pressure and **0** of buy pressure over the trailing 90 days — a net of **0.00%** — and projects **0.00%** for the next 90 days. The inflation monitor reads **+0.29%** for the same window, a gap of **0.29 percentage points**, which is inside the framework's 0.5pp tolerance, so the overview ships with no warning chip. The monitor estimates supply from market value divided by price, and that estimate wobbles by a few tenths of a percent around a circulating figure that, read directly on chain, did not change by a single coin across the window. The label for BGB is a **deflating total with a frozen float**: the count of BGB in existence keeps falling each quarter, while the amount anyone can trade stays exactly where it was.

## Sell pressure: where new BGB comes from

It does not come from minting. Sell #1, protocol inflation, is **0**. The BGB token contract on Ethereum carries only the standard transfer and allowance functions — no mint, no owner, no upgrade path — and its supply counter read **2,000M BGB** at both ends of the window. That counter lives in ordinary contract storage rather than in the code, so a flat reading is a real measurement, not a frozen constant. BGB also lives on the Morph network, where it pays for gas; the Morph copy is only created when the same amount is locked on Ethereum, and the Morph supply matched the Ethereum lock to the last decimal. Nothing new enters from either chain.

Sell #2, vesting unlocks, is **0**. BGB has no remaining team or investor vesting schedule. The one locked pot is the Morph Foundation reserve, created in September 2025 when Bitget handed **440M BGB** to the Morph Foundation, burned half at once and locked the other **220M BGB**. The Morph Foundation describes a release of up to **2% a month** for ecosystem programs, and its own FAQ says this is a ceiling, not an automatic release. The chain settles it: in more than a year, the reserve has never sent a single BGB to the market. Its only outflows were quarterly burns.

Sell #3, Foundation and unscheduled unlocks, is **0**, because no coin crossed from outside the tradable float into it during the window. Sell #4, long-term locked or bankruptcy, is **0** as well: BGB has no bankruptcy estate, no trustee and no court-ordered distribution.

## Buy pressure: where new BGB goes

Buy #1, programmatic buyback, is **0**. Bitget used to spend a share of its quarterly profit buying BGB on the market and burning it; the last of those burns was in July 2025. That program was paused in September 2025, when Bitget burned **220M BGB** in one step and passed the quarterly burn to the Morph Foundation. There has been no market buy-and-burn since.

Buy #2, protocol fee burn, is **0** on the float, and this is the row most worth explaining, because the burn genuinely happens. On **Jul 14 2026**, **3.01M BGB** was sent to the dead address for the second quarter of 2026. The Morph Foundation sizes each burn from Morph network fees, divided by the average BGB price and scaled up by a governance multiplier. The framework read both burn surfaces at both ends of the window: the dead address rose by exactly **3.01M BGB**, and the supply counter stayed at **2,000M**, because BGB burns by transfer rather than by shrinking the counter. The decisive fact is where the coins came from. They came from the Morph Foundation reserve, which fell by exactly the same amount — and that reserve is the only BGB the circulating figure leaves out. Burning coins that were never tradable removes nothing from the tradable float, so the float stayed at **700.0M BGB** at both ends.

Buy #3, Foundation buy, is **0**: neither Bitget nor the Morph Foundation bought BGB on the market, and the reserve received no coins at all in the window. Buy #4, new long-term lock, is **0**: BGB staking on Morph is small, runs for 90 days, and staked coins remain counted as circulating.

## Foundation and overhang

The first overhang is the Morph Foundation reserve itself: **210.9M BGB** at the end of the window, down from **213.9M** at the start, with the whole difference sent to the dead address. It is the only BGB outside the tradable float, and it is read from the chain at every rebuild. The second is a large Bitget-linked wallet holding **227.6M BGB**, which did not move by a single coin across the window. It is already counted as circulating, so it needs no unlock to reach an exchange — which makes it a bigger practical supply risk than the reserve. It is also read from the chain at every rebuild. A cross-chain lock pool holds the Ethereum side of the BGB on Morph; it mirrors coins already in circulation and is not a team holding. If the reserve's balance falls between refreshes by anything other than a burn, that outflow enters Sell #3 at the next refresh. The Bitget-linked wallet is different: it already sits inside the float, so its moves cannot change this reading, but they would matter to anyone watching the order book.

## How BGB compares to other exchange tokens with quarterly burns

Exchange tokens usually shrink through a quarterly burn, and most readers treat every burn as deflation. The mechanism matters more than the headline. When an exchange buys its token on the open market and burns it, coins leave the tradable float and the supply a holder competes with really gets smaller. When the burned coins come from a reserve the exchange or its foundation already held back, the total shrinks but the tradable float does not. BGB today is the second kind: its burn is funded from a locked reserve, so the number of BGB in existence falls each quarter while the float stays still.

On issuance, BGB is stricter than most chains. There is no staking emission, no block reward and no mint function — a harder commitment than a halving-model coin like Bitcoin, which still creates new coins every block, or a staking chain where new coins pay validators. The BGB ceiling of **2,000M** is written into a contract that cannot mint, and more than half of it has already been destroyed.

The practical comparison for a holder is scale. At the current pace of about **3M BGB** a quarter, the reserve would take well over a decade to burn through. For the burn to shrink the float, it would need to be funded by buying BGB on the market, as the older Bitget program was. That is the gap between a burn that happens and a burn that matters for the float.

## What to watch in the next 90 days

First, the third-quarter burn, expected around mid-October 2026: the thing to check is not the size but the sender — if it comes from the reserve again it stays at **0** here, and if it is bought on the market it becomes real buy pressure. Second, the Morph Foundation reserve at **210.9M BGB**: any outflow that does not end at the dead address would be its first real ecosystem release. Third, the Bitget-linked wallet at **227.6M BGB**, which could reach the market without any unlock. Fourth, Morph governance votes on the burn multiplier or the monthly release ceiling, both set by BGB holders. The forward window runs to **Dec 22 2026**.

## Summary

The MrNasdog Pressure Framework reads BGB at **0.00%** over the trailing 90 days and **0.00%** projected forward: mixed flows, supply roughly steady. The structural mechanism is a quarterly burn funded from a locked Morph Foundation reserve, so the total number of BGB falls while the tradable float of **700.0M BGB** does not move. The key risk is not inflation but concentration: a Bitget-linked wallet already inside the float holds **227.6M BGB**. The ceiling is firm — the BGB contract cannot mint, so the **2,000M** created is the most that can ever exist.

MrNasdog Pressure Framework analysis of BGB, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 23 2026.

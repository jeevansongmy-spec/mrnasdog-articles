---
title:         "FET Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "FET supply is growing: the native bridge created 352M FET in 90 days, 317M reached an exchange, plus 10.16M staking rewards — +14.15% net, no burn to offset."
canonical_url: "https://mrnasdog.com/research/fet/inflation"
tags:                    ["crypto", "fet", "fetchai", "ai"]
published:     true
---

Originally published at [FET Inflation Analysis · September 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/fet/inflation).

# FET Inflation Analysis · September 2026 · Supply growing · projected to keep growing

FET, the token of the Artificial Superintelligence Alliance (ASI Alliance), is strongly inflationary on the MrNasdog Pressure Framework: supply grew about **+14.15%** in the 90 days to Sep 29 2026 and is projected at about **+14.20%** for the next 90 days. Almost all of it comes from the native Fetch.ai chain, where the bridge contract created **352M FET** in six batches and **316.995M** reached an exchange wallet, with no Ethereum FET locked or burned to match. Staking added **10.16M**, and nothing was burned or bought back.

## The verdict, in one paragraph

Across the 90 days from Jul 1 to Sep 29 2026, FET sell pressure came to **327.16M FET** against a buy side of **0**, on a circulating supply of **2.31B FET**. That is a net of **+14.15%** in the window and **+14.20%** for the next 90 days. Our inflation monitor, which counts FET on Ethereum only, reads **+2.49%**, a gap of **11.67 percentage points**, so the page carries a ⚠ monitor gap chip. We walked every source class and found the reason: the monitor's whole move is the **55.7M FET** that left the Ethereum bridge, and it cannot see the native chain where the new FET is created. FET is a token whose headline supply stays flat on Ethereum while its native chain adds coins in large, dated batches.

## Sell pressure: where new FET comes from

The largest source is not a published emission at all. The FET native bridge contract on the Fetch.ai chain has a mint function, and its admin used it six times in the window: **60M** on Jul 3, **60M** on Jul 25, **62M** on Aug 5, **70M** on Aug 14, **40M** on Aug 28 and **60M** on Sep 18 2026. Every batch was tagged as an Ethereum-to-native swap. After each one, the admin withdrew the coins and sent them on, and **316.995M FET** reached a wallet set that behaves like an exchange: it pays out thousands of withdrawal-sized amounts and parks the rest in a cold wallet that grew from 487.68M to 625.76M FET. We counted the coins when they reached that exchange wallet, not when they were minted. We looked for the Ethereum side of the swap and found none: Ethereum FET supply stayed at 2,714,384,546.672, the burn address did not move, and the Ethereum bridge received only 25.6M FET in the whole window. The batches came about every two weeks, so the next 90 days carry the same **316.995M**.

Protocol inflation is the second source. The Fetch.ai native chain pays stakers new FET at a fixed 3% a year of native supply, a little every block. The chain ran at 5.71 seconds a block against a shorter target, so the real pace was closer to 2.6% a year: **10.37M** new FET in 90 days, of which **10.16M** went to stakers and 0.21M to the community pool. Because the bridge batches lifted the native supply the reward is paid on, the reward per block rose from about 6.7 to 8.4 FET, and the next 90 days come to about **11.20M**. The Ethereum FET token itself has no emission.

Vesting unlocks are **0**. The original FET team, sale and reserve allocations vested long ago, and the one published line left is a monthly model of leftover AGIX being swapped into FET after the 2024 merger. Those swaps have been paused since Sep 20 2026, and the pool that pays them was already counted as circulating. Foundation and unscheduled unlocks are **0**: none of the team's reserve wallets released coins to the market this window, apart from the bridge batches above. Long-term locked or bankruptcy releases are **0**. The Sep 19 2026 theft of 8.72M FET from a swap contract linking Ethereum and Cardano moved coins that were already circulating, so it added nothing new.

## Buy pressure: where new FET goes

Nothing left the FET float this window, so the buy side is **0**. There was no programmatic buyback: an earlier buyback plan exists on paper, but no purchase showed up on-chain between Jul 1 and Sep 29 2026. The protocol fee burn is **0**: FET supply on Ethereum and the burn address read the same at both ends, and on the native chain supply rose by exactly the new batches plus staking rewards. The last FET burns were 5M in early 2025 and 109,350 in late 2025, and a governance vote to burn a further 110M was rejected. There was no Foundation buy; a listed company kept adding FET through a custody wallet, but it buys on the open market, so those coins were already in the float. New long-term locks are **0**: the old Ethereum staking contract held 80.62M FET at both ends, and the roughly 608M FET staked on the native chain still counts as circulating.

## Foundation and overhang

Four Ethereum wallets hold exactly the FET that is not counted as circulating. The bridge's admin multisig holds **281.21M FET**, 200M of it moved in from the Ethereum bridge on Sep 23 2026. The Ethereum bridge itself holds **14.35M**, the old staking contract **80.62M**, and the Foundation multisig **26.69M**; that multisig also holds the only right to mint FET on Ethereum, a right that has not been used since 2024. On the native chain, the team holds another **72.50M** freshly created FET still inside the bridge contract, **29.27M** sent on Sep 23 2026 to a deposit wallet that has not moved on yet, and about 59.2M in the bridge admin's own account, most of it staked. Several large wallets that are counted as circulating also sit still, including a multisig set up at the 2024 merger with 277.55M and three wallets of 105M to 115M each that have never sent a transaction. We read these balances on-chain at each rebuild. If any of them falls between rebuilds, the outflow enters row 3, Foundation and unscheduled unlocks, at the next rebuild, or row 5 when it comes through the native bridge.

## How FET compares to other AI and multi-chain tokens

Most tokens with a chain of their own report one supply. FET reports the Ethereum ERC-20 supply, which has been flat at 2.71B since early 2026, while the native Fetch.ai chain keeps its own count that grew from 1.40B to 1.76B FET in this window. A bridged token normally keeps the two in step: a coin created on one side is matched by a coin locked on the other. FET's recent batches broke that link, which makes FET's headline supply a poor guide to how many coins actually reach the market.

Compared with Bittensor (TAO), which has a hard cap of 21M and a halving schedule, FET has no cap on the native side and no halving; its staking reward even rises as native supply grows. Compared with Render (RENDER), whose supply is mainly shaped by a burn-and-mint loop tied to paid work, FET has no working burn today. And compared with Ethereum-only AI tokens whose total supply is fixed in one contract, FET adds a second ledger with an admin mint. The comparison that matters is mechanism, not price: FET's new supply comes from discretionary bridge batches, not from a fixed curve that holders can plan around.

## What to watch in the next 90 days

First, the next native bridge batch: at the pace seen since Jun 19 2026, another 40M to 70M FET would be created roughly every two weeks, and any batch that reaches an exchange adds to row 5. Second, the 29.27M FET delivered on Sep 23 2026 to a deposit wallet: once it moves on, it joins the count. Third, when the paused bridge swaps and the AGIX-to-FET swaps restart after the Sep 19 2026 exploit; the modelled AGIX line for Oct 28 2026 books 0 because that pool already counts as circulating. Fourth, any explanation from the ASI Alliance of the Ethereum side of the bridge batches: if Ethereum FET turns out to be locked or burned to match, row 5 falls away and FET's 90-day reading drops to about +0.5%. Fifth, the 281.21M FET now in the bridge's admin multisig: a move out of it to the market would be new supply.

## Summary

FET, the ASI Alliance token, grew its supply about **+14.15%** in the 90 days to Sep 29 2026 and is projected at about **+14.20%** next, on the MrNasdog Pressure Framework. The driver is the Fetch.ai native bridge, which created 352M FET in six batches and passed **316.995M** to an exchange wallet with no Ethereum FET locked to match, on top of **10.16M** from staking; no burn or buyback offsets it. The key risk is that the batches are discretionary and unannounced, and 72.50M freshly created FET plus 281.21M in the bridge's admin multisig still sit ready. There is no cap on the native side, so the only ceiling is the admin's own choice.

*MrNasdog Pressure Framework analysis of FET, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

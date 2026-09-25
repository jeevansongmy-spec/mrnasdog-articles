---
title:         "ZEC Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description:   "Zcash supply growing: 161,234 ZEC mined over 90 days at 1.5625 per block, nothing burned, bought back or locked. +0.95% net, projected to keep growing."
canonical_url: "https://mrnasdog.com/research/zec/inflation"
tags:          ["crypto", "zec", "zcash", "privacy"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/zec/inflation](https://mrnasdog.com/research/zec/inflation)*

# ZEC Inflation Analysis · September 2026 · Supply growing, projected to keep growing

Zcash, the proof-of-work privacy coin, adds new ZEC with every block and removes none. Over the last 90 days the Zcash chain produced **103,190 blocks** at **1.5625 ZEC** each, issuing **161,234 ZEC**, while nothing was burned, bought back or locked. That puts the MrNasdog Pressure Framework reading for ZEC at **+0.95% net** over the last 90 days against a supply-monitor reading of **+0.96%** — a gap of **0.01 percentage points**, which is agreement, not conflict. ZEC supply follows a Bitcoin-style halving schedule toward a hard cap of **21M ZEC**, and the next Zcash halving is not due until about **Nov 2028**.

## The verdict, in one paragraph

For the 90-day window ending **Sep 25 2026**, the Pressure Framework reads **ZEC at +0.95% net**: the sell side added **161,234 ZEC** of fresh block rewards and the buy side removed **zero**. The independent supply monitor reads the realised 90-day change at **+0.96%**. The gap is **0.01 percentage points**, far inside the framework's half-point tolerance, so ZEC ships with **no data-conflict flag**. The forward column reads the same **+0.95%**, because the planned NU7 upgrade keeps Zcash issuance per day unchanged and no halving falls in the next 90 days. The label for ZEC is **a capped proof-of-work chain in its steady emission phase**: new supply arrives every 75 seconds at a fixed rate, and nothing on the chain takes any back.

## Sell pressure: where new ZEC comes from

Sell #1, protocol inflation, carries the whole Zcash sell side at **161,234 ZEC**. Every Zcash block pays a **1.5625 ZEC** subsidy, split three ways by consensus: **80%** to the miner, **8%** to the Zcash Community Grants fund and **12%** to a protocol-held development lockbox. All three shares are new ZEC the moment the block is mined, and all three are counted as circulating, so the framework books the full subsidy once and does not book it again when the development funds later spend it. The figure was measured, not assumed. The chain's own supply total rose by exactly **103,190 × 1.5625** ZEC across the window, to the last fraction of a coin, and the same check held at three points inside the window, including the block where the NU6.3 Ironwood upgrade activated on **Jul 28 2026**. Zcash ran slightly slow, at a measured **75.36 seconds** per block against its 75-second target. Because the Zcash block reward is paid per block and the difficulty rule does not repay lost time, the slow pace means fewer blocks and fewer ZEC — about **766 ZEC** less than a perfectly timed chain would have issued — so the measured block count is used.

Sell #2, vesting unlocks, is **zero**. The founders' reward that paid early Zcash backers ended with the Canopy upgrade in **Nov 2020**, and no unlock schedule remains; the two development-fund shares are paid out of each block and are already inside Sell #1. Sell #3, foundation and unscheduled unlocks, is **zero**: none of the team-linked ZEC balances released new coins into the market, and all of them already sit inside the counted float. Sell #4, long-term locked or bankruptcy supply, is **zero**: no estate or trustee is distributing ZEC, and the listed company that holds about **323K ZEC** bought those coins on the open market.

## Buy pressure: where new ZEC goes

Nowhere, and that is the other half of the Zcash story. Buy #1, programmatic buyback, is **zero**: no protocol or foundation routes revenue into buying ZEC. Buy #2, protocol fee burn, is **zero**: Zcash transaction fees, about **226 ZEC** across the window, are paid to the miner rather than destroyed, and the supply total rising by exactly the block rewards confirms that nothing was burned. Zcash has no burn address convention to read on the other surface, so both views agree. Buy #3, foundation buying, is **zero**; the Zcash Foundation's latest report shows it converting part of its ZEC into dollars, not accumulating.

Buy #4, new long-term locks, is also **zero**, and this is where the ZEC ledger changed this rebuild. The 12% lockbox share grew by **19,348 ZEC** over the window, from **46,111** to **65,459 ZEC**, with no outflow. A lock only removes supply if the coins leave the counted float, and these never do: the published circulating figure sits just **125 ZEC** below the total, far less than the lockbox holds, so lockbox ZEC is already counted as circulating. The previous build treated the lockbox as a lock and read **+0.84%**; the corrected reading is **+0.95%**, and it now sits beside the supply monitor instead of below it. Shielded ZEC is not a lock either: coins in the private pools stay spendable, and the large Orchard-to-Ironwood migration after NU6.3 moved value between pools without creating or removing any.

## Foundation and overhang

Four Zcash balances are tracked on every refresh. The protocol lockbox holds **65,459 ZEC**, grows by 0.1875 ZEC a block, and can only be opened by a future network upgrade; it has not released a coin since its one-time **78,750 ZEC** disbursement in **Nov 2025**, and it is re-read from chain state each time. That disbursement sits in a coinholder-directed grants multisig that now holds **78,183 ZEC** and has not moved since **Apr 14 2026**, also read on-chain. The Zcash Foundation reported **78,986 ZEC** at **Jun 30 2026**, checked against each quarterly report. The Zcash Community Grants address is a pass-through that holds about **143 ZEC** at any moment. Because every one of these balances is already inside the circulating count, spending from them moves ZEC within the market rather than adding to it; if any of them ever sat outside that count and fell between refreshes, the outflow would enter Sell #3 at the next refresh. Mining pools, exchange wallets, the new exchange-traded funds and the listed-company treasury are excluded by rule, because those coins belong to their buyers.

## How ZEC compares to other capped proof-of-work chains

ZEC belongs with Bitcoin-style chains: a hard cap of **21M**, a block subsidy that halves roughly every four years, and no fee burn. Zcash sits at the same point in that curve as Bitcoin in one sense, having halved in **Nov 2024**, but its issuance rate is higher, because Zcash has mined about **80.7%** of its cap against Bitcoin's far higher share, so each block still adds a larger slice of the existing float. Against Monero, the other large privacy coin, the difference is the end state: Monero pays a permanent tail emission that never stops, while ZEC issuance keeps halving toward zero. Against proof-of-stake chains, Zcash has no staking lock and no burn to offset the mint, so its gross issuance is also its net.

What makes Zcash unusual inside the capped proof-of-work class is where the block reward goes. A fifth of every ZEC block reward funds development — the grants fund and the protocol lockbox — rather than miners, which is closer to a built-in treasury than to Bitcoin's pure miner subsidy. That does not change the supply arithmetic, because treasury ZEC counts as circulating, but it does mean a meaningful share of new ZEC sits with community-controlled funds rather than with miners who sell to cover costs. And because Zcash fees go to miners rather than being destroyed, the ZEC fee market offsets none of that issuance, whatever the traffic.

## What to watch in the next 90 days

First, NU7: Zcash developers target mainnet activation on **Nov 5 2026**, with the activation height to be fixed on **Oct 20 2026**. NU7 cuts block spacing from 75 to 25 seconds and divides the reward per block to match, so ZEC issuance per day should not change; the framework will re-measure the real block pace after it lands. Second, NU7's sustainability mechanism sets aside at least 60% of fees for later reissue — small at today's fee levels, but the first Zcash buy-side mechanism if it ships. Third, NU7 disables the old transaction format, which leaves about **22,430 ZEC** in the legacy Sprout pool unspendable; those coins stay in the circulating count, so the framework will watch whether that count is revised. Fourth, any network upgrade that opens the **65,459 ZEC** lockbox would change the Foundation and overhang section, though its coins already count as circulating.

## Summary

The MrNasdog Pressure Framework reads ZEC at **+0.95% net** over the trailing 90 days and **+0.95%** over the next 90, with **161,234 ZEC** of block rewards and nothing on the buy side. The structural mechanism is a capped proof-of-work Zcash chain paying **1.5625 ZEC** a block, a fifth of it to development funds that already count as circulating, with no burn, no buyback and no staking lock. The key risk is simply that issuance runs unopposed: until the next halving, ZEC supply grows at close to **1%** every 90 days. The ceiling is the **21M ZEC** cap, with the next halving to **0.78125 ZEC** per block expected around **Nov 2028**.

*MrNasdog Pressure Framework analysis of ZEC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 25 2026.*

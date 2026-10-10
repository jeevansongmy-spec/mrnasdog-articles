---
title:         "FET Inflation Analysis · October 2026 · Supply growing · projected to keep growing"
description:   "FET supply is growing fast: a native-chain bridge minted 292M FET and 346M reached the market in 90 days, plus 10.5M staking pay. +15.44% net, no burn."
canonical_url: "https://mrnasdog.com/research/fet/inflation"
tags:                    ["crypto", "fet", "fetchai", "ai"]
published:     true
---
Originally published at [FET Inflation Analysis · October 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/fet/inflation).

# FET Inflation Analysis · October 2026 · Supply growing · projected to keep growing

<!-- main-page -->
➜ Start with the ASI Alliance coin page for the short answer (should you buy FET?) and its price drivers: [mrnasdog.com/research/fet](https://mrnasdog.com/research/fet)

FET, the token of the Artificial Superintelligence Alliance, is **strongly inflationary**: over the last 90 days **356.84M FET** of new supply reached the market against **0** bought back or burned, a net **+15.44%** of the **2.31B** FET counted as circulating, and about **+15.48%** is expected in the next 90 days. Almost all of it comes from the bridge on Fetch.ai's own chain, which created **292M** new native FET in five batches with no Ethereum FET locked or burned to match; the monitor reads only **+2.89%** because it counts FET on Ethereum alone.

## The verdict, in one paragraph

The MrNasdog Pressure Framework reads FET at **+15.44%** net supply growth over the last 90 days and **+15.48%** for the next 90 days. The inflation monitor reads **+2.89%**, a gap of **12.55 percentage points**, far above the 0.5-point line, so the coin page carries a ⚠ monitor gap chip. We walked the gap through five kinds of source. The monitor follows the Ethereum token only: its move is FET leaving the Ethereum bridge, and it has not yet caught the **30.0M** FET that left on Oct 1–2 2026. It cannot see Fetch.ai's own chain, where the new coins are created. In one line: FET is **inflationary by bridge minting on its native chain**, with a staking stream on top and nothing on the buy side.

## Sell pressure: where new FET comes from

FET lives on two ledgers. The Ethereum token has a total supply of **2,714,384,547 FET** that did not move in the window, and the circulating count of **2,311,508,384 FET** is taken from that token alone. The second ledger is Fetch.ai's own chain, where native FET is staked and traded. Its supply rose from **1,463.41M** to **1,765.95M** FET between Jul 10 and Oct 7 2026 — **+302.54M** in about 90 days.

Protocol inflation is the staking stream: the native chain pays stakers **3%** a year of its supply, set per block. Blocks arrive about every 5.7 seconds instead of the planned 5, so the real rate is nearer 2.6% a year. After taking out the bridge batches, the native supply shows **10.54M FET** of staking pay in the window, and the same rate on today's larger supply gives about **11.47M FET** next.

The big row is the bridge. The native-chain bridge contract minted **292M FET** in five batches — 60M on Jul 25, 62M on Aug 5, 70M on Aug 14, 40M on Aug 28 and 60M on Sep 18 2026 — each marked as an Ethereum-to-native swap. The Ethereum token's supply stayed flat and no matching Ethereum FET was locked or burned, so these are new coins. The bridge admin then handed **346.7M FET** to exchange deposit wallets in eight lots, the latest on Oct 5 2026. The exchange swapped **110M** of it back to Ethereum, which drained the Ethereum bridge from **278.42M** to **4.36M** FET. Counting what left the team's wallets on both chains, **346.3M FET** reached the market. The handouts have come every 4 to 22 days since June 2026, so the framework carries the same amount into the next 90 days.

Vesting unlocks are **0**: the original FET team and sale schedules ended years ago. Unlock trackers still show monthly lines for the old AGIX swap, but those FET already sit in swap contracts counted as circulating, and swaps have been paused since the Sep 19 2026 hack. Foundation and unscheduled unlocks book **0** on their own row because every team wallet that paid out is counted in the bridge row. Long-term locked or bankruptcy is **0**: no estate or trustee holds FET.

## Buy pressure: where new FET goes

Nothing takes FET off the market. There is **no programmatic buyback**: no contract, fund or treasury buys FET back. The protocol fee burn is **0** — fees on the native chain go to validators, the Ethereum token's supply read the same at both ends of the window, and the dead address did not move. The last burns were **5M FET** on Jan 10 2025 and **109,350 FET** on Nov 5 2025, and a governance vote to burn 110M FET was rejected in October 2025. Foundation buying is **0**. New long-term locks are also **0**: about **614M FET** is staked on the native chain, but native coins sit outside the circulating count, so more staking removes nothing from it.

## Foundation and overhang

Four Ethereum wallets make up the whole gap between total and circulating supply, and they reconcile to the FET at the start of the window: the Fetch.ai admin multisig with **261.21M FET** (it took 200M out of the Ethereum bridge on Sep 23 2026 and sent 20M back on Oct 2), the Ethereum bridge with **4.36M**, the old staking contract with **80.62M**, and the Fetch.ai foundation safe with **26.69M**, which did not move. On the native chain, the bridge admin holds **50.78M FET** withdrawn but not yet handed out, plus **57.49M** staked, and the bridge contract holds **4.17M**. The admin can also mint more through the bridge. A large safe of **277.55M FET** sits inside the circulating count and did not move. We read all of these on-chain at every rebuild; if any balance falls between rebuilds, the outflow is booked as new sell pressure at the next one.

## How FET compares to other AI tokens and multi-chain coins

Most AI tokens of FET's size live on one chain with a fixed supply and a vesting calendar, so their supply story is a list of unlock dates. FET is different in kind: it is both an Ethereum token with a fixed total and a native coin on its own proof-of-stake chain, and the two are joined by a bridge whose admin can mint native coins. That makes FET's supply depend on bridge operations rather than on a published schedule — closer to a wrapped asset whose mint key sits with a team than to a capped token.

Against proof-of-stake chains such as Cosmos-style networks, FET's staking stream is modest: **3%** a year nominal, about 2.6% in practice, with no fee burn to offset it. Against tokens with a buyback or burn engine, FET has no buy side at all. The bridge row is what sets it apart: **346.3M FET** in 90 days is about fifteen times the staking stream, and it arrived with no announcement.

## What to watch in the next 90 days

First, the next bridge batch: any new mint by the native bridge contract, or another handout from the admin's **50.78M FET** to an exchange, keeps the bridge row at its current pace; a 90-day stop would cut the projection to the staking stream alone, about **+0.50%**.

Second, the Ethereum admin multisig's **261.21M FET**: it refilled the Ethereum bridge with 20M on Oct 2 2026, and every further refill lets more Ethereum FET reach the market.

Third, the AGIX-to-FET swap restart after the Sep 19 2026 hack, and the AGIX swap line unlock trackers show for Oct 28 2026 — both move coins already counted as circulating, so they book 0 unless the swap contracts change.

Fourth, the circulating count itself: it has not yet absorbed the 30.0M FET released on Oct 1–2 2026, so it should rise to about 2.34B when it catches up.

## Summary

FET is strongly inflationary at **+15.44%** over the last 90 days and a projected **+15.48%** over the next 90 days, with nothing bought back or burned. The driver is the bridge on Fetch.ai's own chain, which minted **292M** new FET in five batches and handed **346.7M** FET to exchange wallets, on top of a staking stream of about **10.54M** FET. The key risk is that this supply arrives without a schedule or an announcement, and the usual monitor, which counts FET on Ethereum only, shows **+2.89%**. The Ethereum token's total of 2,714,384,547 FET is not a ceiling on the native chain, which has no cap.

*MrNasdog Pressure Framework analysis of FET, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 8 2026.*

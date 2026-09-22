---
title:         "FET Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "FET supply grows 14.14% over 90 days: the native chain's bridge created 352M FET in conversion batches while the Ethereum count stayed flat. Full analysis."
canonical_url: "https://mrnasdog.com/research/fet/inflation"
tags:                    ["crypto", "fet", "fetchai", "ai"]
published:     true
---

Originally published at [FET Inflation Analysis · September 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/fet/inflation).

# FET Inflation Analysis · September 2026 · Supply growing · projected to keep growing

FET supply is growing fast, and the source is not the Ethereum token everyone quotes. The MrNasdog Pressure Framework reads the Artificial Superintelligence Alliance token at **+14.14%** over the last 90 days and **+14.20%** projected for the next 90, from **326.96M FET** of sell pressure and **0** buy pressure. Almost all of it is FET created by the bridge contract on the Fetch.ai native chain in batches labelled as conversions from Ethereum FET, **317.0M FET** of which moved on to the market, while the Ethereum FET count stayed flat at **2,714.4M FET** and the inflation monitor, which watches Ethereum only, reads **+2.33%**.

## The verdict, in one paragraph

Against a circulating base of **2,311.5M FET**, the Pressure Framework books **326.96M FET** of sell pressure and **0** of buy pressure between Jun 24 2026 and Sep 22 2026, a net of **+14.14%**, and projects **+14.20%** for the next 90 days if the batches resume at the same pace. The inflation monitor reads **+2.33%** for the same window, a gap of **11.81 percentage points**, far over the 0.5-point tolerance, so the overview carries a monitor-gap warning. The gap has one clear cause: the monitor counts FET on Ethereum only, and its entire move is **52.6M FET** leaving the Ethereum bridge, coins that were already on the market on the native chain. It cannot see the native chain, where the new coins are made. The label for FET is **a two-chain token whose native side is growing**.

## Sell pressure: where new FET comes from

FET lives on two chains. The Ethereum ERC-20 token read **2,714,384,546.672 FET** at both ends of the window and created nothing, although its mint function is still live and held by a Fetch.ai Foundation wallet. The Fetch.ai native chain is different. Its mint module pays stakers with new FET at a set 3% a year of native supply. Because native blocks run at about 5.7 seconds instead of the planned 5, real issuance is lower than the headline rate: about **10.2M FET** over the window, of which 98% went to stakers. Sell #1, protocol inflation, is **9.96M FET**, and **11.16M FET** next on today's larger native supply.

The main story is a row of its own, Sell #5, native bridge conversions, at **317.0M FET**. A chain upgrade that went live on Jun 2 2026 added a token factory module, and the native side of the Ethereum bridge was changed to use it. Since then the bridge operator has been able to create native FET. Inside this window it created **352M FET** in six batches, on Jul 3, Jul 25, Aug 5, Aug 14, Aug 28 and Sep 18 2026, between 40M and 70M each time, and every batch is labelled on-chain as a conversion from Ethereum FET to native FET. The operator then moved the coins out, sent a small test amount first, and sent **317.0M FET** through two wallets to one high-volume wallet. These are not AGIX or OCEAN merger conversions: Ethereum AGIX supply fell only about **5.8M** before Sep 19 2026 and OCEAN supply did not move. We read every Ethereum FET transfer in the window and found no Ethereum FET locked in the bridge, taken out of use, or gathered in any one wallet to match. So on the chains we can read, these are new FET, and the Pressure Framework counts them when they reach that wallet, not at creation, because coins still in the bridge or with its operator are not yet on the market.

Sell #2, vesting unlocks, is **0**. The old investor, team and sale schedules are finished, and FET held back for AGIX and OCEAN holders who have not converted yet sits in wallets that are already counted as circulating. That includes the converter wallet an attacker emptied on Sep 19 2026, taking **8.7M FET**; those coins were already counted, so the theft moved coins inside the market without adding to it. Sell #3, Foundation and unscheduled unlocks, is **0**, and Sell #4, long-term locked or bankruptcy, is **0**: FET has no bankruptcy estate or court-ordered distribution.

## Buy pressure: where new FET goes

Nowhere, this window. Buy #1, programmatic buyback, is **0**: the last announced FET repurchase belongs to 2025, and nothing ran between Jun 24 and Sep 22 2026. Buy #2, protocol fee burn, is **0**, and it was checked from both sides on both chains. On Ethereum the token count stayed flat and the dead address held **0.47 FET** on both dates. On the native chain, supply only rose, and it rose by exactly the six batches plus staking pay, so nothing was destroyed there either. A 2025 governance vote to burn a leftover 110M FET was rejected.

Buy #3, Foundation buy, is **0**; the Foundation's Ethereum safe held the same **26.7M FET** at both ends. Buy #4, new long-term lock, is **0**. About **28.7M FET** moved into the Ethereum bridge, but that only turns Ethereum FET into native FET for the same owners. In the other direction, **81.3M FET** left the bridge for Ethereum, most of it in 10M batches from one native wallet on Aug 19, Aug 20, Sep 2 and Sep 3 2026. Both directions are owners changing chains, so neither is counted.

## Foundation and overhang

The largest pool to watch is the power to mint itself. The native bridge contract held **101.8M FET**, built mostly from newly minted coins, at the end of the window, and its operator can create more. On Ethereum, the Foundation safe holds **26.7M FET** and the right to mint new ERC-20 FET. The bridge cold wallet holds **81.2M FET** and an old staking contract holds **80.6M FET**; neither moved. On the native chain, one large unlabelled account holds **625.8M FET**. The merger safe holds **277.5M FET**, but it is already counted as circulating, so its payouts add nothing new. All of these are read from the chain at every rebuild. If any of them falls between refreshes by more than known bridge traffic explains, that outflow enters Sell #3 at the next refresh.

## How FET compares to other staking and bridged tokens

Most proof-of-stake chains pay stakers with new coins, and 3% a year is at the low end of that group. On staking alone, FET would read under 0.5% a quarter, a mild number next to chains that emit 7% to 15% a year. What sets FET apart is not its staking design but its two-chain setup. A normal lock-and-release bridge cannot add coins: every coin that appears on one side is locked on the other. FET's native bridge can now create coins directly, and in this window we found nothing locked on Ethereum in return, so its native supply behaves more like an uncapped ledger than a mirror of a capped token.

That also explains why the numbers people quote look calm. Market data for FET, including the published maximum of 2,714.4M FET, comes from the Ethereum token, whose count has not changed since 2024. A hard cap on one chain does not cap a token that lives on two. Tokens with a single supply ledger, such as a halving-model chain like Bitcoin or an exchange token with a quarterly burn, do not have this blind spot, because the number everyone reads is the number that moves.

## What to watch in the next 90 days

First, the bridge pause: the native bridge has been paused since Sep 20 2026, right after the Sep 19 2026 attack on a SingularityNET converter. If the batches stay off through Dec 21 2026, next-90-day inflation falls to about **+0.48%**; if the two-week pace returns, it stays near **+14.20%**. Second, any Fetch.ai statement, or any locked or retired FET on another chain, that shows what stands behind these conversions; that would change how this row is counted. Third, the **101.8M FET** still in the native bridge and the **625.8M FET** native account. Fourth, the Foundation safe's Ethereum mint right, unused since 2024. Fifth, AGIX to FET conversions, which were paused after the attack and pay out from wallets already counted as circulating.

## Summary

The MrNasdog Pressure Framework reads FET at **+14.14%** over the trailing 90 days and **+14.20%** projected forward: supply growing, projected to keep growing. The mechanism is new native-chain FET, **352M** created by the bridge contract in conversion batches and **317.0M** moved on to the market, plus **9.96M** of staking pay, with nothing burned and nothing bought back. The key risk is that these batches are run by one operator account, and we found no public note that explains them or shows what backs them. The Ethereum count of **2,714.4M FET** looks like a cap, but it does not bind the native chain.

MrNasdog Pressure Framework analysis of FET, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 22 2026.

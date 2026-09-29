---
title:         "NIGHT Inflation Analysis · September 2026 · Supply was growing · trend cooling"
description:   "Supply was growing, trend cooling: NIGHT reads +3.10% over 90 days after a Jul 20 2026 bridge hack left 514.6M copies unbacked; 0.00% next. No mint, no burn."
canonical_url: "https://mrnasdog.com/research/night/inflation"
tags:          ["crypto", "night", "midnight", "cardano"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/night/inflation](https://mrnasdog.com/research/night/inflation)*

# NIGHT Inflation Analysis · September 2026 · Supply was growing · trend cooling

The MrNasdog Pressure Framework reads Midnight's NIGHT token at **+3.10% net** over the trailing 90 days and **0.00%** over the next 90. Not one NIGHT was created or burned in the window: the whole rise comes from a bridge exploit on **Jul 20 2026** that left **514.6M** NIGHT copies on BNB Chain trading without backing. The monitor reads **+0.01%**, a gap of **3.09 percentage points**, because its circulating count is a fixed sum of NIGHT's allocation groups that cannot see copies on other chains.

## The verdict, in one paragraph

NIGHT's supply grew **+3.10%** over the last 90 days against a circulating count of **16,607.4M NIGHT**, and the framework projects **0.00%** for the next 90 days, because the one flow behind the rise was a single event and nothing new is scheduled. The inflation monitor reads **+0.01%** for the same 90 days, so the gap is **3.09 percentage points** — well past the 0.5-point line, which means a ⚠ monitor-gap chip ships on the Midnight coin page. A walk through the chain, the unlock trackers, the project's own pages and the governance setup explains the gap but cannot close it: the monitor's count stayed near 16,607.4M every day of the window, while on-chain the bridge's backing fell from **527.0M** to **11.8M NIGHT**. The label that fits: a fixed-supply token whose float grew through a bridge hack, not through minting.

## Sell pressure: where new NIGHT comes from

Protocol inflation added **0 NIGHT**. All **24,000M NIGHT** were created in a single mint on Cardano in November 2025, and the token has had no second mint since. Midnight has no issuance of its own: new NIGHT can reach the market only as block rewards paid out of the **6,000M** Reserve, and those rewards have not started. The Midnight mainnet, live since Mar 30 2026, is still produced by 13 appointed nodes, and the next phase — when Cardano stake pool operators start producing Midnight blocks and rewards begin — has no published date or rate.

Vesting unlocks added **0 NIGHT** to the count, even though coins are unlocking right now. The **4,547.4M NIGHT** claimed in the Glacier Drop and Scavenger Mine airdrop thaw in four quarters over a year; the last quarter has been unlocking since early September, and the thaw ends on **Dec 4 2026**. Every one of those coins is already inside the circulating count, so the thaw moves coins the count already includes.

Foundation and unscheduled unlocks added **0 NIGHT**. The Midnight Foundation's 8,400M NIGHT and its launch company's 3,660M are fully unlocked and already counted, so a sale by either one moves nothing into the count. The three groups outside the count — the Reserve, the 1,200M Treasury and the 192.6M Lost-and-Found pool — released nothing this window. Long-term locks and bankruptcy added **0 NIGHT**: there is no estate and no court schedule behind NIGHT.

The one non-zero row is the bridge exploit, at **514.6M NIGHT**. A third-party bridge between Cardano and BNB Chain held **527.0M NIGHT** on Cardano to back about **526.4M** NIGHT copies it had issued on BNB Chain. On Jul 20 2026, between 14:46 and 14:55 UTC, an attacker reused a valid signature to drain **515.2M NIGHT** from the bridge in four transfers and sold them on the market. The copies on BNB Chain were never cancelled: **526.5M** of them still trade at the NIGHT price, now backed by just **11.8M NIGHT**. The drained Cardano coins were already counted, so the framework books the event once, as the **514.6M** copies that no longer have anything behind them.

## Buy pressure: where new NIGHT goes

The buy side is empty. The programmatic buyback is **0 NIGHT**: fees on Midnight are paid in DUST, a resource that holding NIGHT generates, so the network collects no NIGHT to buy with, and no contract or treasury buys NIGHT back. The protocol fee burn is **0 NIGHT**: DUST decays and cannot be sold, and not one NIGHT has been destroyed since the token was created.

The Foundation buy is **0 NIGHT**: neither the Foundation, the launch company nor the bridge operator bought NIGHT this window, and no plan to restore the bridge's missing backing had been carried out by Sep 29 2026. The new long-term lock is **0 NIGHT**: generating DUST does not lock NIGHT, the coins stay spendable in the owner's wallet, and there is no staking lock yet.

## Foundation and overhang

The largest overhang inside the float is the Midnight Foundation's **8,400M NIGHT** plus the **3,660M NIGHT** held by Midnight TGE, the Foundation's launch company — together **50.25%** of all NIGHT, unlocked since Dec 10 2025. The launch company's share is meant for exchange liquidity, and whatever it does not use is to go back to the Reserve one day, which would take coins out of the float. These wallets are re-read from the chain at every check.

Outside the float sit three pools. The **6,000M NIGHT** Reserve pays block rewards and nothing else; the protocol pays out a fixed share of what remains with each block, so rewards start highest and shrink over time. The **1,200M NIGHT** Treasury stays locked until on-chain voting is live. The **192.6M NIGHT** Lost-and-Found pool is for airdrop-eligible holders who missed their claim, with four years to claim once the phase is open. Finally, **514.6M** unbacked bridged copies remain in the market, and **11.8M NIGHT** still sits in the suspended bridge. If any of these balances falls between our checks, the outflow enters the sell side of the ledger at the next check.

## How NIGHT compares to other privacy chains

Zcash and Monero, the two older privacy coins, pay miners in new coins every block: Zcash on a halving schedule toward a 21M cap, Monero with a small permanent tail emission. Midnight works the other way round. All 24,000M NIGHT already exist, and the only road for new coins into the market is a finite Reserve that pays a shrinking share per block. There is no fee burn on any of the three, but Midnight's fees are paid in DUST rather than the coin itself, so NIGHT is not even spent by using the network.

The comparison that matters more for NIGHT is custody. Half of all NIGHT sits with the Foundation and its launch company, fully unlocked, while a mined coin like Zcash spreads new supply across many miners. And NIGHT's 3.10% rise shows a risk that pure mining coins do not face in the same way: a token copied onto other chains through third-party bridges can grow its tradable supply without a single mint, and a count built from allocation groups will not see it.

Among Cardano-linked assets, NIGHT is closer to a partner-chain governance token than to ADA itself: ADA pays staking rewards from its own reserve, while NIGHT's reserve has not yet started paying anyone.

## What to watch in the next 90 days

First, the start of block rewards: when Cardano stake pool operators begin producing Midnight blocks, NIGHT starts moving out of the 6,000M Reserve, and the framework will book it as protocol inflation; no date has been set. Second, the end of the airdrop thaw on **Dec 4 2026**, followed by a 90-day grace period; it adds nothing to the count, but it is the last scheduled unlock. Third, any restoration of the bridge: if the operator buys or recovers NIGHT to back the 514.6M orphaned copies, or cancels copies, that would book on the buy side. Fourth, the opening of the Lost-and-Found claims, which would release up to 192.6M NIGHT over four years. Fifth, the first moves by the launch company to send unused NIGHT back to the Reserve.

## Summary

Midnight's NIGHT grew **+3.10%** in tradable supply over the 90 days to Sep 29 2026 without creating a single coin: a Jul 20 2026 bridge exploit drained 515.2M NIGHT of backing and left **514.6M** copies on BNB Chain trading without it. The framework projects **0.00%** for the next 90 days, because block rewards from the 6,000M Reserve have not started and every scheduled airdrop unlock is already counted. The key risk sits in custody and in the Reserve: the Foundation and its launch company hold 50.25% of all NIGHT, and the reward stream will begin once outside operators join. The ceiling is 24,000M NIGHT on Cardano, with 7,392.6M of it still outside the circulating count.

*MrNasdog Pressure Framework analysis of NIGHT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

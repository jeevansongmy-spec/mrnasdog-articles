---
title:         "NIGHT Inflation Analysis · September 2026 · Supply was growing · trend cooling"
description:   "Supply was growing, trend cooling: NIGHT reads +3.10% over 90 days after a bridge hack freed 514.6M locked tokens, and 0.00% next. No mint and no burn."
canonical_url: "https://mrnasdog.com/research/night/inflation"
tags:                    ["crypto", "night", "midnight", "cardano"]
published:     true
---

Originally published at [NIGHT Inflation Analysis · September 2026 · Supply was growing · trend cooling](https://mrnasdog.com/research/night/inflation).

# NIGHT Inflation Analysis · September 2026 · Supply was growing · trend cooling

Supply was growing and the trend is cooling. Midnight mints no new NIGHT and burns none, yet the Pressure Framework reads NIGHT at **+3.10%** over the last 90 days and **0.00%** for the next 90, against a monitor reading of **−0.06%**. The whole number is one event: on **Jul 20 2026** an attacker drained the locked backing of the Cardano to BNB Chain bridge, so **514.6M NIGHT** of new tradable claims appeared while the fixed **24,000M NIGHT** total never moved.

## The verdict, in one paragraph

On a counted float of **16,607.4M NIGHT**, the framework books **514.6M NIGHT** of sell pressure and **0** of buy pressure for the trailing 90 days, a net of **+3.10%**, and **0.00%** for the next 90 days because nothing is scheduled to cross into the float. The inflation monitor reads **−0.06%**, a gap of **3.16 percentage points**, well over the 0.5-point tolerance, so the overview carries a monitor-gap warning. The gap is explained, not closed: the monitor's counted float is a fixed sum of Midnight's launch allocations and cannot move, so it cannot see wrapped NIGHT losing its backing. The label for NIGHT is **a non-minting token hit by a one-time float shock**.

## Sell pressure: where new NIGHT comes from

It does not come from minting. All **24,000M NIGHT** were created once, as a Cardano native asset, and the Cardano ledger still records a single mint and no burn. Midnight block rewards are paid only out of a pre-funded Reserve, and that Reserve held **6,000M NIGHT** on **Sep 22 2026**, exactly its starting balance, with no transactions in the window. The network is still run by a small set of trusted block producers who are not paid rewards. Sell #1, protocol inflation, is **0**, watched because a future upgrade will switch Reserve rewards on.

Sell #2, vesting unlocks, is also **0**, and this is the row most readers expect to be large. The Glacier Drop and Scavenger Mine airdrop gave the community **4,547.4M NIGHT** that thaws in four 25% steps, with each claim's first step placed at random in the first 90 days from **Dec 10 2025**. One full step fell inside this window. But the counted float already includes the whole claimed pool: **8,400M** for the Midnight Foundation, plus **3,660M** for Midnight TGE, plus **4,547.4M** claimed equals **16,607.4M NIGHT** exactly. A coin counts once, when it enters the float. A thawed airdrop coin leaving the redemption contract, which still held **1,263.3M NIGHT** on Sep 22 2026, was already counted, so it adds nothing.

Sell #3, Foundation and unscheduled unlocks, is **0**: the only pots outside the float, the Treasury and the Lost-and-Found pool, did not move once. Sell #4, long-term locked or bankruptcy, is **0**; there is no estate or trustee. The number comes from Sell #5, the bridge exploit, at **514.6M NIGHT**. The Wanchain bridge held Cardano NIGHT locked as backing for wrapped NIGHT on BNB Chain. On Jul 20 2026 an attacker replayed a signature and withdrew **515.2M NIGHT** in four transactions, taking the backing from **527.0M** to **11.8M NIGHT**. The **526.5M** wrapped NIGHT were never retired and still move between large exchange wallets. So the attacker's coins and the wrapped copies now both trade, and about 300M NIGHT was sold within hours.

## Buy pressure: where new NIGHT goes

Nowhere. Buy #1, programmatic buyback, is **0**: no programme to buy NIGHT on the market exists or was announced. Buy #2, protocol fee burn, is **0** by design. Midnight transactions are paid in DUST, a shielded resource that holding NIGHT generates over time, so NIGHT itself is never spent on fees or destroyed. Both burn surfaces were read: the Cardano ledger still counts 24,000M NIGHT with no burn ever recorded, and the wrapped supply on BNB Chain has not changed since **Jul 21 2026**.

Buy #3, Foundation buy, is **0**. Midnight TGE's unused tokens are meant to go back to the Reserve one day, which would take them out of the float, but the Reserve did not change. Buy #4, new long-term lock, is **0**. Moving NIGHT onto the Midnight network locks it on Cardano and unlocks it there, so it remains one coin with one count and removes nothing.

## Foundation and overhang

The overhang on NIGHT is large and mostly already counted. The Midnight Foundation was allocated **8,400M NIGHT** and Midnight TGE **3,660M NIGHT**, both unlocked from launch and together half of all supply; how much each still holds is not published by wallet. Both sit inside the counted float, so a sale by either would move coins inside the float rather than add to it, but it would still be selling into the market, and the Foundation has no fixed release calendar. The pots outside the float are smaller and locked: the on-chain Treasury at **1,200M NIGHT**, locked until on-chain governance exists, and the Lost-and-Found pool at **192.6M NIGHT**, waiting for a claim phase with no date. The Reserve's **6,000M NIGHT** opens only as block rewards.

The Reserve, Treasury and Lost-and-Found balances are read from the chain at every rebuild; the Foundation and Midnight TGE balances are checked by hand. If any of these balances falls between refreshes by more than a known schedule explains, that outflow enters Sell #3 at the next refresh. The bridge's remaining backing of **11.8M NIGHT** and the **526.5M** wrapped supply are read at the same rebuilds.

## How NIGHT compares to other capped, non-minting tokens

NIGHT sits in a small class of tokens whose whole supply exists from day one. Unlike a halving chain such as Bitcoin, which still mints on every block, or an uncapped staking chain paying rewards from new coins, Midnight has no mint at all. Its future issuance is a draw-down of the **6,000M NIGHT** Reserve on a slowing curve, which has not started. On the pure issuance axis NIGHT is as tight as any token in the catalogue.

What sets NIGHT apart this quarter is custody risk. Most capped tokens that read positive do so because of a vesting unlock, a dated and predictable release. NIGHT read positive because a bridge failed. A wrapped token is a promise that the original sits locked somewhere, and when that lock is emptied the promise keeps trading while the original trades too. Any token bridged to other chains carries this exposure; the size of the risk is the size of the locked backing, not the size of the cap.

Against exchange tokens that run a buyback or a burn, NIGHT has nothing on the buy side. Fees go to DUST, which decays and cannot be sold, so network use never removes NIGHT from supply. Holding NIGHT pays for usage; it does not shrink the float.

## What to watch in the next 90 days

First, the bridge: Wanchain has shut it and offered the attacker a bounty, and any return of funds that re-locks backing would reverse part of the **514.6M NIGHT** reading. Second, the last airdrop thaw step ends on **Dec 4 2026**; it adds nothing to the float, but it frees the last frozen airdrop coins for sale. Third, the start of Reserve block rewards, planned for the Mōhalu phase when Cardano stake pool operators join; no date is set, and the first reward would open the Reserve for the first time. Fourth, the Lost-and-Found claim phase, which would release up to **192.6M NIGHT** with no thaw. Fifth, any on-chain governance launch, which is the only key to the **1,200M NIGHT** Treasury.

## Summary

The MrNasdog Pressure Framework reads Midnight's NIGHT at **+3.10%** over the trailing 90 days and **0.00%** for the next 90: supply was growing, trend cooling. NIGHT mints nothing and burns nothing, and its airdrop thaw was already inside the float; the whole reading is the **Jul 20 2026** bridge drain that left **514.6M** wrapped NIGHT without backing. The key risks are custody failures like that one and the **12,060M NIGHT** allocated, unlocked, to the Foundation and Midnight TGE. The ceiling holds firm at **24,000M NIGHT**, with the **6,000M** Reserve still untouched.

MrNasdog Pressure Framework analysis of NIGHT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 23 2026.

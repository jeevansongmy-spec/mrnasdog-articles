---
title:         "LDO Inflation Analysis · September 2026 · Supply shrinking · projected to keep shrinking"
description:   "LDO supply is shrinking: no new LDO is minted and the Lido DAO treasury bought back 13.2M LDO, −1.60% net in 90 days and −0.73% next. A 48.93M cliff opens Jan 1 2027."
canonical_url: "https://mrnasdog.com/research/ldo/inflation"
tags:          ["crypto", "ldo", "lido", "defi"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/ldo/inflation](https://mrnasdog.com/research/ldo/inflation)*

# LDO Inflation Analysis · September 2026 · Supply shrinking · projected to keep shrinking

LDO, the governance token of Lido DAO, is shrinking in the market: no new LDO was created over the last 90 days, while the Lido DAO treasury took **13,266,879 LDO** off the market, almost all of it through an LDO buyback paid for with staked ETH. The MrNasdog Pressure Framework reads LDO at **−1.60% net** over 90 days and **−0.73%** for the next 90, against a supply-monitor reading of **−1.53%**. LDO has a fixed supply of 1 billion; the main risk to this reading is a **48.93M LDO** vesting cliff that opens on **Jan 1 2027**, four days after the forward window closes.

## The verdict, in one paragraph

Over the 90 days to Sep 29 2026, LDO's circulating supply fell by **1.60%**. Nothing was added: the LDO token has no emission, no vesting tranche opened, and the Lido DAO treasury paid out no LDO. On the other side, the treasury pulled **13.27M LDO** out of the market and holds it. For the next 90 days the framework projects **−0.73%**, driven by one more buyback batch of about **6.09M LDO**. The supply monitor reads **−1.53%** for its own 90-day window, a gap of **0.07 percentage points** — well inside the 0.5-point tolerance, so no warning chip is shown. The label that fits: LDO is a fixed-supply governance token being slowly bought back by its own DAO treasury.

## Sell pressure: where new LDO comes from

Protocol inflation added **0 LDO**. LDO has no block reward and no staking emission; the token's total supply read exactly **1,000,000,000 LDO** at both ends of the window, and that number is kept in the token's on-chain storage, so any mint would have shown up. The Lido DAO can still mint LDO through its token manager, but only by a governance vote, and no such vote exists.

Vesting unlocks added **0 LDO** in the window and add **0** in the next 90 days. The original team and investor vesting of LDO finished years ago. The one live lock is a re-vesting of contributor LDO: on Jan 1 2026 the token manager placed **48,934,690 LDO** held by ten contributor wallets under a one-year lock, and all of it becomes transferable on **Jan 1 2027**. That cliff sits four days past the forward window, so it is not in the 90-day count, but it is the largest scheduled LDO release of the coming year — about **5.9%** of today's circulating supply.

Foundation and unscheduled unlocks added **0 LDO**. A full sweep of the treasury's LDO transfers found five inflows and no outflows in the window, and the sweep matched the treasury's balance change to the last decimal. The treasury did pay out **7.69M LDO** for contributor and delegate rewards between Nov 10 2025 and Mar 2 2026, but nothing since, and that reward plan's allocation ends on Oct 31 2026 with no new request on the table. The fourth sell row, long-term locked or bankruptcy supply, is **0**: no estate or court schedule holds LDO.

## Buy pressure: where new LDO goes

The largest buy row is the treasury's LDO accumulation program. In April 2026 LDO holders voted **64.5M to 5.5M** to let the Lido DAO spend up to **10,000 stETH** buying LDO in batches of 1,000 stETH, each batch with a price cap in LDO/ETH and a public report. In this window the program returned **13,204,012 LDO** to the treasury on Jul 8, Aug 25 and Sep 25 2026. Because the treasury sits outside the circulating count, every coin it buys leaves the market. Batch 4 — **1,000 stETH**, about **6.09M LDO** at today's prices — runs until Nov 24 2026 with a cap of 0.000165 ETH per LDO, just above today's ratio; it only buys while LDO stays under that cap.

The programmatic buyback added **6,354 LDO**. Lido's automatic buyback contract went live in August 2026 in treasury mode: it spends half of any yearly protocol revenue above **$40M** on LDO, with a $10M yearly cap. It filled once, on Aug 13 2026, and then stopped, because revenue is running below the line; its budget read about **$546K below zero** on Sep 29 2026, so the forward value is **0** unless revenue rises.

The protocol fee burn is **0**: Lido earns its fees in staked ETH, and nothing destroys LDO. New long-term locks are also **0** — LDO has no staking of its own, and a Sep 17 2026 forum idea to make node operators post LDO as a bond is still only a discussion. One extra row counts **56,513 LDO** from a cancelled contributor grant that went back to the treasury on Jul 31 2026; it has no schedule, so it adds nothing forward.

## Foundation and overhang

The Lido DAO treasury is the one large team-controlled overhang: **121,497,546 LDO** on Sep 29 2026, up from 108,230,667 at the start of the window because of the buybacks. The re-vested contributor wallets hold **48.93M LDO** that stays locked until Jan 1 2027. On Sep 21 2026 LDO holders also approved, 54.7M to 0, a standby facility that can lend up to **7.5M treasury LDO** to exchange market makers if trading on exchanges gets too thin; it has not been switched on. The contributor-reward multisig holds about **4.0M LDO**, already counted as circulating. The treasury balance is read on-chain at every rebuild, and the forum is walked for new payout or facility decisions. If the treasury's balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How LDO compares to other DeFi governance tokens

LDO belongs to the class of fixed-supply DeFi governance tokens whose protocol earns real fees in another asset. Its closest structural peers are DAO tokens such as UNI and AAVE: no emission to validators, supply set at launch, and value tied to what the DAO chooses to do with its revenue. Among them, the split is between tokens with a standing fee-funded buyback and tokens that rely on votes. LDO now has both — an automatic buyback that only runs above $40M of yearly revenue, and a one-off, vote-approved accumulation program that did almost all of this window's buying.

The mechanism differs from fee-burn tokens. On a chain like Ethereum the burn destroys coins every block; LDO's buybacks do not destroy anything, they park LDO in the Lido DAO treasury. The coins leave the circulating count, but the DAO keeps the power to spend them again — the Sep 21 2026 market-making facility is an example of how treasury LDO could come back. That makes LDO's shrinkage reversible by vote, unlike a burn.

Against tokens still in their vesting years, LDO is almost fully unlocked: **82.96%** of the 1B supply circulates, and the rest is the treasury plus the one re-vesting lock. The difference is that its largest remaining release, the Jan 1 2027 cliff, arrives in a single day rather than as a monthly drip.

## What to watch in the next 90 days

Batch 4 of the LDO accumulation program, 1,000 stETH with a price cap of 0.000165 ETH per LDO, runs until **Nov 24 2026**; if LDO trades above the cap, buying pauses and the forward buy falls short of 6.09M. The contributor reward plan's allocation ends on **Oct 31 2026**, and any new LDO allocation for it would come from the treasury and count as sell pressure. The standby market-making facility of up to 7.5M LDO can be switched on at any time. The automatic buyback restarts only if Lido's revenue climbs back above a $40M yearly pace. And the **48.93M LDO** re-vesting cliff opens on **Jan 1 2027**, just after the window — it will show up in the next rebuild's forward column.

## Summary

LDO is a fixed-supply governance token of Lido DAO, and its circulating supply is shrinking: **−1.60%** over the last 90 days and a projected **−0.73%** over the next 90, with the supply monitor in agreement at **−1.53%**. No new LDO is created; the shrinkage comes from the Lido DAO treasury buying LDO with staked ETH and holding it. The key risk is that the buying depends on votes and price caps, not on a fixed rule, while a **48.93M LDO** cliff opens on Jan 1 2027. The ceiling on new supply is the 1 billion LDO already minted.

---

*MrNasdog Pressure Framework analysis of LDO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

---
title:         "CFX Inflation Analysis · July 2026 · Mixed flows, supply roughly steady"
description:   "Conflux mints ~22.3M CFX/90d from mining + staking with a dormant burn. Framework reads +0.43% net (monitor +0.56%, gap 0.13pp). Uncapped Tree-Graph PoW + PoS L1."
canonical_url: "https://mrnasdog.com/research/cfx/inflation"
tags:          ["crypto", "cfx", "conflux", "layer1"]
published:     true
---

*Originally published at [mrnasdog.com/research/cfx/inflation](https://mrnasdog.com/research/cfx/inflation)*

Conflux is an uncapped proof-of-work and proof-of-stake Layer 1 whose new supply is a mining block reward plus freshly issued staking interest. Over the next 90 days that mints about **22.3M CFX**, while the network's base-fee and storage burn is near-zero on an almost idle chain, so the Pressure Framework reads about **+0.43%** net. Our supply monitor reads **+0.56%** realized over the last 90 days — a gap of about **0.13 percentage points**, inside tolerance, so no monitor-gap chip ships.

## The verdict, in one paragraph

For the 90-day window starting July 7 2026, the MrNasdog Pressure Framework reads **Conflux at +0.43% net** on the forward view — the whole of it from protocol issuance, with essentially nothing on the buy side to offset it. Our supply monitor reads the realized last-90-day change at **+0.56%**, a gap of about **0.13 percentage points**, which is **within the 0.5-point tolerance**, so **no monitor-gap chip** ships. The small difference is not new minting: on-chain issuance measured about **22.3M CFX** over 90 days, while the reported circulating supply grew closer to 29M, so roughly 7M of the monitor's read is circulating reclassification (residual unlock counted into the float), not fresh coins. Conflux is a **quietly, mildly inflationary uncapped chain** whose burn is currently too small to matter.

## Sell pressure: where new CFX comes from

Sell #1 — protocol inflation — is the entire story, at about **22.3M CFX** over the next 90 days, and Conflux mints it two ways. The first is the proof-of-work block reward: miners are paid **0.4 CFX** per block, halved from 0.8 when the Round 20 governance vote took effect on **April 7 2026**. At Conflux's roughly **0.5-second** block time that is about 6.2M CFX over the window. The second is proof-of-stake: stakers earn freshly issued CFX interest, and with roughly **747M CFX** delegated to PoS that adds about 16.1M more. Measured directly on-chain, total issuance ran near **247,000 CFX** per day, which is where the ~22.3M / 90d figure comes from — not a modeled estimate but the observed change in issued supply.

Sell #2 — vesting unlocks — is **zero**: Conflux's distribution schedule finished in 2024 and about **99.85%** of the total supply is already circulating, so no investor, team or ecosystem cliff hits the market in this window. Sell #3 — Foundation and unscheduled unlocks — is also zero; only about **8M CFX** sits outside the circulating float, and the Conflux Foundation treasury has no published release schedule and showed no outflow this window. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate or court distribution applies to Conflux.

## Buy pressure: where new CFX goes

Every buy row is effectively **zero**. Buy #1 — programmatic buyback — is zero: Conflux runs no buyback, and no protocol or foundation spends to take CFX off the market. Buy #2 — protocol fee burn — is where Conflux does have a real mechanism: part of each transaction's base fee is burned, and storage collateral is converted into burned storage points. But the chain is near-idle right now, at about **0.1** transactions per second, so the flow is negligible — the on-chain burn address held **572.96M CFX** and did not move over the measured window, meaning no coins were removed from supply. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero, with no discretionary buying and no new escrow announced. With the burn dormant, the halved block reward and staking interest are unopposed, and net inflation is simply the gross mint divided by circulating supply.

## Foundation and overhang

Conflux has almost **no team-controlled overhang** to track. With about 99.85% of supply circulating, the non-circulating residual is only around **8M CFX** — the gap between the 5,221.95M total supply and the 5,213.89M circulating. The **Conflux Foundation** treasury and ecosystem wallets sit inside that circulating count and carry no published release schedule; they showed no outflow this window and are monitored rather than projected. Note too that roughly **747M CFX** is delegated to proof-of-stake and about **899M** is locked in governance staking — but staked CFX is still counted as circulating and is not an overhang. If the Foundation treasury ever begins distributing CFX on a schedule, those outflows would enter Sell #3 at the next refresh; until then there is nothing to book.

## How CFX compares to other uncapped Layer 1 chains

Conflux belongs to the class of **uncapped Layer 1s that mint continuously** rather than to the hard-capped, halving family. Where Bitcoin or Ethereum Classic issue only a decaying block reward toward a fixed ceiling, Conflux layers **proof-of-stake issuance** on top of its proof-of-work block reward, so there is no supply cap and two mints running at once. The Round 20 halving of the block reward to **0.4 CFX** pulled the mining half down sharply, which is why forward issuance is far lower than in the network's earlier high-emission years — but the staking half keeps supply growing.

Against fee-burning chains like Ethereum, the contrast is activity. Conflux has the same style of **base-fee burn**, but Ethereum's burn can turn it net-deflationary because usage is high, while Conflux's burn is dormant at **0.1** transactions per second — the mechanism exists but has nothing to work with. So on an inflation lens Conflux sits in the middle: milder than a pure high-emission token thanks to the halved block reward, but unable to go negative the way a busy burn chain can. The dominant force is protocol issuance from mining and staking; the brake — the burn — is real in code but idle in practice, and would only bite if on-chain activity picked up.

## What to watch in the next 90 days

Watch the rolling **governance rounds**: Conflux adjusts its block reward, staking interest rate and storage-point ratio by on-chain vote in 60-day cycles, and the Round 20 cut to **0.4 CFX** per block took effect April 7 2026 — the next round that changes any of those parameters would reset the mining half of issuance. Watch the **PoS staked total** near 747M CFX, since the staking mint scales with how much is delegated and at what interest rate. Watch on-chain **activity and the burn address**: if transactions per second rise from today's ~0.1, the base-fee and storage burn would start removing supply and pull the net reading down. And watch whether the reported circulating supply keeps reclassifying residual locked CFX into the float — that is what makes our monitor read slightly above the on-chain mint.

## Summary

Conflux is an uncapped Tree-Graph proof-of-work and proof-of-stake Layer 1 whose new supply is a 0.4 CFX block reward plus freshly issued staking interest, together minting about 22.3M CFX over the next 90 days. Its base-fee and storage burn is real but dormant on a near-idle chain, so almost nothing is removed, leaving the framework at about +0.43% net — a touch below our supply monitor's +0.56% realized read, a 0.13-point gap that is circulating reclassification rather than new coins. CFX stays quietly, mildly inflationary, with mining and staking the only forces and a burn that would only matter if activity returned.

---

*MrNasdog Pressure Framework analysis of Conflux (CFX), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 7, 2026.*

---
title:         "GRT Inflation Analysis · June 2026 · Issuance in, burns out, supply flat"
description:   "Issuance in, burns out: The Graph issues ~74.8M GRT/90d for indexing rewards and burns ~74.8M back via query-fee, curation, delegation and slashing. Net ~0.0%."
canonical_url: "https://mrnasdog.com/research/grt/inflation"
tags:          ["crypto", "grt", "thegraph", "tokenomics"]
published:     true
---

*Originally published at [mrnasdog.com](https://mrnasdog.com/research/grt/inflation).*

The Graph runs a net-supply model: indexing-reward issuance adds about **74.8M GRT** over the next 90 days at a roughly **2.77%** annual pace, while protocol burns — a query-fee burn plus curation, delegation and slashing taxes — remove about **74.8M GRT** back out. The framework reads net **0.0%**: roughly neutral. Our supply monitor reads the realized last-90-day change at **−0.28%**, and the on-chain Ethereum total has held flat near **10.8B** — so issuance and burns cancel on the float.

## The verdict, in one paragraph

For the 90-day window ending June 20 2026, the MrNasdog Pressure Framework reads **GRT at about 0.0% net** — roughly neutral — because new GRT issuance for indexing rewards and the protocol's built-in burns offset each other almost exactly. Our supply monitor reads the realized last-90-day change at **−0.28%**, versus the framework's **0.0%** read, a gap of about **0.3 percentage points** — inside the half-point tolerance, so **no monitor-gap chip** ships. The agreement is structural: the on-chain Ethereum GRT total supply read this session was **10,800,262,816 GRT**, essentially flat, confirming that destruction kept pace with minting. GRT is **net-flat by mechanism** — an uncapped token whose burn machinery has caught up to its issuance.

## Sell pressure: where new GRT comes from

Sell #1 — protocol inflation — is the only force adding GRT, at about **74.8M GRT** over the next 90 days. The Graph issues new GRT to pay Indexers for serving blockchain data, targeted near a **3%** annual rate and running closer to **2.77%** annualized in the most recent quarterly read. On a circulating base near 10.8B, that 2.77% pace works out to roughly 75M GRT per quarter of fresh issuance. Indexing rewards and billing now run on Arbitrum, the protocol's Layer-2 home, but the supply still anchors to the Ethereum ERC-20 contract.

Sell #2 — vesting unlocks — is **zero**: the original team, investor, Foundation, sale and backer allocations are fully unlocked, with the final cliff clearing December 17 2024, so no scheduled vesting adds GRT in the window. Sell #3 — Foundation and unscheduled unlocks — is also zero as a flow; The Graph Foundation runs an ecosystem and grants treasury, but no dated discretionary release outside the issuance schedule fired in the window. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate or court distribution applies to GRT.

## Buy pressure: where new GRT goes

Buy #2 — protocol fee burn — is the offset that defines GRT, removing about **74.8M GRT** over the window. The protocol destroys GRT through several mechanisms at once: **1%** of every query fee is burned, a **1%** curation tax is burned whenever Curators signal on a subgraph, a **0.5%** delegation tax is burned whenever Delegators delegate, and slashing penalties against misbehaving Indexers are partly burned. Together the explicit taxes burn roughly **1%** of supply a year, and over this window destruction held the on-chain Ethereum total flat at about 10.8B — matching the roughly 75M of new issuance.

The rest of the buy ledger is empty. Buy #1 — programmatic buyback — is zero, because the supply offset comes from burning, not open-market buying; there is no GRT buyback. Buy #3 — Foundation buy — is zero, with no disclosed open-market GRT purchases by the Foundation. Buy #4 — new long-term lock — is zero, with no new escrow or multi-year lock announced that would remove circulating GRT. GRT's deflationary pressure is purely the burn, and the burn currently runs neck-and-neck with issuance.

## Foundation and overhang

GRT has little classic overhang. The original vesting allocations — team, future team, advisors, early backers and the public sale — are fully released, so there is no locked-stock cliff waiting to hit the market. The one team-controlled bucket worth watching is the **The Graph Foundation** ecosystem and grants treasury, which funds core development, indexer incentives and ecosystem programs. That treasury is not projected as a flow today: no dated discretionary release outside the issuance schedule fired in the window, and grants disburse in operational increments rather than scheduled unlocks. The framework re-checks the Foundation treasury and the issuance and burn rates on a roughly bi-weekly walk; if the Foundation treasury balance falls between refreshes — a large grant, an incentive program, a market sale — the outflow enters Sell #3 at the next refresh.

## How GRT compares to other net-burn utility tokens

GRT belongs to the class of **uncapped utility tokens with a built-in burn** — issue new tokens to pay the network's workers, then destroy a slice of activity to claw supply back. That makes GRT fundamentally different from a hard-capped token like a fixed-supply governance token, which mints nothing and simply releases a vesting schedule. GRT has no ceiling; instead its net supply is the live difference between an issuance rate and a burn rate, and right now those two run almost even, leaving the token near-flat rather than steadily inflating.

The closest analogue is a fee-burn smart-contract platform that pairs issuance with a base-fee burn — the burn is real but its size tracks usage, so the token only turns net-deflationary when activity is high enough that burns exceed new issuance. GRT sits right at that crossover: issuance near 2.77% annualized is matched by a burn that has kept the on-chain total flat. Unlike a chain whose fees are paid in a different asset, The Graph burns its own token directly through query fees and the curation and delegation taxes, so heavier network use pushes GRT toward net-deflation, while a quiet quarter would let issuance edge ahead. For an inflation lens, GRT reads as the rare token whose burn engine has genuinely caught its emissions — neutral today, with the direction set by query-fee volume.

## What to watch in the next 90 days

Watch query-fee volume and Substreams revenue: because 1% of query fees is burned and the curation and delegation taxes scale with activity, rising network usage tips GRT net-deflationary while a slowdown lets the 2.77% issuance edge ahead. Watch the protocol's next quarterly state report for the updated annualized issuance figure — it has drifted down from 2.84% to 2.79% to 2.77% over recent quarters, and governance can lower the indexing-reward rate further. Watch for any governance proposal that changes the issuance target or adds a buyback, which would be the first new buy-side mechanism. And expect the framework to keep reading roughly flat, in line with our supply monitor and the flat on-chain Ethereum total, until issuance or burn moves materially.

## Summary

GRT is an uncapped utility token whose supply is governed by a net model: indexing-reward issuance adds about 74.8M GRT over the next 90 days at a roughly 2.77% annual pace, while protocol burns — a 1% query-fee burn, a 1% curation tax, a 0.5% delegation tax and burned slashing penalties — remove about the same amount back out. That leaves the framework at about 0.0% net, roughly neutral, and our supply monitor agrees within a third of a percentage point at −0.28% realized, with the on-chain Ethereum total flat near 10.8B. With original vesting fully complete since December 2024, the only swing factor is network usage: heavier query-fee volume pushes GRT net-deflationary, while a quiet stretch lets issuance edge back ahead.

---

*MrNasdog Pressure Framework analysis of The Graph (GRT), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 20, 2026.*

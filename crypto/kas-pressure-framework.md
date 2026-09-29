---
title: "KAS Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description: "KAS supply is growing: miners got 181.84M new KAS in 90 days with no burn or buyback, +0.66% net. Monthly reward cuts bring +0.55% next, toward a 28.70B cap."
canonical_url: "https://mrnasdog.com/research/kas/inflation"
tags: ["crypto", "kas", "kaspa", "proof-of-work"]
published: true
---

> Originally published at **[mrnasdog.com/research/kas/inflation](https://mrnasdog.com/research/kas/inflation)** by MrNasdog.

# KAS Inflation Analysis · September 2026 · Supply growing · projected to keep growing

KAS supply is growing, and it will keep growing, but more slowly each month. Kaspa miners received **181.84M KAS** of new coins in the last 90 days, nothing was burned or bought back, and the net came to **+0.66%** of the **27.73B KAS** in circulation. Because the Kaspa block reward is cut every month, the next 90 days should add about **153.30M KAS**, or **+0.55%**, and the whole schedule stops at a hard cap of about **28.70B KAS**.

## The verdict, in one paragraph

The MrNasdog Pressure Framework reads KAS at **+0.66%** net supply growth over the last 90 days (Jul 1 to Sep 29 2026) and **+0.55%** over the next 90. Our supply monitor, which tracks the market-wide circulating count, reads **+0.83%** for the same stretch — a gap of **0.18 percentage points**, inside our 0.5-point tolerance, so no warning flag is needed. Every KAS on the market was mined, and mining is the only source of new KAS. Kaspa is a **fair-launch proof-of-work chain on a smooth monthly reward cut**: steady new supply, shrinking every month, with nothing on the other side of the ledger.

## Sell pressure: where new KAS comes from

Protocol inflation is the whole story. Kaspa pays a block reward to miners, and the chain makes about 10 blocks a second. The reward follows a fixed table written into the Kaspa node software: it falls a little every month, by the twelfth root of one half, so it halves once a year without the sudden cliff of a four-year halving. Across this window the reward per block stepped down from **2.60 KAS** to **2.18 KAS**, and miners received **181.84M KAS** in total — about **2.02M KAS a day**. We checked that figure against the chain's own supply count on five dates since June, and the new coins match the reward table almost to the coin.

The forward figure uses the schedule, not the trailing rate. Three more monthly cuts land inside the next 90 days — on **Oct 5 2026**, **Nov 4 2026** and **Dec 5 2026** — taking the reward to about **1.84 KAS** per block, so the next 90 days should add **153.30M KAS**, roughly **1.70M KAS a day**. Carrying the old rate forward would have overstated new supply by nearly a fifth.

Vesting unlocks are **zero**: Kaspa launched in Nov 2021 with no premine, no token sale and no coins held back for founders, developers or investors, so there is no unlock schedule and no locked bucket. Foundation and unscheduled unlocks are **zero** because there is no launch treasury; the community funds that do exist hold donated coins that already circulate. Long-term locked or bankruptcy supply is **zero**: no estate, trustee or long lock holds KAS.

## Buy pressure: where new KAS goes

Nothing on the buy side is active. There is **no programmatic buyback**: the Kaspa chain collects no revenue of its own, since every transaction fee goes to the miner who made the block. There is **no protocol fee burn** either. People can send KAS to an address that nobody can ever spend from, and that address holds about **11.23M KAS**, but only about **1,019 KAS** arrived there in this window — far too little to register — and the chain's supply never fell.

There is **no foundation buy**, because no entity buys KAS for the project, and **no new long-term lock**, because proof-of-work has no staking or bonding to pull coins out of the float. KAS deposited into the bridges of apps built on Kaspa is held for its owners and stays spendable, so it counts as circulating.

## Foundation and overhang

Kaspa has no team allocation, so the overhang is small and made of donations. We track five group wallets: the DAGKnight Fund at about **70.25M KAS**, the Rust Fund at about **46.16M KAS**, the Dev Fund at about **1.19M KAS**, the Mining Dev Fund at about **0.22M KAS**, and a small treasurers multisig at about **1,831 KAS**. None of them fell across the window. All of these coins were mined and donated, so they already sit inside the circulating count — spending them to pay developers moves coins around the market rather than adding new ones.

We re-read these balances at every rebuild. If any of these community funds falls between checks, the outflow enters the Foundation and unscheduled unlocks row at the next refresh — and it books there only if the coins come from outside the circulating count, which today none of them do.

## How KAS compares to other proof-of-work chains

KAS and Bitcoin share the core design — fair launch, mining as the only source of coins, a hard cap — but differ in how the reward falls. Bitcoin cuts its block reward in half every four years in a single step; Kaspa cuts a little every month, so its supply curve has no cliffs and no halving-date shock. At roughly **0.55%** per 90 days going forward, KAS still adds new supply faster than Bitcoin does today, because Kaspa is much younger on its curve — but about **96.6%** of all KAS that will ever exist is already mined, and only about **0.98B KAS** remains.

Against uncapped chains the contrast is sharper. Chains with a permanent tail emission, such as privacy coins that pay a small fixed reward forever, never stop adding supply; Kaspa's reward table has a last entry of zero, so absent a hard fork issuance simply ends. Smart-contract Layer 1s that pay validators in new coins often offset part of it with a fee burn; Kaspa has no burn, so its gross issuance and its net issuance are the same number.

Faster block rates do not change this. When Kaspa moved from 1 to 10 blocks a second in May 2025, the reward per block was cut by ten to match, keeping emission per second on the same curve. The roadmap to more blocks per second is built the same way.

## What to watch in the next 90 days

On **Oct 5 2026** the Kaspa block reward drops from 2.18 to 2.06 KAS; on **Nov 4 2026** it drops to 1.94 KAS; and on **Dec 5 2026** it drops to 1.84 KAS — each cut lowers new supply per day by about 5.6%. The fix for the Sep 20 2026 token-indexer exploit on apps built on Kaspa, and the move toward token rules enforced by the chain itself, are worth watching for use of the network, though neither touches the KAS supply. Any step up in blocks per second would be a watch item for the reward table, which on past practice is re-scaled so emission per second stays the same. And the community development funds, especially the DAGKnight Fund and the Rust Fund, are the balances to watch for large outflows.

## Summary

KAS is a fair-launch proof-of-work coin whose supply grows only through mining: **181.84M KAS** in the last 90 days, **+0.66%**, with no burn, no buyback and no lock to offset it. The Kaspa block reward falls every month, so the next 90 days should add about **153.30M KAS**, or **+0.55%**, and the rate keeps shrinking from there. There is no vesting and no team treasury to unlock; the main risk is simply that new coins keep reaching miners, who may sell to cover their costs. The schedule ends at a hard cap of about **28.70B KAS**, with about 96.6% already mined.

---

*MrNasdog Pressure Framework analysis of KAS, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

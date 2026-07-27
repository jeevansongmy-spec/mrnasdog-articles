---
title: "KAS Inflation Analysis · July 2026 · Supply growing, projected to keep growing"
description: "A MrNasdog Pressure Framework read of Kaspa (KAS): ~173.1M KAS per 90 days of chromatic proof-of-work emission against an empty buy ledger. Framework +0.63% net; monitor +0.43%."
canonical_url: "https://mrnasdog.com/research/kas/inflation"
tags: ["crypto", "kas", "kaspa", "proof-of-work"]
published: true
---

> Originally published at **[mrnasdog.com/research/kas/inflation](https://mrnasdog.com/research/kas/inflation)** by MrNasdog.

Kaspa mints about **173.1M KAS** over the next 90 days through proof-of-work mining, against a buy ledger that is empty in every row — no buyback, no burn, no treasury, no staking lock. That is a net of about **+0.63%** on the forward view, down from **+0.75%** over the last 90 days, because Kaspa's chromatic halving cuts the reward roughly **5.6%** every single month. Our supply monitor reads **+0.43%** for the same window — a gap of **0.31 percentage points**, inside tolerance, so no warning flag ships. KAS is a mined, hard-capped coin whose only supply force is a curve that shrinks on schedule.

## The verdict, in one paragraph

For the 90-day window ending **Jul 27 2026**, the MrNasdog Pressure Framework reads **KAS at +0.63% net** forward and **+0.75%** realised over the last 90 days. Our supply monitor reads **+0.43%** for that same trailing window, a gap of **0.31 percentage points** — under the framework's 0.5-point tolerance, so no monitor-gap flag is attached to the page. The two figures differ only because the monitor tracks a classified circulating figure that trails the chain's own mined total, while the framework books the protocol-encoded issuance directly from Kaspa's emission table. Both agree on the shape: Kaspa is **mildly inflationary and disinflating on a fixed schedule** — a quiet chain with one supply force and no offsets.

## Sell pressure: where new KAS comes from

Sell #1 — protocol inflation — is the entire sell ledger, at about **173.1M KAS** over the next 90 days and about **205.4M KAS** over the last 90. Kaspa is a proof-of-work BlockDAG running the GHOSTDAG protocol, and mining is the only mechanism in the design that creates new KAS. The emission follows what Kaspa calls its chromatic halving: instead of cutting the reward in half once every four years the way Bitcoin does, Kaspa cuts it by a factor of **2^(-1/12)** — about **5.6%** — every single month, which compounds to a full halving every twelve months. The reward is defined per second rather than per block, which is why the Crescendo hard fork of **May 5 2025** could raise block production from 1 to 10 blocks per second without changing issuance at all: the per-block subsidy was simply divided by ten.

Read live from the chain on **Jul 27 2026**, the reward is **2.45 KAS** per block at 10 blocks per second, or **24.50 KAS** a second — an exact match to the protocol's own emission table, which is the check that confirms June's Toccata hard fork did not touch the money. Three step-downs land inside the forward window, on **Aug 5 2026**, **Sep 4 2026** and **Oct 5 2026**, walking the rate from 24.50 down to **20.60 KAS** a second. That is why a flat rate would overstate the quarter: the emission decays inside the window, and the framework integrates the steps rather than holding one number.

Every other sell row is zero, and each is zero for a structural reason rather than a quiet quarter. Sell #2 — vesting unlocks — cannot exist: Kaspa was fair-launched on **Nov 7 2021** with no premine, no ICO and no team or investor allocation, so there is no vesting contract anywhere in the design and no cliff can ever arrive. Sell #3 — Foundation and unscheduled unlocks — is zero because there is no foundation treasury, no DAO treasury and no reserve pool holding KAS; every coin that exists was mined into the open market. Sell #4 — long-term locked or bankruptcy — is zero because no bankruptcy estate, court distribution or escrow applies to KAS.

## Buy pressure: where new KAS goes

The buy ledger is empty in all four rows, and that is the most important structural fact about KAS inflation. Buy #1 — programmatic buyback — is **zero** because Kaspa takes no fee revenue and holds no treasury, so there is nothing that could fund a buyback; third-party sites advertising a "KAS buyback and burn" belong to unaffiliated projects, not to the network. Buy #2 — protocol fee burn — is **zero** because Kaspa pays transaction fees to the miner who merges the block rather than destroying them; even blocks that lose the DAG ordering have their reward and fees claimed by the merging miner, so nothing leaks out of supply.

Buy #3 — Foundation buy — is **zero** because there is no company or foundation entity behind Kaspa with a balance sheet to spend. Buy #4 — new long-term lock — is **zero** because Kaspa is proof-of-work with no staking, so no contract can take KAS out of circulation. The practical consequence is that KAS has no mechanism capable of turning net-deflationary. Its inflation can only fall toward zero as the chromatic curve decays; it can never go negative while the protocol stands as written.

## Foundation and overhang

There is no team-controlled overhang for KAS — not a small one, none at all. Kaspa had no premine, no ICO, no team or investor allocation and no foundation treasury, and the project's own site states plainly that there is no premine and no hidden allocation. That removes every sub-category the framework normally enumerates: no unscheduled unlock pool, no Labs treasury, no buyback accumulation wallet, no DAO treasury and no bankruptcy residual. The only forward supply is the roughly **1.10B KAS** still unmined beneath the **28.7B** cap, which reaches the market only through mining on a protocol-fixed curve that no governance body can alter — Kaspa has no on-chain voting, so changing it would require a hard fork the whole network must adopt. Because there is no identified wallet to watch, the trigger sentence attaches to the emission itself: if the chain's live reward ever departs from the chromatic table between refreshes, that departure enters Sell #1 at the next refresh.

## How KAS compares to other hard-capped proof-of-work chains

KAS belongs to the class of **hard-capped proof-of-work coins with a halving-model emission** — the same structural family as Bitcoin and Litecoin, and the opposite of an uncapped continuous-emission proof-of-stake L1. The distinguishing feature is the smoothness. Bitcoin drops its subsidy 50% in a single block every four years, producing a step function that miners and markets brace for; Kaspa spreads the same annual halving across twelve monthly cuts of about 5.6% each, so the emission curve is continuous and the market never faces a cliff. The trade-off is speed: Kaspa halves annually rather than every four years, so its emission decays far faster. About **96%** of the 28.7B cap is already mined less than five years after launch, whereas Bitcoin is still years from that mark.

Against uncapped staking chains, the contrast is sharper still. A Cosmos-style L1 mints new supply forever to pay stakers, and its rate is a governance parameter that a vote can raise. KAS has neither lever: no staking, no governance, no treasury. Against exchange tokens with quarterly buyback-and-burn programmes, KAS is the mirror image — those coins can and do run net-deflationary because a revenue stream funds the removal, while Kaspa has no revenue stream at all and so no removal is possible. Against privacy coins with a permanent tail emission, Kaspa is stricter: the tail here is a hard **28.7B** ceiling, not a perpetual minimum subsidy. For an inflation lens, KAS reads as a coin whose supply story is fully predictable and monotonically improving, but which will sit slightly above zero for as long as there is a subsidy left to pay.

## What to watch in the next 90 days

First, the three chromatic step-downs on **Aug 5 2026**, **Sep 4 2026** and **Oct 5 2026**, which are the only scheduled supply events on the calendar and each cuts issuance a further 5.6%. Second, the live block reward: it should read **2.31 KAS** per block after the August step and **2.06 KAS** after the October one, and any deviation from those figures would mean the emission code changed. Third, post-Toccata activity — the **Jun 30 2026** hard fork added covenants, ZK verification opcodes and native assets, and while none of that alters KAS issuance, a future fork that introduced a fee burn would be the first thing ever to put a number in the buy ledger. Fourth, the block rate itself: a fork that changes blocks per second again would change the per-block reward but not the per-second emission, so the headline should not move. Fifth, the gap between the chain's mined total and the widely-published circulating figure, which has been holding still while the chain kept issuing — a persistent freeze there would change which denominator this page divides by.

## Summary

The MrNasdog Pressure Framework reads KAS at about **+0.63%** net over the next 90 days, from roughly **173.1M KAS** of proof-of-work emission and nothing at all on the buy side. The structural mechanism is Kaspa's chromatic halving, which cuts the mining reward about **5.6%** every month and compounds to a full halving each year, so the inflation rate falls on a schedule that requires no decision from anyone. The key risk is not dilution but the reverse: with roughly **96%** of the **28.7B** cap already mined and no fee burn to replace the subsidy, Kaspa's long-run security budget will have to come from transaction fees rather than issuance. The ceiling is hard, the schedule is fixed, and there is no mechanism anywhere in the protocol that can push supply the other way.

---

*MrNasdog Pressure Framework analysis of KAS, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 27 2026.*

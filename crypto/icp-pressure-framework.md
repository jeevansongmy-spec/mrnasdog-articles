---
title: "ICP Inflation Analysis · July 2026 · Supply growing, projected to keep growing"
description: "A MrNasdog Pressure Framework read of Internet Computer (ICP): 3.43M ICP minted in 90 days for rewards against a 0.22M cycle burn. Framework +0.58% net; monitor +0.74%."
canonical_url: "https://mrnasdog.com/research/icp/inflation"
tags: ["crypto", "icp", "internet-computer", "staking"]
published: true
---

> Originally published at **[mrnasdog.com/research/icp/inflation](https://mrnasdog.com/research/icp/inflation)** by MrNasdog.

Internet Computer is a rare chain that both mints and burns its own token, and the mint side is still winning. Over the last 90 days the protocol minted **3.43M ICP** in node-provider and voting rewards while burning about **0.22M ICP** into computation cycles, so the ledger's own total supply rose from **552.02M** to **555.23M**. Against a circulating base of **555.2M ICP** that is **+0.58% net**, and our supply monitor reads **+0.74%** — a gap of **0.16 percentage points**, well inside tolerance. ICP has no maximum supply, but the Mission 70 reward cut is easing the mint rate through 2026.

## The verdict, in one paragraph

For the 90-day window ending **Jul 30 2026**, the Pressure Framework reads **ICP at +0.58% net**. Sell pressure is **3.43M ICP** of new issuance, buy pressure is **0.22M ICP** of cycle burn, against **555.2M ICP** circulating. Our supply monitor reads the realised change at **+0.74%**, a gap of just **0.16 percentage points** — inside the framework's half-point tolerance, so no monitor-gap chip ships on the ICP overview. The gap that remains is price-noise in the monitor's market-cap-over-price supply estimate, not a disagreement about the ledger: the chain's own total-supply reading moved **+3.21M ICP** across the window, and adding back the burn recovers the framework's 3.43M mint exactly. Projected forward on the easing reward schedule, the next 90 days read **+0.55%**. Internet Computer is best characterised as **mildly inflationary on an uncapped supply, with a burn that is real but not yet large enough to flip it**.

## Sell pressure: where new ICP comes from

Sell #1, protocol inflation, is **3.43M ICP**, and it is effectively the whole sell side. Two reward streams mint new ICP. The first is node-provider rewards: the operators who run the physical machines are paid in freshly minted ICP each month, and the three distributions inside this window — **May 14 2026**, **Jun 13 2026** and **Jul 13 2026** — came to **2.05M ICP** read directly from the reward ledger. The second is voting rewards: neuron holders who stake ICP and vote in governance earn rewards that accrue as maturity and mint into real ICP when they are spawned and cashed out. Node-provider pay alone does not explain the supply move — the chain's total supply rose **3.21M ICP** while node providers minted **2.05M**, so about **1.38M ICP** of matured voting rewards was minted into circulation over the window. Adding the burn back to the observed supply delta is what puts Sell #1 at 3.43M.

The other three sell rows are all **zero**. Sell #2, vesting unlocks, is zero because Internet Computer has no unlock calendar left: the genesis seed and early-contributor allocations vested linearly over four years from **May 2021** and finished around **2025**, and what looks locked today is voluntary staking inside governance neurons rather than a scheduled release. Sell #3, foundation and unscheduled unlocks, is zero because nothing fired a dated ICP outflow — the DFINITY endowment and team neurons sit on eight-year genesis dissolve schedules, and no discretionary release was observed. Sell #4, long-term locked or bankruptcy, is zero: there is no Internet Computer estate, no trustee and no court-ordered distribution.

## Buy pressure: where new ICP goes

Buy #2, protocol fee burn, is the one live offset at **0.22M ICP**. Every time a developer pays for computation or storage, ICP is converted into cycles and destroyed — the burn is the network's gas meter. At the measured average burn rate that removed about **0.22M ICP** over the window, roughly **6%** of the mint. It is real destruction rather than a transfer, and the network's stated goal is to grow it until the burn exceeds issuance and ICP turns net deflationary; the reward changes now phasing in raise compute prices and add a rule that burns **20%** of cloud-engine revenue, both of which push this figure up.

The remaining buy rows are **zero**. Buy #1, programmatic buyback, is zero because Internet Computer pays rewards from new issuance, not from revenue, and runs no contract that buys ICP on the market. Buy #3, foundation buy, is zero because DFINITY has disclosed no open-market ICP purchase programme. Buy #4, new long-term lock, is zero and deserves the clarification, because more than half of all ICP is staked and that can look like a lock: **288.8M ICP** sits inside governance neurons. It is not a permanent lock — neurons can dissolve after their delay elapses, which is a delay rather than a commitment, and every staked token stays inside the circulating figure, so it does not register as buy pressure.

## Foundation and overhang

Internet Computer's overhang is unusually large but almost entirely staker-owned rather than team-owned. Four pools are tracked. The **DFINITY endowment and team neurons** hold genesis allocations on eight-year dissolve schedules, monitored through governance disclosures rather than a single readable dump wallet. The **Neurons' Fund** — the governance-controlled pool that co-invests in ecosystem projects — held about **15.2M ICP** staked when read this session. The broad **staked-neuron pool** of **288.8M ICP** is over half of all supply and can re-enter the float as neurons dissolve. And a **95.3M-ICP-equivalent** pool of accrued but unspawned staking rewards mints into supply gradually as holders cash out — the very stream that put 1.38M into Sell #1 this window. Each is re-read on every rebuild, and if any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How ICP compares to other mint-and-burn L1s

The first comparison is mint-and-burn versus mint-only. Most uncapped proof-of-stake chains only mint — staking rewards flow out and nothing comes back, so supply grows monotonically. Internet Computer is in the smaller group that also burns its token for gas, which means network usage is a genuine deflationary force rather than a fee recycled to stakers. That is the same structural shape as the large fee-burning smart-contract platforms, except ICP burns the whole compute payment rather than a slice of a transaction fee. The catch is scale: the burn currently offsets only about **6%** of issuance, so the mechanism is directionally right but quantitatively small.

The second comparison is cap versus no cap. Halving-model chains with a hard ceiling have a sell side that decays on a published schedule toward zero; ICP has neither a ceiling nor a schedule, and its issuance is a governance-set reward rate that can be raised or cut by vote. That makes the forward path a policy question, not a countdown — which is exactly why the **Mission 70** reward cut matters. Approved on **Apr 7 2026**, it steps voting and node-provider issuance down across 2026, aiming to take raw annual inflation from roughly **9.7%** at the start of the year toward under **3%** by its end. Because the approval predates this window, the last-90-day rate we measured is already the post-cut rate, and the next 90 days project slightly lower still.

The third comparison is float. Many large tokens carry heavy locked buckets, so much of their supply risk is an unlock calendar. Internet Computer has essentially none — total and circulating supply are effectively identical — so there is no cliff to fear; instead its overhang is the slow, continuous drip of matured staking rewards, which is more predictable than a dated unlock but never fully stops.

## What to watch in the next 90 days

First, the cycle burn: it is the one number that could flip ICP deflationary, and the network is actively trying to grow it — a sustained jump in on-chain compute, or heavy use of the new cloud-engine revenue burn, would show up here first. Second, the Mission 70 glide: each further step-down in voting and node-provider rewards through the back half of 2026 lowers Sell #1, and the reward events are published monthly for anyone tracking the pace. Third, node-provider distributions, which land around the middle of each month and are the largest single measurable mint. Fourth, whether any of the tracked neuron pools — the DFINITY endowment, the Neurons' Fund at **15.2M ICP**, or the **95.3M-equivalent** maturity pool — begins a visible drawdown, which is the first thing that would put a non-zero number in Sell #3. Fifth, the ICP-to-cycles conversion rate, since a falling ICP price raises the ICP burned per unit of compute.

## Summary

Internet Computer (ICP) is mildly inflationary on an uncapped supply, with a real but undersized burn. Node-provider and voting rewards minted **3.43M ICP** over 90 days while the cycle burn destroyed about **0.22M ICP**, giving a framework reading of **+0.58% net** against a monitor reading of **+0.74%** — the ledger's own total supply rose **3.21M ICP**, confirming both. The structural mechanism that makes ICP unusual is that computation burns the token, so heavier usage genuinely offsets issuance; the key risk is that this burn still covers only a small fraction of the mint. The one moving part in the coin's favour is the **Mission 70** reward cut, which is easing issuance through 2026, and the coin has no maximum supply to backstop it — the ceiling is a policy setting, not a hard cap.

---

*MrNasdog Pressure Framework analysis of ICP, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 30 2026.*

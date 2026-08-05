---
title: "ICP Inflation Analysis · August 2026 · Supply growing slowly, projected to keep easing"
description: "A MrNasdog Pressure Framework read of Internet Computer (ICP): 3.41M ICP minted in 90 days for rewards against a 0.19M cycle burn. Framework +0.58% net; monitor +0.99%."
canonical_url: "https://mrnasdog.com/research/icp/inflation"
tags: ["crypto", "icp", "internet-computer", "staking"]
published: true
---

> Originally published at **[mrnasdog.com/research/icp/inflation](https://mrnasdog.com/research/icp/inflation)** by MrNasdog.

Internet Computer is a rare chain that both mints and burns its own token, and the mint side is still winning — but only just. Over the last 90 days the protocol minted about **3.41M ICP** in node-provider and voting rewards while converting only about **0.19M ICP** into computation cycles and destroying it. Against a circulating base of about **555.30M ICP** that is **+0.58% net**, and our supply monitor reads **+0.99%** — a gap of **0.41 percentage points**, inside the framework's tolerance, so no data-conflict chip ships. ICP has no maximum supply, but an issuance cut approved in April is steadily winding the mint rate down through 2026.

## The verdict, in one paragraph

For the 90-day window ending **Aug 5 2026**, the Pressure Framework reads **ICP at +0.58% net** for both the trailing and the forward window. Sell pressure is about **3.41M ICP** of new issuance; buy pressure is about **0.19M ICP** of cycle burn; the base is roughly **555.30M ICP** circulating. Our supply monitor reads the realised change at **+0.99%**, a gap of only **0.41 percentage points** — inside the framework's half-point tolerance, so no monitor-gap chip appears on the ICP overview. The two agree because both capture the same reality: the Internet Computer mints new ICP for node providers and NNS voters faster than its cycle burn can remove it, but by well under one percent a quarter. ICP is best characterised as **a mildly inflationary, uncapped Layer 1 whose issuance is being deliberately wound down**.

## Sell pressure: where new ICP comes from

Sell #1, protocol inflation, is about **3.41M ICP**, and it is effectively the whole sell side. Two reward streams mint new ICP. The larger is node-provider rewards: the operators who run the Internet Computer's physical machines are paid a freshly minted ICP amount each month, which came to roughly **2.05M ICP** across the three monthly distributions inside this window. The remainder, about **1.36M ICP**, is matured NNS voting rewards — ICP that neurons earned for voting in governance and then spawned into liquid supply. Voting rewards accrue far faster than that on paper, but most stay staked and compounding, which is why ICP's realised inflation is a fraction of its headline reward rate. Crucially, the node-provider mint has already stepped down about **30%** since April, when a governance-approved issuance cut began, so this window already runs at the reduced rate.

The other three sell rows are all **zero**. Sell #2, vesting unlocks, is zero because the Internet Computer has no unlock calendar left: the 2021 genesis seed and early-contributor allocations sit in long-dissolving NNS neurons rather than on a release schedule, and unstaking a neuron only makes already-counted ICP liquid — it mints no new supply. Sell #3, foundation and unscheduled unlocks, is zero because no dated ICP outflow fired; the DFINITY Foundation holds a large ICP position across its treasury and neurons, but disclosed no sale or distribution this window. Sell #4, long-term locked or bankruptcy, is zero: there is no Internet Computer estate, no trustee and no court-ordered distribution.

## Buy pressure: where new ICP goes

Buy #2, protocol fee burn, is the one live offset, at about **0.19M ICP**. ICP is destroyed whenever it is converted into cycles, the fuel that canisters spend on computation and storage; the Internet Computer's "reverse gas" model means users burn ICP-derived cycles rather than paying gas directly. Integrating the on-chain cycle-burn rate across the window works out to that roughly **0.19M ICP** — genuine deflationary pressure, real destruction rather than a transfer, but far too small to cover a 3.41M mint. The network's stated goal is to grow it until the burn exceeds issuance and ICP turns net deflationary; rising usage and a plan to route roughly **20%** of cloud-engine revenue into ICP burns would push this figure up over time.

The remaining buy rows are **zero**. Buy #1, programmatic buyback, is zero because the Internet Computer pays rewards from new issuance, not from revenue, and runs no contract that buys ICP on the market. Buy #3, foundation buy, is zero because no discretionary open-market ICP purchase was disclosed this window. Buy #4, new long-term lock, is zero and deserves the clarification, because more than half of all ICP is staked and that can look like a lock: staking ICP into an NNS neuron takes it off the tradable float, but every staked token still counts inside the circulating figure, so it is not a supply removal. With only the cycle burn offsetting the mint, ICP's net reading is simply the mint minus that small burn.

## Foundation and overhang

The Internet Computer's overhang is unusually large but almost entirely staker-owned rather than team-owned. One team-controlled position is tracked: the DFINITY Foundation treasury and its governance neurons hold a large ICP position, but the Foundation does not publicly itemise its exact liquid balance, so it is monitored as an opaque position through its disclosures rather than a live on-chain figure. Separately, the 2021 genesis seed and early-contributor neurons continue to dissolve on their eight-year schedules, but because staked ICP already counts as supply, a dissolving neuron moving ICP from staked to liquid does not add to the framework's reading. Both are re-read on every rebuild, and neither fired in the window. If the Foundation's balance falls sharply between refreshes through a single large distribution, that outflow enters Sell #3 at the next refresh.

## How ICP compares to other mint-and-burn L1s

The first comparison is mint-and-burn versus mint-only. Most uncapped proof-of-stake chains only mint — staking rewards flow out and nothing comes back, so supply grows monotonically, and net supply growth equals the full mint. The Internet Computer is in the smaller group that also burns its token for gas, which means network usage is a genuine deflationary force rather than a fee recycled to stakers. It shares that two-sided structure with post-Merge Ethereum, where staking issuance is partly offset by a base-fee burn — except ICP burns the whole compute payment rather than a slice of a transaction fee. The catch is scale: the burn currently offsets only a sliver of issuance — about **0.19M** against **3.41M** — so the mechanism is directionally right but quantitatively small, and ICP stays net-inflationary.

The second comparison is cap versus no cap. Halving-model chains with a hard ceiling issue on a fixed, shrinking schedule toward that ceiling; ICP has neither a cap nor a schedule, and its issuance is a governance-set reward rate that can be raised or cut by vote. That makes the forward path a policy question, not a countdown — which is exactly why the April issuance cut matters. Approved on **Apr 7 2026**, it steps voting and node-provider rewards down across 2026, aiming to take issuance toward a target roughly **70%** below where it began the year while pushing more revenue into burns. Because the approval predates this window, the last-90-day rate we measured is already the post-first-step rate, and the next 90 days project no higher.

The third comparison is float. Many large tokens carry heavy locked buckets, so much of their supply risk is an unlock calendar. The Internet Computer has essentially none — total and circulating supply are effectively identical — so there is no cliff to fear; instead its overhang is the slow, continuous drip of matured staking rewards, which is more predictable than a dated unlock but never fully stops. That structural gap between a high theoretical reward rate and a modest realised supply growth is the defining feature of ICP's tokenomics.

## What to watch in the next 90 days

First, the cycle burn near **0.19M ICP** a quarter: it is the one number that could flip ICP deflationary, and the network is actively trying to grow it — a sustained jump in on-chain compute, or the planned routing of about **20%** of cloud-engine revenue into burns, would show up here first. Second, the issuance glide: the node-provider cut has already landed, but further step-downs in voting and node-provider rewards are scheduled through the back half of 2026, and each one lowers Sell #1 directly. Third, node-provider distributions, which land around the middle of each month and are the largest single measurable mint. Fourth, the DFINITY Foundation treasury for any single large ICP distribution, which is the first thing that would put a non-zero number in Sell #3. Fifth, the ICP-to-cycles conversion rate, since a falling ICP price raises the ICP burned per unit of compute.

## Summary

Internet Computer (ICP) is a mildly inflationary, uncapped Layer 1 whose supply is a tug-of-war between minting and burning. Node-provider rewards and spawned NNS voting rewards minted about **3.41M ICP** over 90 days, while the cycle burn destroyed only about **0.19M ICP**, leaving net new supply of **+0.58%**; our monitor reads **+0.99%**, a **0.41-point** gap inside tolerance. The structural mechanism that makes ICP unusual is that computation burns the token, so heavier usage genuinely offsets issuance; the key risk is that this burn still covers only a small fraction of the mint. The one moving part in the coin's favour is the April issuance cut, which is easing supply growth through 2026 — and on an uncapped supply, ICP's direction now depends less on a ceiling than on which side of the mint-versus-burn race wins.

---

*MrNasdog Pressure Framework analysis of ICP, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 5 2026.*

---
title:         "CFX Inflation Analysis · August 2026 · Mixed flows, supply roughly steady"
description:   "Conflux mints ~22M CFX a quarter from mining and staking, with an idle burn and no buyback. MrNasdog Pressure Framework reads +0.42% net against a monitor at +0.42%."
canonical_url: "https://mrnasdog.com/research/cfx/inflation"
tags:          ["crypto", "cfx", "conflux", "layer1"]
published:     true
---

*Originally published at [mrnasdog.com/research/cfx/inflation](https://mrnasdog.com/research/cfx/inflation)*

# CFX Inflation Analysis · August 2026 · Mixed flows, supply roughly steady

Conflux is close to flat. Block rewards and staking rewards minted about **22M CFX** over the last 90 days, and nothing at all came off the other side — no buyback, and a fee burn that never fired. The story here is the **Apr 7 2026** governance cut that halved the mining reward from **0.8** to **0.4 CFX** per block, which is why an uncapped chain now reads only **+0.42% net** against our supply monitor at **+0.42%** — a gap of about **0.01 percentage points**. CFX has no maximum supply and no vesting left, so this rate is the whole story.

## The verdict, in one paragraph

For the 90-day window ending Aug 2 2026, the Pressure Framework reads **Conflux at +0.42% net**. Sell pressure is **22M CFX**, buy pressure is **zero**, against a circulating base of **5.21B CFX**. Our supply monitor reads the realised change at **+0.42%**, a gap of roughly **0.01 percentage points** — well inside tolerance, so no monitor-gap chip ships on the CFX overview. The two readings agree because the burn address is frozen: with nothing being destroyed, the growth in circulating supply is simply the gross mint. Conflux is best characterised as **structurally inflationary but nearly flat** — an uncapped proof-of-work and proof-of-stake chain whose issuance was cut in half by governance and whose only offset mechanism is dormant.

## Sell pressure: where new CFX comes from

Sell #1, protocol inflation, is **22M CFX**, and it is the entire sell ledger. Conflux mints new CFX from two sources: proof-of-work block rewards and proof-of-stake finalization rewards. The proof-of-work reward is set by on-chain DAO voting in 60-day rounds, and the decisive event for this reading came before the window even opened — a governance round voted the reward down **0.8** to **0.4 CFX** per block, activated **Apr 7 2026**. Reading the chain directly, the reward parameter is **0.40133 CFX** per block, byte-identical at the value it took after that cut, which confirms no later round changed it inside the window. At roughly **0.4992** seconds per block and about **37.7M** blocks over 90 days, proof-of-work alone accounts for near **15M CFX**, with staking rewards bringing the total to about **22M**.

The remaining sell rows are all **zero**, and for structural reasons rather than a quiet quarter. Sell #2, vesting unlocks, is zero because Conflux has no unlock calendar left at all: the Ecosystem Fund, Genesis Team, private-investor, Community Fund and Foundation allocations finished releasing in **2024**, and the chain's total supply of **5.23B** now sits within about **14.5M CFX** of the circulating figure, so under **0.3%** of supply is non-circulating and none of it is scheduled. Sell #3, foundation and unscheduled unlocks, is zero because nothing was released — the tracked overhangs did not move in the window. Sell #4, long-term locked or bankruptcy, is zero: there is no Conflux estate, no trustee and no court-ordered CFX distribution.

## Buy pressure: where new CFX goes

All four buy rows are **zero**, and this is what keeps Conflux inflationary despite the reward cut. Buy #1, programmatic buyback, is zero because Conflux has never deployed a buyback contract and runs no revenue-funded purchase programme; the supply reductions it does carry out are one-off governance burns, not a standing mechanism. Buy #2, protocol fee burn, is the interesting one: a base-fee burn genuinely exists, but the chain is quiet enough that it never fires. The burn address held **572,964,410 CFX** and did not move by a single unit across the entire window, so the realised burn is **zero**. The **76M CFX** governance burn that Conflux watchers remember was executed in **2025**, more than a year before this window, and is long settled.

Buy #3, foundation buy, is zero because the Conflux Foundation has disclosed no open-market CFX purchase. Buy #4, new long-term lock, is zero and deserves a clarification, because Conflux does have a large staked position that can look like a lock. The **500M CFX** the Foundation staked into proof-of-stake was locked in a **2025** governance round, not this one, and staked CFX remains inside the circulating figure — it is participation, not removal. Nothing new was locked in the window, so this row contributes nothing.

## Foundation and overhang

Two team-controlled overhangs are tracked on Conflux, and both are small relative to a fully unlocked 5.21B-token supply. The first is the **non-circulating residual** — about **14.5M CFX**, the gap between total and circulating supply, held across Foundation and ecosystem addresses with no release schedule. The second is the **500M CFX** the Conflux Foundation staked into proof-of-stake in 2025 to lower the staking yield; it is Foundation-controlled but counted as circulating, and it is monitored for any unstaking. Both are re-read on every rebuild, and if either balance falls between refreshes, the outflow enters Sell #3 at the next refresh. The burn address, holding **573M CFX**, is excluded from the overhang because those tokens are destroyed, not held.

## How CFX compares to other uncapped proof-of-stake chains

The first comparison is cap versus no cap. Halving-model chains with a hard ceiling have a sell side that shrinks on a fixed schedule and eventually reaches zero; Conflux has no ceiling, so its issuance never terminates. What it does have is a governance lever most uncapped chains lack — the proof-of-work reward is a DAO parameter, adjustable every 60 days by vote, and the community used it to halve issuance in April 2026. That makes Conflux's inflation neither a countdown nor a fixed control loop but a discretionary dial, which is a genuinely different risk shape: the rate can be cut again, but it can also be raised again.

The second comparison is burn versus no burn. The large fee-burning networks route a share of every transaction fee to destruction, so a busy chain can print negative net supply. Conflux has the mechanism but not the activity — the base-fee burn is live yet dormant, and until on-chain usage rises enough to feed it, the buy side of this ledger stays empty. Combined with the absence of a buyback, that leaves Conflux in the group of uncapped chains with a live mint and nothing structural on the other side, distinguished only by how far governance has already pushed the mint down.

The third comparison is float. Many large tokens carry heavy non-circulating buckets, so much of their supply risk is a release calendar. Conflux carries almost none — it finished unlocking in 2024, and total and circulating supply are within a fraction of a percent, which removes unlock risk entirely and makes CFX's reading unusually honest. What you see is what exists, and what exists now grows only about **1.7% a year**.

## What to watch in the next 90 days

First, the DAO parameter rounds: the proof-of-work reward is voted every 60 days, and another cut — or a reversal — is the single largest lever on this reading, so the next activated round is the first thing to check. Second, whether on-chain activity rises enough to wake the base-fee burn; the Fireblocks custody integration from **Jun 11 2026** and the Infini stablecoin rail from **Jul 6 2026** are the kind of demand catalysts that would start feeding it, and the burn address moving at all would put a non-zero number in Buy #2. Third, the block rate itself — issuance scales with blocks produced, so a sustained change in block time shifts Sell #1 without any parameter vote. Fourth, the **500M CFX** Foundation stake — any unstaking is the first event that would put a number in Sell #3. Fifth, any fresh governance burn-and-stake proposal, the recurring mechanism that removed 76M CFX in 2025.

## Summary

Conflux (CFX) is structurally inflationary but nearly flat: block and staking rewards minted **22M CFX** over 90 days while buybacks, fee burns, foundation purchases and lockups all contributed **zero**, giving a framework reading of **+0.42% net** against a monitor reading of **+0.42%**. The reason the number is this low on an uncapped chain is governance: a DAO vote halved the proof-of-work reward from **0.8** to **0.4 CFX** per block, effective **Apr 7 2026**. The key risk is that both sides of this equation are discretionary — the mint can be raised again by the same vote that cut it, and the burn stays idle until activity grows into it. CFX has no maximum supply and no unlock calendar left, so the only thing steering its inflation is the community's hand on the reward dial.

---

*MrNasdog Pressure Framework analysis of CFX, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 2 2026.*

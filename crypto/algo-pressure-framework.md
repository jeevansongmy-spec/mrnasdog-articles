---
title:         "ALGO Inflation Analysis · August 2026 · Supply growing slowly, projected to keep growing"
description:   "Algorand mints nothing under its 10B hard cap, yet ~43M ALGO per 90 days reaches the market from a block bonus and Foundation reserve. Framework +0.48% net measured and forward; monitor +0.64%."
canonical_url: "https://mrnasdog.com/research/algo/inflation"
tags:          ["crypto", "algo", "algorand", "layer1"]
published:     true
---

> Originally published at **[mrnasdog.com/research/algo/inflation](https://mrnasdog.com/research/algo/inflation)** by MrNasdog.

# ALGO Inflation Analysis · August 2026 · Supply growing slowly, projected to keep growing

Algorand is a hard-capped chain that never mints, yet its float still grows — because supply comes out of the Algorand Foundation reserve, not out of new issuance. Over the last 90 days a decaying per-block bonus released about **20.1M ALGO** and the Foundation spent about **23.1M ALGO** of reserve into circulation, roughly **43M ALGO** in all, while buybacks, burns, foundation purchases and lockups removed **zero**. That is **+0.48% net** against a circulating base of **8.97B ALGO**, versus our supply monitor at **+0.64%** — a gap of **0.15 percentage points**. ALGO is capped at **10B**, and both taps are easing.

## The verdict, in one paragraph

For the 90-day window ending **Aug 4 2026**, the MrNasdog Pressure Framework reads **ALGO at +0.48% net**. Sell pressure is **43.2M ALGO** — **20.1M** from the block bonus and **23.1M** from Foundation reserve release — and buy pressure is **zero**, against a circulating base of **8,969.018M ALGO**. Our supply monitor reads the realised change at **+0.64%**, a gap of **0.15 percentage points**, comfortably inside the framework's 0.5-point tolerance, so no monitor-gap chip ships on the ALGO overview. The monitor sits a little higher because July fell into an as-yet-unreported quarter and appears to be running slightly above the last reconciled rate. Because both the last-90-day and next-90-day readings land just under half a percent, the verdict is **mixed flows, supply roughly steady** — Algorand is best characterised as **a capped, fully-minted chain whose float grows only as fast as the Foundation chooses to release reserve**.

## Sell pressure: where new ALGO comes from

The important fact about Algorand is that all **10 billion ALGO** were minted in the 2019 genesis block, and the protocol has no mint function and no burn address. So nothing on this ledger is newly created — every ALGO that reaches the market was minted years ago and is simply leaving the Algorand Foundation reserve. Sell #1, protocol inflation, is **20.1M ALGO**, and it is the block-production bonus. Under Algorand's incentivised consensus, live since **Jan 23 2025**, each block pays its proposer a bonus that started at **10 ALGO** and decays **1% every million blocks**, plus half of the block's transaction fees. Reading the chain directly, that bonus is now about **8.44 ALGO** per block, down from roughly **8.70 ALGO** at the start of the window; because blocks proposed by ineligible accounts pay nothing, the average across all blocks is near **7.2 ALGO**, which over roughly **2.83M blocks** comes to about **20.4M ALGO**. The Foundation's own quarterly report books staking rewards at **20.1M ALGO**, so two independent readings agree.

Sell #3, Foundation and unscheduled unlocks, is **23.1M ALGO**, and it is the second and larger discretionary tap. The Foundation's second-quarter transparency report reconciles its holdings line by line: **1,078,875K ALGO** at the end of March fell to **1,035,603K** at the end of June, so **43.3M ALGO** left the Foundation over the quarter. Removing the **20.1M** staking-rewards line leaves **23.1M** of discretionary release — structured and OTC selling of **10.6M**, plus ecosystem support, xGov, grants, marketing, operations and R&D. That structured-selling figure is the headline: it fell from **24.0M** in the first quarter to **10.6M** in the second, so the Foundation is putting materially less ALGO on the market than it was.

The remaining sell rows are **zero** for structural reasons. Sell #2, vesting unlocks, is zero because Algorand has no unlock calendar left: the early-backer and genesis allocations finished releasing in 2024, and unlock trackers list ALGO as fully unlocked. Sell #4, long-term locked or bankruptcy, is zero because there is no Algorand estate, no trustee and no court-ordered ALGO distribution.

## Buy pressure: where new ALGO goes

All four buy rows are **zero**, and this is the defining fact about ALGO. Buy #1, programmatic buyback, is zero because Algorand runs no buyback — and the Foundation is not a buyer at all, it is a disclosed structural net seller through its published structured-selling programme. Buy #2, protocol fee burn, is zero because Algorand does not burn transaction fees. Fees are collected in the protocol fee sink and recycled — half to the block proposer and the rest back through the same pool that funds the block bonus — so fee activity never destroys ALGO, and fees are tiny in any case, well under one percent of what the bonus pays out.

Buy #3, foundation buy, is zero because neither the Foundation nor any ecosystem entity has disclosed an open-market ALGO purchase, and no accumulation wallet has been identified. Buy #4, new long-term lock, is zero and deserves the clarification, because more than **2B ALGO** is staked and that can look like a lock. It is not one: staking on Algorand is non-custodial, has no bonding period and no slashing, so staked ALGO never leaves the holder's wallet and stays fully liquid inside the circulating figure. No new lockup contract was deployed in the window.

## Foundation and overhang

The one team-controlled overhang on Algorand is the **Algorand Foundation reserve** itself — the entire non-circulating gap to the 10B cap, about **1.03B ALGO**, or roughly **1,035,603K** as reported at the end of June. It is the source of both taps in this ledger: it seeds the fee-sink pool that pays the block bonus, and it is spent down directly through structured selling, grants and operations. The reserve is unscheduled — there is no published release calendar, only the observed drain of about **43M ALGO** a quarter that the transparency reports document after the fact. Two on-chain structured-selling wallets execute the market selling but hold almost nothing between transfers, and a small pool of unspent community-voted xGov allocations sits alongside. All of it is re-read on every rebuild, and if the reserve balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How ALGO compares to other capped proof-of-stake L1s

The first comparison is cap versus emission. Uncapped proof-of-stake chains mint new tokens forever, so their sell side is a live issuance rate that never reaches zero. Algorand is the opposite: the **10B** cap was reached at genesis, nothing is ever minted, and the sell side is not issuance at all but the release of an existing reserve. That makes ALGO's supply risk finite and, unusually, fully disclosed — the Foundation publishes exactly how much reserve is left and how fast it is spending it.

The second comparison is burn versus no burn. Fee-burning networks route a share of every transaction fee to destruction, so a busy chain can print negative net supply. Algorand recycles its fees back through the fee sink instead, so activity on Algorand, however strong, can never show up as buy pressure in this framework. Combined with the absence of a buyback, it leaves ALGO with a live sell mechanism and nothing on the other side of the ledger — the same shape as an uncapped chain, even though the cap is real.

The third comparison is who controls the tap. On a halving-model chain the emission schedule is fixed in code and no one can change it. On Algorand the dominant tap is the Foundation's discretionary reserve spend, which means the single biggest driver of ALGO's near-term supply is a governance-and-treasury decision, not a protocol constant. That cuts both ways: the Foundation just halved its structured selling quarter-on-quarter, which is why this reading is milder than the last.

## What to watch in the next 90 days

First, the block bonus: it keeps decaying 1% every million blocks and will step down several more times inside the window, so Sell #1 shrinks slowly on its own; the roughly **24-month** Foundation commitment behind the bonus, which began in January 2025, runs out in early 2027. Second, structured selling — the Foundation cut it from **24.0M** to **10.6M** in a single quarter, and whether that lower pace holds is the biggest swing factor in the next reading. Third, the next monthly supply report and the third-quarter transparency report, which will confirm whether July's slightly hotter pace was a one-off or a new trend. Fourth, community staking participation, which has risen past **80%** community-held and quietly shifts more of the block bonus away from the Foundation's own validators. Fifth, any governance move to change the fee sink or the bonus schedule, which would be the first structural change to this ledger since incentivised consensus launched.

## Summary

Algorand (ALGO) is a hard-capped, fully-minted proof-of-stake chain whose float grows only as fast as the Algorand Foundation releases reserve. Over the last 90 days the block bonus released about **20.1M ALGO** and Foundation reserve spend added about **23.1M**, roughly **43M** in all, while buybacks, burns, foundation purchases and lockups contributed **zero** — a framework reading of **+0.48% net** against a monitor reading of **+0.64%**, a **0.15-point** gap well inside tolerance. Both taps are easing: the per-block bonus decays automatically and the Foundation halved its structured selling quarter-on-quarter. The key risk is that the dominant tap is discretionary, not protocol-fixed, so the largest driver of ALGO's supply is a Foundation decision — and the ceiling is the **10B** cap and the roughly **1.03B** of reserve still behind it.

---

*MrNasdog Pressure Framework analysis of Algorand (ALGO), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated August 4, 2026.*

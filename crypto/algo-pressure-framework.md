---
title:         "ALGO Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description:   "Algorand cannot mint under its 10B cap, yet 111.5M ALGO reached the market in 90 days: 18.7M of measured block bonus plus 92.8M out of Foundation wallets. Framework +1.24%, monitor +1.17%."
canonical_url: "https://mrnasdog.com/research/algo/inflation"
tags:          ["crypto", "algo", "algorand", "layer1"]
published:     true
---

> Originally published at **[mrnasdog.com/research/algo/inflation](https://mrnasdog.com/research/algo/inflation)** by MrNasdog.

# ALGO Inflation Analysis · August 2026 · Supply growing, projected to keep growing

Algorand is a hard-capped chain that cannot mint a single new ALGO — all **10,000,000,000** were created in the 2019 genesis — and it is still one of the more inflationary assets in this coverage, because both of its supply taps run out of pools the **Algorand Foundation** already controls. Over the last 90 days the block-production bonus paid **18.7M ALGO** and another **92.8M ALGO** transferred out of the Foundation's 74 published wallets, against **zero** buyback and **zero** burn — a net of **+1.24%**, with our supply monitor at **+1.17%**.

## The verdict, in one paragraph

For the 90-day window ending **Aug 19 2026**, the Pressure Framework reads **ALGO at +1.24% net**. Sell pressure totals **111.5M ALGO**, buy pressure totals **zero**, against a circulating base of **9.03B ALGO**. Our supply monitor reads the same window at **+1.17%**, a gap of **0.07 percentage points**, comfortably inside tolerance, so no data-conflict chip ships on the overview page. The agreement is worth stating precisely, because the two sides count different things: the monitor divides a classified circulating-supply series — ten billion less the wallets the Foundation publishes — by its own value from 90 days earlier, while this ledger counts the individual transfers that left those wallets plus the block payouts that actually landed. They converge because the Foundation's classification is honest and current. The forward reading is **+0.90%**. ALGO is best characterised as a **hard-capped chain with no mint and no burn, whose entire inflation question is how fast its Foundation spends**.

## Sell pressure: where new ALGO comes from

Sell #1, protocol inflation, is **18.7M ALGO**, and Algorand has no protocol inflation in the usual sense at all. There is no mint function; the ledger read **10,000,000,000** at the open of the window and the same at the close. What behaves like emission is the **block-production bonus**: every block on Algorand carries a bonus paid to whoever proposed it, funded from the fee sink that the Algorand Foundation seeds out of its treasury. The documented rate is **8.35 ALGO per block**, decaying **1% every million blocks**, and the chain produced **2,827,187** blocks over the 90 days — multiply those together and you get **24.0M ALGO**.

That number is wrong, and the gap between it and the truth is the single most important measurement on this page. A block pays its bonus only when the proposer is incentive-eligible; when it is not, the block pays nothing at all. Sampling **2,500** blocks at random across the window shows that only **81%** of them paid, putting the realised payout at **19.5M ALGO** rather than 24.0M — the published rate overstates by **1.23 times**. Strip out the **0.6M** that was proposed by Foundation-run wallets and never left their custody, and the **0.1M** of transaction fees users paid into the sink over the same period, and the bonus tap added **18.7M ALGO** of genuine float. Forward, the decay alone takes that to **18.2M**.

Sell #2, vesting unlocks, is **zero**. Algorand has no vesting contract and no cliff calendar; the original genesis distribution schedule ran out in **2024**. Sell #4, long-term locked or bankruptcy, is **zero**: there is no estate, no trustee and no court-ordered distribution. Sell #3, Foundation and unscheduled unlocks, is **92.8M ALGO** — five times the size of the protocol row, and the reason ALGO reads inflationary. Every one of the **74** addresses the Algorand Foundation publishes was swept transfer by transfer over the exact window, and **92.8M ALGO** left them with nothing coming back. Balances alone would have hidden it: the market-operations wallet holds **1.0M ALGO** today and passed **42.0M** through itself in nine tranches, and one treasury wallet that moved **10.4M** in July has since been closed and deleted from the ledger entirely.

## Buy pressure: where new ALGO goes

All four buy rows are **zero**, and each one is worth proving rather than asserting. Buy #1, programmatic buyback, is **zero** because no ALGO buyback exists — the Algorand Foundation is a disclosed seller through published market-operations wallets, and the sweep found no inbound ALGO to any of the 74 addresses at any point in the 90 days. Buy #3, Foundation buy, is **zero** for the same measured reason: every flow was outbound.

Buy #2, protocol fee burn, is **zero**, and this is where Algorand differs sharply from the fee-burning chains it is often compared with. ALGO fees are not destroyed. They are collected into the fee sink, and half of each block's fees is handed straight back to that block's proposer — verified in the block header, where the payout equals the bonus plus half the fees collected — while the remainder stays in the very pool the bonus is paid from. Fees on Algorand therefore recycle; they never leave the system. There is no burn address, the account model has no destroy operation, and the total has been the same ten billion since 2019. Buy #4, new long-term lock, is **zero** because Algorand consensus participation has no bond, no unbonding period and no slashing: roughly **2.0B ALGO** participates in consensus and stays fully liquid and tradable throughout, which is a holder preference, not supply taken off the market.

## Foundation and overhang

The Algorand Foundation's **74** published wallets still hold **944.1M ALGO**, roughly a tenth of the cap, on no published release schedule at all — this is the whole overhang and it is re-read on every rebuild. Inside it, three pools matter separately. The **market-operations** wallets, used for structured selling, rest at **1.0M ALGO** and are refilled by ten-million-ALGO treasury top-ups, most recently on **Aug 5 2026**; their balance says nothing about their throughput, which was **42.0M** this window. The **fee sink** holds **11.5M ALGO** and drains at the bonus rate, topped up by **10.3M** from the treasury on **Jul 10 2026**. And a fourth item sits outside the registry: **30.0M ALGO** sent on **Jul 17 2026** to an account created two days earlier and never added to the published list, which has already passed **25.0M** onward and holds **5.0M**. If any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How ALGO compares to other hard-capped Layer 1 chains

The first comparison is cap versus mint, and here Algorand looks excellent on paper. Uncapped proof-of-stake Layer 1 chains mint fresh coins to pay validators, so their inflation is permanent and scales with the staking rate. Algorand cannot mint at all: the **10,000,000,000** ceiling was set once, and validator pay comes out of a pre-funded pool instead of new issuance. The arithmetic consequence is that ALGO's worst case is bounded — the **944.1M ALGO** still in Foundation custody is the entire remaining supply overhang, about **10%** of the cap, and when it is spent the float simply stops growing.

The second comparison is with hard-capped chains that also burn. Chains with a fee burn convert usage into supply reduction, so a busy quarter can net negative. Algorand routes the identical fee flow back to block producers rather than to a burn address, so activity on Algorand can never shrink the float — the buy side of this ledger is empty by design, not temporarily quiet. That is the real distinction: a capped supply protects the ceiling, but only a burn or a buyback pushes the number down, and Algorand has neither. Compared with halving-model chains, the resemblance is the decay schedule — the bonus falls 1% per million blocks the way a subsidy halves — but the source is a Foundation commitment, not consensus code, which makes it a policy that can end rather than a rule that cannot.

## What to watch in the next 90 days

First, the pace of the structured selling: nine tranches between **Jun 1 2026** and **Aug 10 2026** is a steady programme, and the forward column carries **43.1M ALGO** on that basis — a pause or an acceleration moves the whole reading. Second, whether the **30.0M ALGO** account from **Jul 17 2026** is ever added to the published registry, which would reverse that call and cut the last-90-day figure by nearly a third. Third, the fee sink balance, at **11.5M ALGO** against a bonus tap consuming roughly **19.5M** a quarter — it needs another treasury top-up before the end of the year, and each top-up is a dated, visible event. Fourth, the consensus upgrade that activated around **Aug 22 2026**, which introduces per-byte fee pricing; more fees mean more recycling, not more burning, but it changes the sink's arithmetic. Fifth, and largest, the Foundation has extended its funding of the block bonus by a year to **January 2028**; the published plan is that without that support the per-block bonus falls to **0.05 ALGO**, which would end Sell #1 almost entirely.

## Summary

The MrNasdog Pressure Framework reads ALGO at **+1.24% net** over the last 90 days and **+0.90%** over the next 90. The structural mechanism is unusual: a hard cap of **10,000,000,000** fully minted in 2019, no mint function and no burn, so every unit of measured inflation is already-created ALGO leaving Algorand Foundation custody — **18.7M** through the block-production bonus and **92.8M** through outright transfers. The key risk is that the larger tap is discretionary: **944.1M ALGO** sits in published Foundation wallets on no schedule, and this quarter's pace was set by a single organisation's decisions, not by protocol code. The ceiling is the comfort: ALGO can never exceed ten billion, the bonus decays by rule, and roughly **90%** of the supply is already in the market — the remaining question is timing, not size.

---

*MrNasdog Pressure Framework analysis of ALGO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 19 2026.*

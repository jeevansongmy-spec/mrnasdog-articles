---
title:         "STX Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "Supply growing, projected to keep growing: STX reads +0.98% over 90 days and +1.22% next, from miner rewards and Stacks Endowment mints, with no buyback or burn."
canonical_url: "https://mrnasdog.com/research/stx/inflation"
tags:                    ["crypto", "stx", "stacks", "bitcoin"]
published:     true
---

Originally published at [STX Inflation Analysis · September 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/stx/inflation).

# STX Inflation Analysis · September 2026 · Supply growing · projected to keep growing

Stacks supply is growing and is projected to grow faster. The Pressure Framework reads STX at **+0.98%** over the trailing 90 days and **+1.22%** over the next 90, against an inflation monitor reading of **+1.02%**. All of it is new STX from two protocol mints — the miner reward paid on every Bitcoin block and a second mint to the Stacks Endowment — and both stepped up at the Jul 30 2026 upgrade. Sell pressure is **18.25M STX**, buy pressure is **0**, and STX has no supply cap.

## The verdict, in one paragraph

Against a circulating base of **1,868.6M STX**, the framework books **18.25M STX** of sell pressure and **0** of buy pressure over the trailing 90 days — a net of **+0.98%** — and projects **22.85M STX**, or **+1.22%**, for the next 90 days. The inflation monitor reads **+1.02%** for the same window, a gap of **0.05 percentage points**, well inside the framework's 0.5-point tolerance, so the overview carries no warning. The forward number sits above the trailing one for a plain reason: the trailing window still holds five weeks of the old, lower rates, and the next window holds none. The label for STX is **an uncapped Bitcoin layer whose issuance rose at its last upgrade**.

## Sell pressure: where new STX comes from

Sell #1, protocol inflation, is **10.29M STX**. Stacks pays its block producer — the miner of each tenure — in newly minted STX, and the reward is counted per Bitcoin block: when a Bitcoin block starts no Stacks tenure, its reward rolls into the next one. Stacks cut that reward from **1,000** to **500 STX** per Bitcoin block in April 2026, then the PoX-5 upgrade, activated at Bitcoin block **960,230** on **Jul 30 2026**, put it back to **1,000 STX** and deleted the halving ladder that would have kept cutting it. The chain's own numbers agree: about **495** STX per Bitcoin block before the upgrade and about **991** after. Bitcoin produced **12,957** blocks in the window, one every ten minutes on average, so no interval correction applies. At the full rate the next 90 days carry about **12.84M STX**.

The second source is an extra row, Sell #5, Endowment emissions, at **7.96M STX**. A 2025 vote created the Stacks Endowment and a five-year mint that pays new STX into an Endowment contract at the start of every Stacks tenure: **475 STX** per tenure until **Jul 30 2026**, and **1,140 STX** per tenure since. The contract's receipts match that schedule to the tenure — **3,865** tenures at 475 before the step and **5,304** at 1,140 after. About two in three Bitcoin blocks start a tenure, which puts the next 90 days at about **10.01M STX**. Because the Endowment contract is already counted as circulating, each mint is new float the moment it lands, and it is counted then, once.

Sell #2, vesting unlocks, is **0**: the chain reports **100%** of STX unlocked at both ends of the window, so the original genesis lockups are finished. Sell #3, Foundation and unscheduled unlocks, is **0** — the Endowment moved large sums, covered below, but only between wallets that already count as circulating. Sell #4, long-term locked or bankruptcy, is **0**: no estate or trustee holds STX. Stacking does not add a sell row either, because stakers are paid in Bitcoin, never in new STX.

## Buy pressure: where new STX goes

Nowhere. Buy #1, programmatic buyback, is **0**: no protocol contract and no treasury programme buys STX on the market. Buy #2, protocol fee burn, is **0**, and that is by design — Stacks transaction fees go to the miner rather than into a burn. Both burn surfaces were read at both ends of the window: total STX supply only rose, and the unspendable burn address took in **0.34 STX** across 90 days. The July upgrade did end a burn, but it was the Bitcoin that miners used to send to a burn address; it never touched STX.

Buy #3, Foundation buy, is **0**. The Stacks Endowment is funded by new mint and spends outward; its second-quarter report says it sold Bitcoin rather than STX to cover costs. Buy #4, new long-term lock, is **0**. Stacked STX fell from **589.7M** at the window start to **441.5M** in the current cycle, because every old staking position unlocked at the upgrade and had to re-enter the new staking contract. Staked STX is counted as circulating in any case, so even a rise would remove nothing.

## Foundation and overhang

The overhang on STX is the Stacks Endowment, spread across four readable wallets holding **171.4M STX** in all. The largest single pot is the Endowment emission contract, at **61.7M STX** at the window end; about **45.8M** of that is the rest of a 2025 grant still releasing in monthly steps, and about **15.9M** is claimable today. The Endowment's main multisig holds **45.9M STX** and an operating wallet **2.7M STX**. The fourth is a multisig holding **61.0M STX**, which took over the entire balance of a wallet the operating wallet had funded, on **Aug 11 2026**. Inside the window the contract paid **58.5M STX** to the main multisig, and the main multisig sent **31.0M STX** onward. All four balances are read on chain at every rebuild.

None of this counts as new supply, and the reason is arithmetic, not a label: the circulating figure the framework divides by equals the chain's whole supply to within about **31,680 STX**, so every one of these wallets is already inside the float. What the overhang carries is sale risk rather than dilution — the Endowment has budget commitments priced in dollars, and a lower STX price means more STX to meet them. If any of these balances falls between refreshes, the outflow is traced at the next refresh, and it enters Sell #3 only if it leaves a balance that sits outside the counted float.

## How STX compares to other Bitcoin-linked and uncapped chains

STX began life on a Bitcoin-style path: a fixed reward that halves on a clock, trending toward a known supply. That path is gone. Stacks first moved its halvings to line up with Bitcoin's, then in July 2026 voted the reduction schedule out altogether, so STX now mints a flat **1,000 STX** per Bitcoin block with no scheduled cut. Bitcoin itself mints on every block too, but at a rate that halves every four years and reads a fraction of a percent per quarter. STX, reading **+1.22%** forward, is closer in shape to an uncapped proof-of-stake chain, where issuance is a policy setting that governance can raise.

What sets STX apart from most uncapped chains is where the mint goes. On a typical proof-of-stake chain, new coins go to stakers, many of whom hold them. On Stacks, stakers are paid in Bitcoin, so the new STX goes to miners — who spend Bitcoin to win it and often need to sell — and to an Endowment with a spending budget. Both of those recipients tend to sell rather than hold.

There is also no offset. Chains that pair issuance with a fee burn or a buyback can hold net supply near flat when usage rises. Stacks has neither: fees go to miners, and nothing on the protocol buys STX back. Gross issuance is the net figure.

## What to watch in the next 90 days

First, the miner reward itself: the July vote set **1,000 STX** per Bitcoin block as a starting rate, to be reviewed in a later staking upgrade, so any proposal to change it before **Dec 22 2026** moves this reading directly. Second, the Endowment mint stays at **1,140 STX** per tenure until Bitcoin block **1,012,860**, expected in mid-2027, where it steps up to 1,705 — outside this window. Third, the Endowment's monthly release continues through the window and adds about **4.17M STX** a month to its claimable pot; claims and sales from the Endowment wallets are the flows to trace. Fourth, the share of Bitcoin blocks that start a Stacks tenure, now about two in three, sets the size of the Endowment mint. Fifth, staking: the new Bitcoin staking system pays yield in Bitcoin, and new staking of STX would not change the supply reading.

## Summary

The MrNasdog Pressure Framework reads STX at **+0.98%** over the trailing 90 days and **+1.22%** projected forward: supply growing, projected to keep growing. The mechanism is two protocol mints — the Stacks miner reward, restored to **1,000 STX** per Bitcoin block on **Jul 30 2026**, and the Stacks Endowment mint of **1,140 STX** per tenure — with no fee burn and no buyback to offset them. The key risk is that both recipients, miners and the Endowment, are natural sellers, and wallets linked to the Endowment already hold **171.4M STX**. STX has no supply cap, and since July no scheduled reduction either.

MrNasdog Pressure Framework analysis of STX, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 23 2026.

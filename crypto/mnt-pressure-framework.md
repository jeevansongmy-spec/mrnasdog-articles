---
title:         "MNT Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "MNT supply is roughly steady: 0.00% net over 90 days and the same next. No mint, no vesting, no burn, and the 2.92B MNT Mantle Treasury did not move a coin."
canonical_url: "https://mrnasdog.com/research/mnt/inflation"
tags:          ["crypto", "mnt", "mantle", "layer-2"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/mnt/inflation](https://mrnasdog.com/research/mnt/inflation)*

# MNT Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

The MrNasdog Pressure Framework reads MNT, the gas and governance token of Mantle, at **0.00% net** over the trailing 90 days and **0.00%** over the next 90: **0 MNT** of new supply against **0 MNT** bought back or burned. MNT has no block rewards and no vesting left, and the Mantle Treasury — **2.92B MNT** held outside the circulating count — did not move a single coin this window. Total supply stays at **6.22B MNT**, with a mint switch that is set to zero today.

## The verdict, in one paragraph

Across Jul 1 2026 to Sep 29 2026, MNT sell pressure was **0 MNT** and buy pressure was **0 MNT**, so the framework net is **0.00%** of the **3.30B MNT** circulating supply, and the forward 90 days read the same **0.00%**. Our inflation monitor, which tracks the market's circulating count day by day, reads **+0.05%** over the same 90 days — a gap of **0.05 percentage points**, well inside the half-point line, so no warning chip ships. That small drift is day-to-day rounding in the market count, not a release: every treasury wallet held the exact same balance at both ends of the window. MNT is a quiet, treasury-held token: nothing new reaches the market unless Mantle governance decides to spend it.

## Sell pressure: where new MNT comes from

Protocol inflation is **0 MNT**. Mantle pays its sequencer and network costs out of fees and treasury budgets, not by printing MNT, and the MNT token contract on Ethereum read exactly **6,219,316,795 MNT** of total supply at the start and at the end of the window. The MNT contract does carry a mint function: its owner, a multisig, may create up to **2%** of supply a year, at most once every 365 days. Today that yearly limit is set to zero, so a mint call fails until the owner raises it first. We watch the limit at every rebuild.

Vesting unlocks are **0 MNT**. MNT replaced the older BIT token in 2023, and the unlock calendar ended that year; no team, investor or advisor tranche is waiting. The old BIT-to-MNT swap contract is switched off and holds no MNT, so no swapped coins can appear from it without a new treasury top-up.

Foundation and unscheduled unlocks are **0 MNT** this window. The Mantle Treasury is the only large holder outside the float, and not one of its wallets sent MNT during the 90 days. The two last releases were earlier: **15M MNT** moved from the treasury to the budget wallet on Mar 3 2026, and **24.35M MNT** moved to a treasury-run wallet on Apr 28 2026. Those two firings came close together and then stopped, and there is no published schedule for the next one, so the forward row stays at zero until a new release is seen. Long-term locks and bankruptcy are **0 MNT**: there is no estate, no trustee and no unwinding lock.

## Buy pressure: where new MNT goes

The programmatic buyback is **0 MNT**. Mantle has no contract or policy that buys MNT off the market. On Sep 18 2026 a holder opened a forum discussion asking for a share of Mantle's revenue to fund MNT buybacks and burns, and a treasury-burn idea from February was archived without a vote — neither is a decision.

The protocol fee burn is **0 MNT**. Gas on Mantle is paid in MNT, but the fees are collected into network vaults rather than destroyed; those vaults grew by about **46,000 MNT** over the window, and the coins stay in the float. Dead addresses on Ethereum and on Mantle picked up only about **1.6 MNT** in total, which rounds to nothing.

The foundation buy is **0 MNT**: the treasury's MNT balance was identical at both ends. The new long-term lock is **0 MNT** as well. Staked and reward-program MNT stays in the circulating count, and the **5.55M MNT** that moved into the bridge pool toward another chain is matched by the same amount issued on the far side, so it never leaves the float.

## Foundation and overhang

The Mantle Treasury is the overhang that matters. It holds **2.92B MNT** outside the circulating count — about **47%** of all MNT — with **2.90B MNT** in its main wallet on Ethereum, **10M MNT** in a second Ethereum wallet and about **7M MNT** across its wallets on Mantle. Spending it takes a governance budget or a separate vote; the current budget allows up to **200M MNT** a year, and its extension runs to about the end of September 2026.

Some treasury-run wallets are already counted as circulating, so their moves add nothing new: the two budget wallets hold **21.9M MNT** after spending **5.3M MNT** this window, and the wallet that received the April release still holds **24.38M MNT**. We read every one of these wallets on chain at each rebuild. If the treasury's balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How MNT compares to other Ethereum Layer-2 tokens

Most Ethereum Layer-2 tokens still carry a vesting calendar: team and early-investor coins open month by month, and that steady unlock is the main source of new supply on their pages. MNT has none left. Its supply risk sits in one place instead — a large treasury that releases coins only when governance decides — so MNT can read flat for months and then jump on a single budget draw, while a vesting-driven token drips out coins on a known date every month.

MNT also differs from Layer-1 coins that pay validators in new coins, such as ETH, and from tokens with a fee burn. Mantle pays for its network with fees and treasury budgets, so there is no issuance to offset — but there is no burn either. Gas fees are kept as network revenue rather than destroyed, so busier blocks do not shrink the MNT supply.

Against tokens with a hard cap, MNT sits in between. Its total of **6.22B MNT** is not fixed by code: the owner could raise the mint limit to **2%** a year. Today that limit is zero, so in practice the cap holds, but it is a setting, not a law of the protocol.

## What to watch in the next 90 days

First, the next Mantle budget vote: the current budget extension ends around Sep 30 2026, and a new cycle would set how many treasury MNT may flow to the budget wallets over the next year. Second, any transfer out of the **2.90B MNT** main treasury wallet — the last one before this window was on Apr 28 2026. Third, the revenue-based buyback discussion opened on Sep 18 2026; if it moves to a vote, MNT could gain its first buyer. Fourth, the mint limit on the MNT contract, which sits at zero today. Fifth, the wallet-based tokenized fund product that Bybit and Franklin Templeton said on Sep 28 2026 they plan to launch on Mantle, which could raise demand for MNT as gas without changing supply.

## Summary

The MrNasdog Pressure Framework reads MNT at **0.00%** net over the last 90 days and **0.00%** for the next 90, with the inflation monitor at **+0.05%**: Mixed flows · supply roughly steady. Mantle mints no MNT, has no vesting left and burns nothing, so supply moves only when the Mantle Treasury spends from its **2.92B MNT**. The key risk is a treasury draw or a new budget, which can arrive without a calendar. The ceiling is the **6.22B MNT** total supply, held there by a mint limit set to zero.

*MrNasdog Pressure Framework analysis of MNT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

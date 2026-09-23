---
title:         "MNT Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "MNT supply held flat over 90 days: no MNT minted, no burn, and the 2,917M MNT Mantle Treasury moved nothing. Read the full Pressure Framework ledger for Mantle."
canonical_url: "https://mrnasdog.com/research/mnt/inflation"
tags:          ["crypto", "mnt", "mantle", "ethereum"]
published:     true
---

Originally published at [MNT Inflation Analysis · September 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/mnt/inflation).

# MNT Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

MNT supply held flat. The Pressure Framework records **0** MNT of sell pressure and **0** MNT of buy pressure, a net of **0.00%** over the last 90 days and **0.00%** projected for the next 90, while the monitor reads **+0.01%**. Mantle minted no MNT, burned none, and the **2,917.0M MNT** Mantle Treasury did not send a single transaction, so the tradable float of **3,302.3M MNT** did not change. The constraint is the treasury itself: nearly half of all MNT sits in wallets with no release calendar.

## The verdict, in one paragraph

Against a circulating base of **3,302.3M MNT**, the framework books **0** MNT of sell pressure and **0** MNT of buy pressure over the trailing 90 days, a net of **0.00%**, and projects **0.00%** for the next 90 days because no MNT mint, vesting unlock, buyback or burn is scheduled. The inflation monitor reads **+0.01%** for the same window, a gap of **0.01 percentage points**, well inside the framework's 0.5-point tolerance, so the overview ships with no monitor-gap warning. The two readings agree because they measure the same boundary: Mantle defines circulating MNT as total supply minus the Mantle Treasury wallets, and both terms of that sum were identical at both ends of the window. The label for MNT this quarter is **a fixed-supply token with a large, idle treasury overhang**.

## Sell pressure: where new MNT comes from

It did not come from minting. Sell #1, protocol inflation, is **0**. The MNT token contract on Ethereum held a total supply of **6,219.3M MNT** at both ends of the window, unchanged to the last decimal, and that number lives in a storage field the contract can write, so the flat reading is a real measurement rather than a hard-coded constant. MNT is not mint-proof, though. The contract has a live mint function owned by a 6-of-14 multisig, with a yearly mint cap that can be set as high as **2%** of supply. Today that cap is **zero**, and a test mint from the owner fails with the contract's own "amount too large" error. Because a multisig decision could raise the cap, the row is watched rather than closed permanently.

Sell #2, vesting unlocks, is **0**. MNT was created in 2023 from the swap out of the older BIT token, and no team or investor vesting schedule is still running. Everything that is not circulating sits in the Mantle Treasury, which is governed by Mantle DAO votes rather than by a vesting calendar.

Sell #3, Foundation and unscheduled unlocks, is **0**, and this is the row that matters most for MNT. The Mantle Treasury holds **2,917.0M MNT** across 11 wallets on Ethereum and on Mantle, **2,900.0M MNT** of it in one Ethereum wallet. Every one of those wallets held the same balance at both ends of the window, and not one of them executed a single transaction in those 90 days. The last time treasury MNT reached the market was **Apr 28 2026**, when **24.4M MNT** moved out, 58 days before this window opened. Sell #4, long-term locked or bankruptcy, is **0**: there is no bankruptcy estate, trustee or court-ordered distribution tied to MNT.

One extra row, Sell #5, covers Mantle's budget wallets. They paid out about **6.2M MNT** in the window, **3.9M** on Ethereum and **2.3M** on Mantle. Mantle's own definition already counts budget wallets as circulating, so those coins were in the market before they moved, and the row stays at **0**.

## Buy pressure: where new MNT goes

Nowhere, this window. Buy #1, programmatic buyback, is **0**. Mantle runs no MNT buyback. A proposal to buy back MNT from network revenue was posted for discussion on **Sep 18 2026**, and an earlier plan to burn 3% to 8% of supply from the treasury, posted in February 2026, was archived without a vote. Neither has been approved.

Buy #2, protocol fee burn, is **0**. Gas on the Mantle network is paid in MNT, but the fees are collected into fee wallets on the network rather than destroyed; those wallets grew by about **45.6K MNT** over the window. The framework checked the burn both ways. The total MNT supply on Ethereum did not fall, and the unspendable addresses on both chains received only about **1.6 MNT** between them, far too little to register.

Buy #3, Foundation buy, is **0**: the Mantle Treasury bought no MNT, and its MNT balance did not change by a single coin. Buy #4, new long-term lock, is **0**. About **5.5M MNT** moved into a cross-chain bridge pool during the window as Mantle moved to a new bridge, but a matching amount is issued on the other side, so the market holds the same coins in a different place.

## Foundation and overhang

The overhang on MNT is one large pot. The Mantle Treasury holds **2,917.0M MNT**, close to half of the **6,219.3M MNT** total supply and almost as much as the entire circulating float. It has no release schedule; any spending needs a Mantle DAO vote or a budget approved by one. The last approved budget allowed up to **200M MNT** a year for July 2025 to June 2026, with a pro-rata extension of up to three months while the next budget is proposed. The treasury is read from the chain at every rebuild.

Two smaller items sit inside the float and are tracked for context: the budget wallets, which held about **9.2M MNT** on Ethereum and **12.8M MNT** on Mantle at the end of the window, and the wallet that received the **24.4M MNT** treasury release in April. If the Mantle Treasury balance falls between refreshes, that outflow enters Sell #3 at the next refresh.

## How MNT compares to other layer-2 tokens

MNT sits in the group of layer-2 tokens with a fixed supply and a large treasury, where the question is never how fast new coins are printed but when the treasury decides to spend. That is a different shape from tokens that still carry team and investor vesting, where a published unlock calendar pushes coins into the market month after month. MNT has no such calendar: its supply only reaches the market when the DAO spends, which makes quarters like this one flat, and makes a single treasury decision the whole story.

It also differs from chains that burn fees. On Ethereum, part of every transaction fee is destroyed, so busy periods can shrink supply. Mantle keeps its gas fees, so network use does not remove MNT, and the only way MNT supply can fall is a deliberate burn or buyback voted through governance. On the issuance side, MNT is stricter than proof-of-stake chains that pay stakers with new coins every block, but looser than a token with a renounced mint: the mint function is there, capped at zero, one multisig decision away from up to **2%** a year.

## What to watch in the next 90 days

First, the next Mantle budget: the extension of the July 2025 to June 2026 budget runs out around **Sep 30 2026**, and a new budget vote would set how much treasury MNT can be spent. Second, the revenue-based buyback discussion opened on **Sep 18 2026**; if it becomes an approved proposal with burns, Buy #1 or Buy #2 turns positive for MNT. Third, the Mantle Treasury wallets themselves, read at every rebuild: any drop from **2,917.0M MNT** is sell pressure. Fourth, the mint cap on the MNT contract, now zero; any change to it would reopen Sell #1.

## Summary

The MrNasdog Pressure Framework reads MNT at **0.00%** over the trailing 90 days and **0.00%** projected forward: mixed flows, supply roughly steady. Mantle minted no MNT, burned none, and its treasury did not move, so the circulating float stayed at **3,302.3M MNT**. The key risk is the **2,917.0M MNT** Mantle Treasury, which has no release schedule and can be spent by DAO vote. Total supply is fixed at **6,219.3M MNT** today, with a mint cap set to zero that a 6-of-14 multisig could raise to **2%** a year.

MrNasdog Pressure Framework analysis of MNT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 23 2026.

---
title:         "XDC Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description:   "XDC supply is roughly steady: 18.87M XDC of masternode rewards and no burn give +0.09% net over 90 days, the same next. No cap; 18.12B XDC held locked."
canonical_url: "https://mrnasdog.com/research/xdc/inflation"
tags:          ["crypto", "xdc", "xdcnetwork", "layer1"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/xdc/inflation](https://mrnasdog.com/research/xdc/inflation)*

# XDC Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

The MrNasdog Pressure Framework reads XDC at **+0.09% net** over the last 90 days and **+0.09%** over the next 90. The only new XDC is the masternode block reward: **18.87M XDC** minted in 90 days, against **0 XDC** burned or bought back, on a circulating supply of **19.95B XDC**. The monitor reads **+0.00%**, a gap of **0.09 percentage points**, inside our 0.5-point tolerance. XDC Network has no supply cap and no fee burn today, so supply keeps growing slowly for as long as the reward stays at 5,000 XDC an epoch.

## The verdict, in one paragraph

Over the 90 days from Jul 9 2026 to Oct 7 2026, XDC Network minted **18.87M XDC** and destroyed none, so the net change is **+0.09%** of the **19.95B XDC** that counts as circulating. The forward reading for Oct 8 2026 to Jan 6 2027 is the same **+0.09%**, because the reward rule did not change and no dated unlock falls inside the window. The monitor reads **+0.00%**: its supply figure has sat at 19.95B XDC since Apr 28 2026. The gap is **−0.09 percentage points**, well under the 0.5-point line, so no warning chip is shown. In one label: XDC is a **slow-mint masternode chain with no burn**, where the real supply story is the large team reserve, not the per-epoch reward.

## Sell pressure: where new XDC comes from

Protocol inflation is the one live source of new XDC. XDC Network runs XDPoS, a proof-of-stake design with 108 masternodes. Every epoch of 900 rounds, the network code mints **5,000 XDC** and shares it among the masternodes that signed blocks: 90% goes to the node owners and 10% to the XDC Foundation reward wallet. We read that wallet on-chain at many epoch boundaries and it took exactly **500 XDC** each time, which matches the 10% slice. Blocks came every **2.30 seconds** on average, slower than the 2-second target, so only **3,774 epochs** passed in the 90 days. That gives **18.87M XDC** of new supply, about 210,000 XDC a day. Because the reward is paid per epoch and not per second, a slower chain mints less; at the 2-second target the same 90 days would have minted about 21.6M XDC.

Vesting unlocks are zero in both windows. At launch the team share was 15B XDC, unlocking about 3% a year, and the ecosystem share was 10B XDC, released at no more than 2.5% a year. These releases come as one yearly step: the last one landed on Feb 5 2026 at about **841M XDC**, and the next is due on Feb 5 2027, after the forward window ends. The founders' wallet, which received 14.95B XDC in December 2020, still holds **13,446.0M XDC** and sent nothing in the window.

Foundation and unscheduled unlocks are zero, even though one project wallet was busy. A project payout wallet sent **400.0M XDC** in eight transfers of 50M each between Jul 9 and Sep 23 2026, into an operations wallet that pays partners and the market. Those coins were already counted as unlocked at earlier yearly steps, so moving them adds nothing new to the circulating count. Long-term locks and bankruptcy estates are also zero: no trustee or court is paying XDC out.

## Buy pressure: where new XDC goes

Nothing removes XDC from the market today. There is no programmatic buyback: no contract or treasury buys XDC back, and the foundation's 10% of each reward is spent again. There is no protocol fee burn either. XDC Network turned on an EIP-1559 style base fee on Jan 28 2026, but the live node code pays the whole fee, base fee included, to the masternode that made the block. A fee burn has been proposed for a later upgrade, with the share to be set by the XDC DAO, but it is not in the code that runs the main network. The two burn addresses moved by only 22 XDC in 90 days, which is stray transfers, not a mechanism.

There was no foundation buy, and the new long-term lock row is zero too. Masternodes lock at least 10M XDC each, and the staking contract grew from **2,730.9M** to **3,701.1M XDC** in the window, up **970.2M XDC**, as new institutional validators joined. Staked XDC still counts as circulating, so a bigger stake takes nothing out of the float; it only raises the number of nodes sharing the same 5,000 XDC reward.

## Foundation and overhang

XDC's overhang is large. About **18.12B XDC**, nearly half of the **38.07B** total, is counted as locked, and three wallets funded at launch hold almost all of it: the founders' wallet with **13,446.0M XDC** (last payout Dec 15 2025), a reserve wallet with **3,609.2M XDC** (untouched since March 2024) and a second reserve with **1,225.8M XDC** (untouched since September 2022). Together they hold 18,281.0M XDC, within 1% of the locked count. Next to them sits the project payout wallet: 2,135.6M XDC a year ago, **675.6M XDC** at the end of the window and 635.6M after two more 20M transfers on Oct 7 2026. Its coins are already counted as circulating, so its sales show up as selling, not as new supply. We read these wallets on-chain at every rebuild. If any of the three locked reserves falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How XDC compares to other enterprise Layer 1s

Among enterprise and payments chains, XDC sits between two models. XRP mints nothing at all; its supply pressure comes from a company releasing coins it already holds, so the XRP ledger is all about custody, not issuance. Hedera's HBAR also has a fixed supply and a treasury that releases coins over time. XDC has both parts: a fixed pre-mined pool of 37.5B XDC held largely by the team, plus a small open-ended mint for masternodes with no cap. Its mint, about 0.38% a year of the circulating supply, is far smaller than the yearly team steps.

Compared with Ethereum, the masternode mint looks similar in shape but differs in one key way: Ethereum burns part of every fee, while XDC Network burns nothing, so all of XDC's issuance stays in the market. Compared with uncapped proof-of-stake chains such as Solana, whose reward is a yearly percentage of supply, XDC's reward is flat in XDC terms (5,000 per epoch), so its inflation rate slowly falls as supply grows, and it falls further when blocks run slow.

## What to watch in the next 90 days

First, the main-network date for the tiered reward upgrade. It pays core validators, protector nodes and observer nodes separately and is already live on the test network; the August 2026 plan pointed to an October launch, but as of Oct 8 2026 the main-network setting is still empty. If it goes live, the mint per epoch could rise well above 5,000 XDC, and the forward number would change.

Second, any XDC DAO vote that switches on a fee burn, which would open the buy side for the first time. Third, the project payout wallet, which holds 635.6M XDC after Oct 7 2026 and has been sending 50M at a time. Fourth, the staking contract, which keeps growing as institutions such as Amber Premium join as validators. Fifth, the next yearly unlock step on Feb 5 2027, just after this window.

## Summary

The MrNasdog Pressure Framework reads XDC at **+0.09%** over the last 90 days and the same over the next 90: **18.87M XDC** of masternode rewards against **0 XDC** burned or bought back. XDC Network has no supply cap and no fee burn, but its 5,000 XDC per-epoch reward is small next to the 19.95B XDC in circulation. The key risk is not the per-epoch mint but the 18.12B XDC held in team-funded reserves and the yearly unlock steps that feed them into the count, plus a reward upgrade that could raise the mint once it reaches the main network.

---

*MrNasdog Pressure Framework analysis of XDC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 8 2026.*

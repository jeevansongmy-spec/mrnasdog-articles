---
title:         "XDC Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "XDC supply is roughly steady: masternode rewards mint 18.97M XDC in 90 days, nothing is burned, net +0.10%. 18.12B XDC sits in reserve; next release Feb 5 2027."
canonical_url: "https://mrnasdog.com/research/xdc/inflation"
tags:                    ["crypto", "xdc", "xdcnetwork", "layer1"]
published:     true
---

Originally published at [XDC Inflation Analysis · September 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/xdc/inflation).

# XDC Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

XDC, the native coin of XDC Network, is only mildly inflationary: masternode rewards created **18.97M XDC** over the last 90 days, nothing was burned or bought back, and circulating supply of **19.95B XDC** grew about **+0.10%**. The same small rate is expected for the next 90 days. The bigger question for XDC supply is not the mint but the **18.12B XDC** held outside the circulating count, which releases on a yearly date — and the next release is not due until **Feb 5 2027**.

## The verdict, in one paragraph

For the 90-day window from **Jul 1 2026** to **Sep 29 2026**, the Pressure Framework reads **XDC at +0.10% net**: the sell side added **18.97M XDC** of new masternode rewards and the buy side removed **0 XDC**, against **19.95B XDC** in circulation. The next 90 days project the same **+0.10%**. The independent inflation monitor reads **0.00%** for the same window, a gap of **0.10 percentage points** — well inside the half-point line, so no warning chip is shown. The monitor's circulating figure only moves when the project reports a new release, and none was reported in the window. XDC Network is a **quiet chain with a slow, steady mint**.

## Sell pressure: where new XDC comes from

Protocol inflation is the only live source. XDC Network runs on delegated proof of stake with 108 masternodes, and the protocol pays them **5,000 newly created XDC** at the end of every epoch of 900 rounds. Rounds ran a little slower than the two-second target this window, so an epoch took about 34 minutes. There were **3,794 epochs** in the 90 days, which gives **18.97M XDC** of new supply, or about 211,000 XDC a day. Of each 5,000 XDC reward, 4,500 goes to the masternode owners and 500 goes to a foundation wallet. We read the reward on the chain at eleven epochs spread across the window, and every one paid exactly 5,000 XDC. At this pace XDC Network mints roughly **0.38% of circulating supply a year**.

Vesting unlocks add **0** this window. XDC Network releases part of its reserve once a year: **841.18M XDC** was released on **Feb 5 2026**, and the next release is due on **Feb 5 2027**. Neither date falls in the last 90 days or the next 90 days, so the vesting row stays at zero for both.

Foundation and unscheduled unlocks also add **0**. The team reserve wallets that sit outside the circulating count did not move at all in the window. An ecosystem wallet did pay out **470M XDC** in nine transfers of 50M to 70M XDC between Jul 7 and Sep 23 2026, but that wallet is already counted as circulating, so the payouts move coins inside the market rather than adding new ones. Long-term locks and bankruptcy estates add **0**: XDC Network has no estate, no trustee and no unwinding lock.

## Buy pressure: where new XDC goes

Nothing takes XDC off the market today. There is **no programmatic buyback**: no contract, treasury or announced programme buys XDC. There is also **no protocol fee burn** on the main network. XDC Network added a base fee in January 2026, but the whole fee — the base fee and the tip — is paid to the masternode owner who made the block, so the base fee is not destroyed the way it is on Ethereum. We checked this in the node code and on a live block, where the owner received the full fee. The burn addresses show only small voluntary sends. A planned reward and burn upgrade would burn part of the fee, but it has no date on the main network yet.

The foundation did not buy XDC either, so the foundation-buy row is **0**. The new long-term lock row is also **0**, even though staking grew fast: the masternode staking contract rose from **2.70B XDC to 3.70B XDC** in 90 days as staking funds and new validators joined. Staked XDC is still counted as circulating and can be withdrawn after a waiting period, so a bigger stake does not shrink the float.

## Foundation and overhang

The overhang is large. About **18.12B XDC** — nearly half of the **38.07B** total — sits outside the circulating count, mostly in a few team reserve wallets. The largest holds **13.45B XDC**; others hold about 3.61B, 1.23B, two of 574.9M each, and several between 115M and 411M. These wallets did not move this window. The largest one last released coins on **Dec 15 2025** (175M XDC), after smaller releases through 2025, so its releases are irregular rather than scheduled. The ecosystem wallet that paid out 470M XDC this window still holds **675.6M XDC**, and the foundation wallet that takes 10% of every reward holds about 194K XDC. We read these balances on the chain at every rebuild. If a reserve wallet's balance falls between checks, the coins that leave it will be added to the foundation and unscheduled unlock row at the next check.

## How XDC compares to other proof-of-stake Layer 1s

Like Ethereum, XDC Network has no supply cap and pays its block producers in newly created coins. The difference is the other side of the ledger: Ethereum burns the base fee of every transaction, so part of its issuance is cancelled out, while XDC Network pays the whole fee to masternode owners and burns nothing. XDC's mint is also a fixed amount per epoch rather than a rate that grows with the stake, so more staking does not mean more new XDC — the 1.0B XDC of new stake this window shared the same 5,000 XDC per epoch.

In its reserve structure XDC looks more like XRP than like Ethereum. Both launched with the whole supply created at the start and a large share held back by the team; XRP releases from escrow every month, while XDC releases on a yearly date. That makes the circulating count of XDC move in steps, not smoothly, and it means a mint of about 211,000 XDC a day matters far less to the float than one yearly release of hundreds of millions.

Against exchange-chain tokens that run regular burns, XDC has no buyer built into the protocol at all. Today its supply story rests on two things: a small, predictable mint of about **0.38% a year**, and the timing of reserve releases.

## What to watch in the next 90 days

First, the reward and burn upgrade. It is running on the XDC test network — a new test release came out on **Sep 28 2026** — and the project has said it aims for the main network in October 2026, but no main-network block is set yet. If it goes live, both the reward per epoch and a new fee burn would change this ledger.

Second, the team reserve wallets: any outflow from them would be new supply in the foundation row. Third, the ecosystem wallet, which has paid out 50M XDC every one to three weeks and holds 675.6M XDC. Fourth, the next yearly release on **Feb 5 2027**, just outside this window, which the next rebuild will bring into view.

## Summary

XDC Network is inflationary only by a little: masternode rewards created **18.97M XDC** in 90 days against **0 XDC** burned or bought back, a net **+0.10%** on **19.95B XDC** circulating, with the same expected next. There is no supply cap and no fee burn today, since the whole fee goes to masternode owners. The main risk sits in the **18.12B XDC** held outside the circulating count, which enters the market through yearly and irregular releases; the next scheduled one is **Feb 5 2027**. A reward and burn upgrade planned for the main network could change both sides of the ledger once it has a date.

*MrNasdog Pressure Framework analysis of XDC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

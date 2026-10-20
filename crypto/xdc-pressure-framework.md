---
title:         "XDC Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description:   "XDC supply is roughly steady: 18.59M XDC of masternode rewards in 90 days, no fee burn, no buyback, +0.09% net and the same next. 18.12B XDC still locked."
canonical_url: "https://mrnasdog.com/research/xdc/inflation"
tags:          ["crypto", "xdc", "xdcnetwork", "layer1"]
published:     true
---
*Originally published at [https://mrnasdog.com/research/xdc/inflation](https://mrnasdog.com/research/xdc/inflation)*

<!-- main-page -->
➜ Start with the XDC Network coin page for the short answer (should you buy XDC?) and its price drivers: [mrnasdog.com/research/xdc](https://mrnasdog.com/research/xdc)

# XDC Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

XDC is close to flat: the MrNasDog Pressure Framework finds **18.59M XDC** of new supply in the last 90 days and **0** taken out, a net change of **+0.09%** on a circulating supply of **19.95B XDC**. All of the new XDC is the fixed masternode reward of **5,000 XDC** per epoch; XDC Network burns no fees and runs no buyback. The monitor reads **0.00%** for the same window, so the two readings agree.

## The verdict, in one paragraph

Over the 90 days from Jul 19 2026 to Oct 17 2026, XDC supply grew by **+0.09%**, and the next 90 days project the same **+0.09%**. The monitor, which reads the classified circulating supply day by day, shows **0.00%** (a tiny fall of 0.0003%). The gap is **0.09 percentage points**, well inside the 0.5-point line, so no warning chip is needed. The small difference has a simple cause: the classified circulating figure only moves on unlock dates, so it does not pick up the epoch rewards between them. XDC is a quiet chain: a slow, steady mint with no burn to offset it.

## Sell pressure: where new XDC comes from

Protocol inflation is the only new XDC. XDC Network runs XDPoS, a delegated proof-of-stake design with 108 masternodes, and at the end of every epoch of 900 consensus rounds the protocol mints exactly **5,000 XDC**. Of that, 4,500 XDC goes to the masternode owners and the people who vote their stake behind them, split by how many blocks each node signed, and 500 XDC goes to the foundation reward wallet. We counted every epoch in the window two ways, by listing each epoch-switch block and by dividing the consensus rounds by 900, and both gave **3,718 epochs**. Every reward record we read paid out exactly 5,000 XDC, so the mint came to **18.59M XDC**, about 206,600 XDC a day.

The reward is paid per epoch, not per day, so a slower chain mints less. Rounds ran a little slower in October (about 37 epochs a day in the last week against about 41 on average), but nothing in the code or the release notes changed, so the next 90 days keep the trailing figure of **18.59M XDC**. The reward does not halve on mainnet, and the new reward system with protector and observer nodes, called Reward 2.0 in XDC 3.0, is still only on the Apothem test network with no mainnet block set.

Vesting unlocks add **0**. XDC team and ecosystem coins unlock in one step a year; the last step, about 841M XDC, came on Feb 5 2026. Unlock trackers place the next step in 2027 (one says Feb 5 2027, another May 14 2027), outside both windows, and the largest team reserve held the same 13.45B XDC at both ends. Foundation and unscheduled unlocks also add **0**: three locked reserves did not move, and the project wallet that did pay out is already counted as circulating (more on that below). There is no bankruptcy estate or court-run distribution holding XDC, so the long-term locked row is **0** too.

## Buy pressure: where new XDC goes

Nothing takes XDC out of the market. There is no programmatic buyback: XDC Network does not route fees to a buyer, so that row is **0**. There is also no protocol fee burn. XDC Network added an EIP-1559 style base fee in January 2026, but unlike Ethereum it does not destroy it: the whole fee, base fee included, is paid to the owner of the masternode that made the block. A fee-burn share was proposed for a later upgrade, but it has no date. Only about 22 XDC landed in the zero address this window, which rounds to nothing.

No foundation buy showed up: the project wallets only paid coins out, so the foundation buy row is **0**. New long-term locks book **0** as well, even though staking grew. Each XDC masternode locks 10M XDC, and the staking contract rose from **3.03B** to **3.69B XDC** as new institutional validators joined. Staked XDC still counts as circulating, so a bigger stake moves coins between holders without taking any out of the float.

## Foundation and overhang

XDC has a large team-controlled overhang: about half of all XDC is not counted as circulating. Of the 38.07B XDC that exist, **18.12B XDC** sit outside the circulating count, and three reserves that have not moved in a year cover all of it: **13.45B XDC** in the largest team reserve, 3.61B XDC in a second reserve, and 1.23B XDC in a third. Their balances were the same on Jul 19 2026 and on Oct 17 2026, and we read them on-chain at every rebuild.

The wallet that does move is a project payout wallet. It sent **340M XDC** in 17 transfers to a spending wallet during the window, and its balance fell from 975.65M to **635.65M XDC**; a year earlier it held about 2.04B XDC. The spending wallet passes the coins on to partners, node operators and other wallets. Because the three still reserves already fill the whole non-circulating bucket, this payout wallet must be inside the circulating count, so its payouts move coins between holders rather than adding new supply. The foundation reward wallet that receives 500 XDC each epoch is swept out regularly and holds only about 0.3M XDC.

We read each of these balances on-chain every rebuild. If a reserve's balance falls between refreshes, the outflow enters the Foundation and unscheduled unlocks row at the next refresh. If the payout wallet is ever moved outside the circulating count, its payouts would start to count as new supply.

## How XDC compares to other delegated proof-of-stake Layer 1s

Most delegated proof-of-stake chains pay validators with a percentage inflation rate, so the mint grows as the supply grows. XDC pays a fixed 5,000 XDC per epoch instead, which makes the mint a flat number of coins and a slowly shrinking share of supply. That puts XDC on the gentle end of the uncapped Layer 1 group: about 0.09% in 90 days, or about 0.38% a year at the current pace.

The bigger difference is on the buy side. Ethereum and Tron destroy part of every fee, and BNB adds a scheduled burn on top, so heavy use pulls supply down. XDC destroys nothing, so busier blocks pay the masternodes more but never shrink supply. For XDC, demand has to come from buyers, not from the protocol.

XDC also sits with the pre-mined chains whose real supply question is the treasury, like XRP with its escrow and Hedera with its treasury releases. On those chains the yearly or monthly releases from team-held reserves matter more than the protocol mint, and XDC is the same: the yearly unlock step and the payout wallet are the lines to watch, while the epoch mint is small and fixed.

## What to watch in the next 90 days

**The mainnet date for XDC 3.0 rewards.** Reward 2.0, with paid protector and observer nodes, went live on the Apothem test network, and v3.0.0-testnet-1 shipped on Oct 16 2026. If a mainnet block is set, the per-epoch mint could change; until then it stays at 5,000 XDC.

**Any fee-burn decision.** A burn share of fees has been proposed but never dated. A live burn would open the first buy-side row XDC has ever had.

**The three locked reserves.** They hold 18.28B XDC between them and did not move this window. Any outflow from them would be new supply, ahead of the next yearly unlock step in 2027.

**The payout wallet and the staking contract.** The payout wallet still holds 635.65M XDC and has sent coins out every few weeks; staking is growing as banks and payment firms join as validators. Both sit inside the circulating count today, so neither changes the number unless that count is redrawn.

## Summary

XDC supply grew **+0.09%** in the last 90 days and is projected to grow about the same in the next 90, so the MrNasDog Pressure Framework reads it as mixed flows with supply roughly steady. The only new supply is the fixed masternode reward of **5,000 XDC** per epoch, **18.59M XDC** in this window, and nothing is burned or bought back. The key risk is the overhang: **18.12B XDC** is not yet circulating and reaches the market through yearly unlock steps and project wallets. XDC has no supply cap, but at the current pace the mint adds well under 1% a year.

---

*MrNasDog Pressure Framework analysis of XDC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 17 2026.*

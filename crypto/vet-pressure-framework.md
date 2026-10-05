---
title:         "VET Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description:   "VET supply is flat: 0 VET minted and 0 burned in 90 days, 0.00% net and 0.00% next. VeChain pays rewards and burns fees in VTHO; 727.58M VET stay frozen."
canonical_url: "https://mrnasdog.com/research/vet/inflation"
tags:          ["crypto", "vet", "vechain", "tokenomics"]
published:     true
---

Originally published at [VET Inflation Analysis · October 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/vet/inflation).

# VET Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

VET, the main coin of the VeChain network, did not change in supply over the last 90 days: **0 VET** was created, **0 VET** was destroyed, and net inflation was **0.00%** on a float of **85.99B VET**. The reason is built into VeChainThor itself: every VET was made in the first block in 2018, and the network pays its validators and stakers in a second token, VTHO, instead of new VET. The supply ceiling is the genesis figure of **86.71B VET**, of which **727.58M** are frozen for good after a 2019 theft.

## The verdict, in one paragraph

From Jul 7 to Oct 5 2026 the VeChain ledger books **0.00%** net change in VET supply, and the next 90 days project the same **0.00%**. Our inflation monitor, which tracks the market-wide supply figure day by day, read **−0.01%** for its latest 90-day window — a gap of **0.01 percentage points**, well inside our 0.5-point tolerance, so no warning chip is shown. Both readings say the same thing: VET is a **fixed-supply coin with zero issuance**, and the only thing that moves is who holds it.

## Sell pressure: where new VET comes from

Protocol inflation is **0 VET**. We read the VeChainThor node code this week and listed every place that can change a VET balance: the genesis block, ordinary transfers, and the hand-over when a contract closes. Each transfer takes VET from one account and gives the same amount to another, so the total never grows. Since the Hayabusa upgrade moved VeChain to delegated proof of stake in December 2025, block rewards go out as VTHO. The Interstellar hard fork on Sep 16 2026 (VIP-255) fell inside this window, and it changed only the smart-contract engine.

Vesting unlocks are **0 VET**. VeChain's 2017 token sale, team and foundation shares were handed out years ago, no unlock tracker lists a VET schedule, and circulating supply equals total supply — there is no locked pile waiting for a cliff date.

Foundation and unscheduled unlocks are **0 VET**. The VeChain Foundation's coins already count as circulating, so a Foundation sale would move existing VET from one wallet to another rather than add supply. The long-term locked row is also **0 VET**: the **727.58M VET** taken in the 2019 theft sit in 469 accounts that the network's consensus rules refuse to process, and we read all 469 at both ends of the window without finding a single coin moved.

## Buy pressure: where new VET goes

The programmatic buyback is **0 VET**. VeChain has no contract that buys VET back, and the Foundation's old 2019 buyback wallet held nothing at either end of the window.

The protocol fee burn is **0 VET**. Every transaction fee on VeChain is paid in VTHO, and that VTHO is destroyed — so the burn shrinks the gas token, not VET. The zero address held **249,020 VET** and the dead address **2,014 VET** on both Jul 7 and Oct 5 2026, which confirms nothing was sent away to be destroyed.

Foundation buying is **0 VET**; no report or on-chain flow shows a treasury purchase this window. New long-term locks are **0 VET** as well, even though staking kept growing: the staking contract ended the window at **14.85B VET**, up **427.24M VET**. Staked VET can be withdrawn and still counts as circulating, so a bigger stake removes nothing from the float.

## Foundation and overhang

The VeChain Foundation is the only team-controlled holder we track. It does not publish its wallets, and its latest financial report, for the quarter to the end of June 2025, valued the whole treasury — stablecoins, BTC, ETH and VET together — at **$167.2M** without splitting out the VET share. We check that disclosure by hand every two weeks. Because these coins are already part of the 85.99B float, a sale would change who holds VET, not how much VET exists.

The second overhang is the frozen theft pile of **727.58M VET**, which we read on-chain every day. It is the only VET outside the float, and only a new hard fork could release it. We also note one large unnamed wallet that grew from **114.82M** to **3.36B VET** during the window; it is inside the float, so it cannot change a row. If any tracked overhang's balance falls between our checks, that outflow enters the Foundation and unscheduled unlocks row at the next check.

## How VET compares to other fixed-supply Layer 1 chains

Most proof-of-stake Layer 1 chains pay validators by printing their main coin, so their supply rises every year and the reward is a cost borne by holders who do not stake. VeChain splits the job across two tokens: VET is the fixed asset people hold and stake, and VTHO is the reward and the gas. That design keeps VET inflation at zero while the network still pays for security — the dilution lands on VTHO, whose new issuance and fee burn are a separate story.

Against halving-model chains such as Bitcoin, which still add new coins on a falling schedule until a hard cap is reached, VET has already reached its cap: nothing is left to mine or unlock. Against chains with an EIP-1559-style burn in their main coin, VET gives up the chance to shrink — busy blocks destroy VTHO, never VET. So VET's supply can neither grow nor fall through normal use; only a hard fork could change that.

## What to watch in the next 90 days

First, any new VeChain Improvement Proposal on the VeVote portal; VIP-255 passed on Aug 18 2026 and went live on Sep 16 2026, and no follow-up proposal touching VET supply was open on Oct 5 2026.

Second, the VeChain Foundation's next financial report, the first since the one for the quarter to Jun 30 2025, for the size of its VET holdings and any sales.

Third, the 469 frozen theft accounts holding **727.58M VET**: any proposal to unfreeze them would add new circulating VET.

Fourth, the staking contract at **14.85B VET**. A rush of withdrawals would not change supply, but it would show holders preparing to sell coins that already exist.

## Summary

VeChain's VET has a fixed supply: all 86.71B coins were created in 2018, **85.99B** circulate, and the last 90 days added and removed **0 VET** for a net change of **0.00%**, with the same projected for the next 90 days. Rewards and fees run on the VTHO token, so VET never inflates and never burns. The main risk is not new supply but existing holders — chiefly the VeChain Foundation and large unnamed wallets — choosing to sell. The ceiling is hard-coded: only a hard fork could create VET or release the 727.58M frozen coins.

*MrNasdog Pressure Framework analysis of VET, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 5 2026.*

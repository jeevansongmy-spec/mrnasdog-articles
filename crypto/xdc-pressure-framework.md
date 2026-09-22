---
title:         "XDC Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "XDC reads +0.09% over 90 days: mixed flows, supply roughly steady. Masternode rewards mint 18.82M XDC, nothing is burned, and 470M of payouts were already counted."
canonical_url: "https://mrnasdog.com/research/xdc/inflation"
tags:                    ["crypto", "xdc", "xdcnetwork", "layer1"]
published:     true
---

Originally published at [XDC Inflation Analysis · September 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/xdc/inflation).

# XDC Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

XDC supply is roughly steady: the Pressure Framework reads XDC at **+0.09%** over the last 90 days and **+0.09%** projected for the next 90, against a monitor reading of **+0.18%**. The only new supply is the XDC Network masternode reward, which minted **18.82M XDC**; buy pressure is **0**, because no fee is burned on chain today. XDC has no supply cap, so the reward mint never ends, but at this pace it adds well under half a percent a year.

## The verdict, in one paragraph

Against a circulating base of **19,946.7M XDC**, the framework books **18.82M XDC** of sell pressure and **0** of buy pressure over the trailing 90 days, a net of **+0.09%**, and projects the same **+0.09%** for the next 90 days. The inflation monitor reads **+0.18%** for the same window, a gap of **0.09 percentage points**, which is inside the framework's tolerance, so the overview carries no monitor warning. Two very large flows happened on XDC Network in this window, **470M XDC** paid out of a Foundation wallet and **1,020.2M XDC** newly staked, and neither changes the reading, because both moved coins the project already counts as circulating. The label for XDC is **a slow, uncapped reward mint with no working burn**.

## Sell pressure: where new XDC comes from

Protocol inflation is **18.82M XDC**. XDC Network runs the XDPoS consensus, and at the end of every epoch of 900 rounds the chain credits **5,000 XDC** that did not exist before: **4,500 XDC** split across masternode owners and **500 XDC** to a Foundation reward wallet. We added up the owner credits at an epoch at the start of the window and another at the end, and both summed to exactly 4,500, with no reserve wallet paying them. The chain completed **3,764 epochs** in the 90 days, about 2.3 seconds per round, so the mint was 18.82M XDC. The reward is paid per epoch, so the forecast uses the same epoch count and lands at 18.82M again.

Vesting unlocks are **0**. XDC Network describes a 3% a year release for its founders and team and a capped release for ecosystem development, but no dated unlock landed in this window; the next calendar entry, an Ecosystem Development unlock, is on **Feb 5 2027**, after the forecast window. Foundation and unscheduled unlocks are also **0**: the locked team wallets held **21,308.9M XDC** at both ends of the window, and the largest of them last released coins on **Dec 15 2025**. Long-term locked or bankruptcy releases are **0**, since XDC has no bankruptcy estate or trustee.

## Buy pressure: where new XDC goes

Programmatic buyback is **0**: XDC Network has no programme that buys XDC on the market. Protocol fee burn is also **0**, and this is the row most worth explaining. The January 2026 Cancun upgrade brought an EIP-1559 fee market to XDC Network, and its notes describe the base fee as burned. On chain, it is not. In every block we tested, the masternode owner received the entire fee, base fee included, down to the last fraction of a coin. The randomness transactions that validators send carry a zero gas price, so they burn nothing either. The burn addresses held **887,332.6 XDC** at both ends of the window, and new supply matched the reward count exactly. The burn exists in the documents, not yet in the chain.

Foundation buy is **0**; Foundation wallets only paid coins out. New long-term lock is **0**, even though staking grew fast: the staking contract rose from **2,680.9M** to **3,701.1M XDC**as new operators joined, from institutional custody products to exchange staking. Staked XDC stays in the project's own circulating count, and a node can withdraw its stake about a month after it resigns, so this growth moves coins within the float rather than out of it.

## Foundation and overhang

The overhang on XDC comes in two parts. The first is the locked team bucket: **21,308.9M XDC** across a set of wallets that never trade, led by one wallet of **13,446.0M XDC**. That wallet has released coins in irregular blocks, 250M in May 2025, 100M in August 2025 and 175M in December 2025, with no public date for the next one. The project counts only these wallets as outside the circulating float, and they are read from the chain at every rebuild.

The second part is the Foundation ecosystem wallet, which is inside the circulating count but is still the most active seller-side pot on the chain. It fell from **1,195.6M** to **725.6M XDC** in this window, sending **470M XDC** in blocks of 50M to 70M through two payout wallets to node operators, partners and the node reward programme. At that pace the wallet empties in about five months. If a locked team wallet falls between refreshes, the outflow enters the Foundation row at the next refresh; the ecosystem wallet is watched for any change in how the project counts it.

## How XDC compares to other uncapped proof-of-stake chains

XDC sits in the class of proof-of-stake chains with no hard cap that pay validators with new coins. Most chains in that class issue far more: a typical staking chain mints several percent a year so that stakers keep up with dilution. XDC Network mints a flat 5,000 XDC per epoch no matter how much is staked, which works out to well under half a percent of the circulating float a year. Next to a halving chain like Bitcoin, XDC has no schedule that shrinks the reward over time, but its current rate is already lower than Bitcoin's.

The difference from exchange-chain tokens is the burn. Chains that burn a share of every fee can turn net negative when usage is high. XDC Network set a record of 27.7M transactions in August 2026, yet the fee burn produced nothing, because the fee goes to the node operator in full and the fee per transaction is a fraction of a cent. Even a working burn would need a large jump in usage to offset 18.82M XDC per quarter.

The third comparison is float versus total. On XDC the tradable float can move far more than the mint: the Foundation paid out 470M XDC and operators staked 1,020.2M in one quarter. Those flows matter for market depth, but they do not change how many XDC are counted as circulating, and that count is what this framework measures.

## What to watch in the next 90 days

First, the XDC 3.0 upgrade, aimed at mainnet in October 2026, which would move node rewards on chain and add a real burn; if it ships before **Dec 22 2026**, the reward and burn rows both change. Second, the locked team wallets at **21,308.9M XDC**: any release crosses straight into the float, and the last one was **Dec 15 2025**. Third, the Foundation ecosystem wallet at **725.6M XDC**, paying out about 50M every one to three weeks. Fourth, the staking contract at **3,701.1M XDC**, where an operator exit returns coins to wallets after about a month. Fifth, the aggregator calendar's next Ecosystem Development unlock on **Feb 5 2027**.

## Summary

The MrNasdog Pressure Framework reads XDC at **+0.09%** over the trailing 90 days and **+0.09%** projected forward: mixed flows, supply roughly steady. The whole reading is the XDC Network masternode reward, **18.82M XDC** per quarter, while the fee burn described in the January 2026 upgrade removed nothing on chain. The key risk is the **21,308.9M XDC** locked team bucket, which releases on no public schedule. XDC has no cap, so the mint runs forever, but at **5,000 XDC** per epoch it stays small.

MrNasdog Pressure Framework analysis of XDC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 23 2026.

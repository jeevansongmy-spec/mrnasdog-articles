---
title: "BTC Inflation Analysis · July 2026 · Mixed flows, supply roughly steady"
description: "A MrNasdog Pressure Framework read of Bitcoin (BTC): ~40.05K BTC mined over 90 days at 3.125 per block, no buyback and no burn. Framework +0.20% net; monitor +0.25%, under a 21M cap."
canonical_url: "https://mrnasdog.com/research/btc/inflation"
tags: ["crypto", "btc", "bitcoin", "proof-of-work"]
published: true
---

> Originally published at **[mrnasdog.com/research/btc/inflation](https://mrnasdog.com/research/btc/inflation)** by MrNasdog.

Bitcoin has exactly one source of new BTC — the block subsidy — and nothing at all on the other side of the ledger. Over the 90 days to **Jul 16 2026** the network mined **40.05K BTC** at **3.125 BTC** per block, while buyback, burn, foundation buying and locking all read **zero**, because Bitcoin has no such mechanism to run. Against a **20.06M** circulating supply that is **+0.20%** net, and our supply monitor independently reads **+0.25%** — a gap of just **0.05 percentage points**, so the two agree and no data-conflict chip ships. BTC is the slowest-inflating major asset on the framework, and its cap of **21M** is now roughly **95%** spent.

## The verdict, in one paragraph

For the 90-day window ending Jul 16 2026 the MrNasdog Pressure Framework reads **BTC at +0.20% net** — the entire figure produced by proof-of-work block subsidy, with an empty buy ledger beneath it. Our supply monitor reads the realized last-90-day change in circulating Bitcoin at **+0.25%**, so the gap is **0.05 percentage points** — the two readings agree, and **no monitor-gap chip ships**. They agree because Bitcoin is the one asset where nothing is hidden: circulating supply equals total mined supply, so there is no classification argument to have. The small residual is measurement noise on the monitor side, which infers supply from market cap and price, while the coinbase issuance is exact to the satoshi. BTC is a **quiet chain with a decaying mint and no offsetting sink** — mildly inflationary by arithmetic, and the tightest supply schedule in the framework.

## Sell pressure: where new BTC comes from

The whole sell side of Bitcoin is Sell #1 — protocol inflation — at **40.05K BTC** over 90 days. Every new BTC in existence arrives in the coinbase transaction of a mined block, paid to the miner who found it. Since the April 2024 halving that block subsidy has been **3.125 BTC**, and it will stay there until block **1,050,000**, around **April 2028**, when the halving schedule cuts it to **1.5625 BTC**. The figure above is measured rather than assumed: Bitcoin's own supply record moved from **20,016,872 BTC** on **Apr 17 2026** to **20,056,925 BTC** on **Jul 15 2026**, a difference of exactly **12,817** blocks of subsidy. That is about **142** blocks a day, not the textbook 144 — the network has been running a touch slow against rising difficulty, so the common shortcut of 450 BTC a day overstates the real mint by roughly a percent. Miners sell a large share of that subsidy to pay for power and hardware, which is why the framework books it as genuine sell pressure rather than a paper number.

The other three sell rows are zero, and each for a reason rooted in Bitcoin's design rather than a quiet window. Sell #2 — vesting unlocks — is **zero** because Bitcoin was a fair launch: no premine, no ICO, no investor or team allocation, and so no vesting schedule that could ever cliff. Sell #3 — Foundation and unscheduled unlocks — is **zero** because there is no foundation allocation, no DAO treasury and no reserve pool anywhere in the protocol; the mined total and the circulating count are the same number, which means there is no held-back bucket left to release. Sell #4 — long-term locked or bankruptcy — is **zero** in supply terms even though the Mt. Gox estate still holds roughly **34.5K BTC**, because those coins were mined years ago and are already counted as circulating. Bitcoin, uniquely, cannot surprise the market with supply that was minted but never counted.

## Buy pressure: where new BTC goes

Nowhere — and that is the honest structural answer, not a gap in the research. Buy #1 — programmatic buyback — is **zero**: Bitcoin has no treasury and no contract that could bid for its own coin. Buy #2 — protocol fee burn — is **zero**: transaction fees are paid to the miner inside the same coinbase as the subsidy, never destroyed, so Bitcoin has no equivalent of a base-fee burn to offset issuance. Coins sent to unspendable addresses, and the millions lost to discarded keys, are losses suffered by their owners, not a burn performed by the protocol, and the framework refuses to book them as buy pressure.

Buy #3 — Foundation buy — is **zero** because no foundation, company or protocol entity holds a Bitcoin budget with a mandate to buy. Buy #4 — new long-term lock — is **zero** because Bitcoin has no staking, no escrow and no lockup primitive; a coin in a corporate treasury, an ETF or a government reserve remains freely spendable and stays inside circulating supply, so the framework does not credit it as removed. The result is a ledger with a single live row. Every point of BTC inflation is the mint, and the only thing that ever reduces it is the halving.

## Foundation and overhang

Bitcoin has no team-controlled overhang to enumerate, and the proof is arithmetic rather than assertion: total supply and circulating supply are both **20.06M**, so the headroom between them is **zero**. There is no wallet holding minted-but-uncounted BTC that could be released, because no such allocation was ever created. The large balances people watch are third-party, not protocol: the dormant early-mining coins from 2009 to 2011, roughly **1.1M BTC** that have not moved in over a decade; government-seized coins; exchange custody holding depositor funds; and the Mt. Gox estate's remaining **34.5K BTC**, whose trustee has until **Oct 31 2026** to finish repaying creditors. None of these are a foundation or team, and each of them already sits inside circulating supply.

That matters for how the Mt. Gox distribution should be read. When the estate pays a creditor, an already-counted coin moves from one wallet to another; supply does not grow by a single satoshi. The framework still tracks the estate as an overhang because a creditor who receives BTC may choose to sell it, and its largest recent move — **10,422 BTC** in **June 2026** — went to the estate's own wallets and reached no exchange. If that balance drains toward an exchange or custodian between refreshes, the framework surfaces the outflow in Sell #3 at the next refresh, as a market event rather than as new supply.

## How BTC compares to other hard-capped proof-of-work chains

BTC is the original of the class it defines: **hard-capped proof-of-work with a halving schedule**. Its peers in structure — Litecoin, Bitcoin Cash, and newer halving assets like Bittensor's TAO — share the shape of a block reward that halves on a fixed rule toward a permanent ceiling. Against those, Bitcoin is simply further along the curve. At roughly **95%** of the **21M** cap mined, its remaining issuance is under **1M BTC** spread across the next century, which is why a 90-day mint of 40.05K reads as only **+0.20%** where a younger halving chain still prints multiples of that.

The sharper contrast is with everything that has a buy side. An uncapped proof-of-stake L1 mints continuously to pay validators with no ceiling to stop it, so its inflation is a policy choice that governance can revisit. A fee-burning chain destroys part of every transaction fee, so heavy usage can push it net-deflationary — Bitcoin cannot do that, because its fees pay miners rather than the fire. An exchange token that buys back and burns from quarterly profit can drive supply down by several percent a year, but only for as long as the issuer chooses to keep doing it. Bitcoin's answer to all three is that it does nothing at all: no burn to raise, no buyback to cancel, no emission vote to lose. The **21M** cap is enforced by every node independently, and this year's failed **BIP-110** fight — a soft fork that never cleared **1%** miner signalling — is a reminder of how little the network changes even on rules far less sacred than supply.

## What to watch in the next 90 days

Watch the block rate, because it is the only thing that moves Sell #1 before 2028. At **142** blocks a day the mint is running below the nominal 144; a hashrate surge pulls it back toward **40.5K BTC** a quarter, while further slowing trims it. Watch the Mt. Gox trustee ahead of the **Oct 31 2026** deadline — the deadline itself falls just outside this window, which closes **Oct 14 2026**, but a transfer of the remaining **34.5K BTC** toward an exchange or custodian would be a real market event even though it creates no supply. Watch the US Strategic Bitcoin Reserve legislation, where a mandate to buy or a decision to sell seized coins would move demand, never issuance. And watch the countdown to block **1,050,000** around **April 2028**, the next halving, which mechanically halves the framework's only sell row to roughly **+0.10%** a quarter.

## Summary

The MrNasdog Pressure Framework reads BTC at **+0.20% net** over the 90 days to **Jul 16 2026**, matching our supply monitor's **+0.25%** within **0.05 percentage points** — no data conflict, no chip. The structure is the simplest in the framework: **40.05K BTC** of block subsidy at **3.125** per block is the entire sell ledger, and the buy ledger is empty by design, because Bitcoin has no buyback, no fee burn, no treasury and no lock. The key risk is not dilution but demand — with no mechanism absorbing supply, every BTC miners sell must be bought by someone at the price, and the estate and government balances that overhang the market are all coins already counted. The ceiling is **21M**, about **95%** of it already mined, and the next halving in **April 2028** cuts the last live row in half again.

---

*MrNasdog Pressure Framework analysis of BTC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 16 2026.*

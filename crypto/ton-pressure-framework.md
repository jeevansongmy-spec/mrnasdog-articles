---
title:         "GRAM Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "GRAM supply keeps growing: a per-block reward paid every 0.41 seconds adds 50.89M a quarter, plus lock and Telegram payouts. +3.97% net in 90 days, +3.65% next."
canonical_url: "https://mrnasdog.com/research/gram/inflation"
tags:          ["crypto", "gram", "toncoin", "layer1"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/gram/inflation](https://mrnasdog.com/research/gram/inflation)*

# GRAM Inflation Analysis · September 2026 · Supply growing · projected to keep growing

**GRAM**, the coin of The Open Network (called Toncoin until Jun 15 2026), is clearly inflationary. In the 90 days to Sep 29 2026, **111.97M GRAM** reached the market against only **74.9K GRAM** taken out, a net rise of **+3.97%** of the circulating supply, with about **+3.65%** expected in the next 90 days. Most of it is new coins paid for every block since the network moved to 0.41-second blocks; the rest is coins leaving the Believers Fund lock and a Telegram treasury wallet. The monitor reads **+4.25%**, close to our number.

## The verdict, in one paragraph

Over the last 90 days GRAM supply grew by **+3.97%** net: **111.97M GRAM** of sell pressure against **74.9K GRAM** of buy pressure, on a circulating supply of **2.82B GRAM**. The next 90 days project **+3.65%**, a little lower only because we expect three Telegram treasury payments instead of four. The monitor, which reads supply from market data, shows **+4.25%** over the same 90 days. The gap is **0.28 percentage points**, small enough that the two readings agree, so no warning is shown. In one line: GRAM is an **inflationary Layer-1 by design**, where block rewards alone add about 1.8% of the circulating supply every quarter.

## Sell pressure: where new GRAM comes from

The first and largest source is protocol inflation: **50.89M GRAM** in 90 days. The Open Network pays block makers a fixed amount per block, 1.7 GRAM for each main-chain block and 1 GRAM for each work-chain block. That fixed amount did not change when the network switched to its faster Catchain 2.0 consensus on Apr 9 2026 and cut the block time from about 2.5 seconds to about 0.41 seconds. The same reward per block, paid about six times as often, is why GRAM's yearly issuance jumped from well under 1% of total supply to more than 3%. A plan to cut the reward to 0.35 and 0.2 GRAM was discussed in April 2026, but it was never voted into the network settings. We measured this row directly: total GRAM supply rose from about 5,206.56M to 5,257.37M across the window, and adding back the small fee burn gives 50.89M new coins, about 565,000 a day. Since Aug 20 2026, when collators were switched on, the network makes a few more blocks a day, so the next 90 days use the newer pace of about 575,000 a day, or **51.75M GRAM**.

The second source is vesting: **21.09M GRAM** left the Believers Fund lock in the window. Holders deposited 1.03B coins into this lock in 2023. Since Oct 12 2025 the lock opens one slice of about 36.6M GRAM every 30 days, 36 slices in all, ending in 2028. Unlock trackers count each slice as released, but GRAM only reaches the market when a holder claims it, and most have not: only 67.46M has been claimed in total, while 402.5M is already open. We count what actually left the lock, not what opened, and we project the same claimed pace forward: 21.09M GRAM in the next 90 days.

The third source is a Telegram treasury wallet: **40.0M GRAM**. That wallet sent 10M GRAM four times (Jul 3, Aug 8, Aug 29 and Sep 21 2026) to the wallet that pays channel owners and sellers on Telegram's marketplace, falling from 142.4M to 102.4M. The market-data classifier counts this treasury wallet as not circulating, so every payment out of it is new supply for the market. At about one payment every 27 days, we expect three in the next 90 days, **30.0M GRAM**.

The fourth row, long-term locks, is **0**. In February 2023 validators froze 180 early-miner wallets holding **1.08B GRAM**, about 38% of today's circulating supply. The freeze is part of the network settings and runs until Feb 21 2027, so none of these coins can move in the next 90 days. There is no bankruptcy estate and no court schedule for GRAM.

## Buy pressure: where new GRAM goes

There is no programmatic buyback: **0**. No contract, company or treasury buys GRAM off the market for the project, and none of the Telegram roadmap steps announced so far adds one. Companies that hold GRAM as a treasury bought it on the open market, so their coins were already circulating.

The protocol fee burn removed about **71.0K GRAM**. Half of every network fee is destroyed, but fees are tiny: they were cut six times on May 1 2026 to make transfers almost free. We sampled 240 main-chain blocks across the window, which gives about 790 GRAM burned a day, around 700 times smaller than new issuance. The next 90 days use the same rate.

Foundation buying is **0**: the Telegram treasury wallet received nothing in the window, it only paid out. New long-term locks are also **0**. About 544M GRAM is staked with validators, and Telegram itself became the largest validator in May 2026, but staked GRAM stays inside the circulating count, so more staking takes nothing off the market. One small extra row: people sent **3.83K GRAM** to the all-zero address, which is on the frozen list, so those coins can never move again.

## Foundation and overhang

GRAM carries some of the largest tracked overhangs in our catalog. The biggest is the Believers Fund lock with **1.25B GRAM**: about 335M of it is already open and could be claimed at any time, and the rest opens in 30-day slices until 2028. Next come the frozen early-miner wallets with **1.08B GRAM**, locked by the network until Feb 21 2027. The Telegram treasury wallet holds **102.4M GRAM** and pays out about 10M a month. Other Telegram-linked and marketplace wallets (about 248M, 99M and 87M GRAM) are already counted as circulating, and the old TON Foundation wallet holds about 1.59M GRAM and did not move. Together the lock, the frozen wallets and the treasury explain almost all of the 2.44B GRAM that is not circulating. We re-read these balances at every rebuild. If any of them falls between checks, the coins that left enter the Foundation and unscheduled row at the next check.

## How GRAM compares to other proof-of-stake Layer 1s

Most large proof-of-stake chains tie new coins to time or to the amount staked. Ethereum pays validators based on the total stake and burns part of every fee, so its supply grew only about 0.2% in a recent quarter. Solana issues new coins on a fixed schedule that shrinks every year. GRAM is different: it pays a fixed amount per block, so when the network made blocks about six times faster, issuance rose with it. That makes GRAM one of the few large chains where a speed upgrade raised inflation, and it leaves the reward cut as the one lever that could bring it back down.

The burn side is also weak by comparison. Chains like Ethereum and Tron destroy a large share of fees, and in busy periods that can match new issuance. GRAM burns half its fees too, but after the six-fold fee cut its fees are so small that the burn removes about 71K GRAM a quarter against about 51M created. And unlike most Layer 1s that finished their vesting years ago, GRAM still has two large locks feeding the market: the Believers Fund, opening until 2028, and the frozen miner wallets that reopen in February 2027.

## What to watch in the next 90 days

On Sep 30 2026 validators vote on a network settings change whose content has not been published; a cut to the block reward would lower the biggest sell row at once. The Believers Fund opens new 36.6M GRAM slices on Oct 7, Nov 6 and Dec 6 2026, and a jump in claims from the 335M already open would raise the vesting row fast. The Telegram treasury wallet's next 10M payments are expected around mid-October, mid-November and early December. Further out, the Feb 21 2027 end of the miner-wallet freeze is the largest single supply event ahead, at 1.08B GRAM.

## Summary

GRAM is inflationary by design: supply grew **+3.97%** in the 90 days to Sep 29 2026 and is projected to grow about **+3.65%** in the next 90, close to the monitor's +4.25%. The engine is a fixed block reward paid about every 0.41 seconds, which creates about 51M GRAM a quarter, joined by coins claimed from the Believers Fund and paid out by a Telegram treasury wallet. The fee burn is too small to offset any of it, and there is no buyback. The key risk is the 1.08B GRAM of frozen miner wallets that can move again after Feb 21 2027; the one lever that would cut issuance is a validator vote to lower the block reward.

---

*MrNasdog Pressure Framework analysis of GRAM, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

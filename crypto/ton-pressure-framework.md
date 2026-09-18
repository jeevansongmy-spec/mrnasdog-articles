---
title:         "GRAM Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description:   "Gram (formerly Toncoin) supply grows +3.74% a quarter: a flat block reward on six-times-faster blocks mints 50.91M, plus 53.65M of unlocks, vs a tiny fee burn."
canonical_url: "https://mrnasdog.com/research/ton/inflation"
tags:          ["crypto", "gram", "toncoin", "layer1"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/ton/inflation](https://mrnasdog.com/research/ton/inflation)*

# GRAM Inflation Analysis · September 2026 · Supply growing, projected to keep growing

Gram (GRAM), the native coin of The Open Network and the coin known as Toncoin until **Jun 15 2026**, is growing its supply by about **3.74%** a quarter. The Open Network pays a flat block reward — **1.7 GRAM** per masterchain block and **1.0 GRAM** per basechain block — and the Catchain 2.0 upgrade made blocks about six times faster without cutting that reward, so block minting alone created **50.91M GRAM** in 90 days. An early-supporter lock released **18.65M** and the Telegram treasury wallet sent out **35.00M**, while the fee burn removed only about **104K**. The MrNasdog Pressure Framework reads Gram at **+3.74% net** over the last 90 days against a supply-monitor reading of **+3.77%** — a gap of **0.04 percentage points**, which is agreement, not conflict.

## The verdict, in one paragraph

For the 90-day window ending **Sep 18 2026**, the Pressure Framework reads **Gram at +3.74% net**: the sell side added **104.56M GRAM** through block minting, the early-supporter lock and the Telegram treasury wallet, while the buy side removed **107,958 GRAM** through the protocol fee burn and voluntary burns to the zero address. The independent supply monitor reads the realised 90-day change at **+3.77%**. The gap is **0.04 percentage points**, well inside the framework's half-point tolerance, so Gram ships with **no data-conflict flag**. The forward column reads **+3.59%**, a little softer, because the Telegram treasury wallet has settled into 10M tranches about four weeks apart, which puts three tranches rather than four in the next 90 days. The label for Gram is **structurally inflationary by block reward**: an uncapped chain whose supply grows with the number of blocks it makes, and it now makes far more of them.

## Sell pressure: where new GRAM comes from

Sell #1, protocol inflation, is **50.91M GRAM**, and it is the core of the Gram story. The Open Network creates new coins as a fixed fee on every block: **1.7 GRAM** for a masterchain block and **1.0 GRAM** for a basechain block, set in the chain's own configuration and unchanged at every point read this window. What changed is the pace. Catchain 2.0 went live on **Apr 9 2026** and cut the masterchain interval from about **2.35 seconds** to about **0.41 seconds**, and no reward cut came with it. A proposal to lower the reward was discussed around the upgrade, but the chain's configuration still reads the old values and no change is pending on-chain. So the block count is the issuance: **18,976,941** masterchain blocks and **18,651,959** basechain blocks in 90 days. Blocks sped up a little more after a validator change in mid-August, so the forward column uses that faster rate, **51.79M GRAM**.

Sell #2, vesting unlocks, is **18.65M GRAM**, and it was measured on the lock itself rather than taken from the calendar. In 2023 early supporters placed their coins in a voluntary lock that, with its bonus, pays out about 1.32B in 36 slices, one every 30 days until **Oct 2028**. Three slices, about **109.78M GRAM**, came due in this window, but holders withdrew only **18.65M**; the rest sits inside the lock, vested and unclaimed. Sell #3, foundation and unscheduled unlocks, is **35.00M GRAM** from the Telegram treasury wallet, which sits outside the counted float. It sent **5M** on **Jun 22 2026** and **10M** each on **Jul 3**, **Aug 8** and **Aug 29**, every time to a payout wallet that spread the coins to thousands of recipients. Sell #4, long-term locked or bankruptcy supply, is **zero**: no estate distributes Gram, and the 2023 freeze on untouched early-mining accounts, about **1.08B GRAM**, runs until **Feb 21 2027**, outside both windows.

## Buy pressure: where new GRAM goes

Buy #1, programmatic buyback, is **zero**: The Open Network has no buyback contract, and the listed companies that hold Gram as a treasury asset bought on the open market, so their coins were already in the float. Buy #2, the protocol fee burn, is about **104K GRAM**. Half of every transaction fee is destroyed by the protocol, a split written into the chain's configuration, and the burn address holds nothing because the protocol deletes the coins rather than parking them. Because fees on Gram are tiny, the burn removes about one coin for every **490** that block minting creates. The mint and the burn are separate flows — an empty block still pays its reward with nothing burned — so they are booked on separate lines.

Buy #3, foundation buying, is **zero**: the Telegram treasury wallet took in nothing this window, after monthly top-ups from Telegram's marketplace stopped at the end of May, and no other team wallet bought Gram. Buy #4, new long-term locks, is **zero**. Gram staking grew this window, but staked coins return after each validation round and stay inside the circulating count. One extra line, Buy #5, records **3,846 GRAM** sent by holders to the zero address, which is on the frozen list and can never move them again.

## Foundation and overhang

Three large Gram balances sit outside the float, and each is read on-chain at every rebuild. The early-supporter lock holds **1.25B GRAM**, of which more than 330M has already vested and could be withdrawn at any time. The Telegram treasury wallet holds **112.42M GRAM** and has been the most active seller of the three. The frozen early-mining accounts hold about **1.08B GRAM** until **Feb 21 2027**, and many of those keys may be lost. Inside the float, the framework also tracks Telegram's marketplace wallets at about **128M GRAM**, a foundation wallet at **1.59M** that did not move, and two closed bridges holding **11.34M**. If any of these balances falls between refreshes and the coins reach the market, the outflow enters Sell #3 at the next refresh.

## How GRAM compares to other proof-of-stake Layer-1 chains

Most proof-of-stake Layer-1 chains tie issuance to time or to the amount staked. A chain with a yearly inflation schedule pays a set share of supply per year, so making blocks faster changes nothing; when one such chain sped up its slots, it rescaled its slots-per-year figure to keep issuance flat. Gram ties issuance to the block. Its reward is a fixed amount per block, so when Catchain 2.0 made blocks about six times faster, Gram's issuance rose about six times too. That is why stale tokenomics pages still quote Gram at well under 1% a year, while the chain itself now adds close to 4% a year before any unlocks.

Against burn-heavy chains the contrast is stark. On a chain like Ethereum, a base-fee burn can offset a large part of issuance when activity is high. Gram also burns half of its fees, but its fees are very small: the chain's own gas income is about **$1M a year** against a market value near **$3.75B**. Most of the money moving through the Gram economy is in Telegram's collectibles marketplace, which is paid in Gram but is not a network fee, so none of it is burned. Against capped proof-of-work chains, Gram has no supply cap at all: supply rises every day, with no halving to slow it.

## What to watch in the next 90 days

First, the block reward: any validator vote that lowers the **1.7** and **1.0 GRAM** per-block reward would cut Sell #1 at once, and it is the only change that could move Gram's forward reading by more than a point. Second, the Telegram treasury wallet: the forward column books three **10M** tranches, and a pause or a larger tranche moves Sell #3 directly. Third, the early-supporter lock: the next slices come due around **Oct 7 2026**, **Nov 6 2026** and **Dec 6 2026**, and a rush to claim the backlog of more than 330M would lift Sell #2 far above its **18.65M** pace. Fourth, the Gram Wallet rollout inside Telegram that began on **Aug 31 2026**: more use means more fees, but it would need to grow many times over before the burn meets the block reward.

## Summary

The MrNasdog Pressure Framework reads Gram, formerly Toncoin, at **+3.74% net** over the trailing 90 days and **+3.59%** over the next 90, in agreement with the supply monitor. The structural mechanism is a flat per-block reward on a chain that now makes blocks about six times faster than before **Apr 2026**, which created **50.91M GRAM** in 90 days, joined by **18.65M** from the early-supporter lock and **35.00M** from the Telegram treasury wallet, against a fee burn of only about **104K**. The key risk is the size of the locked backlog: more than 330M vested coins in the early-supporter lock can be claimed at any time, and the **1.08B GRAM** freeze on early-mining accounts ends on **Feb 21 2027**. There is no supply cap, so the only brake on Gram issuance is a validator vote to lower the per-block reward.

---

*MrNasdog Pressure Framework analysis of GRAM, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 18 2026.*

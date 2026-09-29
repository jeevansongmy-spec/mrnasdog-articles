---
title:         "BTC Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "BTC supply is roughly steady: miners created 40,384 BTC in 90 days at 3.125 per block, with no burn and no buyback. Net +0.20%, the same next, under a 21M cap."
canonical_url: "https://mrnasdog.com/research/btc/inflation"
tags:          ["crypto", "btc", "bitcoin", "proof-of-work"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/btc/inflation](https://mrnasdog.com/research/btc/inflation)*

# BTC Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

BTC, the coin of Bitcoin, grows slowly and only from mining: Bitcoin miners created **40,384 BTC** over the last 90 days, and nothing on the network burned, bought back or locked away a single coin. The MrNasdog Pressure Framework therefore reads BTC at **+0.20% net** over 90 days, and the same for the next 90, against a supply-monitor reading of **+0.19%** — a gap of just **0.01 percentage points**, so the two agree. Bitcoin's block subsidy halves on a fixed schedule and the total can never pass **21M BTC**, of which about **95.7%** is already mined.

## The verdict, in one paragraph

For the 90-day window ending **Sep 29 2026**, the Pressure Framework reads **BTC at +0.20% net**: the sell side added **40,384 BTC** of newly mined coins and the buy side removed **0 BTC**, out of a circulating supply of **20.09M BTC**. The independent supply monitor reads **+0.19%**. The gap is **0.01 percentage points**, far inside the framework's half-point tolerance, so BTC ships **without a data-conflict flag**. The forward column also reads **+0.20%**, because Bitcoin's block reward does not change again until the next halving, around **April 2028**. The label for BTC is **slow, fixed-schedule issuance under a hard cap**: a proof-of-work coin whose only new supply is the mining reward, and which has no mechanism of any kind that takes coins out.

## Sell pressure: where new BTC comes from

All of it comes from one place. Sell #1, protocol inflation, is **40,384 BTC**. Every Bitcoin block pays the miner who finds it a subsidy of **3.125 BTC**, the rate set by the April 2024 halving. Between **Jul 1 2026** and **Sep 29 2026** miners found **12,923** blocks, from block **956,150** to block **969,072**, and 12,923 blocks at 3.125 BTC each is 40,384 BTC. The count was measured, not assumed: blocks arrived about every **601.7 seconds**, a touch slower than Bitcoin's ten-minute target, so the textbook figure of 12,960 blocks a quarter would have overstated new BTC by about 0.3%. An independent read of total mined Bitcoin supply at both ends of the window rose by the same amount. Bitcoin issuance is tied to blocks, not to time, and the difficulty adjustment only re-aims the pace every 2,016 blocks, so the measured count is the one that ships and the forward column holds the same rate.

Sell #2, vesting unlocks, is **zero**, and it is zero by design: Bitcoin had no premine, no token sale and no team or investor allocation, so there has never been a Bitcoin vesting schedule to unlock. Sell #3, foundation and unscheduled unlocks, is also **zero**. Bitcoin has no foundation and no project treasury, and almost every mined coin already counts as circulating — only about **309 BTC** sits outside the circulating count. When governments sell seized bitcoin, when very old wallets wake up, or when exchanges move funds, those coins were already part of the market count and add no new BTC. Sell #4, long-term locked or bankruptcy supply, is **zero** as well, even though the Mt. Gox estate still holds about **34,500 BTC** and must finish paying its creditors by **Oct 31 2026**. Those coins were mined years ago and are already counted, so paying them out moves BTC from one holder to another and does not add to supply.

## Buy pressure: where new BTC goes

Nowhere — every Bitcoin buy row reads **zero**. Buy #1, programmatic buyback, is zero because Bitcoin has no treasury, no contract and no fee share that buys BTC off the market. Spot bitcoin funds, listed companies and governments do buy bitcoin, sometimes in large size, but they buy coins already counted as circulating, so their buying changes who holds BTC, not how much BTC exists. Buy #2, the protocol fee burn, is zero because Bitcoin burns nothing: every transaction fee is paid to the miner in the block reward. A few people still send small amounts to addresses no one can spend from; inside this window those sends came to well under one thousandth of a bitcoin.

Buy #3, foundation buying, is **zero** because there is no foundation to buy. Buy #4, new long-term locks, is **zero** because Bitcoin has no staking and no lock contract. A United States bill that would stop the government from selling its seized bitcoin for 20 years passed a House committee on **Sep 16 2026**. Even if it becomes law, it would keep coins that already exist where they are; those BTC would still count as circulating, so the lock removes nothing from Bitcoin supply.

## Foundation and overhang

Bitcoin has no team-held overhang at all. There is no foundation, no company treasury, no DAO, no buyback wallet and no unscheduled reserve — every BTC ever created came from mining, and circulating supply of **20.09M BTC** is within about **309 BTC** of everything mined. The large balances people watch belong to third parties: the Mt. Gox estate with about **34,500 BTC**, governments holding seized bitcoin, spot bitcoin funds and exchanges holding coins for their customers, and the dormant wallets mined in Bitcoin's first years. All of them sit inside the circulating count, so none of them can add new BTC to the market when they move; they are tracked as context only. The circulating-versus-mined gap is re-read on every refresh, and if a balance ever appears outside the circulating count and then falls between refreshes, that outflow enters Sell #3 at the next refresh.

## How BTC compares to other proof-of-work chains

BTC is the original halving-model coin: a fixed block subsidy that halves every 210,000 blocks, roughly every four years, toward a hard cap of 21M BTC. Litecoin and Bitcoin Cash copy that design with their own caps and halving dates, so their supply growth also falls in steps. Tail-emission coins take the other route: Monero, for example, pays a small fixed reward per block forever, so it never reaches a cap and its percentage growth only shrinks as supply grows. Dogecoin pays a fixed reward per block with no cap at all. Next to all of them, Bitcoin is the most predictable issuer — anyone can work out the new BTC for any future block from the block height alone.

Against uncapped proof-of-stake chains the contrast is sharper. Chains that pay validators in new coins usually issue more each quarter as more coins are staked, and many rely on a fee burn to offset part of it. Bitcoin has neither: no staking reward that grows, and no burn that shrinks supply when the network is busy. That leaves BTC with a small, steady, falling rate of new supply — about **0.20%** a quarter today, halving to about 0.1% a quarter after the next halving — and with no buy-side mechanism, so Bitcoin supply can only grow until the last coin is mined, expected around 2140.

## What to watch in the next 90 days

First, the Mt. Gox deadline on **Oct 31 2026**: the estate still holds about **34,500 BTC**, and paying creditors would move those coins toward exchanges, but the coins are already counted, so the supply reading does not change. Second, the pace of blocks: Bitcoin difficulty re-adjusts every 2,016 blocks, and if hashrate keeps rising faster than difficulty, blocks arrive quicker and the quarter mints a little more than the **40,384 BTC** booked forward. Third, the Strategic Bitcoin Reserve bill, which still needs the full House and the Senate; it would lock government bitcoin in place, not remove it from the count. Fourth, BIP-361, a draft proposal to phase out old address types that a quantum computer could one day break and to freeze coins that are not moved in time; it has no activation date, but it is the one idea on the table that could ever take coins out of Bitcoin's usable supply. The next halving, around **April 2028**, falls well outside this window.

## Summary

The MrNasdog Pressure Framework reads BTC at **+0.20% net** over the trailing 90 days and **+0.20%** over the next 90: **40,384 BTC** of Bitcoin block subsidy from **12,923** blocks at 3.125 BTC each, with no vesting, no unlocks, no burn and no buyback. The structural mechanism is a proof-of-work reward that halves every 210,000 blocks, so Bitcoin issuance is fixed by code and falls over time. The key risk to the reading is small: a faster block pace mints slightly more, and third-party holders such as the Mt. Gox estate move coins that are already counted. BTC has a hard cap of **21M**; about 95.7% is already mined, and supply keeps growing, ever more slowly, until the last coin.

---

*MrNasdog Pressure Framework analysis of BTC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

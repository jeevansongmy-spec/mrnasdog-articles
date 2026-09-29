---
title:         "LTC Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "LTC is mildly inflationary: miners got 324K new LTC in 90 days at 6.25 per block, with no burn and no buyback, so supply rose +0.42%. The same is expected next."
canonical_url: "https://mrnasdog.com/research/ltc/inflation"
tags:          ["crypto", "ltc", "litecoin", "pow"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/ltc/inflation](https://mrnasdog.com/research/ltc/inflation)*

# LTC Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

Litecoin (LTC) is **mildly inflationary**, and only one thing makes it so: the mining reward. In the 90 days to Sep 29 2026 the network created **324,038 new LTC** for miners and destroyed **none**, so supply grew **+0.42%**. The next 90 days look the same, and the reward is fixed at 6.25 LTC per block until the next halving, around late July 2027, under a hard cap of **84 million LTC**.

## The verdict, in one paragraph

Our 90-day reading for Litecoin is **+0.42%** net new supply: 324,038 LTC created against 77.66M LTC in circulation, with nothing taken back. Our independent supply monitor reads **+0.47%** over its own 90-day window, a gap of **0.05 percentage points** — well inside our 0.5-point tolerance, so no warning chip is shown and the two readings agree. The forward reading is the same **+0.42%**, because the block reward does not change inside the next 90 days. In one line: **a quiet proof-of-work chain with slow, fixed issuance and no sink**.

## Sell pressure: where new LTC comes from

**Protocol inflation** is the whole sell side. Every Litecoin block pays its miner **6.25 LTC** of new coins, the amount set by the third halving in August 2023. Litecoin aims for one block every 2.5 minutes, and over the last 90 days it hit that almost exactly: block 3,134,412 on Jul 1 2026 to block 3,186,258 on Sep 29 2026 is **51,846 blocks**, one every 149.98 seconds. At 6.25 LTC each, that is **324,038 LTC** of new supply. We checked it three ways — block count times reward, the miners' total reward less their fees, and the chain's supply at both ends of the window — and all three agree to within a few LTC. Litecoin re-sets its mining difficulty every 2,016 blocks, so a run of fast or slow blocks can nudge issuance up or down a little, but this window ran on target. Looking forward, the same pace gives about **324,042 LTC** over the next 90 days.

**Vesting unlocks are zero**, and always have been. Litecoin launched in October 2011 as a fair launch: no premine, no team share, no investor round, no foundation allocation. Every LTC in existence came out of a mined block, so there is no unlock calendar and no locked bucket waiting to open.

**Foundation and unscheduled unlocks are zero.** The Litecoin Foundation is a non-profit funded by donations; it never received coins from the protocol and publishes no wallet, and we saw no sale by it in the window. **Long-term locked or bankruptcy is zero** too: no estate, trustee or court-ordered distribution holds LTC. The one frozen amount on the chain — 85,034 LTC tied to the March 2026 bug in the MWEB privacy layer — was locked back into that layer at block 3,078,098, before this window, and it already sits inside the counted supply.

## Buy pressure: where new LTC goes

Litecoin has **no buy side at all**. There is **no programmatic buyback**: no protocol treasury, no fee share and no contract that buys LTC. There is **no protocol fee burn**: transaction fees go to miners on top of the block reward. Over the window, users paid about 734 LTC in fees across 15.4M transactions, and every coin of it went to the block finders rather than being destroyed. The best-known unspendable address on Litecoin holds just 0.18 LTC in its whole life.

There is **no foundation buy** either. Buying by funds and companies did happen — US spot Litecoin funds reached a record of about 175,000 LTC on Sep 25 2026 — but that is ordinary market buying of coins already in circulation; it moves LTC from one holder to another and removes nothing from supply. And there is **no new long-term lock**: Litecoin has no staking. Coins can move into the MWEB privacy layer — about 442,800 LTC sat there at the end of the window, up about 108,300 in 90 days — but they stay counted and can move back at any time, so the buy total is **0 LTC**.

## Foundation and overhang

Because Litecoin had no premine, its team-controlled overhang is small and mostly unknown in size. The Litecoin Foundation holds whatever donations it has received but publishes no balance; we re-check its public reports every two weeks. The frozen 85,034 LTC from the March 2026 MWEB incident is fixed by the software and cannot move; we re-read it at each rebuild. The largest listed company holding Litecoin reports **832,716 LTC** (last updated Jul 17 2026) and has sold some coins in the past to fund a share buyback, but it bought those coins on the open market, so a sale moves coins already counted. The gap between Litecoin's total and circulating supply is only about 2,900 LTC, which means no large wallet sits outside the circulating count. If any tracked holder's balance falls between our checks, the outflow will be weighed as sell pressure at the next check.

## How LTC compares to other proof-of-work chains

Litecoin copies Bitcoin's supply design at four times the scale: a hard cap of 84 million against Bitcoin's 21 million, a halving every 840,000 blocks instead of every 210,000, and blocks every 2.5 minutes instead of every 10. Litecoin has had three halvings (2015, 2019, 2023); Bitcoin has had four. Litecoin's 90-day issuance of **+0.42%** is about double Bitcoin's current rate, because Litecoin's third halving came in 2023 while Bitcoin's fourth came in 2024 — Bitcoin is simply one cut further down the same curve. After Litecoin's next halving in mid-2027, its rate falls to roughly 0.21% per 90 days.

Against Dogecoin, the other big Scrypt-mined coin, the difference is the cap. Dogecoin pays a fixed 10,000 DOGE per block forever, with no cap and no halving, so its supply keeps growing by the same number of coins every year. Litecoin's issuance shrinks by half every four years or so and stops for good at 84 million. Like Bitcoin and Dogecoin, Litecoin has no fee burn — unlike chains such as Ethereum, where part of each fee is destroyed — so nothing ever offsets new supply.

## What to watch in the next 90 days

No dated supply event falls inside the next 90 days: the reward stays **6.25 LTC** per block, and the next halving, at block 3,360,000, is about 301 days away, around late July 2027. The first watch item is block pace — if miners find blocks faster than every 2.5 minutes, issuance runs slightly above 324,042 LTC. The second is the MWEB privacy layer: the software patches released on Aug 2 2026 and Sep 12 2026 tightened its checks after the March 2026 bug, and any new flaw there is the one way supply could break from the schedule. The third is LitVM, a smart-contract layer planned for Q4 2026, which could lock LTC into bridges without changing issuance. The fourth is the spot ETF filing for the Grayscale Litecoin Trust, filed on Sep 11 2026, which could bring more fund buying but would not change supply.

## Summary

Litecoin is mildly inflationary at **+0.42% per 90 days**, from a single source: 6.25 new LTC to miners in every block, 324,038 LTC in the last 90 days, with no burn, no buyback and no lock to offset it. It launched with no premine, so there are no vesting unlocks or team sales to watch, and our independent monitor agrees with the reading. The main supply risk is a software flaw in the MWEB privacy layer, not a planned release. The ceiling is hard: 84 million LTC, and the next halving around late July 2027 cuts new supply in half.

---

*MrNasdog Pressure Framework analysis of LTC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

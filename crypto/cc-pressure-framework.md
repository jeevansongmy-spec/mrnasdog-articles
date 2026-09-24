---
title:         "CC Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description:   "CC supply growing, projected to keep growing: Canton Coin reads +1.93% net over 90 days as 2.10B CC of new coins outrun the 1.33B CC burned for network traffic."
canonical_url: "https://mrnasdog.com/research/cc/inflation"
tags:          ["crypto", "cc", "canton", "layer1"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/cc/inflation](https://mrnasdog.com/research/cc/inflation)*

# CC Inflation Analysis · September 2026 · Supply growing, projected to keep growing

Canton Coin supply is still growing. CC is an **uncapped burn-and-mint coin** with no pre-mine and no vesting calendar: over the 90 days to **Sep 24 2026** the Canton Network minted **1.94B CC** in rewards, the Canton development fund paid out **58.5M CC** in grants, and super-validator votes released **102.8M CC** from the unminted reward pool. Against that, **1.33B CC** was burned paying for network traffic. The MrNasdog Pressure Framework reads Canton Coin at **+1.93% net** against a supply-monitor reading of **+2.06%**, a gap of **0.13 percentage points**, with the same **+1.93%** projected for the next 90 days.

## The verdict, in one paragraph

For the 90-day window ending **Sep 24 2026**, the Pressure Framework reads Canton Coin at **+1.93% net** — a sell side of **2.10B CC** against a buy side of **1.33B CC**, leaving **766M CC** of new float on a circulating base of **39.67B CC**. The independent supply monitor reads the realised 90-day change at **+2.06%**. The gap is **0.13 percentage points**, inside the framework's half-point tolerance, so Canton Coin ships with **no data-conflict flag**. The ledger also closes against the Canton Network's own supply reading day by day: on 73 of the 90 days the reward mint minus the traffic burn matches the change in total CC supply, and on each of the other 17 days the extra coins trace to a dated development-fund grant or a dated governance mint. The forward column reads the same **+1.93%**, because every leg held a steady pace and no scheduled event is due. The label for Canton Coin is **inflationary by design while the mint leads the burn**: every fee is destroyed, and the Canton Network still creates more CC than it destroys.

## Sell pressure: where new CC comes from

Almost all new Canton Coin comes from Sell #1, protocol inflation, at **1.94B CC** over the window. Every ten-minute round the Canton Network mints CC and pays it to the apps, validators and super validators that carry traffic across its shared public network: apps take about **72%** of the reward mint, super validators and validators about **14%** each. The Canton minting curve currently allows **10B CC a year**, and the realised mint came to about **79%** of that budget — 5% of the budget is set aside for a development fund, and rewards nobody claims expire into an unminted pool. The Canton Coin mint held between roughly 20M and 22M CC a day all window, with no step. A vote to switch app rewards over to a traffic-based measure was turned down in August, so nothing changed the rate, and the curve itself does not step down to 5B CC a year until mid-2029.

Sell #2, vesting unlocks, is **zero**: Canton Coin had no pre-mine, no investor round and no team allocation, so there is no CC vesting calendar at all. Sell #3, foundation and unscheduled unlocks, is **58.5M CC**. The CIP-0082 development fund earns 5% of the minting budget as unminted credit, and those coins are created only when the foundation pays a grant. Grants reached supply in batches through the window — about **13.6M CC** on **Jul 16 2026**, **11.6M** on **Aug 5** and **13.8M** on **Sep 3** — and grant batches have landed every month since May, which is why the forward column carries the same pace. Sell #4, long-term locked or bankruptcy supply, is **zero**: no Canton estate or trustee distributes CC and no long-dated lock is unwinding.

A fifth sell row carries the governance milestone mints. Canton super validators can vote CC out of the unminted reward pool to a named operator once it reaches an agreed milestone, usually tied to joining the network as a super validator. Eleven of those mints reached supply in the window, **102.8M CC** in total — the largest **25.4M CC** to Zenith on **Sep 5 2026**, **19.6M** to LayerZero on **Aug 13**, **19.2M** to Chainlink on **Jul 31** and **15.1M** to Wormhole on **Sep 18**. One more August vote reached quorum but never minted because it named the wrong wallet, and it is not counted.

## Buy pressure: where new CC goes

Canton Coin has one buy-side mechanism, and it is a large one. Buy #2, the protocol fee burn, destroyed **1.33B CC** over the window. Traffic on the Canton Global Synchronizer is priced in dollars per megabyte and paid in CC, and the CC is burned on purchase — no validator keeps a tip and no treasury takes a cut. That is about **3.4%** of circulating Canton Coin destroyed in 90 days, and about **63%** of all the new CC created in the same period. The pace rose through the window, from about **12.6M CC** a day in the first two weeks to about **15.3M** a day since mid-August; the forward column holds the 90-day average rather than the faster recent rate. Because the fee is set in dollars, a lower CC price burns more coins for the same traffic, and part of the rise reflects that.

Buy #1, programmatic buyback, is **zero**: there is no Canton Coin buyback programme and no wallet buying CC back. Buy #3, foundation buying, is **zero**. Buy #4, new long-term locks, is also **zero**, and that one needs explaining. Canton super validators must now hold a share of their lifetime rewards back to keep their voting weight, and featured apps must hold CC to keep their status — about **18.31B CC** is disclosed as held back by super validators alone. But every one of those coins is still counted in the circulating CC figure, which equals total supply, so a new lock removes nothing from the float this framework measures, and an unlock would add nothing either.

## Foundation and overhang

Two pools of Canton Coin sit outside supply and can enter it. The first is the CIP-0082 development fund: about **210M CC** earned but not yet paid out, none of it tied to an active milestone today, growing by roughly **1.37M CC** a day. The second is the unminted reward pool, which fills with every Canton reward that goes unclaimed and can only be drawn down by a super-validator vote. Both are read on every rebuild. The development fund pays monthly; the pool pays when a milestone vote executes. Inside the float, the super-validator hold-back wallets are watched as well, but they cannot add new CC because they are already counted. If the development fund or the unminted pool falls faster than this ledger assumes between refreshes, the outflow enters Sell #3 or Sell #5 at the next refresh.

## How CC compares to other layer-1 chains

Most proof-of-stake layer-1 chains pay validators in freshly minted coin and hope a fee burn catches up. Canton Coin is built the same way in outline — a reward mint on one side, a fee burn on the other — but with two differences. Canton pays nothing to validators out of fees: the whole fee is destroyed, and every reward comes from the mint. And Canton prices its fees in dollars rather than in its own coin, so the Canton Coin burn grows when network traffic grows and also when the CC price falls. Measured in money, the burn came to about **$154M** over the 90 days, a yearly pace near **15%** of Canton Coin's market value.

Against proof-of-work coins with a hard cap, CC differs twice. It has no cap, so supply can rise forever, and its minting curve steps down on a calendar rather than by block height: the Canton budget went from 20B to 10B CC a year around the turn of 2026 and next halves in mid-2029. A capped proof-of-work coin issues less every four years until issuance stops; Canton Coin keeps a permanent 2.5B CC a year floor on the mint after year ten, and relies on the burn to outrun it. Canton also has a governance mint that most chains lack — super validators can vote coins out of an unminted pool — which adds a discretionary line that a pure block-reward chain does not carry.

## What to watch in the next 90 days

First, the Canton burn pace: it has run near **15.3M CC** a day since mid-August against a mint near **21.5M**, and the gap between the two is the whole of the net reading. Second, a new vote to switch app rewards to the CIP-0104 traffic-based measure — the August attempt failed, and a passed vote would change the largest line on the page. Third, CIP-0120, still a proposal, which would do the same for validator rewards. Fourth, milestone mints for super validators approved this autumn, including Paxos (CIP-0125, approved **Sep 14 2026**) and LSEG (CIP-0124): each can release a new tranche from the unminted pool once its milestone is met. Fifth, the development fund's next grant batches against its **210M CC** balance.

## Summary

The MrNasdog Pressure Framework reads Canton Coin at **+1.93% net** over the trailing 90 days and **+1.93%** over the next 90, against a supply-monitor reading of **+2.06%**. The structural mechanism is an uncapped burn-and-mint design: the Canton Network mints about **21.5M CC** a day in rewards, adds development-fund grants and governance milestone mints on top, and destroys every coin spent on traffic — **1.33B CC** in 90 days, or about 63% of new supply. The key risk is that the burn depends on traffic that is partly driven by the same rewards, while the mint runs on a fixed calendar, so a slower quarter for traffic widens the net at once. The ceiling is the minting curve itself: 10B CC a year until mid-2029, then 5B, then a permanent 2.5B CC a year — the burn has to outrun that floor for Canton Coin supply ever to shrink.

*MrNasdog Pressure Framework analysis of CC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 24 2026.*

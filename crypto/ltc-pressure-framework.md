---
title:         "LTC Inflation Analysis · September 2026 · Mixed flows, supply roughly steady"
description:   "Mixed flows, supply roughly steady: Litecoin mining minted 322,906 LTC in 90 days at 6.25 LTC a block, with no burn or buyback. +0.42% net; halving Jul 2027."
canonical_url: "https://mrnasdog.com/research/ltc/inflation"
tags:          ["crypto", "ltc", "litecoin", "pow"]
published:     true
---

# LTC Inflation Analysis · September 2026 · Mixed flows, supply roughly steady

*Originally published at [https://mrnasdog.com/research/ltc/inflation](https://mrnasdog.com/research/ltc/inflation)*

Litecoin (LTC) is a proof-of-work coin with a hard **84M LTC** cap, and mining is its only source of new supply. Over the last 90 days Litecoin miners found **51,665** blocks at a fixed **6.25 LTC** block reward, minting **322,906 LTC**, while nothing on the buy side removed a single coin: Litecoin has no fee burn, no buyback and no lock. The MrNasdog Pressure Framework reads LTC at **+0.42% net** against a supply-monitor reading of **+0.54%** — a gap of **0.13 percentage points**, inside tolerance. The next Litecoin halving, to 3.125 LTC, is about **183,000 blocks** away, around late **Jul 2027**.

## The verdict, in one paragraph

For the 90-day window ending **Sep 13 2026**, the Pressure Framework reads **LTC at +0.42% net**: **322,906 LTC** of new mining supply against a circulating base of **77.60M LTC**, with every buy row at zero. The independent supply monitor reads the realised 90-day change at **+0.54%**. The gap is **0.13 percentage points**, inside the framework's half-point tolerance, so Litecoin ships with **no data-conflict flag**; the monitor sits a little higher only because its reading 90 days ago was a single low day in an otherwise smooth series. The forward column also reads **+0.42%**, because the block reward does not change until the halving and no other supply event is scheduled. The label for LTC is **a clockwork proof-of-work emitter with an empty buy side**: small, predictable, bounded only by the 84M ceiling, and never offset.

## Sell pressure: where new LTC comes from

Sell #1, protocol inflation, is **322,906 LTC**, and it is the entire Litecoin sell side. Each Litecoin block pays the miner who finds it **6.25 LTC**, a per-block amount that halves every **840,000** blocks. The number was built from the chain, not from the schedule: the window held exactly **51,665** blocks, every block's coinbase was counted, and not one paid more or less than 6.25 LTC. Litecoin blocks ran slightly slow — **150.51 seconds** each against a 150-second target — and because the Litecoin reward is paid per block with no adjustment for time, a slow chain simply mints less. The textbook figure of 576 blocks a day would have overstated LTC issuance by about a third of a percent.

Sell #2, vesting unlocks, is **zero**, and permanently so: Litecoin launched in Oct 2011 with no premine and no team, investor or foundation allocation, so no Litecoin vesting schedule has ever existed. Sell #3, foundation and unscheduled unlocks, is **zero**. There is no protocol treasury, and the Litecoin Foundation is funded by donations with no published LTC reserve. Sell #4, long-term locked or bankruptcy supply, is **zero**: no estate or trustee distributes LTC, and the spot LTC funds bought their coins on the open market. Two Litecoin upgrades landed inside the window — soft forks at block **3,154,440** on **Aug 4 2026** and block **3,172,640** on **Sep 5 2026** — both tightening validation of the MWEB privacy layer. Neither touched the block reward; the block count spans both heights and every reward read 6.25 LTC.

## Buy pressure: where new LTC goes

Nowhere, and that is the other half of the Litecoin story. Buy #1, programmatic buyback, is **zero**: Litecoin has no protocol revenue and no buyback contract. Buy #2, protocol fee burn, is **zero**: Litecoin miners keep every transaction fee, about **741 LTC** across the window. The burn was checked both ways rather than assumed — Litecoin supply rose by exactly the mining reward, and the one known Litecoin burn address has received nothing since **Apr 17 2026**. Buy #3, foundation buying, is **zero**, with no programme announced or visible on-chain.

Buy #4, new long-term locks, is **zero**. Proof-of-work has no staking, so nothing on Litecoin is locked for a reward. The closest thing is MWEB, Litecoin's optional privacy layer, which grew sharply this window — from about **333K LTC** to **563K LTC** pegged in. Those coins stay spendable, and they stay inside the counted supply: Litecoin holds every MWEB coin in one ordinary on-chain output that is rebuilt each block, so moving LTC into or out of the privacy layer changes who can see a balance, never how many LTC exist. That was the one mechanism that could plausibly have split the framework from the monitor, and the chain reads rule it out.

## Foundation and overhang

Litecoin has no team-controlled overhang in the usual sense, because nothing was ever allocated to a team. Two balances are still tracked. The largest listed-company LTC holder reports **819,070 LTC** and has been selling some to fund share buybacks; those Litecoin coins were bought on the open market and sat inside the circulating count the whole time, so a sale moves them between holders without adding supply, and the framework did not credit a buy row when they were bought. Second, **85,034 LTC** has been frozen inside MWEB since **Mar 25 2026**, when coins taken through a validation bug were returned and locked by consensus; they cannot move. Exchange wallets and unlabelled large holders are excluded by rule. Both tracked balances are re-read on every refresh, and if either falls in a way that puts new LTC into circulation, the outflow enters Sell #3 at the next refresh.

## How LTC compares to other capped proof-of-work coins

Litecoin belongs to the halving-model class: a fixed per-block reward, a hard cap, and a schedule that cuts issuance in half on a block count rather than a calendar. With about **92.4%** of the 84M LTC cap already mined, Litecoin's supply growth is modest and shrinking in steps, the same shape as the larger capped chains. Against uncapped proof-of-stake Layer 1s, Litecoin issues far less as a share of supply, and its issuance cannot be raised by a governance vote; against coins with a tail emission, Litecoin's reward eventually goes to zero. What Litecoin lacks is anything on the other side of the ledger. Chains that burn part of every fee can offset some issuance; Litecoin pays all fees to miners, so every mined LTC stays in the float.

The fee base shows why a burn would change little here. Litecoin fees run about **$161K** a year against a market capitalisation near **$4.16B**, roughly **0.004%** — among the quiet chains, where fees are a rounding error next to the block reward. Litecoin miners are paid almost entirely in new LTC, which is exactly the sell pressure this ledger measures.

## What to watch in the next 90 days

First, the LitVM smart-contract layer, targeted for mainnet in Q4 2026: its bridge locks LTC on the Litecoin base layer, and if it launches with a real locked balance, that could become the first non-zero Buy #4 on this page. Second, block speed: Litecoin issuance tracks blocks, not days, so a sustained hashrate move changes the next-90-day figure directly. Third, the Litecoin trust that filed on **Sep 11 2026** to convert into an exchange-traded fund; a fund buys LTC on the market, so it adds no supply either way. Fourth, further MWEB validation releases after the public upgrade of **Sep 12 2026** — none so far has changed the reward, and any that did would re-base the forward column. The halving at block **3,360,000** stays outside this window, around late **Jul 2027**.

## Summary

The MrNasdog Pressure Framework reads Litecoin (LTC) at **+0.42% net** over the trailing 90 days and **+0.42%** over the next 90. The structural mechanism is a fixed **6.25 LTC** proof-of-work block reward — **322,906 LTC** across **51,665** measured blocks — with no burn, no buyback and no lock on the other side. The key risk is simply that nothing ever offsets Litecoin issuance, so the float grows every block until the next halving cuts the reward to 3.125 LTC around late Jul 2027. The ceiling is the **84M LTC** hard cap, of which about **6.4M LTC** is still to be mined.

---

*MrNasdog Pressure Framework analysis of LTC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 13 2026.*

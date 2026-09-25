---
title:         "LTC Inflation Analysis · September 2026 · Mixed flows, supply roughly steady"
description:   "Mixed flows, supply roughly steady: Litecoin mined 323,693.75 LTC over 51,791 blocks in 90 days, with no buyback and no burn. Net +0.42%, monitor +0.22%."
canonical_url: "https://mrnasdog.com/research/ltc/inflation"
tags:          ["crypto", "ltc", "litecoin", "pow"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/ltc/inflation](https://mrnasdog.com/research/ltc/inflation)*

# LTC Inflation Analysis · September 2026 · Mixed flows, supply roughly steady

LTC, the coin mined on the Litecoin proof-of-work chain, gets all of its new supply from one place: the block reward, a fixed **6.25 LTC** per block under an **84M** cap. Over the last 90 days **51,791** Litecoin blocks were mined, adding **323,693.75 LTC**, while nothing on the buy side took a single LTC back — no buyback, no fee burn, no staking lock. The MrNasdog Pressure Framework therefore reads LTC at **+0.42% net** over the last 90 days against a supply-monitor reading of **+0.22%**, a gap of **0.20 percentage points**. Litecoin supply grows slowly and on a known schedule toward its cap, with about **92%** already mined and the next halving around **late July 2027**.

## The verdict, in one paragraph

For the 90-day window ending **Sep 24 2026**, the Pressure Framework reads **LTC at +0.42% net**: the sell side added **323,693.75 LTC** of mined coins against a circulating supply of **77.64M LTC**, and the buy side removed **zero**. The independent supply monitor reads the realised 90-day change at **+0.22%**. The gap is **0.20 percentage points**, inside the framework's half-point tolerance, so LTC ships with **no data-conflict flag**; the monitor divides market value by price each day, and that read carries more noise than a block count. The forward column also reads **+0.42%** — **323,695 LTC** at the pace the chain actually kept — because no halving and no other supply event falls in the next 90 days. The label for LTC is **slowly inflationary on a fixed mining schedule**: a capped proof-of-work coin whose float grows by the block reward and by nothing else.

## Sell pressure: where new LTC comes from

All of it comes from mining. Sell #1, protocol inflation, is **323,693.75 LTC** over the window: every Litecoin block pays its miner a fixed **6.25 LTC** subsidy, and the framework counted the **51,791** blocks between Jun 26 2026 and Sep 24 2026 rather than assuming a block count, then checked the total two further ways — the reward paid across exactly those blocks, less their fees, came back to **6.25 LTC** a block to the ten-thousandth of a coin. The Litecoin subsidy halves every **840,000** blocks; the last halving was in Aug 2023 and the next falls at block **3,360,000**, about **176,000** blocks away, which puts it around **late July 2027** — well outside the next 90 days.

The block count deserves a sentence, because it is where a proof-of-work reading usually goes wrong. Litecoin targets one block every **150 seconds**, or **576** a day, which would have produced **51,840** blocks in 90 days. The chain actually produced **51,791** — an average of **150.14 seconds** per block, a touch slow — so the target would have over-stated the window by about **306 LTC**. Unlike a chain whose difficulty rule steers back to a fixed clock, Litecoin resets difficulty every **2,016** blocks from the pace of the previous stretch alone and never makes up lost time, so a slow run stays slow in the supply record. Over the past year Litecoin averaged **150.30 seconds**, and nothing changed the mechanism in this window, so the next-90-day column holds the measured pace: **323,695 LTC**.

Sell #2, vesting unlocks, is **zero** because nothing was ever allocated: Litecoin launched in **Oct 2011** with no premine, no token sale and no team or investor share, and the LTC in existence matches the mining schedule alone. Sell #3, foundation and unscheduled unlocks, is **zero**: the Litecoin Foundation runs on donations, no Litecoin wallet was ever funded from supply, and every block pays its full reward and all its fees to the miner. Sell #4, long-term locked or bankruptcy supply, is also **zero**: no estate distributes LTC on a schedule and no long-dated lock is unwinding. A listed company holds about **819,070 LTC** and has sold part of its holding to buy back its own shares, but circulating and total LTC differ by only about **2,800 LTC**, so those coins were already inside the counted float and a sale moves them between holders without adding any.

## Buy pressure: where new LTC goes

Nowhere, and that is the whole story of the Litecoin buy side. Buy #1, programmatic buyback, is **zero**: Litecoin has no protocol revenue pot, no treasury and no programme that takes LTC off the market. Buy #2, the protocol fee burn, is **zero**: Litecoin burns no part of its fees, and every fee goes to the miner together with the block reward. The framework read both burn surfaces rather than assuming: the supply record rose by exactly the mined amount, and the best-known keyless Litecoin burn address received nothing in the window.

Buy #3, foundation buying, is **zero** because there is no project treasury to buy with; funds and companies that hold LTC buy it with their own money on the open market, which moves coins between holders inside the float. Buy #4, new long-term locks, is **zero**: proof-of-work has no staking, bonding or lockup, and no new lock with a stated size appeared this window. Litecoin's private-send layer, MWEB, deserves a line here because large sums move through it — the balance held there rose from about **334,500 LTC** to **457,200 LTC** across the window, peaking above **563,000 LTC** in mid-September. Those coins stay spendable and stay counted in supply, so moving LTC in or out of MWEB is a transfer between two layers of the same chain, never a mint and never a lock.

## Foundation and overhang

Litecoin has no team-controlled reserve to name. There is no foundation allocation, no DAO treasury, no unscheduled supply bucket and no buyback wallet, because none of those were ever created. The gap between total and circulating LTC is about **2,800 LTC** — less than half a day of mining — so there is no non-circulating bucket anywhere for coins to leave. Two balances are watched anyway. The first is a frozen recovery balance of **85,034 LTC** inside MWEB, left from a Mar 2026 incident in which a validation bug let an attacker fake a withdrawal; the coins were recovered, pegged back and frozen, and they cannot move. The second is the listed company's **819,070 LTC**, re-read at each refresh from its own filings. Exchange custody, spot funds and unlabelled large holders are excluded by rule. If either watched balance falls between refreshes and the coins turn out to have come from outside the counted float, the outflow enters Sell #3 at the next refresh.

## How LTC compares to other proof-of-work coins

LTC belongs to the family of capped proof-of-work coins built on Bitcoin's monetary design, and against that family its supply shape is a scaled copy. Litecoin runs four times Bitcoin's block speed with four times Bitcoin's cap — **84M** against **21M** — and halves every **840,000** blocks, which lands on roughly the same four-year rhythm. Both issue on a falling curve toward a hard ceiling, so their quarterly growth drops by half at each halving and never turns negative. Against Dogecoin the contrast is the cap: Dogecoin mints a fixed amount every block forever, so its supply never stops growing, while Litecoin's issuance heads toward zero.

Against proof-of-stake chains, the contrast is on the buy side. Many proof-of-stake chains pay validators in new coins and burn part of every fee, so their float can shrink in busy periods; Litecoin has neither a staking reward nor a fee burn, so its net reading is simply its mining rate. Fees play no part in Litecoin supply: they neither burn LTC nor replace the block reward. The one feature no other coin in this family carries is MWEB, a built-in private-send layer that moves value between two views of the same ledger — and because every pegged coin stays counted, it changes who can see a balance, not how many LTC exist.

## What to watch in the next 90 days

First, hash power: the forward reading assumes Litecoin keeps its measured pace of **150.14 seconds** a block, and a sustained move of one second in either direction would shift the booked **323,695 LTC** by roughly **2,100 LTC**. Second, the Grayscale Litecoin Trust, which held **1,969,057 LTC** on Jun 30 2026 and filed on Sep 11 2026 to become a listed spot fund; any conversion is an access wrapper for coins already in the float and moves no new supply. Third, the listed treasury's next filing, which will update its **819,070 LTC**. Fourth, MWEB: Litecoin Core shipped validation-only soft forks on Aug 2 2026 and Sep 12 2026, and any future change that touched how coins enter or leave MWEB would be read against the supply record at the next refresh. Fifth, LitVM, a separate smart-contract layer targeting a Q4 2026 mainnet: if its bridge locks LTC with a stated size, that lock is tested for Buy #4.

## Summary

The MrNasdog Pressure Framework reads LTC at **+0.42% net** over the trailing 90 days and **+0.42%** over the next 90, with a buy side that is zero across all four canonical rows. The structural mechanism is a capped proof-of-work coin whose only source of new LTC is a fixed **6.25 LTC** block reward, measured this window at **51,791** blocks and **323,693.75 LTC**. The key risk to the reading is the block pace, which Litecoin's difficulty rule never pulls back to a fixed clock, so drift in hash power flows straight into issuance. The ceiling is the **84M** cap, about **92%** already mined, and the halving around **late July 2027** cuts the block reward to **3.125 LTC**.

*MrNasdog Pressure Framework analysis of LTC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 25 2026.*

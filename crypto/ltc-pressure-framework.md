---
title:         "LTC Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description:   "LTC supply grows slowly: 322,794 LTC of mining rewards in 90 days, almost no burn and no buyback, +0.42% net, the same next. 84M cap; halving July 2027."
canonical_url: "https://mrnasdog.com/research/ltc/inflation"
tags:          ["crypto", "ltc", "litecoin", "pow"]
published:     true
---
*Originally published at [https://mrnasdog.com/research/ltc/inflation](https://mrnasdog.com/research/ltc/inflation)*

<!-- main-page -->
The Litecoin coin page has the score, the price drivers and every question answered — [mrnasdog.com/research/ltc](https://mrnasdog.com/research/ltc). Below: supply, line by line.

# LTC Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

**Litecoin (LTC)** grows its supply slowly and on a fixed timetable. In the 90 days to Oct 12 2026, miners were paid **322,794 new LTC** through the block reward, while only **5.59 LTC** was destroyed, so net supply rose about **+0.42%**. Our monitor reads **+0.41%**, the same picture. Litecoin has no premine, no vesting, no buyback and no fee burn, and its supply can never pass the **84M LTC** cap.

## The verdict, in one paragraph

Over the last 90 days, Litecoin supply grew by a net **+0.42%** of the **77.71M LTC** in circulation, and the next 90 days should add the same **+0.42%**. The monitor measured **+0.41%** over the same kind of window, a gap of **less than 0.01 percentage points**, well inside our 0.5-point limit, so no warning chip is needed. All of the new supply is the Litecoin block reward, and almost nothing leaves. Litecoin is a **quiet, capped proof-of-work chain that inflates by its mining schedule and nothing else**.

## Sell pressure: where new LTC comes from

**Protocol inflation is the only source: 322,794 LTC in 90 days.** Every Litecoin block pays its miner **6.25 new LTC**, a reward that has held since the August 2023 halving. Between Jul 14 and Oct 12 2026 miners found **51,647 blocks**, one every 150.6 seconds on average against the 150-second target, which works out to about **3,587 new LTC a day**. We counted the blocks at both ends of the window and checked the coinbase payouts, and two separate supply records agree to within one LTC. Because the blocks ran very slightly slow, the next 90 days should bring about **322,809 LTC** — practically the same amount. Miners usually sell part of this pay to cover power and machines, which makes it real sell pressure.

**Vesting unlocks are zero.** Charlie Lee launched Litecoin in October 2011 with no premine and no share for a team or investors. Every LTC in existence was mined, so there is no unlock calendar, and circulating supply equals total supply.

**Foundation and unscheduled unlocks are zero.** The Litecoin Foundation is a non-profit funded by donations; the protocol never gave it coins, and we found no sign of it releasing LTC in this window.

**Long-term locked or bankruptcy supply is zero.** No court estate or trustee is paying out LTC. The Litecoin held by US funds and by the Grayscale Litecoin Trust was bought in the open market, so it was already part of the circulating float.

## Buy pressure: where new LTC goes

**Programmatic buyback: zero.** Nothing in Litecoin buys LTC back. Transaction fees go to miners, and the listed Litecoin treasury company buys back its own shares, not LTC.

**Protocol fee burn: zero.** Unlike chains with a base-fee burn, Litecoin destroys no part of its fees. Fees are tiny — about 0.01 LTC per block in the last 1,000 blocks — and miners keep all of them. An old public burn address holds just 0.18 LTC and has received nothing since April 2026.

**Foundation buy: zero.** We found no Litecoin Foundation purchase and no project treasury buying LTC in the window.

**New long-term lock: zero.** Litecoin has no staking. Its private MWEB pool grew from about **356.4K** to **465.5K LTC** in these 90 days, a sign that more people use the privacy layer, but coins there can move back at any time and still count as circulating.

**Coins sent to unspendable outputs: 5.59 LTC.** Some users attach small amounts of LTC to data-only outputs that can never be spent. In this window **376** such outputs destroyed **5.59 LTC**, and supply rose by exactly that much less than miners were paid. It is real, but it is less than one block of mining pay over three months.

## Foundation and overhang

Litecoin has no team-controlled supply waiting to unlock. The Litecoin Foundation publishes no LTC balance and never received a protocol allocation; we check its news by hand every rebuild. One pot is frozen by the protocol itself: after the March 2026 MWEB bug, developers put **85,034 LTC** back into the MWEB pool in an output that cannot be spent, so the pool stayed balanced and no coins were created. We re-check that output with each Litecoin Core release.

The largest company holder is a listed Litecoin treasury firm, which reported **819,070 LTC** on Jul 17 2026 and has sold some LTC to pay for buying back its own shares. Those coins were bought in the market, so a sale moves coins from one holder to another and adds nothing new; we watch its filings each quarter. If any of these balances falls between our checks and the coins come from outside the float, the outflow enters Sell #3 at the next refresh.

## How LTC compares to other proof-of-work chains

Litecoin copies the Bitcoin design with four times as many coins and four times faster blocks: a hard cap (**84M LTC** against 21M BTC) and a reward that halves every four years. Litecoin's last halving was in August 2023 and Bitcoin's in April 2024, so right now Litecoin issues a larger share of its supply — about **0.42%** every 90 days, roughly double Bitcoin's pace. After the next Litecoin halving at block 3,360,000, expected around late July 2027, the reward drops to **3.125 LTC** and the rate falls to about half.

Dogecoin, which is mined together with Litecoin through merged mining, works the other way: it pays a fixed 10,000 DOGE per block forever, with no cap and no halving. Monero also keeps a small fixed tail reward after its main emission ended. Litecoin has neither — its block reward keeps halving until new supply is close to zero, and fees alone will one day have to pay miners.

Compared with proof-of-stake chains such as Ethereum, Litecoin has no staking pot that grows with participation and no fee burn that can offset issuance in busy months. Its supply path is set by block height, not by usage, which makes it one of the easiest coins in our catalog to forecast.

## What to watch in the next 90 days

**Block speed.** Litecoin pays per block, so if hash power jumps and blocks come faster than every 150 seconds before the next difficulty adjustment, issuance runs slightly above 322,809 LTC; slower blocks do the opposite.

**The Grayscale ETF conversion.** Grayscale filed on Sep 11 2026 to turn its Litecoin Trust into an exchange-listed fund. A decision would change who buys LTC, but not how many coins are made.

**The treasury company's next report.** Its next quarterly filing will show whether it kept selling LTC to fund share buybacks — flows inside the float that matter for demand, not for supply.

**MWEB releases.** Any new Litecoin Core release that touches the frozen 85,034 LTC output or the MWEB rules would be checked against supply on the next rebuild.

**The halving countdown.** Block 3,360,000 is about 290 days away, outside this window; the next 90 days still pay 6.25 LTC per block.

## Summary

Litecoin (LTC) is mildly inflationary on a fixed schedule: miners received **322,794 LTC** in the 90 days to Oct 12 2026, almost none was removed, and net supply rose **+0.42%**, in line with the monitor's **+0.41%**. There is no premine, no vesting, no buyback and no fee burn, so the only lever is the block reward. The main risk is steady miner selling of about 3,587 new LTC a day, with no burn to offset it. The ceiling is hard: supply cannot pass **84M LTC**, and the reward halves to 3.125 LTC around late July 2027.

*MrNasdog Pressure Framework analysis of LTC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 12 2026.*

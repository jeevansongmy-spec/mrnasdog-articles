---
title:         "XMR Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description:   "XMR supply grows slowly: a fixed 0.6 XMR per block made 38,812 new XMR in 90 days, +0.21% net, with no burn, no vesting and no cap. Same pace expected."
canonical_url: "https://mrnasdog.com/research/xmr/inflation"
tags:          ["crypto", "xmr", "monero", "privacy"]
published:     true
---
*Originally published at [https://mrnasdog.com/research/xmr/inflation](https://mrnasdog.com/research/xmr/inflation)*

<!-- main-page -->
Looking for the buy-or-sell answer? It is on the XMR coin page, with demand and price drivers: [mrnasdog.com/research/xmr](https://mrnasdog.com/research/xmr)

# XMR Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

Monero (XMR) is mildly inflationary and fully predictable: the protocol pays miners a fixed **0.6 XMR** per block, which created **38,812 XMR** between Jul 13 2026 and Oct 11 2026, while nothing at all removed XMR from supply. That is **+0.21%** of the **18.82M XMR** in circulation over 90 days, the same rate is expected for the next 90 days, and our independent monitor reads **+0.21%** too. Monero has no supply cap, but its tail emission is a flat number of coins, so the yearly rate keeps falling slowly as supply grows.

## The verdict, in one paragraph

Over the last 90 days the MrNasdog Pressure Framework counts **38,812 XMR** of new supply and **0 XMR** removed, a net change of **+0.21%** of circulating supply. The monitor, which measures the same window from market data, reads **+0.21%** (exactly +0.2084% against our +0.2063%), a gap of **0.002 percentage points**, far inside our 0.5-point tolerance, so no warning chip is shown. The next 90 days project the same **+0.21%**, because the Monero block reward does not change and no mainnet upgrade is scheduled. Put simply: Monero is a quiet tail-emission chain, inflationary by a small, fixed amount, with no unlocks and no burn.

## Sell pressure: where new XMR comes from

Protocol inflation is the only source of new Monero. Since 2022 the block reward has sat on its permanent floor, the tail emission of **0.6 XMR** per block, with no end date. In the 90-day window the Monero chain produced **64,689 blocks**, one every 120.2 seconds on average, slightly slower than the 2-minute target. Because the reward is paid per block and nothing in the protocol corrects for a slow chain, we count real blocks rather than the 64,800 the target implies: 64,689 × 0.6 gives 38,813.4 XMR.

One small detail lowers that figure. A Monero block heavier than the recent median earns a reduced reward, and the coins it gives up are simply never created. In this window **4,772 blocks** were heavier than the 300,000-unit median, the largest at 456,144, and together they gave up about **1 XMR**. That leaves **38,812 XMR** of protocol inflation, about 431 XMR a day. Miners also collected about 685 XMR in transaction fees, but fees are existing coins changing hands, not new supply.

Vesting unlocks are **zero**. Monero launched in April 2014 with no premine, no token sale and no team or investor allocation, so there is no vesting calendar and no cliff. Foundation and unscheduled unlocks are also **zero**: there is no foundation treasury holding coins outside the float. Long-term locked or bankruptcy supply is **zero** too: no court estate, trustee or long lock is releasing Monero.

## Buy pressure: where new XMR goes

Nothing on the buy side removes Monero from supply. There is no programmatic buyback, because there is no company, treasury or fee share behind XMR that could buy coins back. The protocol fee burn is **zero**: every fee goes to the miner who includes the transaction, and Monero's total supply rose by exactly the newly mined coins, which confirms that nothing was destroyed. Because Monero hides amounts, there is no public burn address to read, and the supply total is the only surface that can show a burn; it showed none.

Foundation buying is **zero**, since no team or treasury buys XMR on the market. New long-term locks are **zero** as well: Monero is a proof-of-work chain, so there is no staking and no reward lock that pulls coins out of circulation. Buy pressure for Monero therefore comes only from ordinary buyers, never from the protocol itself.

## Foundation and overhang

Monero has almost no overhang to watch. Circulating supply (**18,816,184 XMR**) and total supply (**18,816,191 XMR**) differ by only about 7 XMR, so no wallet of any size sits outside the counted float. The one group-controlled pot is the Monero community fund, which collects donations and pays developers when a funded task is delivered. Its balance is private and not published, so we cannot read it on-chain, but it is already part of the float: a payout moves existing coins from one holder to another and adds no new supply. We re-check the fund by hand at every rebuild. If a group wallet outside the float ever appears and its balance falls between our checks, that outflow would enter the foundation and unscheduled unlock line at the next refresh.

## How XMR compares to other proof-of-work chains

Monero and Bitcoin end up in a similar place today by very different roads. Bitcoin pays 3.125 BTC per block and halves that reward every four years toward a hard 21M cap, and its supply also grows about 0.2% every 90 days right now. The difference is the future: Bitcoin's new supply keeps halving toward zero, while Monero's **0.6 XMR** per block never stops. Monero chose a permanent tail emission so miners are always paid by the protocol and not by fees alone, and the cost is a small, endless inflation.

Against Zcash, the other large privacy coin, the mechanisms differ again. Zcash copies Bitcoin's halving model and 21M cap, and part of each Zcash block reward has gone to development funds, while Monero has no development tax at all: every new XMR goes to the miner who found the block. Dogecoin is the closest match in shape, since it also pays a fixed reward per block forever with no cap, but its 10,000 DOGE per one-minute block is a much larger share of its supply each year than Monero's 0.6 XMR per two-minute block.

Compared with proof-of-stake chains, Monero has no staking rewards, no unlock calendar and no fee burn. Its supply story fits in one line: about **0.84%** new coins a year at today's pace, shrinking slowly as a share of supply, and nothing else.

## What to watch in the next 90 days

First, the FCMP++ upgrade: its third test network forked on Oct 5 2026, but no mainnet date is set. The upgrade is about privacy, not supply, so we expect the 0.6 XMR reward to stay; we will re-check the release notes when a mainnet date appears. Second, block size: if blocks keep growing past the median, the reward penalty grows, though today it costs only about 1 XMR every 90 days. Third, the block pace: a slower or faster chain changes the count of new XMR by the same share, and we measure real blocks at every rebuild. Fourth, exchange access: from Jul 10 2027, EU rules bar regulated crypto firms from handling privacy coins, which matters for who can buy XMR but does not change its supply. Our next full re-check is expected around Jan 9 2027 at the latest.

## Summary

Monero (XMR) grew its supply by **+0.21%** over the 90 days to Oct 11 2026, from a fixed tail emission of **0.6 XMR** per block that created **38,812 XMR**, with nothing burned, bought back or locked, and the monitor agrees at **+0.21%**. There are no unlocks, no team allocation and no treasury outside the float, so the only supply risk is the steady mining reward itself. Monero has no cap, but because the reward is a flat number of coins, its yearly inflation rate keeps falling slowly, from about 0.84% today.

*MrNasdog Pressure Framework analysis of XMR, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 11 2026.*

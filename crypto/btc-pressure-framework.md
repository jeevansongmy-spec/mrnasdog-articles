---
title:         "BTC Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "BTC supply is roughly steady: mining made 40,447 BTC in 90 days at 3.125 per block, with no burn and no buyback. Net +0.20%, the same next, under a 21M cap."
canonical_url: "https://mrnasdog.com/research/btc/inflation"
tags:          ["crypto", "btc", "bitcoin", "proof-of-work"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/btc/inflation](https://mrnasdog.com/research/btc/inflation)*

# BTC Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

Bitcoin's supply is growing slowly and on a fixed path. In the 90 days to Sep 30 2026, miners created **40,447 BTC** from **12,943 blocks** at **3.125 BTC** each, and nothing took any BTC out of the market: no burn, no buyback, no lock. That puts net supply growth at **+0.20%** over 90 days, with the same **+0.20%** expected for the next 90 days, under a hard cap of **21 million BTC**.

## The verdict, in one paragraph

The MrNasdog Pressure Framework reads Bitcoin at **+0.20%** net supply growth over the last 90 days: **40,447 BTC** of new coins against a **20.09M BTC** circulating supply, and **0 BTC** removed. Our independent supply monitor reads **+0.21%** for the same window, a gap of **0.004 percentage points** — far inside our 0.5-point tolerance, so no warning chip is shown. The forward reading for the next 90 days is also **+0.20%**, because the block reward stays at 3.125 BTC until the next halving in 2028. In one line: Bitcoin is a slow, fixed-issuance chain with an empty buy side — mildly inflationary, and becoming less so with every halving.

## Sell pressure: where new BTC comes from

**Protocol inflation — 40,447 BTC.** The only source of new BTC is the block subsidy paid to miners. Since the April 2024 halving at block 840,000, every Bitcoin block creates **3.125 BTC**. We counted the blocks directly: the last block before the window was 956,362 and the chain tip on Sep 30 2026 was 969,305, so **12,943 blocks** were mined — about **144 a day**, with an average gap of 600.8 seconds, just over the ten-minute target. At 3.125 BTC each, that is **40,446.9 BTC**. A second count, taken from a per-block record of total Bitcoin supply, agrees to within 0.1%.

Because Bitcoin pays its reward per block, not per day, block speed matters. Difficulty adjusts every 2,016 blocks to pull the pace back toward one block every ten minutes, so the count moves only a little from one quarter to the next. We carry the measured count of 12,943 blocks into the next 90 days.

**Vesting unlocks — 0.** Bitcoin has never had a vesting schedule. There was no premine, no token sale and no team or investor allocation when Satoshi Nakamoto mined the genesis block on Jan 3 2009. Every BTC in existence was mined, so there is no locked bucket that could open.

**Foundation and unscheduled unlocks — 0.** Bitcoin has no foundation, no company treasury and no reserve waiting to be released. Circulating supply and total supply are the same number, **20,090,909 BTC**, so no coins sit outside the market count. The big holders people talk about — a listed company with about **845,050 BTC**, the US government with about **198,000 BTC** from seizures, and the spot Bitcoin funds — all hold coins that are already counted. When they sell, coins change hands; supply does not grow.

**Long-term locked or bankruptcy — 0.** The Mt. Gox estate still holds about **34,500 BTC**, and the trustee's deadline to repay creditors is **Oct 31 2026**. Those coins were mined more than a decade ago and are already inside the circulating count, so a payout adds nothing to Bitcoin supply. It can still add selling, because some creditors will sell what they receive.

## Buy pressure: where new BTC goes

**Programmatic buyback — 0.** No contract, fund or treasury buys BTC and takes it out of the market. Spot funds, companies and governments buy Bitcoin all the time, but the coins they buy stay in the circulating count, so the buying does not shrink supply.

**Protocol fee burn — 0.** Bitcoin does not burn transaction fees. Every fee goes to the miner who finds the block, on top of the 3.125 BTC subsidy. Some people send BTC to addresses no one can spend from; we read the two best-known ones across the window and they received about **0.0013 BTC** in all — too small to change the reading.

**Foundation buy — 0.** With no foundation or treasury, there is no one buying BTC on behalf of the network, and we found no such buying this window.

**New long-term lock — 0.** Bitcoin has no staking and no lock-up contract. A US bill that cleared a House committee **28–21** on **Sep 16 2026** would make the government hold its seized BTC for at least 20 years. Even if it becomes law, those coins stay in the circulating count, so a lock like that removes nothing from the reading.

## Foundation and overhang

Bitcoin has no team-controlled overhang. There is no foundation wallet, no treasury, no DAO and no unreleased reserve — circulating supply equals total supply, so every coin is already in the market count. We still track the balances that could bring selling: the Mt. Gox estate at about **34,500 BTC** with a repayment deadline of Oct 31 2026, government seizure wallets such as the US holding of about **198,000 BTC**, the largest corporate holder at about **845,050 BTC**, and the dormant early-mined coins linked to Bitcoin's first year. We re-check the gap between total and circulating supply at every refresh. If a bucket of coins outside the circulating count ever appears and then shrinks between refreshes, that outflow enters the foundation-and-unscheduled row at the next refresh.

## How BTC compares to other proof-of-work chains

Bitcoin is the reference case for a halving model with a hard cap. About **95.7%** of all **21 million BTC** is already mined, and each halving cuts the new-coin flow in half again. Litecoin follows the same design with a larger 84 million cap and a shorter block time; Bitcoin Cash shares Bitcoin's schedule exactly. Against those chains, Bitcoin's current +0.20% per 90 days is low, and its path is known years ahead.

Proof-of-work chains with tail emission take a different path. Monero pays a fixed 0.6 XMR per block forever, so its supply never stops growing, though the rate shrinks as a share of supply. Dogecoin adds a fixed 10,000 DOGE per block with no cap at all. Bitcoin has no tail: after the last halvings the subsidy falls toward zero, and miners are paid by fees alone.

Compared with proof-of-stake chains, the big difference is the buy side. Ethereum burns part of every fee, and many newer chains burn fees or buy back tokens. Bitcoin does neither: its only supply control is the halving schedule. That makes its sell side small and predictable, and its buy side always empty — any change in BTC supply comes only from mining.

## What to watch in the next 90 days

**Oct 31 2026 — Mt. Gox repayment deadline.** The estate holds about 34,500 BTC. A payout does not change supply, but it puts coins in the hands of creditors who may sell, and the trustee could extend the deadline again.

**The US reserve bill.** The bill that cleared committee on Sep 16 2026 still needs a full House vote, the Senate and a signature. A separate bill to buy **1 million BTC** over five years has not had a hearing. Either one would change who holds BTC, not how much exists.

**BIP-361, the quantum freeze idea.** A draft proposal would, in stages, stop coins in older address types from moving once quantum computers become a real threat. It is not merged or scheduled, but if it moved forward it would be the first Bitcoin change to touch coins that already exist.

**Block pace and difficulty.** The 3.125 BTC reward holds until block 1,050,000, about Apr 2028. Faster or slower blocks move the 90-day count by a few hundred BTC at most.

## Summary

Bitcoin's supply grew **+0.20%** in the 90 days to Sep 30 2026 — **40,447 BTC** from mining and nothing removed — and the framework expects the same **+0.20%** over the next 90 days. The only source of new BTC is the block subsidy of 3.125 BTC, fixed until the next halving at block 1,050,000 around Apr 2028. The key risk to watch is selling, not new supply: large existing holders such as the Mt. Gox estate can move coins that are already counted. With **95.7%** of the **21 million** cap already mined, Bitcoin's new supply only gets smaller from here.

---

*MrNasdog Pressure Framework analysis of BTC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 30 2026.*

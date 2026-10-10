---
title:         "SOL Inflation Analysis · October 2026 · Supply growing · projected to keep growing"
description:   "SOL supply is growing: 5.17M SOL of staking issuance plus 4.88M SOL from ended locks, against a 139K burn and new locks, give +1.68% in 90 days; +1.26% next."
canonical_url: "https://mrnasdog.com/research/sol/inflation"
tags:          ["crypto", "sol", "solana", "layer1"]
published:     true
---
# SOL Inflation Analysis · October 2026 · Supply growing · projected to keep growing

*Originally published at [mrnasdog.com/research/sol/inflation](https://mrnasdog.com/research/sol/inflation).*

<!-- main-page -->
This is the long supply read. For the signal, the price drivers and the questions people ask about Solana, see [mrnasdog.com/research/sol](https://mrnasdog.com/research/sol).

**SOL supply is growing.** In the 90 days to Oct 10 2026, Solana paid **5.17M SOL** of new staking rewards into the market and **4.88M SOL** more left locked accounts, while the fee burn and new locks took out only **139K SOL**. That is **+1.68%** of the **588.79M SOL** in circulation, and the next 90 days project **+1.26%**. Solana has no supply cap: its inflation rate is 3.61% a year and falls 15% a year toward a 1.5% floor.

## The verdict, in one paragraph

Over the last 90 days SOL supply on the market grew **+1.68%** on our ledger. The supply monitor we check against reads **+1.12%**, a gap of **0.56 percentage points**, which is above our 0.5-point line, so the page carries a warning chip. We walked the gap: the supply figure the monitor reads fell 3.62M SOL in a single day on Jul 29 2026 and never came back, and we found no lock, burn or move of that size on the Solana chain that day. Put that step back and the monitor shows about +1.74%, close to our number, so our number stays. For the next 90 days we project **+1.26%**. In one line: **Solana is inflationary by design, with staking rewards plus a steady stream of lock expiries.**

## Sell pressure: where new SOL comes from

**Protocol inflation is the largest source: 5.17M SOL.** At the end of every epoch Solana mints new SOL and pays it to stake accounts and validators. The rate is set by a fixed curve — it started at 8%, falls 15% a year and stops at 1.5% — and it sits at 3.61% today. In this window 52 epochs paid 5.38M SOL; 216K of that went to accounts that do not count as circulating, so 5.17M SOL reached the market. Solana also cut its block time four times in these 90 days, from 400 milliseconds to 350, 300, 250 and finally 200 milliseconds on Oct 9 2026. Each cut shortened the epoch, and the reward per epoch was cut by the same ratio, so the pace of new SOL per day did not jump. For the next 90 days we project **4.66M SOL**, because the rate keeps falling and the faster chain still runs a little slower than its target.

**Vesting unlocks added 3.78M SOL.** About 15M SOL sits in Solana stake accounts with a lock that ends on a set date, mostly from earlier private sales. A coin joins the circulating supply on the day its lock ends. The biggest stream is a monthly release of about 639K SOL on the 7th of every month (Aug 7, Sep 7, Oct 7 in this window); one-off dates added 625K on Aug 1 and 875K on Aug 30. The next 90 days hold about **2.25M SOL** of lock expiries: 638K on Nov 7, 640K on Dec 7 and 637K on Jan 7 2027, plus smaller ones.

**Foundation and unscheduled unlocks added 692.8K SOL.** On Aug 26 2026 the Solana Foundation split 587,871 SOL out of one of its stake accounts and handed it to an outside owner, so it left the reserve and joined the market. Other listed reserve keys withdrew about 105K SOL, including two payouts of 49,250 SOL on Oct 4 2026. These moves have no schedule, so the forward figure is 0.

**The bankruptcy row added 404.4K SOL.** The FTX/Alameda estate still holds 2.44M SOL in locked stake accounts that open on the 11th of each month until Sep 2027. It withdrew 201,741 SOL on Aug 11 and 202,708 SOL on Sep 12 2026. Three more releases of about 203K SOL fall in the next 90 days, **609.8K SOL** in total.

## Buy pressure: where new SOL goes

**There is no buyback.** No contract or treasury buys SOL back. Companies and funds buy SOL on the open market, which moves coins between holders without taking any out of supply. A founder's idea from Aug 15 2026 — mint SOL to buy a company and burn its income — never became a proposal.

**The fee burn removed 79.06K SOL.** Every signature pays a base fee of 5,000 lamports, and half of it is destroyed; validator votes pay it too. Priority fees go to the block maker in full and are not burned. Counted block by block across 22.8M blocks, the burn came to 79,058 SOL, about 880 SOL a day — less than one sixtieth of the new staking rewards. Faster blocks mean more votes per day, so we project about **99.8K SOL** for the next 90 days. In Aug 2026 a governance vote to change the fee design and burn far more did not reach the needed majority.

**Foundation buys: 0.** We found no Foundation or project buying of SOL. **New long-term locks took 59.54K SOL off the market:** 78 new locked stake accounts were opened in the window, and 59,539 SOL of their deposits came from ordinary wallets. Staking itself is not a lock here — 437.9M SOL is staked, but staked SOL can be withdrawn and still counts as circulating. We project no new locks, as none is announced.

## Foundation and overhang

About **46.74M SOL**, 7.4% of the 635.54M total, does not count as circulating. The largest part is the Solana Foundation's own stake, about 27.2M SOL held under one key with no lock date, plus about 2.2M SOL in other listed reserve accounts. These coins have no release schedule. Next come the dated locks: about 15M SOL of private-sale stake accounts opening monthly into early 2028, and the FTX/Alameda estate's 2.44M SOL opening on the 11th of each month until Sep 2027. We read every one of these accounts on-chain at each rebuild. If any of these balances falls between rebuilds, the outflow enters the Foundation row (Sell #3) at the next rebuild.

## How SOL compares to other proof-of-stake Layer 1s

Solana and Ethereum both pay stakers in new coins and burn part of each fee, but the two designs set issuance differently. Ethereum's issuance follows the amount staked and has no time schedule; Solana's follows a calendar curve that falls 15% a year to a 1.5% floor. Solana's burn is also far smaller relative to its issuance, because only half of a small base fee is destroyed, while priority fees — most of what users pay — go to the block maker. So Solana supply grows close to its headline inflation rate, while Ethereum's net growth depends on how busy blocks are.

Compared with chains that still carry large team or investor vesting, Solana's genesis allocations have long been unlocked; what remains is a tail of locked stake from private sales and the FTX estate. That tail adds roughly 0.8M to 0.9M SOL a month, smaller than staking rewards but not small. Compared with fixed-cap coins such as Bitcoin, Solana has no cap at all: supply keeps growing at the floor rate forever once the curve bottoms out.

Solana validators approved a faster fall in the inflation rate on Aug 28 2026 (the yearly cut doubles from 15% to 30%). It is not live yet: it needs a client release and a scheduled switch. Once on, it would bring the 1.5% floor in about three years instead of six, which would make Solana's issuance curve one of the steeper declines among large proof-of-stake chains.

## What to watch in the next 90 days

**Lock expiries on fixed dates:** the FTX/Alameda estate's releases on Oct 11, Nov 11 and Dec 11 2026 (about 203K SOL each) and the private-sale releases on Nov 7, Dec 7 2026 and Jan 7 2027 (about 638K SOL each).

**The faster rate cut:** the approved change that doubles Solana's yearly disinflation has no switch date yet. If it goes live inside the window, the forward staking figure falls slightly; the bigger effect builds over years.

**The Alpenglow upgrade:** no mainnet date is set after the Sep 28 2026 window passed. When it lands, validator votes stop paying burned fees and each validator burns an admission fee instead (about 0.8 SOL a day), so the burn stays about the same size.

**Foundation moves:** any release from the Foundation's 27.2M SOL reserve would land in the Foundation row. The Aug 26 and Oct 4 2026 moves show it happens without notice.

## Summary

SOL supply grew **+1.68%** in the 90 days to Oct 10 2026 and is projected to grow **+1.26%** in the next 90 days. The engine is Solana's staking inflation — 3.61% a year today, falling 15% a year to a 1.5% floor — plus a monthly stream of lock expiries from private sales and the FTX estate. The fee burn, about 880 SOL a day, offsets almost none of it, and there is no buyback. The key risk on the supply side is unscheduled Foundation releases from its 27.2M SOL reserve; the key relief is the approved faster rate cut, which is not yet live.

---

*MrNasdog Pressure Framework analysis of SOL, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 10 2026.*

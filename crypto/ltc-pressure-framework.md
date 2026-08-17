---
title: "LTC Inflation Analysis · August 2026 · Mixed flows, supply roughly steady"
description: "A MrNasdog Pressure Framework read of Litecoin (LTC): a 6.25 LTC block subsidy mints 0.321M LTC per 90 days into an empty buy ledger, plus 0.063M LTC of listed-treasury selling. Net +0.50%; halving Jul 27 2027."
canonical_url: "https://mrnasdog.com/research/ltc/inflation"
tags: ["crypto", "ltc", "litecoin", "pow"]
published: true
---

> Originally published at **[mrnasdog.com/research/ltc/inflation](https://mrnasdog.com/research/ltc/inflation)** by MrNasdog.

Litecoin (LTC) mints **0.321M LTC** every 90 days from a fixed proof-of-work block subsidy of 6.25 LTC, and the Litecoin protocol offsets none of it — no buyback, no fee burn, no staking lock. One extra push sits on top of the mining this window: the largest identified LTC treasury, a Nasdaq-listed company, sold roughly **0.063M LTC** to fund a share buyback. The MrNasdog Pressure Framework reads **+0.50% net** against a **77.50M** circulating base and an 84M hard cap — about 92% of all Litecoin is already mined, and the next Litecoin halving is due **Jul 27 2027**.

## The verdict, in one paragraph

For the 90-day window ending **Aug 17 2026**, the framework reads **LTC at +0.50% net inflation**: clockwork mining emission plus one coordinated treasury seller, against a buy ledger that is completely empty. The independent supply monitor reads **+0.35%** over the same window — a gap of **0.15 percentage points**, comfortably inside the half-point tolerance, so no monitor-gap warning is raised on the Litecoin reading. The direction of that small gap is exactly what the mechanism predicts: the monitor measures newly minted supply, so it sees the Litecoin block subsidy but not the redistribution of already-mined LTC out of a corporate treasury. The framework sees both. Litecoin is a **quiet chain with a predictable, decaying issuance curve** — fifteen years of proof-of-work mining edging toward a fixed ceiling, with nothing discretionary in the supply picture at all.

## Sell pressure: where new LTC comes from

Litecoin has exactly one mint, and Sell #1, protocol inflation, is it: **0.321M LTC** over the window. The number is measured from the chain rather than assumed from the parameter. Litecoin targets a 2.5-minute block, which would imply 576 blocks in each 24 hours, but the chain actually sealed **51,407** blocks between the two window boundaries — **571** a day, 99.2% of nominal. Multiplied by the **6.25 LTC** coinbase subsidy that is **321,294 LTC** of brand-new Litecoin paid to Scrypt miners. Cumulative-subsidy arithmetic at the two block heights returns the identical figure, and on-chain supply sits 0.003% **below** the theoretical maximum for that height — proof that no Litecoin has ever been minted outside the block reward, including through the MWEB validation bug patched earlier in 2026.

Sell #2, vesting unlocks, is **0** and always will be. Litecoin launched in Oct 2011 as a fair launch: no presale, no insider allocation, no investor tranche, therefore no vesting contract and no unlock calendar that could ever fire. Sell #4, long-term locked or bankruptcy, is also **0** — no estate, no trustee schedule and no escrowed block of LTC exists anywhere in the coin's history to unwind into the market.

Sell #3, Foundation and unscheduled unlocks, is the one row where this Litecoin window differs from a pure mining read. The Litecoin Foundation is a donation-funded non-profit and holds no protocol allocation, so the surprise-distribution risk that shadows most tokens simply does not exist. But the framework enumerates every identified coordinated holder, and Litecoin has one: **Lite Strategy, Inc.** (Nasdaq: LITS), the first US-listed company to run a Litecoin treasury. Its own regulated filings show that stake falling from **894,298 LTC** on Mar 31 2026 to **819,070 LTC** on Jul 17 2026 — **75,228 LTC** in 108 days, or about 697 LTC a day, sold to fund a share-repurchase programme that has retired roughly 13% of the company's float. Carried across the 90-day window at that measured rate, the framework books **0.063M LTC**. A stricter reading that counts only the disclosed measurement days inside the window gives 0.041M; the run-rate figure ships because the buyback is continuous and roughly $19.6M of the $25M authorisation is still undeployed.

## Buy pressure: where new LTC goes

Nowhere. All four Litecoin buy rows are **0**, and three of them are zero by protocol design rather than by inactivity. Buy #1, programmatic buyback, is **0**: Litecoin captures no protocol revenue and holds no treasury contract, so there is nothing to fund a buyback with and no contract on the chain that could execute one. Buy #2, protocol fee burn, is **0** because Litecoin pays transaction fees straight to the miner inside the coinbase output — a block reward reads as the 6.25 LTC subsidy plus fees added on top, never a base fee destroyed. There is no burn opcode and no fee sink anywhere in the Litecoin codebase. Buy #3, Foundation buy, is **0**: the Litecoin Foundation runs on donations, grants and merchandise and has never announced or executed an open-market accumulation programme. Buy #4, new long-term lock, is **0** because proof-of-work Litecoin has no staking, no lockup contract and no vault; coins are mined or simply held. The listed spot Litecoin fund held about 126,800 LTC at the end of Jun 2026, but that is redeemable custodial float owned by its shareholders, not supply removed from the market, so it does not count as a lock.

## Foundation and overhang

Two team-adjacent overhangs are tracked on Litecoin, and only one carries a real balance. The Litecoin Foundation holds no protocol allocation and publishes no current LTC treasury figure; it is donation-funded, has never shown a pattern of market selling, and is walked by hand rather than read on-chain. The material overhang is the Nasdaq-listed treasury company, which still held **819,070 LTC** — a little over **1%** of circulating Litecoin — at its last disclosure on Jul 17 2026, refreshed through quarterly and event filings rather than a live wallet feed. Its live holdings page still shows that same number today. If that balance falls between refreshes, the outflow enters Sell #3 at the next refresh; if the company halts the buyback, Sell #3 drops to zero and the Litecoin reading collapses to pure mining at roughly +0.41%.

## How LTC compares to other hard-capped proof-of-work chains

Litecoin belongs to the smallest and cleanest supply class in the framework: fair-launch, hard-capped, halving proof-of-work. Its structural analogues are Bitcoin and Bitcoin Cash, and the mechanism is identical in shape — a coinbase subsidy that is the only mint, cut in half on a fixed block interval, with fees paid to miners rather than burned. Litecoin sits further along that curve than most: **92%** of the 84M cap is already mined, so each remaining halving removes a smaller absolute quantity of new supply than the last. What separates this class from uncapped continuous-emission chains is the absence of any discretion. A delegated proof-of-stake L1 can change its emission by governance vote; Litecoin cannot, short of a hard fork that miners would have to adopt.

The contrast with exchange tokens and fee-burning smart-contract platforms is sharper still. Those assets can and do run the buy side — quarterly revenue buybacks, base-fee burns, staking locks — which is how they reach a negative net reading. Litecoin has no mechanism capable of producing one. Every asset with a hard cap eventually stops inflating, but only assets with a live sink can actively shrink, and Litecoin has never had a sink. The result is an asset whose inflation is low, honest and completely predictable, but which can never print a deflationary quarter on mechanism alone.

Against privacy coins with permanent tail emission, Litecoin looks strictly better on supply: the tail-emission model floors inflation at a small positive number forever, while Litecoin's number keeps halving toward zero. Against Bitcoin, the difference is timing rather than kind — Litecoin halves in Jul 2027, one class of the same clockwork.

## What to watch in the next 90 days

First, the Litecoin treasury company's next filing: its fiscal year ended Jun 30 2026, so an annual report due around late Sep 2026 is the next hard datapoint on whether the 697-LTC-a-day sale rate held, accelerated or stopped. Second, whether the $25M share-repurchase authorisation is extended or exhausted — that single decision moves Sell #3 between 0 and roughly 0.063M. Third, the LitVM zero-knowledge layer-2, with mainnet targeted for Q4 2026; it changes no Litecoin issuance, but a live L2 would be the first thing in years capable of creating LTC demand the framework would need to classify. Fourth, further Litecoin Core maintenance releases — three shipped in 2026, all security hardening with zero issuance impact, and the on-chain supply check confirms none created LTC. Fifth, the halving itself on **Jul 27 2027** at block 3,360,000: still four windows away, but every rebuild from here should confirm the block-height estimate rather than the calendar date.

## Summary

The MrNasdog Pressure Framework reads Litecoin at **+0.50% net supply growth** over 90 days and projects the same forward: **0.384M LTC** of sell pressure against a buy ledger of exactly **0**. The structure behind that number is the simplest in coverage — a 6.25 LTC proof-of-work subsidy that is the only mint Litecoin has, with no vesting, no Foundation allocation, no burn, no buyback and no staking lock anywhere in the design. The key risk is not the mining but the corporate one: a single Nasdaq-listed holder controls over 1% of circulating LTC and is selling it steadily to fund its own share buyback, and that flow is disclosed quarterly rather than observed live. The ceiling is fixed at **84M LTC**, about 92% of it already mined, with the subsidy halving to 3.125 LTC on **Jul 27 2027**.

---

*MrNasdog Pressure Framework analysis of LTC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 17 2026.*

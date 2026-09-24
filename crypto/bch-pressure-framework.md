---
title:         "BCH Inflation Analysis · September 2026 · Mixed flows, supply roughly steady"
description:   "Mixed flows, supply roughly steady: Bitcoin Cash mined 40,806.25 BCH over 13,058 blocks in 90 days, with no buyback and no burn. Net +0.20%, monitor +0.19%."
canonical_url: "https://mrnasdog.com/research/bch/inflation"
tags:          ["crypto", "bch", "bitcoincash", "proofofwork"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/bch/inflation](https://mrnasdog.com/research/bch/inflation)*

# BCH Inflation Analysis · September 2026 · Mixed flows, supply roughly steady

BCH, the coin mined on the Bitcoin Cash proof-of-work chain, gets all of its new supply from one place: the block reward, a fixed **3.125 BCH** per block under a **21M** cap. Over the last 90 days **13,058** Bitcoin Cash blocks were mined, adding **40,806.25 BCH**, while nothing on the buy side took a single BCH back — no buyback, no fee burn, no staking lock. The MrNasdog Pressure Framework therefore reads BCH at **+0.20% net** over the last 90 days against a supply-monitor reading of **+0.19%**, a gap of **0.02 percentage points**. Bitcoin Cash supply grows slowly and on a known schedule toward its cap, with about **96%** already mined and the next halving around **April 2028**.

## The verdict, in one paragraph

For the 90-day window ending **Sep 24 2026**, the Pressure Framework reads **BCH at +0.20% net**: the sell side added **40,806.25 BCH** of mined coins against a circulating supply of **20.09M BCH**, and the buy side removed **zero**. The independent supply monitor reads the realised 90-day change at **+0.19%**. The gap is **0.02 percentage points**, far inside the framework's half-point tolerance, so BCH ships with **no data-conflict flag**. The forward column also reads **+0.20%** — **40,500 BCH** at the chain's target pace of one block every ten minutes — because no halving and no other supply event falls in the next 90 days. The label for BCH is **slowly inflationary on a fixed mining schedule**: a capped proof-of-work coin whose float grows by the block reward and by nothing else.

## Sell pressure: where new BCH comes from

All of it comes from mining. Sell #1, protocol inflation, is **40,806.25 BCH** over the window: every Bitcoin Cash block pays its miner a fixed **3.125 BCH** subsidy, and the framework read the subsidy and fees of every one of the **13,058** blocks between Jun 26 2026 and Sep 24 2026 rather than assuming a block count. The Bitcoin Cash subsidy halves every **210,000** blocks; the last halving was in 2024 and the next falls at block **1,050,000**, about **80,000** blocks away, which puts it around **April 2028** — well outside the next 90 days.

The block count deserves a sentence, because it is where a proof-of-work reading usually goes wrong. Bitcoin Cash targets one block every ten minutes, or **144** a day, which would have produced **12,960** blocks in 90 days. The chain actually produced **13,058** — an average of **595.6 seconds** per block, about **0.74%** fast — because miners added hash power during the window and difficulty took time to catch up; difficulty rose by roughly a quarter from the first block of the window to the last. The Bitcoin Cash difficulty rule does not simply react to recent blocks: it prices difficulty off the chain's distance from a fixed ten-minute schedule, so once hash power stops rising the chain returns to one block every ten minutes. Over the past year it averaged **601.3 seconds**, almost exactly on target. The last-90-day column therefore books the measured **13,058** blocks, and the next-90-day column books the target pace, **12,960** blocks or **40,500 BCH**.

Sell #2, vesting unlocks, is **zero** because nothing was ever allocated: Bitcoin Cash split from Bitcoin in **Aug 2017** by copying its ledger, with no premine, no token sale and no team or investor share, and the BCH in existence matches the mining schedule alone. Sell #3, foundation and unscheduled unlocks, is **zero**: there is no Bitcoin Cash foundation, DAO or team wallet, and every block pays its full reward and all its fees to the miner. A 2020 plan to divert part of each Bitcoin Cash block reward to a development fund was rejected, and the side that adopted it left as a separate coin. Sell #4, long-term locked or bankruptcy supply, is also **zero**. A bankruptcy estate still holds part of the Bitcoin Cash it recovered and must finish paying creditors by **Oct 31 2026**, but here circulating supply equals mined supply to within a few blocks, so those BCH were already inside the counted float and a payout moves them between holders without adding any. The same holds for listed companies building BCH treasuries: they buy on the open market, so their coins add nothing new.

## Buy pressure: where new BCH goes

Nowhere, and that is the whole story of the Bitcoin Cash buy side. Buy #1, programmatic buyback, is **zero**: Bitcoin Cash has no protocol revenue pot, no treasury and no programme that takes BCH off the market. Buy #2, the protocol fee burn, is **zero**: Bitcoin Cash burns no part of its fees, and every fee goes to the miner together with the block reward. The framework also read the two well-known keyless Bitcoin Cash addresses at both ends of the window: they received about a thousandth of a coin in 90 days from voluntary sends, and those coins are still counted in supply, so nothing is booked.

Buy #3, foundation buying, is **zero** because there is no project treasury to buy with; companies holding BCH on their balance sheet buy it with their own money on the open market, which moves coins between holders inside the float. Buy #4, new long-term locks, is **zero**: proof-of-work has no staking, bonding or lockup, and no new lock with a stated size appeared this window. Four canonical buy rows, four zeros — the Bitcoin Cash float can only grow, and it grows exactly as fast as blocks are mined.

## Foundation and overhang

Bitcoin Cash has no team-controlled overhang to name. There is no foundation reserve, no DAO treasury, no unscheduled allocation and no buyback wallet, because none of those were ever created. The gap between total and circulating BCH is **37.5 BCH** — twelve blocks of reward still to be counted — so there is no non-circulating bucket anywhere for coins to leave. The one balance the framework watches is the bankruptcy estate's remaining Bitcoin Cash, whose size the trustee does not publish; it is re-checked by hand on every refresh against the trustee's own notices. Exchange custody wallets, investment trusts and unlabelled large holders are excluded by rule — those BCH belong to depositors or to no identified group. If the estate's balance falls between refreshes, the outflow enters Sell #4 at the next refresh, where it is booked as zero new supply for as long as those coins sit inside the counted float.

## How BCH compares to other proof-of-work payment coins

BCH belongs to the family of capped proof-of-work coins that copy Bitcoin's monetary schedule, and against that family its supply mechanism is almost identical. Bitcoin Cash and Bitcoin share the same 21M cap, the same 210,000-block halving interval and, today, the same **3.125**-coin block subsidy, so both issue on the same curve and both reach it through mining alone. What separates Bitcoin Cash on supply is the difficulty rule: Bitcoin retargets every 2,016 blocks and can drift off schedule for weeks, while Bitcoin Cash re-anchors to a fixed ten-minute clock continuously, which is why a burst of hash power moved its block count by well under one percent. Against uncapped proof-of-work coins that pay a flat reward forever, BCH differs in direction of travel — its issuance halves toward zero, while theirs never stops.

Against smart-contract chains, the contrast is on the buy side. Many proof-of-stake chains pay validators in new coins and burn part of every fee, so their float can shrink in busy periods; Bitcoin Cash has neither a staking reward nor a fee burn, so its net reading is simply its mining rate. Fees play no part in Bitcoin Cash supply: they neither burn BCH nor replace the block reward, and until the reward halves again they stay a small addition to what miners earn. Against Bitcoin itself, the practical supply difference is therefore close to nil — both coins add the same reward per block, so both floats grow at roughly the same pace each quarter.

## What to watch in the next 90 days

First, hash power: the forward reading assumes the Bitcoin Cash chain returns to one block every ten minutes, and another rise in hash power as large as this window's — about a quarter — would add roughly **100** extra blocks, or about **300 BCH** above the booked **40,500 BCH**. Second, **Oct 31 2026** is the deadline for the bankruptcy estate to finish repaying creditors; any Bitcoin Cash it releases is already inside the counted float and would not change the net. Third, **Nov 15 2026** is the lock-in date for the May 2027 Bitcoin Cash upgrade; one candidate proposal would shorten the block interval, and the thing to check is that any version adopted scales the block reward down in step so that BCH issued per day stays the same. Fourth, Bitcoin Cash futures planned to start on a major US derivatives exchange on **Oct 19 2026** and a planned exchange listing of an existing Bitcoin Cash trust change who holds BCH, not how many exist.

## Summary

The MrNasdog Pressure Framework reads BCH at **+0.20% net** over the trailing 90 days and **+0.20%** over the next 90, with a buy side that is zero across all four canonical rows. The structural mechanism is a capped proof-of-work coin whose only source of new BCH is a fixed **3.125 BCH** block reward, measured this window at **40,806.25 BCH** over **13,058** blocks, with no burn, no buyback and no lock to offset it. The key risk to the reading is small and mechanical — sustained hash-power growth adds blocks faster than the ten-minute target — and a future upgrade that changed the block interval without re-scaling the reward. The ceiling is the **21M BCH** cap: about **96%** is already mined, and the next halving around **April 2028** cuts the pace in half again.

---

*MrNasdog Pressure Framework analysis of BCH, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 24 2026.*

---
title:         "BNB Inflation Analysis · September 2026 · Supply shrinking · projected to keep shrinking"
description:   "BNB supply is shrinking: no issuance, a 1.62M BNB quarterly Auto-Burn plus the BEP-95 gas burn give −1.22% net over 90 days, −1.24% next, toward a 100M floor."
canonical_url: "https://mrnasdog.com/research/bnb/inflation"
tags:          ["crypto", "bnb", "binance", "auto-burn"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/bnb/inflation](https://mrnasdog.com/research/bnb/inflation)*

# BNB Inflation Analysis · September 2026 · Supply shrinking · projected to keep shrinking

BNB, the gas coin of BNB Chain, is deflationary: BNB Chain creates no new BNB, and two burns remove coins every day and every quarter. Over the last 90 days the quarterly Auto-Burn destroyed **1,615,828 BNB** and the BEP-95 gas burn another **7,271 BNB**, so the MrNasdog Pressure Framework reads BNB at **−1.22% net**, with **−1.24%** projected for the next 90 days, against a supply-monitor reading of **−1.20%**. The burns stop once BNB supply reaches a floor of **100M BNB**, about **33.16M BNB** away.

## The verdict, in one paragraph

For the 90-day window ending **Sep 29 2026**, the Pressure Framework reads **BNB at −1.22% net**: the sell side added **zero** new BNB and the buy side destroyed **1,623,099 BNB**, out of a circulating supply of **133.16M BNB**. The independent supply monitor reads **−1.20%**. The gap is **0.02 percentage points**, well inside the framework's half-point tolerance, so no data-conflict flag is needed. The next 90 days read **−1.24%**, because the next Auto-Burn, about **1.65M BNB**, is expected on **Oct 15 2026** and the gas burn keeps running. The label for BNB is **deflationary by scheduled burn**: a fixed-supply coin with no issuance at all, shrinking a little every block and a lot once a quarter.

## Sell pressure: where new BNB comes from

Nowhere. Sell #1, protocol inflation, is **zero**. BNB Chain pays its validators only from the gas fees users pay; there is no block reward, and on every block we checked, the payment into the validator contract equalled that block's fees. BNB started with a fixed **200M BNB** and the only way its supply moves is down. Sell #2, vesting unlocks, is **zero**: the founding team and angel shares finished unlocking on **Jul 28 2021**, and no unlock tracker lists any BNB left to release.

Sell #3, foundation and unscheduled unlocks, is **zero**. The one team-held BNB wallet is the Auto-Burn reserve, which held **6.87M BNB** at the start of the window and **5.25M BNB** at the end; its only outflow in 90 days was the **1,615,828 BNB** it sent to the burn address on Jul 15 2026. The old bridge contract left over from the retired BNB Beacon Chain holds **25.97M BNB** and paid out **8,957 BNB** to people recovering coins. Both wallets sit inside the BNB circulating count, which equals total supply, so moving those coins adds nothing new to the market. Sell #4, long-term locked or bankruptcy supply, is **zero**: no estate or trustee releases BNB, and the listed companies that hold BNB, the largest with about **515,000 BNB**, bought it on the open market.

## Buy pressure: where new BNB goes

Almost all of it goes through the BNB Auto-Burn, booked as Buy #5. Once a quarter the reserve wallet sends BNB to the burn address, and the amount follows a fixed rule: the number of BNB Smart Chain blocks in the quarter, divided by the BNB price plus a constant, so more blocks and a lower price mean a bigger burn. The 36th Auto-Burn, on **Jul 15 2026**, destroyed **1,615,828 BNB**. We re-ran that rule on the April-to-June quarter and landed within one BNB of the amount burned. For July to September, the same rule gives about **1,648,559 BNB**, and the project's own running estimate lands within **0.1%** of it.

Buy #2, the protocol fee burn, is **7,271 BNB**. Under BEP-95, every block burns **10%** of its gas fees on the spot, sending them to the same burn address the Auto-Burn uses. We split the two by reading the burn address just before and just after the Jul 15 Auto-Burn transaction: everything else that arrived in the window is the gas burn. The pace rose from about **52 BNB** a day in early July to about **86 BNB** a day since, as BNB Chain got busier, while the 10% share stayed the same, so the forward column holds the trailing total. Buy #1, programmatic buyback, is **zero**, because nothing is bought on the market: the Auto-Burn destroys BNB already held. Buy #3, foundation buying, is **zero**, and Buy #4, new long-term locks, is **zero**, because staked BNB stays inside the circulating count and can be unstaked within days.

## Foundation and overhang

The one team-controlled BNB overhang is the Auto-Burn reserve, at **5.25M BNB** after the July burn. It is topped up by transfer when it runs low: it held only about **439,000 BNB** in early April before an **8.0M BNB** top-up landed just ahead of the April burn. After the expected October burn it should hold about **3.6M BNB**. The old Beacon Chain bridge contract, **25.97M BNB**, is tracked too, though it is a protocol contract, not a team wallet. Both are re-read on every refresh. Because BNB circulating supply equals total supply, neither is outside the float today; if a balance outside the float ever appears and it falls between refreshes, that outflow enters Sell #3 at the next refresh. Exchange custody wallets and corporate treasuries are context only.

## How BNB compares to other exchange tokens

BNB belongs to the class of exchange-linked tokens that shrink supply on a schedule, but its mechanism is unusual inside that class. Many exchange tokens buy coins back on the market with a share of exchange profit, so the size of the burn depends on how well the business did. The BNB Auto-Burn is set by a public rule built on BNB Smart Chain block counts and the BNB price, so anyone can check the amount, and it is paid from a reserve rather than from open-market buying. That makes BNB supply more predictable, but it also means the burn does not create a buyer in the market the way a buyback does.

Against smart-contract Layer 1s, the difference is issuance. Most proof-of-stake chains pay validators in new coins and burn part of their fees, so the net depends on which side is bigger. BNB Chain has no issuance at all, so even a small BEP-95 gas burn is pure reduction, and against capped proof-of-work coins, which still add new supply until their cap, BNB is already past the point of creating anything. Its limit is the other way round: a **100M BNB** floor where the Auto-Burn ends.

## What to watch in the next 90 days

First, the quarter closes on **Sep 30 2026**, which fixes the block count and price behind the next BNB Auto-Burn. Second, the 37th Auto-Burn itself, expected on **Oct 15 2026** at about **1.65M BNB**; a later date inside the window would not change the forward reading. Third, the BNB Chain zero-fee promotion for stablecoin transfers ends on **Sep 30 2026**, which could lift gas fees and so the BEP-95 burn. Fourth, the reserve wallet balance, which falls to about **3.6M BNB** after the October burn and has been topped up by transfer before. Fifth, any validator vote to change the **10%** burn share.

## Summary

The MrNasdog Pressure Framework reads BNB at **−1.22% net** over the trailing 90 days and **−1.24%** over the next 90: no issuance and no unlocks, against a quarterly Auto-Burn of **1,615,828 BNB** and a BEP-95 gas burn of **7,271 BNB**. The structural mechanism is a burn sized by a fixed public rule and paid from a reserve wallet, plus a small burn on every block. The key risk for the reading is that the Auto-Burn is a policy, not a market buyer: it shrinks BNB supply but does not buy BNB. BNB supply keeps shrinking until it reaches the **100M BNB** floor, about **33.16M BNB** below today.

---

*MrNasdog Pressure Framework analysis of BNB, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

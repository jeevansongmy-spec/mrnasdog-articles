---
title: "KCS Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description: "Supply growing: KCS reads +1.82% per 90 days. No KCS is minted, but a 2021 lockup releases 2.5M a quarter and KuCoin's burn is idle since Dec 31 2025."
canonical_url: "https://mrnasdog.com/research/kcs/inflation"
tags: ["crypto", "kcs", "kucoin", "exchange"]
published: true
---

> Originally published at **[mrnasdog.com/research/kcs/inflation](https://mrnasdog.com/research/kcs/inflation)** by MrNasdog.

KuCoin Token creates no new KCS — KuCoin Community Chain pays its validators from gas fees, and the KCS total supply only fell in the last 90 days — yet the Pressure Framework reads KCS at **+1.82%** over the trailing 90 days and **+1.82%** over the next 90. All of it comes from one mechanism: a 2021 lockup of **50M KCS** that releases **2.5M KCS** every quarter into the tradable float. Sell pressure is **2.5M KCS**, buy pressure is **0**, because the KuCoin buyback and burn has not fired since **Dec 31 2025**; the lockup has only **5.0M KCS** left, so it ends after **early Jan 2027**.

        
## The verdict, in one paragraph

        
Against a circulating base of **137.2M KCS**, the framework books **2.5M KCS** of sell pressure and **0** of buy pressure over the trailing 90 days — a net of **+1.82%** — and projects **+1.82%** for the next 90 days, because one more quarterly unlock slice falls inside that window. The inflation monitor reads **+1.74%** for the same trailing window, a gap of **0.08 percentage points**, well inside the framework's 0.5pp tolerance, so no monitor-gap warning ships on the overview page. The label for KCS is an **exchange token whose burn went quiet while its last locked coins unlock**: nothing is minted, but for now nothing is burned either, and the float grows one slice at a time.

        
## Sell pressure: where new KCS comes from

        
It does not come from minting. Sell #1, protocol inflation, is **0**. KCS is the native gas coin of KuCoin Community Chain, and that chain has no block subsidy: its explorer reports a block reward of zero, and a validator's balance did not move across a block it produced itself. Gas fees go to validators out of KCS that already exists. The KuCoin Token copy on Ethereum has no mint function. The published KCS total supply moved only downward in the window, by a fraction of one coin. Because a KuCoin Community Chain upgrade could in principle add issuance, the row is watched rather than closed permanently.

        
The whole supply story is Sell #2, vesting unlocks, at **2.5M KCS**. In 2021 the KCS founders and early investors re-locked **90M KCS**; **20M** was burned, **20M** became a holder-rewards pool, and the remaining **50M KCS** — early-investor coins plus a grant to the KCS Management Foundation — was put on a five-year schedule released in equal quarterly slices from 2022. Twenty slices of **2.5M KCS**. KuCoin's own circulating figure steps up by exactly that amount at the start of each quarter while total supply stays flat; the July 2026 slice took it from **134.7M** to **137.2M KCS**. The coins do not move on chain to do this — the lock wallet has not sent a single KCS since **Mar 2022** — but each slice becomes free to sell, which is the thing the Pressure Framework counts, and it is counted once, at the moment it joins the float.

        
Sell #3, Foundation and unscheduled unlocks, is **0**: every watched KCS wallet was read at both ends of the window and none of them moved. Sell #4, long-term locked or bankruptcy, is **0** as well: KuCoin is a going concern, with no bankruptcy estate, no trustee and no court-ordered distribution of KCS.

        
## Buy pressure: where new KCS goes

        
Nowhere, this window, and that is the headline change for KCS. Buy #1, programmatic buyback, is **0**. KuCoin ran a monthly KCS buyback and burn for **66** months without a break; the last one, on **Dec 31 2025**, bought **20,240 KCS** and sent it to the burn address on KuCoin Community Chain. There has been no burn since — nine months — and no KuCoin announcement explains the pause or restarts it. The burn address gained under **0.02 KCS** across these 90 days, which is dust sent by users rather than a buyback. The framework does not assume the programme comes back: the next 90 days are booked at zero until a burn actually fires.

        
Buy #2, protocol fee burn, is also **0**. KuCoin Community Chain destroys nothing per transaction. KCS burns only happen as transfers to the burn address, and the published KCS total supply is defined as the coins on chain minus that address. The framework read both surfaces at both ends of the window: they moved by the same **0.02 KCS**, one flow seen twice, and it is dust. Buy #3, Foundation buy, is **0** — no purchase was announced or seen, and none of the watched team wallets received a KCS. Buy #4, new long-term lock, is **0**: staked KCS on KuCoin Community Chain fell from **55.9M** to **55.4M**, and staked KCS already counts as circulating either way.

        
## Foundation and overhang

        
The KCS overhang is large, readable on chain, and has sat still for more than four years. The first item is the lock wallet itself, holding **47.5M KCS**: the **5.0M** still locked, plus **42.5M** released on paper but never moved since **Mar 2022**. That 42.5M is already counted as circulating, so selling it later would not add to this reading — but it is the single biggest pile of KCS that could reach the market. The second item is the holder-rewards pool at **19.9M KCS**, which last paid out in **Jun 2022**. The third is two wallets that took the first 2022 slice, at **1.6M** and **0.9M KCS**, both untouched since. All of them are read from the chain at every rebuild. The buyback destination is the burn address, where KCS is destroyed rather than held. If any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

        
## How KCS compares to other exchange tokens

        
KCS belongs to the exchange-token class: coins whose supply story is a company buying back and burning its own token out of trading revenue. The strongest members of that class run a burn set by a fixed, published rule, so the burn keeps firing whether or not anyone announces it, and their inflation readings are genuinely negative quarter after quarter. KCS used to sit in that group on rhythm alone — a burn every month for five and a half years. What separates it now is that its burn is a company decision with no rule enforced on chain, and the decision has been to stop, at least for now.

        
On issuance, KCS is stricter than most layer-one chains. Uncapped proof-of-stake chains mint new coins to pay stakers every day, and even a halving chain like Bitcoin still mints on every block. KuCoin Community Chain mints nothing, so KCS sits closer to a capped token whose only growth is an unlock. And that unlock is small and finite: **2.5M KCS** a quarter with **5.0M** left, against the multi-year, multi-billion-coin vesting calendars many newer tokens carry.

        
So the comparison cuts both ways. Against an exchange token with an automatic burn, KCS looks weak, because its demand-side removal is switched off and nothing in the code turns it back on. Against a young token still vesting its team and investors, KCS looks clean, because its unlock ends within two quarters. Once the last slice lands, KCS supply will be flat unless the burn returns.

        
## What to watch in the next 90 days

        
First, the next quarterly unlock slice of **2.5M KCS**, expected in **early Oct 2026**; it is the only scheduled event in the window and it sets the next-90-day reading. Second, the KuCoin burn announcement channel: a single restarted monthly burn would pull the reading down, and at the 2025 pace of roughly **18,000** to **146,000 KCS** a month it would take far more than one burn to offset a 2.5M slice. Third, the burn address on KuCoin Community Chain, read at every rebuild, which shows a real burn the day it lands. Fourth, the lock wallet at **47.5M KCS** — any outflow is the first movement in more than four years. Fifth, the final slice in **early Jan 2027**, just after this window, which ends the schedule.

        
## Summary

        
The MrNasdog Pressure Framework reads KCS at **+1.82%** over the trailing 90 days and **+1.82%** projected forward: supply growing, projected to keep growing. The mechanism is not inflation but unlock — KuCoin Community Chain mints no KCS, while a 2021 lockup releases **2.5M KCS** a quarter into a float of **137.2M**. The key risk is on the buy side: the KuCoin buyback and burn that used to offset this has not fired since **Dec 31 2025**, and nothing on chain forces it to return. The ceiling is the comfort — only **5.0M KCS** of the lockup is left, and total supply of **142.2M KCS** can only go down from here unless the chain itself changes.

---

*MrNasdog Pressure Framework analysis of KCS, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 18 2026.*

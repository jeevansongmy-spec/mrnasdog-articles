---
title:         "ONDO Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "Supply roughly steady: ONDO mints nothing, no unlock fell in 90 days, and 300M Foundation payouts were already circulating. 0.00% net; next unlock Jan 18 2027."
canonical_url: "https://mrnasdog.com/research/ondo/inflation"
tags:          ["crypto", "ondo", "rwa", "tokenunlocks"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/ondo/inflation](https://mrnasdog.com/research/ondo/inflation)*

# ONDO Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

The MrNasdog Pressure Framework reads ONDO, the token of Ondo Finance, at **0.00% net** over the last 90 days and **0.00%** over the next 90: nothing was minted, no ONDO unlock date fell in the window, and nothing was bought back or burned. The Ondo Foundation paid out **300M ONDO** from its main wallet, but by the foundation's own disclosure those were unlocked coins it already held, so they were already counted as circulating and added no new supply. An independent supply monitor reads **+0.001%**, a gap of **0.001 percentage points**. ONDO has a fixed **10B** supply, **4.87B** of it circulating; the next ONDO unlock, about **1.71B**, lands on **Jan 18 2027**, just after the forward window closes.

## The verdict, in one paragraph

For the 90-day window ending **Sep 25 2026**, the Pressure Framework reads **ONDO at 0.00% net**: **zero** ONDO added to the counted float and **zero** removed from it, against a circulating supply of **4,869,330,647 ONDO**. The independent supply monitor reads the realised 90-day change at **+0.001%**. The gap is **0.001 percentage points**, far inside the framework's half-point tolerance, so ONDO ships with **no data-conflict flag**. The forward column also reads **0.00%**, because the Ondo Finance unlock calendar has no date between now and **Dec 24 2026** and the foundation's recent payouts come from coins that already circulate. The label for ONDO this quarter is **a quiet window between yearly cliffs**: a fixed-supply token whose float moves in one large step each January and barely at all in between.

## Sell pressure: where new ONDO comes from

Sell #1, protocol inflation, is **zero**. ONDO has no emission schedule: all **10B ONDO** were created at the start, and total supply read exactly **10B** at both ends of the window. That reading was tested rather than assumed, because the ONDO contract can mint — the function exists, and only the Ondo Foundation's main wallet holds the right to call it. The supply figure lives where a mint would have changed it, so a flat reading here is a real measurement: no ONDO was minted this window. Sell #2, vesting unlocks, is also **zero**. The locked ONDO allocations — ecosystem growth, protocol development and private sales — open once a year on **Jan 18**. The last step, on **Jan 18 2026**, lifted the circulating count by about **1.71B ONDO**, and no unlock date falls in either the last or the next 90 days.

Sell #3, foundation and unscheduled unlocks, is **zero**, and this is the row that needed the most care. The Ondo Foundation's main wallet held **5,479,207,574 ONDO** at the start of the window and **5,179,207,574 ONDO** at the end. It sent **150M ONDO** on **Aug 21 2026** and another **150M ONDO** on **Sep 23 2026** to a payout wallet, which passed the coins on to outside addresses in pieces of about **9M to 26M ONDO**, much of it to an exchange. The question for the framework is where those coins sat before they moved. The foundation discloses that **4,422,519,707 ONDO** in that wallet is still locked; everything above that — **756.7M ONDO** today — is unlocked ONDO the foundation holds, and it is already inside the circulating count, which covers every coin the calendar has released no matter who holds it. The **300M ONDO** came out of that unlocked share, so it moved within the float and adds nothing new. Sell #4, long-term locked or bankruptcy supply, is **zero**: no estate, trustee schedule or long ONDO lock releases coins outside the yearly calendar.

## Buy pressure: where new ONDO goes

The ONDO buy side is empty in both windows, and each row was checked rather than assumed. Buy #1, programmatic buyback, is **zero**: Ondo Finance runs no ONDO buyback, and no buyback proposal has reached the Ondo DAO vote portal, which has had no new proposal since January 2024. Buy #2, the protocol fee burn, is **zero**. A burn can show up in two places — a rising balance at a burn address, or a falling total supply — so both were read at both ends of the window: the burn address held the same **7.59 ONDO** throughout, and total supply stayed at **10B**. Neither moved, so no ONDO was destroyed. Buy #3, foundation buying, is **zero**: the foundation's main wallet received nothing but dust from look-alike addresses this window, and its payout wallet received coins only from the main wallet. Buy #4, new long-term locks, is **zero**: no new ONDO lock contract and no announced lock-up with a stated size appeared in the window. Zero sell against zero buy is what puts the ONDO net at **0.00%**.

## Foundation and overhang

The Ondo Foundation's main wallet is the one overhang that matters, and it is readable on-chain, so it is re-read on every refresh. It now holds **5.18B ONDO** in two parts: **4.42B ONDO** the foundation says is still locked, and **756.7M ONDO** of unlocked coins it holds. The locked part is outside the circulating count and joins it only on the Jan 18 cliffs; the unlocked part is already counted. Over the last six months the foundation has moved **125M to 150M ONDO** at a time to its payout wallet, five times since April; at that pace the unlocked share lasts beyond the next 90 days, so the forward window books nothing either. The payout wallet itself holds **150M ONDO** waiting to be passed on. A further **708.1M ONDO** is locked outside the foundation and opens on the same yearly calendar. Exchange wallets and unlabelled large holders are left out by rule. If the foundation's main wallet falls below its disclosed locked balance between refreshes, or any locked ONDO reaches the market before its January date, that outflow enters Sell #3 at the next refresh.

## How ONDO compares to other tokenized-asset tokens

ONDO belongs to the group of project tokens with a fixed supply and a scheduled release, rather than an emission curve. An uncapped proof-of-stake chain adds new coins every block to pay validators, so its float grows a little every day; ONDO adds none, and its float moves in one large step a year. That makes ONDO's inflation lumpy rather than smooth: a quarter like this one reads **0.00%**, while the quarter that contains a Jan 18 cliff carries about **1.71B ONDO** of new float against today's **4.87B**.

Against tokens that route revenue into buybacks or burns, ONDO has no offsetting buy side at all — nothing takes ONDO off the market, so the yearly cliffs are not netted against anything. Against tokens that are fully unlocked, ONDO still has **5.13B ONDO**, about half its supply, waiting on the calendar, with three steps left in **January 2027**, **January 2028** and **January 2029**. The comparison that matters most is foundation behaviour: some foundations hold their unlocked coins, while the Ondo Foundation pays its out steadily. On this framework that steady payout is not new supply, because the coins were already counted — but it is real selling of already-counted coins, and it is why the unlocked share of the foundation wallet is watched as closely as the locked share.

## What to watch in the next 90 days

First, the Ondo Foundation's main wallet against its disclosed locked balance of **4,422,519,707 ONDO**: another two or three payouts of **150M ONDO** would still leave it above that line, but any move below it before **Jan 18 2027** would put locked coins on the market early and open a Sell #3 row. Second, the **Jan 18 2027** cliff itself, **115 days** away: the last step was about **1.71B ONDO** and some trackers quote up to **1.94B**, so the size is checked at the source again once it falls inside the forward window. Third, any Ondo DAO proposal that would send part of Ondo Finance revenue into ONDO buybacks — talked about in public, but not on the vote portal as of **Sep 25 2026**; a passed vote would open the first ONDO buy row. Fourth, any change to the Ondo Foundation's wallet disclosure, last updated on **Aug 26 2026**, which is what splits the main wallet into locked and unlocked parts.

## Summary

The MrNasdog Pressure Framework reads ONDO at **0.00% net** over the trailing 90 days and **0.00%** over the next 90, with every sell and buy row at zero. The mechanism is a fixed **10B ONDO** supply that nothing mints or burns, released in yearly Jan 18 steps, with the Ondo Foundation paying out unlocked coins that are already part of the circulating count. The key risk is the calendar: about **1.71B ONDO** is due on **Jan 18 2027**, and the ONDO buy side has nothing to absorb it. The ceiling is the **10B** total — **5.13B ONDO** is still locked, and it all reaches the circulating count by **Jan 18 2029**.

---

*MrNasdog Pressure Framework analysis of ONDO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 25 2026.*

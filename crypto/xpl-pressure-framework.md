---
title: "XPL Inflation Analysis · October 2026 · Supply growing · projected to keep growing"
description: "XPL supply is growing: the Sep 25 2026 team and investor cliff and monthly unlocks added 1.93B XPL, +42.65% in 90 days, with +15.07% more due next."
canonical_url: "https://mrnasdog.com/research/xpl/inflation"
tags: ["crypto", "xpl", "plasma", "stablecoin"]
published: true
---

Originally published at [XPL Inflation Analysis · October 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/xpl/inflation).

# XPL Inflation Analysis · October 2026 · Supply growing · projected to keep growing

XPL supply is growing fast, and all of the growth comes from unlocks. In the 90 days to Oct 7 2026, **1.93B XPL** moved from locked allocations into the market — mostly the **1.67B** team and investor cliff on Sep 25 2026 — while the Plasma fee burn removed only about **15 XPL**. On today's float of **4.53B XPL** that is a net rise of **+42.65%**, and the published calendar adds another **683.3M XPL**, or about **+15.07%**, in the next 90 days. No new XPL is minted yet; every one of the 10B coins already exists, and the unlock calendar runs to Sep 25 2028.

## The verdict, in one paragraph

Our ledger reads **+42.65%** net supply growth over the last 90 days and **+15.07%** for the next 90. The monitor reads **+74.37%**, a gap of **31.72 percentage points**, which is above our 0.5-point line, so we walked every source again. Both sides measured the same flow: the monitor saw circulating XPL rise by about **1.93B**, the same 1.93B our ledger books. The monitor divides that rise by the float of 90 days ago (**2.60B XPL**); we divide it by today's float (**4.53B XPL**). Put on the same base, the two numbers agree to a hundredth of a point, so no warning chip ships. Plasma is an **unlock-driven chain**: no issuance, no meaningful burn, and a monthly vesting calendar that decides almost everything about XPL supply.

## Sell pressure: where new XPL comes from

Protocol inflation is **0**. Plasma's plan pays validators 5% a year, stepping down by half a point a year to a 3% floor, but those rewards switch on only when outside validators and stake delegation go live. They have not. We checked the chain itself: the block producer on Plasma receives exactly the tips users pay and not one extra XPL, so nothing is being printed. Plasma published a design on Oct 1 2026 for handing blocks between validator groups without pausing the chain — a step toward opening the validator set, with no reward start date attached.

Vesting unlocks are the whole story: **1,933.3M XPL** in the window. All 10B XPL were created at the mainnet beta on Sep 25 2025. The 4B Ecosystem & Growth allocation releases **88.9M XPL** on the 25th of each month, and three of those landed in the window (Jul 25, Aug 25 and Sep 25 2026). The big event was the one-year cliff on Sep 25 2026, when one third of the team's 2.5B and one third of the investors' 2.5B opened together — **1,666.7M XPL** in a single day. From Oct 25 2026 the remaining team and investor coins vest monthly for two years, **69.4M XPL** each, so every month now adds **227.8M XPL**: **683.3M XPL** across the next 90 days. The Jul 28 2026 release of coins bought by US buyers in the public sale adds nothing to our count, because the whole public sale was already counted as circulating.

Foundation and unscheduled unlocks are **0**: every locked XPL sits on the published calendar, so there is no loose reserve that could appear without warning. Long-term locked or bankruptcy supply is also **0**; no estate, court or trustee holds XPL.

## Buy pressure: where new XPL goes

Very little leaves. Plasma follows the EIP-1559 model and burns the base fee on every transaction, but the base fee sits almost at zero. Adding up all 7.78M blocks of the window, the fee burn destroyed about **15.4 XPL**, and 12.5 of those came in one busy stretch on Oct 1 2026. Against a float of 4.53B, that rounds to **0**. About 22,000 XPL were also sent to dead addresses by users this window; those are one-off sends, not a protocol burn, and they do not change the reading.

There is no programmatic buyback and no foundation buying: no contract, treasury or announcement puts XPL back into a lock. The newest sink is the Plasma One card. Holders can lock XPL for 12 months to reach a higher card tier, and the Aurora perks layer launched on Sep 25 2026 to make that lock more attractive. Plasma has not published how much is locked, and locked card coins still count as circulating, so the new long-term lock row books **0** — a real behaviour we track, not yet a measurable drain.

## Foundation and overhang

The overhang is large and fully scheduled. Still locked: **1.67B XPL** for the team, **1.67B XPL** for investors and **2.13B XPL** for ecosystem growth — **5.47B XPL**, more than the whole float today. These coins sit in custody wallets, not in a lock contract anyone can read, so the calendar is what we measure. On the chain we can see the wallets move: on Sep 25 2026 the two largest allocation wallets sent out 1.45B and 1.29B XPL, more than the cliff itself, as coins were spread into new per-holder wallets (ten of them hold about 100M XPL each and have never sent a coin). The wallet that appears to hold the ecosystem pool holds 2.24B XPL and stayed above its still-locked share at every read. We re-read these wallets on the chain at every rebuild and walk Plasma's pages every two weeks. If any of these balances falls between refreshes faster than the calendar allows, the outflow enters Sell #3 at the next refresh.

## How XPL compares to other stablecoin and payment chains

Most payment chains grow supply through issuance and shrink it through fees. Ethereum pays validators in new ETH and burns the base fee; Tron charges for network use and burns part of it. XPL sits at the other end today: Plasma has no live issuance and a burn so small it rounds away, because the chain was designed to make stablecoin transfers nearly free. That means fees will not offset anything, and the day validator rewards start, XPL gains a second source of new supply on top of the unlocks.

In structure, XPL looks most like the young venture-backed Layer-1s: a fixed 10B minted at launch, with a large share held by the team, investors and an ecosystem fund and released on a monthly calendar after a one-year cliff. For those chains the vesting calendar, not the protocol, sets the pace of new supply for the first three or four years. XPL is now past its cliff, so the pace drops from the Sep 25 jump to a steady 227.8M XPL a month — about 5% of today's float every month — until Sep 25 2028.

## What to watch in the next 90 days

**Oct 25 2026**: the first monthly team and investor tranche (69.4M XPL each) arrives with the ecosystem's 88.9M — 227.8M XPL in one day.

**Nov 25 2026** and **Dec 25 2026**: the same 227.8M XPL each, completing the 683.3M XPL the ledger projects for the next 90 days.

**Validator rewards**: any date for outside validators and delegation would switch on the 5% yearly reward and add a new sell row; the validator-handoff design published on Oct 1 2026 is the step to watch.

**Plasma One locks**: if Plasma publishes the amount of XPL locked for card tiers, we will check whether those coins leave the circulating count; until then they book 0.

## Summary

XPL is an unlock-driven supply: Plasma mints nothing today and burns almost nothing, so the vesting calendar decides the numbers. The Sep 25 2026 cliff and three ecosystem tranches put **1.93B XPL** into the market in 90 days, a net **+42.65%**, and the monthly calendar adds **683.3M XPL** (**+15.07%**) next. The key risk is the **5.47B XPL** still locked, which keeps arriving at 227.8M a month until Sep 25 2028, with validator rewards still to come on top. The ceiling is the fixed 10B minted at launch — until validator inflation begins.

*MrNasdog Pressure Framework analysis of XPL, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 8 2026.*

---
title: "CRV Inflation Analysis · August 2026 · Supply growing slowly, emission stepping down"
description: "A MrNasdog Pressure Framework read of Curve DAO (CRV): ~28.73M / 90D of declining gauge emission with no buyback and no burn. Framework +1.86% net; monitor +2.24%, gap +0.38pp — inside tolerance."
canonical_url: "https://mrnasdog.com/research/crv/inflation"
tags: ["crypto", "crv", "curve", "defi"]
published: true
---

> Originally published at **[mrnasdog.com/research/crv/inflation](https://mrnasdog.com/research/crv/inflation)** by MrNasdog.

Curve DAO's CRV has exactly one source of new supply: a preset, declining gauge emission that mints CRV to liquidity providers. On-chain, total supply rose **28.73M CRV** over the last 90 days against a circulating base of **1.55B**, so the Pressure Framework reads **+1.86% net** — mildly inflationary, with no buyback and no burn to offset it. The emission steps down about **16%** on **Aug 12 2026**, cutting the forward pace to roughly **24.31M CRV** and a **+1.57%** next-90-day read. Our supply monitor reads **+2.24%**, a gap of just **0.38 percentage points** — within tolerance, so no monitor-gap flag is raised. CRV is best understood as a **capped token that inflates in one direction only, on a rate that steps down every year**.

## The verdict, in one paragraph

For the 90-day window ending Aug 6 2026, the Pressure Framework reads **CRV at +1.86% net**. Sell pressure is a single row — the Curve gauge emission, about **28.73M CRV** minted to liquidity providers — and buy pressure is **zero**, because Curve runs no CRV buyback and burns no CRV. Against a circulating base of **1.55B CRV**, that is a clean, one-mechanism read. Our supply monitor puts the realised change at **+2.24%**, a gap of only **0.38 percentage points**, which is inside the framework's tolerance and ships no chip; the small residual is a net **4.8M CRV** of vote-escrow (veCRV) unlocking that returned to the float. CRV is best characterised as **structurally inflationary on a declining, protocol-encoded emission with nothing on the buy side to absorb it**.

## Sell pressure: where new CRV comes from

Sell #1, protocol inflation, is the entire story. The CRV token contract mints new CRV on a fixed, annually-decaying schedule and routes it to Curve's liquidity gauges, where liquidity providers claim it — so every newly-minted CRV reaches the tradable market. Reading the contract directly, total supply climbed from **2.378B** to **2.407B** over the window, a gauge emission of **28.73M CRV**, matching the on-chain rate of about **3.6639 CRV per second**, or **316,563 CRV** a day, constant across the window with no mid-window cut.

Every other sell row is **zero**. Sell #2, vesting unlocks, is zero: every genesis allocation — team, investors, employees and early users, each vesting at most four years from the Aug 2020 launch — finished distributing by Aug 2024, so there is no unlock calendar and no cliff left. Sell #3, Foundation and unscheduled unlocks, is zero as a flow; the only non-circulating CRV beyond veCRV is a small DAO/community reserve of about **11M** that did not move in the window, and while Curve is founder-concentrated, those coins already sit in circulating supply, not in a team-controlled unlock. Sell #4, long-term locked or bankruptcy, is zero: there is no CRV estate and no trustee distribution — the 2023 exploit and the founder's 2024 debt episode were market and protocol events that created no new CRV supply.

## Buy pressure: where new CRV goes

Every buy-side row is **zero**, and that is the defining feature of CRV's supply profile. Buy #1, the programmatic buyback, is **zero**: Curve does not buy CRV on the open market. Trading and crvUSD revenue is instead paid to vote-locked holders in **stablecoin**, and since Jun 2025 a share of protocol revenue routes to a DAO treasury — but none of that recycles into CRV. That is a yield to lockers, not a bid under the token, so it does not enter the framework as buying power. Buy #2, protocol fee burn, is **zero** because CRV is never burned; fees are distributed, not destroyed, and the contract has no burn path in use.

Buy #3, Foundation buy, is **zero** — no Curve entity has disclosed an open-market CRV purchase, and revenue is returned to lockers as stablecoin rather than recycled into CRV. Buy #4, new long-term lock, is **zero** for the window, and this needs a careful distinction. Vote-escrow is Curve's lock mechanism, with about **851M CRV** — roughly 55% of circulating — locked for up to four years. But that balance actually **fell about 4.8M CRV** over the window as expiries outpaced new locks, so it removed nothing net from the float; in fact the net unlock added supply back. With no burn, no buyback and no net new lock, there is simply nothing to net against the emission.

## Foundation and overhang

Two pools sit outside the tradable float. The larger is **veCRV**, the vote-escrow contract, holding about **851M CRV** — roughly 35% of total supply and 55% of circulating — locked by ordinary holders for up to four years. The supply monitor classifies it as non-circulating, so the tradable float already excludes it, and the framework tracks it as a stable, slightly-draining pool rather than a fresh lock. The smaller is a DAO/community reserve of about **11M CRV** with no published release schedule, which did not move in the window. Neither is a team unlock in the usual sense — Curve's founder and investor allocations vested out years ago — so the real overhang is user-driven veCRV behaviour. If the locked veCRV balance drains faster between refreshes, that outflow enters Sell #3 at the next refresh.

## How CRV compares to other capped DeFi governance tokens

The sharp contrast is emitting versus fully-minted. A token such as **AAVE** is capped at 16M and entirely minted, so its sell side is essentially nil — no new supply is created at all. CRV is also capped, at **3.03B**, but it is only about **80% minted** and still issues new CRV every day through gauges, so its sell side is a live, continuous stream. That makes CRV structurally more inflationary than a fully-minted governance token even though both are "capped."

The closer analogue is a decaying-emission schedule. Like a proof-of-work chain that halves, CRV's issuance steps down on a fixed calendar — about **16%** a year, every August — so the inflation rate falls predictably toward the **3.03B** cap over decades. The difference from a burn-and-buyback exchange token is decisive: those tokens run buybacks that end in a burn address and can print a real supply shrink, while Curve returns revenue to lockers as stablecoin and touches CRV supply not at all. That is why CRV, despite a large and famous vote-lock, still reads mildly inflationary here — the lock holds supply off the float but does not remove it, and nothing on the buy side offsets the daily emission. The framework's value in this case is separating the vote-escrow narrative from the supply reality: veCRV is a demand-and-governance story, not a supply-reduction one.

## What to watch in the next 90 days

First, the annual emission cut on **Aug 12 2026**, which drops the daily rate from about **316K** to **266K CRV** and is already priced into the framework's forward **+1.57%** read. Second, the veCRV locked balance: it is slowly draining, and a faster unlock would add CRV back to the float and lift the realised inflation. Third, any governance move to buy back or burn CRV with crvUSD or protocol revenue — none exists today, but it is the single change that would turn the buy side non-zero. Fourth, new liquidity gauges, which redistribute where emission lands but do not change its total. Fifth, the monitor gap, which at **0.38 points** is well within tolerance and would only matter if veCRV flows swung sharply.

## Summary

Curve DAO's CRV is a 3.03B-capped token whose only new supply is a preset, declining gauge emission to liquidity providers — about 28.73M CRV over 90 days, which puts the framework at +1.86% net, mildly inflationary. There is no CRV buyback and no CRV burn, and all genesis vesting finished by 2024, so the sell side is a single clean mechanism with nothing on the buy side to offset it. The emission steps down about 16% on Aug 12 2026, easing the forward read to +1.57%, and our monitor's +2.24% sits just 0.38 points away — within tolerance, no flag. The key structural fact is that CRV's large veCRV lock holds supply off the float without removing it, so the token stays inflationary until either the emission decays much further or governance decides to buy back or burn.

*MrNasdog Pressure Framework analysis of Curve DAO (CRV), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated August 6 2026.*

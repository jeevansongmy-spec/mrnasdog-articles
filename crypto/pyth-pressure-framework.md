---
title:         "PYTH Inflation Analysis · August 2026 · Supply was growing, trend cooling"
description:   "Pyth Network reads +26.95% net: mint authority is null, so its only dilution is one annual cliff — and the 2,125M May 2026 unlock already landed. Forward −0.06%."
canonical_url: "https://mrnasdog.com/research/pyth/inflation"
tags:          ["crypto", "pyth", "solana", "oracles"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/pyth/inflation](https://mrnasdog.com/research/pyth/inflation)*

# PYTH Inflation Analysis · August 2026 · Supply was growing, trend cooling

The MrNasdog Pressure Framework reads **PYTH at +26.95%** net supply over the last 90 days, and the entire figure is one event: the Pyth Network vesting cliff of **2,125M PYTH** that released on **May 19 2026**. PYTH is a fixed **10,000,000,000** Solana token whose mint authority and freeze authority both read null on-chain, so no PYTH can ever be created and the vesting calendar is the only supply engine there is. The next and final cliff is **May 19 2027**, which is why the forward 90 days carry no unlock at all and the framework flips to **−0.06%** on the strength of a revenue-funded DAO buyback of **2.95M PYTH**. Our supply monitor reads **+36.71%** for the same window; the **9.77 percentage point** difference is a denominator base, not a data conflict.

## The verdict, in one paragraph

For the 90-day window running **May 19 2026** to **Aug 17 2026**, the MrNasdog Pressure Framework reads **PYTH at +26.95% net**: sell pressure of **2,125M PYTH** against buy pressure of **2.95M PYTH**, on a tradable base of **7,874.97M PYTH**. Our supply monitor reads **+36.71%** for the same period, a gap of **9.77 percentage points**, and the page carries a monitor-gap note because that exceeds the framework's half-point tolerance. The gap is not a disagreement about what happened. Both numbers measure the identical Pyth Network cliff; the monitor sizes it against the pre-unlock float of **5.76B PYTH**, while the framework sizes it against today's larger float of **7.87B PYTH**, and running the same token delta through the two bases reproduces the gap to within a tenth of a point. PYTH is best labelled a **fixed-cap token with a single annual dilution event** — sharply inflationary on one calendar day a year, and quiet on every other.

## Sell pressure: where new PYTH comes from

Nowhere, in the literal sense. Protocol inflation on Pyth Network is **0**, and that zero is permanent rather than merely current: the PYTH mint on Solana carries no mint authority and no freeze authority, a state that cannot be reversed once set, so the **10,000,000,000** tokens issued at genesis in November 2023 are all the PYTH that will ever exist. Pyth also closed the one channel that could have looked like emission — the oracle integrity staking reward rate was set to **0** by governance on **Apr 22 2026**, and the leftover reward pool of **849,208 PYTH** was withdrawn back to the Pyth DAO treasury on **Jul 23 2026**, leaving a residue of **84,834 PYTH** in the retired pool. Staking and slashing still work; they simply pay nothing.

Vesting unlocks are therefore the whole of the sell ledger, and they are lumpy by design. Pyth Network locked **85%** of supply at launch and releases it in four equal annual cliffs of **2,125M PYTH** at six, eighteen, thirty and forty-two months after the token generation event. The thirty-month cliff fired on **May 19 2026**, inside this window, which is the entire **+26.95%**. Its composition matters: roughly **1.13B** went to ecosystem growth and **537.5M** to publisher rewards, both of which remain protocol-controlled rather than immediately tradable, with the remaining **457.5M** spread across protocol development, private sales and community allocations. Foundation and unscheduled unlocks read **0**, because no dated discretionary release was found anywhere in the window. Long-term locked or bankruptcy reads **0** for the simplest reason available: PYTH has never been part of a bankruptcy estate, so there is no trustee schedule to draw down.

## Buy pressure: where new PYTH goes

The one live buy-side mechanism is the Pyth Reserve, a programmatic buyback the Pyth DAO approved in December 2025. Each month roughly a third of the DAO treasury's non-PYTH assets is passed to the Pythian Council operations multisig, which buys PYTH on the open market under slippage and per-transaction limits and returns it to the DAO treasury. Two firings land inside this window: **1.80M PYTH** on **Jun 9 2026** and **1.15M PYTH** on **Jul 29 2026**, totalling **2.95M PYTH**. The treasury token account holds **37.8M PYTH** today. Note the destination carefully — bought PYTH is **held in the reserve, not destroyed**, so it reduces float only for as long as the DAO chooses to sit on it.

Protocol fee burn reads **0** because Pyth Network has no burn of any kind. A proposal to split each reserve purchase and destroy part of it was floated on the Pyth DAO governance forum in **June 2026**, alongside a separate idea to burn Entropy protocol fees, but neither has reached a vote, so not one PYTH has ever been removed from supply. Foundation buy reads **0** because the DAO reserve is the only buyer on the network and it is already counted as the buyback. New long-term lock reads **0** for two reasons at once: oracle staking rewards pay nothing since April 2026, so no fresh lock-up is being created, and counting reserve accumulation again here would double-count the buyback.

## Foundation and overhang

The overhang on PYTH is large and unusually legible. First, **2,125M PYTH** remains locked until the final cliff on **May 19 2027** — a figure that is not an estimate but an exact arithmetic residue, since the on-chain supply of **9,999.97M** minus the tradable **7,874.97M** lands on that number to the token. Second, the ecosystem growth allocation of roughly **1.13B PYTH** and the publisher reward allocation of **537.5M PYTH** released in May 2026 are counted as tradable by market classifiers but are still held by the protocol and deploy by discretion, with no published release schedule. Third, the Pyth DAO treasury holds **37.8M PYTH** in the reserve, and a retired staking reward pool holds a further **84,834 PYTH**. The operations multisig holds **0**, swept clean each buyback cycle. All four are watched on-chain and all four carry the same trigger: if any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How PYTH compares to other fixed-cap utility tokens

Compared to an uncapped continuous-emission Layer 1, PYTH is a different animal entirely. A chain that pays validators from new issuance dilutes every single day, and its holders can never point to a date on which dilution stops; Pyth Network dilutes on exactly four dates in its entire history, three of which have already passed. That trade is worth naming honestly: continuous emission is small and relentless, while the Pyth Network cliff model is enormous and rare. A holder who owns PYTH from June to April sees zero new supply; a holder who owns it across a May cliff absorbs a quarter of the float in a single step.

Compared to a halving-model token with a hard cap, PYTH shares the fixed ceiling but not the smoothing. Bitcoin's cap is enforced by a subsidy that decays geometrically, spreading the last of the supply over a century; Pyth Network's cap is enforced by a mint authority that was simply deleted, and the remaining supply arrives on one day in 2027. Compared to exchange tokens with quarterly buyback-and-burn, PYTH is one structural step behind: the buyback exists and is funded by real oracle and data-subscription revenue, but the destination is a treasury rather than a dead address, so the reserve is a claim the DAO could reverse rather than supply that is gone. The June 2026 burn discussion is precisely an attempt to close that gap, and it is the single most important thing to watch on the buy side.

## What to watch in the next 90 days

First, the monthly Pyth Reserve purchase reports, which have run at **2.57M**, **1.80M** and **1.15M PYTH** across May, June and July 2026 — a declining sequence that determines whether the forward **4.4M** estimate holds. Second, any governance vote on the partial-burn split floated in June 2026; a passed burn converts the reserve from an overhang into genuine supply destruction and would move this page from a fractional negative to a real one. Third, the Pyth Core sunset and cross-chain fee repatriation proposals moving through the DAO in **August 2026**, which change how much revenue reaches the treasury and therefore how large each buyback is. Fourth, any drawdown from the ecosystem growth allocation unlocked in May 2026, which is the largest single discretionary pool on the network. Fifth and furthest out, the final vesting cliff on **May 19 2027** — outside this window, but the last dilution event PYTH will ever have.

## Summary

The MrNasdog Pressure Framework reads Pyth Network at **+26.95%** net supply over the last 90 days and **−0.06%** over the next 90, an inflation score of **4 out of 5**. The structural mechanism is unusually clean: PYTH cannot be minted, cannot be frozen, pays no staking rewards and burns nothing, so its supply is a four-step staircase and three steps have already been taken. The key risk is concentration rather than rate — one date a year moves a quarter of the float, and the ecosystem growth and publisher reward allocations released in May 2026 sit in protocol hands with no published release schedule, counted as tradable while behaving as an overhang. The ceiling is absolute at **10,000,000,000 PYTH**, of which **2,125M** remains locked until **May 19 2027**, after which Pyth Network has no dilution left at all.

---

*MrNasdog Pressure Framework analysis of PYTH, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 17 2026.*

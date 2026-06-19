---
title: "OHM Inflation Analysis · June 2026 · Supply shrinking as the burn outruns the mint"
description: "A MrNasdog Pressure Framework read of Olympus (OHM): rebase APY retired, no vesting vs ~0.30M / 90D of treasury-yield buy-and-burn on ~14.96M circulating. Framework reads −2.0% net; monitor −4.86%."
canonical_url: "https://mrnasdog.com/research/ohm/inflation"
tags: ["crypto", "ohm", "olympus", "burn"]
published: true
---

> Originally published at **[mrnasdog.com/research/ohm/inflation](https://mrnasdog.com/research/ohm/inflation)** by MrNasdog.

Olympus retired its high-APY staking rebase, so OHM adds **no new supply on net** over the next 90 days — new OHM is minted only when the token trades above its treasury backing, and there is no vesting left to unlock. Meanwhile a yield-funded facility buys and burns roughly **0.30M OHM** a quarter. The framework reads about **−2.01% net** on **~14.96M** circulating. Our supply monitor reads the trailing 90 days at **−4.86%**, a **2.85 percentage-point** gap, so the page carries a monitor-gap flag.

## The verdict, in one paragraph

For the 90-day window from June 20 2026, the MrNasdog Pressure Framework reads **OHM at about −2.01% net** — supply shrinking, driven entirely by the burn rather than by anything new entering the float. Our supply monitor reads the realized last-90-day change at **−4.86%**, a gap of **2.85 percentage points**, so the page ships a **monitor-gap flag**. The gap is a mechanism artefact rather than a conflict: the trailing window front-loaded a heavier burn because the Yield Repurchase Facility buys more OHM per dollar as the price falls, and that pace has since decelerated to roughly **0.30M OHM** a quarter. The framework projects the recent rate, not the front-loaded one. OHM is best characterised as a **treasury-backed reserve currency that now burns more than it mints** — structurally deflationary on the active float, but at a rate that tracks treasury yield and price.

## Sell pressure: where new OHM comes from

On net, no new OHM comes from anywhere this window. Sell #1 — protocol inflation — is zero: Olympus has retired the old high-APY staking rebase entirely, and new OHM is now minted only by the **Emissions Manager**, which activates solely when OHM trades at a **100%** or larger premium to its measured treasury backing. Because supply contracted across the trailing window, that minting added nothing on net, and the framework projects no new OHM into the float. Sell #2 — vesting unlocks — is also zero: the Olympus DAO formally ended all future unlocks and allocations, so OHM is effectively fully circulating and supply is set by policy rather than a calendar. There is no scheduled unlock cliff inside the window.

Sell #3 — Foundation and unscheduled unlocks — is zero in the window. The Olympus treasury — its sUSDS reserves, the gOHM collateral locked in Cooler loans, and the roughly **4.88M OHM** between circulating and total supply — is the standing team-controlled overhang. But treasury OHM leaves only through the price-gated Emissions Manager, not a discretionary calendar release, and no such release is dated inside these 90 days. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate or court distribution applies to OHM.

## Buy pressure: where new OHM goes

The buy side is the whole story for OHM, and it is a burn story. Buy #1 — programmatic buyback — is zero as a separate line, because Olympus runs no accumulation buyback: the **Yield Repurchase Facility** buys OHM and then burns it rather than parking it in a treasury wallet, so that activity is booked under the fee burn below and never double-counted. Buy #2 — protocol fee burn — is about **0.30M OHM** over the trailing 90 days, and it is the reason supply is shrinking. The Yield Repurchase Facility uses treasury yield — roughly **6.5M dollars a year** from sUSDS reserves and Cooler-loan interest — to buy OHM daily on a price-agnostic basis, then borrows USDS against it at backing value and burns the OHM. The burn is **price-dependent**: as OHM falls, the same dollar yield buys and burns more tokens. Buy #3 — Foundation buy — is zero: there is no discretionary open-market purchase beyond the yield-funded burn already counted. Buy #4 — new long-term lock — is zero: borrowers lock gOHM in Cooler loans, which holds supply off the free float, but that is standing collateral rather than a new disclosed lockup that fired in the window.

## Foundation and overhang

OHM carries a sizeable structural overhang, all of it policy-gated rather than scheduled. The **Olympus treasury** — sUSDS reserves plus the gOHM collateral locked in Cooler loans — together with the roughly **4.88M OHM** of headroom between the ~14.96M circulating and the ~19.84M total supply, is the standing team-controlled overhang. None of it has a release dated inside this window. Treasury OHM can only re-enter the float through the Emissions Manager, and only when OHM trades above a 100% backing premium, so the overhang is throttled by price rather than by a calendar. The framework re-checks the DAO governance forum, the published burn activity and the treasury policies on a roughly bi-weekly walk; none books a discretionary sell value today, and each is tracked as scope. If the treasury or Emissions Manager releases OHM between refreshes, the outflow enters Sell #3 at the next refresh.

## How OHM compares to other reserve-currency and buyback tokens

OHM belongs to the class of **treasury-backed reserve-currency tokens** whose supply is steered by policy rather than a fixed schedule. Unlike a continuous-emission proof-of-stake Layer-1 that mints fresh tokens forever to pay validators, Olympus mints OHM only above a backing premium and otherwise removes it, so its supply growth can be negative for an entire quarter. Unlike a halving-model coin whose supply still grows — only more slowly each cycle — OHM has no structural source of new supply at all when it trades below premium.

The closer comparison is to **exchange tokens with revenue-funded buybacks**. Both use protocol cash flow to buy and burn the token. The difference is the funding source and the timing: an exchange token burns a share of trading fees on a quarterly schedule, while Olympus burns continuously from **treasury yield** and accelerates that burn as the price falls, because a fixed dollar yield buys more OHM at a lower price. That makes OHM **countercyclical** — the burn is strongest exactly when the price is weakest — whereas a fee-funded buyback weakens when activity dries up. The trade-off is that OHM's deflation is **yield-dependent and price-dependent**: it scales with how much the treasury earns and how cheap OHM is, so the −2.01% is a function of those inputs, not a fixed rule.

## What to watch in the next 90 days

Watch the running **Yield Repurchase Facility** burn rate — this is the only live driver of the reading, and a change in treasury yield or in OHM's price moves the quarterly burn directly. Watch the **OHM premium to backing**: if OHM climbs above a 100% premium, the Emissions Manager turns on and begins minting and selling new OHM, which would push the net back toward neutral or positive. Watch the **Olympus DAO governance forum** for any change to the Emissions Manager base rate, the Yield Repurchase Facility configuration, or treasury allocation, each of which would re-rate the supply path. Watch the **Cooler-loan** origination LTV drip, which changes how much gOHM is locked as collateral. And watch treasury yield itself, since the entire burn is funded by it.

## Summary

OHM is a treasury-backed reserve currency whose supply is now steered by two policies: an Emissions Manager that mints new OHM only above a 100% backing premium, and a Yield Repurchase Facility that buys and burns OHM from treasury yield. The next 90 days add no new OHM on net — no rebase, no vesting and no scheduled treasury release — while the facility burns about 0.30M OHM, leaving the framework at about −2.01% net on ~14.96M circulating. Our supply monitor reads −4.86% over the trailing window, 2.85 percentage points deeper, because the burn front-loaded when OHM was cheaper and has since decelerated; the page carries a monitor-gap flag. The key risk ahead is that the deflation is yield- and price-dependent, and a climb above the backing premium would flip the Emissions Manager back on; the structural backstop is that every OHM remains treasury-backed.

---

*MrNasdog Pressure Framework analysis of Olympus (OHM), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 20 2026.*

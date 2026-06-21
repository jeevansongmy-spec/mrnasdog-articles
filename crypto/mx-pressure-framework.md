---
title:         "MX Inflation Analysis · June 2026 · Mixed last 90 days, projected to shrink"
description:   "No mint and no burn fired in window → 0.00% net vs monitor −0.25%. Quarterly profit-funded buyback-and-burn (~2.5M MX) due ~Jul 2026; ~317M held in named reserves."
canonical_url: "https://mrnasdog.com/research/mx/inflation"
tags:          ["crypto", "mx", "mexc", "exchange-token"]
published:     true
---

*Originally published at [mrnasdog.com/research/mx/inflation](https://mrnasdog.com/research/mx/inflation)*

MX Token (MX), the exchange token of MEXC, has no mint function and a quarterly buyback-and-burn funded by **40% of platform profit**. No burn fired in the trailing 90 days, so the framework reads MX at **0.00% net** over the window on a ~91.84M circulating base — in line with the monitor's **−0.25%**. The next quarterly burn is due ~Jul 2026, projecting **~−2.7% net** for the following 90 days. MX is a managed float trimmed by an event-driven burn, not a continuous emission.

## The verdict, in one paragraph

For the 90-day window ending June 21 2026, the framework reads **MX at 0.00% net inflation**: there is no protocol issuance and no MX burn fired inside the window, so neither side of the ledger moved. The inflation monitor reads **−0.25%** over the same window — a gap of only **0.25 percentage points**, comfortably inside tolerance, so no warning chip is raised. The reason the two agree is structural: MEXC's quarterly burn reduces the non-circulating reserve and the total token count, while the circulating float is managed toward a ~100M target, so a burn does not register as a circulating-supply shrink in the monitor's series. Looking forward, the next quarterly buyback-and-burn (Q2 2026) is expected ~Jul 2026, which lands in the next 90 days and projects **~−2.7% net**. MX is a quiet float today, deflationary on its next scheduled burn event.

## Sell pressure: where new MX comes from

Nowhere — every MX sell row reads zero. Sell #1 (protocol inflation) is **0** because MX has no mint function: it is a fixed-supply ERC-20 exchange token, so no new MX is issued and the only supply movement is removal through burns. Sell #2 (vesting unlocks) is **0**; the MX non-circulating reserves carry no published vesting calendar, and MEXC manages the circulating float toward a ~100M target rather than on a fixed cliff schedule, so there is no scheduled unlock in the window. Sell #3 (Foundation and unscheduled unlocks) is **0** with no observed release of MX from any reserve in the window. Sell #4 (bankruptcy) is **0**; no estate distributes MX.

## Buy pressure: where new MX goes

The MX buy side is event-driven, and no event fired this window. Buy #1 (programmatic buyback) is **0** for the trailing 90 days: MEXC funds a quarterly buyback-and-burn from **40% of platform profit** and sends the repurchased MX to an on-chain burn destination, verifiable on Ethereum, but the last confirmed round destroyed **~2.581M MX** on Oct 16 2025, and no Q1 2026 burn had been announced before this window closed — so no burn landed between March and June 2026. Buy #2 (protocol fee burn) is **0**; MX has no continuous protocol-level fee burn — all destruction runs through the quarterly buyback captured in row #1. Buy #3 (Foundation buy) and Buy #4 (new long-term lock) are both **0** — there is no separate accumulation programme and no new lockup with an announced quantum. The forward read is the Q2 2026 burn, projected at **~2.5M MX** from the quarterly schedule.

## Foundation and overhang

The MX overhang is large and named. The ~409M on-chain total minus the ~91.84M circulating leaves roughly **~317M MX** in three team-controlled reserves established in the 2021 MX Token 2.0 plan: the **MEXC Foundation Reserve (~100M)**, **MEXC Labs (~150M)**, and a **Strategic Partnership allocation (~100M)**. None of these carries a published release schedule — MEXC manages the circulating float administratively toward its ~100M target, which means the reserve is the supply that could in principle enter the market. The framework monitors these wallets on a bi-weekly walk rather than projecting a value. If any reserve's balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How MX compares to other exchange tokens

MX sits in the revenue-funded-burn cohort of exchange tokens, alongside BNB, OKB, GT and KCS — all of which remove supply using a slice of exchange profit rather than minting new tokens. Mechanically MX is closest to a quarterly-schedule burner: like GT and OKB it destroys MX in scheduled rounds tied to platform revenue, where BNB runs an automated quarterly auto-burn and KCS burns monthly in smaller relative quanta. The distinguishing feature of MX is the **managed float**: MEXC explicitly targets ~100M circulating, so its burns reduce the reserve and total supply more visibly than they shrink the freely-tradable float — the opposite emphasis of a token like GT, where ~62% of genesis has been permanently destroyed and the circulating count falls every quarter.

Against fixed-cap mining assets the contrast is sharper still. A proof-of-work chain's scarcity is fixed in code through a hard cap and a halving schedule, so its trajectory is knowable years ahead. MX's deflation is contingent on MEXC's profitability — a weaker quarter funds a smaller burn, and recent rounds (Q4 2024 ~3.39M, Q1 2025 ~2.206M, Q2 2025 ~2.398M, Q3 2025 ~2.581M) show exactly that revenue sensitivity. MX trades the certainty of a coded schedule for a burn whose size tracks the exchange's business.

## What to watch in the next 90 days

Three items move the MX framework reading. First, the **Q2 2026 buyback-and-burn**, expected ~Jul 2026 — projected at ~2.5M MX; a materially larger or smaller round shifts the next-90D reading directly, and its publication will confirm the quarterly schedule held. Second, any movement of MX out of the **~317M named reserves** — an observed outflow from the Foundation Reserve, MEXC Labs, or the Strategic Partnership wallet would activate Sell #3 at the next refresh. Third, any change to the **40%-of-profit** burn commitment or the ~100M circulating target — a governance or policy update there would re-rate both the burn size and the managed-float assumption underpinning this read.

## Summary

MX is a no-mint MEXC exchange token whose supply is removed by a quarterly profit-funded buyback-and-burn. No burn fired in the trailing 90 days, so the framework reads **0.00% net** for the window — matching the monitor's −0.25% with no warning chip — while the next round (~Jul 2026) projects **~−2.7% net** for the following 90 days. The key dependency is MEXC's profitability, which sets the burn size, and the key watch item is the ~317M held in three named reserves against a managed ~100M circulating float. MX is quiet today and deflationary on its next scheduled event.

*MrNasdog Pressure Framework analysis of MX, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 21, 2026.*

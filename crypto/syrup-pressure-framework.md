---
title:         "SYRUP Inflation Analysis · June 2026 · Supply Growing, But the Emission Ends in September"
description:   "Inherited 5%/yr emission runs to Sep 2026; a 25%-of-revenue buyback removes ~6M. Framework reads +2.27% net on a ~1.19B uncapped float."
canonical_url: "https://mrnasdog.com/research/syrup/inflation"
tags:          ["crypto", "syrup", "maple", "defi"]
published:     true
---

*Originally published at [mrnasdog.com/research/syrup/inflation](https://mrnasdog.com/research/syrup/inflation)*

# SYRUP Inflation Analysis · June 2026 · Supply Growing, But the Emission Ends in September

Maple Finance still mints SYRUP under an inherited **5%-per-year emission** that runs to September 2026 — roughly **33M new SYRUP** over the next 90 days. A **25%-of-revenue buyback** into the Syrup Strategic Fund removes about **6M**. Framework reading: **+2.27% net** on a ~1.19B float with no hard cap. SYRUP is mildly inflationary today, but the meter resets when the emission schedule expires.

## The verdict, in one paragraph

For the 90-day window ending June 21 2026, the Pressure Framework reads **SYRUP at +2.27% net inflation** — about **33M** of new SYRUP enters from the protocol emission, against roughly **6M** bought back into the Syrup Strategic Fund. The inflation monitor reads **+2.82%**, a gap of **0.56 percentage points**. That gap is wide enough to carry a **monitor-gap flag**: the monitor counts circulating supply as market cap divided by price, so it still includes the SYRUP that Maple has bought back and is holding in the strategic fund — the framework nets that ~6M out, the monitor does not. SYRUP is **structurally inflationary on the float for one more quarter** while the inherited emission runs down.

## Sell pressure: where new SYRUP comes from

The only sell-side row that carries a value is **Sell #1 Protocol inflation**, at **~33M SYRUP** over 90 days. This is not staking emission — Maple sunset staking rewards in November 2025 under MIP-019. It is an **inherited 5%-per-year emission schedule** that came across in the MPL recapitalization: a three-year emission running October 2024 through September 2026, funding the Maple Treasury. Maple's own documentation puts the expected supply at **~1,267.88M SYRUP by September 2026**; on-chain total supply is already **1,244.68M**, with circulating at **1,191.85M**. The supply is still drifting up, but the schedule has a hard end date.

Every other sell-side row is zero. **Sell #2 (vesting unlocks)** is zero because there are no cliffs in the window — the team, investor, and public allocations are fully unlocked, and the MPL→SYRUP conversion closed in May 2025. **Sell #3 (Foundation and unscheduled unlocks)** is zero because there is no discretionary release beyond the scheduled emission, though the non-circulating treasury and the strategic fund are tracked as overhangs. **Sell #4 (bankruptcy)** is zero — Maple has no bankruptcy estate distributing SYRUP.

## Buy pressure: where SYRUP goes

The buy side is **Buy #1 Programmatic buyback**, at **~6M SYRUP** over 90 days. Under MIP-019, Maple routes **25% of protocol revenue** into the Syrup Strategic Fund, which buys SYRUP from the open market. The first buyback in November 2025 was **2M SYRUP**; revenue has since grown — April 2026 revenue was $793K and May 2026 was **$1.4M** — so 25% at the current SYRUP price implies a steady run-rate of about **6M SYRUP per quarter**. The bought-back tokens accumulate in the strategic fund rather than being burned, which is why the monitor still counts them.

**Buy #2 (protocol fee burn)** is zero — Maple does not burn SYRUP; revenue funds the buyback instead. **Buy #3 (Foundation buy)** is zero, since the revenue buyback already captures all programmatic accumulation. **Buy #4 (new long-term lock)** is zero — staking, which would have locked SYRUP, was retired in November 2025, and no replacement lockup has been announced.

## Foundation and overhang

Two team-controlled overhangs sit behind the float. First, the **non-circulating treasury** — about **52.8M SYRUP** (on-chain total of 1,244.68M minus circulating of 1,191.85M) that has not yet entered circulation. Second, the **Syrup Strategic Fund**, where the revenue buybacks accumulate; this balance grows by roughly 6M per quarter and is tracked through Maple's official disclosures rather than a single published wallet. Neither is releasing supply to the market today. If the Syrup Strategic Fund's balance falls between refreshes — that is, if Maple sells from the fund rather than holding — that outflow enters Sell #3 at the next refresh.

## How SYRUP compares to other revenue-funded DeFi tokens

SYRUP belongs to the small group of DeFi tokens that route protocol revenue back into the token. The closest analogues are Aave's AAVE and Hyperliquid's HYPE. AAVE's $50M-per-year buyback now exceeds its reduced Safety Module emission, so AAVE reads net deflationary; HYPE buys back aggressively from perp fees and is firmly deflationary. SYRUP is one step behind both, for a structural reason: it still has an active **5%-per-year emission** to outrun. Its ~6M-per-quarter buyback is real, but the ~33M emission is larger, so the net is still positive.

The difference from a fixed-cap token is the key point. SYRUP has **no hard cap** — supply is technically infinite — but the inherited emission is a one-time schedule, not a perpetual inflation rate. Once it expires in September 2026, the only flows left are the revenue buyback (removing SYRUP) and whatever new emission governance might choose to vote in. If nothing new is added, SYRUP flips from mildly inflationary to net deflationary on the buyback alone — the same place AAVE reached when its emission was cut below its buyback.

## What to watch in the next 90 days

Three things move the framework reading. First, the **September 2026 emission expiry** — when the inherited 5%-per-year schedule ends, Sell #1 drops toward zero and the buyback becomes the dominant flow. Second, **Maple protocol revenue** — the buyback is 25% of revenue, so the ~6M quarterly pace scales directly with Maple hitting its $100M ARR target for end-2026; faster revenue means a larger buyback and a quicker flip to deflation. Third, any **governance vote on a new emission** — there is no hard cap, so the DAO could authorise fresh issuance after September 2026, which would keep Sell #1 alive.

## Summary

SYRUP is a ~1.19B-float, uncapped DeFi governance token whose supply is still growing under an inherited 5%-per-year emission that expires in September 2026. The framework reads **+2.27% net** for the trailing 90 days — about 33M of new SYRUP against a ~6M revenue-funded buyback — versus a monitor reading of +2.82%, a 0.56pp gap explained by the bought-back SYRUP that the monitor still counts as circulating. The structural risk is a new emission vote after the schedule ends; the structural upside is that, with the emission gone and the buyback intact, SYRUP would flip net deflationary. For now it is mildly inflationary, with a clear date on the calendar when that changes.

---

*MrNasdog Pressure Framework analysis of SYRUP (Maple Finance), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 21, 2026.*

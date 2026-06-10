---
title: "GT Inflation Analysis · June 2026 · Supply shrinking, projected to keep shrinking"
description: "A MrNasdog Pressure Framework read of GateToken (GT): quarterly revenue burn destroyed ~2.56M GT against zero sell flow. Framework reads −2.40% / 90D; ~62% of genesis already burned. Structurally deflationary."
canonical_url: "https://mrnasdog.com/research/gt/inflation"
tags: ["crypto", "gt", "gatetoken", "exchange"]
published: true
---

> Originally published at **[mrnasdog.com/research/gt/inflation](https://mrnasdog.com/research/gt/inflation)** by MrNasdog.

GateToken (GT) has no mint function and a quarterly revenue-funded burn that destroyed **~2.56M GT** on Apr 25 2026 against zero sell-side flow. Framework reading: **−2.40% net** over the trailing 90 days on a ~106.5M circulating base. About 62% of the 300M genesis supply has already been burned — GT is one of the most structurally deflationary exchange tokens in coverage.

## The verdict, in one paragraph

For the 90-day window ending June 11 2026, the framework reads **GT at −2.40% net inflation** — the quarterly buyback-and-burn is the only live flow, and nothing on the sell side offsets it. The aggregator monitor reads **−33.93%** over the same window, a **31.5-percentage-point** gap that triggers the ⚠ chip. The deep walk resolved it: the monitor's 90-day-ago base (161M) exceeded GateToken's entire on-chain effective max (~113M = 300M genesis minus ~187M cumulatively burned) — an impossible figure, meaning the upstream circulating count was over-stated and corrected mid-window. The real in-window flow is the burn. GT is deflationary by structural buyback.

## Sell pressure: where new GT comes from

Nowhere — every sell row reads zero. Sell #1 (protocol inflation) is **0** because GateToken has no mint function: the supply was fixed at the 300M genesis (the original 1B was cut by a one-time 700M burn) and can only shrink. Sell #2 (vesting unlocks) is **0**; third-party unlock calendars list a multi-year linear vest for GT, but the locked total those calendars claim is larger than the token's entire remaining supply — inconsistent with the chain, so the framework does not adopt it. On-chain, at most **~6.1M GT** sits outside circulation. Sell #3 (Foundation and unscheduled unlocks) is **0** with no observed release event in the window. Sell #4 (bankruptcy) is **0**; no estate distributes GT.

The vesting question deserves one more sentence, because it is where this build differs from the previous one. The framework's supply-arithmetic check requires that any claimed locked allocation fit inside the gap between circulating supply and the on-chain maximum. For GateToken that gap is ~6.1M GT — so a calendar claiming hundreds of millions still locked, or even a single ~6M monthly unlock, cannot all be real. Rather than ship a number that fails arithmetic, the framework ships zero and watches the residual. If a verifiable unlock event appears on-chain, it enters the ledger at the next refresh with its observed quantum.

## Buy pressure: where new GT goes

The buy side carries the whole story. Buy #1 (programmatic buyback) booked **~2.56M GT** this window: the Gate platform funds a quarterly buyback-and-burn from its revenue — trading fees plus chain gas — and the Q1 2026 round destroyed 2,557,729 GT (~$20.7M) on Apr 25 2026, sent to an on-chain burn address. Cumulatively, **~187M GT** has been destroyed since 2019 — about 62% of genesis supply. Buy #2 (protocol fee burn) is **0** as a separate row; chain gas contributes to the quarterly burn budget rather than burning continuously, so the destruction is captured in row #1. Buy #3 (Foundation buy) and Buy #4 (new long-term lock) are both **0** — there is no separate accumulation programme and no new lockup with an announced quantum.

## Foundation and overhang

Two overhangs are tracked. First, the **non-circulating residual of ~6.1M GT** — the difference between the effective max (~112.6M) and the circulating count (~106.5M). It has no published schedule that survives supply arithmetic, so it is monitored on a bi-weekly walk rather than projected. Second, the exchange's own corporate treasury, whose size is not separately disclosed — monitored through official announcements. If either overhang's balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How GT compares to other exchange tokens

Among exchange tokens with revenue-funded burns, GT sits at the aggressive end by cumulative effect. BNB's quarterly auto-burn has destroyed roughly 30% of its genesis supply over a longer life; OKB's buyback-and-burn runs a comparable quarterly cadence; KCS burns monthly but in far smaller quanta relative to supply. GT's 62%-of-genesis cumulative burn is the highest ratio in this cohort, and the remaining float keeps shrinking every quarter the platform earns.

The structural difference from fixed-cap mining assets is the funding source: a PoW chain's scarcity comes from a hard cap and slowing emission, while GT's comes from corporate revenue actively removing supply. That makes GT's deflation contingent on platform performance — a quarter of weak exchange revenue shrinks the burn — where a halving-schedule chain's trajectory is fixed in code. Mechanism-wise, GT trades certainty of schedule for magnitude of effect.

## What to watch in the next 90 days

Three things move the framework reading. First, the **Q2 2026 quarterly burn**, expected ~Jul 25 2026 — projected at ~2.5M GT from the quarterly cadence; a materially larger or smaller round shifts the next-90D reading directly. Second, any movement in the **~6.1M non-circulating residual** — an observed outflow would activate Sell #3 at the next refresh. Third, the upstream circulating count — this window's 31.5-point monitor gap came from a data correction there, and a further re-baseline would re-widen the chip.

## Summary

GateToken is a no-mint exchange token whose supply only shrinks: a quarterly revenue-funded buyback-and-burn destroyed ~2.56M GT this window against zero sell-side flow, putting the framework at **−2.40% net** for the trailing 90 days and roughly −2.35% projected for the next. The key dependency is platform revenue — the burn scales with it — and the key watch item is the ~6.1M non-circulating residual. With ~62% of genesis already destroyed, GT's ceiling keeps falling every quarter.

---

*MrNasdog Pressure Framework analysis of GT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 11, 2026.*

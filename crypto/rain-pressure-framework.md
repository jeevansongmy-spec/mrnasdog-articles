---
title: "RAIN Inflation Analysis · June 2026 · Supply growing, projected to keep growing"
description: "A MrNasdog Pressure Framework read of Rain (RAIN): Jun 10 2026 cliff moved ~50.4B (4.37% of supply) to market. Framework reads +8.09% net, monitor +30.40% (⚠). Heavy vesting on Arbitrum."
canonical_url: "https://mrnasdog.com/research/rain/inflation"
tags: ["crypto", "rain", "prediction-markets", "arbitrum"]
published: true
---

> Originally published at **[mrnasdog.com/research/rain/inflation](https://mrnasdog.com/research/rain/inflation)** by MrNasdog.

Rain, the prediction-market protocol on Arbitrum, is in a young, heavy vesting schedule: the verified Jun 10 2026 cliff alone moved **~50.4B RAIN** (4.37% of total supply) into the market against a negligible buyback. The Pressure Framework books **+8.09% net** inflation over the trailing 90 days from that cliff alone, while the monitor reads **+30.40%** — a heavily inflationary token whose true sell-side flow is larger than the page conservatively books.

## The verdict, in one paragraph

For the 90-day window the framework reads **RAIN at +8.09% net** inflation, booking only the verified Jun 10 2026 unlock cliff. The inflation monitor reads **+30.40%** over the same window — a gap of **22.31 percentage points** that triggers a ⚠ data-conflict chip. The deep walk explains it: the confirmed cliff (~50.4B) accounts for about a third of the +145B the monitor observed, and the remainder is the continuous linear vest that has run since Mar 10 2026, whose week-by-week quantum sits behind paywalled trackers this session. Critically, this is the rare case where the framework reads LOWER than reality — RAIN is structurally inflationary on a vesting flood, and the true flow is larger, not smaller.

## Sell pressure: where new RAIN comes from

The sell side is the whole story. **Protocol inflation** is zero — RAIN has a **1.15T** hard cap, fully minted, with no emission mechanism; supply growth comes from vesting, not new mint. **Vesting unlocks** booked **~50.4B RAIN**: the vesting programme started Mar 10 2026 and runs both a continuous linear stream and large monthly cliffs, and the Jun 10 2026 cliff moved ~50.4B (4.37% of total supply) into the transferable pool in a single event — confirmed by three independent trackers. The next cliff is expected ~Jul 10 2026. **Foundation and unscheduled unlocks** are recorded as zero in the active flow because the releases run through the scheduled vesting rather than discretionary deploys — but the locked buckets behind that schedule are large (covered below). **Bankruptcy** is zero.

## Buy pressure: where new RAIN goes

The buy side is structurally negligible against the unlock flood. **Programmatic buyback** is zero as a standalone row — the buyback half of Rain's 5% trading fee feeds the burn, not a separate accumulation wallet. **Protocol fee burn** is zero at display precision: 2.5% of trading volume funds an automatic buyback-and-burn, but cumulative destruction is only **~69M RAIN** against a 623B float, and the in-window quantum was not separately verifiable this session, so it is monitored rather than booked. **Foundation buy** and **new long-term lock** are both zero — no accumulation programme and no staking-lock with an announced quantum. In short, nothing on the buy side is large enough to offset even a single monthly cliff.

## Foundation and overhang

RAIN's overhang is enormous and front-loaded. The published allocation buckets — Reserve & Treasury at 20% of supply, Treasury at 18%, and Team & Shareholders at 22.5% (mostly locked) — leave over **526B RAIN** still outside circulation by supply arithmetic (total 1,149.87B minus circulating 623.36B). These release through the scheduled monthly cliffs and the continuous linear stream rather than through discretionary deploys, and the bucket structure is walked bi-weekly. If any of these balances falls between refreshes faster than the published schedule implies, the outflow enters Sell #3 at the next refresh. The standing follow-up is to read the Arbitrum vesting contract's events directly to quantify the linear stream rather than infer it.

## How RAIN compares to other heavy-unlock launches

RAIN belongs to the young, high-float-expansion cohort — tokens in the first year of a multi-year vesting schedule where unlocks dominate every other supply flow. Mechanically it resembles other recent launches whose monthly cliffs and linear streams add several percent of supply per quarter, and it sits at the heavy end: a single Jun 10 2026 cliff alone is 4.37% of total supply. The contrast with mature fixed-cap tokens is total — where a Litecoin or a PEPE has nothing material moving, RAIN's circulating count is still expanding toward its 1.15T cap with more than half the supply yet to unlock.

The defining mechanism is the schedule itself: vesting against a near-empty buy side. The 5% trading-fee burn is real but cumulatively trivial (~69M), so unlike an exchange token where revenue burns offset emissions, RAIN has no structural counterweight to the unlock. Until the linear stream tapers or the buyback scales by orders of magnitude, the framework will keep reading RAIN as one of the more inflationary tokens in coverage — and the ⚠ chip flags that the booked figure is a conservative floor.

## What to watch in the next 90 days

Three things move the reading. First, the **~Jul 10 2026 cliff** — the next monthly unlock, expected at a similar ~50B scale, lands inside the next window and books directly into Sell #2. Second, the **continuous linear vest** — a contract-level read of the Arbitrum vesting events would quantify the residual the monitor sees and likely raise the booked figure toward the monitor's +30%. Third, any **scaling of the buyback-and-burn** — only an order-of-magnitude increase from the current ~69M cumulative would begin to offset the unlock.

## Summary

RAIN is a 1.15T hard-cap prediction-market token on Arbitrum in the heavy phase of a vesting schedule that began Mar 10 2026, with a verified Jun 10 2026 cliff of **~50.4B** driving a framework reading of **+8.09% net** against a monitor reading of **+30.40%** — a 22.31-point gap carrying a ⚠ chip. The key risk is the over 526B still locked and unlocking on schedule, with a negligible buyback as the only counterweight. This is the unusual case where the framework deliberately books a conservative floor: RAIN's real sell-side flow is larger than the page shows.

---

*MrNasdog Pressure Framework analysis of RAIN, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 12, 2026.*

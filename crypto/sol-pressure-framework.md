---
title: "SOL Inflation Analysis · June 2026 · Staking issuance, disinflating each year"
description: "Staking issuance ~3.78%/yr (~5.87M SOL over 90 days) with only a tiny fee burn. Framework reads +1.01% net — inflationary but disinflating toward 1.5%."
canonical_url: "https://mrnasdog.com/research/sol/inflation"
tags: ["crypto", "solana", "staking", "layer1"]
published: true
---

> Originally published at **[mrnasdog.com/research/sol/inflation](https://mrnasdog.com/research/sol/inflation)** by MrNasdog.

Solana mints new SOL to pay stakers at about **3.78% a year** on-chain, roughly **5.87M SOL** over 90 days, with only a tiny base-fee burn offsetting it. Framework reading: about **+1.01%** net for the window against the inflation monitor's **+1.43%**. Supply is growing, but the issuance rate falls about 15% a year on a fixed schedule toward a 1.5% floor.

## The verdict, in one paragraph

For the 90-day window ending June 24 2026, the MrNasdog Pressure Framework reads **SOL at +1.01% net** on its circulating base. The independent inflation monitor reads **+1.43%**, a gap of **0.42 percentage points** — inside the 0.5pp tolerance, so no data-conflict chip is raised. Issuance is sized on the total-supply base (about 3.78% of roughly 628.95M total), and the small residual against the monitor is staking rewards re-entering circulation plus negligible estate movement on top of issuance, not a sizing error. SOL is **structurally inflationary but disinflating** — the rate is positive today and scheduled to keep falling.

## Sell pressure: where new SOL comes from

Sell #1 — protocol inflation — is the only material flow. On-chain, Solana's **getInflationRate** returns about **3.78% a year** as of June 2026, with the foundation share at zero and all issuance paid to validators and stakers. That is roughly **5.87M SOL** over the 90-day window. The rate sits on a published disinflation curve: it began at 8% at launch and falls about 15% a year toward a long-run 1.5% floor. Because issuance is a percentage of total supply rather than a fixed token amount, the framework sizes it on the total-supply base of roughly 628.95M SOL.

The rest of the sell ledger is booked zero. Sell #2 — vesting unlocks — is zero: team and early-backer vesting has fully expired, with no published unlock cliff in the next 90 days. Sell #3 — Foundation and unscheduled unlocks — is zero, with about 48.5M SOL non-circulating (foundation residual and stake-pool accounts) tracked but with no in-window discretionary deployment booked. Sell #4 — long-term locked or bankruptcy — is zero; the large FTX estate tranche unlocked back in early 2025, what remains is about 5M SOL in negligible monthly releases (tens of thousands of SOL a month), and the roughly 68% of supply that is staked locks SOL rather than adding it.

## Buy pressure: where new SOL goes

The buy ledger is empty at this scale. Buy #1 — programmatic buyback — is zero, because staking rewards are paid from fresh issuance rather than market purchases. Buy #2 — protocol fee burn — is non-zero but negligible: 50% of each base fee is burned, but the absolute pace is tiny next to 5.87M SOL of issuance, so it nets to zero at the precision shown. Buy #3 — Foundation buy — is zero; there is no accumulation programme. Buy #4 — new long-term lock — is zero as a programmatic line: staking locks SOL for yield but is validator-driven, not a programme with an announced lock quantum.

## Foundation and overhang

The tracked overhang is the **non-circulating pool** — about 48.5M SOL across foundation residual and stake-pool accounts, with no published in-window cliff. The framework books no in-window discretionary deployment, so its flow is zero for the period, but it is monitored on a roughly bi-weekly web walk. If this overhang's balance falls between refreshes — a tranche entering circulation faster than expected — the outflow enters Sell #3 at the next refresh. This pool, layered on top of issuance, is one source of the small residual between the framework reading and the monitor.

## How SOL compares to other uncapped Layer 1 chains

Solana is a **continuous-emission, uncapped Layer 1** with a disinflation curve — the same broad family as Ethereum, but with a key mechanism difference. Ethereum pairs its issuance with a full base-fee burn, so its net collapses toward zero; Solana burns only half of a tiny base fee, so almost all of its issuance reaches the float and the net stays clearly positive. Against a reserve-drain model like Cardano, where new supply is drawn from a depleting reserve at a falling rate, Solana's curve is a fixed percentage-of-supply schedule rather than a reserve mechanic.

What distinguishes SOL for an inflation reading is the **disinflation schedule**: today's 3.78% is not stable but falling about 15% a year toward 1.5%. So the +1.01% net is a number with a known downward trajectory — each year the same analysis should produce a lower issuance figure, absent a governance change to the curve. Two prior attempts to accelerate that curve, SIMD-0228 and SIMD-0411, both failed to pass, and a third, SIMD-0550 — filed June 2 2026 to double the disinflation rate to 30% a year — is still only at the proposal stage with no vote date, so the schedule is as-launched today. That is a structurally different shape from a fixed-rate emitter, whose number stays flat, or a capped halving chain, whose number steps down in discrete jumps.

## What to watch in the next 90 days

Watch the disinflation step — the issuance rate ratchets down on its annual schedule, so the next reading should be modestly lower. Watch the non-circulating pool's release pace, the most likely driver of any gap between the framework reading and the monitor; a faster-than-expected tranche would lift Sell #3 above zero. Watch the staking participation rate, which interacts with effective yield. And watch SIMD-0550, the live proposal to double the disinflation rate to 30% a year — if it advances to a validator vote and passes, the trajectory resets sharply lower. None of these is a single dated event; they are schedule and policy variables the next refresh re-reads.

## Summary

SOL is inflationary but on a falling path. Staking issuance of about 5.87M SOL over the window — roughly 3.78% a year on the total-supply base — is barely offset by a tiny fee burn, for a framework reading of +1.01% net against the monitor's +1.43%, a 0.42-percentage-point gap that stays inside tolerance. The small residual is staking rewards re-entering circulation plus negligible estate movement on top of issuance, not a sizing error, and the other ledger rows are booked zero-and-monitored rather than fabricated. The defining feature is the disinflation curve: the rate falls about 15% a year toward a 1.5% floor, so SOL's number is positive today but structurally trending down.

---

*MrNasdog Pressure Framework analysis of Solana (SOL), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 24, 2026.*

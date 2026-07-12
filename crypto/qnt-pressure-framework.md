---
title:         "QNT Inflation Analysis · July 2026 · Mixed flows, supply roughly steady"
description:   "Quant has issued no new QNT since 2018, vesting is long expired, and Overledger licence fees are locked in treasury not burned. Framework reads a flat 0.00% net."
canonical_url: "https://mrnasdog.com/research/qnt/inflation"
tags:          ["crypto", "qnt", "quant", "interoperability"]
published:     true
---

*Originally published at [mrnasdog.com/research/qnt/inflation](https://mrnasdog.com/research/qnt/inflation)*

# QNT Inflation Analysis · July 2026 · Mixed flows, supply roughly steady

Quant Network has issued no new QNT since its 2018 sale, its vesting is long expired, and the Overledger licence model locks tokens in treasury rather than burning them. Framework reading: **0.00% net** over the trailing 90 days, with the supply monitor at **-0.005%** — a gap of about **0.01pp**, well inside tolerance, so no conflict flag ships. Every row of the eight-row ledger reads zero, and the one thing worth watching is a large static treasury overhang.

## The verdict, in one paragraph

For the 90-day window ending July 13 2026, the framework reads **QNT at 0.00% net inflation** — a structurally flat ledger. The inflation monitor reads **-0.005%**, a gap of roughly **0.01 percentage points** that is pure market-cap-over-price noise; the two agree, so no monitor-gap chip ships. There is nothing happening on the supply side of QNT. No new tokens have been minted since the Quant token sale closed in 2018, the founder and advisor lockups from that sale expired years ago, and the Overledger licence model that drives Quant's revenue does not destroy supply. This is a fixed-supply, fully-distributed utility and governance token — quiet by structure.

## Sell pressure: where new QNT comes from

Sell #1 — protocol inflation — is **zero**. The QNT ERC-20 has issued no new tokens since the 2018 token sale; the on-chain **totalSupply() has read 45.47M** and been static for years. There is no staking-reward emission, no block reward, and no continuous mint. The framework uses the recognized circulating base of **14.54M QNT** — against a recognized cap of 14.61M — as its denominator.

Sell #2 — vesting unlocks — is **zero**, and permanently so. The 2018 sale placed founder and advisor allocations on one-year lockups that expired years ago; there are no remaining cliffs, no linear streams, and no future vesting events to model for the next 90 days or beyond. Sell #4 — long-term locked or bankruptcy — is also **zero**; there is no bankruptcy estate and no distressed-seller schedule attached to QNT.

Sell #3 — Foundation and unscheduled unlocks — is **zero** in flow but carries a large enumerated overhang. The contract's raw on-chain **totalSupply() reads 45.47M**, while only **14.54M** is recognized as circulating. The roughly **30.9M** difference sits in Quant-controlled and locked wallets — and strikingly, **9.55M** of it is held inside the QNT token contract itself, the single largest holder at about 21% of minted supply. That reserve is non-circulating and static across the window; no release into the market was observed, so the row is booked zero and monitored.

## Buy pressure: where new QNT goes

The buy ledger is equally empty. Buy #1 — programmatic buyback — is **zero**; Quant Network does not buy QNT on the open market. Buy #2 — protocol fee burn — is **zero**, and this is the load-bearing structural fact about QNT's tokenomics. The Overledger licence model is **use-and-lock**, not use-and-burn: enterprises pay annual licence fees that the Quant treasury settles in QNT, those tokens are locked in treasury for 12 months, and on expiry they return to the treasury. No QNT is destroyed, so there is no deflationary burn flow.

Buy #3 — Foundation buy — is **zero**; no treasury open-market accumulation was observed in the window. Buy #4 — new long-term lock — is **zero**; the 12-month licence locks are internal treasury locks on tokens Quant already holds, not fresh market-removing locks that pull circulating QNT off the float. Nothing on the buy side shrinks the tradable supply, which is why a coin often marketed as deflationary reads as an honest flat on the framework.

## Foundation and overhang

The one item worth watching is the treasury overhang. The gap between the **45.47M** tokens seen on-chain and the **14.54M** recognized as circulating — roughly **30.9M QNT**, more than twice the entire circulating float — is held in Quant's treasury and locked reserve wallets, with **9.55M** sitting inside the token contract itself. It is non-circulating, it has not moved into the market on any schedule, and the recognized supply is correctly capped at 14.61M. This overhang is tracked and re-read on-chain each refresh. If its balance falls — that is, if Quant begins moving treasury QNT into the market — the outflow would enter Sell #3 as real sell pressure at the next refresh. Today there is nothing of the sort.

## How QNT compares to other fixed-supply utility tokens

Among fixed-supply utility and governance tokens with completed vesting, QNT is one of the cleanest no-flow cases. The closest mechanism analogue is a token like YFI: a fixed cap, fully-completed vesting, no buyback, no burn — both read near zero for the same structural reason, that nothing is happening and nothing is designed to. That is the opposite shape from fee-burn chains like ETH and BNB, where usage actively destroys supply, and from quarterly-buyback exchange tokens where revenue is recycled into open-market purchases and the balance can go net-deflationary.

QNT's differentiator is the enterprise licence model: Overledger generates revenue without consuming supply, so the token is meant to capture value through rising demand — more enterprises licensing Overledger, more QNT locked in treasury — rather than through supply contraction. That is a demand-side story, and the inflation framework only measures the supply dimension. On that dimension QNT is flat, and structurally so. The large treasury reserve is the single thing that separates it from a token that is fully circulating; it is the reason QNT is an observed zero rather than a perfect one.

## What to watch in the next 90 days

For QNT the watch lines are unusually quiet. There are no scheduled supply events between now and mid-October 2026 — no unlock cliffs, no emission changes, no burns. Recent headlines — a Fusion Rollup connecting 74 chains on Jun 24 2026 and a renewed enterprise-and-bank focus around Jul 7 2026 — are demand and adoption news, not supply events, and do not touch the ledger. The framework reading should stay at 0.00% net unless something genuinely new happens: a buyback announcement, a governance change to the licence model, or a visible treasury deployment from the ~30.9M reserve. The single structural variable is whether Quant publishes a treasury transparency report, which would let the framework promote Sell #3 from a watched, zero-value overhang to a quantified row.

## Summary

QNT is a fixed-supply, fully-vested, no-flow asset. No new tokens have been issued since 2018, the vesting from that sale is long complete, the Overledger licence model locks tokens in treasury rather than burning them, and there is no buyback. The framework reads 0.00% net for the trailing 90 days and the monitor agrees to within about 0.01 points. The one structural feature is a large, static, non-circulating treasury overhang of roughly 30.9M QNT — the key risk to watch, but not a current flow. From a supply-pressure perspective, QNT is one of the quietest assets in coverage.

---

*MrNasdog Pressure Framework analysis of Quant (QNT), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 13 2026.*

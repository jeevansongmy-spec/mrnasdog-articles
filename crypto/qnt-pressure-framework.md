---
title:         "QNT Inflation Analysis · June 2026 · Mixed flows, supply roughly steady"
description:   "Quant has issued no new QNT since 2018, vesting completed 2019, and Overledger licence fees are locked in treasury not burned. Framework reads a flat 0.00% net."
canonical_url: "https://mrnasdog.com/research/qnt/inflation"
tags:          ["crypto", "qnt", "quant", "interoperability"]
published:     true
---

*Originally published at [mrnasdog.com/research/qnt/inflation](https://mrnasdog.com/research/qnt/inflation)*

# QNT Inflation Analysis · June 2026 · Mixed flows, supply roughly steady

Quant Network has issued no new QNT since its 2018 sale, all vesting finished in 2019, and the Overledger licence model locks tokens in treasury rather than burning them. Framework reading: **0.00% net** over the trailing 90 days, with the monitor at **+0.06%** — a gap of **0.06pp**, well inside tolerance, so no conflict flag. Every row of the eight-row ledger reads zero.

## The verdict, in one paragraph

For the 90-day window ending June 24 2026, the framework reads **QNT at 0.00% net inflation** — a structurally flat ledger. The inflation monitor reads **+0.06%**, a gap of just **0.06pp** that is pure mcap/price noise; the two agree. There is nothing happening on the supply side of QNT. No new tokens have been minted since the Quant token sale closed in 2018, the entire founder and advisor vesting finished by April 30 2019, and the Overledger licence model that drives Quant's revenue does not destroy supply. This is a fixed-supply, fully-distributed governance and utility token — quiet by structure.

## Sell pressure: where new QNT comes from

Sell #1 — protocol inflation — is **zero**. The QNT ERC-20 has issued no new tokens since the April 2018 token sale; the supply read on-chain has been static for years. There is no staking-reward emission, no block reward, no continuous mint. The framework uses the recognized circulating base of **14.54M QNT** (against a recognized cap of 14.61M) as its denominator.

Sell #2 — vesting unlocks — is **zero**, and permanently so. The original sale allocated 1.35M QNT to founders and 651K to advisors, both on one-year lockups that completed by April 30 2019. There are no remaining cliffs, no linear streams, and no future vesting events to model for the next 90 days or beyond.

Sell #3 — Foundation and unscheduled unlocks — is **zero** in flow but carries a large enumerated overhang. The QNT contract's raw on-chain **totalSupply() reads 45.47M**, while only **14.54M** is recognized as circulating. The roughly **30.9M** difference sits in Quant's own treasury and reserve wallets — non-circulating, and static across the window. No release into the market was observed, so the row is booked zero and monitored. Sell #4 — long-term locked or bankruptcy — is **zero**; there is no bankruptcy estate and no distressed-seller schedule attached to QNT.

## Buy pressure: where new QNT goes

The buy ledger is equally empty. Buy #1 — programmatic buyback — is **zero**; Quant Network does not buy QNT on the open market. Buy #2 — protocol fee burn — is **zero**, and this is the load-bearing structural fact about QNT's tokenomics. The Overledger licence model is **use-and-lock**, not use-and-burn: enterprises pay annual licence fees that the Quant treasury settles in QNT, those tokens are locked in treasury for 12 months, and on expiry they return to the treasury. No QNT is destroyed, so there is no deflationary burn flow.

Buy #3 — Foundation buy — is **zero**; no treasury open-market accumulation was observed in the window. Buy #4 — new long-term lock — is **zero**; the 12-month licence locks are internal treasury locks that move tokens the company already holds, not fresh market-removing locks that pull circulating QNT off the float. Nothing on the buy side shrinks the tradable supply.

## Foundation and overhang

The one item worth watching is the treasury overhang. The gap between the **45.47M** tokens seen on-chain and the **14.54M** recognized as circulating — roughly **30.9M QNT** — is held in Quant's treasury and reserve wallets. It is non-circulating, it has not moved into the market on any schedule, and the recognized supply is correctly capped at 14.61M. This overhang is tracked and re-read on-chain. If its balance falls — that is, if Quant begins moving treasury QNT into the market — the outflow would enter Sell #3 as real sell pressure at the next refresh.

## How QNT compares to other fixed-supply utility tokens

Among fixed-supply utility and governance tokens with completed vesting, QNT is one of the cleanest no-flow cases. The closest mechanism analogue is a token like YFI: a fixed cap, fully-completed vesting, no buyback, and no burn — both read near zero for the same structural reason, that nothing is happening and nothing is designed to. This is the opposite shape from fee-burn chains like ETH and BNB, where usage actively destroys supply, and from quarterly-buyback exchange tokens where revenue is recycled into open-market purchases.

QNT's differentiator is the enterprise licence model: Overledger generates revenue without consuming supply, so the token is meant to capture value through rising demand — more enterprises licensing Overledger, more tokens locked in treasury — rather than through supply contraction. That is a demand-side story, not a supply-side one, and the inflation framework only measures the supply dimension. On that dimension QNT is flat, and structurally so. The large treasury reserve is the single thing that separates it from a token that is fully circulating; it is the reason QNT is not a perfect zero, just an observed one.

## What to watch in the next 90 days

For QNT the watch lines are unusually quiet. There are no scheduled supply events between now and mid-September 2026 — no unlock cliffs, no emission changes, no burns. The framework reading should stay at 0.00% net unless something genuinely new happens: a buyback announcement, a governance change to the licence model, or a visible treasury deployment from the ~30.9M reserve. The single structural variable is whether Quant publishes a treasury transparency report, which would let the framework promote Sell #3 from a watched, zero-value overhang to a quantified row.

## Summary

QNT is a fixed-supply, fully-vested, no-flow asset. No new tokens have been issued since 2018, the last vesting completed in April 2019, the Overledger licence model locks tokens in treasury rather than burning them, and there is no buyback. The framework reads 0.00% net for the trailing 90 days and the monitor agrees within 0.06pp. The one structural feature is a large, static, non-circulating treasury overhang of roughly 30.9M QNT — the key risk to watch, but not a current flow. From a supply-pressure perspective, QNT is one of the quietest assets in coverage.

---

*MrNasdog Pressure Framework analysis of Quant (QNT), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 24 2026.*

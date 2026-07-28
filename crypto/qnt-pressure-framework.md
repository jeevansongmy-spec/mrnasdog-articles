---
title:         "QNT Inflation Analysis · July 2026 · Mixed flows, supply roughly steady"
description:   "Quant has issued no new QNT since 2018, vesting is long expired, and Overledger licence fees lock in treasury not burned. Framework reads a flat 0.00% net, monitor +0.03%."
canonical_url: "https://mrnasdog.com/research/qnt/inflation"
tags:          ["crypto", "qnt", "quant", "interoperability"]
published:     true
---

*Originally published at [mrnasdog.com/research/qnt/inflation](https://mrnasdog.com/research/qnt/inflation)*

# QNT Inflation Analysis · July 2026 · Mixed flows, supply roughly steady

Quant has issued no new QNT since its 2018 sale: the token's on-chain total supply is a frozen **45,467,000 QNT** with no working mint, its vesting is long expired, and the Overledger licence model locks tokens in treasury rather than burning them. The framework reads **0.00% net** over the trailing 90 days against a supply monitor at **+0.03%** — a gap of about **0.03pp**, well inside tolerance, so no conflict flag ships. Every row of the eight-row ledger reads zero, and the one thing worth watching is a large, static treasury overhang of roughly **30.9M QNT**.

## The verdict, in one paragraph

For the 90-day window ending **Jul 28 2026**, the Pressure Framework reads **QNT at 0.00% net** — a structurally flat ledger, with sell pressure of **0 QNT** and buy pressure of **0 QNT** against a circulating base of **14.54M QNT**. Our supply monitor reads the realised change at **+0.03%**, a gap of about **0.03 percentage points** that is pure market-cap-over-price noise, so no monitor-gap chip ships on the QNT overview. Nothing is happening on the supply side of Quant. No new tokens have been minted since the 2018 sale, the founder and advisor lockups from that sale expired years ago, and the Overledger licence model that drives Quant's revenue does not destroy supply. QNT is best characterised as a **fixed-supply, fully-distributed token whose inflation is structurally zero**.

## Sell pressure: where new QNT comes from

Sell #1, protocol inflation, is **zero**, and permanently so. The QNT ERC-20 at **0x4a220E60…48254675** has issued no new tokens since the 2018 sale; read directly this window, its on-chain **totalSupply() returned 45,467,000 QNT**, a clean round constant, and the mintable helpers on the contract revert when called, meaning there is no working mint path. There is no staking-reward emission, no block reward and no continuous issuance. The framework uses the recognized circulating base of **14.54M QNT** — against a recognized cap of **14.61M** — as its denominator, because that is the market's classification of the freely tradable float.

Sell #2, vesting unlocks, is **zero**. The 2018 sale placed founder and advisor allocations on one-year lockups that expired years ago; there are no remaining cliffs, no linear streams, and no future vesting events to model for the next 90 days or beyond. Sell #4, long-term locked or bankruptcy, is also **zero** — there is no Quant bankruptcy estate, no trustee and no court-ordered distribution attached to QNT. Sell #3, Foundation and unscheduled unlocks, is **zero** in flow but carries a large enumerated overhang. The contract's raw on-chain supply is **45.47M** while only **14.54M** is recognized as circulating; the roughly **30.9M** difference sits in Quant-controlled and locked wallets, and strikingly, **9.55M** of it is held inside the QNT token contract itself, the single largest holder at about 21% of minted supply. That reserve is non-circulating and static across the window; no release into the market was observed, so the row is booked zero and monitored.

## Buy pressure: where new QNT goes

The buy ledger is equally empty. Buy #1, programmatic buyback, is **zero** — Quant Network does not buy QNT on the open market; its revenue is a fiat Overledger licence fee, not a token-recycling programme. Buy #2, protocol fee burn, is **zero**, and this is the load-bearing structural fact about QNT's tokenomics. The Overledger licence model is **use-and-lock**, not use-and-burn: enterprises pay annual licence fees, any portion settled in QNT is locked in the Quant treasury for the licence term, and on expiry those tokens return to the treasury. No QNT is destroyed, so there is no deflationary burn flow, despite QNT often being marketed as a scarce, deflationary asset.

Buy #3, Foundation buy, is **zero**; no treasury open-market accumulation was observed in the window, and Quant sources the QNT it needs for operations from its own reserve rather than buying float on exchanges. Buy #4, new long-term lock, is **zero**; the licence locks are internal treasury locks on tokens Quant already holds off-market, not fresh market-removing locks that pull circulating QNT off the tradable float. Nothing on the buy side shrinks the supply, which is why a token often described as deflationary reads as an honest flat on the framework.

## Foundation and overhang

The one item worth watching is the treasury overhang. The gap between the **45.47M** QNT seen on-chain and the **14.54M** recognized as circulating — roughly **30.9M QNT**, more than twice the entire circulating float — is held in Quant's treasury and locked-reserve wallets, with **9.55M** sitting inside the token contract itself. It is non-circulating, it has not moved into the market on any schedule, and the recognized supply is correctly capped at **14.61M**. This overhang is tracked and re-read on-chain each refresh. If its balance falls between refreshes — that is, if Quant begins moving treasury QNT into the market — the outflow enters Sell #3 as real sell pressure at the next refresh. Today there is nothing of the sort: the reserve is static.

## How QNT compares to other fixed-supply utility tokens

The mechanism comparison that matters is what a token does with usage. Fee-burn chains like Ethereum and exchange tokens like BNB actively destroy supply as the network is used, so heavy usage makes them net-deflationary; quarterly-buyback exchange tokens recycle revenue into open-market purchases and send the result to a burn address, so their supply visibly shrinks. QNT does none of that. It is closest in shape to a fixed-cap governance token with fully-completed vesting and no buyback and no burn — the kind of asset that reads near zero for the same structural reason, that nothing is happening and nothing is designed to happen on the supply side.

QNT's differentiator is the enterprise licence model: Overledger generates revenue in fiat without consuming supply, so the token is meant to capture value through rising demand — more enterprises licensing Overledger, more QNT locked in treasury — rather than through supply contraction. That is a demand-side story, and the inflation framework only measures the supply dimension. On that dimension QNT is flat, and structurally so. The large treasury reserve is the single thing that separates it from a token that is fully circulating; it is the reason QNT is an observed zero rather than a guaranteed-forever one.

## What to watch in the next 90 days

For QNT the watch lines are unusually quiet. First, there are no scheduled supply events between now and mid-October 2026 — no unlock cliffs, no emission changes, no burns — so the base case is that the reading stays at 0.00% net. Second, the **~30.9M treasury reserve**: any visible deployment of it into the market would immediately register as Sell #3 pressure. Third, the licence model itself — a governance change from use-and-lock to a genuine burn would flip QNT from flat to deflationary. Fourth, recent headlines such as the Fusion Rollup going live on **Jun 2 2026** and the renewed enterprise-and-bank focus around **Jul 7 2026** are demand and adoption news, not supply events, and do not touch the ledger. Fifth, whether Quant publishes a treasury transparency report, which would let the framework promote Sell #3 from a watched, zero-value overhang to a quantified row.

## Summary

QNT is a fixed-supply, fully-vested, no-flow asset. No new tokens have been issued since 2018, the on-chain total supply is frozen at 45,467,000 with no working mint, the vesting from the 2018 sale is long complete, and the Overledger licence model locks tokens in treasury rather than burning them, so there is no buyback and no burn. The framework reads 0.00% net for the trailing 90 days and the supply monitor agrees to within about 0.03 points. The one structural feature is a large, static, non-circulating treasury overhang of roughly 30.9M QNT — more than the entire float, and the key risk to watch, but not a current flow. From a supply-pressure perspective, QNT is one of the quietest assets in coverage.

*MrNasdog Pressure Framework analysis of Quant (QNT), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 28 2026.*

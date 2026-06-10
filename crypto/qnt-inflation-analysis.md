---
title: "Quant (QNT) Inflation Analysis: Fixed Cap, Completed Vesting, Use-and-Redistribute Licensing"
description: "A MrNasdog Pressure Framework read of Quant (QNT): 14.6M effective cap locked 2018, all vesting completed Apr 2020, licensing model redistributes not burns. Framework reads 0.00% — every ledger row reads zero."
canonical_url: "https://mrnasdog.com/research/qnt/inflation"
tags: ["crypto", "quant", "interoperability", "enterprise"]
published: true
---

> Originally published at **[mrnasdog.com/research/qnt/inflation](https://mrnasdog.com/research/qnt/inflation)** by MrNasdog.

Quant's supply is essentially at its 14.6M cap, vesting completed in April 2020, and the licensing model redistributes rather than burns. Framework reading: **0.00% net** — every row in the eight-row ledger reads zero.

## The verdict, in one paragraph

For the 90-day window ending June 10 2026, the framework reads **QNT at 0.00% net inflation** — a structurally flat ledger. The aggregator monitor reads **−0.007%**, well inside any reasonable noise floor. There is nothing happening on the supply side. QNT's 14.6M effective cap was locked in 2018 when the ICO finalisation called `finishMinting()` on the ERC-20, and the protocol has had no mint capability since. All scheduled vesting completed by April 2020. The licensing model that powers Overledger does not consume supply.

## Sell pressure: every row is zero

Sell #1 — protocol inflation — is zero because the QNT contract has no callable mint function. The on-chain `totalSupply()` reads 45.47M, but this is an accounting artifact from the ICO-era mint pattern that all aggregators correctly normalise to the 14.6M effective cap (the post-burn cap set when the crowdsale finalised on September 14 2018). The framework follows the same convention — using the 14.6M cap as the supply base — and applies the anti-fabrication rule against back-deriving any flow from the 45.47M raw read.

Sell #2 — vesting unlocks — is zero forever. The original ICO allocation included a 1.35M founder allocation and a 651K advisor allocation, both with one-year lockups from April 30 2019. Both completed on April 30 2020. There are no remaining cliffs, no continuing linear streams, no relock decisions, no future vesting events to model.

Sell #3 — Foundation discretion — is zero with an opacity caveat. Quant (the UK corporate entity) accrues QNT from its enterprise licensing revenue, which gets redistributed in part to gateway operators and in part to the Quant corporate treasury. The treasury wallet set is not publicly enumerated, so the framework treats this as a watching opacity rather than a quantified row — the same structural shape as OKB's corporate treasury opacity. Sell #4 — bankruptcy estate — is zero; there is no estate.

## Buy pressure: every row is zero

The buy ledger is equally empty. Buy #1 — programmatic buyback — is zero; Quant Network has not announced any programmatic buyback funded by licensing revenue or corporate treasury reserves. Buy #2 — protocol fee burn — is zero. This is the load-bearing structural fact about QNT's tokenomics: the licensing model is **"use-and-redistribute"**, not "use-and-burn." Enterprises that license Overledger pay in QNT; the collected QNT does not get burned. Instead it gets distributed proportionally back to gateway operators (the infrastructure providers running Overledger nodes) plus the Quant corporate treasury slice. Supply does not decrease.

Buy #3 — Foundation buy — is zero; Quant is a UK corporate entity, not a foundation running a token accumulation programme. Buy #4 — new long-term lock — is zero; there is no staking contract, no veQNT, no protocol-enforced lockup mechanism. Lock-ups exist at the enterprise client level (multi-year licensing contracts), but those consume already-circulating QNT rather than locking fresh supply.

## Foundation and overhang

There is no Foundation overhang in the conventional sense. Quant Limited is a UK private company that issued the QNT token; the corporate treasury is governance-internal at the company. The 19.6% original team allocation (4.7M QNT) is fully vested and has been held or sold at the company's discretion since 2020. The opacity here is structural — there's no on-chain registry of the team's remaining holdings — but the framework reading treats this as a tag-B watching item with value zero, because the company has not made meaningful market-impacting sells visible in the trailing window.

## How QNT compares to other fixed-supply governance tokens

Among fixed-supply governance tokens with completed vesting, QNT is one of the cleanest "no flow" cases. Comparable shapes: Maker (now Sky) before the rebrand had a similar profile of complete-vesting plus active buyback; Aave has small ongoing safety module incentives but no major flow; Yearn (YFI) is the closest analogue — fixed cap, completed vesting, no buyback, no burn. YFI's and QNT's framework readings both sit near zero for the same structural reason: there's nothing happening, and nothing is supposed to be happening.

QNT's differentiator is the enterprise licensing model — it generates revenue without consuming supply, which means the token captures value via increased demand (more enterprises licensing Overledger) rather than via supply contraction. That is a different value-accrual model than fee-burn tokens (UNI, BNB, ETH) or revenue-buyback tokens (SKY, AAVE's historical safety-incentive model). Whether that model is sustainable long-term is a separate question; the framework only measures the supply-pressure dimension.

## What to watch in the next 90 days

For QNT the watch lines are unusually quiet. There are no scheduled supply events. The framework reading should remain at 0.00% net unless something genuinely new happens — a buyback announcement, a governance proposal to change the licensing model, a corporate treasury deployment large enough to be visible in the aggregator data. None of these are currently signalled. The only structural variable is whether Quant Limited publishes a transparency report on the corporate treasury, which would let the framework promote Sell #3 from "watching opacity, value zero" to a quantified row.

## Summary

QNT is a fixed-cap, fully-vested, no-flow asset. The 14.6M effective cap was locked in 2018; the last vesting completed in 2020; the licensing model redistributes rather than burns; there is no buyback. The framework reads 0.00% net for the trailing 90 days; the aggregator agrees within noise. There is no Foundation overhang to surprise the market and no scheduled event in the next 90 days. QNT's value accrual depends entirely on Overledger licensing demand, which sits outside the inflation framework. From a supply-pressure perspective, QNT is one of the quietest assets in coverage.

---

*MrNasdog Pressure Framework analysis of Quant (QNT), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 10, 2026.*

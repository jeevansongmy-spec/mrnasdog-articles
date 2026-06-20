---
title: "LINK Inflation Analysis · June 2026 · Capped token, but reserve supply still grows"
description: "A MrNasdog Pressure Framework read of Chainlink (LINK): no protocol mint, a ~19M/quarter non-circulating reserve release vs a ~1.5M Chainlink Reserve lock. Framework +2.3% net; monitor +5.55%."
canonical_url: "https://mrnasdog.com/research/link/inflation"
tags: ["crypto", "link", "chainlink", "oracles"]
published: true
---

> Originally published at **[mrnasdog.com/research/link/inflation](https://mrnasdog.com/research/link/inflation)** by MrNasdog.

Chainlink has a hard **1 billion LINK** cap and mints no new tokens, yet supply still grows: a non-circulating reserve releases about **19M LINK** into circulation each quarter, while the Chainlink Reserve locks roughly **1.5M** back. The Pressure Framework reads about **+2.3% net**. Our supply monitor reads **+5.55%** — the gap is reserve LINK that reaches the market beyond the single dated quarterly transfer.

## The verdict, in one paragraph

For the 90-day window ending June 20 2026, the MrNasdog Pressure Framework reads **LINK at +2.3% net** on the forward view, driven entirely by a quarterly release of LINK from a large non-circulating reserve. Our supply monitor reads the realized last-90-day change at **+5.55%**, versus the framework's **+2.34%** dated-release read for the same window — a gap of about **3.2 percentage points** that ships a **⚠ monitor-gap chip**. The gap is structural, not a missed unlock: beyond the single dated quarterly transfer the framework books, Chainlink also feeds reserve LINK to node-operator pay, staking rewards, ecosystem programs and grants across the quarter, so realized float grows faster than the one visible event. LINK is best read as **capped but still structurally diluting** while the reserve unwinds.

## Sell pressure: where new LINK comes from

Sell #1 — protocol inflation — is **zero**, and that is the headline fact about Chainlink: LINK is capped at 1 billion tokens, the network mints nothing, and there is no block reward or staking emission. Every LINK that will ever exist already exists; the only question is how fast it moves from reserves into circulation.

Sell #3 — Foundation and unscheduled unlocks — is therefore the whole story, at about **19M LINK** over the next 90 days. Chainlink Labs releases LINK from a large non-circulating reserve roughly once a quarter, on a Jan / Apr / Jul / Oct rhythm, in batches of about 14M to 19M. The April 2026 release was around 19M — about 14.4M to an exchange and 4.6M to a staking multisig — and the next quarterly release is due in July, inside this window. These tokens fund node operators, ecosystem development and grants; they are discretionary, but the recurring quarterly history makes the next firing a confident projection. Sell #2 — vesting unlocks — is zero, because Chainlink never ran a dated contractual vesting calendar; the original allocations sit in discretionary reserves, not a fixed lockup with cliffs. Sell #4 — long-term locked or bankruptcy — is zero.

## Buy pressure: where new LINK goes

Buy #1 — programmatic buyback — is the only active offset, at about **1.5M LINK** over 90 days, and it takes the form of the Chainlink Reserve. Through Payment Abstraction, on-chain and off-chain revenue is automatically converted into LINK and deposited into a reserve contract that holds, never sells, under a multi-day timelock with no withdrawals expected for years. Reserve holdings grew from about 1.4M LINK at the start of the year to roughly 3.9M by early June, so the Reserve locked away on the order of 1.5M LINK inside this window. Buy #2 — protocol fee burn — is zero: LINK has no burn mechanism, since network fees are paid to node operators rather than destroyed. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero beyond the Reserve already counted above.

## Foundation and overhang

The defining feature of LINK is its overhang: roughly **252M LINK** still sits outside circulation in non-circulating reserve allocations controlled by Chainlink Labs, with no published cliff calendar. That is the pool the quarterly releases draw from, and it is the single biggest supply variable for the token. On the buy side, the Chainlink Reserve is the opposite force — a tracked, on-chain accumulation wallet that locks revenue-funded LINK away, holding about 3.9M as of early June 2026. The framework books no discretionary outflow beyond the dated quarterly release and re-checks the reserve wallets on a roughly bi-weekly walk; if a reserve balance falls faster than the quarterly schedule, the extra outflow enters Sell #3 at the next refresh.

## How LINK compares to other capped-supply utility tokens

LINK belongs to the class of **hard-capped utility tokens with a large discretionary reserve** — closer to a fixed-supply token than to an uncapped, continuously-minting proof-of-stake chain. Unlike a halving-model coin, LINK has no emission curve and no miners; unlike a fully-distributed token, a meaningful share of supply still sits in reserves waiting to be released. That makes LINK's dilution a release problem, not a mint problem: the cap is real, but circulating supply keeps rising until the reserve is exhausted, which on the current ~7%-of-supply-per-year pace runs into 2027.

The contrast worth drawing is with exchange tokens that burn supply to go net-deflationary. LINK does the reverse — it has no burn at all, and its only supply sink is the Chainlink Reserve, which accumulates rather than destroys. The Reserve genuinely removes float, but at roughly a tenth of the quarterly release it slows dilution rather than reversing it. For an inflation lens, LINK reads as a capped token that is still structurally diluting on the active float.

## What to watch in the next 90 days

Watch the July 2026 quarterly release — the single dated event that decides most of the window's sell pressure, with the size (14M to 19M) and the exchange-versus-staking split being the numbers that matter. Watch the Chainlink Reserve's monthly accumulation, since it is the only force pulling LINK back off the market. Watch for any change to the quarterly rhythm or a one-off non-circulating transfer outside the schedule, which would enter Sell #3 immediately. And expect the framework to keep reading below our supply monitor for as long as reserve LINK reaches circulation through node-operator pay and ecosystem flows rather than a single dated transfer — that gap is structural, not a new unlock.

## Summary

LINK is a hard-capped utility token that mints nothing, yet its circulating supply keeps growing as a large non-circulating reserve is released into the market. Chainlink moves about 19M LINK out of reserves each quarter to fund node operators and the ecosystem, while the Chainlink Reserve locks roughly 1.5M back, leaving the framework at about +2.3% net. Our supply monitor reads +5.55% realized, with the gap explained by reserve LINK reaching circulation beyond the one dated quarterly transfer. The key risk is the ~252M reserve overhang, which keeps LINK structurally diluting until the reserve is drained toward 2027 — even though the 1 billion cap is fixed.

*MrNasdog Pressure Framework analysis of Chainlink (LINK), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 20, 2026.*

---
title: "LINK Inflation Analysis · June 2026 · Capped token, but reserve supply keeps growing"
description: "A MrNasdog Pressure Framework read of Chainlink (LINK): no protocol mint, two non-circulating reserve releases (~39M) vs a ~2M Chainlink Reserve lock. Framework +4.9% net; monitor +5.62%."
canonical_url: "https://mrnasdog.com/research/link/inflation"
tags: ["crypto", "link", "chainlink", "oracles"]
published: true
---

> Originally published at **[mrnasdog.com/research/link/inflation](https://mrnasdog.com/research/link/inflation)** by MrNasdog.

Chainlink has a hard **1 billion LINK** cap and mints no new tokens, yet circulating supply still grows: a non-circulating reserve releases LINK into the market each quarter, and the last 90 days caught two releases — about **17.9M in April** and about **21M on Jun 20 2026**, roughly **39M** together — while the Chainlink Reserve locked about **2M** back. The Pressure Framework reads about **+4.9% net** over that window. Our supply monitor reads **+5.62%**; the small remaining gap is reserve LINK that reaches the market beyond the two dated transfers.

## The verdict, in one paragraph

For the 90-day window ending June 26 2026, the MrNasdog Pressure Framework reads **LINK at +4.9% net** on the realized last-90-day view and **+2.3% net** on the forward view, driven entirely by the release of LINK from a large non-circulating reserve. Our supply monitor reads the realized last-90-day change at **+5.62%**, versus the framework's **+4.95%** dated-release read for the same window — a gap of about **0.7 percentage points** that ships a **⚠ monitor-gap chip**. The gap is structural, not a missed unlock: beyond the two dated quarterly transfers the framework books, Chainlink also feeds reserve LINK to node-operator pay, staking rewards, ecosystem programs and grants across the quarter, and the Chainlink Reserve's ~2M accumulation is still counted as circulating by the monitor. LINK is best read as **capped but still structurally diluting** while the reserve unwinds.

## Sell pressure: where new LINK comes from

Sell #1 — protocol inflation — is **zero**, and that is the headline fact about Chainlink: LINK is capped at 1 billion tokens, the network mints nothing, and there is no block reward or staking emission. Every LINK that will ever exist already exists; the only question is how fast it moves from reserves into circulation.

Sell #3 — Foundation and unscheduled unlocks — is therefore the whole story, at about **39M LINK** over the last 90 days. Chainlink Labs releases LINK from a large non-circulating reserve roughly once a quarter, in batches of about 10M to 21M, to fund node operators, staking rewards, ecosystem development and grants. This window caught two firings: the April 2026 release of about 17.9M (around 14.9M to an exchange and 4.1M to a staking multisig) and a second, larger release on Jun 20 2026 of about 21M (about 18.4M to an exchange and 2.6M to a staking multisig). The next quarterly release is due in July, projected near 19M, inside the forward window. These releases are discretionary, but the recurring quarterly history makes the next firing a confident projection. Sell #2 — vesting unlocks — is zero, because Chainlink's original contractual vesting schedule physically finished in 2024; there is no dated cliff calendar left. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate or court distribution applies to LINK.

## Buy pressure: where new LINK goes

Buy #1 — programmatic buyback — is the only active offset, at about **2M LINK** over 90 days, and it takes the form of the Chainlink Reserve. Through Payment Abstraction, on-chain and off-chain revenue is automatically converted into LINK and deposited into a reserve contract that holds, never sells, under a multi-day timelock with no withdrawals expected for years. Reserve holdings grew from about 1.5M LINK in early January to roughly 4.5M by June, so the Reserve locked away on the order of 2M LINK inside this window — supply taken off the open market and held. Buy #2 — protocol fee burn — is zero: LINK has no burn mechanism, since network fees are paid to node operators rather than destroyed. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero, with no discretionary open-market buying or new escrow beyond the Reserve already counted above.

## Foundation and overhang

The defining feature of LINK is its overhang: roughly **252M LINK** still sits outside circulation in non-circulating reserve allocations controlled by Chainlink Labs, with no published cliff calendar. That is the pool the quarterly releases draw from, and it is the single biggest supply variable for the token. On the buy side, the Chainlink Reserve is the opposite force — a tracked, on-chain accumulation wallet that locks revenue-funded LINK away, holding about 4.5M as of June 2026. The framework books the dated quarterly releases as Sell #3 and re-checks the reserve wallets and on-chain transfers on a roughly bi-weekly walk; if a reserve balance falls faster than the quarterly schedule, the extra outflow enters Sell #3 at the next refresh.

## How LINK compares to other capped-supply utility tokens

LINK belongs to the class of **hard-capped utility tokens with a large discretionary reserve** — closer to a fixed-supply token than to an uncapped, continuously-minting proof-of-stake chain. Unlike a halving-model coin, LINK has no emission curve and no miners; unlike a fully-distributed token, a meaningful share of supply still sits in reserves waiting to be released. That makes LINK's dilution a release problem, not a mint problem: the cap is real, but circulating supply keeps rising until the reserve is exhausted, which on the current ~7%-of-supply-per-year release pace runs toward the start of the next decade.

The contrast worth drawing is with exchange tokens that burn supply to go net-deflationary. LINK does the reverse — it has no burn at all, and its only supply sink is the Chainlink Reserve, which accumulates rather than destroys. The Reserve genuinely removes float, but at roughly a twentieth of this window's release it slows dilution rather than reversing it. For an inflation lens, LINK reads as a capped token that is still structurally diluting on the active float.

## What to watch in the next 90 days

Watch the July 2026 quarterly release — the single dated event that decides most of the forward window's sell pressure, with the size (about 19M, in the 10M to 21M range) and the exchange-versus-staking split being the numbers that matter. Watch whether the cadence stays quarterly after two releases landed only about two months apart this spring. Watch the Chainlink Reserve's monthly accumulation, since it is the only force pulling LINK back off the market. Watch for any one-off non-circulating transfer outside the schedule, which would enter Sell #3 immediately. And expect the framework to keep reading just below our supply monitor for as long as reserve LINK reaches circulation through node-operator pay and ecosystem flows rather than the dated transfers alone.

## Summary

LINK is a hard-capped utility token that mints nothing, yet its circulating supply keeps growing as a large non-circulating reserve is released into the market. Two releases landed in the last 90 days — about 17.9M in April and about 21M on Jun 20 2026, roughly 39M together — while the Chainlink Reserve locked about 2M back, leaving the framework at about +4.9% net for the window and +2.3% projected forward. Our supply monitor reads +5.62% realized, with the small remaining gap explained by reserve LINK reaching circulation beyond the two dated transfers. The key risk is the ~252M reserve overhang, which keeps LINK structurally diluting until the reserve is drained — even though the 1 billion cap is fixed.

*MrNasdog Pressure Framework analysis of Chainlink (LINK), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 26, 2026.*

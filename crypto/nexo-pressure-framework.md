---
title:         "NEXO Inflation Analysis · July 2026 · Mixed flows, supply roughly steady"
description:   "Net flat: a fixed 1B supply with no mint or vesting, and a revenue buyback held in a locked reserve, not burned. Framework 0.00% / 90D; monitor +0.0077%."
canonical_url: "https://mrnasdog.com/research/nexo/inflation"
tags:          ["crypto", "nexo", "cefi", "exchange-token"]
published:     true
---

*Originally published at [mrnasdog.com/research/nexo/inflation](https://mrnasdog.com/research/nexo/inflation)*

**TL;DR.** Nexo has one of the cleanest supply profiles in the Pressure Framework. NEXO is a fixed **1,000,000,000** token supply, minted in full at the 2018 sale, with no mint function and no vesting calendar left to run down. Over the last 90 days the framework reads **0.00% net** — nothing added and nothing removed — against a supply monitor at **+0.0077%**, a gap of well under **0.01 percentage points**. The one thing that could have made NEXO deflationary, its revenue-funded buyback, does not register on the ledger, because repurchased tokens are **held** in a reserve that is still counted as circulating rather than burned.

## The verdict, in one paragraph

For the 90-day window ending **Jul 28 2026**, the Pressure Framework reads **NEXO at 0.00% net**. Sell pressure is **zero**, buy pressure is **zero**, against a circulating base of **1,000,000,000 NEXO**. Our supply monitor reads **+0.0077%**, which is a few thousandths of one percent — the difference between the two is **0.0077 percentage points**, far inside the framework's half-point tolerance, so no monitor-gap note ships. That tiny monitor figure is not real issuance; it is rounding noise in a market-cap-over-price supply series that hovers around a constant on-chain 1B. Looking forward, the next 90 days project the same **0.00%**, because nothing in the mechanism changes. NEXO is best characterised as **a fixed, fully-issued supply with a buyback that warehouses rather than destroys**.

## Sell pressure: where new NEXO comes from

No new NEXO comes from anywhere, and all four sell rows are **zero**. Sell #1, protocol inflation, is zero because NEXO is not a blockchain — there is no consensus layer, no staking and no block reward paid in the token. The Ethereum contract's supply counter reads exactly **1,000,000,000 NEXO** and has held that value for years; there is no mint function that can grow it. Sell #2, vesting unlocks, is zero because the entire supply was delivered at the **2018** token sale, and every team, advisor and treasury vesting schedule finished long ago. The clearest proof of this is that circulating supply already equals both total supply and max supply, and fully diluted valuation equals market cap — there is simply no locked tranche waiting to be released.

Sell #3, foundation and unscheduled unlocks, is **zero**, and it is worth being precise about why. The one identified company-controlled holding is the Investor Protection Reserve, which holds about **114.8M NEXO**, roughly **11.5%** of the supply. That reserve has not moved a single token since **Mar 1 2023**, so there is no observed release and nothing to project forward. There is a second, subtler reason it stays at zero: the reserve is already counted inside the circulating figure this ledger divides by, so even a release from it would not change the supply the framework measures. Sell #4, long-term locked or bankruptcy, is zero because Nexo is a solvent operating company with no estate, no trustee and no court-ordered NEXO distribution.

## Buy pressure: where new NEXO goes

All four buy rows are **zero**, and the most important one is Buy #1. Nexo runs a genuine revenue-funded **buyback** — it has committed well over **$150M** to open-market repurchases across several programmes since 2020 — but the mechanism is buyback-and-**hold**, not buyback-and-burn. Repurchased NEXO is sent to the on-chain Investor Protection Reserve, locked for at least twelve months, and then recycled into interest payouts and strategic use rather than destroyed. Because those tokens land in a wallet the circulating figure still counts, the buyback removes **no counted supply** — it is float-neutral against the framework's denominator. And separately, on-chain the reserve has taken in nothing since **Mar 2023**, so no repurchase falls inside this window to book in the first place. Either way the row is zero.

The remaining buy rows are zero for structural reasons. Buy #2, protocol fee burn, is zero because NEXO is not a gas token on any chain it lives on, so no transaction fee is ever paid or burned in it; there is no burn address that removes NEXO from supply. Buy #3, foundation buy, is zero because no open-market NEXO purchase separate from the buyback programme was disclosed inside the window. Buy #4, new long-term lock, is zero because no new escrow, staking cap or multi-year lock was announced — and even the reserve's twelve-month lock is temporary, recycling tokens back rather than removing them for good.

## Foundation and overhang

One team-controlled pool is tracked for NEXO: the Investor Protection Reserve at **114,800,950 NEXO**, read on-chain at every rebuild. It carries the single most important caveat on this page. The reserve is where the buyback's repurchased tokens accumulate, so on paper it looks like a supply sink — but it has been completely **static since Mar 2023**, and its balance is already classified as circulating, so it is neither shrinking the float today nor able to shrink the framework's denominator if it releases. Beyond the reserve, Nexo holds undisclosed operational company reserves, but there is no separately identified, published on-chain address for them, and all **1B** tokens are counted as circulating regardless. If the reserve's balance falls between refreshes, that outflow enters Sell #3 at the next refresh — though because the tokens are already counted as circulating, it would change the market's free float, not this ledger's net.

## How NEXO compares to other exchange and CeFi tokens

The natural comparison class for NEXO is other exchange and CeFi platform tokens that run buyback programmes funded from company revenue. The defining difference is what happens to the repurchased tokens. The large exchange tokens in that class run buyback-and-**burn** — every token they buy is permanently destroyed, so their circulating supply genuinely shrinks quarter after quarter and their inflation reading is negative by structure. NEXO runs buyback-and-**hold**: the tokens are parked in a reserve and later reused, so the same revenue produces no lasting reduction in counted supply. Two platforms can spend comparable sums on their token and land in completely different places on this framework — one deflationary, one flat.

Against ordinary proof-of-stake Layer 1s the contrast is sharper still. An uncapped staking chain typically issues somewhere between **3%** and **12%** a year of genuinely new supply. NEXO issues **nothing** — its **1B** cap is not a promise in a document but a fixed on-chain supply that has never grown. Judged purely on issuance, NEXO is as quiet as an asset can be: there is no emission curve, no unlock cliff and no dilution schedule to model. The whole supply story is already written.

The closest structural analogue is not a chain at all but a fully-distributed fixed-cap token with no remaining vesting. Those assets share NEXO's core property: the supply is settled, so the only genuine variable is demand. What makes NEXO distinct inside that group is the presence of a live buyback that could, if the company ever chose to burn rather than hold, flip the asset from flat to deflationary overnight — the machinery already exists; only the destination would need to change.

## What to watch in the next 90 days

The single most informative thing to watch is the Investor Protection Reserve balance. If its **114.8M NEXO** starts rising again, the buyback has resumed accumulating; if Nexo ever announces that repurchased tokens will be **burned** rather than held, that is the change that would move this reading from flat to deflationary. Watch the U.S. relaunch, which went live via Bakkt on **Feb 16 2026** — higher platform revenue is what funds buybacks, so a strong revenue quarter is the most likely trigger for a new repurchase programme. Watch the governance-voting module introduced in **Q1 2026** for any proposal touching the token's supply or the reserve's use. And watch for any burn announcement at all: with a fixed cap and a funded buyback already in place, a burn is the only mechanism that could change NEXO's supply trajectory, and it would show up on-chain immediately.

## Summary

The MrNasdog Pressure Framework reads Nexo at **0.00%** net supply change over the last 90 days and **0.00%** projected for the next 90, against a monitor reading of **+0.0077%** that is rounding noise rather than real issuance. The structural mechanism is a fixed, fully-issued **1,000,000,000** supply: no mint, no vesting, no burn, minted in full at the **2018** sale and unchanged since. The key nuance is the buyback — it is real and well-funded, but it holds repurchased NEXO in a reserve that is still counted as circulating, so it removes no counted supply and the framework reads flat rather than deflationary. The one genuine ceiling is the cap itself: supply cannot exceed **1B**, so the only way NEXO's supply story ever changes is if the company decides to burn what it buys instead of holding it.

---

*MrNasdog Pressure Framework analysis of NEXO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 28 2026.*

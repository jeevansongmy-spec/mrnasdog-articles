---
title: "RAY Inflation Analysis · September 2026 · Mixed flows, supply roughly steady"
description: "Supply roughly steady: RAY cannot be minted, 0.40M RAY left a reserve, and the 12%-of-fees buyback holds 4.47M RAY inside the float. +0.15% net over 90 days."
canonical_url: "https://mrnasdog.com/research/ray/inflation"
tags: ["crypto", "ray", "raydium", "defi"]
published: true
---

> Originally published at **[mrnasdog.com/research/ray/inflation](https://mrnasdog.com/research/ray/inflation)** by MrNasdog.

# RAY Inflation Analysis · September 2026 · Mixed flows, supply roughly steady

RAY, the token of the Raydium exchange on Solana, can never be minted again, yet RAY supply on the market still edged up this quarter. A release wallet the project keeps outside the counted float refilled a Raydium reward pool with **0.40M RAY**, and that is new float. The Raydium buyback spent **12%** of trading fees on **4.47M RAY**, but it parks the coins in a wallet that is already counted as circulating, so it takes **zero** off the market and burns nothing. The MrNasdog Pressure Framework therefore reads RAY at **+0.15% net** over the last 90 days against a supply-monitor reading of **+0.37%** — a gap of **0.22 percentage points**, inside tolerance. RAY supply is capped at **555M**, and **282.66M** of it still sits in project vaults that did not move.

## The verdict, in one paragraph

For the 90-day window ending **Sep 25 2026**, the Pressure Framework reads **RAY at +0.15% net**: the sell side added **0.40M RAY** to a circulating supply of **269.74M**, and the buy side removed nothing. The independent supply monitor reads the same 90 days at **+0.37%**. The gap is **0.22 percentage points**, inside the framework's half-point tolerance, so RAY ships with **no data-conflict flag**. The forward column also reads **+0.15%**, because the reward refills run at a steady pace and nothing dated is due. The label for RAY is **roughly steady, with a buyback that holds inside the float**: a capped token whose fee-funded purchases change who owns RAY, not how much RAY is on the market.

## Sell pressure: where new RAY comes from

Sell #1, protocol inflation, is **0.40M RAY**, and it does not come from minting. The RAY mint authority is switched off, so the Raydium protocol cannot create a single new RAY. What it can do is move RAY that already exists from a place the circulating count leaves out to a place it includes. A Raydium release wallet, fed long ago from the mining reserve, sits outside the counted float; it refilled the vault behind a Raydium reward pool with **200,000 RAY** on **Aug 10 2026** and another **200,000 RAY** on **Sep 10 2026**. Each refill showed up as a step of the same size in the circulating count, which is how the boundary was confirmed rather than assumed. The pool pays out about **3,600 RAY** a day and its vault holds less than a week of that, so the forward column keeps the same two refills.

Sell #2, vesting unlocks, is **zero**: Raydium team and seed vesting finished on **Feb 21 2024**, and no unlock tracker carries a remaining RAY schedule. Sell #3, foundation and unscheduled unlocks, is also **zero**, and it was measured account by account. Five Raydium project vaults under one key hold **282.66M RAY** — partnership and ecosystem **138.59M**, mining reserve **123.32M**, advisors **11.10M**, team **7.30M**, community and seed **2.35M** — and not one of them sent a single transaction in the 90 days. Sell #4, long-term locked or bankruptcy supply, is **zero**: no estate distributes RAY and no long-dated RAY lock is unwinding.

## Buy pressure: where new RAY goes

Buy #1, the programmatic buyback, is the part of the RAY story most readers get wrong. Raydium routes **12%** of every trading fee on its pools into open-market RAY purchases, and the buyback bought **4.47M RAY** this window, about **$4.68M** at each day's price — measured coin by coin at the holding wallet and checked against a fee aggregator's count of the same stream. It books **zero** anyway, because the wallet it fills is already inside the circulating count. The proof is in the count itself: while the wallet grew by **4.47M RAY**, circulating RAY rose rather than fell. A purchase that moves RAY from traders into a wallet the market already counts is a transfer inside the float, not a reduction of it. The RAY is held, not burned.

Buy #2, the protocol fee burn, is **zero**: Raydium runs no fee burn. Stray user burns remove dust, and the whole RAY supply sits only **2,550 RAY** below its **555M** cap after five years, which bounds any burn in this window to a rounding error. Buy #3, foundation buying, is **zero** — the **4%** Raydium treasury share of fees is kept in dollars rather than RAY. Buy #4, new long-term locks, is **zero**: no new lockup contract appeared, and RAY deposited in the reward pool stays in the circulating count.

## Foundation and overhang

RAY carries a large, readable overhang in two parts. The first is the **282.66M RAY** in the five Raydium project vaults, all outside the circulating count and all without a release schedule; they are re-read on chain every refresh. The second is the Raydium buyback wallet at **87.25M RAY**, about **32%** of circulating supply, held under a single key rather than a contract. It is inside the float already, but it is one decision away from moving: it has sent RAY out before — **552,905 RAY** across 2021 to 2023, the last on **Feb 24 2023** — and nothing since. The Raydium protocol multisig holds another **8.87M RAY**, flat for more than two years. The project's stated position is that what happens to the bought-back RAY is a governance question. If any vault's balance falls between refreshes, the outflow enters Sell #3 at the next refresh; if the buyback wallet's balance falls, the destination decides the row.

## How RAY compares to other DEX tokens with buybacks

Exchange tokens that turn fees into buybacks split into two designs, and RAY sits in the one that moves supply least. In buy-and-burn, the purchased coins go to an address no one controls, total supply falls, and the float shrinks by the full amount. In buy-and-hold, the purchased coins go to a wallet the project controls; whether the float shrinks depends entirely on whether that wallet is counted as circulating. RAY's is, so the Raydium buyback supports the order book without reducing the RAY on it — flow support without float reduction, the mirror image of a reserve burn.

Against uncapped proof-of-stake tokens, RAY looks calm by design. An uncapped chain mints new coins every epoch and hopes a fee burn offsets them; RAY mints nothing, and its only new float comes from pre-minted reserves released by the project in visible, dated transfers. Against capped proof-of-work coins, the difference is who holds the key: a mined coin's remaining supply is released by protocol arithmetic, while RAY's **282.66M** unreleased coins are released only when the project chooses. The fee base underneath is real — Raydium collected about **$39.4M** in trading fees over the last 30 days — and it is what funds the buyback, but the buyback's effect on supply depends on the wallet, not on the size of the fees.

## What to watch in the next 90 days

First, the reward-pool refills: the last two landed on **Aug 10 2026** and **Sep 10 2026**, and a larger or more frequent refill would lift the sell side above its booked **0.40M RAY**. Second, any governance decision on the bought-back stack: burning the **87.25M RAY** would remove it from supply and open a large buy row, while sending it to market would change nothing in the count but everything in the order book. Third, the five project vaults at **282.66M RAY**: they have not moved in the window, and any outflow into the market would enter Sell #3 at the next refresh. Fourth, the circulating count itself: one small step of about **25,000 RAY** in late August has no identified source yet, and the next rebuild re-checks it.

## Summary

The MrNasdog Pressure Framework reads RAY at **+0.15% net** over the trailing 90 days and **+0.15%** over the next 90, with supply roughly steady. The structural mechanism is a capped token with the mint switched off, whose only new float is reserve RAY released into a reward pool, and whose **12%**-of-fees buyback holds the coins in a wallet the market already counts. The key risk is concentration: **282.66M RAY** in project vaults and **87.25M RAY** in the buyback wallet can each move on one decision. The ceiling is the **555M RAY** cap, which can never rise.

*MrNasdog Pressure Framework analysis of RAY, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 25 2026.*

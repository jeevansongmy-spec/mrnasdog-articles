---
title: "IMX Inflation Analysis · June 2026 · Capped, fully unlocked, structurally flat"
description: "A MrNasdog Pressure Framework read of Immutable (IMX): fixed 2B supply, fully unlocked, no mint and no burn. Framework reads 0.00% net; monitor −1.28% is a reclassification, not an outflow."
canonical_url: "https://mrnasdog.com/research/imx/inflation"
tags: ["crypto", "imx", "immutable", "gaming"]
published: true
---

> Originally published at **[mrnasdog.com/research/imx/inflation](https://mrnasdog.com/research/imx/inflation)** by MrNasdog.

Immutable's **IMX** is capped at **2 billion** coins, finished vesting in 2025, and has no mint function and no burn. Over the next 90 days the protocol adds **0 IMX** and removes **0 IMX**, so the Pressure Framework reads **0.00% net** — supply is structurally flat. Our supply monitor reads **−1.28%**, but with no burn that can destroy coins, that move is a bookkeeping reclassification, not a real outflow.

## The verdict, in one paragraph

For the 90-day window ending June 16 2026, the MrNasdog Pressure Framework reads **IMX at 0.00% net**. Nothing mints and nothing burns: IMX is a fixed-supply **2 billion** ERC-20, fully unlocked since 2025, so both the sell and the buy ledgers come out to zero. Our supply monitor reads the realized last-90-day change at **−1.28%**, a gap of about **1.3 percentage points** that ships a **⚠ monitor-gap chip**. Because Immutable has no burn and no buyback that destroys supply, IMX simply cannot have lost 1.28% of its coins — the monitor is reading a reclassification of reserve and staking tokens between the circulating and non-circulating columns. IMX is best characterised as **a capped, fully-unlocked token with no live inflation mechanism**.

## Sell pressure: where new IMX comes from

Sell #1 — protocol inflation — is **zero**. IMX has a hard cap of **2 billion** coins and no mint function, so the network creates no new supply at all; this is not a low rate, it is a structural impossibility. Sell #2 — vesting unlocks — is also **zero**: the original team, investor, public-sale and ecosystem allocations all finished their cliff-based vesting in 2025, so there is no remaining unlock calendar and no cliff inside this window.

Sell #3 — Foundation and unscheduled unlocks — is **zero** as a flow. About **1.16B IMX** sits in the Ecosystem Development and Project Development reserves; those coins are already unlocked but held off the open market with no published release schedule and no dated discretionary release in the window, so the framework books no outflow and monitors them as overhang. Sell #4 — long-term locked or bankruptcy — is **zero**, because no bankruptcy estate or court-ordered distribution applies to IMX.

## Buy pressure: where new IMX goes

Buy #1 — programmatic buyback — is carried at **zero**, and the reason is the most interesting part of IMX's structure. Staking rewards are funded by **20%** of protocol fees, which Immutable swaps into IMX on the open market and then redistributes to stakers every 14 days. That is a market buy, but the coins are handed straight back to holders rather than burned or locked, so on a supply-pressure basis they are recycled within the float, not removed. Buy #2 — protocol fee burn — is **zero**: IMX has no burn function, so trading fees fund rewards instead of destroying coins. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both **zero**, with no discretionary open-market buying and no new escrow; the June 19 2026 staking migration actually unstakes coins back to wallets rather than locking them.

## Foundation and overhang

The one thing to keep an eye on with IMX is the reserve. Of the 2 billion cap, only about **842M** is classified as circulating; the remaining **~1.16B** sits in the Ecosystem Development and Project Development buckets, fully unlocked but held back from the market. There is no published release schedule for these reserves, so the framework treats them as monitored overhang rather than scheduled supply, and re-checks the reserve balances on a roughly bi-weekly walk. If one of those reserve balances falls between refreshes, the outflow enters Sell #3 at the next refresh. Until then, the reserve is only capacity, not an actual flow, and it scores zero.

## How IMX compares to other capped fixed-supply tokens

IMX belongs to the class of **hard-capped, fully-vested tokens with no live emission** — structurally closer to a fixed-supply utility token than to a continuous-emission L1 or a halving-model coin. Unlike a proof-of-stake chain that mints block rewards forever, IMX cannot create a single new coin; unlike an exchange token that burns a slice of revenue every quarter, it has no burn either. That leaves it in a quiet middle: no dilution, but no structural scarcity engine pulling supply down.

The useful contrast is with a fee-burning chain that runs net-deflationary, or an inflationary staking chain that runs net-positive. IMX sits exactly between them at zero, because its staking mechanism recycles coins instead of either minting or burning them. For an inflation lens specifically, that makes IMX one of the cleaner reads in the catalog: the only variable that can move it is a discretionary decision to release reserve coins, which would show up immediately as Sell #3.

## What to watch in the next 90 days

Watch the staking migration on **June 19 2026**, when staking moves from Immutable X to Immutable zkEVM and existing staked coins are unstaked back to wallets — a one-off that adds to float rather than removing it, though most of it is expected to re-stake. Watch the Ecosystem Development and Project Development reserve balances; a sustained drawdown there is the only event that would push Sell #3 above zero. Watch for any governance proposal to introduce a burn or a buy-and-lock, which IMX currently does not have. And expect the framework to keep reading flat while the monitor drifts, for as long as the reclassification of reserve and staking coins continues.

## Summary

IMX is a capped, fully-unlocked gaming token with no inflation mechanism: the 2 billion supply is fixed, vesting ended in 2025, and there is no mint and no burn. Over the next 90 days the framework books zero new supply and zero removal, leaving net inflation at 0.00% — structurally flat. Our supply monitor reads −1.28%, but since no burn exists to destroy coins, that is a reclassification of reserve and staking tokens, not an outflow, and the framework keeps the structural read. The one real risk is the ~1.16B reserve overhang, which scores zero only until the project actually moves it to market.

*MrNasdog Pressure Framework analysis of Immutable (IMX), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 16, 2026.*

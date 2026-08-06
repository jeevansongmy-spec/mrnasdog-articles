---
title: "VET Inflation Analysis · August 2026 · Supply flat, projected to stay flat"
description: "VeChain's inflation lives in VTHO, not VET: supply fixed at 86.71B cap with ~85.99B circulating, no mint, no vesting, no VET burn, no buyback. Framework reads 0.00% (monitor +0.076%)."
canonical_url: "https://mrnasdog.com/research/vet/inflation"
tags: ["crypto", "vet", "vechain", "fixed-supply"]
published: true
---

> Originally published at **[mrnasdog.com/research/vet/inflation](https://mrnasdog.com/research/vet/inflation)** by MrNasdog.

# VET Inflation Analysis · August 2026 · Supply flat, projected to stay flat

VeChain is one of the few large chains whose inflation question has a one-word answer: none. **VET** is capped at **86.71B** coins and every unit was minted at genesis in 2017, so no new VET is ever created. The network does issue and burn tokens constantly — but those are **VTHO**, a separate gas token on its own ledger, and the **100%** gas-fee burn destroys VTHO, never VET. Over the 90 days to **Aug 6 2026** the Pressure Framework reads **0** VET of sell pressure and **0** VET of buy pressure, a net of **0.00%**. Our supply monitor reads the realised change at **+0.076%** — a gap of just **0.08 percentage points**, so no monitor-gap chip ships. VET is a purely fixed supply.

## The verdict, in one paragraph

For the 90-day window ending **Aug 6 2026**, the Pressure Framework reads **VET at 0.00% net** for both the trailing and forward windows — nothing adds VET and nothing removes it. Sell pressure is **0**, buy pressure is **0**, against a circulating base of roughly **85.99B VET** below a hard **86.71B** cap. Our supply monitor reads the realised 90-day change at **+0.076%**, a gap of just **0.08 percentage points** — well inside the framework's half-point tolerance, so no monitor-gap chip appears on the VET overview. That tiny reading is rounding noise around a fixed cap, not real issuance: the monitor's market-cap-over-price series simply wobbles day to day on a constant supply. VET is best characterised as **a hard-capped, fixed-supply token whose inflation lives entirely in a second gas token**.

## Sell pressure: where new VET comes from

The honest answer is that no new VET comes from anywhere. Sell #1, protocol inflation, is **0**. The full **86.71B VET** was created at genesis in 2017, the cap can never rise, and VeChainThor mints no VET as a block or staking reward. This is the point most often misread about VeChain: the December 2025 Hayabusa upgrade introduced staking, but stakers earn **VTHO**, the network's gas token, not fresh VET. Hayabusa cut VTHO generation by roughly half and tied it to actively staked VET, yet it left the VET supply itself untouched. VET has no mint function, and that single fact governs the whole page.

Sell #2, vesting unlocks, is **0**. The 2017 genesis allocations for the public sale, team, foundation and ecosystem were distributed and their lock-ups expired years ago, leaving no live vesting cliff still releasing VET into the market. Sell #3, foundation and unscheduled unlocks, is **0** this window: the VeChain Foundation holds VET, but disclosed no sale or distribution, and the roughly **728M VET** that sits outside the circulating float as an undistributed reserve showed no observed outflow. Sell #4, long-term locked or bankruptcy, is **0**: there is no estate, no trustee and no court-ordered VET tranche anywhere in VeChain's history.

## Buy pressure: where new VET goes

The buy side is just as empty, and for the same two-token reason. Buy #2, protocol fee burn, is **0** in VET terms even though VeChain burns **100%** of the gas paid on every transaction — because the gas is denominated in VTHO, not VET. Every transaction on VeChainThor is paid for in VTHO, and 100% of the VTHO consumed is burned; but VET is never spent on fees and never destroyed, so that burn removes no VET at all. The deflationary pressure real users create lands entirely on VTHO, which is why the VET float does not shrink even as network usage rises. Counting that burn as a VET buy would be a category error.

The other three buy rows are **0** as well. Buy #1, programmatic buyback, is zero because VeChain runs none — the protocol never repurchases VET off the market, so there is no buy-and-hold or buy-and-burn program pulling VET out of supply. Buy #3, foundation buy, is zero: no VeChain entity disclosed an open-market VET purchase this window, and no accumulation wallet has been identified. Buy #4, new long-term lock, is zero, and this one needs the closest look: VET staked on the StarGate platform grew sharply after Hayabusa, but that stake is voluntary, reversible, and still counted as circulating supply, so it earns VTHO rather than removing VET from the float. With nothing minting and nothing burning, VET's net reading is simply zero.

## Foundation and overhang

Two team-controlled overhangs sit behind VET, and both are watched rather than active. The first is about **728M VET** — roughly **0.84%** of the 86.71B cap — that sits outside the circulating float as an undistributed reserve, with no published release schedule and no observed outflow over the trailing year. The second is the VeChain Foundation treasury, which holds VET inside a mixed asset base; the Foundation does not itemise a single liquid VET balance on-chain, so it is tracked through its disclosures rather than a live figure. Neither fired in the window. There is no separate DAO treasury and no bankruptcy residual. The large StarGate staking balance is explicitly not an overhang — it is user-owned VET in free-exit custody that stays circulating-classified. If the reserve or the Foundation's VET balance falls between refreshes through a distribution or sale, that outflow enters Sell #3 at the next refresh.

## How VET compares to other fixed-cap and dual-token chains

VET belongs to a small class of chains that split value and gas into two tokens, and to the broader class of hard-capped tokens whose supply is set once and never expands. In these dual-token systems the coin you buy is deliberately not the coin the network spends, and the inflation you would expect on the main asset is exported onto the gas token. That is why VET reads flat while VTHO is where all the monetary action lives: dynamic issuance tied to staking, a roughly fifty-percent issuance cut under Hayabusa, and a full fee burn. Judging VET by VTHO's mechanics is the most common mistake made about this coin, and it is the mistake this page exists to prevent.

Against ordinary single-token proof-of-stake layer ones, VET looks unusually clean. An uncapped continuous-emission chain mints new coins to pay stakers, so its supply grows every block; VeChain pays stakers in VTHO instead, so VET issuance is zero by design. Against capped-and-halving chains like Bitcoin, VET is stricter in one sense — there is no ongoing subsidy at all, because distribution finished at genesis, so its issuance is not merely low but exactly zero — yet weaker in another, since VET has no VET-denominated burn of its own to make the fixed supply actively shrink. Against burn-driven chains or an exchange token with quarterly buybacks, VET looks different again: those assets can tip net-deflationary when their burn or buyback outruns issuance, whereas VET has no VET burn to lean on. The honest label is fixed-and-flat: nothing is being added, but nothing is being removed either, which is exactly why the framework's inflation reading sits at the flat middle of the band rather than at the deflationary end.

The practical takeaway is that VET carries none of the dilution risk that drives most inflation analysis. There is no unlock calendar to fear and no emission curve to model. The only supply questions worth watching are discretionary ones — whether the reserve or the Foundation ever moves VET into the market — rather than anything the protocol does on its own.

## What to watch in the next 90 days

Watch the VeChain Foundation treasury for any single large VET distribution or open-market sale, which would register as a discrete Sell #3 release — the only realistic way VET supply pressure changes. Watch the roughly **728M VET** undistributed reserve for any first movement out of its wallet. Watch StarGate staking totals, not because staking removes VET, but because a very large migration into stake could change how much VET is practically available to trade even while it still counts as circulating. And watch VeChain's roadmap upgrades for any future proposal that would issue VET directly — none exists today, and Hayabusa deliberately kept rewards in VTHO, but a fixed cap is only as durable as the governance that guards it. There is no dated unlock, burn or cliff to watch, because VET has none.

## Summary

VeChain's VET is a hard-capped, fixed-supply token: all **86.71B VET** were minted at genesis, no new VET is ever created, and no VET is ever burned because the network runs its rewards and fees through the separate VTHO gas token. The Pressure Framework reads net new supply of **0.00%** over 90 days, and our monitor confirms it at **+0.076%**, a **0.08-point** gap inside tolerance. The one fact that resolves almost every question about this coin is the dual-token split — VeChain's heavy, 100% fee burn destroys VTHO and never touches VET. The key risk for holders is not dilution but discretion — a future Foundation or reserve release — while the structural strength is that VET's float simply cannot inflate on its own.

*MrNasdog Pressure Framework analysis of VeChain (VET), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated August 6, 2026.*

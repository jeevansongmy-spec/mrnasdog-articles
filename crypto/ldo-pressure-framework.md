---
title:         "LDO Inflation Analysis · August 2026 · Supply shrinking on a DAO buyback"
description:   "LDO mints nothing and has no vesting left, while a DAO buyback pulled ~12.7M LDO into the treasury in 90 days. Framework −1.52% net; monitor −1.50%."
canonical_url: "https://mrnasdog.com/research/ldo/inflation"
tags:          ["crypto", "ldo", "lido", "defi"]
published:     true
---

*Originally published at [mrnasdog.com/research/ldo/inflation](https://mrnasdog.com/research/ldo/inflation)*

Lido's LDO is a fixed **1,000,000,000** token that finished vesting in 2024, so it has no mint, no unlock calendar and no burn — all four sell rows read **zero**. The only force moving supply is a holder-approved buyback, and reading the DAO treasury wallet directly shows it drew **~12.7M LDO** off the open market over 90 days and parked it in the treasury. The framework reads **−1.52% net**, and our supply monitor agrees at **−1.50%**, a gap of just **0.01 percentage points** — well within tolerance, no flag. LDO is best characterised as a capped, fully-vested token whose float is shrinking by buyback-and-hold rather than by any burn.

## The verdict, in one paragraph

For the 90-day window from **May 11 2026** to **Aug 9 2026**, the Pressure Framework reads **LDO at −1.52% net**: sell pressure of **zero** against buy pressure of about **12.7M LDO**, on a circulating base of **836.3M LDO**. Our supply monitor reads the same period at **−1.50%**, a gap of only **0.01 percentage points**, comfortably inside tolerance, so the page carries no monitor-gap flag. The two numbers agree because they measure the same event from opposite ends: the buyback pulled roughly **12.7M LDO** off the open market and into the non-circulating DAO treasury, which is exactly the drop the monitor's circulating series recorded. LDO is best labelled a **fixed-supply governance token that shrinks by buyback, not by burn** — deflationary today only because the DAO is actively buying.

## Sell pressure: where new LDO comes from

Nowhere — and that is the point. Sell #1, protocol inflation, is **zero** and cannot turn on: LDO is an Ethereum ERC-20 with a fixed **1,000,000,000** supply, all minted once at launch in December 2020, and the token has no mint function and no staking or emission rewards. Unlike a proof-of-stake base asset, LDO does not pay validators in new units; it only votes and holds treasury, so there is no issuance curve of any kind. Sell #2, vesting unlocks, is also **zero** and permanent. Every original allocation — the DAO treasury, investors, initial developers, founders and validators — vested on a one-year cliff plus one-year linear schedule that ran from December 2020 and physically finished in **2024**. LDO is fully unlocked, and no cliff falls inside this window or the next 90 days.

Sell #3, Foundation and unscheduled unlocks, is **zero**. The Lido DAO treasury holds about **114.76M LDO** in its main on-chain wallet, part of roughly **163.7M** non-circulating LDO across Lido contracts, with no published release schedule — a real, governance-controlled overhang. But in this window the treasury was a net **buyer**, not a seller: no treasury LDO was sent to the market, so the row books zero and stays monitored. Sell #4, long-term locked or bankruptcy, is **zero**: Lido is a going concern, and no estate, trustee schedule or court-ordered distribution touches LDO. All four sell rows read zero, which is why the entire supply story lives on the buy side.

## Buy pressure: where LDO goes

Buy #1, the programmatic buyback, is about **12.7M LDO** — the whole story of this page. After LDO traded at a steep discount to the protocol's fundamentals, holders approved a treasury-funded buyback of up to **10,000 stETH** (about **$20M**), executed on the open market in roughly 1,000-stETH batches routed through exchanges and market makers. Read straight off the DAO treasury's on-chain LDO log, three batches landed inside the window: **4.5M LDO** on **Jun 1 2026**, **1.72M LDO** on **Jun 11 2026** and **6.47M LDO** on **Jul 8 2026**, delivered by the buyback executor contract into the DAO treasury. Crucially the LDO is **held, not burned**: it removes float today but leaves a DAO-controlled balance that a future vote could redeploy.

Buy #2, protocol fee burn, is **zero**: LDO has no EIP-1559-style burn and no burn function, so the only way supply is removed is the discretionary buyback above. Buy #3, Foundation buy, is **zero**, because the DAO buyback is the only entity purchase and is already counted in Buy #1. Buy #4, new long-term lock, is **zero**: the bought-back LDO sits unlocked in the treasury rather than in a time-lock, and no new escrow contract was created in the window. So the buy side is a single, on-chain, revenue-independent buyback — and because every sell row is zero, that one buyback sets the entire reading.

## Foundation and overhang

LDO carries one clean overhang: the **163.7M LDO** that is non-circulating — the gap between the **1B** cap and the **836.3M** circulating — which sits in the DAO treasury and related Lido contracts, about **114.76M** of it in the main Aragon Agent wallet. There is no vesting calendar behind it; it moves only when Lido governance votes to move it, which makes it a discretionary lever rather than a scheduled unlock. The buyback is now **adding** to this balance, not draining it, so the overhang is growing even as circulating supply falls — the same tokens simply move from market to treasury. This is the important asymmetry: a burn would make the shrink permanent, but a hold means the DAO could, by a later vote, return bought-back LDO to the market. If any treasury LDO leaves through a discretionary sale between refreshes, the outflow enters Sell #3 at the next refresh.

## How LDO compares to other fixed-cap governance tokens

LDO's natural peers are fixed-cap, no-mint governance tokens whose supply was issued once and whose only levers are vesting and treasury. On the vesting axis LDO is already at the calm end: its unlocks finished in 2024, so unlike the many 2021-era tokens still dripping monthly, LDO has no scheduled dilution left at all. What separates LDO from most of that cohort is the buyback. A continuous-emission Layer 1 mints new coins every block and needs a fee burn just to stand still; LDO issues nothing, so a buyback of any size pushes it straight into deflation. That is why a token with no burn mechanism still reads **−1.52%**.

Against the exchange tokens that popularised buybacks, LDO shares the mechanic but not the finality. A mature exchange token typically buys back with revenue and then **burns**, permanently retiring supply; Lido's program buys with treasury stETH and **holds** the LDO, so the float reduction is real but reversible. It is also revenue-independent in its current one-off form — funded from the treasury balance rather than a fixed cut of fees — which makes the pace a governance decision rather than an automatic function of protocol income. A gated automated successor was approved on **Aug 8 2026** in treasury-only mode, but it only fires when ETH trades above **$3,000** and annual revenue clears **$40M**; with ETH near **$1,918** it is dormant, so today the reading rests on the discretionary buyback, not the automated one.

## What to watch in the next 90 days

First, the buyback pace: the framework projects Buy #1 forward at its observed rate of about **12.7M LDO** per quarter, which keeps the forward read near **−1.5%** — but the program is discretionary and gated per batch, so a pause would flatten it quickly. Second, whether the automated buyback begins firing, which requires ETH to reclaim **$3,000**; below that it contributes nothing. Third, any governance move to **burn** the accumulated LDO rather than hold it, which would convert a reversible float reduction into permanent deflation. Fourth, any treasury deployment of the roughly **163.7M** non-circulating LDO, which would turn Sell #3 positive and could swamp the buyback. Fifth, the circulating supply itself, which should keep drifting down from **836.3M** as long as the buyback runs.

## Summary

The Pressure Framework reads Lido DAO at **−1.52% net** supply over the last 90 days, in near-exact agreement with our monitor's **−1.50%**. LDO is a fixed **1B** token with no mint and no burn, and its vesting ended in 2024, so every sell row is zero — the only force on the supply is a holder-approved buyback that pulled about **12.7M LDO** off the market and into the DAO treasury. The key nuance is that the tokens are **held, not burned**, so the shrink is real but reversible, and the pace depends on a discretionary program plus a dormant automated one. As long as the buyback runs, LDO is that rare thing: a token shrinking without ever destroying a coin.

---

*MrNasdog Pressure Framework analysis of Lido DAO (LDO), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated August 9 2026.*

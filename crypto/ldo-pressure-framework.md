---
title:         "LDO Inflation Analysis · August 2026 · Supply shrinking, projected to keep shrinking"
description:   "LDO mints nothing and has no vesting left, while a DAO buyback pulled ~12.75M LDO into the treasury in 90 days. Framework −1.52% net; monitor −1.42%."
canonical_url: "https://mrnasdog.com/research/ldo/inflation"
tags:          ["crypto", "ldo", "lido", "defi"]
published:     true
---

*Originally published at [mrnasdog.com/research/ldo/inflation](https://mrnasdog.com/research/ldo/inflation)*

Lido's LDO is a fixed **1,000,000,000** token that finished vesting in 2024, so it has no mint, no unlock calendar and no burn — all four sell rows read **zero**. The only force moving supply is a holder-approved buyback, and reading the DAO treasury wallet directly shows it drew **~12.75M LDO** off the open market over 90 days and parked it in the treasury. The framework reads **−1.52% net**, and our supply monitor agrees at **−1.42%**, a gap of just **0.11 percentage points** — well within tolerance, no flag. LDO is best characterised as a capped, fully-vested token whose float is shrinking by buyback-and-hold rather than by any burn.

## The verdict, in one paragraph

For the 90-day window ending Aug 2 2026, the Pressure Framework reads **LDO at −1.52% net**. Sell pressure is **zero LDO** across all four rows, and buy pressure is **~12.75M LDO**, against a circulating base of **836.3M LDO**. Our supply monitor reads the realised change at **−1.42%**, a gap of only **0.11 percentage points**, which is inside tolerance and ships no monitor-gap chip. The two measures agree because the buyback's destination — the DAO treasury — is counted as non-circulating, so buying LDO off the float and holding it there genuinely reduces circulating supply, and both the framework and the monitor see the same shrink. LDO is best characterised as **a hard-capped token deflating by treasury accumulation, not by burn**.

## Sell pressure: where new LDO comes from

There is no new LDO. Sell #1, protocol inflation, is **zero**: Lido minted its entire **1,000,000,000** LDO supply once at the 2020 genesis, and the token contract has no live emission — no block reward, no staking curve, no inflation schedule. Sell #2, vesting unlocks, is also **zero**. Every team, investor and treasury vesting stream finished releasing in **2024**, so there is no unlock calendar and no cliff inside this window; the supply is fully vested. Sell #3, Foundation and unscheduled unlocks, is **zero** as a flow — the DAO treasury is large, but it took coins IN this quarter rather than selling any out, which is covered below. Sell #4, long-term locked or bankruptcy, is **zero**: there is no Lido estate, no trustee and no court-ordered distribution. With no mint and no burn, the sell side of LDO is structurally empty, and the only way the number changes is a governance decision to release treasury LDO.

## Buy pressure: where new LDO goes

Buy #1, the programmatic buyback, is the entire story. In March 2026, with LDO trading roughly 95% below its 2021 high and at a deep discount to ETH, the DAO approved spending up to **10,000 stETH** from its treasury to buy LDO in the open market, executed in **1,000-stETH** batches through Easy Track with each batch separately disclosed. Reading the destination directly rather than trusting the announcements, the DAO treasury wallet's LDO balance rose from **102.0M** to **114.8M** over the window — an inflow of **~12.75M LDO** bought off the float. That figure is corroborated independently: our supply monitor shows circulating LDO falling by about **12.0M** across the same period, so the treasury inflow and the float outflow agree to within about 6%.

The other three buy rows are **zero**. Buy #2, protocol fee burn, is zero because Lido burns no LDO at all — staking revenue is collected in stETH and other assets, and the buyback keeps the LDO it buys rather than destroying it. Buy #3, Foundation buy, is zero because the DAO's only open-market buying is the buyback already counted in Buy #1; crediting it again would double the effect. Buy #4, new long-term lock, is zero: the automated LP-mode variant of the buyback, which would pair bought LDO with wstETH into a liquidity pool, had its contracts deployed and verified on-chain in late **Jul 2026**, but it only fires when ETH is above **$3,000** and Lido's annualised revenue clears **$40M**, and no execution is visible on-chain yet.

## Foundation and overhang

One team-controlled pool dominates: the **Lido DAO treasury**, an on-chain Aragon Agent that holds about **114.8M LDO**, roughly 11.5% of total supply. This is where bought-back LDO accumulates, which is why the balance grew ~12.75M this quarter — the treasury is absorbing float, not releasing it. Crucially, the buyback is **held, not burned**: the LDO sits in a DAO-controlled wallet and remains re-deployable by a future governance vote, so the deflation is reversible in a way a burn is not. There is no published schedule for releasing any of the treasury balance, so it is a tracked overhang rather than sell pressure. The wallet is re-read every rebuild, and if its LDO balance falls between refreshes, that outflow enters Sell #3 at the next refresh.

## How LDO compares to other DeFi governance tokens

The mechanism comparison that matters is cap-and-vested versus emitting. Many DeFi and liquid-staking governance tokens still mint — liquidity-mining programmes, staking curves and uncapped treasuries mean their sell side scales with usage. LDO does neither: the **1B cap** is fixed and all vesting ended in 2024, so its structural sell pressure is zero. That puts it in a small group of tokens whose only supply variable is discretionary buying, not scheduled selling.

The second comparison is burn versus buy-and-hold. Exchange tokens that run buybacks usually send the purchased supply to a burn address, so the reduction is irreversible and every supply feed books it immediately. Lido buys and **keeps**: the LDO it purchases lands in the DAO treasury, which outside supply feeds already treat as non-circulating, so the float shrinks and the monitor and framework agree. The trade-off is reversibility — because the tokens are held rather than destroyed, a future vote could send the whole **114.8M** treasury stack back toward the market, whereas a burned token is gone for good. LDO's deflation is therefore real but conditional on the DAO continuing to buy and continuing to hold.

## What to watch in the next 90 days

First, whether the one-off buyback keeps firing: only about a fifth of the **10,000-stETH** budget has been spent, and each remaining batch needs a fresh disclosure, so a pause would flatten this reading quickly. Second, whether the automated LP-mode buyback goes live — its contracts were deployed around **Jul 28 2026**, and if ETH holds above **$3,000** while revenue clears the threshold, it would add a second, non-discretionary stream of buying. Third, any governance proposal to release or redeploy treasury LDO, which is the only event that could turn Sell #3 non-zero. Fourth, the pace of the treasury balance itself, since a stall in its growth is the earliest sign the buyback has slowed. Fifth, Lido protocol revenue, which is the gate the automated program depends on.

## Summary

Lido's LDO is a fixed 1B token that finished vesting in 2024, so it has no mint, no unlock calendar and no burn, and all four sell rows are zero. The only force on supply is a holder-approved buyback, which drew about 12.75M LDO off the open market over 90 days and parked it in the DAO treasury, held rather than burned. That leaves the framework at −1.52% net, matched by our supply monitor at −1.42% because the treasury destination is counted as non-circulating and the float genuinely shrinks. The key structural fact is that this deflation is reversible — a governance vote could return the 114.8M-LDO treasury stack to the market — and the key risk is simply that the buyback stops, at which point a token with zero sell pressure would sit flat.

---

*MrNasdog Pressure Framework analysis of Lido DAO (LDO), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated August 2 2026.*

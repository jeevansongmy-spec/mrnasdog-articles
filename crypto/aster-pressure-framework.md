---
title:         "ASTER Inflation Analysis · September 2026 · Mixed last 90D · projected to grow"
description:   "ASTER: mixed last 90 days, projected to grow. Supply rose 0.25% and is set to rise 2.50% as a 63.4M airdrop pays out; buyback and burn remove no tradable coins."
canonical_url: "https://mrnasdog.com/research/aster/inflation"
tags:                    ["crypto", "aster", "bnbchain", "defi"]
published:     true
---

Originally published at [ASTER Inflation Analysis · September 2026 · Mixed last 90D · projected to grow](https://mrnasdog.com/research/aster/inflation).

# ASTER Inflation Analysis · September 2026 · Mixed last 90D · projected to grow

ASTER supply in the market grew **+0.25%** over the last 90 days and is projected to grow **+2.50%** over the next 90, as a **63.4M ASTER** Stage 6 airdrop tranche pays out on **Oct 28 2026**. Aster runs a real fee buyback and a real burn, but the buyback hands every coin back to stakers and the burn draws only on locked team coins, so the Pressure Framework books **6.75M ASTER** of sell pressure against **0** of buy pressure. The ceiling is a fixed **8,000M ASTER** that no contract function can raise; the monitor reads **+1.30%**.

## The verdict, in one paragraph

Against a circulating base of **2,710.5M ASTER**, the framework records **6.75M ASTER** of sell pressure and **0** of buy pressure between Jun 24 and Sep 22 2026, a net of **+0.25%**, and projects **+2.50%** for the next 90 days. The inflation monitor reads **+1.30%** for the same window, a gap of **1.05 percentage points**, which is over the framework's 0.5-point tolerance and ships with a monitor-gap warning on the overview. The gap is fully explained. About **0.99 points** is the Aster reserve burn itself: the monitor's supply figure counts coins sitting in the dead address as circulating, so each burn of locked team ASTER shows up there as new supply. About **0.06 points** is the monitor's own supply estimate, and under **0.01 points** comes from its smaller starting base. The label for ASTER is **a real burn that cuts the ceiling, not the float**.

## Sell pressure: where new ASTER comes from

Nothing is minted. The ASTER contract on BNB Chain is a plain token with no mint function, and total supply read **8,000M ASTER** at both ends of the window. The value is stored in a field the contract can write, so the flat reading is a real measurement rather than a number fixed in code. Sell #1, protocol inflation, is **6.75M ASTER** because Aster pays stakers from coins minted at launch. Staking on Aster Chain earns **450K ASTER** a week, and the pre-minted ecosystem pool funds it in blocks of **2.25M ASTER** every five weeks. Three blocks left the pool in the window, on **Jul 13**, **Aug 17** and **Sep 21 2026**. Two more are due around **Oct 26** and **Nov 30 2026**, so the forward figure is **4.5M ASTER**.

Sell #2, vesting unlocks, is **0** for the last 90 days and **63.4M ASTER** for the next. That is the Stage 6 airdrop. Aster let Stage 6 users either claim half at once, with the other half burned, or wait six months for the full amount. Almost everyone waited: only **0.62M ASTER** went down the early path. The vested claim opens on **Oct 28 2026**, and the Aster airdrop reserve pays such a claim in one move. Stage 5 worked exactly that way: **0.91M ASTER** early on Mar 9 2026, then **95.1M ASTER** on Jun 9 2026, adding up to its published **96M ASTER** to the token. The 400M team allocation adds nothing. Its first release was due Sep 17 2026, and on Sep 1 2026 Aster pushed it to **Sep 17 2027**.

Sell #3, Foundation and unscheduled unlocks, is **0**: the treasury, the airdrop reserve and a further idle reserve wallet did not send a single ASTER out in the window. Sell #4, long-term locked or bankruptcy, is **0**, because ASTER has no estate, trustee or court-ordered distribution.

## Buy pressure: where new ASTER goes

Buy #1, programmatic buyback, is **0**, and this needs explaining because the Aster buyback is genuine. Since the Jun 17 2026 upgrade, 99% of platform fees buy ASTER on the open market every day, about **26.5M ASTER** over this window. Every one of those coins is then paid to veASTER stakers the same week. Staked ASTER sits in the Aster deposit bridge, and that bridge is counted as circulating. The buyback moves coins from sellers to stakers; it does not take them out of the market.

Buy #2, protocol fee burn, is also **0**, and the burn is genuine too. For every ASTER bought back, Aster burns the same amount every two weeks, team coins first, until total supply falls to **3,000M ASTER**. We read both places a burn can show. Total supply did not move, because Aster burns by sending coins to the dead address. The dead address did move, from **177.8M** to **204.3M ASTER**, through seven burns totalling **26.5M ASTER**. All seven came from the locked team wallet, which fell from **400M** to **373.5M ASTER**. Those coins were never in the market, so the burn lowers the ceiling and removes no tradable ASTER.

Buy #3, Foundation buy, is **0**: the treasury held exactly **560M ASTER** at both ends. Buy #4, new long-term lock, is **0**. Staking locks run up to four years, and since Aug 11 2026 each new perp listing must lock **1M ASTER** for four years, but both sit in the same bridge that is already counted as circulating.

## Foundation and overhang

The Aster overhang is large and fully mapped. The airdrop reserve holds **2,917.2M ASTER** and pays out only when a claim window opens; Stage 6 will take **63.4M** of it. The ecosystem pool holds **1,240.5M ASTER** and feeds staking. The Foundation treasury holds **560M ASTER**, untouched since launch and spendable only by governance. A further reserve wallet holds **198.3M ASTER** and has not moved since Nov 17 2025. The team wallet holds **373.5M ASTER** and shrinks with every burn. Together these five wallets are exactly the coins not counted as circulating.

The buyback wallet holds almost nothing, because it passes each purchase to stakers. Every wallet here is read on-chain at each rebuild. If any balance falls by more than its schedule explains, and the coins go anywhere but the dead address, the outflow enters Sell #3 at the next refresh.

## How ASTER compares to other perp-DEX and exchange tokens

Most exchange tokens that advertise a buyback do one of two things with the coins: destroy them, or park them in a wallet that sits outside the tradable float. Either way the bought coins leave the market, and the inflation reading can turn negative. ASTER does neither. It pays the coins to stakers, so its buyback works as a staking yield, not a supply cut.

The Aster burn looks like the burns other exchange tokens run, and it is not. A burn funded from coins that were already trading shrinks the float. A burn funded from a locked reserve shrinks only the fully diluted supply. Aster chose the second kind, team coins first. So ASTER's fully diluted count falls, from **8,000M** toward a stated **3,000M**, while the tradable count keeps rising with every staking block and airdrop stage.

On issuance, ASTER is stricter than any continuous-emission chain: the contract has no way to mint. Its supply growth comes from releases, like a young token working through airdrop and team schedules. Unlike a smooth day-by-day vest, it comes in steps.

## What to watch in the next 90 days

First, the Stage 6 vested claim on **Oct 28 2026**: a release of about **63.4M ASTER** from the airdrop reserve is almost the whole forward reading. Second, the staking blocks around **Oct 26** and **Nov 30 2026**, **2.25M ASTER** each. Third, the source of each bi-weekly burn: while it is the team wallet the buy side stays at zero, but a burn from coins already trading would count. Fourth, any new airdrop stage, since the reserve still holds **2,917.2M ASTER** and no calendar exists past Stage 6. Fifth, the **560M ASTER** treasury, the one pot with no schedule and a governance spender.

## Summary

The MrNasdog Pressure Framework reads ASTER at **+0.25%** over the trailing 90 days and **+2.50%** projected forward: mixed last 90 days, projected to grow. Nothing is minted, but pre-minted coins keep reaching the market through staking pay and airdrop stages, and the **63.4M ASTER** Stage 6 tranche on Oct 28 2026 drives the forward figure. The key risk is that the headline buyback and burn remove no tradable ASTER at all, because the buyback pays stakers and the burn uses locked team coins. The ceiling is a fixed **8,000M ASTER** with no mint function, and it is falling as the team reserve is burned.

MrNasdog Pressure Framework analysis of ASTER, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 23 2026.

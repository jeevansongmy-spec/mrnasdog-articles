---
title: "RAY Inflation Analysis · August 2026 · Supply shrinking, projected to keep shrinking"
description: "Supply shrinking: Raydium releases ~0.51M RAY/90d while a 12%-of-fees buyback holds ~2.6M off market. Framework −0.78% net vs a +0.14% monitor read, so a gap chip ships."
canonical_url: "https://mrnasdog.com/research/ray/inflation"
tags: ["crypto", "ray", "raydium", "defi"]
published: true
---

*Originally published at [mrnasdog.com/research/ray/inflation](https://mrnasdog.com/research/ray/inflation)*

Raydium releases about **0.51M RAY** over 90 days from a fixed mining reserve, while the buyback funded by **12%** of every pool's trading fee took roughly **2.6M RAY** off the open market and held it. RAY minting is permanently disabled, so the buyback outpaces the emission and the Pressure Framework reads **−0.78% net** on the active float. Our supply monitor reads **+0.14%** because it still counts the held buyback wallet as circulating — a **0.92-point** gap that is mechanical, not an error.

## The verdict, in one paragraph

For the 90-day window ending **Aug 9 2026**, the MrNasdog Pressure Framework reads **RAY at −0.78% net**: **0.51M RAY** of sell pressure against **2.6M RAY** of buy pressure on a circulating base of **269.31M RAY**. Our supply monitor reads the realised change over the same 90 days at **+0.14%**, a gap of **0.92 percentage points**. That exceeds the framework's half-point tolerance, so a **monitor-gap chip ships** on the RAY overview. The gap resolves cleanly: the Raydium buyback does not burn RAY, it accumulates it in a public wallet that the monitor's upstream classification still treats as circulating supply. The **2.6M RAY** absorbed is worth about **0.97 points** of the gap on its own, which the small difference between the framework's emission read and the monitor's realised float growth trims to the observed **0.92 points**. RAY is best read as **structurally deflationary on the active float**, with the held buyback stack sitting behind it as a governance-reversible overhang.

## Sell pressure: where new RAY comes from

Sell #1, protocol inflation, is the only live sell row and it is small: about **0.51M RAY** over 90 days. Raydium's RAY mint authority is disabled, so no new RAY can ever be created — on-chain total supply sits at **554.998M** against a **555M** hard cap and cannot rise. What reads as inflation is the fixed mining reserve paying already-issued RAY out as staking and farming rewards. Raydium's single-sided RAY staking farm emits at **0.065 RAY per second**, or roughly **2.06M RAY a year**, which lands at **0.51M RAY** over a quarter. Raydium's own documentation puts current emissions at approximately **1.9M RAY a year** — the two figures agree within eight percent, which is why this row ships as a measured value rather than an estimate.

Sell #2, vesting unlocks, is **zero** and permanently so. Raydium's team and seed allocations, together **25.9%** of total supply, were locked for twelve months after the token generation event and then released daily from month 13 to month 36; that schedule concluded on **Feb 21 2024**. RAY has been fully unlocked ever since, so no vesting cliff can reach the market in this window or any future one.

Sell #3, foundation and unscheduled unlocks, is **zero** because nothing moved. Every project-held allocation wallet was read directly on-chain for this build and every one was flat across the full 90 days: the mining reserve at **123.3M RAY**, partnership and ecosystem at **138.6M**, team at **7.3M**, advisors at **11.1M** and community and seed at **2.3M**. Two events in the window touched only already-circulating coins, not new supply: the **Jul 8 2026** wind-down of the legacy AcceleRaytor launch program returned user deposits and unclaimed tokens to their own addresses, and a **Jun 10 2026** exploit of five retired 2021 pools took 150,177 RAY plus SOL and USDC that Raydium is covering from treasury. Sell #4, long-term locked or bankruptcy, is **zero** for the simple reason that Raydium has no bankruptcy estate and no court-ordered distribution schedule.

## Buy pressure: where new RAY goes

Buy #1, the programmatic buyback, carries the whole buy side at roughly **2.6M RAY** over 90 days. Raydium routes **12%** of every pool's trading fee into automatic open-market RAY purchases — the same share on concentrated-liquidity pools, constant-product pools and legacy AMM v4 pools, applied to the trading fee rather than to the trade size. This build measured the row two independent ways. Raydium collected about **13.9M dollars** in trading fees over the window, so the **12%** buyback slice is close to **1.67M dollars**, which at a RAY price near **64 cents** buys about **2.6M RAY**. The on-chain buyback accumulation wallet confirms it: it held **83.8M RAY** on **Aug 9 2026** and has only grown, with no outflow. The buyback has not collapsed with the fee decline, because a lower RAY price buys more RAY per dollar of fees.

Buy #2, protocol fee burn, is **zero**, and this is the single most misread fact about RAY. Raydium does not burn its buyback. Bought-back RAY is transferred to a public accumulation wallet and held there; RAY total supply has not moved off **554.998M**, which proves nothing was destroyed. Several secondary articles describe Raydium as a "buy-and-burn" token — that is false, contradicted by both the official documentation and the on-chain state, where the wallet visibly holds the entire accumulated stack. Buy #3, foundation buy, is **zero** — Raydium does no discretionary open-market buying outside the automatic fee buyback. Buy #4, new long-term lock, is **zero** as well: RAY staking is user-initiated and withdrawable at any time, so it locks nothing structurally, and no new escrow or multi-year lock was announced in the window.

## Foundation and overhang

RAY's overhang is large and fully enumerable. Roughly **285.7M RAY** sits outside circulation, and this build accounted for almost all of it by address. The Raydium mining reserve holds **123.3M RAY** with no published release schedule beyond the staking emission tail. Partnership and ecosystem holds **138.6M**, advisors **11.1M**, team **7.3M** and community and seed **2.3M**. All five are read by chain RPC on every rebuild, and all five were unchanged across this window.

The sixth and most consequential overhang is the buyback wallet itself, now **83.8M RAY** — about **31%** of circulating RAY, bought with well over **$200M** of cumulative Raydium protocol fees. Because Raydium holds rather than burns, that stack is a real, reversible supply overhang: a future governance decision could redeploy it, sell it, or burn it, and only one of those three outcomes is good for holders. It is tracked on-chain daily. If the buyback wallet's balance falls between refreshes, that outflow enters Sell #3 at the next refresh. The same trigger applies to each of the five Raydium allocation wallets.

## How RAY compares to other fee-funded DEX tokens

The useful comparison for RAY is not other Solana assets but other tokens whose supply story is a fee-funded buyback. Exchange tokens that run quarterly buy-and-burn programmes convert revenue into permanent supply destruction: the coins leave the ledger, total supply falls, and an aggregator and a mechanism-level framework end up agreeing on the number. Raydium sits one step short of that. The revenue conversion is identical — arguably better, since it runs continuously at **12%** of every fee rather than quarterly at management discretion — but the destination is a wallet, not a burn address. The effect on the tradable float today is the same; the durability is not.

Against uncapped, emission-driven DeFi tokens, RAY looks structurally strong. Raydium has a **555M** hard cap, a disabled mint authority, a vesting schedule that ended in **Feb 2024**, and an emission tail of roughly **2.06M RAY a year** that is being outrun more than five to one by the buyback. Very few DeFi tokens can claim all four at once. The genuine risk is not dilution, it is revenue: Raydium protocol revenue ran near **$27M** over the trailing year but only about **$0.7M** in the last 30 days. Because the buyback is a fixed percentage of fees, a fee collapse is a buyback collapse — and the deflation this framework measures is a function of trading activity Raydium does not control.

## What to watch in the next 90 days

First, the Raydium buyback wallet balance — the cleanest single number on RAY, read directly on every rebuild; a flattening curve would show the fee decline reaching the buyback before any dashboard reports it. Second, the fee run rate: Raydium trading volume has slipped behind newer Solana venues, and the RAY buyback is only as large as the fees behind it. Third, any governance move on the held RAY stack: a decision to burn it would be the largest deflationary event in RAY's history, and a decision to redeploy it would be the largest supply event. Fourth, the aftermath of the **Jul 8 2026** AcceleRaytor wind-down and the **Jun 10 2026** exploit of five retired 2021 pools — both move already-circulating coins rather than new supply, but the treasury drawdown from the reimbursement is worth tracking. Fifth, the mining reserve token account, which has not changed balance since 2024; any release there would open a genuine new sell row.

## Summary

The MrNasdog Pressure Framework reads RAY at **−0.78% net** over 90 days: a **0.51M RAY** mining-reserve emission against a **2.6M RAY** fee-funded buyback, on **269.31M RAY** circulating. Raydium's supply mechanism is unusually clean — a **555M** hard cap, a permanently disabled mint, vesting closed since **Feb 2024**, and a buyback that outruns the emission more than five to one. The key risk is not dilution but revenue: the buyback is a fixed **12%** slice of trading fees that have fallen hard, and a weaker quarter mechanically shrinks the deflation. The second risk is that the buyback holds rather than burns, leaving **83.8M RAY** — about **31%** of the float — parked in a wallet that governance could one day reverse.

---

*MrNasdog Pressure Framework analysis of Raydium (RAY), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 9 2026.*

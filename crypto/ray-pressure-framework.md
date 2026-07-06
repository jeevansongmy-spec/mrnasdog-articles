---
title: "RAY Inflation Analysis · July 2026 · Buyback outpaces the last of the emission"
description: "Buyback outpaces emission: Raydium releases ~0.5M RAY/90d vs a ~2.9M buyback held off market. Framework reads −0.89% net; monitor +0.26% flat, so a gap chip ships."
canonical_url: "https://mrnasdog.com/research/ray/inflation"
tags: ["crypto", "ray", "raydium", "defi"]
published: true
---

> Originally published at **[mrnasdog.com/research/ray/inflation](https://mrnasdog.com/research/ray/inflation)** by MrNasdog.

Raydium releases only about **0.5M RAY** over 90 days from a fixed mining reserve, while a buyback funded by **12%** of all trading fees takes roughly **2.9M RAY** off the open market and holds it. RAY minting is permanently switched off, so the buyback clearly outpaces the emission and the Pressure Framework reads about **−0.89% net** on the float. Our supply monitor reads **+0.26%** — essentially flat — because it counts the held buyback wallet as circulating, leaving a **1.15-point** gap.

## The verdict, in one paragraph

For the 90-day window ending July 6 2026, the MrNasdog Pressure Framework reads **RAY at about −0.89% net**: the fee-funded buyback removes far more RAY from the open market than the mining reserve issues. Our supply monitor reads the realized last-90-day change at **+0.26%** — flat — versus the framework's **−0.89%** read, a gap of about **1.15 percentage points**. Because that exceeds the 0.5-point tolerance, a **monitor-gap chip ships**. The gap is structural, not an error: the buyback sends RAY to a public accumulation wallet that the monitor's upstream still counts as circulating. On-chain the buyback wallet holds **83.09M RAY** on July 6 2026 while RAY's total supply has not moved from **554.998M** — the coins were bought and held, not burned. RAY is best read as **structurally deflationary on the active float**, with the held buyback as a governance-reversible overhang.

## Sell pressure: where new RAY comes from

Sell #1 — protocol inflation — is small and shrinking, at about **0.5M RAY** over the next 90 days. RAY's mint authority is renounced, so no new RAY can ever be created; what looks like inflation is the fixed mining reserve paying out already-issued coins as farming and staking rewards. Raydium's own staking pool emits RAY at **0.065 RAY per second** — about **2.06M RAY a year**, or roughly 0.5M over a quarter. That is the only genuinely new float entering the market, and at this pace it is a fraction of one percent of circulating RAY per 90 days.

Sell #2 — vesting unlocks — is **zero**: every team, seed, advisor and ecosystem allocation finished vesting in 2024, so RAY is fully unlocked and no cliff hits the market. Sell #3 — Foundation and unscheduled unlocks — is also zero as a flow; about **285.7M RAY** sits outside circulation across the mining reserve, the Raydium treasury, and the buyback wallet, but none of it has a published release schedule. The one in-window event was a June 10 2026 exploit of legacy 2021 AMM V3 pools — about **$1.34M** in RAY, SOL and USDC, including roughly 150,000 RAY — that Raydium is reimbursing from treasury. That is already-held supply redeployed, not a new mint. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate or court distribution applies to RAY.

## Buy pressure: where new RAY goes

Buy #1 — programmatic buyback — is the dominant force, at about **2.9M RAY** over 90 days. Raydium routes **12%** of all trading fees into automatic RAY purchases on the open market across every pool type, regardless of fee tier. Over the trailing 90 days Raydium generated roughly **$16.6M** in trading fees, so 12% of that funds close to $2M of RAY buying at an average price near $0.69. The critical detail is the destination — bought-back RAY is sent to a public accumulation wallet and **held, not burned**. On-chain, that wallet holds about **83.09M RAY**, and RAY's total supply is unchanged at 554.998M, confirming the coins were removed from the float without being destroyed. Because they leave the open market, they count as buy-side pressure here.

Buy #2 — protocol fee burn — is **zero**, because there is no burn: the buyback accumulates RAY in a wallet rather than destroying it, so total supply never falls. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero, with no discretionary open-market buying outside the fee buyback and no new escrow or lockup announced in the window.

## Foundation and overhang

The team-controlled overhang for RAY is the roughly **285.7M RAY** that sits outside circulation. It breaks into three tracked buckets: the remaining mining reserve that funds the thin emission tail; the Raydium protocol treasury, which held around **$240M** in assets at its last quarterly report; and the buyback accumulation wallet, which has now gathered about **83.09M RAY** — roughly 31% of the circulating float — at a cumulative cost above $200M since the program began. None of these carries a published release schedule, so each is booked at zero flow and watched rather than projected. The framework re-reads the buyback wallet on-chain and the treasury on a roughly bi-weekly walk; if any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How RAY compares to other DEX and exchange tokens

RAY belongs to the class of **fee-sharing DEX tokens with a hard cap and a revenue-funded buyback**. Unlike an uncapped proof-of-stake L1 that mints continuously, RAY is capped at **555M**, is almost fully issued, and — unusually — has renounced its mint authority outright, so dilution risk is structurally near zero. The closest analogues are exchange and DEX tokens that recycle a share of fees into buybacks — but the key mechanism split is what happens to the coins afterward.

Some exchange tokens **burn** what they buy, which permanently shrinks total supply; Raydium instead **holds** bought-back RAY in a treasury wallet. For an inflation lens over a single window the effect is similar — the coins leave the open float either way — but the long-run read differs: a hold can in principle be reversed by governance, whereas a burn cannot. That distinction is exactly what drives the monitor gap: the framework nets the buyback off the active float and reads RAY as deflationary, while the supply monitor counts the held wallet as circulating and reads flat.

## What to watch in the next 90 days

Watch the buyback run-rate — it tracks Solana DEX trading volume, since the buyback is 12% of trading fees, and recent monthly fees of about **$4.6M** set the pace of the only real offset; fees have cooled from the prior quarter, which slows the buyback. Watch Solana DEX volume directly, as it drives the fee pool that funds everything. Watch for any governance move on the buyback wallet, since a decision to burn the held RAY — or to redeploy it — would change the read overnight. And watch the treasury for how the June 2026 AMM V3 exploit reimbursement is settled, in case any of it is paid in RAY.

## Summary

RAY is a hard-capped, fully-unlocked DEX token with its mint authority renounced, so new float is now just a thin mining-reserve tail of about 0.5M RAY over 90 days. Against it, a buyback funded by 12% of trading fees takes roughly 2.9M RAY off the open market and holds it in a treasury wallet, leaving the framework at about −0.89% net. Our supply monitor reads +0.26% — flat — because it counts the held wallet as circulating, so a 1.15-point gap chip ships. The key risk is the buyback run-rate, which tracks DEX volume, plus the governance-reversible held position; the key ceiling is the 555M cap, almost fully reached and no longer mintable, which keeps dilution structurally low.

---

*MrNasdog Pressure Framework analysis of Raydium (RAY), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 6, 2026.*

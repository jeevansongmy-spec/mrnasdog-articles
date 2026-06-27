---
title: "RAY Inflation Analysis · June 2026 · Buyback outpaces the last of the mint"
description: "Buyback outpaces the mint: Raydium issues ~0.5M RAY/90d vs a ~3M buyback held off market. Framework reads −0.9% net; monitor +0.24% flat, so a gap chip ships."
canonical_url: "https://mrnasdog.com/research/ray/inflation"
tags: ["crypto", "ray", "raydium", "defi"]
published: true
---

> Originally published at **[mrnasdog.com/research/ray/inflation](https://mrnasdog.com/research/ray/inflation)** by MrNasdog.

Raydium mints only about **0.5M RAY** over 90 days from a shrinking mining reserve, while a buyback funded by **12%** of all trading fees takes roughly **3M RAY** off the open market and holds it. The buyback clearly outpaces the mint, so the Pressure Framework reads about **−0.9% net** on the float. Our supply monitor reads **+0.24%** — essentially flat — because it counts the held buyback wallet as circulating, leaving a **1.17-point** gap.

## The verdict, in one paragraph

For the 90-day window ending June 28 2026, the MrNasdog Pressure Framework reads **RAY at about −0.9% net**: the fee-funded buyback removes far more RAY from the open market than the mining reserve issues. Our supply monitor reads the realized last-90-day change at **+0.24%** — flat — versus the framework's **−0.93%** read, a gap of about **1.17 percentage points**. Because that exceeds the 0.5-point tolerance, a **monitor-gap chip ships**. The gap is structural, not an error: the buyback sends RAY to a public accumulation wallet that the monitor's upstream still counts as circulating, so on-chain the buyback wallet grew from about **72M** to about **82.8M RAY** over the period while the realized circulating count barely moved. RAY is best read as **structurally deflationary on the active float**, with the held buyback as a governance-reversible overhang.

## Sell pressure: where new RAY comes from

Sell #1 — protocol inflation — is small and shrinking, at about **0.5M RAY** over the next 90 days. Raydium's original three-year emission schedule front-loaded **74%** of the mining reserve into its first year and finished in 2024; what remains is a thin tail of farming and staking rewards drawn from the reserve at roughly **1.9M RAY a year**. That is the only genuinely new RAY entering the market, and at this pace it is a fraction of one percent of the float per quarter.

Sell #2 — vesting unlocks — is **zero**: every team, seed, advisor and ecosystem allocation finished vesting in 2024, so RAY is fully unlocked and no cliff hits the market. Sell #3 — Foundation and unscheduled unlocks — is also zero as a flow; about **286M RAY** sits outside circulation across the mining reserve, the treasury, and the buyback wallet, but none of it has a published release schedule. The one in-window event was a June 10 2026 governance vote covering a **$1.3M** exploit of legacy 2021 AMM V3 pools (about 150,000 RAY plus SOL and USDC) out of treasury — already-held supply redeployed, not a new mint. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate or court distribution applies to RAY.

## Buy pressure: where new RAY goes

Buy #1 — programmatic buyback — is the dominant force, at about **3M RAY** over 90 days. Raydium routes **12%** of all trading fees into automatic RAY purchases on the open market across every pool type, regardless of fee tier. The critical detail is the destination — bought-back RAY is sent to a public accumulation wallet and **held, not burned**. On-chain, that wallet now holds about **82.8M RAY**, up roughly 10.8M over the period, confirming the buyback ran through the window. Because the coins leave the open float even though they are not destroyed, they count as buy-side pressure here.

Buy #2 — protocol fee burn — is **zero**, because there is no burn: the buyback accumulates RAY in a wallet rather than destroying it, so nothing is permanently removed from total supply. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero, with no discretionary open-market buying outside the fee buyback and no new escrow or lockup announced in the window.

## Foundation and overhang

The team-controlled overhang for RAY is the roughly **286M RAY** that sits outside circulation. It breaks into three tracked buckets: the remaining mining reserve that funds the thin emission tail; the protocol treasury, which closed Q3 2025 near **$240M** in assets; and the buyback accumulation wallet, which has now gathered about **82.8M RAY** — roughly 31% of the circulating float — at a cumulative cost above $200M since the program began. None of these carries a published release schedule, so each is booked at zero flow and watched rather than projected. The framework re-checks the buyback wallet on-chain and the treasury on a roughly bi-weekly walk; if any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How RAY compares to other DEX and exchange tokens

RAY belongs to the class of **fee-sharing DEX tokens with a hard cap and a revenue-funded buyback**. Unlike an uncapped proof-of-stake L1 that mints continuously, RAY is capped at **555M** and almost fully issued, so dilution risk is structurally low. The closest analogues are exchange and DEX tokens that recycle a share of fees into buybacks — but the key mechanism split is what happens to the coins afterward.

Some exchange tokens **burn** what they buy, which permanently shrinks total supply; Raydium instead **holds** bought-back RAY in a treasury wallet. For an inflation lens over a single window the effect is similar — the coins leave the open float either way — but the long-run read differs: a hold can in principle be reversed by governance, whereas a burn cannot. That distinction is exactly what drives the monitor gap: the framework nets the buyback off the active float and reads RAY as deflationary, while the supply monitor counts the held wallet as circulating and reads flat.

## What to watch in the next 90 days

Watch the buyback run-rate — it tracks Solana DEX trading volume, since the buyback is 12% of trading fees, and recent monthly fees of about **$4.6M** set the pace of the only real offset. Watch DEX trading volume on Solana directly, as it drives the fee pool that funds everything. Watch for any governance move on the buyback wallet, since a decision to burn the held RAY — or to redeploy it — would change the read overnight. And note that the mining-reserve tail keeps thinning each year, so the small new-supply line only gets smaller.

## Summary

RAY is a hard-capped, fully-unlocked DEX token whose new supply is now just a thin mining-reserve tail of about 0.5M RAY over 90 days. Against it, a buyback funded by 12% of trading fees takes roughly 3M RAY off the open market and holds it in a treasury wallet, leaving the framework at about −0.9% net. Our supply monitor reads +0.24% — flat — because it counts the held wallet as circulating, so a 1.17-point gap chip ships. The key risk is the buyback run-rate, which tracks DEX volume, and the governance-reversible held position; the key ceiling is the 555M cap, almost fully reached, which keeps dilution structurally low.

---

*MrNasdog Pressure Framework analysis of Raydium (RAY), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 28 2026.*

---
title: "RAY Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description: "RAY supply is roughly steady: 525K RAY of staking rewards gave +0.19% in 90 days. The 12% fee buyback bought 4.51M RAY but keeps it. Minting is off."
canonical_url: "https://mrnasdog.com/research/ray/inflation"
tags: ["crypto", "ray", "raydium", "defi"]
published: true
---
> Originally published at **[mrnasdog.com/research/ray/inflation](https://mrnasdog.com/research/ray/inflation)** by MrNasDog.

<!-- main-page -->
This is the long supply read. For the signal, the price drivers and the questions people ask about Raydium, see [mrnasdog.com/research/ray](https://mrnasdog.com/research/ray).

# RAY Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

RAY supply is roughly steady. Over the 90 days to Oct 11 2026, Raydium released **525,000 RAY** of staking rewards from its mining reserve, which grew the circulating supply by **+0.19%**, and the next 90 days look about the same. The 12% fee buyback bought **4.51M RAY** in the same window, but Raydium keeps the bought RAY in a wallet that already counts as circulating, so the buyback removes nothing from the supply count. RAY cannot be minted: the 555M cap is fixed in the token itself.

## The verdict, in one paragraph

The MrNasDog Pressure Framework reads RAY at **+0.19%** net new supply over the last 90 days (525,000 RAY sold into the float against 0 RAY taken out, on **269.86M RAY** circulating), and projects the same **+0.19%** for the next 90 days. The inflation monitor, which reads the same circulating figure every day, shows **+0.32%**. The gap is **0.13** percentage points, inside our 0.5-point tolerance, so no warning chip is shown. Part of the monitor's extra comes from one small step of about 25,000 RAY on Aug 26 2026 that we could not tie to any wallet, and part is rounding in its reading. In one line: RAY is a capped token with a small reward drip and a large buyback that hoards rather than burns.

## Sell pressure: where new RAY comes from

Protocol inflation is the only live sell row: **525,000 RAY** in 90 days. RAY cannot be minted — the mint authority on Solana is switched off — so new float comes only from the **188.7M RAY** mining reserve set aside at launch. Raydium moves reserve RAY into a release wallet, and that wallet sends RAY to the staking reward pool about once a month: 200,000 RAY on Aug 10 2026, 200,000 RAY on Sep 10 2026 and 125,000 RAY on Sep 28 2026. The moment RAY leaves the release wallet it becomes part of the circulating supply; the circulating figure stepped up by the same amounts the next day. Stakers then earn it at about **5.6%** a year on the **43.26M RAY** staked. Raydium's own docs put the reward stream at about 1.9M RAY a year, and our 90-day count sits a little above that pace.

Vesting unlocks are **0**. The team and seed allocations, 25.9% of supply, finished vesting on Feb 21 2024, and no vesting calendar is left. Foundation and unscheduled unlocks are also **0**: none of the six allocation wallets moved in the window (more in the overhang section below). Long-term locked or bankruptcy supply is **0**; there is no estate, trustee or long lock releasing RAY.

## Buy pressure: where new RAY goes

The programmatic buyback is real and large, but it books **0**. Raydium sends 12% of every trading fee to buy RAY: 84% of a CLMM or CPMM pool fee goes to liquidity providers, 12% to the RAY buyback and 4% to the treasury, while older AMM v4 pools split 88% and 12%. In the 90 days to Oct 11 2026 that bought **4.51M RAY**, most of it after Raydium's fees jumped in September on tokenized-stock launches. The bought RAY is not burned. It is held in a public protocol wallet that now holds **87.72M RAY**, about 32.5% of the circulating supply. Because that wallet is already counted as circulating, buying into it moves RAY between holders inside the float; it does not shrink the supply we measure. It does take RAY off exchanges, which matters for price, but that belongs to demand, not supply.

The protocol fee burn is **0**: Raydium has no burn. Only about 2,620 RAY has ever been destroyed, by single users, since 2021. Foundation buying is **0** beyond the fee buyback. New long-term locks are **0**: the 43.26M RAY in staking can be withdrawn at any time and still counts as circulating.

## Foundation and overhang

Raydium controls **282.66M RAY** that sits outside the circulating supply, in six allocation wallets with no release schedule: partnership and ecosystem **138.59M**, mining reserve **123.32M**, advisors **11.10M**, team **7.30M**, community and seed **2.35M**, and an empty liquidity wallet. Their last real moves were years ago: the ecosystem wallet in September 2023, the team and community wallets in February 2024, and the mining reserve on Feb 25 2024, when it sent 2.9M RAY to the reward release wallet. The advisors' 11.10M has not moved since 2021. The release wallet itself holds **254,372 RAY**, about 45 days of rewards at the recent pace, so a new top-up from the mining reserve is likely soon; that top-up moves RAY between two wallets outside the float and adds nothing until the RAY is released to stakers.

Inside the float, Raydium also controls the buyback wallet (**87.72M RAY**) and a protocol multisig (**8.87M RAY**). These are already counted, so a sale from either would not add supply, but either could reach the market. We read all of these wallets on-chain at every rebuild. If any outside-the-float wallet's balance falls between refreshes, the outflow enters the Foundation and unscheduled unlocks row at the next refresh.

## How RAY compares to other DEX tokens

Among exchange tokens, RAY sits between the burners and the printers. Some DEX and launchpad tokens send fee buybacks to a burn address or lock them for good, so every buyback shrinks the count; others pay no fees to the token at all and grow supply through farm emissions alone. RAY has a large, mechanical buyback — **12% of all fees**, visible on-chain — but keeps the bought coins in a treasury wallet. That makes the buyback a strong demand force and a weak supply force: the 87.72M RAY could, in principle, be sold or used again.

On emissions, RAY is light. A fixed 555M cap with minting switched off is stricter than most DeFi tokens, whose teams can often mint more by vote. RAY's new float of about **0.19%** a quarter is small next to tokens still running heavy farm rewards or monthly team unlocks. The real risk is not the reward drip but the **282.66M RAY** of reserve and team wallets with no published schedule — more than the whole circulating supply of 269.86M RAY. A token with that much undecided supply depends on the team choosing not to move it.

## What to watch in the next 90 days

First, a top-up of the reward release wallet from the mining reserve: at about 200,000 RAY a month, its 254,372 RAY runs low before the end of 2026. Second, any move from the partnership and ecosystem wallet (138.59M RAY) or the advisors wallet (11.10M RAY), which have been still since 2023 and 2021. Third, the buyback pace: fees jumped in September 2026, and a lasting change would show up in the buyback wallet each month. Fourth, any change to what happens to bought-back RAY — a burn or a permanent lock would turn the buyback into a real supply cut. No dated supply event is scheduled before Jan 9 2027.

## Summary

RAY, the token of the Raydium exchange on Solana, grew its circulating supply by **+0.19%** in the 90 days to Oct 11 2026, from **525,000 RAY** of staking rewards released from the mining reserve, and the next 90 days look the same. The 12% fee buyback bought **4.51M RAY** but keeps it in a wallet counted as circulating, so it supports demand without cutting supply. Minting is switched off and the cap is 555M RAY. The key risk is the **282.66M RAY** in reserve and team wallets that have no release schedule.

---

*MrNasDog Pressure Framework analysis of RAY, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 11 2026.*

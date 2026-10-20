---
title:         "TRX Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description:   "TRX supply is roughly steady: TRON minted 352M TRX in block rewards against a 227M TRX fee burn, +0.13% net over 90 days and about the same next. No cap."
canonical_url: "https://mrnasdog.com/research/trx/inflation"
tags:          ["crypto", "trx", "tron", "payments"]
published:     true
---
# TRX Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

*Originally published at [mrnasdog.com/research/trx/inflation](https://mrnasdog.com/research/trx/inflation).*

<!-- main-page -->
**Main page:** the full TRX coin page — signal, price drivers and the buy/sell questions → [mrnasdog.com/research/trx](https://mrnasdog.com/research/trx)

TRON's supply is close to flat. Over the last 90 days the TRON network minted **352.4M TRX** in block rewards and destroyed **226.95M TRX** in fees, so TRX supply grew a net **+0.13%**, and we expect about the same over the next 90 days. TRX has no supply cap and no vesting left: the only things that move supply are the 136 TRX minted with every block and the fee burn, and the burn now covers about two thirds of the new coins.

## The verdict, in one paragraph

TRX supply rose **+0.13%** over the last 90 days (Jul 13 2026 to Oct 10 2026) and is projected to rise **+0.13%** over the next 90. Our supply monitor, which reads circulating supply from the market each day, shows **+0.13%** for the same stretch, a gap of about **0.00 percentage points** — far inside our 0.5-point tolerance, so no warning chip is needed and the reading stands as checked. TRON is a **low-inflation chain held near flat by its fee burn**: it prints new TRX every three seconds, and the people paying for transactions destroy most of it.

## Sell pressure: where new TRX comes from

Protocol inflation is the only source of new TRX. Every block mints **136 TRX**: 8 TRX to the Super Representative that produced it, and 128 TRX shared among the top 127 vote-getters, who pass much of it on to the TRX holders who vote for them. The TRON network produced **2,591,074 blocks** in the window, so it minted **352.4M TRX**, about **3.92M TRX a day**. That reward was last changed by a network vote in June 2025 (from 16 + 160 TRX down to 8 + 128 TRX per block), and no vote to change it again is open.

Vesting unlocks are **zero**. The TRX token sale and team allocation date back to 2017, and every coin from them was released years ago; today circulating supply sits within 0.001% of total supply, so there is no locked bucket left to unlock. Foundation and unscheduled unlocks are also **zero**: the old Foundation fund accounts are dormant, and every large holder already counts as circulating. Long-term locks and bankruptcy releases are **zero** too: no estate or trustee holds TRX for release, and staked TRX can leave its stake 14 days after unstaking but was already counted as circulating while staked.

## Buy pressure: where new TRX goes

The protocol fee burn is the only thing removing TRX. Every fee paid in TRX on TRON — for bandwidth and energy, smart contract calls such as USDT transfers, new accounts, memos and multisig — is destroyed rather than paid to anyone. Over the 90 days it destroyed **226.95M TRX**, about **2.52M TRX a day**, which offsets about **64%** of the new block rewards. We measured it as the gap between new coins minted and the change in total supply, and a random sample of blocks read straight from the chain gave a matching figure.

The burn is slowly shrinking. It destroyed **84.2M TRX** in the first 30 days of the window, **72.4M** in the middle 30 and **70.3M** in the last 30, with no fee change behind it. Many users stake TRX for free energy instead of paying fees, and the energy price was cut from 210 to 100 sun in August 2025. Because no new rule changed in the window, the forward figure keeps the 90-day rate; if the decline continues, the next 90 days will come in a little above +0.13%.

Programmatic buyback is **zero**: the protocol buys nothing back. Foundation buy is **zero** as well. Tron Inc., a Nasdaq-listed company, buys about 150,000 TRX every day under a 360-day plan that began Jan 22 2026 and now holds about **716.8M TRX**, but it buys coins already in the market, so the float does not shrink. New long-term lock is **zero**: about **45.39B TRX** is staked, down from 45.78B at the start of the window, and a staked TRX fund began trading in September, yet staked TRX still counts as circulating.

## Foundation and overhang

The team-controlled overhang on TRON is small and quiet. The old TRON Foundation fund accounts are all but empty: together they hold about **283 TRX** (164 and 119 in the two main accounts, dust in the rest), and neither main account has made a transaction of its own since 2020. Tron Inc.'s treasury of about **716.8M TRX** is a listed company's holding rather than a project reserve, and it has only been buying. We read the Foundation accounts on-chain at every rebuild and walk the company's purchase reports by hand. If any of these balances falls between rebuilds, the outflow is checked against circulating supply and enters the Foundation row at the next rebuild — though because these coins are already counted as circulating, a sale would move TRX between holders rather than add new supply.

## How TRX compares to other high-throughput Layer 1s

TRON sits between two common designs. Chains like Ethereum mint new coins for validators and burn part of each fee, but on Ethereum the burn now covers under 2% of new issuance; on TRON the burn covers about two thirds, because TRON's USDT traffic pays a large and steady fee bill. Chains like BNB Chain add a scheduled burn on top of the gas burn and shrink their supply, while TRON has no scheduled burn, so its net stays slightly positive.

Against uncapped staking chains such as Solana or Cardano, TRX inflation is far lower: those chains pay stakers new coins as a share of supply or from a reserve, while TRON mints a fixed 136 TRX per block no matter how much is staked, so its inflation rate falls slowly as supply grows. Unlike a capped proof-of-work coin such as Bitcoin, TRX has no halving and no maximum supply; the block reward only changes when the Super Representatives vote to change it.

The key difference is what sets the burn. On TRON the burn is paid mostly by stablecoin users, so TRX supply depends on how much USDT moves on TRON and how many users pay in TRX rather than with staked energy. In 2024 the burn was larger than the mint and TRX supply shrank; since the 2025 energy price cut, it has run below the mint.

## What to watch in the next 90 days

The monthly fee burn: it fell from **84.2M** to **70.3M TRX** over the window, and a further drop would push TRX's 90-day net above +0.13%.

Two open fee proposals on TRON's improvement board: cutting the account-permission fee from 100 to 8 TRX (discussion updated Oct 7 2026) and the multisig fee from 1 to 0.5 TRX (opened Oct 6 2026). Neither has an on-chain vote yet; both would trim the burn slightly.

Any network vote on the block reward or the energy price. The last ones passed in June 2025 and August 2025; a new vote would change the mint or the burn directly.

Tron Inc.'s buying plan, set to run to about Jan 2027, and the staked TRX fund that began trading in September 2026. Both move coins already counted as circulating, so they change who holds TRX, not how much exists.

## Summary

TRX supply is roughly steady: TRON minted **352.4M TRX** in block rewards over 90 days and its fee burn destroyed **226.95M TRX**, a net **+0.13%**, matching our supply monitor. TRX has no cap and no vesting, so the only supply levers are the fixed 136 TRX per block and the fee burn. The main risk is a shrinking burn as users switch to staked energy and fees are cut, which would let the net creep up. The ceiling is set by the mint itself: even with no burn at all, TRX supply would grow only about **0.37%** in 90 days.

---

*MrNasDog Pressure Framework analysis of TRX, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 11 2026.*

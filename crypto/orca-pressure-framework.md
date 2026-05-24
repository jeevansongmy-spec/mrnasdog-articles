---
title: "Orca (ORCA): Solana DEX with a 100M Hard Cap, Final Stretch of Emissions"
description: "A MrNasdog Pressure Framework read of Orca (ORCA): the Solana DEX's native token. 60.8M circulating of 100M hard cap, ~25M remaining team/foundation/community emissions. Buy ledger is currently empty; fee switch debate ongoing."
canonical_url: "https://mrnasdog.com/research/orca/full"
tags: ["crypto", "orca", "solana", "dex", "defi"]
published: true
---

> Originally published at **[mrnasdog.com/research/orca/full](https://mrnasdog.com/research/orca/full)** by MrNasdog.

This is a MrNasdog Pressure Framework analysis of **Orca (ORCA)** on Metric 1 (sell pressure) and Metric 2 (buy pressure). Narrative (Metric 3) is covered separately. The short version: Orca is the main concentrated-liquidity DEX on Solana. ORCA has a fixed 100M hard cap with 60.8M circulating — most of the original distribution is unlocked, with ~25M remaining in team / foundation / community emissions. The buy ledger is structurally empty.

## The setup

Orca is the leading Solana concentrated-liquidity AMM (Whirlpools), launched 2021. ORCA is the governance token. It's an SPL token on Solana with a **fixed 100M max supply** set at the genesis allocation.

Original allocation (per Orca docs):
- 51% team / advisors / strategic investors (vested over 3 years from 2021)
- 26% community-allocated emissions (yield farming, grants, retroactive)
- 13% Orca DAO treasury
- 10% public liquidity bootstrapping

Most allocations are now fully vested. Remaining locked supply (~25M) is in DAO-controlled emissions and treasury — Tag B-adjacent.

Live numbers, origin-first from Solana RPC + Orca docs:

- **Max supply: 100M ORCA** (fixed cap)
- **Total supply minted: ~75M ORCA** (per CoinGecko cross-check)
- **Circulating: ~60.8M ORCA** (~80% of minted)
- **Still-minted-but-not-circulating: ~14M ORCA** (in DAO treasury + emissions pools)
- **Still-to-mint: ~25M ORCA** (toward the 100M cap)
- Price ~$1.44 → market cap ~$90M · FDV ~$144M

## The sell ledger

*What the design predictably puts on the market.*

| # | Source | Tag | Value |
|---|---|---|---|
| 1 | Protocol inflation | — | **0** (100M cap is the limit; emissions are not inflation in the macro sense) |
| 2 | **Emissions / vesting (still-locked, scheduled release)** | **Tag A** | **~25M ORCA** remaining toward the 100M cap, plus emission release schedule |
| 3 | Team / DAO / identified-group holdings | **Tag B** | Orca DAO treasury + Foundation reserves — ~14M ORCA |
| 4 | Bankruptcy estate | — | **0** |

**Vesting / remaining emissions is the structural sell line.** ~25M ORCA is still to be minted (the gap from 75M minted to the 100M cap), and another ~14M is minted-but-not-circulating in DAO/emissions pools. At today's circulating of ~60.8M, that's another ~39M of supply expansion to come — substantial relative to current float.

**Tag B is the Orca DAO + Foundation** — Solana program-controlled, on-chain readable. Discretionary deployment via DAO votes for grants, liquidity incentives, etc.

## The buy ledger

*What the design predictably takes off the market.*

| # | Source | Value |
|---|---|---|
| 1 | Revenue-backed buyback | **0** — Orca DEX collects fees but no buyback contract |
| 2 | Burn mechanism | **0** structural |
| 3 | Locked allocations | — context only |
| 4 | Protocol-level demand (governance only) | **~0** — ORCA is governance; trading on Orca uses SOL/SPL tokens |

**Buy ledger is empty.** Orca generates real DEX revenue from Whirlpools (concentrated liquidity) fees — but the fees go to LPs, not to ORCA. A fee switch / buyback was debated in 2023–2024 but never permanently activated.

## Net position

- **Sell, Tag A:** ~39M of remaining supply expansion ahead (emissions + Tag B deployments)
- **Buy, Tag A:** 0

Same shape as UNI in DeFi terms: clean fixed cap, vest mostly done, but structural buy is zero pending a fee switch. Smaller scale, similar lever.

Compared to the rest of our coverage:
- **ORCA / UNI**: small DEXes with empty buy ledger, fee switch is the lever — neutral / lever-dependent
- **RAY**: structural ~12% of fees buy back RAY — favorable (the standout DEX)
- **SKY / HYPE**: structural revenue → buyback — favorable
- **CHIP / SUI / ARB**: heavy still-locked supply — unfavorable

## What could flip the buy ledger

Same as UNI: **fee switch**. Orca's Whirlpools generate notable fee revenue; if the DAO routes a portion to a structural buyback (à la Raydium's ~12% of swap fees → RAY buyback), the picture changes. Pending DAO governance.

## What to watch

1. **Orca DAO governance proposals on fee-share / buyback**.
2. **Orca emissions schedule** — the path from 75M minted toward the 100M cap.
3. **Whirlpools fee volume** — sizing the latent buyback lever.
4. **DAO Treasury balance** — readable on Solana.

---

*MrNasdog Pressure Framework analysis of ORCA, Metrics 1 &amp; 2. Data + explanation only. Not financial advice. Numbers as of May 2026.*

*Data note: Max supply (100M) per Orca official tokenomics. Total supply + circulating cross-checked via CoinGecko. ORCA mint address on Solana available via Orca docs; balances of the DAO treasury and emission pools require querying the Solana RPC for the specific program-controlled accounts.*

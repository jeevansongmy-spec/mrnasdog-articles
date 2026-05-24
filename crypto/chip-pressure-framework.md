---
title: "USD.AI (CHIP): 80% of Supply Still Locked, AI-Compute Stablecoin Thesis"
description: "A MrNasdog Pressure Framework read of USD.AI (CHIP): 2B circulating of 10B max (80% locked). Multi-chain across Ethereum / Arbitrum / Base / Solana. Stablecoin-adjacent project; demand depends on USDai adoption."
canonical_url: "https://mrnasdog.com/research/chip/full"
tags: ["crypto", "chip", "usd-ai", "ai", "stablecoin"]
published: true
---

> Originally published at **[mrnasdog.com/research/chip/full](https://mrnasdog.com/research/chip/full)** by MrNasdog.

This is a MrNasdog Pressure Framework analysis of **USD.AI (CHIP)** on Metric 1 (sell pressure) and Metric 2 (buy pressure). Narrative (Metric 3) is covered separately. The short version: CHIP is early — 80% of total supply is still locked under team / investor / ecosystem schedules, and the buy ledger depends on whether USDai (the project's stablecoin) gets real adoption.

## The setup

USD.AI is a project building "the dollar that scales AI" — a stablecoin (USDai) and a related governance/utility token (**CHIP**) positioned around AI compute and on-chain financial primitives. CHIP is deployed on **four chains** with the same EVM contract address (`0x0c1c…1f6e`) — Ethereum, Arbitrum, Base — plus a separate SPL on Solana (`chipCAT7vi5CZtbZsn9z7iMPXvFwyAnKz3QFu8XVuHm`).

Live numbers, origin-first from usd.ai docs + CoinGecko cross-check:

- **Max supply: 10,000M (10B) CHIP** — fixed cap
- **Circulating: ~2,000M (~20%)**
- **Still locked: ~8,000M (~80%)** — distributed across team, investors, ecosystem, treasury per the project's published tokenomics
- Price ~$0.048 → market cap ~$96M · FDV ~$480M
- Multi-chain deployment: ETH + Arbitrum + Base + Solana

## The sell ledger

*What the design predictably puts on the market.*

| # | Source | Tag | Value |
|---|---|---|---|
| 1 | Protocol inflation | — | **0** (10B fixed cap) |
| 2 | **Vesting unlocks (still-locked allocations on schedule)** | **Tag A** | **~8B CHIP** scheduled to release per published cliffs (multi-year) |
| 3 | Team / DAO / identified-group holdings | **Tag B** | USD.AI Foundation / Permian Labs treasuries — TBD on-chain enumeration |
| 4 | Bankruptcy estate | — | **0** |

**Vesting is the structural sell line.** With ~8B CHIP still locked against ~2B circulating, **the next 24–48 months will see circulating supply roughly multiply** as cliffs release. The exact pace depends on the team / investor / ecosystem cliff schedule published in USD.AI's tokenomics — a typical 4-year linear vest from TGE means ~25%/yr of locked supply releasing.

**Tag B is USD.AI Foundation + Permian Labs treasury** (the entity building the protocol). Discretionary. The 4-chain deployment makes enumeration slightly more involved — need to read the contract address `0x0c1c…1f6e` on each of ETH / ARB / Base, plus the Solana SPL. Flagged TBD here.

**Bankruptcy estate: zero.**

## The buy ledger

*What the design predictably takes off the market.*

| # | Source | Value |
|---|---|---|
| 1 | Revenue-backed buyback | **0** — no buyback contract today |
| 2 | Burn mechanism | **0** structural |
| 3 | Locked allocations | — context only |
| 4 | Protocol-level demand (USDai adoption + AI-compute payments) | **Tag B** — entirely adoption-dependent |

**The buy ledger is entirely thesis-dependent.** USD.AI's pitch is that CHIP underpins a stablecoin (USDai, ~$288M circulating per CoinGecko) and AI-compute payment rails. If USDai grows materially and CHIP captures a fee share, that becomes a Tag A line. **Today, nothing structural buys CHIP** — adoption is the entire bet.

## Net position

- **Sell, Tag A:** ~8B CHIP still under multi-year vesting (estimated ~2B/yr at linear rate)
- **Buy, Tag A:** 0 (adoption-dependent, not structural)

**Structurally unfavorable today** — same shape as SUI and ARB: scheduled supply up, structural buy ~0. The wrinkle: at 20% circulating, CHIP has the **largest unvested fraction in our coverage**. The adoption thesis would have to do a lot of work in the next 2 years to absorb the vest.

Compared to the rest of our coverage:
- **CHIP**: ~80% still locked, vested over multi-year — **highest unvested fraction in lineup**
- **SUI**: ~60% still locked through ~2030 — very unfavorable
- **ONDO**: ~17%/yr cliffs through 2029 — very unfavorable
- **ARB**: ~37% still vesting + 27% in DAO Treasury — unfavorable

## What could flip the buy ledger

USDai adoption is the entire thesis. If the stablecoin reaches the multi-billion mark and CHIP captures protocol fees (or a buyback funded by stablecoin yield), the picture changes materially. Until then, the buy ledger is empty.

## What to watch

1. **USDai circulating supply growth** — proxy for adoption.
2. **USD.AI published vesting schedule** — precise per-month CHIP unlock pace.
3. **Any protocol fee → CHIP buyback proposal**.
4. **CHIP balances on the 4 chains** — multi-chain enumeration is the Tag B project.

---

*MrNasdog Pressure Framework analysis of CHIP, Metrics 1 &amp; 2. Data + explanation only. Not financial advice. Numbers as of May 2026.*

*Data note: Total supply + circulating from CoinGecko cross-check (CHIP id `chip-2`). Multi-chain contract address `0x0c1c…1f6e` (ETH / Arbitrum / Base) + Solana SPL `chipCAT…UHm` per CoinGecko platforms field. Project homepage: `usd.ai`. Vesting cliff details require USD.AI's official tokenomics page; enumeration of Foundation / Permian Labs balances across all 4 chains is the next step.*

---
title: "Arbitrum (ARB): 37% of Supply Still Unlocked, DAO Treasury Holds 27%"
description: "A MrNasdog Pressure Framework read of Arbitrum (ARB): fixed 10B supply, ~6.26B circulating, ~3.74B still under team/investor vesting through 2027. DAO Treasury holds 2.66B ARB (~27%) — read on-chain from the Arbitrum L2 RPC."
canonical_url: "https://mrnasdog.com/research/arb/full"
tags: ["crypto", "arbitrum", "layer2", "rollup"]
published: true
---

> Originally published at **[mrnasdog.com/research/arb/full](https://mrnasdog.com/research/arb/full)** by MrNasdog.

This is a **MrNasdog Pressure Framework** analysis of **Arbitrum (ARB)** on Metric 1 (sell pressure) and Metric 2 (buy pressure). Narrative (Metric 3) is covered separately. The short version: ARB has a fixed 10B cap, but **37% of supply is still under team/investor vesting through 2027**. The Arbitrum DAO Treasury holds **2.66B ARB on-chain** — the largest identified treasury we've measured. Buy ledger is empty.

## The setup

Arbitrum is the leading Ethereum L2 rollup, built by Offchain Labs and governed by the Arbitrum Foundation + Arbitrum DAO. ARB launched in March 2023 (airdrop) and is native to Arbitrum One (`0x912c…6548`). Genesis supply: **10B ARB** with the following allocation per the official Arbitrum Foundation tokenomics:

- **42.78% DAO Treasury** (4.278B) — controlled by ARB-token governance via the Treasury Timelock
- **26.94% Team (Offchain Labs)** (2.694B) — 4-year vest with 1-year cliff (cliff hit March 2024; linear vest through March 2027)
- **17.53% Investors** (1.753B) — same vest schedule
- **11.62% Airdrop recipients** (1.162B) — fully unlocked at TGE
- **1.13% DAOs (other community)** (0.113B)

The DAO controls protocol parameters and can enable inflation up to 2%/yr (similar to UNI's latent option).

Live numbers, origin-first from the Arbitrum One mainnet RPC (`arb1.arbitrum.io/rpc`):

- **Total supply: ~9,999.999M ARB** (`totalSupply()` on `0x912c…6548`, fixed cap)
- **Circulating: ~6,255.8M ARB** (per CoinGecko cross-check)
- **Still-locked / Tag A on schedule: ~3,744M ARB** (~37% of total) releasing linearly through March 2027
- **DAO Treasury (Timelock `0xf3fc…9b58`): ~2,656.9M ARB** (~26.6% of supply — read on-chain via `balanceOf`)
- Price ~$0.106 → market cap ~$0.66B · FDV ~$1.06B

## The sell ledger

*What the design predictably puts on the market.*

| # | Source | Tag | Value |
|---|---|---|---|
| 1 | Protocol inflation | — | **0** (2%/yr available but not enabled by DAO) |
| 2 | **Vesting unlocks (still-locked Team + Investor allocations)** | **Tag A** | **~3.74B ARB**, linear vest through March 2027 |
| 3 | **Team / DAO / identified-group holdings** | **Tag B** | DAO Treasury **2.66B ARB** (on-chain, deployed via votes) |
| 4 | Bankruptcy estate | — | **0** |

**Vesting is the headline.** 3.74B ARB is still locked under the Team + Investor schedule, releasing linearly through March 2027. **At today's circulating ~6.26B, the additional ~3.74B coming over ~22 months means roughly +60% to circulating supply** by the end of the vest. This is a substantial structural sell wave.

**Tag B is the DAO Treasury Timelock** (verified on-chain: 2.66B ARB at `0xf3fc…9b58`). This is the largest single identified treasury we've measured in our coverage. Deployed via Arbitrum DAO governance — grants programs, retroactive funding, market-making, etc. Discretionary. **Note: de-duped against #2 — the DAO Treasury portion is already unlocked, so it counts here, not in #2.**

**Inflation: zero.** The DAO can enable up to 2%/yr; never enabled.

## The buy ledger

*What the design predictably takes off the market.*

| # | Source | Value |
|---|---|---|
| 1 | Revenue-backed buyback | **0** — no contract buys ARB |
| 2 | Burn mechanism | **0** — no protocol burn (sequencer fees collected, distributed to DAO Treasury) |
| 3 | Locked allocations | — context only (ARB staking is governance-only; functionally liquid) |
| 4 | Protocol-level demand | **~0** — ARB is governance, not gas (gas on Arbitrum One is paid in ETH) |

**This is where Arbitrum is structurally weakest.** ARB is purely a governance token. Sequencer revenue flows to the DAO Treasury — but the DAO has not voted to deploy any of it as a buyback. Gas on Arbitrum One is paid in ETH, not ARB; there's no native protocol-level demand sink for ARB.

## Net position

- **Sell, Tag A:** ~3.74B ARB through March 2027 (~1.7B/yr at the linear rate)
- **Sell, Tag B:** 2.66B in DAO Treasury (deployed via governance)
- **Buy, Tag A:** 0

**This is the most-unfavorable structural read in our coverage.** ARB combines the worst-of-both: massive scheduled supply (~37% of total still vesting, same scale as SUI) AND a giant identified Tag B treasury that could be deployed any time (~27% of total). All against zero structural buy pressure.

Compared to the rest of our coverage:
- **ARB**: ~37% still vesting + 27% in DAO Treasury, no buy — **most unfavorable**
- **ONDO**: ~17%/yr cliffs through 2029, no buy — very unfavorable
- **SUI**: ~60% still unvesting through ~2030 — very unfavorable
- **TAO**: ~27%/yr inflation but halving in 10mo — unfavorable, with programmed catalyst

## The two governance levers

Like UNI, ARB has two latent governance-controlled levers:

1. **Positive:** **Fee switch / revenue routing** — sequencer revenue (significant) could be routed to ARB buyback or stakers. Never enabled. The largest possible structural buy-side catalyst available in our coverage today.
2. **Negative:** **2%/yr inflation enablement** — DAO can pass this. Latent risk.

## What to watch

1. **Monthly Team + Investor unlock disclosures** — Arbitrum Foundation publishes; track cliff effects.
2. **Any DAO proposal on fee-switch / revenue routing** — would flip the buy ledger.
3. **DAO Treasury balance** — read live via Arbitrum L2 RPC; large grants programs move this.
4. **Arbitrum One sequencer revenue trend** — sizing the latent buy-side lever.

---

*MrNasdog Pressure Framework analysis of ARB, Metrics 1 &amp; 2. Data + explanation only. Not financial advice. Numbers as of May 2026.*

*Data note: Total supply + DAO Treasury balance read directly from the Arbitrum One mainnet RPC (`arb1.arbitrum.io/rpc`) — `totalSupply()` on the ARB ERC-20 (`0x912c…6548`) and `balanceOf(0xf3fc…9b58)` on the DAO Treasury Timelock. Vesting schedule per the Arbitrum Foundation tokenomics docs. Circulating supply cross-checked via CoinGecko.*

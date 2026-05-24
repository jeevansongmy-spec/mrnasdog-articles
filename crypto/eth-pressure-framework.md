---
title: "Ethereum (ETH): Net Deflationary, Most of the Time"
description: "A MrNasdog Pressure Framework read of Ethereum (ETH): ~0.5%/yr gross issuance to validators, EIP-1559 base-fee burn that flips supply net-deflationary during active periods. No team allocation, no scheduled vesting. The cleanest structural sell ledger of any major L1."
canonical_url: "https://mrnasdog.com/research/eth/full"
tags: ["crypto", "ethereum", "layer1", "defi"]
published: true
---

> Originally published at **[mrnasdog.com/research/eth/full](https://mrnasdog.com/research/eth/full)** by MrNasdog.

This is a **MrNasdog Pressure Framework** analysis of **Ethereum (ETH)** on Metric 1 (sell pressure) and Metric 2 (buy pressure). Narrative (Metric 3) is covered separately. The short version: ETH has the cleanest structural sell ledger of any major layer-1 — no team allocation, no scheduled vesting, ~0.5%/yr gross issuance to validators, with EIP-1559 burning base fees in real time. When the chain is active, net supply is flat or shrinking.

## The setup

Ethereum is the leading smart-contract platform. Genesis July 2015 with a public ICO. Moved to proof-of-stake in September 2022 ("The Merge"), reducing issuance ~90% overnight. Shanghai/Capella (April 2023) enabled validator withdrawals. EIP-1559 (August 2021) introduced a base-fee burn on every transaction.

Live numbers, origin-first from the Ethereum mainnet:

- **Circulating supply: ~120.7M ETH** (per CoinGecko cross-check)
- **No fixed max supply** — issuance is dynamic, capped only by the deposit-aware schedule (issuance falls as more ETH is staked)
- **Validator issuance: ~0.5%/yr gross** (varies with total staked ETH; ~30%+ of supply is staked)
- **EIP-1559 burn**: every transaction destroys its base fee in ETH; burn rate scales with gas demand
- **Net supply trend (post-merge era)**: roughly **flat-to-deflationary** in active periods, mildly inflationary in quiet ones
- Price ~$2,116 → market cap ~$255B

The fundamental design: validators get paid in newly-issued ETH (gross sell pressure), users pay base fees in ETH that get burned (gross buy pressure). The two flows offset; net direction depends on activity.

## The sell ledger

*What the design predictably puts on the market.*

| # | Source | Tag | Value |
|---|---|---|---|
| 1 | **Protocol inflation** — validator issuance, deposit-aware | **Tag A** | **~0.5%/yr gross**, scales inversely with total staked |
| 2 | Vesting unlocks (still-locked allocations on schedule) | — | **0** — original 2014 ICO + Ethereum Foundation grants have no published cliff schedule today |
| 3 | Team / DAO / identified-group holdings | **Tag B** | Ethereum Foundation reserves + Vitalik wallet — TBD on-chain enumeration |
| 4 | Bankruptcy estate (Genesis estate, post-bankruptcy distributions) | **Tag A small** | DCG/Genesis estate has distributed most BTC + ETH from the 2023 bankruptcy; residual modest |

**Inflation is the only meaningful Tag A line.** Post-merge issuance is ~0.5%/yr gross — about 600K–700K new ETH/yr distributed to validators. This is tiny relative to ETH's market cap and is the lowest-inflation top-tier L1 we cover.

**Vesting is zero by the framework's definition.** The 2014 ICO completed a decade ago; there is no scheduled team/investor vesting today. Ethereum Foundation grants are discretionary, not scheduled — they belong in source #3.

**Tag B is the Ethereum Foundation and identified founder wallets.** The Foundation publishes annual transparency reports; recent balances are in the hundreds of millions USD-equivalent. Vitalik Buterin's identified wallet is small relative to total supply. Both are discretionary. Flagged TBD here pending exact on-chain enumeration.

## The buy ledger

*What the design predictably takes off the market.*

| # | Source | Value |
|---|---|---|
| 1 | Revenue-backed buyback | **0** — no contract buys ETH from market |
| 2 | **Burn mechanism (EIP-1559 base-fee burn)** | **Tag A** — variable, scales with network activity |
| 3 | Locked allocations | — context only (~30%+ of supply is staked, ~days-to-weeks withdrawal queue) |
| 4 | Protocol-level demand (gas) | **Tag A** — ETH is gas; demand baseline is real and structural |

**EIP-1559 is the entire structural buy story.** Every transaction's base fee gets burned. In active periods (DeFi summer 2021, NFT mania, restaking flows) the burn exceeded validator issuance, making ETH net deflationary. In quiet periods (the 2024 L2 era after L2s absorbed most activity), the burn fell below issuance, making ETH mildly inflationary again. **Direction depends on L1 demand.**

## Net position

Combine the ledgers:

- **Sell, Tag A:** ~0.5%/yr gross issuance (validator rewards)
- **Buy, Tag A:** EIP-1559 burn, variable, has historically offset most or all of issuance
- **Net structural change:** roughly **flat-to-deflationary** in active periods, **mildly inflationary** in quiet ones

This makes ETH the **cleanest structural read of any major L1** — both sides are Tag A, both are tied to a single variable (L1 activity), and the two flows offset by design.

Compared to the rest of our coverage:
- **ETH**: Tag A on both sides, nets to roughly zero — most-favorable structurally
- **BNB**: ↓3–6%/yr from burns, no inflation — also favorable
- **HYPE**: AF buyback > vesting, supply flat — favorable
- **SKY**: revenue-linked buyback — moderately favorable
- **NEAR / TAO**: ↑ inflation with weak buy — unfavorable
- **SUI / ONDO**: ↑ scheduled supply, weak buy — most unfavorable

## What could flip the buy ledger negatively

The structural risk is **L1 activity collapse driving the EIP-1559 burn to ~0** while validator issuance continues. This happened mildly in 2024 when most activity moved to L2s. If L1 activity stays low while issuance continues, ETH drifts mildly inflationary. The Pectra and Fusaka upgrades modify validator economics but don't change the basic burn-vs-issuance mechanic.

## What to watch

1. **Burn rate vs. issuance rate** — ultrasound.money or similar; the cross-over point flips ETH from deflationary to inflationary.
2. **L1 activity** — base-layer gas usage drives the burn; L2 settlement to L1 is a partial substitute.
3. **Total staked ETH** — higher staking lowers per-validator issuance rate (deposit-aware curve).
4. **Ethereum Foundation transparency reports** — annual disclosures of Tag B holdings.

---

*MrNasdog Pressure Framework analysis of ETH, Metrics 1 &amp; 2. Data + explanation only. Not financial advice. Numbers as of May 2026.*

*Data note: Issuance rate per ethereum.org documentation (deposit-aware curve). Burn rate variable per real-time gas activity. Circulating supply cross-checked via CoinGecko. Ethereum Foundation balance flagged as TBD pending direct on-chain enumeration of identified Foundation multisigs.*

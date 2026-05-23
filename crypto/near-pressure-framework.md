---
title: "NEAR Protocol (NEAR): Validator Inflation, Empty Buy Side"
description: "A MrNasdog Pressure Framework read of NEAR Protocol on Metric 1 (sell pressure) and Metric 2 (buy pressure): 2.5% annual inflation paid entirely to validators, against a structural buy ledger that's effectively zero. Numbers pulled origin-first from the NEAR mainnet RPC."
canonical_url: "https://mrnasdog.com/research/near/full"
tags: ["crypto", "near", "layer1", "defi"]
published: true
---

> Originally published at **[mrnasdog.com/research/near/full](https://mrnasdog.com/research/near/full)** by MrNasdog.

This is a **MrNasdog Pressure Framework** analysis of **NEAR Protocol (NEAR)** on Metric 1 (sell pressure) and Metric 2 (buy pressure). Narrative (Metric 3) is covered separately. The short version: NEAR mints 2.5% new supply every year to pay validators, against a buy ledger that is structurally empty.

## The setup

NEAR Protocol is a layer-1 proof-of-stake smart-contract platform that pays its validators by minting new NEAR. The protocol parameters, read directly from the mainnet RPC (`rpc.mainnet.near.org` → `EXPERIMENTAL_protocol_config`):

- **`max_inflation_rate: 1/40` = 2.5% per year** (the actual cap, not a temporary low; older third-party docs that cite "5%" are outdated)
- **`protocol_reward_rate: 0/1` = 0%** — the share of inflation routed to the protocol treasury was reduced to zero by governance. Today all inflation goes directly to validators, none to a treasury.
- Total supply: ~1,296.2M NEAR · circulating ~1,249.8M (~96.4%) · staked ~595.6M (~47.7% of total, ~409 active validators)
- Price ~$2.43 → market cap ~$3.16B (May 2026)

The "treasury share zeroed" detail matters for what comes next. Pre-2025-ish, 10% of NEAR's annual inflation flowed into a protocol treasury that funded grants and ecosystem ops — meaning there was a growing on-chain NEAR pool the foundation could theoretically have used for buybacks or burns. With that line zeroed, all dilution goes to validators, and there is no protocol-level NEAR accumulating anywhere to push back on supply.

## The sell ledger

*What the design predictably puts on the market.*

| # | Source | Tag | Value |
|---|---|---|---|
| 1 | Protocol inflation | **Tag A** | **~32.5M NEAR / yr** (~2.51% net, observed) |
| 2 | Vesting unlocks (still-locked allocations) | — | ~0 |
| 3 | Team / DAO / identified-group holdings | **Tag B** | NEAR Foundation lockups — TBD pending on-chain enumeration |
| 4 | Bankruptcy estate distributions | — | 0 |

The headline is **inflation**. Net observed supply growth across a 6-day window in May 2026 was ~89,000 NEAR/day, or **~32.5M NEAR/year**. That's what validators absorb in exchange for ~4.84% staking APY — and the portion they sell to cover operating costs is the protocol-level sell pressure.

The original 4-year vests on team, backers, and contributors started at mainnet launch in **July 2020** and finished by **mid-2024**. Today they contribute effectively nothing.

The Tag B watch is **NEAR Foundation lockup contracts**. The official protocol-treasury account (`treasury.near`) currently holds only ~89K NEAR — small, because the 10% treasury share of inflation was zeroed. But NEAR Foundation's *legacy operating reserves* (from the original allocation) remain large, sit in a network of lockup contracts, and are discretionary. Enumerating those balances on-chain is a project of its own; the article flags this as a known unknown rather than guessing a number.

There is no FTX-style bankruptcy estate distributing NEAR. Source #4 is zero.

## The buy ledger

*What the design predictably takes off the market.*

| # | Source | Value |
|---|---|---|
| 1 | Revenue-backed buyback | **0** — no structural buyback contract |
| 2 | Burn mechanism | **Tag A, ~426K NEAR / yr** (~0.03% of supply) |
| 3 | Locked allocations | — context only (~595.6M staked is functionally liquid) |
| 4 | Protocol-level demand (gas) | **Tag A, small** — ~14 TPS sustained, ~$2K/day in txn fees |

NEAR has no contract anywhere that buys NEAR with protocol revenue. The Nightshade gas-fee burn does destroy NEAR on every block — but at the chain's current on-chain volume (a few thousand dollars of daily transaction fees) it cancels only about **1.3% of inflation**. Trackable, predictable, real — and functionally negligible at today's activity level. The ~595.6M staked NEAR is context (the framework's existing rule treats short-unbond stakes as liquid, same as HYPE/BNB).

## Net position

Combine the ledgers and the structural picture is clean:

- **Sell, Tag A:** ~32.5M NEAR / year (inflation).
- **Buy, Tag A:** ~0.4M NEAR / year (gas burn).
- **Net structural dilution:** ~32M NEAR / year ≈ ~$78M / year at the current price.

This is the same shape as Ondo — scheduled supply up, structural buy ≈ 0 — but driven by smooth annual inflation rather than annual cliffs. The unfavorable verdict applies for the same reason: price has to come from discretionary demand growing faster than the structural supply tide, and the framework gives no credit for that.

## The only entry that could flip the buy ledger

The single mechanism that would move NEAR's buy ledger off zero is the same as for Ondo: a fee-switch-style change that routes some portion of fees (or restored treasury inflation) to a structural buyback. A reinstatement of `protocol_reward_rate` to a non-zero share, paired with a buyback policy on the accumulated treasury, would be the on-chain version. Until governance does that, NEAR's structural conditions on Metric 1 + Metric 2 are unfavorable.

## What to watch

1. **Any governance proposal restoring the protocol treasury share of inflation** (currently `protocol_reward_rate: 0/1`). This is the precondition for everything else.
2. **Any governance proposal introducing a structural buyback** (none today).
3. **NEAR Foundation lockup balances** — once enumerated, sets the Tag B size precisely.
4. **NEAR Chain Abstraction / Intents adoption** — drives on-chain gas burn higher. Today the burn is too small to matter; if activity scales 100× the offset becomes meaningful.

---

*MrNasdog Pressure Framework analysis of NEAR, Metrics 1 & 2. Data + explanation only. Not financial advice. Numbers as of May 2026.*

*Data note: inflation rate, treasury share, protocol parameters, supply numbers, and validator stats are origin-first from the NEAR mainnet RPC (`rpc.mainnet.near.org` → `EXPERIMENTAL_protocol_config` and `query`/`view_account`). Daily supply growth + gas burn computed from NearBlocks daily stats. NEAR Foundation lockup balance noted as TBD pending on-chain enumeration of the Foundation's lockup-contract network.*

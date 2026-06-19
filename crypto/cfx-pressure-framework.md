---
title:         "CFX Inflation Analysis · June 2026 · Net Inflationary (Mild, Cooling)"
description:   "Conflux PoW+PoS mints ~14.9M CFX/90D, fee + storage burn removes ~3.0M. Framework reads +0.23%, monitor +0.35% (gap 0.10pp). Uncapped Tree-Graph L1, reward halved Apr 2026."
canonical_url: "https://mrnasdog.com/research/cfx/inflation"
tags:          ["crypto", "cfx", "conflux", "layer1"]
published:     true
---

*Originally published at [mrnasdog.com/research/cfx/inflation](https://mrnasdog.com/research/cfx/inflation)*

Conflux mints roughly **14.9M new CFX** every 90 days from combined PoW and PoS issuance, while a continuous base-fee and storage-collateral burn removes about **3.0M CFX**. Framework reading: **+0.23% net** on an uncapped ~5.21B supply. The aggregator monitor reads **+0.35%** realised — a gap of **0.10 percentage points**, within tolerance, so no data-conflict chip. Conflux is a quietly inflationary chain whose issuance was just halved by governance.

## The verdict, in one paragraph

For the 90-day window beginning June 20 2026, the framework reads **Conflux at +0.23% net inflation**. New supply comes from two protocol sources — PoW mining and PoS staking — and is partly cancelled by two continuous burns. The aggregator monitor measured **+0.35%** over the trailing 90 days, but that realised window straddled the April 7 2026 reward cut, so it still carried some days at the old higher rate; the framework's forward read sits below it because the entire next window runs at the halved 0.4 CFX/block rate. The **0.10 percentage-point gap** is within the framework's 0.5pp tolerance, so no monitor-gap chip is raised. Conflux is best characterised as a **mildly inflationary uncapped Layer 1 whose new issuance is being actively throttled by DAO governance**.

## Sell pressure: where new CFX comes from

Conflux has two issuance sources, both sitting in Sell #1 of the framework's eight-row ledger. The first is the **PoW block subsidy** on the Tree-Graph Core Space: the **powBaseReward** parameter pays miners on every block. Conflux produces a block every 0.5 seconds — roughly 172,800 blocks a day — and the **Round 20** governance vote (concluded February 6 2026, live April 7 2026) cut the per-block reward from **0.8 to 0.4 CFX**, halving PoW issuance. At 0.4 CFX per block that is about **6.2M CFX** over 90 days. The second source is **PoS staking issuance**: validators earn a base interest rate of **3.26%** (left unchanged in Round 20), which adds roughly **8.7M CFX** over the window. Together, Sell #1 gross issuance is about **14.9M CFX per 90 days**.

Every other sell-side row is zero. Sell #2 (vesting unlocks) is zero — the genesis distribution across the team, private-equity funders, ecosystem fund, community fund and Foundation finished unlocking in 2024, and about **98.7%** of supply is now unlocked, with no scheduled cliff inside this window. Sell #3 (Foundation and unscheduled unlocks) is zero on the ledger: roughly **71M CFX** (1.3% of supply) remains locked but carries no published release schedule, and there is no observed in-window discretionary release. Sell #4 (bankruptcy estate) is zero; there is no estate.

## Buy pressure: where new CFX goes

The buy ledger is carried entirely by Buy #2, the **protocol fee burn**. Conflux burns CFX through two continuous mechanisms, both DAO-governed. The first is a **base-fee burn**: every transaction pays a base fee, part of which goes to miners and the remainder of which is permanently burned. The second is the **storage-collateral burn** introduced by CIP-107 — when storage collateral is sponsored, a portion is permanently converted to storage points, and Round 20 raised that **storage-point ratio from 63% to 78%**, deepening the burn. More than **496M CFX** has accumulated in the network's zero address since 2020. Over the window these burns remove roughly **3.0M CFX**.

The other buy rows are zero. Buy #1 (programmatic buyback) is zero — there is no protocol-revenue buyback; block rewards and the miner share of fees flow to miners, and staking rewards flow to stakers. Buy #3 (Foundation buy) is zero — the Conflux Foundation funds ecosystem grants and executed a one-time 76M-CFX burn in May 2025, but runs no ongoing market-buy programme. Buy #4 (new long-term lock) is zero inside this window; the Foundation's 500M-CFX stake was a May 2025 event already reflected in the current staked pool, not a fresh in-window lock.

## Foundation and overhang

The single tracked overhang is the residual locked supply: roughly **71M CFX** (about 1.3% of total) that has not yet entered circulation and carries no published release schedule. With the genesis vesting complete since 2024, this is a small overhang relative to the ~5.21B circulating float, and it has not been observed moving to market. The Conflux Foundation and Ecosystem Fund have, if anything, been net-deflationary over the past year — the May 2025 round burned 76M CFX from the Ecosystem Fund and staked 500M to lower the PoS yield. If this residual locked balance falls between refreshes, the outflow enters Sell #3 at the next refresh; until then it stays a tracked overhang at value zero.

## How CFX compares to other uncapped Layer-1 chains

Conflux sits among **uncapped, continuous-emission Layer 1s** — but with two features that set it apart. First, unlike a pure-PoW chain such as Ethereum Classic or Kaspa, Conflux is a **hybrid PoW + PoS** system, so new supply comes from both mining and staking; the PoS leg means the staked pool itself compounds issuance, similar to a delegated-PoS chain. Second, unlike most uncapped L1s, Conflux runs **two protocol burns** — a base-fee burn closer in spirit to Ethereum's EIP-1559, plus a storage-collateral burn unique to its sponsored-storage model. That burn side is what keeps net inflation near zero despite an uncapped design.

The other distinguishing feature is **DAO-tunable monetary policy**. Where a Bitcoin-style chain hard-codes its halving schedule and a typical PoS chain fixes its emission curve, Conflux lets on-chain governance adjust the PoW reward, the PoS interest rate and both burn ratios through the ParamsControl contract. The April 2026 halving of the PoW reward — and the simultaneous increase in the storage-point burn ratio — is a live example: the network is steering its own inflation downward by vote rather than by fixed schedule. That makes CFX more like an exchange-token model (where buybacks and burns are governance decisions) than a fixed-supply commodity chain.

## What to watch in the next 90 days

Three things bear watching. First, the next **chain-parameter governance round**: Conflux adjusts the PoW reward, PoS interest rate and burn ratios through recurring DAO votes, and any further reward cut or burn-ratio increase would push net inflation lower still. Second, **network activity**: both burns scale with on-chain usage — higher transaction volume burns more base fee, and more sponsored storage burns more collateral — so a usage spike would deepen the buy side. Third, any **Foundation transparency post** announcing a fresh burn or staking round in the style of the May 2025 action; the residual ~71M locked CFX and the Ecosystem Fund are the levers to watch.

## Summary

Conflux is an uncapped Tree-Graph PoW + PoS Layer 1 whose supply grows from combined mining and staking issuance and shrinks from a continuous base-fee and storage-collateral burn. For the next 90 days the framework reads **+0.23% net inflation** — about 14.9M CFX minted against 3.0M burned on a ~5.21B supply. The aggregator monitor reads **+0.35%** realised, a 0.10-point gap within tolerance, so the reading ships clean. The key structural fact is that Conflux's monetary policy is set by DAO vote: the April 2026 halving of the PoW reward shows governance actively cooling issuance, and the twin burns keep an uncapped chain hovering just above flat.

*MrNasdog Pressure Framework analysis of Conflux (CFX), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 20, 2026.*

---
title:         "ETH Inflation Analysis · September 2026 · Mixed flows, supply roughly steady"
description:   "Ethereum minted ~258.9K ETH to validators and burned only ~3.5K ETH over 90 days — a net +0.22%, as the EIP-1559 base-fee burn keeps fading."
canonical_url: "https://mrnasdog.com/research/eth/inflation"
tags:          ["crypto", "eth", "ethereum", "layer1"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/eth/inflation](https://mrnasdog.com/research/eth/inflation)*

# ETH Inflation Analysis · September 2026 · Mixed flows, supply roughly steady

Ethereum minted about **258.9K ETH** to validators over the last 90 days and destroyed only about **3.5K ETH** through the EIP-1559 base-fee burn — the burn now covers barely one and a third percent of what the protocol pays out. Add roughly **8.3K ETH** released from Ethereum Foundation wallets and the net is **+0.216%** of supply to market over 90 days, with **+0.219%** projected next. Ethereum has no hard cap and no buyback; the only brake on issuance is the burn, and the burn has been shrinking since rollup data moved to blobspace.

## The verdict, in one paragraph

Against a circulating supply of **122.02M ETH**, the Pressure Framework reads sell pressure of **267.2K ETH** and buy pressure of **3.5K ETH** over the trailing 90 days — a net of **+0.216%**. Projected forward on the live protocol run rate the next 90 days come out at **+0.219%**. The inflation monitor, which reads Ethereum supply from a market-capitalisation-over-price series rather than from the chain, prints **+1.17%** for the same window — a gap of **0.957 percentage points**, so a **⚠ monitor gap** chip ships on the overview. The deep walk resolved it: the chain added **255,426 ETH** between Jun 6 2026 and Sep 4 2026, while the end-check series stepped up **1.33M ETH** in a single day on Sep 3 2026 as its upstream supply figure re-based to match the chain. That step is an accounting catch-up, not issuance. Ethereum in September 2026 is a **quietly inflating settlement layer**: supply grows slowly, predictably, and entirely from staking rewards.

## Sell pressure: where new ETH comes from

Ethereum has exactly one mint. Consensus-layer validator issuance produced **258.9K ETH** over the window, about **2,877 a day**, and that is the entire Sell #1 row. The rate is not a fixed block reward: Ethereum pays the square root of the total staked balance, so issuance rises as more ETH is staked. The staked pool now holds **43.00M ETH**, roughly **35%** of supply, and it grew across the window — which is why the live 30-day run rate, **262.99K ETH** per 90 days, sits above the trailing average and is what the forward column uses. A **2.23M ETH** validator entry queue reported on Aug 17 2026, with a roughly 39-day activation wait, points the same direction.

Sell #2, vesting unlocks, is **zero** and permanently so. The 2014 crowdsale and both founding endowments were fully distributed by 2017; there is no vesting contract, no cliff, and no unlock tracker carries an entry for Ethereum. Sell #3 is **8.3K ETH**. Five Ethereum Foundation wallets were read on-chain at both ends of the window and fell from **37,676 ETH** to **29,412 ETH** — three 1,000-ETH tranches out of the main multisig, a single 4,938-ETH release from the ecosystem wallet in late Jun 2026, and a 3,750-ETH sale reported on Jul 19 2026. Coins that only moved between Foundation wallets cancel inside that cluster and are not counted as sell pressure. Sell #4 is **zero**: the largest bankruptcy estate settles ether claims in cash, and the in-kind distribution rounds concluded years ago, moving only coins that were already circulating.

## Buy pressure: where new ETH goes

There is one buy mechanism and it is small. The EIP-1559 base fee on every Ethereum transaction is destroyed outright — subtracted from the sender and credited to nobody, so total supply falls directly and no burn address is ever involved. That burn came to **3.5K ETH** over 90 days, about **39 a day**, or roughly **1.35%** of what validators were paid. The distinction that matters here is between the base fee and the fee: the priority fee sitting on top of it goes to the block proposer and is never burned, and neither are builder or MEV payments. Measured directly from transaction receipts across the window, only **22.44%** of Ethereum's execution-layer fees actually burn — the other **77.56%** is proposer income. Reading "fees" as "burn" would overstate this row roughly four and a half times.

Buy #1, a programmatic buyback, is **zero**: validator pay is minted rather than bought, and the protocol holds no treasury with which to buy. Buy #3, a Foundation buy, is **zero** — the Ethereum Foundation is a structural net seller funding research and grants, and has announced no accumulation programme. Buy #4, a new long-term lock, is also **zero**, and this was re-tested rather than assumed. Staking keeps growing, but it is not a lock in the framework's sense: there is no lockup contract with a stated size, no staking cap, stakers can exit at will, the position stays liquid through liquid-staking tokens, and staked ETH remains inside the circulating count. The growing stake is counted where it actually acts — on the mint side, in Sell #1.

## Foundation and overhang

The only identified team-controlled overhang on Ethereum is the Ethereum Foundation cluster: a main multisig, two disbursing safes, an operational wallet and an ecosystem wallet, holding **29,412 ETH** between them at the close of the window. That cluster is refreshed by direct chain read on every rebuild. The Foundation's published treasury policy targets annual operating expenses at about **15%** of holdings, declining toward a long-term 5% baseline, converted periodically into fiat with no published calendar — so releases are sporadic by design and the forward row carries the realised run rate rather than a projected tranche count. Nothing else qualifies. Exchange custodial wallets belong to depositors, venture holdings are dispersed across too many uncoordinated funds to read as a unit, and corporate ETH treasuries are third-party holders that bought on the open market and already sit inside the circulating count — the test is direction, not actor. If the Foundation cluster's balance falls between refreshes, that outflow enters Sell #3 at the next refresh.

## How ETH compares to other proof-of-stake Layer 1 chains

Ethereum sits between the two extremes of its class. Against a hard-capped proof-of-work chain, ETH has no ceiling at all — issuance is a live consensus parameter, it scales with the staked pool, and it can be changed by hard fork rather than by a fixed halving calendar. Against the high-emission proof-of-stake Layer 1s that mint several percent a year to bootstrap validators, ETH is austere: **+0.219%** projected over 90 days is under one percent annualised, an order of magnitude below the inflationary end of the category. The mechanism that makes the difference is the burn, and the mechanism that is failing is also the burn.

The comparison worth making is against exchange chains and application tokens that run structural buybacks. Those designs convert revenue into buy pressure directly, so their supply can shrink while activity holds. Ethereum converts only the base-fee slice, and that slice has collapsed. Total execution-layer fees on Ethereum ran about **$12.0M** over the last 30 days, of which roughly **$2.7M** burned. For scale, the largest single decentralised-exchange protocol family currently clears about **$95.4M** in 30-day fees and the leading chain by fee take about **$49.0M** — so Ethereum, with a **$308B** market capitalisation, is neither the fee leader nor close to it, and its fee-to-market-cap ratio of roughly **0.004%** per 30 days sits at the low end of the field. That is the honest structural reading: Ethereum captures settlement value in coin terms, not in fee terms, because the rollups it settles pay for blobspace rather than for Layer 1 gas.

## What to watch in the next 90 days

First, EIP-8361 and EIP-8363, the "Tapered Issuance Burn" drafts filed on **Aug 4 2026** by six researchers, which would burn a rising share of validator rewards until net consensus issuance reaches zero at about 50% staked. They are drafts with no activation height and no upgrade slot, so they change nothing today — a proposal is not a schedule — but activation would move Sell #1 more than any other single event. Second, the Glamsterdam upgrade, which has not activated on mainnet and carries no locked date; it changes block building rather than issuance, but a large capacity increase would pull base fees down further and shrink Buy #2. Third, the validator entry queue: **2.23M ETH** waiting on Aug 17 2026 means issuance rises mechanically as those validators activate. Fourth, the Ethereum Foundation cluster balance, currently **29,412 ETH**, which is read on every rebuild. Fifth, base fees themselves — they averaged **0.18 gwei** this window and fell across it; any sustained return of activity to Layer 1 would be the only mechanism that lifts the burn.

## Summary

Ethereum is a quietly inflating settlement layer. Validator issuance of **258.9K ETH** per 90 days is the chain's only mint, and the EIP-1559 base-fee burn of **3.5K ETH** offsets barely **1.35%** of it, leaving a net of **+0.216%** last window and **+0.219%** projected. The structural mechanism is that issuance scales with the staked pool while the burn scales with Layer 1 blockspace demand — and staking is growing while Layer 1 demand keeps migrating to rollups, so the two move apart rather than together. The key risk is that the burn is not merely small but shrinking, and that only **22%** of the fees Ethereum collects are burned at all. There is no cap and no ceiling: the only thing that would make ETH deflationary again is either a protocol change to issuance, still at draft stage, or a return of paid activity to the base layer.

---

*MrNasdog Pressure Framework analysis of ETH, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 4 2026.*

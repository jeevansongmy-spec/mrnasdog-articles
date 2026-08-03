---
title:         "GRT Inflation Analysis · August 2026 · Supply flat, projected to stay flat"
description:   "The Graph schedules 77.9M GRT of issuance per 90 days at 120.73 per block, yet measured on-chain supply did not grow. Framework reads 0.00% net; our monitor -0.082% (gap 0.082pp, no chip)."
canonical_url: "https://mrnasdog.com/research/grt/inflation"
tags:          ["crypto", "grt", "the-graph", "infrastructure"]
published:     true
---

*Originally published at [mrnasdog.com/research/grt/inflation](https://mrnasdog.com/research/grt/inflation)*

# GRT Inflation Analysis · August 2026 · Supply flat, projected to stay flat

The Graph is an uncapped work token that mints indexing rewards every block, so on paper it inflates about **3%** a year. Measured on-chain it does not. The rewards contract schedules roughly **77.9M GRT** of issuance over 90 days at **120.73 GRT** per Ethereum block, yet total supply across the Ethereum contract and the Arbitrum layer-2 did **not grow** over the window — the Ethereum side was flat and the layer-2 was slightly lower. Burns and reclaimed rewards for ineligible subgraphs offset the issuance, so the MrNasdog Pressure Framework reads **0.00% net** against our supply monitor at **-0.082%**, a gap of **0.082 percentage points** that stays inside tolerance, so no monitor-gap chip ships. GRT is best read as **an inflating token currently offset to flat**.

## The verdict, in one paragraph

For the 90-day window ending **Aug 3 2026**, the Pressure Framework reads **GRT at 0.00% net**. Gross sell pressure — the indexing-reward issuance — is about **77.9M GRT**, and the buy side offsets it with roughly **77.9M GRT** of burns and reclaimed rewards, against a circulating base of **10.80B GRT**. Our supply monitor reads **-0.082%**, a gap of just **0.082 percentage points**, so the framework and the monitor agree that GRT supply was essentially flat this window. The confirmation is on-chain and origin-first: The Graph's Ethereum **totalSupply** returned **10,800,262,816** at both ends of the window and has moved by only a few GRT in over a year, while the Arbitrum layer-2 supply — where all live issuance now mints — actually fell by about **4.95M**. The scheduled 120.73-per-block issuance is real, but it is not reaching net supply, which is why the honest reading is **a work token whose issuance is fully absorbed — flat, not growing**.

## Sell pressure: where new GRT comes from

Almost all of it is one row. Sell #1, protocol inflation, is **~77.9M GRT**: The Graph pays indexers with newly minted GRT, and the rewards contract on the Arbitrum layer-2 issues at a fixed **120.73 GRT** per Ethereum block. Over the roughly 645,000 blocks in 90 days that schedules about **77.9M GRT** of gross new issuance — genuine, continuous, and the largest single figure on the page. This is what makes GRT an inflating asset by design rather than a fixed-supply one.

The other three sell rows are empty, and their absence is the point. Sell #2, vesting unlocks, is **zero**: every tranche has finished — sale and early-backer tokens unlocked at 24 months, team allocations completed in December 2024, and the last multi-year lockups ran out by December 2025, so no cliff releases GRT in this window. Sell #3, foundation and unscheduled unlocks, is **zero**: on the supply figure the market reads, GRT is already about **99.99%** circulating, so the Foundation and ecosystem reserves are a small, static, monitored overhang rather than active sell pressure. Sell #4, long-term locked or bankruptcy, is **zero**: there is no estate, trustee distribution or court-ordered tranche anywhere in the picture. Issuance is the whole sell story.

## Buy pressure: where new GRT goes

The buy side is where the flat reading comes from. Buy #1, programmatic buyback, is **zero**: The Graph runs no revenue-funded program that purchases GRT on the open market. Buy #2, protocol fee burn, is **~77.9M GRT** — and it carries the whole reconciliation. The protocol burns a slice of activity directly: **1%** of query fees, a **1%** curation tax when curators signal on a subgraph, and a **0.5%** delegation tax when delegators stake to an indexer. On its own that burn is small, because query-fee revenue is modest. What makes the offset complete is the live rewards-eligibility upgrade: rewards for ineligible subgraphs are denied or reclaimed rather than paid out. The decisive evidence is the chain itself — reading total supply across both the Ethereum contract and the Arbitrum layer-2, supply did not grow over the 90 days, so the roughly 77.9M of scheduled issuance was effectively fully absorbed and net new supply reaching the market was about zero.

Buy #3, foundation buy, is **zero**: no Graph entity has disclosed an open-market GRT purchase program, and no accumulation wallet has been identified. Buy #4, new long-term lock, is **zero**: no new lockup or staking-vault contract removed GRT from the float this window — ordinary delegation and indexer self-stake are part of normal operation, not a fresh lock. So the ledger is a single large issuance row on one side and a single large offset row on the other, and they cancel.

## Foundation and overhang

There is one item to enumerate: The Graph Foundation and ecosystem reserves. On the Ethereum supply the market reads, total supply is **10,800,262,816 GRT** and circulating is **10,799,867,657 GRT** — a difference of only about **395K GRT**, so almost nothing is held off-market on that view. The reserves have no published near-term release schedule and showed no observed outflow across the trailing year, so they are tracked on a rolling review rather than a fixed calendar and their status is unscheduled. The trigger condition is simple: if the Foundation's balance falls between refreshes — that is, if reserve GRT starts moving onto the market — the outflow enters Sell #3 at the next refresh and the framework re-rates. As of this build nothing has moved, so it remains a monitored overhang and nothing more.

## How GRT compares to other uncapped work tokens

Structurally GRT belongs with the uncapped, continuous-emission networks rather than the fixed-supply tokens. Like Ethereum or Solana, it mints new units every block to pay the workers who secure the network — here indexers rather than validators — and there is no hard cap that ever stops issuance. That puts it in a different bucket from a token such as a fixed-supply ERC-20, where the supply question is settled forever; GRT's supply question is permanently open, and only the balance between issuance and burn decides which way it tips.

The closest mechanism comparison is to fee-burn chains. Ethereum offsets its issuance with a base-fee burn that scales with on-chain demand; when blockspace is busy, the burn can exceed issuance and ETH goes net deflationary, and when it is quiet, issuance wins. GRT works the same way but with query fees and taxes instead of gas: when query demand and curation activity are healthy the burns bite, and when usage slows the 120.73-per-block issuance dominates. The difference this window is that a second lever — reclaiming rewards for ineligible subgraphs under the eligibility upgrade — is doing much of the offsetting, which is why supply held flat even though raw query-fee burn alone would be far too small to cancel 77.9M of issuance.

It differs sharply from exchange tokens with scheduled buyback-and-burn, which shrink supply on a fixed corporate schedule regardless of network usage. GRT has no buyback; its deflationary force is entirely usage-driven and, right now, issuance-reclaim-driven. That makes GRT's reading more fragile than a burn-token's: the flat print depends on the offset holding. If query demand keeps sliding or the eligibility reclaim is dialed back, the same 77.9M issuance would show up as real net growth of roughly **0.7%** per 90 days — the ceiling reading — rather than the flat reading measured today.

## What to watch in the next 90 days

First, the layer-2 total supply: the single cleanest tell is whether the Arbitrum GRT supply starts rising, because that is where issuance mints and where the offset either holds or fails. Second, query-fee and burn trends: query volume fell about 8.9% quarter-on-quarter into Q4 2025, and a further slide would weaken the burn side and push the net reading up. Third, the rewards-eligibility and issuance-allocator settings: any governance change to how much issuance is reclaimed versus paid out would move the offset directly. Fourth, the Foundation reserve balance: any transfer out of it is the only unlock-style event that could add a second source of sell pressure. Fifth, any proposal to change the 120.73-per-block issuance rate itself, which would reset the entire sell side. None of these has a fixed calendar date; all are watch lines.

## Summary

The Graph (GRT) is an uncapped work token that mints indexing rewards continuously, so it is an inflating asset by design — yet over the 90-day window its measured on-chain supply did not grow. The rewards contract schedules about **77.9M GRT** of issuance at **120.73 GRT** per Ethereum block, but burns and reclaimed rewards under the live eligibility upgrade offset it, leaving the framework at **0.00% net** against a monitor reading of **-0.082%** — agreement that supply is flat, not the +0.7% the raw issuance ceiling would imply. The defining risk is one-directional and usage-dependent: the flat print holds only while the offset holds, so a sustained drop in query demand or a smaller reward reclaim would surface the full issuance as real net growth. With vesting finished and no buyback, issuance versus burn is the entire story, and today they cancel.

---

*MrNasdog Pressure Framework analysis of The Graph (GRT), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 3 2026.*

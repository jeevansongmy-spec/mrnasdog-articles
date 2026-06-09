---
title: "TAO Inflation Analysis · June 2026 · Net Zero to Market"
description: "Bittensor mints ~324K TAO per 90 days post-halving, but subnet auto-stake absorbs nearly all of it — the MrNasdog Pressure Framework reads ~0% net inflation on the active float against a 21M hard cap."
canonical_url: "https://mrnasdog.com/research/tao/inflation"
tags: ["crypto", "tao", "bittensor", "ai"]
published: true
---

> Originally published at **[mrnasdog.com/research/tao/inflation](https://mrnasdog.com/research/tao/inflation)** by MrNasdog.

Bittensor mints about 324,000 TAO every 90 days. Almost all of it ends the window bonded into subnet stake, not on an exchange. Framework reading: **~0% inflation on the active float**, against a 21M hard cap.

## The verdict, in one paragraph

For the 90-day window ending June 10, 2026, the framework reads **TAO at +0.00% net inflation** — sell-side flow of about 324,000 newly-minted TAO is structurally offset by an equivalent 324,000 absorbed into bonded subnet stake. The aggregator-side inflation monitor reads **−0.19%** (a small deflation), well inside the framework's 0.5-percentage-point tolerance, so no data-conflict flag is raised. The two readings agree. Bittensor in June 2026 is, in supply-pressure terms, a **quiet chain** — it mints aggressively and locks aggressively, and the net flow reaching the market is essentially nil.

## Sell pressure: where new TAO comes from

Bittensor has exactly one source of new supply: **block subsidies to subnet participants**. The first halving fired on **December 14, 2025**, cutting the per-day emission from 7,200 TAO to 3,600. At 3,600 TAO per day, the 90-day window mints **~324,000 TAO**. The annualised inflation rate sits at roughly **12.5%** of current circulating supply — high in absolute terms, but the rate compresses with every halving and with every additional TAO that enters circulation. The fixed **21-million** cap is the absorbing barrier.

The halving schedule is issuance-based, not time-based: the next halving fires automatically when cumulative issuance reaches **15,750,000 TAO**, roughly four and a half years out at the current rate. One wrinkle pushes that date later — subnet registration fees are **recycled back into the emission pool** rather than burned, which slows the march toward the next threshold. None of this changes the 90-day picture, but it explains why the rate decays gradually rather than on a fixed calendar.

The other three sell rows are empty. There is **no vesting schedule** — Bittensor was a fair launch in 2023, with no premine, no team allocation, and no investor cliff. There is no Foundation unlock programme and no bankruptcy estate. The only sell-side row that carries a real number on the TAO ledger is the post-halving emission itself.

## Buy pressure: where new TAO goes

Bittensor distributes block subsidies via the **dTAO subnet model**. The protocol mints a fixed **0.5 TAO per block** post-halving, divided across whichever of the network's 128-plus subnets receive emission that block. Within each subnet the split is roughly **41% to validators, 41% to miners, and 18% to subnet owners**. All three groups have strong economic reasons to re-stake their rewards: validators need bonded stake to keep their slot, miners need stake to register and stay competitive, and subnet owners need locked reserves to bootstrap their incentive curves. Selling TAO means selling future emission; holding and re-bonding it means compounding future emission.

The result is that most of the freshly-minted 3,600 TAO per day flows directly back into bonded stake within the same block cycle. The framework books this as a **Buy #4 — new long-term lock** at the same magnitude as Sell #1, producing a structural round-trip. The buyback row is empty (no protocol-revenue buyback exists on TAO), the fee-burn row is empty (Bittensor does not burn transaction fees at the protocol level — fees reward validators and miners instead), and there is no Foundation accumulation programme. The single non-trivial buy-side flow is the auto-stake absorption.

## Foundation and overhang

The Opentensor Foundation operates the protocol but does not control a transparently-tracked treasury. Whatever operational allocation exists is small relative to the chain's supply, and there is no documented schedule of discretionary deploys to market — so the framework leaves Sell #3, Foundation and unscheduled unlocks, at zero, with a standing watch line on any future on-chain Opentensor wallet activity.

The far larger pool to watch is the cumulative **subnet validator and miner stake**: more than **70% of supply** currently sits bonded, at the boundary between circulating and locked. That bonded stake is the real overhang on TAO — not a team wallet, but the staked float itself. If a large coordinated un-stake occurred, it would flush bonded TAO back into the active market and flip the framework reading from neutral to inflationary inside a single window. The trigger is explicit: **if the bonded-stake balance falls between refreshes, the outflow enters Sell #3 at the next refresh.**

## How TAO compares to other halving-model chains

The closest structural analogues are Bitcoin and Litecoin, both of which use a hard cap plus a halving schedule. The differences are practical. Bitcoin's emission rewards miners who provide hashpower, and the hashpower market is mature enough that most newly-minted BTC sells immediately to cover electricity costs — Bitcoin's framework reading is therefore inflationary at the protocol rate. Litecoin behaves similarly. TAO is structurally different: its block rewards pay validators and miners who provide a different kind of work (AI inference, retrieval, prediction), and those participants have strong economic reasons to bond rather than sell. Same supply discipline, very different demand-side absorption.

Against uncapped continuous-emission Layer-1s, the contrast is sharper still. Most general-purpose proof-of-stake chains inflate 4–8% forever with no terminal ceiling; TAO has both a decaying rate and a fixed 21-million terminus. And among AI-compute tokens specifically, TAO is unusual in having a cap at all — most AI-themed L1s and L2s use uncapped or extremely high-supply tokenomics with continuous emission.

The combination of **hard cap + halving + productive work** is rare; it is the single most-cited structural reason institutional accumulators give for taking the chain seriously. The supply discipline of a store-of-value asset is layered on top of a token that actually funds compute — a pairing almost no other network offers at once.

## What to watch in the next 90 days

Three things move the framework reading materially. First, any change to the dTAO emission split that reduces the validator or miner share — a smaller share weakens the auto-stake feedback loop and pushes more TAO toward the free float. Second, a large coordinated unstake from a major subnet, which would flush bonded TAO back into the active market. Third, any announcement from the Opentensor Foundation about a discretionary deploy from operational reserves. None of these is currently signalled, and the next halving is approximately four and a half years away. The single recurring watch item is the share of daily emission that ends the day still bonded versus sitting on a public exchange — as of mid-2026 that share is high enough that the framework reads neutral.

## Summary

TAO is a 21-million-cap, fair-launched, halving-model token operating on a productive-work network. Post-December-2025 halving, daily emission is 3,600 TAO — about 324,000 per 90 days. The dTAO subnet model absorbs nearly all of that into bonded stake, so the Pressure Framework reads the 90-day window as essentially neutral on market-facing supply, with the inflation monitor confirming at −0.19%. The structural risk is a governance change to the emission split that weakens the staking incentive; the structural ceiling is the 21-million cap.

---

*MrNasdog Pressure Framework analysis of Bittensor (TAO), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 10, 2026.*

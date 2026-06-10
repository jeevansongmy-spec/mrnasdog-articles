---
title: "Kaspa (KAS) Inflation Analysis: A Fair-Launch PoW BlockDAG Still in Its Emission Years"
description: "A MrNasdog Pressure Framework read of Kaspa (KAS): smooth chromatic emission mints ~692M KAS / 90D with zero offsetting flow. Framework reads +2.58%, aggregator agrees. Net inflationary by mining schedule."
canonical_url: "https://mrnasdog.com/research/kas/inflation"
tags: ["crypto", "kaspa", "pow", "blockdag"]
published: true
---

> Originally published at **[mrnasdog.com/research/kas/inflation](https://mrnasdog.com/research/kas/inflation)** by MrNasdog.

Kaspa mints roughly 692M new KAS every 90 days under its smooth chromatic emission schedule. Nothing offsets it — no fee burn, no buyback, no Foundation accumulation. Framework reading: **+2.58% net** on a 28.7B asymptotic cap. KAS is a fair-launch PoW chain still working through its first decade of supply.

## The verdict, in one paragraph

For the 90-day window ending June 10 2026, the framework reads **KAS at +2.58% net inflation** — purely mining emission, with no offsetting flow. The aggregator monitor reads **+2.58%** as well: the two agree exactly. There is nothing complicated about Kaspa's tokenomics. It launched fair, with no team allocation and no premine, and the chromatic emission curve has been running unchanged ever since. The supply growth is mechanical, predictable, and slowing month-by-month under the smooth monthly halving.

## Sell pressure: where new KAS comes from

Kaspa has exactly one source of supply: the **chromatic emission curve**, which pays mining rewards on every block. Today the per-second emission runs at roughly 27.5 KAS, distributed across roughly 10 blocks per second (about 2.75 KAS per block) since the Crescendo hardfork compressed block time to 100ms in May 2025. Crescendo divided the per-block reward by 10 while keeping the per-second curve identical — same emission, more blocks. Over 90 days, that comes to about **692M new KAS**, which sits in Sell #1 of the framework's 8-row ledger.

The emission rate decays smoothly: every calendar month the per-second rate multiplies by (1/2)^(1/12) ≈ 0.9439, so it halves every 12 months. The next monthly step falls early in the next window, lowering the per-block reward from 2.75 to ~2.60. This is why Kaspa's 90-day net inflation has been ticking down quarter after quarter, and will keep ticking down for the next ~25 years until the asymptotic cap of ~28.7B is effectively reached.

Every other sell-side row is zero. Sell #2 (vesting unlocks) is zero forever — there was no team allocation, no ICO, no investor cohort, no advisor pool. Bitcoin block hashes embedded in the genesis coinbase prove no hidden pre-mining occurred before launch. Sell #3 (Foundation discretion) is zero — the Kaspa Foundation is a donation-funded research entity with no protocol-level token allocation. Sell #4 (bankruptcy estate) is zero; there is no estate.

## Buy pressure: where the KAS goes

Buy pressure is also zero — the entire buy ledger is empty by design. There is no programmatic buyback (Buy #1), because there's no protocol revenue mechanism to fund one. Transaction fees on Kaspa flow to miners as part of the coinbase, not to a treasury or a burn address. There is no fee burn (Buy #2), no Foundation accumulation programme (Buy #3), and no new long-term lock mechanism (Buy #4), because Kaspa has no native staking system — it's pure PoW.

This is structurally identical to Bitcoin, Bitcoin Cash, Dogecoin, Monero, Zcash, and Ethereum Classic — pure PoW chains where new supply enters and nothing leaves. The framework reading for these chains tracks the protocol's emission schedule exactly, with no offsetting flows to model.

## Foundation and overhang

There is no Foundation overhang to worry about. The Kaspa Foundation exists as a stewardship and research entity, funded by donations and grants from the broader community. It holds no protocol-level allocation, runs no vesting cliffs, and operates no token treasury that could be deployed to market. The same structural shape applies to Dogecoin's and Monero's foundations — none of these chains carry a Foundation supply that could surprise the market with a discretionary sell.

## How KAS compares to other fair-launch PoW assets

Among fair-launch PoW assets, KAS sits in a distinct subgroup: its emission curve is steeper today than Bitcoin's, Litecoin's, or Bitcoin Cash's because Kaspa launched in late 2022 and is still in its high-emission years. Bitcoin is currently emitting at roughly 0.83% per year post-the-2024-halving; Kaspa is roughly 12 times that pace at ~2.58% per 90 days (~10.5%/yr equivalent). But Kaspa's emission halves every 12 months, whereas Bitcoin only halves every four years — so the gap closes quickly. By 2030, KAS's 90-day inflation will be inside Bitcoin's range.

Among newer PoW chains with smooth-emission curves, Kaspa is the only one operating at 10 blocks per second on a BlockDAG via the GHOSTDAG protocol. This is structural background — it doesn't change the inflation reading — but it means Kaspa achieves much higher throughput than a single-chain PoW system at the same emission pace.

## What to watch in the next 90 days

Three things bear watching. First, the **monthly chromatic halving** continues — the per-second emission steps down by ~6% every calendar month, so the 90-day inflation reading will continue to drop modestly each quarter. Second, the **Toccata hardfork** is scheduled for June 5 2026 to add native asset support and smart contracts. Importantly, Toccata does not modify the emission curve per the published KIP design, so the inflation reading should remain unaffected — but governance could amend that prior to activation. Third, watch for any **KIP proposal** that touches the chromatic emission table; none has done so since Crescendo (KIP-14, May 2025).

## Summary

KAS is a fair-launch PoW BlockDAG with no team allocation, no Foundation reserve, no buyback, no fee burn, and no discretionary supply. New supply enters mechanically on every block; nothing leaves. The framework reads +2.58% net for the trailing 90 days; the aggregator monitor agrees. The supply trajectory is slowing under smooth monthly halvings, and there is no overhang to surprise the market. KAS is one of the cleanest mechanically-inflationary cases in coverage.

---

*MrNasdog Pressure Framework analysis of Kaspa (KAS), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 10, 2026.*

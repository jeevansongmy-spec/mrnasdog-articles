---
title:         "ALGO Inflation Analysis · July 2026 · A capped chain that still feeds slowly from Foundation reserve"
description:   "Algorand mints no ALGO above its 10B cap, yet the Foundation releases ~36M ALGO/90d from reserve with no burn to offset it. Framework reads +0.40% (monitor +0.76%)."
canonical_url: "https://mrnasdog.com/research/algo/inflation"
tags:          ["crypto", "algo", "algorand", "layer1"]
published:     true
---

*Originally published at [mrnasdog.com/research/algo/inflation](https://mrnasdog.com/research/algo/inflation)*

Algorand is **hard-capped at 10B ALGO**, all minted at genesis, so there is no protocol mint — yet supply still grows because the Algorand Foundation releases reserve ALGO into circulation. Block-production staking rewards add about **20M ALGO** over the next 90 days and discretionary Foundation reserve deployment about **16M**, roughly **36M ALGO** in all, against **no buyback and no burn**. The framework reads ALGO at **+0.40%** net supply — a slow, one-sided inflation. Our supply monitor reads **+0.76%**, a gap of about **0.36 percentage points** that stays within tolerance, so no monitor-gap flag is raised.

## The verdict, in one paragraph

For the 90-day window beginning July 13 2026, the MrNasdog Pressure Framework reads **ALGO at about +0.40% net supply growth** — roughly **36M ALGO** released from Algorand Foundation reserve into circulation, with **nothing on the buy side** to offset it. Our supply monitor reads the realized last-90-day change at **+0.76%**, a gap of about **0.36 percentage points** that **does not raise a monitor-gap chip** because it sits inside the framework's half-point tolerance. The small gap is structural: the monitor's circulating-supply source counts Foundation reserve movement into circulation slightly faster than the Foundation's own transparency reports, which show circulating supply rising about **0.40% a quarter**. Both agree on direction. ALGO is best read as a **hard-capped chain that is still structurally inflationary on its float**, because a fixed cap is not the same as a fixed circulating supply.

## Sell pressure: where new ALGO comes from

Sell #1 — protocol inflation — is **zero**, and that is the fact to hold onto: Algorand mints **no new ALGO**. All 10B were created at genesis in 2019, and the protocol cannot issue above that cap. The **block-production staking reward** introduced with the Algorand 4.0 upgrade in January 2025 might look like protocol inflation, but it is not new issuance — the per-block **Foundation bonus** that pays validators (10 ALGO per block at launch, decaying about 1% every million blocks and funded until roughly early 2027) is paid out of the fee sink, which the Foundation **seeds from its own reserve**. Because it is pre-minted reserve rather than a mint, that flow is counted in Sell #3, not here.

Sell #3 — Foundation and unscheduled unlocks — is therefore the whole sell side, about **36M ALGO** over the next 90 days. It has two parts. The **staking rewards** release about **20M ALGO** — observed payouts of 6.89M in March 2026, 6.62M in April and 6.93M in May, near 6.8M a month, almost all genuine reserve release since fees run only about 50K ALGO a month. On top of that the Foundation deploys reserve for **ecosystem grants**, **xGov** community-voted funding — about **1.45M ALGO** to nine proposals in May 2026, and 384K to three grants in January — and operations, about **16M ALGO** more; the Foundation's own transparency figures show circulating supply rising about 0.40% a quarter, and staking accounts for roughly 20M of that. The remaining sell rows are **zero**: Sell #2 — vesting unlocks — is zero because all 10B ALGO were minted at genesis and the original team, early-backer and relay-runner allocations finished vesting by around 2024, leaving no contractual schedule. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate applies to ALGO.

## Buy pressure: where new ALGO goes

There is no buy pressure at all — every buy row is **zero**. Buy #1 — programmatic buyback — is zero: Algorand runs no token buyback and no protocol revenue is used to purchase ALGO. Buy #2 — protocol fee burn — is zero, and this is the structural point that makes ALGO one-sided: **Algorand does not burn fees**. Transaction fees, tiny at about 50K ALGO a month, are collected in the fee sink and **recycled to consensus participants** as part of the staking reward, so no ALGO is ever destroyed. Buy #3 — Foundation buy — is zero, because the Foundation is a net releaser of reserve, not an open-market buyer. Buy #4 — new long-term lock — is zero: about **2.11B ALGO** is staked to secure the network, but Algorand staking is **liquid** — no lockup and no slashing — so it creates no new multi-year lock. With reserve release on one side and nothing on the other, ALGO's supply can only drift up.

## Foundation and overhang

Because ALGO is fully minted, the overhang is not a vesting cliff — it is the **Algorand Foundation reserve** itself. About **1.04B ALGO**, the gap between the 8.96B circulating and the 10B cap, sits in non-circulating Foundation pools earmarked for community and staking incentives, ecosystem support, and the Foundation endowment. This reserve is what funds both the staking bonus and the discretionary grants, and the network's long-term plan is for it to release gradually toward full circulation by around 2030. It is monitored on the Foundation's roughly monthly transparency cadence. The reserve is the single lever that sets ALGO's inflation: if the Foundation's balance falls faster between refreshes — a larger grant round, an accelerated staking seed — that additional outflow enters Sell #3 at the next refresh.

## How ALGO compares to other capped Layer-1 tokens

ALGO sits in an unusual spot. Like **Bitcoin**, it has a **hard cap** — 10B ALGO that can never be exceeded — so it looks scarce on paper. But unlike Bitcoin, whose supply growth comes from newly mined coins on a fixed halving schedule, ALGO was **fully minted at genesis**, and its circulating growth comes from a Foundation reserve being paid out. A hard cap constrains the ceiling; it does not stop the float from rising while roughly 1.04B ALGO is still being released. In practice that makes ALGO's near-term inflation look more like an uncapped chain than like Bitcoin.

Against uncapped continuous-emission Layer-1s like **Cosmos Hub** (ATOM), whose staking inflation runs near 10% a year, or a delegated proof-of-stake chain that mints forever, ALGO is far gentler — about 0.40% a quarter, well under 2% a year, and structurally falling as the reserve depletes and the block bonus decays. The sharpest contrast is with a chain like **Polygon** or post-Merge **Ethereum**, where an **EIP-1559 base-fee burn** claws issuance back and can tip the token deflationary. ALGO has **no burn**, so its emission has no offset — the only thing that slows ALGO's inflation is the reserve running down and the bonus decaying, not usage. That is the key mechanism difference: ALGO is one-sided by design.

## What to watch in the next 90 days

Watch the **monthly Algo Insights transparency reports**, the cleanest read on how fast reserve is entering circulation — the staking-reward figure has held near 6.8M ALGO a month and any drift signals a change in the pace. Watch the **staking bonus decay**: the 10-ALGO-per-block bonus falls about 1% per million blocks and its Foundation funding runs to roughly **early 2027**, so the emission is set to shrink and eventually the question becomes what replaces it. Watch **xGov grant rounds**, which drive the discretionary Sell #3 flow and can spike in any given month. Watch for any governance move to add a **fee burn** — none exists today, and introducing one would be the single biggest change to this ledger. And watch total **ALGO staked**, near 2.11B, since a large shift would change how much reward flows into circulating hands.

## Summary

ALGO is a hard-capped, fully-minted proof-of-stake token whose supply still grows because the Algorand Foundation releases reserve into circulation — about 20M ALGO a quarter through block-production staking rewards and about 16M through discretionary grants and operations, for roughly 36M in all, a net of about +0.40%. There is no buyback and, critically, no fee burn: transaction fees are recycled to stakers, so nothing offsets the release and the token drifts slowly upward. Our supply monitor reads +0.76%, about 0.36 points higher, but that stays within tolerance and both measures agree ALGO is mildly inflationary on its float. The key point is structural: a 10B cap limits the ceiling, but with ~1.04B still in reserve and no burn, ALGO's circulating supply keeps rising until that reserve is spent.

---

*MrNasdog Pressure Framework analysis of Algorand (ALGO), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 13 2026.*

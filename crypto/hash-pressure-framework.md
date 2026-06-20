---
title:         "HASH Inflation Analysis · June 2026 · Supply Shrinking"
description:   "Deflationary: Provenance Blockchain staking emission is dormant while a fee-funded burn auction destroys ~1.57B HASH over 90 days. Framework reads −2.88% net."
canonical_url: "https://mrnasdog.com/research/hash/inflation"
tags:          ["crypto", "hash", "provenance", "rwa"]
published:     true
---

*Originally published at [mrnasdog.com/research/hash/inflation](https://mrnasdog.com/research/hash/inflation)*

# HASH Inflation Analysis · June 2026 · Supply Shrinking

Provenance Blockchain's staking emission is dormant while a fee-funded burn auction permanently destroys winning HASH bids. Over the trailing 90 days the burn removed roughly **1.57B HASH**, so the framework reads **−2.88% net** — deflationary. The aggregator monitor reads **−2.81%**, agreeing within **0.07 percentage points**.

## The verdict, in one paragraph

For the 90-day window ending June 20 2026, the MrNasdog Pressure Framework reads **HASH at −2.88% net inflation** — supply is contracting. The independent supply monitor reads **−2.81%**, a gap of just **0.07 percentage points**, well inside the 0.5-point tolerance, so no data-conflict chip is raised. The whole story is one mechanism out-running another: Provenance Blockchain's staking inflation is structurally dynamic but currently producing no net new HASH, while the HASH market burn — a fee-funded on-chain auction that burns every winning bid — keeps pulling supply out of circulation. The honest label is a **structurally deflationary RWA settlement chain**: the supply pressure is downward, driven by network fees rather than by a buyback or a fixed schedule.

## Sell pressure: where new HASH comes from

Sell #1 — protocol inflation — is the only sell row with a live mechanism, and it reads **zero** this window. Provenance Blockchain uses a dynamic, staking-linked inflation curve: the documented design pays as little as **1%** when 60% of supply is staked and as much as **52.5%** when nothing is staked. In practice the staking yield currently reads near **0%** per year, the chain's lineage was an explicit no-inflation model, and the 2026 tokenomics upgrade introduced network fees rather than net emission. No net new HASH was issued over the trailing 90 days, so the framework books emission at zero and watches the curve rather than projecting a number from it.

Sell #2 — vesting unlocks — is zero. There is no published per-cliff vesting calendar releasing HASH into the window. The large non-circulating balance sits with Figure and the Provenance Foundation as identified holdings, not on a dated public unlock schedule, so it belongs in the Foundation row rather than as a scheduled vesting cliff.

Sell #3 — Foundation and unscheduled unlocks — is zero by value but is the largest tracked overhang on the asset. Sell #4 — long-term locked or bankruptcy — is zero: there is no bankruptcy estate and no lockup releasing in the window. A planned supply-neutral **reverse-split to 1B total supply** is proportional and undated, so it adds no sell pressure — every holder's share is unchanged.

## Buy pressure: where new HASH goes

Buy #2 — protocol fee burn — carries the entire ledger and is the structural reason HASH is deflationary. The HASH market burn is a decentralized auction that receives **40% of network fees** and **100% of settlement fees**; participants bid HASH to win assets, and every winning HASH bid is **permanently burned**. This is a continuous, usage-linked destruction of supply: the more the chain settles, the more HASH leaves circulation. Over the trailing 90 days the observed supply fell by roughly **1.57B HASH**, and with emission dormant that contraction is attributable to the burn auction. Roughly **5B HASH** has already left the maximum supply over the chain's life — total supply now sits near **94.98B** against the **100B** genesis cap.

Buy #1 — programmatic buyback — is zero; there is no revenue-funded open-market buy of HASH, because value returns to holders through the burn rather than through a buy program. Buy #3 — Foundation buy — is zero; the Foundation accumulates HASH through the Figure transfer, not by buying on the open market. Buy #4 — new long-term lock — is zero; staking is liquid by design and no new lockup contract moved fresh supply into 90-plus-day locks in the window.

## Foundation and overhang

The dominant overhang is the team- and Foundation-controlled balance. At genesis the full **100B HASH** was minted and held almost entirely by Figure Technology Solutions. Under the community-approved update voted on **Jan 14 2026**, Figure is transferring **40% of its holdings** to the Provenance Foundation, lifting the Foundation's share to roughly **44%** of supply. Beyond that, the non-circulating remainder is large: total supply **94.98B** minus circulating **54.38B** leaves about **40.6B HASH** outside the float. None of this is on a dated public release schedule, so the framework values the row at zero and treats the balance as monitored overhang. If the Foundation or Figure balance falls between refreshes — an unscheduled distribution or treasury deployment — that outflow enters Sell #3 at the next refresh.

## How HASH compares to other fee-burn L1 chains

HASH's mechanism most resembles fee-burn Layer 1s rather than fixed-cap or pure continuous-emission chains. Like Ethereum's EIP-1559 base-fee burn or BNB's fee-driven destruction, HASH ties supply contraction directly to network usage — but Provenance routes the burn through an **auction** (winning bids burned) instead of a per-transaction base-fee sink, which makes the burn lumpier and settlement-driven. Unlike a halving-model chain with a hard, scheduled emission curve, HASH's issuance side is governed by a staking-target rule that can swing between 1% and 52.5%; today that side is quiet, so the burn dominates.

The contrast with continuous-emission Cosmos-SDK chains is the sharpest. Most Cosmos L1s run a positive net inflation to pay stakers, so their framework reading is supply growth. Provenance inverts that: emission is dormant, the burn is live, and the net is negative. The closest structural analogue is a fee-burn token whose deflation is real but **conditional** — it holds only while network fees (and therefore the auction burn) exceed whatever staking emission the curve later switches back on. That conditionality, not a fixed cap, is the thing to watch.

## What to watch in the next 90 days

First, the staking ratio: if staking participation falls further, the dynamic curve is designed to raise emission, which could flip Sell #1 from zero to a positive number and narrow or reverse the net deflation. Second, network-fee and settlement volume on Provenance — the burn is usage-linked, so a sustained drop in settlement activity shrinks the burn and softens the deflation. Third, execution of the Jan 2026 tokenomics upgrade (Prop 85): the new fee structure, the HASH Ecosystem Model, and the proposed new HASH token could each change how fees route into the burn. Fourth, any dated step toward the planned reverse-split to 1B total supply — proportional and supply-neutral, but worth confirming it stays that way. Fifth, any unscheduled Foundation or Figure treasury movement, which would promote Sell #3 from monitored overhang to a quantified flow.

## Summary

HASH is a structurally deflationary RWA settlement chain whose supply is currently shrinking. Staking emission is dynamic but dormant — yield reads near zero and no net new HASH was issued this window — while the HASH market burn destroys every winning auction bid funded by 40% of network fees and 100% of settlement fees. The framework reads **−2.88% net** over the trailing 90 days; the monitor agrees at **−2.81%**. The key risk is conditionality: the deflation holds only while fees and the burn out-run a staking curve that can switch emission back on, and a Foundation that controls roughly 44% of supply remains the largest monitored overhang. From a supply-pressure standpoint, HASH is one of the few Cosmos-SDK chains reading clearly negative.

---

*MrNasdog Pressure Framework analysis of Provenance Blockchain (HASH), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 20, 2026.*

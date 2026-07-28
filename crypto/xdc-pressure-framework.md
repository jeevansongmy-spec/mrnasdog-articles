---
title:         "XDC Inflation Analysis · July 2026 · Mixed flows, supply roughly steady"
description:   "XDC's 108 masternodes mint ~18.83M XDC/90d at 5.5 per block, with no buyback and a sub-cent fee burn. Framework reads +0.09% net (monitor +0.02%)."
canonical_url: "https://mrnasdog.com/research/xdc/inflation"
tags:          ["crypto", "xdc", "xdc-network", "layer1"]
published:     true
---

*Originally published at [mrnasdog.com/research/xdc/inflation](https://mrnasdog.com/research/xdc/inflation)*

XDC Network mints about **18.83M XDC** every 90 days as masternode block rewards, and almost nothing removes any of it. The MrNasdog Pressure Framework reads **+0.09% net** on a **19.95B** circulating base against no hard cap — the XDC block reward is the only real new-supply force, and the independent monitor agrees the chain is essentially flat at **+0.02%**.

## The verdict, in one paragraph

For the 90-day window ending **Jul 28 2026**, the framework reads **XDC at +0.09% net inflation** — masternode block-reward emission alone, with a buy ledger that is empty in practice. The independent monitor reads **+0.02%** over the same window, a gap of **0.08 percentage points**, well inside the half-point tolerance, so no monitor-gap flag is raised. XDC is a quiet, uncapped delegated-proof-of-stake chain: a small, steady mint on a very large float, structurally inflationary but only just.

## Sell pressure: where new XDC comes from

One source carries the whole reading. Sell #1, protocol inflation, booked **~18.83M XDC**. The XDC Network pays masternodes a fixed **5.5 XDC** per block, and this is newly minted supply rather than a payout from a reserve — the chain has no fixed cap, so every block reward grows total supply. The number here is measured on-chain, not assumed: over the window the chain moved from block 101,548,639 to block 105,437,663, which is **3,889,024** blocks in **8,833,735 seconds**, an actual block time of **2.27 seconds** rather than the 2-second nominal. At that real rate a 90-day window produces about 18.83M XDC, roughly 76M a year, a touch below the 86.7M a nominal 2-second block would imply.

Every other sell row is zero, and each for a concrete reason. Sell #2, vesting unlocks, is **0**: XDC investor and team allocations unlock once a year on a Feb 5 cliff, the **Feb 5 2026** lot of about 841M is already past, and the next cliff is **Feb 5 2027** — well outside this window. Sell #3, Foundation and unscheduled unlocks, is **0**: the large reserve exists but did not move in the window. Sell #4, long-term locked or bankruptcy, is **0**: XDC has no estate, no trustee and no court-ordered distribution.

## Buy pressure: where new XDC goes

The XDC buy ledger is empty in every line that matters. Buy #1, programmatic buyback, is **0**: neither the protocol nor the foundation runs a contract that repurchases XDC. Buy #2, protocol fee burn, is **0** in effect: XDC actually carries two burns — an EIP-1559 base-fee burn added in the January 2026 Cancun upgrade, and a long-standing 20% burn on smart-contract fees — but XDC fees are a fraction of a cent, so the amount destroyed across 90 days is well under 0.5M XDC. The proof is in the supply itself: total supply has grown at essentially the gross mint rate over the last five years, which means burns are barely registering. Buy #3, Foundation buy, is **0**, with no announced accumulation programme. Buy #4, new long-term lock, is **0**: the masternode set held at 108 validators, so no new collateral was locked, and masternode stake can be withdrawn anyway.

## Foundation and overhang

The team-controlled overhang on XDC is large but dormant. About **18.1B XDC** — the gap between the 38.07B total supply and the 19.95B circulating — sits outside the float in Founder and team reserves (~29% of the genesis mint), Ecosystem Development (~26%) and Contingency (~9%) allocations. That reserve is the single biggest structural fact about XDC supply, and it releases only on the annual Feb 5 cliff, so nothing from it lands inside this window. A second, smaller identified block is the masternode collateral: 108 masternodes each lock **10M XDC**, about **1.08B XDC** in total, static across the window. Both are booked at zero and watched. The trigger line is the standard one: if either the reserve or the collateral balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How XDC compares to other uncapped proof-of-stake chains

Among uncapped continuous-emission layer-1s, XDC sits at the low-inflation end. Its block reward is a fixed 5.5 XDC rather than a percentage of stake, so as the float grows the emission rate falls in relative terms — roughly 0.09% of circulating supply per 90 days, or under 0.4% a year. That is far below the 4–8% annual issuance typical of large delegated-proof-of-stake chains that pay stakers a percentage yield, and it is why XDC reads almost flat despite having no hard cap at all. The mechanism matters more than the label: a fixed per-block subsidy on a multi-billion float behaves much like a capped chain deep into its emission curve.

The contrast with fee-burn chains is the interesting one. XDC has the same EIP-1559 base-fee burn that can turn a busy Ethereum-style chain net deflationary, but XDC's fees are far too small for the burn to bite — so unlike a high-throughput burn chain, XDC cannot presently offset its own mint. Against capped proof-of-work coins, XDC gives up the hard ceiling but keeps a comparably slow real issuance rate; the difference is that XDC's emission could, in principle, be changed by governance, whereas a coded halving cannot. And against exchange tokens with quarterly buybacks, XDC has no buy-side mechanism at all: its near-flat reading comes entirely from a small mint, not from anything actively removing supply.

## What to watch in the next 90 days

Little is scheduled, which is the point. The next vesting cliff is **Feb 5 2027** — a large annual unlock, but a full quarter beyond this window, so it does not touch the current reading. On-chain block timing is the one live variable: the chain runs at about 2.27 seconds rather than 2, and any drift in that rate moves the emission figure directly, so it is re-measured each rebuild. The fee burns are worth a periodic check — if XDC transaction activity or fees rose sharply, the EIP-1559 and smart-contract burns could finally start to register on the buy side. Beyond those, the only structural watch line is a governance proposal touching the masternode reward or the emission schedule, and no such proposal is live today.

## Summary

XDC is an uncapped delegated-proof-of-stake chain emitting **~18.83M XDC per 90 days** from a fixed 5.5 XDC masternode block reward, with a buy ledger that is empty in practice and a reserve overhang that stays dormant between annual cliffs. The framework reads **+0.09% net** and the independent monitor agrees at **+0.02%**, a 0.08-point gap. The supply path is simple and slow: a small mint on a 19.95B float, no hard cap but no aggressive issuance either, and burns too small to offset it. The key risk is not the schedule but the size of the non-circulating reserve — roughly 18.1B XDC that releases each Feb 5 — while the near-term reading stays mildly inflationary and steady.

*MrNasdog Pressure Framework analysis of XDC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 28, 2026.*

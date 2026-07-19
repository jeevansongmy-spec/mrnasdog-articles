---
title: "XRP Inflation Analysis · July 2026 · Nothing is minted, but escrow still drips"
description: "XRP has zero protocol inflation: all 100B minted at genesis. Escrow releases 1B XRP monthly, ~2.10B of 3.00B re-locked. Framework +1.44% net, monitor +1.39%."
canonical_url: "https://mrnasdog.com/research/xrp/inflation"
tags: ["crypto", "xrp", "ripple", "payments"]
published: true
---

*Originally published at [https://mrnasdog.com/research/xrp/inflation](https://mrnasdog.com/research/xrp/inflation)*

# XRP Inflation Analysis · July 2026 · Nothing is minted, but escrow still drips

XRP has no protocol inflation at all — every one of the **100B XRP** was created in the XRP Ledger's first ledger in 2012, and the network has no way to issue more. The supply pressure comes from Ripple's escrow instead: **1.00B XRP** unlocks on the first of each month, so **3.00B** came out across this window, of which about **2.10B** was re-escrowed within days. The MrNasdog Pressure Framework reads **+1.44%** net against our supply monitor at **+1.39%** — a gap of **0.05 percentage points**, comfortably inside tolerance, so no data-conflict flag ships.

## The verdict, in one paragraph

For the 90-day window ending **Jul 19 2026**, the Pressure Framework reads **XRP at +1.44% net**. Gross sell pressure is **3.00B XRP** — three monthly escrow unlocks of a billion each — and gross buy pressure is **2.10B XRP** of re-escrow plus **37.1K XRP** of transaction-fee burn, leaving roughly **900M XRP** as the real release to market. Our supply monitor, which tracks the realized change in circulating XRP, reads **+1.39%** over the same window — about **858M XRP** of float growth. The gap is **0.05 percentage points**, far under the framework's half-point tolerance, so the on-chain derivation and the realized measurement agree almost exactly and no flag is needed. XRP is best described as **structurally non-inflationary but schedule-inflationary on the active float**: the total can never grow, yet the escrow release keeps expanding the tradable share of a fixed pie.

## Sell pressure: where new XRP comes from

Sell #1 — protocol inflation — is **zero**, and it is zero for a reason no governance vote can undo. The XRP Ledger has no minting operation in its transaction set. The entire 100B XRP supply was created in a single genesis ledger in 2012, and every read of the ledger's total-supply field since has been lower than the one before it. Two direct on-chain reads bracket this window: **99,985,672,961 XRP** at the start and **99,985,635,850 XRP** at the end. Supply fell. There is no emission curve, no block reward, no staking issuance, and no inflation parameter to tune — XRP is the rare asset where the protocol-inflation row is structurally, permanently empty.

Sell #2 — vesting unlocks — carries the entire sell side at **3.00B XRP**, and it is Ripple's escrow. Under contracts written in December 2017, exactly **1.00B XRP** is released from a dated escrow on the first of every month. Three of those firings fall inside this window — **May 1 2026**, **Jun 1 2026** and **Jul 1 2026** — which is why the row is the full three billion rather than a trailing average. The July tranche moved in three pieces, **200M**, then **300M**, then **500M**. Crucially, this is the gross number: the escrow unlock is a mechanical ledger event, not a decision to sell, and the offsetting re-escrow is tracked on the buy side rather than netted quietly inside this row.

Sell #3 — Foundation and unscheduled unlocks — is **zero** as a flow. Ripple did not make any unscheduled release inside the window; every billion that moved, moved on the published monthly schedule. Sell #4 — long-term locked or bankruptcy — is also **zero**: no bankruptcy estate, trustee schedule or court-ordered distribution applies to XRP, and the escrow contracts, the only long-dated lock on the asset, are already accounted for in Sell #2.

## Buy pressure: where new XRP goes

Buy #4 — new long-term lock — is the dominant offset at **2.10B XRP**. This is the re-escrow leg. Ripple does not keep the billion it unlocks; within hours or days it writes most of it back into fresh dated escrow contracts, typically returning 60% to 80% of each tranche. Reading the escrow contracts directly at both ends of the window shows the balance falling from **33.20B XRP** to **32.30B XRP** — a decline of exactly **900M XRP** against **3.00B** unlocked, which pins the re-escrow at 2.10B. That is the single most important number on this page, because it converts a headline that reads "a billion a month" into a real release of roughly **300M XRP** a month.

Buy #2 — protocol fee burn — is **37.1K XRP**, small but genuinely deflationary. Every XRP Ledger transaction destroys its fee outright rather than paying it to a validator, at a base of 0.00001 XRP per transaction. Across this window that burned about **412 XRP a day**. The burn was designed to make transaction spam expensive, not to shrink supply. Buy #1 — programmatic buyback — is **zero**: the XRP Ledger has no buyback mechanism, and Ripple's **$750M** repurchase announced in **Mar 2026** buys its own equity at a roughly $50B valuation, not XRP. Buy #3 — Foundation buy — is **zero** as well: Ripple is a structural seller of XRP, not an accumulator, and while a listed treasury vehicle is buying XRP on the open market, open-market buying transfers coins between holders without removing anything from the tradable float.

## Foundation and overhang

Two team-controlled overhangs sit behind XRP, and together they are the largest in the framework by absolute size. The first is the escrow itself: **32.30B XRP** remains locked in dated contracts held by identified issuer accounts, refreshed by direct ledger read each rebuild. At the observed net drain of about 300M a month, that pool runs roughly nine more years. The second is Ripple's unescrowed treasury: **3.62B XRP** sitting in identified issuer wallets outside escrow, up only **52.4M** across the whole window — meaning nearly all of the 900M released passed through and out to the market rather than accumulating.

A third item is watched but not counted. Evernorth Holdings, an XRP treasury company pursuing a Nasdaq listing through a SPAC merger, held **473.3M XRP** and filed an amended registration statement on **Jul 13 2026**; the merger had not closed inside this window. Ripple has agreed to contribute roughly **127M XRP** to it on closing, which would move XRP that already circulates and so would not change the ledger. If any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How XRP compares to other fixed-supply chains

XRP belongs to a small class: assets with a hard cap that was fully issued at genesis rather than mined out over decades. Bitcoin and Litecoin also have hard caps, but they reach them through a halving-model block subsidy, so their protocol-inflation row is non-zero and shrinks on a schedule. XRP's protocol-inflation row is zero from day one and will stay zero forever — no halving is coming because there is nothing to halve. Against an uncapped continuous-emission chain, where new coins are minted every block to pay stakers, XRP is structurally the more conservative asset: an uncapped chain's supply grows without limit, while XRP's can only shrink.

The honest comparison, though, is not to proof-of-work coins but to tokens with a large scheduled unlock overhang. XRP's escrow behaves like a vesting cliff that fires monthly and never fully completes, which is why its framework reading looks closer to a young token still working through its unlock calendar than to a mature fixed-supply chain. Where it differs is the discretion built into the mechanism: a normal vesting contract releases into circulation and cannot take it back, but the escrow's re-lock step means the issuer chooses each month how much of the billion actually reaches the market. That discretion is the framework's main sensitivity here. Compared with a chain that runs a base-fee burn, XRP's burn is negligible — an EIP-1559-style burn can offset a meaningful share of issuance, while XRP's spam-prevention fee removes about 0.00006% of supply per quarter.

## What to watch in the next 90 days

First, the monthly escrow unlocks on **Aug 1 2026**, **Sep 1 2026** and **Oct 1 2026** — each releasing **1.00B XRP** gross, with the re-escrow ratio determining whether the net stays near 300M. Second, any change in that re-escrow ratio: a month where Ripple locks back materially less than 70% would raise the framework reading immediately, and is the single most likely source of a surprise. Third, the closing of the Evernorth SPAC merger and the roughly **127M XRP** issuer contribution attached to it. Fourth, the fixCleanup3_2_0 amendment activating on **Jul 29 2026**, which carries no issuance, fee or escrow effect but should be re-read on activation to confirm that holds. Fifth, the transaction-fee burn rate, which rises with XRP Ledger throughput and would need to grow by three orders of magnitude before it mattered to this ledger.

## Summary

The MrNasdog Pressure Framework reads XRP at **+1.44%** net over 90 days, against a supply monitor reading of **+1.39%** — a **0.05 percentage point** gap that requires no flag. The structural mechanism is unusual: XRP has zero protocol inflation because all 100B were created at genesis and the XRP Ledger cannot mint, so every unit of pressure comes from Ripple's monthly escrow release of **1.00B XRP**, of which about **2.10B** of each **3.00B** quarterly gross is re-escrowed, leaving roughly **900M XRP** reaching the market. The key risk is discretionary rather than mechanical — Ripple chooses the re-escrow ratio each month, and a smaller re-lock would raise the reading without any protocol change. The ceiling is absolute: **100B XRP** can never be exceeded, **32.30B** of it remains escrowed on a roughly nine-year drain, and the fee burn means the true total will only ever fall.

---

*MrNasdog Pressure Framework analysis of XRP, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 19 2026.*

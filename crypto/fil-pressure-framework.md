---
title: "FIL Inflation Analysis · June 2026 · Minting and vesting still ahead of the burn"
description: "A MrNasdog Pressure Framework read of Filecoin (FIL): ~33M / 90D block-reward minting plus ~15M vesting vs a ~20M base-fee burn. Framework +3.5% net; monitor +3.68%."
canonical_url: "https://mrnasdog.com/research/fil/inflation"
tags: ["crypto", "fil", "filecoin", "storage"]
published: true
---

> Originally published at **[mrnasdog.com/research/fil/inflation](https://mrnasdog.com/research/fil/inflation)** by MrNasdog.

Filecoin mints about **33M FIL** in block rewards and vests roughly **15M** more to early backers over 90 days, while a base-fee burn removes about **20M**. New supply stays well ahead of the burn, so the Pressure Framework reads about **+3.5% net**. Our supply monitor reads **+3.68%** realized — the two agree to within a fifth of a percentage point, so no monitor-gap chip is needed.

## The verdict, in one paragraph

For the 90-day window ending June 16 2026, the MrNasdog Pressure Framework reads **FIL at +3.5% net** on the last-90-day view and about **+3.3% net** on the forward view, driven by block-reward minting and 6-year vesting that together out-issue the base-fee burn. Our supply monitor reads the realized last-90-day change at **+3.68%**, versus the framework's **+3.54%** read for the same window — a gap of about **0.14 percentage points**, comfortably inside tolerance, so **no monitor-gap chip ships**. Filecoin is **structurally inflationary** at a mid-single-digit annual pace, with the burn slowing dilution rather than reversing it.

## Sell pressure: where new FIL comes from

Sell #1 — protocol inflation — is the largest source, at about **33M FIL** over the next 90 days. Filecoin is a storage-mining chain: new FIL is minted to storage providers as block rewards on a published schedule that combines simple minting — a fixed pool released on a six-year half-life — with baseline minting, which only releases its larger pool as the network's storage power tracks a rising baseline. Gross block reward currently runs near 130M FIL a year and declines over time, so this row is large but slowly shrinking.

Sell #2 — vesting unlocks — adds about **15M FIL** over 90 days. SAFT investors, Protocol Labs, the team and the Foundation all vest linearly over six years from the October 2020 network launch. The bulk of those six-year cohorts finishes vesting around **October 2026**, so this stream is real today but tapering — it falls to roughly **14M** on the forward view and largely ends just after this window. Sell #3 — Foundation and unscheduled unlocks — is **zero** as a flow: the Mining Reserve, a governance-controlled pool of more than 300M FIL, has no published release schedule and did not move in the window. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate or court distribution applies to FIL.

## Buy pressure: where new FIL goes

Buy #2 — protocol fee burn — is the only active offset, at about **20M FIL** over 90 days. Every network base fee is burned to an unrecoverable address in an EIP-1559 style, alongside penalty burns for storage and consensus faults; the FIP-0100 upgrade in April 2025 added a per-sector daily fee that is also burned, scaling the burn with network activity. Because the destination is a burn, those coins are gone for good. Buy #1 — programmatic buyback — is **zero**: Filecoin has no buyback mechanism. Buy #3 — Foundation buy — is zero, and Buy #4 — new long-term lock — is zero, because the FIL that storage providers post as collateral is structural day-to-day pledging, not a newly announced multi-year lock.

## Foundation and overhang

The overhang to watch is the **Mining Reserve** — a pool of more than 300M FIL set aside at genesis with no fixed release schedule, governed by the community. It is not a stockpile on a vesting calendar; any release would require a governance decision, and none is pending, so the framework books it at zero. Beyond that, the still-vesting six-year cohorts — Protocol Labs' 300M FIL, the team and the Foundation — are the predictable overhang, and they are nearly exhausted as October 2026 approaches. The framework re-checks block emission, the burn and the vesting schedule on a roughly bi-weekly walk; if the Mining Reserve balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How FIL compares to other uncapped storage and infrastructure chains

FIL belongs to the class of **uncapped, work-based infrastructure tokens** that mint a block reward to the providers who supply the network's resource — here, storage capacity rather than hashpower. Unlike a hard-capped, halving-model coin, Filecoin has no fixed ceiling; its block reward decays gradually on a half-life and a baseline curve rather than stepping down at discrete halvings. And unlike a pure inflation chain, it pairs the mint with a real base-fee burn, so net inflation is the difference between a large, slowly-declining mint and a burn that scales with usage.

The contrast worth drawing is with exchange tokens that buy back and burn aggressively enough to go net-deflationary. Filecoin has no buyback at all, and its burn — while genuine and growing under FIP-0100 — is still well below the combined block-reward and vesting issuance. That keeps FIL clearly on the inflationary side of the ledger for now. The structural turn to watch is October 2026: once the six-year vesting ends, vesting drops out of the sell side, and FIL's net inflation depends only on the gap between the declining block reward and the rising fee burn.

## What to watch in the next 90 days

Watch the block-reward rate, which declines gradually and is the single largest input to net inflation. Watch the base-fee burn, since FIP-0100's per-sector fee makes the burn scale with storage activity — a busier network burns more FIL and lowers the net. Watch the vesting taper into the **October 2026** completion of the six-year cohorts, which removes a steady source of new supply just after this window. And watch the Mining Reserve for any governance proposal to release or burn it, which would move Sell #3 off zero.

## Summary

FIL is an uncapped, work-based storage token whose supply grows from block-reward minting plus the tail of a six-year vesting schedule. Filecoin mints about 33M FIL in block rewards and vests roughly 15M more over 90 days, while a base-fee burn removes about 20M, leaving the framework at about +3.5% net. Our supply monitor reads +3.68% realized, agreeing to within 0.14 percentage points, so no monitor-gap chip is needed. FIL stays mid-single-digit inflationary, with the burn slowing dilution rather than reversing it — and the October 2026 end of vesting the key step toward a lower net rate.

*MrNasdog Pressure Framework analysis of Filecoin (FIL), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 16, 2026.*

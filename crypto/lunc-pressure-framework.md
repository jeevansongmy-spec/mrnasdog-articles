---
title:         "LUNC Inflation Analysis · July 2026 · Staking mint still ahead of the burn"
description:   "Terra Classic issues ~95B LUNC/90d as staking rewards vs a ~12B burn tax + exchange burns. Framework reads +1.5% net, in line with our monitor (+1.31%)."
canonical_url: "https://mrnasdog.com/research/lunc/inflation"
tags:          ["crypto", "lunc", "terra-classic", "staking"]
published:     true
---

*Originally published at [mrnasdog.com/research/lunc/inflation](https://mrnasdog.com/research/lunc/inflation)*

Terra Classic mints about **95B LUNC** over 90 days as staking rewards, while a **0.5%** on-chain burn tax and voluntary exchange burns remove roughly **12B**. New supply stays ahead of the burn, so the framework reads about **+1.5%** net. Our supply monitor reads **+1.31%** — the two agree, so no monitor-gap flag is raised.

## The verdict, in one paragraph

For the 90-day window ending July 5 2026, the MrNasdog Pressure Framework reads **LUNC at +1.5% net** on the forward view, driven by a staking-reward mint that out-issues the network's burns. Our supply monitor reads the realized last-90-day change at **+1.31%**, versus the framework's **+1.5%** read for the same window — a gap of about **0.19 percentage points**, comfortably inside tolerance, so **no monitor-gap chip** is shipped. The picture is clean: Terra Classic is uncapped and mints new LUNC every block for validators and delegators, and although the chain burns aggressively by reputation, the mint is simply the larger number today. LUNC is **structurally inflationary on the active float**, at a low-single-digit pace.

## Sell pressure: where new LUNC comes from

Sell #1 — protocol inflation — is the whole story, at about **95B LUNC** over the next 90 days. Terra Classic runs a Cosmos-SDK mint module that issues new LUNC every block at roughly **7%** a year, paid to validators and the delegators who stake with them. On a circulating base near **5.53 trillion LUNC**, that nominal rate works out to about 95B minted per quarter — a large absolute figure precisely because the supply itself is enormous. This is the single dominant force on LUNC supply, and it is why the coin still inflates despite a well-publicized burn programme.

The other three sell rows are **zero**. Sell #2 — vesting unlocks — is zero because Terra Classic has no active team, seed or investor vesting schedule; the original allocations were distributed years before the May 2022 collapse, so there is no cliff waiting to hit the market. Sell #3 — Foundation and unscheduled unlocks — is zero because the chain is fully community-governed with no central team or foundation treasury paying coins out to the market. Sell #4 — long-term locked or bankruptcy — is zero as a flow: the bankruptcy estate tied to the original Terra collapse does not release new LUNC into the open-market float inside this window.

## Buy pressure: where new LUNC goes

Buy #1 — programmatic buyback — is **zero**: there is no protocol-run treasury spending revenue to buy LUNC on the open market. The network removes supply only by burning. Buy #2 — protocol fee burn — is the built-in sink, at about **5.5B LUNC** over 90 days. An on-chain burn tax, live since 2023 and currently set at **0.5%**, destroys a slice of every transaction; at recent activity that runs on the order of 60 to 130 million LUNC a day, so roughly 5.5B over the quarter, gone for good. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero, with no discretionary open-market buying and no new escrow announced in the window.

Beyond the canonical four, LUNC carries one coin-specific offset — Buy #5, exchange-led burns — at about **6.5B LUNC** over 90 days. Major exchanges voluntarily burn the LUNC they collect in trading fees; a leading exchange burned roughly **2.2B** in June 2026 alone, and across the three monthly burns in the window that adds up to about 6.5B destroyed. Together the fee burn and exchange burns remove about **12B LUNC** — real and permanent, but still smaller than the ~95B mint.

## Foundation and overhang

LUNC has no classic unlock overhang and no foundation stockpile in the usual sense — there is no company, no team wallet on a vesting cliff, and no treasury drip. What functions as the "overhang" here is the continuous staking mint itself: new LUNC that accrues to validators and delegators every block and is largely claimed, re-staked or sold at the holder's discretion. Because that mint is embedded in the protocol and set by community governance rather than by a schedule, the framework books it as the ongoing Sell #1 rather than as a discrete release. The one thing to track is governance: if a proposal cuts the mint rate or raises the burn tax, the balance between the two shifts, and that change enters the ledger at the next refresh.

## How LUNC compares to other uncapped proof-of-stake chains

LUNC belongs to the class of **uncapped proof-of-stake L1s that mint continuously for stakers** — structurally closer to a Cosmos staking chain than to a hard-capped, halving-model coin. Unlike a fixed-supply token, LUNC has no ceiling; new coins are created every block. What sets it apart from a plain inflation chain is the pairing with an on-chain burn tax and exchange burns, which claw some of that issuance back. The result is a two-sided supply model where the mint and the burn pull in opposite directions, and the net sign depends entirely on which is larger at the moment.

Today the mint wins, so LUNC reads as mildly inflationary — but the comparison worth drawing is with chains where the burn has grown big enough to flip the sign. A fee-burning smart-contract chain can go net-deflationary when usage is high; LUNC cannot yet, because its ~12B of quarterly burns is a fraction of its ~95B mint. For an inflation lens specifically, that means LUNC behaves like a high-issuance staking chain with a partial brake: the mint is the dominant force, and the burns slow dilution rather than reversing it.

## What to watch in the next 90 days

Watch the monthly exchange burns — the ~2.2B pace of the largest exchange's burn, landing near the first of each month (next up around **Aug 1 2026**), is the single most visible number on the buy side. Watch the on-chain burn-tax throughput, since it scales with transaction activity, so a busier chain burns more. Watch governance most of all: any proposal to change the mint rate or the burn-tax parameter would move the net directly, and a re-activated market module for the legacy stablecoin is on the community roadmap for mid-2026. And expect the framework to keep tracking close to our supply monitor for as long as the staking mint stays the larger of the two forces.

## Summary

LUNC is the uncapped, community-governed proof-of-stake token of Terra Classic, and its supply grows because a staking-reward mint out-issues the network's burns. The chain mints about 95B LUNC over 90 days for stakers, while a 0.5% burn tax and exchange-led burns remove roughly 12B, leaving the framework at about +1.5% net. Our supply monitor reads +1.31% realized, so the two agree and no gap flag is raised. LUNC stays mildly inflationary on the active float, with the burns slowing dilution rather than reversing it — and the balance turning only if governance cuts the mint or lifts the burn.

*MrNasdog Pressure Framework analysis of Terra Classic (LUNC), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 5, 2026.*

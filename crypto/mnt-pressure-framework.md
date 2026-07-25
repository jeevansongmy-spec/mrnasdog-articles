---
title:         "MNT Inflation Analysis · July 2026 · Supply was growing, trend cooling"
description:   "MNT is capped at 6.22B with no mint, yet one Mantle treasury wallet released 24.4M MNT on Apr 28 2026. Framework net +0.85%, forward +0.12%, monitor +0.75%."
canonical_url: "https://mrnasdog.com/research/mnt/inflation"
tags:          ["crypto", "mnt", "mantle", "ethereum"]
published:     true
---

*Originally published at [mrnasdog.com/research/mnt/inflation](https://mrnasdog.com/research/mnt/inflation).*

Mantle's MNT is capped at **6.22B** coins with no mint and no vesting left, so nothing is created. Supply still grew over the last 90 days, because one Mantle treasury wallet was emptied of **24.4M MNT** on **Apr 28 2026** and the governance budget wallets spent another **3.8M**. That puts the framework at **+0.85%** net for the window against a supply monitor reading of **+0.75%** — but the release was a one-off, and the forward read falls to **+0.12%**.

## The verdict, in one paragraph

For the 90-day window closing Jul 24 2026, the MrNasdog Pressure Framework reads MNT at **+0.85% net** on the realised view and **+0.12%** on the forward view. Total sell pressure was **28.2M MNT** against **zero** buy pressure, on a circulating base of **3.30B MNT**. Our independent supply monitor puts the same window at **+0.75%**, so the gap is **0.10 percentage points** — inside tolerance, and **no monitor-gap chip** is raised. The small difference is explainable rather than mysterious: the monitor only sees the Mantle treasury classification change, while the framework also counts the budget wallets paying MNT out into the ecosystem. MNT is best described as a **capped coin with a lumpy, governance-controlled treasury release** — quiet by construction, punctuated by single large transfers.

## Sell pressure: where new MNT comes from

Sell #1 — protocol inflation — is **zero**, and this is the cleanest row on the page. MNT was issued once, at the 2023 BitDAO-to-Mantle merger, and the Ethereum layer-1 contract reports the same **6,219,316,794.89** MNT at both ends of the window. Max supply equals total supply. Mantle is a layer-2 rollup, so there is no validator reward and no emission curve to fund. Sell #2 — vesting unlocks — is also **zero**: every team, investor and contributor allocation completed vesting in 2023, and the unlock tracker walked for this build lists MNT as fully unlocked with no remaining events.

Sell #3 — Foundation and unscheduled unlocks — carries the entire window at **24.4M MNT**, and it is a single dated event rather than a drip. One of Mantle's treasury wallets held **24,350,327 MNT** in late April and was emptied in one transfer on **Apr 28 2026** into a wallet that has not moved a coin in the **87 days** since. Every other Mantle treasury wallet reads identically at both ends of the window, including the main one holding **2.90B MNT**. Because Mantle publishes circulating supply as total minus treasury, that one transfer is the whole of the reported float growth. The forward value is **zero**: the wallet is empty and no successor release has been published. Sell #4 — long-term locked or bankruptcy — is **zero**, since no bankruptcy estate or creditor distribution applies to MNT.

A fifth row is added because Mantle has a second live outflow that does not fit under the canonical four. The two governance budget wallets, which fund core and ecosystem programmes, paid out a combined **3.8M MNT** over the window, with the drawdown starting in June and still running. Those wallets already sit inside the published circulating figure, so their spending does not move the headline supply number — but the MNT does reach recipients, so the framework counts it. That is precisely the **0.10 percentage point** the framework reads above the monitor.

## Buy pressure: where new MNT goes

The buy side is **empty across all four rows**. Buy #1 — programmatic buyback — is zero: Mantle runs no buyback contract and publishes no buyback rate. A phased treasury burn of 3% to 8% of supply was floated on the Mantle governance forum in February 2026, but it never left the discussion stage and never became a proposal, so it cannot be counted. Buy #2 — protocol fee burn — is zero, and this surprises people: gas on Mantle is denominated in MNT, but the published fee mechanism splits a transaction into an execution fee and an Ethereum rollup fee, both routed to the network operator, with no burn leg. The unchanged total supply confirms it — no MNT has been destroyed. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero, with no treasury open-market buying and no new escrow announced in the window.

## Foundation and overhang

The defining fact about MNT is the overhang. The Mantle Treasury holds about **2.92B MNT**, roughly **47%** of the entire supply and nearly as much as the whole circulating float, alongside billions of dollars of other assets. It is spread across a small number of readable wallets: the main Ethereum treasury near **2,900M MNT**, a second holding wallet at **10M**, two treasury wallets on the Mantle network holding **7M** between them, and the governance budget wallets at **25.2M**. Beyond those sits the **24.4M** released in April, now parked in one unlabelled wallet and watched as a separate line. None of it is on a published release calendar; it enters the market only when Mantle governance authorises a budget or a transfer. If any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How MNT compares to other capped Ethereum L2 tokens

Mechanically, MNT sits in a small group of layer-2 tokens with a hard cap and no issuance at all. That places it closer to a fixed-cap store-of-value asset than to an uncapped layer-1 with continuous staking emission, where new coins arrive every block regardless of what the treasury does. Against those chains MNT looks quiet by design: its worst case is bounded by how much treasury exists, not by an open-ended emission curve.

Against other major layer-2 tokens, though, the comparison is less flattering. Most large rollup tokens still run a multi-year unlock calendar, so their supply growth is at least predictable and dated. Mantle finished vesting in 2023 and replaced that calendar with something harder to forecast: a very large treasury released by vote, with no schedule at all. The April transfer is the pattern in miniature — nothing for months, then **24.4M MNT** in a single block. A reader who prefers a published unlock table to a discretionary treasury will find MNT less legible, even though the total quantity at risk is capped.

The other structural difference is the missing burn. Rollups that burn a share of fees, in the style of Ethereum since 2021, get a small permanent offset that grows with usage. Mantle does not burn MNT at all, so there is no mechanism anywhere in the design that removes supply. Every reading of MNT is therefore weakly positive or flat — it cannot go deflationary without a governance vote that has not happened.

## What to watch in the next 90 days

First, the wallet that received **24.4M MNT** on Apr 28 2026 and has held it untouched ever since — a first outflow from it would be genuine market pressure, not a bookkeeping change. Second, the next Mantle budget proposal: the third budget cycle ran to Jun 30 2026, so a fourth is due, and passing one would refill the budget wallets and lift the Sell #5 pace. Third, the phased treasury burn discussion opened Feb 25 2026 — if it ever becomes a formal Mantle Improvement Proposal and passes, Buy #1 flips from zero for the first time. Fourth, MIP-34, the strategic credit facility passed Apr 24 2026, whose proceeds were floated as a possible source of MNT burns. Fifth, the budget drawdown itself, which only began moving in June and could accelerate.

## Summary

MNT is a hard-capped Ethereum layer-2 coin with no mint, no vesting and no burn, so its entire supply story is the Mantle Treasury. Over the last 90 days that story was one transfer — **24.4M MNT** out of a treasury wallet on Apr 28 2026 — plus **3.8M** of budget spending, giving **+0.85%** net against a monitor reading of **+0.75%**. Looking forward, with the released wallet empty and only budget spending left, the framework reads **+0.12%**. The key risk is not inflation but discretion: **2.92B MNT**, about **47%** of the capped supply, can reach the market whenever a vote says so, and nothing in the design ever takes MNT back.

---

*MrNasdog Pressure Framework analysis of MNT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 25 2026.*

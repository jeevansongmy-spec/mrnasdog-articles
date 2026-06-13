---
title: "XRP Inflation Analysis · June 2026 · Escrow drips in, most of it re-locks"
description: "No mint: XRP's supply already exists. Ripple's escrow releases 1B/month and re-locks most, netting ~900M over 90 days. Framework reads +1.45%."
canonical_url: "https://mrnasdog.com/research/xrp/inflation"
tags: ["crypto", "xrp", "ripple", "escrow"]
published: true
---

> Originally published at **[mrnasdog.com/research/xrp/inflation](https://mrnasdog.com/research/xrp/inflation)** by MrNasdog.

XRP has no mint — all 100 billion were created at genesis. The only supply that reaches the market comes from Ripple's monthly escrow release, which sends 1 billion XRP out and re-locks most of it, leaving a net of about **900M XRP** over 90 days. That is roughly **+1.45%** against the inflation monitor's **+1.51%** — a steady, schedule-driven drip rather than open-ended issuance.

## The verdict, in one paragraph

For the 90-day window ending June 14 2026, the MrNasdog Pressure Framework reads **XRP at +1.45% net**. The independent inflation monitor reads **+1.51%**, a gap of just **0.06 percentage points**, comfortably inside tolerance, so no data-conflict chip is raised. XRP creates no new tokens; what looks like inflation is the conversion of escrowed XRP into circulating XRP on a fixed monthly schedule. The reading is **structurally inflationary on the active float**, paced entirely by how much of each monthly escrow release Ripple keeps versus re-locks.

## Sell pressure: where new XRP comes from

Sell #1 — protocol inflation — is zero. All 100 billion XRP were created at genesis; the XRP Ledger has no mint and no staking issuance, so no new XRP is ever made. Every XRP that exists already exists. This is the single most important structural fact: XRP cannot inflate through emission the way a proof-of-stake or proof-of-work chain does.

Sell #2 — vesting unlocks — is the only live sell flow, at about **900M XRP** for the window. Ripple's escrow releases **1 billion XRP** on the 1st of each month, then re-locks most of it — roughly 60–80% — back into escrow. The net reaching the market is therefore about 200–300M a month, or around 900M over the three monthly releases inside the window. Sell #3 — Foundation and unscheduled unlocks — is zero as a flow: Ripple still holds tens of billions of XRP in escrow plus its own treasury, but those release only on the published monthly schedule, with no discretionary release beyond it. Sell #4 — long-term locked or bankruptcy — is zero; there is no bankruptcy estate, and the escrowed XRP is on a published schedule, not a one-off cliff.

## Buy pressure: where new XRP goes

The buy ledger is effectively empty. Buy #1 — programmatic buyback — is zero; there is no protocol buyback on XRP. Buy #2 — protocol fee burn — is technically non-zero but negligible: each transaction burns a tiny fee, a fraction of a drop, far too small to register against a circulating float above 62 billion. Buy #3 — Foundation buy — is zero, because Ripple absorbs unused XRP by re-locking it into escrow rather than buying on the open market. Buy #4 — new long-term lock — is zero as a separate line: the re-escrow of unreleased XRP is already counted as a reduction of the gross monthly release (it is what turns 1B gross into ~900M net), not booked again as a market buy.

## Foundation and overhang

The dominant overhang is the **on-ledger escrow plus Ripple's treasury**, still holding tens of billions of XRP. It is Ripple-controlled and releases on the 1-billion-per-month schedule, with roughly 60–80% re-locked each time. The framework treats the escrow as a scheduled overhang rather than a discretionary one, monitored on a roughly bi-weekly web walk. If the balance falls between refreshes — for example if Ripple were to re-lock a smaller share and keep more of a release — the additional outflow enters Sell #3 at the next refresh. The size of this overhang is why XRP's reading is sensitive to the re-lock ratio.

## How XRP compares to other fixed-supply, scheduled-release chains

XRP belongs to a small class of **pre-mined, fixed-supply assets that release on a schedule** rather than emit continuously. Unlike Bitcoin's halving model — where new supply is mined and falls on a fixed curve — XRP's entire supply already exists and the "inflation" is purely the unlocking of escrowed tokens. Unlike uncapped proof-of-stake chains like Solana or Ethereum, there is no validator issuance at all; the supply schedule is a corporate escrow policy, not a protocol emission rate.

That makes XRP's reading unusually **policy-driven**: the number depends on how much of each monthly release Ripple chooses to keep versus re-lock, a discretionary decision inside a published framework. The closest analogues are other foundation-held genesis allocations on partial release schedules. The mechanism difference that matters for an inflation reading is that XRP's float can only grow up to the escrow ceiling, and the pace is set by a re-lock ratio that Ripple publishes but can adjust within its policy.

## What to watch in the next 90 days

The clearest dated item is the **monthly escrow release on July 1 2026**, expected to add roughly 300M net after re-lock. Watch the re-lock ratio across the next few releases — if Ripple keeps a larger share of a release, the net climbs above the ~300M-a-month baseline; if it re-locks more, the net falls. Watch for any change to the escrow policy itself, which would reset the whole schedule. The per-transaction fee burn is worth nothing at current scale and can be ignored. There is no issuance variable to track because there is no issuance.

## Summary

XRP does not inflate through emission — it has no mint. The +1.45% net reading for the window is entirely the net escrow release: 1 billion XRP unlocked each month with roughly 60–80% re-locked, leaving about 900M reaching the market over 90 days, against the monitor's +1.51% — agreement within 0.06 percentage points. The buy side is empty apart from a negligible fee burn. The dominant overhang is the tens of billions still escrowed, released on a published monthly schedule. The reading is policy-driven: it rises or falls with the re-lock ratio Ripple applies to each release, and the next scheduled release is July 1 2026.

---

*MrNasdog Pressure Framework analysis of XRP, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 14, 2026.*

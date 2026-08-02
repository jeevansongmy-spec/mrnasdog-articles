---
title: "ZRO Inflation Analysis · August 2026 · The unlock calendar and the chain disagree"
description: "A MrNasdog Pressure Framework read of LayerZero (ZRO): the vesting calendar released ~72M in 90 days, the lock contracts released ~4.1M. Framework +1.04% net vs a monitor +40.35%."
canonical_url: "https://mrnasdog.com/research/zro/inflation"
tags: ["crypto", "zro", "layerzero", "token-unlocks"]
published: true
---

> Originally published at **[mrnasdog.com/research/zro/inflation](https://mrnasdog.com/research/zro/inflation)** by MrNasdog.

LayerZero's published vesting calendar showed about **72M ZRO** unlocking to strategic partners and core contributors over the last 90 days. The lock contracts that actually hold those allocations released only about **4.07M** — roughly a seventeenth of it. Against that, a Stargate-revenue buyback bought about **0.41M ZRO** on the open market and parked it in a public wallet that has never sold a token, so the MrNasdog Pressure Framework reads ZRO at about **+1.04% net** on a circulating base of **353.3M ZRO**. Our supply monitor reads **+40.35%** over the same window, a gap of about **39.3 percentage points** that resolves to a single-day bookkeeping restatement rather than a real release. ZRO is **diluting far more slowly than its own unlock schedule implies** — and carrying an enormous undrawn backlog because of it.

## The verdict, in one paragraph

For the last 90 days the MrNasdog Pressure Framework reads **ZRO at about +1.04% net**: sell pressure of about **4.07M ZRO** of realised release against buy pressure of about **0.41M ZRO** of accumulation, on a circulating base of **353.3M ZRO**. Our supply monitor reads **+40.35%** for the same period — a gap of about **39.3 percentage points**, far outside the half-point tolerance, so a monitor-gap flag ships with this page. The gap is not a disagreement about LayerZero's mechanics; it is a disagreement about dates. The monitor's entire 90-day move happened in **one** day, **Jul 8 2026**, when the classified circulating figure jumped about **+100.9M** in twenty-four hours while the token contract itself did not move a single unit. Every other day in that series drifts by less than **0.2M**. ZRO is best labelled **structurally inflationary on the active float** — but the calendar overstates that inflation many times over.

## Sell pressure: where new ZRO comes from

Sell #2 — vesting unlocks — is the whole sell-side story, and it is where the framework parts ways with every unlock tracker. The published calendar carries three monthly cliffs in the window — **May 20**, **Jun 20** and **Jul 20 2026**, roughly **24M ZRO** each, for about **72.15M ZRO** scheduled. But those allocations sit in a readable 36-contract escrow layer, and reading that same contract set on-chain at both ends of the window shows the aggregate fell from about **464.6M ZRO** to about **460.5M ZRO** — a realised release of only about **4.07M ZRO**, roughly **17.7 times** below the scheduled figure. The tokens vest on paper but stay inside the lock contracts, unclaimed; the framework books what actually left, not the calendar entitlement, because supply that never reaches the market is not sell pressure yet.

Sell #1 — protocol inflation — is **zero**, and structurally so. The full **1B ZRO** was minted at the June 2024 token generation event, and there is no active protocol mint. On the live block explorer, LayerZero token supply held near **951.1M** across the whole window, moving only about **156K** from routine bridge netting, with the burn address holding zero. Sell #3 — foundation and unscheduled unlocks — is **zero** because no team-controlled wallet made a discretionary off-calendar move, and Sell #4 — long-term locked or bankruptcy — is **zero** because LayerZero is a live project with no bankruptcy estate.

## Buy pressure: where new ZRO goes

Buy #1 — programmatic buyback — is the only non-zero buy row, at about **0.41M ZRO** over the window. LayerZero directs Stargate bridge revenue into open-market ZRO purchases — the full share of Stargate revenue since April 2026 — and parks the bought-back tokens in a public accumulation wallet. That wallet grew by about **0.41M ZRO** (roughly **124,600** in May and **141,600** in June), lifting its balance to about **2.03M ZRO**. The important structural point is that these tokens are **held, not burned**: the buyback removes ZRO from the open market but keeps it in a Foundation-controlled wallet, so it offsets float rather than permanently retiring supply.

Buy #2 — protocol fee burn — is **zero**, and this is the most consequential open question on ZRO. LayerZero has a designed fee switch that would charge a fee on every message verified across the network, convert those fees to ZRO and burn them permanently. It has been put to referendum four times and rejected each time for failing to reach quorum, most recently on **Jun 27 2026**. Until a referendum passes and executes on-chain, no protocol burn exists. Buy #3 — foundation buy — is **zero** beyond the buyback already counted, and Buy #4 — new long-term lock — is **zero** because no new fixed-size lockup was announced in the window.

## Foundation and overhang

The team-controlled overhang on ZRO is very large. About **460.5M ZRO** sits in the readable escrow layer — a 36-contract set inside the top-100 holders, anchored by a Foundation multisig holding about **106M ZRO**, a second custody safe holding about **69.5M ZRO**, and dozens of strategic-partner and core-contributor vesting contracts. Separately, the buyback accumulation wallet holds about **2.03M ZRO**. Together these are the tracked overhangs behind the zero in Sell #3: the capacity to add supply is enormous — roughly **646.7M ZRO**, about 65% of the cap, is non-circulating — but the observed cadence is tiny. The escrow layer and the buyback wallet are read on-chain at every rebuild; if any of these balances falls between refreshes faster than the realised run-rate, the excess outflow enters Sell #3 at the next refresh rather than being absorbed silently into the vesting row.

## How ZRO compares to other capped interoperability tokens

ZRO belongs to the class of hard-capped, venture-funded infrastructure tokens whose scarcity is real at the level of total supply but almost meaningless at the level of tradable float. Like Aptos, Sui or Celestia, its **1B** cap tells you little about near-term supply — what matters is that only **35.3%** is circulating and the rest arrives on a vesting calendar. Where ZRO is unusual is the gap between that calendar and reality: the escrow contracts are readable, and they show the calendar overstating realised release about **17.7 times**.

Against fee-burn and buyback chains the contrast is sharper still. Ethereum can post negative net issuance when base-fee burn exceeds validator rewards; BNB retires supply on a quarterly schedule. ZRO has the design for the first mechanism — a fee switch that would burn message-fee revenue — but it is switched off, rejected four votes running, so the burn does not exist. And its buyback, unlike a burn, accumulates in a wallet rather than destroying supply. The result is a token whose best-case net supply is a slow drift toward zero as the vesting backlog eventually drains, not a deflationary print — unless and until the fee switch passes and turns real message revenue into a permanent burn.

## What to watch in the next 90 days

Watch the monthly vesting cliffs on **Aug 20 2026** (about **32.6M ZRO** scheduled), **Sep 20 2026** and **Oct 20 2026** — but watch the escrow-contract balances rather than the calendar, because the whole question is whether the vested-but-unclaimed backlog starts to drain or keeps building. Watch the buyback wallet: the Stargate-funded purchases run monthly, and any change in that cadence or a move out of the accumulation wallet would shift Buy #1. Watch the next fee-switch referendum, expected roughly six months after the Jun 2026 vote — a pass would open the first real burn row on ZRO and change the structural verdict. And watch the tracked circulating figure, which will likely restate again in single-day steps as the calendar and the realised float reconcile.

## Summary

The MrNasdog Pressure Framework reads ZRO as **structurally inflationary on the active float** at about **+1.04% net** over 90 days — but far less inflationary than the calendar implies. LayerZero's unlock schedule shows about **72M ZRO** vesting, yet the readable lock contracts released only about **4.07M**, against a Stargate-funded buyback of about **0.41M** that accumulates rather than burns. Our supply monitor's **+40.35%** reading is a single-day restatement of classified circulating supply on Jul 8 2026, not a measured release, so the framework keeps the on-chain read and flags the gap. The key risk is the roughly **646.7M ZRO** — about 65% of the fixed cap — that is still locked; the key catalyst is a fee switch that stays off, four votes running, and would be the only lever that could ever make ZRO supply shrink.

*MrNasdog Pressure Framework analysis of ZRO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 2 2026.*

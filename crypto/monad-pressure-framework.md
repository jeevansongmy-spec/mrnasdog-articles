---
title: "MON Inflation Analysis · July 2026 · Supply growing, projected to keep growing"
description: "A MrNasdog Pressure Framework read of Monad (MON): ~493M/90d minted as block rewards vs a tiny ~10M base-fee burn. Framework +4.1% net; monitor +0.02% float (4.1pp gap)."
canonical_url: "https://mrnasdog.com/research/monad/inflation"
tags: ["crypto", "mon", "monad", "layer-1"]
published: true
---

> Originally published at **[mrnasdog.com/research/monad/inflation](https://mrnasdog.com/research/monad/inflation)** by MrNasdog.

**TL;DR.** Monad mints about **493M MON** over 90 days as validator block rewards — 25 MON a block, roughly 2% a year — while only a tiny base-fee burn of about **10M MON** offsets it, so the framework reads about **+4.1%** net, inflationary. Our supply monitor reads the tradable float almost flat at **+0.02%** over the same window, a gap of about **4.1 percentage points** that ships a data-conflict flag: the minted rewards go to stakers and never enter the float. MON is structurally inflationary on an uncapped supply, with much larger team and investor unlocks still ahead.

## The verdict, in one paragraph

For the 90-day window ending July 14 2026, the MrNasdog Pressure Framework reads **Monad at about +4.1% net** on both the last-90-day and next-90-day views, driven almost entirely by protocol block rewards that the base-fee burn barely dents. Our supply monitor reads the realized circulating float at just **+0.02%** — essentially flat — so the gap is about **4.1 percentage points**, well past the half-point tolerance, and a **monitor-gap flag ships**. The reason is mechanical rather than a data error: Monad mints **25 MON** every 400-millisecond block straight into validator and delegator balances, which are staked and never reach the tradable float the monitor measures, and the base-fee burn is too small to offset issuance. MON is best labelled **structurally inflationary on an uncapped supply** — the total supply climbs steadily even while the visible float looks quiet.

## Sell pressure: where new MON comes from

Sell #1 — protocol inflation — is the entire sell story, at about **493M MON** minted over 90 days. Monad pays a fixed inflationary reward of **25 MON** per block to the validator that produces it and its delegators, and with a 400-millisecond block time that annualizes to roughly **2B MON** a year, about 2% of the 100B genesis supply. The chain is **uncapped**, and its total supply already sits above the 100B genesis figure, confirming the mint is real and continuous. Because the reward rate is fixed rather than usage-driven, the next 90 days carry the same **493M** figure.

The other three sell rows are zero in this window. Sell #2 — vesting unlocks — is **zero** because no scheduled cliff lands in the next 90 days; the first large insider unlock, combining team, investor and Category Labs treasury coins into roughly **16.62B MON**, is a 12-month cliff from the November 2025 launch that fires on **Nov 24 2026**, just outside this window. Sell #3 — Foundation and unscheduled unlocks — is zero as a flow even though the overhang is enormous, because the Foundation publishes no dated release cadence for its ecosystem pool. Sell #4 — long-term locked or bankruptcy — is zero, since no bankruptcy estate applies and the team and investor allocations are locked, not releasing.

## Buy pressure: where new MON goes

The buy ledger is almost empty. Buy #1 — programmatic buyback — is **zero**: Monad runs no revenue-funded buyback, and as a young chain it has no fee stream to recycle into MON. Buy #2 — protocol fee burn — is the only live offset, at about **10M MON** over 90 days. Monad burns the base component of every transaction fee in an EIP-1559 style, but at current activity the burn is a rounding error against the mint: the network would need to burn far more MON each day just to offset issuance, and it destroys only a small fraction of that. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero, with no open-market buying and no new escrow announced; staking MON with validators is not counted as a buy, and the launch delegation is already in the base. With the burn near a fiftieth of the mint, MON stays a clear net issuer.

## Foundation and overhang

Monad's defining feature is how much supply is not yet circulating: only about **11.8B** of the 100B genesis MON is in the float. The single largest team-controlled overhang is the **Ecosystem Development** pool of about **38.5B MON** — technically unlocked at launch but foundation-controlled, with under 2% committed so far and about **15B MON** of it delegated to bootstrap validators rather than sold. Behind it sit the locked **Team** allocation of about 27B, the **Investor** allocation of about 19.7B, and the Category Labs treasury, all subject to a one-year cliff from November 2025. None of these carries a dated flow inside this window, so the framework books them at zero and re-checks the ecosystem deployment and unlock calendar on a roughly bi-weekly walk; if any of these balances falls between refreshes, that outflow enters Sell #3 at the next refresh.

## How MON compares to other uncapped Layer-1 chains

Monad belongs to the class of **uncapped, continuous-emission Layer-1s** that both mint and burn — structurally closer to Ethereum and Solana than to a hard-capped, halving coin like Bitcoin. Like Ethereum after the merge, Monad pairs a validator-reward mint with an EIP-1559 base-fee burn; the difference is direction. Ethereum can flip net-deflationary when block space is in heavy demand, because its burn scales with usage on a mature fee market. Monad, as a brand-new chain, has almost no fee volume yet, so its burn is negligible and the mint wins outright — a profile much like Solana's early years, when high fixed issuance ran well ahead of on-chain burn.

The other axis that separates **Monad** from established chains is float maturity. Bitcoin, Ethereum and Solana have most of their supply already circulating, so their inflation reads are dominated by protocol issuance. Monad has only about 11.8% of MON in the float and roughly half the supply locked behind a November 2026 cliff, which means its future dilution is driven less by the 2% block reward than by the unlock schedule. For an inflation lens today, MON reads as mildly-to-moderately inflationary from issuance alone — but the structural risk that dwarfs the block reward is the cliff calendar, not the mint.

## What to watch in the next 90 days

Watch the block-reward rate, the single mint line — it is fixed at 25 MON per block today, but any protocol change to issuance would move Sell #1 directly. Watch the base-fee burn: rising network usage would lift the burn toward the mint and pull the net reading down, so a genuine activity ramp is the main thing that could soften MON's inflation. Watch Foundation ecosystem deployment, since grants, incentives and fresh validator delegations from the roughly **38.5B MON** pool are what move the visible float and could reopen a gap with the monitor. And above all watch the **Nov 24 2026** cliff, when about **16.62B MON** of team, investor and treasury supply begins unlocking — the event that will dominate MON's inflation reading once it enters the 90-day window.

## Summary

Monad is a young, uncapped parallel-EVM Layer-1 whose supply grows from a fixed block reward: it mints about 493M MON over 90 days as validator rewards while only a tiny base-fee burn of about 10M MON offsets it, leaving the framework at about +4.1% net. Our supply monitor reads the tradable float almost flat at +0.02%, a gap of about 4.1 percentage points, because the minted rewards are staked and never reach the float — so a data-conflict flag ships. The structural mechanism is continuous issuance with no meaningful burn, and the key risk is not the 2% mint but the November 2026 cliff, when roughly 16.62B MON of team and investor supply begins to unlock. With no supply cap, MON's ceiling is set by that unlock calendar rather than by code.

---

*MrNasdog Pressure Framework analysis of Monad (MON), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 14 2026.*

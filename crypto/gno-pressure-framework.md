---
title:         "GNO Inflation Analysis · August 2026 · Supply roughly flat, projected to stay flat"
description:   "GNO is a capped staking token with almost no new supply — only a thin Gnosis Chain validator-reward mint of about 3.1K GNO over 90 days. Framework +0.12% net, monitor +0.10%, no buyback and no GNO fee burn."
canonical_url: "https://mrnasdog.com/research/gno/inflation"
tags:          ["crypto", "gno", "gnosis", "inflation"]
published:     true
---

*Originally published at [mrnasdog.com/research/gno/inflation](https://mrnasdog.com/research/gno/inflation)*

Gnosis GNO is a capped staking token with almost no new supply. The only mechanism that adds float is Gnosis Chain minting validator rewards — about **3.1K GNO** over 90 days against a circulating base of **2.64M** — so the framework reads **+0.12% net**, barely inflationary. There is no GNO buyback and no GNO fee burn, because Gnosis Chain charges gas in xDAI rather than GNO, and GnosisDAO is actively burning its legacy 10M supply down toward a **3M target**. Our supply monitor reads **+0.10%**, a gap of just **0.02 percentage points** — inside tolerance, so no monitor-gap flag ships.

## The verdict, in one paragraph

For the 90-day window ending Aug 9 2026, the Pressure Framework reads **GNO at +0.12% net**. Sell pressure is a single small row — roughly **3.1K GNO** of Gnosis Chain staking rewards minted by the consensus layer — and every buy row is **zero**, against a circulating base of **2.64M GNO**. Our supply monitor reads the realised change at **+0.10%**, a gap of just **0.02 percentage points**, which is well inside tolerance and ships **no monitor-gap chip**. The two readings agree: GNO's float is nearly flat and the validator-reward trickle is the whole of it. GNO is best characterised as **a capped staking token being burned down toward a 3M target, whose only new supply is a thin and cooling validator-reward stream**.

## Sell pressure: where new GNO comes from

Sell #1, protocol inflation, is the only non-zero row. Gnosis Chain is a proof-of-stake network where validators stake **1 GNO** each and the consensus layer mints fresh GNO as attestation, proposal and sync-committee rewards — genuine new issuance, which the reward curve labels as overall inflation per year. About **145K GNO** is staked today, one per validator, down from roughly **300K** a year earlier, and at a documented yield near **8.54%** that mints close to **3.1K GNO** over 90 days, a **+0.12%** trickle. Because the reward rate falls as more GNO stakes and the active set is shrinking, this stream is cooling rather than growing.

Sell #2, vesting unlocks, is **0**: the old 10M cap left about 7M GNO in an 8-year vesting contract from Nov 2020, but GnosisDAO is burning that GNO toward the 3M target — a **3.15M** burn cleared in Jan 2025 — so it shrinks supply rather than releasing it. Sell #3, Foundation and unscheduled unlocks, is **0** as a flow: the DAO holds the roughly **360K** of non-circulating GNO but is not selling, and the June 2026 GIP-151 vote pulls GNO into the DAO rather than out. Sell #4, long-term locked or bankruptcy, is **0**: there is no GNO estate and no trustee distribution.

## Buy pressure: where new GNO goes

Every buy row is **0**, but for structural reasons rather than inactivity. Buy #1, a programmatic buyback, does not exist: GnosisDAO runs no open-market GNO buyback. The June 2026 GIP-151 proposal is often misread as one — it is a one-time pro-rata **treasury redemption** that lets holders surrender GNO for a share of the DAO's roughly **$223M** treasury at about **$170** per GNO, which removes float when realised, but it is holder-initiated and so far immaterial to the classified circulating count.

Buy #2, protocol fee burn, is **0** because Gnosis Chain charges gas in **xDAI**, a stablecoin — the chain's EIP-1559-style base-fee burn destroys xDAI-equivalent value, never GNO. Buy #3, Foundation buy, is **0** because no DAO or foundation open-market purchase is disclosed; the DAO's supply lever is burning the vesting contract, not buying. Buy #4, new long-term lock, is **0**: staking into validators is a cooldown-withdrawable lock and staked GNO still counts as circulating, so it removes no float.

## Foundation and overhang

Two team-controlled pools matter. The first is the **vesting contract** holding the gap between the on-chain 10M ERC-20 supply and the 3M target — roughly 7M GNO — which is being progressively burned rather than released, so it is a deflationary overhang, not a sell overhang. The second is the **GnosisDAO treasury**, which sits behind the difference between the 2.64M circulating and the 3M target, about **360K GNO** of non-circulating supply, plus a liquid treasury valued near $223M. The live variable here is GIP-151: if holders redeem in size through the redemption portal, GNO flows into the DAO and the tradable float shrinks. The DAO's wallets and the redemption volume are re-read every rebuild, and if the balance moves between refreshes — either the DAO releasing GNO or redemptions pulling it in — that outflow or inflow enters Sell #3 or the buy side at the next refresh.

## How GNO compares to other capped staking tokens

The useful comparison is capped-and-burning versus uncapped-and-emitting. Many proof-of-stake layer-1s issue new supply continuously with no ceiling, so their sell side scales up with the validator set — the more that stakes, the more is minted. GNO inverts both halves: it has a **3M target cap** the DAO is burning toward, and its reward curve pays **less** as more GNO stakes, so issuance is bounded and, with a shrinking validator set, currently falling. That places GNO closer to a capped asset like **BNB** — which also burns supply down toward a floor — than to an uncapped emitter.

The sharper contrast is where the fee burn lands. Chains such as **ETH** burn their own native token in the EIP-1559 base fee, so heavy usage directly shrinks the native supply. Gnosis Chain deliberately does not: gas is paid and burned in **xDAI**, keeping GNO purely a staking and governance asset, so network activity never touches GNO supply. The result is that GNO's supply story is unusually quiet — no buyback, no GNO fee burn, no unlock calendar — and the entire reading rests on one small, measurable validator-reward stream that the framework can size directly.

## What to watch in the next 90 days

First, GIP-151 redemption volume: if holders surrender GNO to the DAO in size, the circulating float would shrink and the framework would turn genuinely deflationary. Second, the validator count, which sets Sell #1 — a continued decline from the current **~145K** would cool the staking trickle further, while a rebound would lift it. Third, the next scheduled vesting-contract burn toward the 3M target, which shrinks total supply without touching the tradable float. Fourth, any change to the Gnosis Chain reward curve or staking yield, since the yield is what sizes the only non-zero row. Fifth, the treasury itself — a governance decision to deploy or sell any of the roughly 360K non-circulating GNO would be a real, one-time supply event to book in Sell #3.

## Summary

Gnosis GNO is a capped staking token whose supply is nearly flat: the only mechanism adding float is Gnosis Chain minting about 3.1K GNO of validator rewards over 90 days, which puts the framework at +0.12% net against a 2.64M circulating base, barely inflationary and cooling as the validator set shrinks. There is no GNO buyback and no GNO fee burn — gas is paid in xDAI — while GnosisDAO burns its legacy 10M supply down toward a 3M target. Our supply monitor reads +0.10%, a 0.02-point gap that keeps the two readings in agreement with no flag. The key structural fact is that GNO's float is quiet by design, and the thing most likely to change it is not new issuance but GIP-151 redemptions pulling GNO into the DAO treasury.

---

*MrNasdog Pressure Framework analysis of Gnosis (GNO), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated August 9 2026.*

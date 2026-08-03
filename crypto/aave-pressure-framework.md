---
title:         "AAVE Inflation Analysis · August 2026 · Mixed flows, supply roughly steady"
description:   "Aave's capped 16M AAVE is fully minted with no burn, and the Aavenomics 3.0 buyback moves price, not supply. Framework +0.15% net; monitor +1.52%."
canonical_url: "https://mrnasdog.com/research/aave/inflation"
tags:          ["crypto", "aave", "aavenomics", "defi"]
published:     true
---

*Originally published at [mrnasdog.com/research/aave/inflation](https://mrnasdog.com/research/aave/inflation)*

Aave's AAVE is a fixed **16,000,000** token, fully minted, with no mint function and no burn — so the entire supply story is a slow staking-reward stream out of one DAO reserve. Reading that reserve on-chain, it paid about **23K AAVE** to stakers over 90 days against a circulating base of **15.42M**, so the framework reads **+0.15% net** — barely inflationary. The headline Aavenomics 3.0 buyback (live Jun 27 2026, ~292 AAVE a day) supports price but does not shrink the float, because the coins it buys are redistributed rather than locked away. Our supply monitor reads **+1.52%**, a gap of **1.37 percentage points** that we attribute to a supply-count reclassification, not to new tokens hitting the market.

## The verdict, in one paragraph

For the 90-day window ending Aug 3 2026, the Pressure Framework reads **AAVE at +0.15% net**. Sell pressure is a single small row — about **23K AAVE** of Safety Module staking rewards paid out of the Aave DAO Ecosystem Reserve — and buy pressure that reduces supply is **zero**, against a circulating base of **15.42M AAVE**. Our supply monitor reads the realised change at **+1.52%**, a gap of **1.37 percentage points**, which is outside tolerance and ships a monitor-gap chip. The gap is a classification artifact, not a real conflict: on-chain the only non-circulating AAVE pool net-drained just ~23K, while a one-time **302K AAVE** sweep out of the LEND migrator into the reserve on **May 7 2026** was reserve-to-reserve and never touched the market. AAVE is best characterised as **a capped, fully-minted token whose float is essentially flat, with a buyback that moves price rather than supply**.

## Sell pressure: where new AAVE comes from

There is no new AAVE minted. The token contract read on-chain returns a totalSupply of exactly **16,000,000**, all issued at the 2020 LEND→AAVE migration, and there is no live mint. Sell #1, protocol inflation, is therefore not real issuance but a redistribution: the Aave DAO Ecosystem Reserve pays Safety Module (stkAAVE) staking rewards out of its own already-minted AAVE, and because the reserve is the only pool classified as non-circulating, coins leaving it are the only coins reaching the tradable float. Reading the reserve directly, it drained about **23K AAVE** to stakers over the window, and on the post-Jun 27 2026 pace that runs closer to **29K** over the next 90 days. Sell #2, vesting unlocks, is **zero**: all team, investor and migration allocations finished years ago, and the last unclaimed LEND-migration balance swept out of the migrator on **May 7 2026** — into the reserve, not the market. Sell #3, Foundation and unscheduled unlocks, is **zero** as a flow, though the ~578K-AAVE reserve is a tracked overhang covered below. Sell #4, long-term locked or bankruptcy, is **zero**: there is no AAVE estate, and the Apr 18 2026 Kelp/rsETH exploit that left bad debt in the protocol's asset pools created no AAVE token supply.

## Buy pressure: where new AAVE goes

Buy #1, the programmatic buyback, is the loudest part of the AAVE story and the most misread. On **Jun 27 2026** the Aave DAO activated Aavenomics 3.0, an immutable automated engine that routes protocol and GHO revenue — roughly **$402M** annualised — into open-market AAVE purchases at about **292 AAVE** a day, replacing the earlier discretionary program that was paused on **Apr 19 2026** after the exploit. But the framework measures supply, not price, and on that basis the buyback nets to **zero**: reading the only non-circulating pool on-chain, no bought AAVE was parked there over the window, so the purchased coins are redistributed to holders rather than locked away, and the circulating float does not shrink. Buy #2, protocol fee burn, is **zero** because Aave burns no AAVE — revenue funds the buyback, it does not destroy tokens. Buy #3, Foundation buy, is **zero** because the only open-market buying is the buyback already in Buy #1. Buy #4, new long-term lock, is **zero**: Safety Module staking is a cooldown, not a lock, and staked AAVE is still counted as circulating.

## Foundation and overhang

One team-controlled pool matters: the **Aave DAO Ecosystem Reserve**, an on-chain contract that holds about **578K AAVE**, roughly 3.6% of the 16M cap. It is the wallet that pays the staking rewards counted in Sell #1, so it is being drawn down slowly rather than released in bulk, and because circulating supply is defined as sixteen million minus this reserve, its balance is effectively the master supply dial. A second, conditional overhang sits behind it: a proposed Kraken deal would send **250K AAVE** from the DAO in exchange for 35,000 ETH and a 15% equity stake, but it is unconfirmed and unexecuted, so it books nothing today. The reserve is re-read every rebuild, and if its balance falls faster between refreshes — through a larger reward stream or a governance release — that outflow enters Sell #3 at the next refresh.

## How AAVE compares to other capped DeFi governance tokens

The comparison that matters is cap-and-minted versus emitting. Many DeFi governance tokens still issue new supply through liquidity mining or staking curves, so their sell side scales with usage. AAVE does not: the **16M cap** is fully minted, nothing new is created, and the only float growth is a reserve slowly paying out already-existing coins — structurally close to **LDO**, another capped, fully-vested governance token whose sell rows are near zero.

The sharper comparison is burn versus buy-and-distribute. Exchange tokens such as **BNB** run buybacks that end in a burn address, so every purchased coin is destroyed and the supply feed books an irreversible shrink. Aavenomics 3.0 does the opposite: it buys AAVE with protocol revenue but **redistributes** the coins to holders rather than burning or sequestering them, so the float is unchanged even as the buy volume is large. That is why a token with a headline automated buyback still reads roughly flat here — the mechanism is a demand and yield story, not a supply-reduction story. The framework's value in this case is precisely that it separates the two: AAVE's supply is quiet regardless of how loud the buyback is.

## What to watch in the next 90 days

First, whether Aavenomics 3.0 changes its destination — if a future vote routes bought AAVE into a locked or burned reserve rather than back to holders, Buy #1 would turn genuinely deflationary overnight. Second, the Kraken deal: if it closes, **250K AAVE** leaving the DAO would be a real, one-time supply event to book in Sell #3. Third, the pace of the Ecosystem Reserve drawdown, which is the single cleanest signal of float growth and is read every rebuild. Fourth, any Safety Module or Umbrella staking-reward change, since the reward rate is what sets the size of Sell #1. Fifth, the monitor gap itself — if the supply-count reclassification finishes settling, the monitor should converge back toward the framework's near-flat reading.

## Summary

Aave's AAVE is a fixed 16M token, fully minted, with no mint and no burn, so its only supply movement is a slow staking-reward stream out of the DAO Ecosystem Reserve — about 23K AAVE over 90 days, which puts the framework at +0.15% net, barely inflationary. The headline Aavenomics 3.0 buyback, live since Jun 27 2026 at roughly 292 AAVE a day, supports price but is circulating-neutral, because the coins it buys are redistributed rather than locked, and no bought AAVE accumulates in the sole non-circulating pool. Our supply monitor reads +1.52%, a 1.37-point gap we attribute to a supply-count reclassification rather than new tokens, so we keep the primary reading and flag it. The key structural fact is that AAVE's float is quiet whatever the buyback does, and the key thing that would change it is a governance decision to lock or burn what the buyback buys.

---

*MrNasdog Pressure Framework analysis of AAVE, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 3 2026.*

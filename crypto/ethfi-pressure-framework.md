---
title:         "ETHFI Inflation Analysis · August 2026 · Supply growing slowly, a count catch-up aside"
description:   "No protocol mint: only the last of ether.fi's core-contributor vesting still releases — ~13.06M ETHFI over 90 days — while the buyback pays stakers instead of burning. Framework +1.34% net (monitor +16.41%, a circulating-count catch-up)."
canonical_url: "https://mrnasdog.com/research/ethfi/inflation"
tags:          ["crypto", "ethfi", "etherfi", "defi"]
published:     true
---

> Originally published at **[mrnasdog.com/research/ethfi/inflation](https://mrnasdog.com/research/ethfi/inflation)** by MrNasdog.

**TL;DR.** ether.fi's ETHFI is a fixed **1,000,000,000** token, fully minted on-chain with no mint function and no burn, so the entire supply story is vesting. The only allocation still releasing is the core-contributor grant, which put about **13.06M ETHFI** into the float over 90 days against a circulating base of **973.5M**, so the framework reads **+1.34% net** — mildly inflationary. The revenue buyback that buys ETHFI weekly and monthly is redistributed to sETHFI stakers, so it supports price without shrinking supply. Our supply monitor reads **+16.41%**, a gap of about **15 percentage points** that we attribute to a circulating-count catch-up, not to new tokens hitting the market.

## The verdict, in one paragraph

For the 90-day window ending Aug 6 2026, the Pressure Framework reads **ETHFI at +1.34% net**. Sell pressure is a single small row — about **13.06M ETHFI** of core-contributor vesting — and buy pressure that reduces supply is **zero**, against a circulating base of **973.5M ETHFI**. Our supply monitor reads the realised change at **+16.41%**, a gap of about **15 percentage points**, which is far outside tolerance and ships a monitor-gap chip. The gap is a classification artifact, not a real conflict: on-chain totalSupply held flat at **998.5M** with no mint, while the circulating count rose in three roughly **45M** monthly steps as already-vested treasury and airdrop buckets were reclassified into circulating. ETHFI is best characterised as **a capped, near-fully-vested restaking token whose float grows only from the last of core-contributor vesting, with a buyback that moves price rather than supply**.

## Sell pressure: where new ETHFI comes from

There is no new ETHFI minted. The token contract read on-chain returns a totalSupply of **998,535,999** against a fixed **1B cap**, and there is no live mint or staking emission, so Sell #1, protocol inflation, is **zero**. All supply movement is vesting. Sell #2, vesting unlocks, is the only non-zero sell row: of the seven original allocations, six reached their final unlocked value before this window — investors fully unlocked on **Mar 18 2026**, and the airdrop, treasury, incentive and liquidity buckets were done well before that. The one allocation still releasing is the **core-contributor** grant, which vests linearly at about **145K ETHFI** a day and put roughly **13.06M** into the float over the last 90 days, running until **Mar 14 2027**. Sell #3, Foundation and unscheduled unlocks, is **zero** as a flow: the ether.fi DAO treasury holds a large ~216M ETHFI allocation and roughly 31.8M of core-contributor tokens are still locked, but neither has a published sell schedule and no bulk outflow to the market was observed. Sell #4, long-term locked or bankruptcy, is **zero**: there is no ETHFI estate and no trustee distribution.

## Buy pressure: where new ETHFI goes

Buy #1, the programmatic buyback, is the loudest part of the ETHFI story and the most misread. ether.fi routes 100% of eETH withdrawal-fee revenue each week, plus a slice of monthly protocol revenue, into open-market ETHFI purchases. But the framework measures supply, not price, and on that basis the buyback nets to **zero**: the bought ETHFI is handed to **sETHFI** stakers rather than burned or locked away, so the coins flow straight back into circulation and the float does not shrink. Buy #2, protocol fee burn, is **zero** because ether.fi burns no ETHFI — revenue funds the buyback, it does not destroy tokens. Buy #3, Foundation buy, is **zero** because the only open-market buying is the buyback already in Buy #1. Buy #4, new long-term lock, is **zero**: staking ETHFI into sETHFI is a yield wrapper, not a supply lock, and staked ETHFI is still counted as circulating.

## Foundation and overhang

Two team-controlled pools matter. The first is the remaining **core-contributor** lock — about **31.8M ETHFI** still vesting linearly to **Mar 14 2027**, which is the source of the Sell #2 flow already counted above. The second is the **ether.fi DAO treasury**, a DAO-governed allocation of roughly **216M ETHFI** with no published sell schedule; it is a capacity overhang rather than an active flow, so it books nothing today. Both are re-read every rebuild, and if either balance falls faster between refreshes — through a larger contributor claim or a governance-authorised treasury release — that outflow enters Sell #3 at the next refresh.

## How ETHFI compares to other capped DeFi governance tokens

The comparison that matters is cap-and-vest versus emitting. Many DeFi and liquid-staking governance tokens still issue new supply through liquidity mining or staking curves, so their sell side scales with usage. ETHFI does not: the **1B cap** is fully minted, nothing new is created, and the only float growth is the tail of a vesting schedule — much like **AAVE** or **LDO**, other capped governance tokens whose sell rows are small and shrinking as vesting completes.

The sharper comparison is burn versus buy-and-distribute. Exchange tokens such as **BNB** run buybacks that end in a burn address, so every purchased coin is destroyed and the supply feed books an irreversible shrink. ether.fi does the opposite: it buys ETHFI with protocol revenue but **redistributes** the coins to sETHFI stakers rather than burning or sequestering them, so the float is unchanged even when the buy volume is large. That is why a token with a real revenue buyback still reads mildly inflationary here — the buyback is a yield-and-demand story, and the supply reading is driven entirely by the last stretch of core-contributor vesting. The framework's value in this case is precisely that it separates the two: ETHFI's supply is quiet regardless of how loud the buyback is.

## What to watch in the next 90 days

First, the core-contributor vesting pace, which is the single cleanest signal of float growth — it is scheduled to add roughly **13.06M ETHFI** before **Nov 4 2026** and to finish entirely by **Mar 14 2027**, after which the framework's sell side goes to zero. Second, whether the buyback ever changes its destination — if a future vote routes bought ETHFI into a locked or burned reserve rather than back to stakers, Buy #1 would turn genuinely deflationary overnight. Third, any DAO decision to deploy the ~216M-ETHFI treasury, which is the largest dormant overhang and would land in Sell #3 if released. Fourth, the monitor gap itself — if the circulating-count catch-up finishes settling, the monitor should converge back toward the framework's near-flat reading. Fifth, protocol-revenue trends, since a larger buyback pays more yield but still leaves the supply reading unchanged.

## Summary

ether.fi's ETHFI is a fixed 1B token, fully minted on-chain with no mint and no burn, so its only supply movement is the last of core-contributor vesting — about 13.06M ETHFI over 90 days, which puts the framework at +1.34% net, mildly inflationary. The revenue buyback that buys ETHFI weekly and monthly is circulating-neutral, because the coins it buys are redistributed to sETHFI stakers rather than locked or burned. Our supply monitor reads +16.41%, a roughly 15-point gap we attribute to a circulating-count catch-up rather than new tokens, so we keep the primary reading and flag it. The key structural fact is that ETHFI's float is quiet whatever the buyback does, and the sell side is set to fade to zero when vesting completes in March 2027.

---

*MrNasdog Pressure Framework analysis of ether.fi (ETHFI), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated August 6 2026.*

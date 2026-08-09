---
title: "SEI Inflation Analysis · August 2026 · Supply growing on the unlock calendar"
description: "A MrNasdog Pressure Framework read of Sei (SEI): the launch unlock calendar releases about 360.8M SEI over 90 days — team and investor vesting plus a reserve-funded staking drip — with no buyback and no burn. Framework reads +5.36% net."
canonical_url: "https://mrnasdog.com/research/sei/inflation"
tags: ["crypto", "sei", "sei-network", "layer1"]
published: true
---

*Originally published at [mrnasdog.com/research/sei/inflation](https://mrnasdog.com/research/sei/inflation).*

Sei adds about **360.8M SEI** to the market over the next 90 days — roughly **318.3M** from team and investor vesting and **42.5M** from staking rewards paid out of a reserve — against **zero** buyback and **zero** fee burn. The MrNasdog Pressure Framework reads **+5.36% net**, while the supply monitor reads about **-0.03%** over the same window — a gap of about **5.43 percentage points** that trips a **monitor-gap flag**, because the monitor's circulating feed has been frozen since March. Sei capped its supply at **10B** and mints nothing new, yet the launch unlock calendar still floods the float.

## The verdict, in one paragraph

Over the last 90 days the MrNasdog Pressure Framework reads Sei at **+5.40% net**: about **363.3M SEI** of new supply reaching the market against **no** buy-side offset at all, on a circulating base of **6.73B SEI**. The supply monitor reads the same trailing window at roughly **-0.03%** — essentially flat — for a gap of about **5.43 percentage points**, well outside the framework's half-point tolerance. That gap ships with a **monitor-gap flag**, and the reason is specific and datable: the circulating-supply feed the monitor divides by has been pinned at exactly **6,733,333,333 SEI** since **Mar 22 2026** — about four and a half months frozen — while the published vesting schedule kept releasing coins the whole time. The framework books the real unlock supply; the frozen feed shows almost none. Sei is **structurally inflationary on its unlock calendar** — a hard-capped token that mints nothing new, but whose four-plus-year vesting schedule still dilutes the float faster than anything removes it.

## Sell pressure: where new SEI comes from

Sell #2 — vesting unlocks — is the dominant stream, at about **318.3M SEI** over the next 90 days. Sei launched in August 2023 with a fixed **10B** supply split into five buckets — 48% ecosystem reserve, 20% team, 20% private-sale investors, 9% Foundation and 3% Binance Launchpool — and the team and investor allocations are still vesting on the original launch calendar. They release as a steady daily stream rather than in one cliff: over the window that is roughly **166.7M SEI** to early investors, **126.7M** to the team and **25M** to strategic backers. This single calendar is the whole inflation story for Sei.

Sell #1 — protocol inflation — is real but small, and it is not what most chains call inflation. Sei's Cosmos mint module is switched off: the chain mints no new SEI and supply is capped at **10B**. Staking rewards are instead paid out of a pre-allocated ecosystem-reserve bucket, so on the roughly **4.19B SEI** currently staked the reserve releases about **42.5M SEI** over 90 days as a continuous drip. It is new supply reaching stakers, but it comes from a fixed pool that shrinks as it pays out — not from open-ended minting that could ever push supply past the cap.

Sell #3 — foundation and unscheduled unlocks — is **zero** on this build, though the overhang behind it is large: about **2.5B SEI** is still locked and team-controlled, spanning the ecosystem-reserve remainder, the Sei Foundation treasury and the unvested tail of the team and investor buckets. The framework books nothing here because every one of those pools releases through the published calendar already counted in Sell #1 and Sell #2, and no off-schedule Foundation distribution was observed in the window. Sell #4 — long-term locked or bankruptcy — is **zero** and structurally so: Sei is a live, solvent project with no bankruptcy estate and no trustee distribution.

## Buy pressure: where new SEI goes

Every buy row is **zero**, and that is the crux of Sei's reading. Buy #1 — programmatic buyback — is zero: Sei runs no protocol or Foundation mechanism that repurchases SEI on the open market. Buy #2 — protocol fee burn — is zero too, and this is the structural weakness: unlike an EIP-1559-style chain, Sei does **not** burn its gas fees. The base fee is paid out to validators and application developers, not destroyed, so network usage generates no deflationary offset. Buy #3 — Foundation buy — is zero, with no disclosed open-market accumulation program. Buy #4 — new long-term lock — is zero as well: staked SEI can be unbonded after a short waiting period, so staking is not a permanent lock and no new fixed-size lock-up fired in the window. With nothing on the buy side, every coin the calendar unlocks lands on the float unopposed.

## Foundation and overhang

The team-controlled overhang is roughly **2.5B SEI**, and it sits in three readable pools: the ecosystem reserve (the largest single allocation at 48% of genesis, the same pool that funds staking rewards), the Sei Foundation treasury (9% of genesis), and the unvested remainder of the team and investor tranches. On-chain the picture is consistent — the chain's bank supply is about **9.2B SEI** against a **6.73B** circulating classification, so roughly **2.5B** is minted-but-locked, with the rest of the **10B** cap still unreleased. All of it releases on the published calendar; none is booked as active sell pressure until it actually fires. If any of these pools distributes off-schedule between refreshes, that outflow enters Sell #3 at the next refresh.

## How SEI compares to other capped Layer 1 chains

Sei belongs to the family of **hard-capped, pre-allocated Layer 1s** whose inflation is entirely a vesting phenomenon — closest in shape to **Aptos** and **Sui**, which also launched with fixed allocations that unlock on multi-year calendars. Like those chains, Sei's headline dilution comes from the unlock schedule, not from block rewards. The key difference is the offset: Aptos, after its 2026 overhaul, burns 100% of its base fee, giving it at least a small deflationary lever that scales with usage; Sei has **no burn at all**, so nothing counteracts the unlock.

That separates Sei sharply from a chain like **Ethereum**, where fee burn can turn net supply negative in busy periods, and from exchange tokens that run structural quarterly buybacks. Against an uncapped continuous-emission chain, Sei looks better on the far horizon — its **10B** cap is a real ceiling and the mint is genuinely off — but on the **trailing and forward 90-day window that the framework measures**, a capped token with a heavy unlock calendar and no burn reads more inflationary than a low-emission chain that at least destroys some of what it makes. The cap protects the endgame; it does nothing for the next quarter.

## What to watch in the next 90 days

First, the **circulating-supply feed**: it has been frozen at 6.733B since **Mar 22 2026**, and whenever the market data providers re-sync it upward toward the true float, the monitor reading will jump and the monitor-gap flag will close on its own. Second, the **daily vesting drip** — the team and investor calendar runs continuously, so the ~360M-per-90-day pace holds unless a tranche completes; watch for the point where the four-plus-year team and investor vest tails off. Third, any **governance move on fee burn**: Sei introducing even a partial base-fee burn would be the single biggest change to this reading, since the buy side is currently empty. Fourth, any **Foundation or ecosystem-reserve deployment** announced outside the normal calendar, which would move Sell #3 off zero.

## Summary

The MrNasdog Pressure Framework reads Sei as **structurally inflationary**, about **+5.36%** over the next 90 days, driven almost entirely by **318.3M SEI** of team and investor vesting plus **42.5M** of reserve-funded staking rewards, with **no buyback and no fee burn** to offset any of it. The supply monitor reads flat only because its circulating feed has been frozen at **6.733B** since **Mar 22 2026**; the framework books the real unlock the frozen feed misses, which is why this build ships a monitor-gap flag. The key risk is simple — a heavy unlock calendar meeting an empty buy side — and the one real ceiling is the **10B** hard cap, which bounds the endgame but not the next quarter.

*MrNasdog Pressure Framework analysis of SEI, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 9 2026.*

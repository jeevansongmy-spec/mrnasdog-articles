---
title:         "BORG Inflation Analysis · June 2026 · Mixed flows, supply roughly steady"
description:   "BORG is a hard-capped exchange token with no emission; fee-funded buybacks and a ~0.5M quarterly burn give −0.05% net (monitor −0.06%). Mildly deflationary."
canonical_url: "https://mrnasdog.com/research/borg/inflation"
tags:          ["crypto", "borg", "swissborg", "exchange"]
published:     true
---

*Originally published at [mrnasdog.com/research/borg/inflation](https://mrnasdog.com/research/borg/inflation).*

SwissBorg's BORG (formerly CHSB) is a hard-capped exchange token with no emission: every coin was minted at genesis, so supply can only fall. The Pressure Framework books **zero new BORG** on the sell side and a projected **~0.5M BORG** quarterly burn on the buy side, for a net of **−0.05% over 90 days** against a monitor reading of **−0.06%** — a fixed supply nudged gently lower by burns.

## The verdict, in one paragraph

For the 90-day window the framework reads **BORG at −0.05% net** — mildly deflationary, driven entirely by the next quarterly community-voted burn. The inflation monitor reads **−0.06%** over the same window, a gap of just **0.01 percentage points**, far inside the 0.5-point tolerance, so no monitor-gap chip is raised. BORG is a fixed-supply exchange token: there is no protocol inflation, no vesting cliff, and no Foundation deploy, so the only supply flow is the burn, which slowly grinds the circulating count down.

## Sell pressure: where new BORG comes from

New BORG comes from nowhere. **Protocol inflation** is zero — the 1-billion BORG cap was minted at the 2017 genesis and fully distributed, and there is no emission, no staking-reward issuance, and no active mint function, so the protocol cannot create more supply. **Vesting unlocks** are zero — there is no team or investor cliff schedule minting new supply; the roughly 407M BORG shown as "locked" on the SwissBorg dashboard are voluntary user vote-locks taken to boost cashback rank, already counted inside circulating, not a scheduled team release. **Foundation and unscheduled unlocks** are zero — no discretionary treasury deploy was observed in the window. **Bankruptcy** is zero — no estate distributes BORG. The entire sell column is structurally empty.

## Buy pressure: where new BORG goes

The buy side carries the only real supply flow. **Programmatic buyback** books zero — not because buybacks do not happen, but because of where the BORG goes. The Paid-to-Trade program converts exchange fees into USDC and buys BORG on the open market every week, but that BORG is handed straight back to traders as auto-locked cashback, so it recirculates rather than being destroyed or stockpiled in a growing treasury. It is real demand with a net-zero effect on the supply count, so the framework notes it and books it at zero. **Protocol fee burn** is the live row: each quarter, Premium guardians vote a portion of the buyback ("Protect") pool to be burned on-chain. Recent burns ran **500K on Jun 15 2026**, 400K on Dec 2 2025, and 350K on Oct 1 2025 — a steady ~0.35–0.5M-per-quarter cadence. The next burn (~Sep 2026) falls inside the window, so the framework projects **~0.5M BORG** removed. **Foundation buy** is zero — there is no separate accumulation programme beyond the fee-funded buyback. **New long-term lock** is zero as a booked row — users voluntarily vote-lock BORG for cashback rank, but that is demand-side holder behaviour with no protocol-enforced quantum, so it is monitored, not booked.

## Foundation and overhang

BORG carries two tracked team-controlled overhangs, neither of which is a market-sell risk. The first is the **buyback ("Protect") pool** — roughly 5.64M BORG bought back from fees and held pending the quarterly guardian vote; its destination is a burn or an ecosystem allocation, not a market dump, and it is the pool that feeds the burn row above. The second is the **~407M of voluntary user vote-locks**, which are holder-owned, already inside circulating, and subject to a 30-day cooldown before withdrawal. Neither is a Foundation treasury that could surprise the market with a discretionary sell. The trigger line is simple: if the Protect pool's balance falls between refreshes toward an outflow that is not a burn, that outflow would enter Sell #3 at the next refresh — but every observed movement so far has been a burn, which is a buy-side, supply-reducing event.

## How BORG compares to other exchange tokens with buybacks

BORG belongs to the exchange-token class whose value loop is "fees fund buybacks and burns," the model BNB popularised with its quarterly auto-burn and that exchange tokens like OKB and KCS run in their own forms. Against BNB's burn — which targets a fixed percentage of supply on a published schedule until a hard floor — BORG's burn is smaller, discretionary, and governance-voted each quarter, so its deflation is gentler and less mechanical. The defining difference from an emission-driven L1 token is direction: an uncapped chain like Solana or a DEX token like Aerodrome mints new supply continuously and is structurally inflationary, whereas BORG cannot mint at all and can only shrink.

What makes BORG distinctive within the buyback class is the cashback recirculation. Most exchange-token buybacks either burn the bought tokens outright or escrow them; SwissBorg instead returns the bought BORG to active traders as locked cashback, which is why the framework separates the buyback (net-zero, recirculating) from the burn (the genuine supply reducer). The result is a token that is barely deflationary by the numbers — about −0.05% per 90 days — but whose fixed cap and steady burn cadence mean it never inflates, which is the structural opposite of most utility tokens.

## What to watch in the next 90 days

Three things move the reading. First, the **quarterly Protect & Choose vote** (~Sep 2026) — guardians decide how much of the buyback pool is burned versus re-allocated; a larger burn deepens the deflation, a re-allocation vote shrinks it toward flat. Second, the **exchange-fee run-rate** — buybacks and the pool that funds burns scale with SwissBorg's trading volume, so a quieter quarter means a smaller pool and a smaller next burn. Third, **vote-lock behaviour** — the 30-day cooldown introduced Feb 25 2026 and the cashback ranks keep a large share of supply locked, and any shift in that locked share changes how much BORG sits on the active float even though it does not change total supply.

## Summary

SwissBorg's BORG is a hard-capped exchange token with no emission, no vesting, and no Foundation deploy — the entire sell column is zero, and the only supply flow is the quarterly community-voted burn of roughly **0.5M BORG**. That gives a framework reading of **−0.05% net** over 90 days against a monitor reading of **−0.06%**, a 0.01-point gap with no chip. The key risk is not inflation, which is structurally impossible, but the size of each quarterly burn, which depends on trading volume and a guardian vote. BORG is mildly, deliberately deflationary against a fixed 1-billion ceiling.

*MrNasdog Pressure Framework analysis of BORG, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 21, 2026.*

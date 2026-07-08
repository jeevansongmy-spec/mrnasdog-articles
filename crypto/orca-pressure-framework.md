---
title: "ORCA Inflation Analysis · July 2026 · Supply shrinking, buyback the only mover"
description: "A MrNasdog Pressure Framework read of Orca (ORCA): no protocol inflation, vesting complete, a fee-funded DAO buyback of ~0.40M/90d. Framework −0.66% net; monitor −0.41% — clean."
canonical_url: "https://mrnasdog.com/research/orca/inflation"
tags: ["crypto", "orca", "solana", "dex"]
published: true
---

> Originally published at **[mrnasdog.com/research/orca/inflation](https://mrnasdog.com/research/orca/inflation)** by MrNasdog.

ORCA is a **fixed-supply** Solana DEX governance token — supply sits static near **75M** on-chain, all vesting ended in 2024, and the protocol mints nothing. The only active force is a DAO buyback that spends **30% of protocol fees** plus staked-SOL yield to take about **0.40M ORCA** off the open market each 90 days, leaving the Pressure Framework at roughly **−0.66% net**. Our supply monitor reads **−0.41%** over the same window, a gap inside tolerance, so the read ships with no monitor-gap chip.

## The verdict, in one paragraph

For the 90-day window ending July 8 2026, the MrNasdog Pressure Framework reads **ORCA at about −0.66% net** — mildly deflationary. There is no sell pressure at all: ORCA is a fixed-supply token, so the Orca protocol issues no new coins, and every original team, investor and treasury allocation finished vesting back in 2024. The only mover is the buy side — a 24-month DAO buyback funded by **30% of protocol fees** and the yield on roughly **55,000 staked SOL**. Our supply monitor reads the realized last-90-day change at **−0.41%**, a gap of about **0.25 percentage points** — inside the 0.5-point tolerance, so ORCA ships **clean, with no monitor-gap chip**. The small gap is simply the share of the buyback that recycles back to xORCA stakers rather than being burned. ORCA is **structurally non-inflationary**, with a fee-funded buyback slowly tightening the float.

## Sell pressure: where new ORCA comes from

The short answer is that new ORCA does not come from anywhere. Sell #1 — protocol inflation — is **zero**. The ORCA mint on Solana reads a total supply held static at about **75M**, with no block emission and no staking-reward issuance adding coins. The DAO still holds mint keys up to the **100M cap**, leaving roughly **25M** unminted, but it has issued nothing — so we tag the row watched rather than permanent, and book it at zero.

Sell #2 — vesting unlocks — is also **zero**: the ORCA team, private-sale and advisory allocations followed a multi-year vesting schedule that finished in **2024**, so no dated cliff hits the market in this window. Sell #3 — Foundation and unscheduled unlocks — is zero as a flow. About **14M ORCA** sits non-circulating in the DAO treasury, and the **25M** unminted headroom is a second overhang, but neither is a vesting release; any movement is a discretionary governance decision, and none is dated inside the window. We carry both at zero and keep them monitored. Sell #4 — long-term locked or bankruptcy — is zero, with no estate or court distribution applying to ORCA.

## Buy pressure: where new ORCA goes

Buy #1 — programmatic buyback — is the only active force on the page, at about **0.40M ORCA** bought off the open market over 90 days. The Orca DAO runs a 24-month treasury program, approved in August 2025, that spends **30% of protocol fees** plus the staking yield on roughly **55,000 SOL** buying ORCA on the open market every month; in January 2026 the Council **raised the xORCA-staker fee share from 20% to 40%**. Repurchased ORCA is held in the DAO treasury multisig and then either burned, paid to xORCA stakers as rewards, or used for ecosystem grants. Because a chunk of it is paid back to stakers, the net float reduction is a little smaller than the gross buy — which is exactly the 0.25-point gap between the framework and our supply monitor.

Buy #2 — protocol fee burn — is **zero**: Orca has no automatic per-transaction burn, so no ORCA is destroyed on every trade. Any burning of ORCA is a discretionary use of the buyback stack, already folded into Buy #1, not a separate recurring flow. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero, with no discretionary open-market buying outside the published buyback program and no new escrow announced in the window; xORCA staking is liquid and does not count as a lock.

## Foundation and overhang

ORCA has no vesting overhang left — the schedule is done. What it has instead are two governed reserves. The first is the DAO Token Treasury, holding roughly **14M ORCA** non-circulating, which historically funded grants and the buyback program. The second is the **25M** of unminted supply under an active mint authority — capacity that exists but has stayed idle, with total supply flat near 75M. Both are tracked team-controlled overhangs rather than scheduled flows. None of them is on a fixed calendar, so the framework books no discretionary release, and re-checks the quarterly buyback reports, the treasury multisig balance, and the on-chain mint supply on a roughly bi-weekly walk. If the treasury balance falls faster than a known grant, or the mint supply rises, that outflow enters Sell #3 at the next refresh.

## How ORCA compares to other DEX governance tokens

ORCA belongs to the class of **fixed-supply DEX governance tokens** — closer to a capped, no-emission asset than to an inflationary proof-of-stake chain. Unlike a Solana or an L1 that mints staking rewards every block, ORCA issues nothing; unlike a token still bleeding through a multi-year unlock, its vesting is complete. That puts the entire inflation question on the buy side: the only thing moving net supply is what the Orca DAO chooses to do with fee revenue.

Against peers, ORCA reads cleaner than most. Many exchange and DEX tokens pair real fee revenue with a buyback but still carry an unlock tail that offsets it; ORCA has the buyback without the tail. The contrast worth drawing is with tokens whose buyback is a pure burn — those go more firmly net-deflationary, because every repurchased coin is destroyed. ORCA's buyback splits between burn, staker rewards and grants, so its supply effect is gentler: it trims the open-market float rather than erasing supply outright. For an inflation lens, that leaves ORCA reading mildly deflationary — no dilution to fight, and a fee-funded buyback nudging supply down.

## What to watch in the next 90 days

Watch the quarterly buyback reports — the share of protocol fees going to buybacks (now paired with a raised 40% xORCA fee split) and Orca's trading volume together decide how much ORCA leaves the market each month. Watch the disposition mix: any governance vote that shifts more of the buyback stack from staker rewards toward outright burns would tip ORCA from mildly to firmly deflationary. Watch the DAO treasury and the idle mint authority, the two sources that could add float — and the only things that would push Sell #3 above zero. And expect the framework to keep tracking our supply monitor closely, because with no mint and no unlocks, the realized and modeled numbers move together.

## Summary

ORCA is a fixed-supply Solana DEX governance token with no protocol inflation and no remaining vesting, its supply held static near 75M on-chain under a 100M cap. The only active force is a 24-month DAO buyback that spends 30% of protocol fees plus staked-SOL yield to take roughly 0.40M ORCA off the open market over 90 days. That leaves the framework at about −0.66% net, against our supply monitor's −0.41% realized read — a 0.25-point gap inside tolerance, so the page ships clean. ORCA stays mildly deflationary, with the buyback the only number that moves supply and a governed treasury the only thing that could change that.

*MrNasdog Pressure Framework analysis of Orca (ORCA), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 8, 2026.*

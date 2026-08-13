---
title:         "SOL Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description:   "SOL runs +0.97% net new supply over 90 days: 3.70% staking issuance against a 58.5K SOL burn, while 3.95M SOL of stake lockups re-lock instead of selling."
canonical_url: "https://mrnasdog.com/research/sol/inflation"
tags:          ["crypto", "sol", "solana", "layer1"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/sol/inflation](https://mrnasdog.com/research/sol/inflation)*

# SOL Inflation Analysis · August 2026 · Supply growing, projected to keep growing

Solana (SOL) added **+0.97%** to its tradable supply over the last 90 days and is projected to add **+0.95%** over the next 90 — real growth, but under 1% a quarter and falling. The whole of it is staking issuance: **5.73M SOL** minted on a disinflation curve that has already walked the mint rate down from 8% at launch to **3.70%** a year, against a base-fee burn of only **58.5K SOL**. The lockup calendar looks scarier than it is — **3.95M SOL** of Solana stake lockups expire in the next 90 days, but the locked pool has been growing, not draining, so none of it reached the market this window.

## The verdict, in one paragraph

Over the trailing 90 days the MrNasdog Pressure Framework reads Solana at **+0.97%** net new supply: **5.73M SOL** of staking issuance minus a **58.5K SOL** base-fee burn, divided by a circulating supply of **582.6M SOL**. The independent supply monitor reads **+0.75%** for the same window, a gap of just **0.23** percentage points — inside the framework's 0.5pp tolerance, so no data-conflict chip is raised on the SOL overview. The small residual is itself explained by the mechanism: Solana mints against total supply of **632.1M SOL**, and part of every epoch's issuance lands in stake accounts that sit outside the tradable float. The label for SOL is a **decaying-issuance Layer-1 with a negligible burn** — inflationary by design, but with the inflation visibly and mechanically shrinking year after year.

## Sell pressure: where new SOL comes from

Sell pressure on Solana is one row and one row only. Protocol inflation contributed **5.73M SOL** over 90 days. Solana mints new SOL every epoch and pays all of it to validators and their delegators — the Foundation's share of issuance reads zero on-chain. The mint rate follows the curve Solana launched with: 8.00% to start, stepping down 15% every protocol year, heading to a permanent 1.50% floor. It read **3.85%** at the start of this window and **3.70%** today, and it will read roughly **3.55%** in 90 days' time. That decay is the single most important fact about SOL inflation: without any governance action at all, the sell row shrinks a little every quarter.

The vesting-unlock row is zero, and that is the finding that most often surprises people reading a SOL unlock tracker. Solana's locked stake is a readable on-chain escrow, so the framework reads the balance at both ends of the window rather than trusting the calendar. The calendar says **3.95M SOL** of lockups expire between **Aug 13 2026** and **Nov 11 2026**, including an **875K SOL** cliff on **Aug 30 2026**. The escrow says something else: the non-circulating pool *grew* by about **1.32M SOL** across the last 90 days, from roughly 48.2M to **49.5M**. Expiring estate stake is re-accumulating in reserve accounts instead of being sold, so the realised release to the market was zero. Released beats scheduled, every time.

Foundation and unscheduled unlocks are also zero. There are two tracked overhangs — **29.82M SOL** in reserve stake accounts carrying no lockup at all, and **19.70M SOL** still under an on-chain lockup running into early 2028 — but neither released this window. The bankruptcy row is zero for the same reason: the estate's locked stake is the same pool already measured, and one roughly **202K SOL** estate stake that came out of lockup in **Aug 2026** was more than offset by the pool's overall growth.

## Buy pressure: where new SOL goes

Solana has almost no buy side, and the framework does not pretend otherwise. The programmatic-buyback row is zero and always will be under current mechanics: staking rewards on Solana are minted fresh, never purchased on the open market, so there is no contract quietly taking SOL out of circulation.

The protocol fee burn is the only real buy row, at **58.5K SOL** over 90 days. Solana destroys half of every base transaction fee — 5,000 lamports per signature, split evenly between the burn and the block leader. Priority fees and validator tips, which are the large majority of what a busy Solana block actually earns, are paid entirely to the leader and never burned. At roughly **650 SOL** a day, the burn offsets about 1% of issuance. It is a rounding error against a 5.73M mint, and naming it honestly is more useful than dressing it up.

Foundation buying is zero — no open-market SOL purchase was disclosed or observed in this window — and the new-long-term-lock row is zero too. The locked pool did grow, but it grew from stake re-accumulating rather than from any announced lockup programme with a stated size, so the framework carries that growth as an overhang note rather than crediting it as a buy.

## Foundation and overhang

Solana carries **49.52M SOL** outside the tradable float — **7.8%** of the 632.1M that exists. It splits into two pieces the framework watches separately. The first is **29.82M SOL** of delegated stake in reserve accounts with no lockup at all: nothing on-chain restrains it, only its classification keeps it out of the float, and it is currently the destination of expiring estate stake. The second is **19.70M SOL** still carrying a future lockup, on a calendar that releases roughly 0.85M to 1.35M SOL a month and finishes in **Mar 2028**.

Both are read straight from the chain on every rebuild, so the tripwire is simple: if either pool's balance falls between refreshes, that outflow enters the Foundation and unscheduled-unlocks row at the next refresh. Right now the pools are moving the other way. That is the whole reason SOL's framework reading is under 1% while a Solana unlock calendar read literally would put it near 1.7%.

## How SOL compares to other uncapped Layer-1 chains

Solana has no supply cap, which puts it in a different structural class from Bitcoin or BNB. A halving chain with a hard cap converges on zero new issuance by arithmetic; SOL converges on a permanent **1.50%** floor instead. That floor is the honest ceiling on how good SOL inflation can ever get without governance changing the curve — capped chains can eventually print nothing, Solana will always print something.

Against its true peers — the uncapped, continuous-emission smart-contract Layer-1s — Solana sits in the middle. Ethereum pairs a much smaller issuance with a base-fee burn large enough to flip net supply negative in busy months; Solana's burn is roughly 1% of its issuance, so no amount of Solana activity currently makes SOL deflationary. What Solana has that most uncapped chains do not is a *dated, mechanical* decay: the 15%-a-year taper is protocol code, not a promise, and it has been walking the rate down on schedule since launch. Chains that emit at a flat rate offer no such glide path.

The other structural difference is where the unlocks live. Many Layer-1s hold team and investor allocations in off-chain custody where the framework can only read a published vesting table. Solana's sit in on-chain stake accounts with a lockup timestamp anyone can query, which is why the released-versus-scheduled divergence is even visible here. It is a transparency advantage, and it currently works in SOL's favour.

## What to watch in the next 90 days

The formal governance vote on SIMD-0550 and SIMD-0553 closes on **Aug 18 2026**; SIMD-0550 would double the Solana disinflation taper from 15% to 30% a year and pull the 1.5% floor forward from 2032 to 2029, and SIMD-0553 would replace part of the flat fee with a resource fee burned in full, taking the burn from about 650 SOL a day to 7,500–9,000. Neither has a feature gate active, so neither is in this ledger — but a yes on both would cut the sell row and multiply the buy row at once.

Second, the **875K SOL** lockup cliff on **Aug 30 2026** is the largest single scheduled release in the window and the cleanest test of whether the re-locking pattern holds. Third, the monthly tranches on **Sep 7 2026**, **Oct 7 2026** and **Nov 7 2026** each release roughly **633K SOL**. Fourth, the non-circulating balance itself is the single number that decides the vesting row: if it turns down, SOL's reading moves up quickly. Fifth, SIMD-0123 block revenue distribution is code-complete but not live; it changes who receives fees, not how many SOL exist, so it will not move this ledger when it ships.

## Summary

Solana is inflationary by design and will stay that way, but the MrNasdog Pressure Framework reads SOL at **+0.97%** net new supply over the last 90 days and **+0.95%** projected for the next — under 1% a quarter, entirely from staking issuance, and mechanically shrinking as the 15%-a-year taper walks the mint rate toward its 1.50% floor. The key risk is not the mint but the **49.52M SOL** sitting outside the float: the vesting row is zero only because that pool grew by **1.32M SOL** this window instead of releasing the **3.95M SOL** its calendar allows, and that behaviour can reverse without notice. The ceiling on SOL inflation is the 1.50% floor the curve is heading for — unless the **Aug 18 2026** vote lowers it, Solana will always be printing something, and the base-fee burn is far too small to offset it.

---

*MrNasdog Pressure Framework analysis of SOL, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 13 2026.*

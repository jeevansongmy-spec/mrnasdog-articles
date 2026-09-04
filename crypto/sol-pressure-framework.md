---
title:         "SOL Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description:   "SOL runs +1.27% net new supply over 90 days: 3.66% staking issuance plus 2.29M SOL of realised lockup and estate unlocks, against a burn of only 74.9K SOL."
canonical_url: "https://mrnasdog.com/research/sol/inflation"
tags:          ["crypto", "sol", "solana", "layer1"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/sol/inflation](https://mrnasdog.com/research/sol/inflation)*

# SOL Inflation Analysis · September 2026 · Supply growing, projected to keep growing

Solana runs two supply stories at once, and only one of them is slowing. Staking issuance added **5.24M SOL** over the last 90 days at a rate that decayed from **3.81%** to **3.66%** a year, while Solana's monthly stake-lockup ladders released another **2.29M SOL** that genuinely drained out of escrow. Against that, the only mechanism removing SOL is the base-fee burn, and it destroyed just **74.9K SOL** — under **2%** of what was minted. Net **+1.27%** of circulating supply reached the market over 90 days, against **+0.77%** on the inflation monitor, and there is **no supply cap** anywhere in the Solana design.

## The verdict, in one paragraph

The framework reads Solana at **+1.27%** net new supply over the trailing 90 days and **+1.22%** projected over the next 90 — sell pressure of **7.53M SOL** against buy pressure of **74.9K SOL**, on a circulating base of **585.4M SOL**. The inflation monitor reads **+0.77%** for the same window, a gap of **0.50 percentage points**, which crosses the framework's tolerance and ships a data-conflict chip on the overview card. The gap is a classification effect, not a missing flow: Solana's circulating classifier reclassifies a stake lockup the instant its timestamp passes, whether or not the SOL moves, while this ledger books only what actually drained. Solana is **structurally inflationary on a decaying curve** — issuance falls every epoch, but nothing meaningful is being destroyed underneath it.

## Sell pressure: where new SOL comes from

Protocol inflation is the whole engine. Solana mints new SOL every epoch against total supply and pays all of it to validators and delegators — the inflation governor read on-chain still returns the as-launched curve: an **8%** start, a **15%** annual taper and a **1.5%** terminal floor, with a foundation share of zero. Over the window the annual rate fell from **3.81%** to **3.66%**, and integrating that decay across the realised protocol-year gives **5.24M SOL** of new issuance. The forward column is **4.91M SOL**, lower purely because the curve keeps decaying.

One thing that did **not** change the mint is speed. Solana cut its slot time twice inside this window — to **350ms** on Aug 21 2026 and to **300ms** on Aug 28 2026 — and the measured interval fell from **0.417** seconds to **0.317** seconds a slot. Faster slots would normally mean more issuance periods per year, but the upgrade raises the protocol's own year counter by exactly the inverse ratio, so wall-clock issuance is unchanged by design. An on-chain reward read at epoch 1027 confirms it: the observed per-epoch payout matches the re-scaled constant to **0.29%**, while the un-rescaled one would have over-forecast issuance by **17%**.

Vesting unlocks contributed **1.69M SOL**. Solana runs a monthly stake-lockup ladder that releases one tranche on the 7th of every month, a full tranche being 34 stake accounts holding about **635K SOL**. Read account by account rather than in aggregate, the calendar released **1.91M SOL** across Jun, Jul and Aug 2026 and only **220K** is still sitting in those accounts, so **1.69M** actually left — an **88%** realisation rate. A second escrow behaves the opposite way: it released a **1.38M SOL** cliff on Aug 1 2026 and an **875K SOL** cliff on Aug 30 2026, and neither has moved a lamport, so neither is booked as sell pressure here.

Foundation and unscheduled unlocks are **zero** — no public evidence of release in the window. The Solana Foundation's discounted sales to listed treasury vehicles are a real mechanism, but every deal carrying a dated size belongs to 2025, and nothing observable left the Foundation's stake accounts in this window. Long-term locked and bankruptcy supply contributed **607K SOL**: the FTX and Alameda bankruptcy estate holds its own ladder releasing about **202K SOL** on the 11th of every month, and all three in-window tranches drained essentially to the lamport — the Jun 11 2026 account was closed outright, and outside reporting puts the Aug 11 2026 release at **201,741 SOL** forwarded to a custody account for liquidation.

## Buy pressure: where new SOL goes

There is no programmatic buyback on Solana and there is no mechanism that could fund one — staking rewards are minted fresh rather than bought, and the protocol keeps no revenue pool. That row is **zero**, and it is the single biggest structural difference between Solana and the deflationary tokens it is often compared with.

The protocol fee burn is the only real buy-side mechanism, and it is small. Solana charges a fixed **5,000**-lamport fee per signature and destroys exactly half of it; the other half goes to the block leader. Reading **120** whole blocks spread across two days gives **146,727** signatures and **832 SOL** burned a day, or **74.9K SOL** over 90 days. The rest of what users pay is priority fees — **72%** of all fee revenue — and every lamport of that goes to the block producer rather than being destroyed. A proposal to burn far more, lifting the daily burn toward **9,000 SOL**, is drafted but has no feature gate and is not booked.

Foundation buying is **zero**: the Solana Foundation is a net seller of SOL to treasury vehicles, not a buyer of it. New long-term locks are **zero** as well. About **437M SOL** is staked, which is a genuine lock in the sense that stake accounts only unbond at an epoch boundary, but no new lockup programme was created in the window, and staking rewards are new coins rather than coins taken off the market. Listed treasury companies keep accumulating — one alone holds over **7.5M SOL** — but corporate demand is market demand, not a protocol lock, and the framework does not book it.

## Foundation and overhang

Solana's team-controlled overhang is large and fully readable. Non-circulating supply stands at **48.1M SOL** across **3,285** accounts. The biggest block is **29.3M SOL** in **2,355** stake accounts that carry no lockup at all and are held out of the float by classification alone — **27.1M** of it under a single withdraw authority. A further **18.8M SOL** remains under live lockup across **796** accounts, releasing monthly into 2028, of which **2.63M** belongs to the bankruptcy-estate ladder running through Sep 2027. Alongside those sits a third pile the classifier no longer counts: roughly **6.6M SOL** whose lockups have already expired but which has never been withdrawn, including the two dormant cliffs described above.

All four escrow programmes are refreshed by direct chain reads on every rebuild, and the Foundation's discounted-sale channel is refreshed by a walk of its public announcements. If any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh — and on the evidence of this window, the difference between an escrow that empties and one that sits untouched is the difference between **1.69M SOL** of real sell pressure and **2.25M SOL** of paper unlocks that never reached anyone.

## How SOL compares to other uncapped proof-of-stake Layer-1 chains

Solana belongs to the uncapped continuous-emission class, and inside that class its distinguishing feature is a hard-coded disinflation curve rather than a governance-set rate. Chains that mint at a flat percentage never get cheaper; Solana's falls **15%** a year on its own, and a governance vote that passed on Aug 28 2026 with **67.00%** of participating stake would double that taper — pulling the terminal **1.5%** floor forward by roughly three years and preventing an estimated **18.9M SOL** of issuance. It is not booked in either column, because the on-chain inflation governor still returns the **15%** taper and no activation epoch exists.

Against fee-burning smart-contract platforms, the contrast is starker. A chain that burns its base fee at scale can offset or invert its own issuance; Solana's burn covers under **2%** of the mint, because only half of a fixed signature fee is destroyed while the priority-fee majority is paid out. That is a design choice, not a demand problem — Solana's protocol fees annualise to roughly **0.38%** of market cap, an order of magnitude above the quiet enterprise Layer-1s in the same catalog, and the busiest smart-contract chain in it. The supply is inflationary despite heavy usage, not because of light usage.

And against hard-capped chains the difference is categorical. Solana has no maximum supply and total supply was observed rising through the window. Its float is also unusually calendar-driven for a large Layer-1: monthly lockup ladders plus a bankruptcy estate keep adding supply on fixed dates independent of the mint, which is closer to a vesting-era token than to a mature capped asset.

## What to watch in the next 90 days

Four dated items move this reading. The monthly stake-lockup tranches land on **Sep 7 2026**, **Oct 7 2026** and **Nov 7 2026**, each about **635K SOL** across 34 accounts, and the ladder's **88%** realisation rate is what the forward column assumes. The bankruptcy-estate tranches land on the 11th of each of those months at about **202K SOL**, and have drained in full every time. A dormant escrow releases **325K SOL** of cliffs between **Sep 13 2026** and **Sep 17 2026**; it has never drawn, so it is watched rather than booked, and a first withdrawal there would raise Sell #2 immediately.

The two governance items are the bigger swing. If the doubled disinflation taper gets a feature gate and an activation epoch, the forward issuance column falls; if the resource-fee burn proposal is revived and activated, the burn row could rise by an order of magnitude. Neither has an activation height today, so both stay out of the ledger and stay on the watch list.

## Summary

Solana is inflationary by design and will stay that way for years. The framework reads **+1.27%** net new supply over the trailing 90 days and **+1.22%** forward, driven by **5.24M SOL** of staking issuance and **2.29M SOL** of stake-lockup and bankruptcy-estate unlocks that genuinely reached the market, against a base-fee burn of only **74.9K SOL**. The key risk is that the calendar, not the mint, controls the surprises: **18.8M SOL** remains under live lockup and another **29.3M SOL** sits unlocked-but-unclassified behind a single withdraw authority, and any of it can move without a vote. There is no ceiling — Solana has no maximum supply, and the only thing capping issuance is a disinflation curve that will take until the 2030s to reach its **1.5%** floor unless the passed governance vote is finally switched on.

---

*MrNasdog Pressure Framework analysis of SOL, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 4 2026.*

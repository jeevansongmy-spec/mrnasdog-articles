---
title:         "STX Inflation Analysis · August 2026 · The chain deleted its own halving schedule"
description:   "On Jul 30 2026 Stacks removed its emission reduction schedule and stepped up both of its protocol mints at once — combined issuance went 975 to 2,140 STX per Bitcoin block. Framework +0.68% rising to +1.17%, monitor +0.66%."
canonical_url: "https://mrnasdog.com/research/stx/inflation"
tags:          ["crypto", "stx", "stacks", "bitcoin"]
published:     true
---

*Originally published at [mrnasdog.com/research/stx/inflation](https://mrnasdog.com/research/stx/inflation)*

Stacks STX runs **two separate protocol mints** — a mining coinbase and an ecosystem endowment emission — and both are paid on every Bitcoin block. Together they created **12.72M STX** over the last 90 days against **1.86B circulating**, so the Pressure Framework reads **+0.68% net**, matching our supply monitor's **+0.66%** within **0.02 percentage points**. Nothing offsets it: Stacks has no STX buyback, no STX fee burn, and its stacking mechanism pays rewards in bitcoin rather than STX. On **Jul 30 2026** both mints stepped up at once and the network deleted its remaining reduction schedule, so the forward reading rises to **+1.17%** and STX no longer has a supply cap.

## The verdict, in one paragraph

For the 90-day window ending **Aug 10 2026**, the Pressure Framework reads **STX at +0.68% net**. Sell pressure is **12.72M STX** across two rows — **6.40M** of Stacks mining coinbase and **6.32M** of Stacks Endowment emission — and every buy row is **zero**, against a circulating base of **1.86B STX**. Our supply monitor reads the realised change at **+0.66%**, a gap of **0.02 percentage points**, comfortably inside tolerance, so the page ships **no monitor-gap flag**. The chain read and the monitor tell the same story. STX is best characterised as **a Bitcoin layer that removed its own halving schedule and now runs two uncapped mints in parallel with nothing on the buy side**.

## Sell pressure: where new STX comes from

Stacks mining is settled on Bitcoin: miners commit bitcoin, a sortition picks the winner of each Bitcoin block, and the Stacks protocol pays that winner a freshly minted STX coinbase. That coinbase had been cut to 500 STX per Bitcoin block in April 2026 under the older emission schedule. The Jul 30 2026 PoX-5 upgrade reversed the cut — restoring **1,000 STX per Bitcoin block** — and, more consequentially, removed the step-down schedule altogether, so no further halving of the Stacks coinbase is written into the code. Measured on the chain across the window, the mining mint contributed **6.40M STX**.

The second and now larger stream is the Stacks Endowment emission, an additional STX mint paid on every Bitcoin block into the ecosystem treasury on a published five-year schedule. Its per-block amount stepped from **475 STX to 1,140 STX** on **Jul 30 2026**, the same day as the mining change, and it contributed **6.32M STX** over the window. Because that endowment mint is protocol-encoded new supply rather than a release of existing tokens, the framework carries it as its own ledger row rather than folding it into a foundation line.

Taken together, combined issuance went from **975 to 2,140 STX per Bitcoin block** in the middle of the window. That is why the trailing and forward columns are not the same shape: the trailing number stays as measured, while the forward column is re-based on the post-change run rate. Measured after the upgrade, actual issuance is running at about **1,681.68 STX per Bitcoin block** — below the 2,140 nominal, because not every Bitcoin block wins a sortition. Carried across the next 90 days that projects **21.79M STX**, split roughly **10.18M** mining and **11.61M** endowment, which is what lifts the forward reading to **+1.17%**.

The remaining sell rows are all zero, and each for a reason built into the chain. Vesting unlocks are **zero** because the chain reports **100% of STX supply already unlocked** — the original Stacks distribution schedule has fully expired, there is no lock-up contract left, and STX therefore has no unlock calendar and no cliff dates at all. Foundation and unscheduled unlocks are **zero** because, while the endowment's wallets do move STX, those movements are internal transfers of tokens the emission row already counts; booking them again would double-count the same supply. Long-term locked or bankruptcy is **zero** because Stacks has no bankruptcy estate and no trustee distribution schedule.

## Buy pressure: where new STX goes

Every buy row on the STX ledger is **zero**, and the reasons are structural rather than temporary. There is no programmatic buyback: the Stacks Endowment is funded by new issuance, so it is a net seller of STX into ecosystem programmes, and its own treasury disclosures list STX, bitcoin and stablecoins being spent, never bought on the open market.

Protocol fee burn is **zero** because Stacks transaction fees are paid to miners rather than destroyed — the chain has no fee-burn mechanism of any kind. The Jul 30 2026 PoX-5 upgrade actually removed the last burn left in the system, and even that one destroyed bitcoin committed by miners, never STX. Foundation buy is **zero**: no foundation or endowment purchase of STX is disclosed, and with newly minted STX arriving in the treasury every Bitcoin block there is no reason for one.

New long-term lock is the row most readers expect to carry something, because stacking locks a large share of STX. It is still **zero**. Stacking commitments run on rolling two-week reward cycles, the locked STX continues to count as circulating everywhere it is measured, and the rewards are paid in **bitcoin** rather than STX — so stacking neither adds nor removes STX supply. Participation also fell over the window, from about **566M STX** stacked to about **447M**. The new bitcoin-bond product that launched with PoX-5 on Jul 30 2026 does introduce a genuine six-month lock, pairing timelocked bitcoin with committed STX, but no size is committed yet, so it is watched rather than booked.

## Foundation and overhang

Three team-controlled wallets are tracked. The Stacks Endowment's primary mint address, the wallet the protocol emission accrues into, held **45.9M STX** on Aug 10 2026. Its operating multisig, the wallet that actually deploys capital into ecosystem programmes, held **8.4M STX** — it has received about **115M STX** in total and already sent out roughly **107M**, so it runs close to empty by design. A retired predecessor operating wallet has been drained to effectively zero. Together the identified overhang is about **54.4M STX**, or roughly **2.9%** of circulating supply, and both live wallets are read on-chain at every rebuild.

The sweep pattern between them is visible and regular: **17.9M STX** moved from the mint address to the operating multisig on **May 21 2026** and **31.0M STX** on **Jul 2 2026**, following earlier sweeps roughly every five to seven weeks. Those transfers are relocation, not new supply, which is why they sit in the overhang narrative rather than in a sell row. If either wallet's balance falls between refreshes in a way the emission schedule does not explain, that outflow enters Sell #3 at the next refresh.

## How STX compares to other Bitcoin-secured layers

The natural comparison class for Stacks is chains whose security is anchored to Bitcoin, and the mechanism contrast is stark. Bitcoin itself is the archetype of a capped, halving-driven emission: a fixed schedule, a hard 21M ceiling, and no governance path to raise either. Stacks was originally built to rhyme with that model — a coinbase on a halving-style schedule aligned to Bitcoin's own halvings, converging on a supply figure near 1.8B. As of Jul 30 2026 that rhyme is gone. The PoX-5 upgrade removed the reduction schedule outright, which means STX has neither a halving path nor a supply cap, and any future reduction would require a fresh governance vote rather than being pre-committed in code.

Against uncapped continuous-emission layer ones, STX now looks conventional in shape but unusual in structure, because it carries **two** mints instead of one. A typical proof-of-stake layer one mints once, to validators, and often offsets part of that with a fee burn. Stacks mints to miners and, separately, to a treasury, and burns nothing — so its gross issuance and its net issuance are the same number. That absence of any offset is what pushes the forward reading to **+1.17%** even though neither individual mint is extreme by layer-one standards.

The comparison that flatters Stacks is on the staking side. Chains that pay staking rewards in their own token compound their inflation: stakers receive newly minted units, which count as fresh supply. Stacks pays its stackers in **bitcoin**, not STX, so its lock-up mechanism is genuinely inflation-neutral — a real structural advantage that the ledger records as a buy row of zero rather than a hidden sell row. The trade-off is that stacking removes no float either, so it cannot offset the two mints running above it.

## What to watch in the next 90 days

First, the Genesis Bond, billed as the first bitcoin protocol bond on Stacks, is expected in late **Aug 2026**; if it draws meaningful STX into six-month bonded positions it would be the first credible entry in the new-long-term-lock row. Second, the next endowment sweep from the mint address to the operating multisig is due on the observed five-to-seven-week rhythm following **Jul 2 2026** — the size of that sweep signals how fast the treasury intends to deploy. Third, the post-upgrade mining sortition rate is worth re-measuring: the forward projection here uses the conservative observed rate of issuance rather than the nominal 2,140 STX per Bitcoin block, and a rise in miner participation would push realised issuance toward that nominal ceiling. Fourth, the next scheduled endowment step takes the per-block mint to **1,705 STX**, but it does not land until well into 2027, so it is outside this window. Fifth, watch for any governance proposal restoring a reduction schedule — with the old reduction path deleted, a cap or halving can only come back through a new vote.

## Summary

The MrNasdog Pressure Framework reads Stacks (STX) at **+0.68% net supply growth** over the 90 days to Aug 10 2026, against a monitor reading of **+0.66%**, and projects **+1.17%** for the next 90 days. The structural mechanism is two parallel protocol mints paid on every Bitcoin block — a **1,000 STX** mining coinbase and a **1,140 STX** Stacks Endowment emission — against a buy side that is entirely empty, since Stacks has no STX buyback, no STX fee burn, and pays stacking rewards in bitcoin. The key risk is that both mints stepped up on the same day, **Jul 30 2026**, and the PoX-5 upgrade deleted the reduction schedule that would have shrunk the mining reward over time. There is now no cap and no halving path in the code, so the ceiling on STX supply is a governance decision rather than a protocol constraint.

*MrNasdog Pressure Framework analysis of STX, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 10 2026.*

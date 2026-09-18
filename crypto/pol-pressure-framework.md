---
title:         "POL Inflation Analysis · September 2026 · Mixed flows, supply roughly steady"
description:   "Mixed flows, supply roughly steady: POL grows +0.49% per 90 days. Polygon mints 52.2M POL at 2% a year, and its base-fee burn has not destroyed those fees yet."
canonical_url: "https://mrnasdog.com/research/pol/inflation"
tags:          ["crypto", "pol", "polygon", "layer2"]
published:     true
---

> Originally published at **[mrnasdog.com/research/pol/inflation](https://mrnasdog.com/research/pol/inflation)** by MrNasdog.

Polygon adds about **0.49%** to the POL supply every 90 days, and the Pressure Framework reads POL at **+0.49%** over the trailing 90 days and **+0.49%** over the next 90 — a small, steady rise with nothing on the other side of the scale. The whole of it is one mechanism: a **2%** yearly mint that paid **52.2M POL** into the market, half to stakers and half to the Polygon community treasury. The Polygon PoS base-fee burn that most write-ups credit with making POL deflationary has not destroyed those fees yet — they sit parked in two wallets on Polygon — so buy pressure is about **0.97K POL**, and POL has no supply cap.

## The verdict, in one paragraph

Against a circulating base of **10,716.4M POL**, the framework books **52.2M POL** of sell pressure and **0.97K POL** of buy pressure over the trailing 90 days — a net of **+0.49%** — and projects **+0.49%** for the next 90 days, because the POL emission rate did not change inside the window and no vote to change it is scheduled. The inflation monitor reads **+0.50%** for the same window, a gap of **0.01 percentage points**, well inside the framework's 0.5pp tolerance, so the overview page carries no monitor-gap warning. The label for POL is **a low, steady mint with a burn that has not landed yet**: every new coin is accounted for, and almost nothing is being removed.

## Sell pressure: where new POL comes from

Sell #1, protocol inflation, is **52.2M POL**, and it is the whole sell side. The POL token on Ethereum has an emission manager that mints new POL once a day at a rate of **2%** a year, compounding. Half goes to the staking contract that pays Polygon validators and delegators, and half goes to the Polygon community treasury. Across the window there were **90** mints, one a day, and the count of POL in existence rose by exactly the sum of them, with no burn events against it. Every setting of the emission manager read the same at both ends of the window, so the forward reading uses the same rate: **52.46M POL** over the next 90 days. POL has no hard cap. The token contract limits how fast new POL can be minted, but not how much can exist, and a governance vote can change the rate. None has been held.

It matters that the treasury half counts now, not later. The market's circulating figure for POL counts essentially every POL that exists, the treasury included, so a new coin joins the float the moment it is minted. That also explains why Sell #2, vesting unlocks, is **0**: the old MATIC team, investor and foundation schedules ended in 2022, and the move from MATIC to POL is a one-for-one swap. In this window **34.4M POL** left the swap contract while exactly **34.4M MATIC** went in, so the migration added nothing. Sell #3, Foundation and unscheduled unlocks, is **0** for the same reason — anything the treasury spends was already counted when it was minted. Sell #4, long-term locked or bankruptcy, is **0**: POL has no bankruptcy estate and no court-ordered distribution.

## Buy pressure: where new POL goes

Buy #1, programmatic buyback, is **0**. Polygon runs no buyback. A forum proposal from October 2025 to end the 2% mint and buy POL back never reached a vote, and a newer draft, PIP-87, which would use payment fees to buy POL, is still a draft with no purchases shown.

Buy #2, protocol fee burn, is about **0.97K POL**, and this is the row that needs the most care, because Polygon's base-fee burn is widely described as larger than the mint. On Polygon PoS, the base fee of every transaction goes to a 3-of-5 multisig under PIP-82, which pays some of it back as rebates to agent-payment services and forwards the rest to a holding contract set up under PIP-24. In this window about **47.6M POL** of fees moved into those two places: **31.3M** into the holding contract, which now holds **121.6M POL** and has no way to send coins out today, and the rest into the multisig, now at **50.8M POL**. But neither burn surface on the ledger that counts POL moved. The count of POL on Ethereum rose by exactly the mint, and the Ethereum dead address gained **0.3 POL**. PIP-24 itself calls the holding contract temporary and says a real burn on Ethereum needs a future protocol change; that change has not been made, and the contract's admin can still upgrade it. So the fees are parked, not destroyed, and they will count here on the day they are actually burned. The only POL truly gone this window is about **0.97K POL** sent to dead and zero addresses on Polygon PoS, which can never be spent.

Buy #3, Foundation buy, is **0**: the community treasury grew by exactly its share of the mint, to the last decimal, with no purchases. Buy #4, new long-term lock, is **0**, and staking moved the other way — POL staked on Ethereum fell from **3,684.4M** to **3,620.9M**. Staked POL counts as float in any case, so staking would not remove supply here.

## Foundation and overhang

Three pots are watched on every rebuild. The Polygon community treasury holds **93.2M POL**, up from **67.1M** at the start of the window, and it sent nothing out; it pays for grants, and two grant contracts paid out their last **0.85M POL** this window. The fee holding contract on Polygon PoS holds **121.6M POL**, and the fee multisig holds **50.8M POL**; both are read from the chain at every rebuild. Because the market already counts all three as circulating, spending them would not add new supply to this reading — but the fee pots are the difference between a real burn and a parked one, so if the holding contract's or the multisig's balance falls between refreshes without a matching burn on Ethereum, that outflow is recorded against Sell #3 at the next refresh.

## How POL compares to other uncapped proof-of-stake chains

POL sits in the class of uncapped proof-of-stake tokens with a fixed-rate emission. A **2%** yearly mint is low for that class: many Cosmos-style chains pay stakers with emission rates several times higher. A halving chain like Bitcoin sits lower, at under 1% a year since its 2024 halving, and it has a hard cap that POL does not. On the issuance axis alone, POL is modest and predictable.

The comparison that matters is with Ethereum, because Polygon copied Ethereum's fee design. On Ethereum, the base fee is destroyed inside the protocol, so the burn shows up in the supply count the same block it happens. On Polygon PoS, the same base fee is taken from the payer but held in a contract on Polygon, while the POL supply is counted on Ethereum. The mechanism looks the same; the result is not. Until the burned fees are destroyed on Ethereum, POL behaves like a token with a mint and no burn.

Exchange tokens with scheduled burns, like BNB, show the opposite shape: coins are destroyed on a published date and the supply count falls. If Polygon moves the **121.6M POL** in its holding contract to Ethereum and burns it, POL would book a one-time buy larger than two quarters of its mint — the difference between a supply that grows and one that shrinks.

## What to watch in the next 90 days

First, the mint itself, which runs at about **52.46M POL** per 90 days and changes only by a governance vote. Second, the fee holding contract on Polygon PoS — any upgrade that finally burns its **121.6M POL** on Ethereum would flip this page's buy side overnight. Third, the PIP-82 fee program, which ends on **Dec 31 2026** or when its rebate budget runs out; what happens to base fees after that is not yet written. Fourth, PIP-87 and PIP-85, the drafts that would buy POL with payment fees and share priority fees with stakers. Fifth, the community treasury at **93.2M POL**, the one pot with a spender rather than a schedule.

## Summary

The MrNasdog Pressure Framework reads POL at **+0.49%** over the trailing 90 days and **+0.49%** projected forward: mixed flows, supply roughly steady. The structural mechanism is a **2%** yearly mint on Ethereum that paid **52.2M POL** in 90 days, half to stakers and half to the Polygon community treasury, with no vesting and no buyback. The key risk and the key upside are the same place: Polygon PoS base fees, about **47.6M POL** this window, are parked rather than destroyed, so the famous burn does not reduce supply yet. POL has no supply cap, only a limit on how fast it can be minted.

*MrNasdog Pressure Framework analysis of POL, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 18 2026.*

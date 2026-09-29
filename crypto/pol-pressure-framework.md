---
title:         "POL Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "Mixed flows, supply roughly steady: a 100M POL fee burn beat the 52.2M POL mint, so POL fell 0.45% in 90 days. No next burn is dated, so POL is +0.49% next."
canonical_url: "https://mrnasdog.com/research/pol/inflation"
tags:          ["crypto", "pol", "polygon", "layer2"]
published:     true
---

> Originally published at **[mrnasdog.com/research/pol/inflation](https://mrnasdog.com/research/pol/inflation)** by MrNasdog.

The MrNasdog Pressure Framework reads POL, the token of Polygon, at **−0.45% net** over the trailing 90 days and **+0.49%** over the next 90. A fixed 2% yearly mint created **52.23M POL** in the window, and a one-off burn of saved Polygon base fees destroyed **100M POL** on **Sep 23 2026**. With no next burn on the calendar, the forward reading counts only the mint, so POL supply is roughly steady: it shrank this quarter and is set to grow again unless the fee burn repeats.

## The verdict, in one paragraph

Over the 90 days to **Sep 29 2026**, POL supply moved by **−0.45%** of its **10.62B** circulating coins: **52.23M POL** minted against **100M POL** burned. The inflation monitor, which reads the same supply from market data, shows **−0.43%** over the same stretch — a gap of **0.02 percentage points**, well inside the 0.5-point tolerance, so no monitor-gap warning is shown. For the next 90 days the framework projects **+0.49%**, because the mint is scheduled and the burn is not. The cite-able label for POL today is a **steady 2% minter with a lumpy fee burn**.

## Sell pressure: where new POL comes from

Protocol inflation is the only source of new POL. The Polygon emission contract mints once a day at **2% a year**, compounding by the second, and splits each mint evenly: half to the staking contract that pays Polygon validators and their delegators, half to the Polygon Community Treasury. Across the window that meant 90 mints, one a day, and **52,230,063 POL** — exactly the rise in the POL token's total supply on Ethereum, with **26.12M POL** going to each side. Because the rate compounds, the same schedule mints slightly more in the next 90 days: **52.49M POL**.

Vesting unlocks are **zero**. The 10B POL created at launch backed a one-for-one swap from the old MATIC token, and no unlock tracker lists any team, investor or ecosystem tranche still waiting. The swap itself runs out of a fixed pot that still holds **376.59M POL** for late swappers; it trades one existing coin for another and adds nothing.

Foundation and unscheduled unlocks are also **zero**. The Community Treasury sent out nothing this window, and every other Polygon-controlled wallet is already counted as circulating, so moving those coins adds no new supply. The long-term locked or bankruptcy row is **zero** too: Polygon has no estate, no trustee schedule and no unwinding lock.

## Buy pressure: where new POL goes

The protocol fee burn did all the work this window. Every Polygon transaction pays a base fee in POL, and since 2023 those fees have been collected in a contract on the Polygon chain instead of being destroyed. On **Sep 23 2026**, **100M POL** left that collector, crossed the bridge to Ethereum through a new permissionless burn contract and landed at a dead address in a single transfer. That one burn removed almost twice the POL the 2% mint created in the same 90 days, and it is why POL supply fell this quarter.

The next POL burn is the open question. The collector still holds **21.62M POL**, the Polygon team has said about 25M POL is ready and that burns should come quarterly, and anyone can now start one. But no date is set, and one burn is not yet a pattern, so the framework books **zero** fee burn for the next 90 days and will count the next burn when it happens.

The programmatic buyback row is **zero**. A draft Polygon proposal would take money from payment companies and use it to buy POL for stakers and for the burn, and a community proposal to end the 2% mint has sat in discussion since October 2025 without a vote; neither has bought a coin. The Foundation buy row is **zero**, with no purchase announced or visible on-chain. The new long-term lock row is **zero** as well: staked POL still counts as circulating, and the staking contract actually shrank from **3.70B** to **3.55B POL** as more POL left staking than joined.

## Foundation and overhang

Four POL balances controlled by Polygon or its governance are tracked. The Polygon Community Treasury holds **96.35M POL**; it gains half of every mint and sent nothing out this window. On the Polygon chain, the base-fee collector keeps **21.62M POL** after the burn, the fee routing wallet that also pays gas rebates to some payment apps holds **55.61M POL**, and a **27.33M POL** staker share of past priority fees is due to be paid out through staking rewards from Oct 1 2026. The Polygon Foundation's own operating wallets are not published. All of these coins already sit inside the circulating count, so none of them is new supply when spent. Each balance is re-read at every rebuild; if one of them falls between refreshes, the outflow is recorded and the ledger is re-checked at the next refresh.

## How POL compares to other proof-of-stake chains

POL sits between two familiar designs. Like Ethereum, Polygon has no supply cap and pays stakers in newly minted coins, and like Ethereum it takes a base fee from every transaction. The difference is timing: Ethereum destroys its base fee inside every block, so its burn shows up as a smooth flow, day after day, while Polygon saves its base fees and destroys them in large batches. A POL quarter with a burn can shrink supply; a POL quarter without one grows it by the full mint.

That batch style is closer to exchange tokens such as BNB, which burn on a quarterly calendar, but with one structural gap: BNB's burn has fixed dates and a published way to size each burn, while the POL burn has a stated quarterly aim, no set size and no date yet. Against chains with a falling emission schedule, such as Solana, POL's mint is simpler and flat — 2% a year, split half to stakers and half to a treasury — and only a governance vote can lower it.

The treasury half is what sets POL apart from most staking coins. Where Ethereum and Solana pay all new issuance to stakers, POL sends **1% a year** to the Polygon Community Treasury, which grows by about **26M POL** every 90 days and spends only when grants are approved.

## What to watch in the next 90 days

The next POL fee burn: about 25M POL was said to be ready on **Sep 27 2026**, and a burn of that size inside the window would take the next-90-day reading from **+0.49%** to roughly **+0.26%**.

The staker fee payout from **Oct 1 2026** to **Dec 1 2026**: 27.33M POL of saved fees goes to stakers through higher rewards. These are existing coins, so supply does not change, but the payout adds tradable POL in stakers' hands.

The Lugano network upgrade, targeted for **Oct 1 2026**: no change to POL minting or the fee burn has been announced with it, and any such change would re-base the ledger.

Polygon governance: the draft buyback programme funded by payment companies and the proposal to end the 2% mint. Either one reaching a vote would change a row directly.

## Summary

The MrNasdog Pressure Framework reads POL at **−0.45%** over the last 90 days and **+0.49%** over the next 90: a fixed 2% yearly mint of **52.23M POL** per quarter, offset this time by a one-off burn of **100M POL** of saved Polygon base fees. The structural mechanism is a flat, uncapped mint split between stakers and the Community Treasury, against a fee burn that now works but comes in lumps. The key risk is timing: without a second burn, POL supply goes back to growing by the full mint. POL has no supply cap; its supply falls only when saved fees are burned faster than 2% a year is minted.

---

*MrNasdog Pressure Framework analysis of POL, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

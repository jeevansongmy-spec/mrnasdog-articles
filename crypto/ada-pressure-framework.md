---
title:         "ADA Inflation Analysis · September 2026 · Supply was growing · trend cooling"
description:   "Supply was growing, trend cooling: Cardano reserve rewards and voted treasury withdrawals put ADA at +0.77% net over 90 days and +0.29% next, with no burn."
canonical_url: "https://mrnasdog.com/research/ada/inflation"
tags:          ["crypto", "ada", "cardano", "layer1"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/ada/inflation](https://mrnasdog.com/research/ada/inflation)*

# ADA Inflation Analysis · September 2026 · Supply was growing · trend cooling

Cardano adds new ADA every five days from a protocol reserve, and its on-chain treasury releases more whenever a governance vote passes. Over the last 90 days Cardano stake rewards added **112.8M ADA** and approved treasury withdrawals added **194.2M ADA**, while treasury donations took **19.9M ADA** back out, so the MrNasdog Pressure Framework reads ADA at **+0.77% net** against a supply-monitor reading of **+0.68%** — a gap of **0.09 percentage points**, which is agreement. The forward reading falls to **+0.29%** because no new ADA treasury withdrawal is approved yet; ADA supply is capped at **45B**, and the reserve that feeds it shrinks a little every epoch.

## The verdict, in one paragraph

For the 90 days ending **Sep 21 2026**, the Pressure Framework reads **ADA at +0.77% net**: **307.1M ADA** entered the counted float and **19.9M ADA** left it. The independent supply monitor reads the realised 90-day change at **+0.68%**. The gap is **0.09 percentage points**, well inside the framework's half-point tolerance, so ADA ships with **no data-conflict flag**. The forward column reads **+0.29%** — the steady reserve draw alone, because the lumpy part of Cardano supply growth, treasury spending, has nothing approved for the next 90 days. The label for ADA is **mildly inflationary by reserve decay plus voted treasury spending**: a proof-of-stake chain with a fixed cap, no burn, and two separate taps into the float.

## Sell pressure: where new ADA comes from

Sell #1, protocol inflation, is **112.8M ADA**. Every Cardano epoch — a fixed five days — the protocol moves 0.3% of the remaining reserve into a reward pot, scaled by how many blocks the stake pools actually produced; this window they produced about **98%** of the expected blocks. The treasury keeps a fifth of the pot, stakers receive the rest, and whatever is not paid out returns to the reserve. Read at both ends of the window, the Cardano reserve fell **179.8M ADA** to **6.11B**; after the treasury's cut, **112.8M ADA** reached stakers' reward accounts, and a separate count of every epoch's paid rewards lands within a fraction of a percent of that figure. Because the draw is a share of a shrinking reserve, it falls slowly on its own: the next 90 days project to about **109.6M ADA**. Sell #2, vesting unlocks, is **zero** — the Cardano genesis allocations were delivered years ago and no unlock schedule remains.

Sell #3, foundation and unscheduled unlocks, is **194.2M ADA**, and it is the Cardano treasury. The ledger defines the counted float as issued ADA minus the treasury, to the last coin, so ADA counts as new supply the moment a governance vote moves it out of the treasury — not later, when the budget administrator pays a vendor. Sixteen approved withdrawals left the Cardano treasury this window: **10M ADA** on **Jun 28 2026**, **18.3M** on **Jul 3**, **5.1M** on **Jul 13**, **6.2M** on **Jul 23**, **32.9M** on **Jul 28**, **1.8M** on **Aug 2**, and **120M ADA** for a 12-month DeFi growth programme on **Aug 17 2026**. Nothing is booked forward: the only open request, **11.8M ADA** for a smart-contract development stack, sits in a vote that closes on **Oct 11 2026** with about **2%** of delegated voting power in favour so far against the **67%** it needs. Sell #4, long-term locked or bankruptcy supply, is **zero** — no Cardano estate or long-dated lock is unwinding.

## Buy pressure: where new ADA goes

Almost nowhere, and that is the other half of the Cardano story. Buy #1, programmatic buyback, is **zero**: nothing buys ADA back from the market. Buy #2, protocol fee burn, is **zero** as well. Cardano has no burn — transaction fees, about **627,600 ADA** across the window, are poured into the same reward pot as the reserve draw, so most of them flow straight back to stakers and a fifth lands in the treasury. The ledger's own identity, issued supply plus reserve equal to the **45B** cap, held exactly at both ends of the window, which leaves no room for any destroyed ADA. Buy #3, foundation buying, is **zero**.

Buy #4, new long-term locks, is **zero**, and this is where Cardano differs from chains that lock their staked coins. About **57%** of circulating ADA — **21.36B** — is delegated to stake pools, but Cardano delegation moves no coins: they stay spendable in the owner's wallet, with no lock-up, no unbonding period and no slashing. The only ADA the protocol actually holds is a set of small refundable deposits, about **5.2M ADA**, that barely moved. The one real buy row is Buy #5, treasury donations, at **19.9M ADA**: any holder can send ADA straight into the Cardano treasury, which takes it out of the counted float, and on **Jul 2 2026** a single transfer of **19,498,234 ADA** did exactly that, from a wallet that had set **20M ADA** aside the previous November. Donations have no schedule, so none are booked for the next 90 days.

## Foundation and overhang

The overhang that matters for ADA is the on-chain Cardano treasury itself, now **1.36B ADA**, or about **3.6%** of circulating supply. It is read from the ledger on every refresh, it can only be spent by a governance vote, and every withdrawal enters Sell #3 at the next refresh. Two other balances are watched but sit inside the counted float already, so they cannot add new supply: the budget administrator's contracts, holding about **214M ADA** of past withdrawals including most of the August DeFi budget, and the Cardano Foundation's own reserve, **561M ADA** at its last annual report. The protocol reserve of **6.11B ADA** is not a team balance — it is the source of Sell #1 and drains a fixed share each epoch. If the treasury balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How ADA compares to other proof-of-stake Layer 1s

Cardano sits between the two common designs for paying a proof-of-stake chain. Many Layer 1s mint new coins at a set yearly rate and lean on a fee burn to offset it; Ethereum is one example, where the burn scales with network use. Cardano has the mint side without the burn: new ADA comes from a finite reserve rather than an open-ended mint, which is why ADA supply is hard-capped at **45B**, but no ADA is ever destroyed, so fees can only redistribute supply, never shrink it. Against a hard-capped proof-of-work chain such as Bitcoin, the shape is similar — issuance that shrinks toward zero — but Cardano's shrinks smoothly, as a share of what is left, instead of halving on a date.

The second difference is the treasury. Many Layer 1s pay their ecosystem from a foundation wallet that the market treats as circulating. Cardano routes a fifth of every reward pot into a protocol treasury that sits outside the counted float until holders vote to spend it, so ADA supply growth arrives in two speeds: a slow, predictable reserve draw and a lumpy, vote-driven release that added more than the reserve draw did this window. The fee economy underneath is thin next to the coin's value — roughly **$0.6M** a year of fees against a market capitalisation near **$8.8B**, about **0.007%** — so rewards are paid almost entirely from the reserve, not from use.

## What to watch in the next 90 days

First, the **Oct 11 2026** close of the vote on an **11.8M ADA** treasury withdrawal for a smart-contract development stack; if it passes, it enters Sell #3 at the next refresh. Second, any new treasury withdrawal: the forward reading books none, and this window alone saw sixteen, so a single approved budget would lift the forward number quickly. Third, the four-month release gate on the **120M ADA** DeFi programme approved on **Aug 17 2026**, expected around mid-December: undisbursed tranches go back to the treasury if the gate fails, which would count as ADA leaving the float. Fourth, the Dijkstra hard fork, targeted for the fourth quarter of 2026, and a pending change cutting the minimum stake-pool fee from **170** to **75 ADA** — neither touches the reserve draw or the treasury's fifth, so both leave the forward reading alone unless the parameters change.

## Summary

The MrNasdog Pressure Framework reads ADA at **+0.77% net** over the trailing 90 days and **+0.29%** over the next 90. The structural mechanism is a Cardano reserve that pays stakers a steady, slowly shrinking **112.8M ADA** a quarter, plus a voted treasury that released **194.2M ADA** this window, against no burn and no buyback — only **19.9M ADA** of donations flowed the other way. The key risk is the treasury: **1.36B ADA** can move into the float on any passed vote, and the forward reading counts none of it until a vote passes. The ceiling is the **45B ADA** cap, with **6.11B ADA** still in the reserve, so Cardano supply keeps growing, but more slowly every year.

*MrNasdog Pressure Framework analysis of ADA, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 24 2026.*

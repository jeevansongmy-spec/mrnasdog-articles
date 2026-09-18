---
title: "CFG Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description: "CFG supply is growing: a 3% contract mint plus 33.61M CFG released from Centrifuge's own reserves, nothing bought back or burned. +9.67% net over 90 days."
canonical_url: "https://mrnasdog.com/research/cfg/inflation"
tags: ["crypto", "cfg", "centrifuge", "rwa"]
published: true
---

> Originally published at **[mrnasdog.com/research/cfg/inflation](https://mrnasdog.com/research/cfg/inflation)** by MrNasdog.

# CFG Inflation Analysis · September 2026 · Supply growing, projected to keep growing

CFG, the token of the Centrifuge tokenization platform, is growing in the market on two lines at once. A permissionless Centrifuge contract mints about **3% a year** into the Centrifuge treasury — **3.17M CFG** this window, in one mint on **Aug 3 2026** — and the project's own wallets released a further **33.61M CFG** they already held, **16.88M** of it to Grove's strategic stake. Nothing is bought back or burned. That is **36.78M CFG** added against **zero** removed, so the MrNasdog Pressure Framework reads CFG at **+9.67% net** over the last 90 days and **+7.06%** over the next 90, against a supply-monitor reading of **−0.07%** — a gap the monitor cannot close, because its circulating figure has not moved since June. CFG has no supply cap.

## The verdict, in one paragraph

For the 90-day window ending **Sep 18 2026**, the Pressure Framework reads **CFG at +9.67% net**: the sell side added **36.78M CFG** to a circulating supply of **380.38M**, and the buy side removed nothing. The independent supply monitor reads the same 90 days at **−0.07%**. The gap is **9.74 percentage points**, far past the framework's half-point tolerance, so CFG ships with a **data-conflict flag**. The deep walk found why: the monitor's circulating figure has held near **380.38M** every day since a one-day restatement on **Jun 9 2026**, while the Centrifuge project wallets paid out coins week after week — a flat figure cannot register a release. The primary on-chain reading is kept. The forward column reads **+7.06%**: the contract schedule adds about **5.12M CFG**, and the release line is held at the lowest of the last four quarters rather than the latest one. The label for CFG is **inflationary by treasury release**: an uncapped token whose mint is modest and whose real supply pressure is the project spending coins it already holds.

## Sell pressure: where new CFG comes from

Sell #1, protocol inflation, is **3.17M CFG**. The CFG token sits on Ethereum, and a separate Centrifuge InflationMinter contract is allowed to mint it. The rule is written into that contract: every seven days, supply may grow by a fixed step that compounds to **2.998% a year**, and the new CFG goes to the Centrifuge treasury. Anyone can trigger the mint, so it lands in lumps: the only mint this window, on **Aug 3 2026**, paid out exactly eight weeks at once. Total CFG supply moved from **697.16M** to **700.33M** across the window by exactly that amount. The minted CFG counts as sell pressure because the Centrifuge treasury passed it straight on — the treasury paid out more than it received in this window and in each of the four windows before it. On the same rule the next 90 days add about **5.12M CFG**, and seven weeks were already owed on **Sep 18 2026**. The same CFG contract address also exists on Base, Arbitrum, BNB Chain, Avalanche and Plume, but holds zero supply on each, so there is one CFG supply to count.

Sell #2, vesting unlocks, is **zero** as a separate line. Centrifuge lists team vesting to May 2030 and a locked incentive pool vesting into its own treasury to April 2029, but no CFG vesting lock can be read on-chain; every coin the project pays out leaves through its own wallets, and Sell #3 measures that flow, so booking the calendar as well would count the same CFG twice. Sell #3, foundation and unscheduled releases, is the biggest line on the CFG page at **33.61M CFG**. Three project wallets — the Centrifuge foundation wallet, the Centrifuge treasury and an incentives wallet — sent a net **36.78M CFG** to outside holders, and every wallet's balance change matched its transfers to the last unit. The newly minted **3.17M** is already Sell #1, so Sell #3 is the **33.61M** drawn from CFG the project already held. The largest leg was **16.88M CFG** to Grove on **Aug 4 and Aug 5 2026**, a partner that announced a strategic stake in the Centrifuge ecosystem on **Aug 25 2026**. The rest went to trading firms on loan, to grants and to payments, with **10.64M CFG** across **Sep 1 to Sep 3 2026** alone. Sell #4, long-term locked or bankruptcy supply, is **zero**: there is no estate, and the swap from the old CFG token closed for good on **Apr 10 2026**.

## Buy pressure: where new CFG goes

Nowhere — every CFG buy row is **zero**. Buy #1, programmatic buyback, is zero: in its answers on the CP172 proposal on **Aug 26 2026**, Centrifuge said it will not buy CFG back and will spend its money on growth. Buy #2, protocol fee burn, is zero, and it was checked both ways rather than assumed: the dead addresses hold no CFG at either end of the window, and total CFG supply rose rather than fell, so no CFG was destroyed. Buy #3, foundation buying, is zero — the only CFG that came back into Centrifuge wallets from outside was a small **62.5K** return on **Jun 22 2026**, already netted inside the release line. Buy #4, new long-term locks, is zero: nothing new was locked with a stated size, and Grove's CFG stake carries no published lock-up, so it is not counted as locked.

## Foundation and overhang

The Centrifuge overhang is large and readable on-chain. The Centrifuge foundation wallet holds **116.07M CFG** — about **31%** of circulating supply — and it funds the treasury in round blocks: **27M CFG** moved across four transfers between **Aug 4 and Sep 3 2026**. The Centrifuge treasury, where the mint lands, is nearly empty at **1.39M CFG**, which is why it keeps drawing on the foundation wallet. An incentives wallet holds **0.15M CFG**. All three are re-read from the chain on every refresh. Grove's **33.75M CFG** is no longer a project balance and is tracked as an outside holder. If any of these Centrifuge balances falls between refreshes and the CFG does not land at a burn address, the outflow enters Sell #3 at the next refresh.

## How CFG compares to other RWA tokens

RWA tokens split into two supply designs. A fixed-supply token issues nothing new, and its float grows only as vesting cliffs open, on dates anyone can read in advance. CFG is the other design: an uncapped token with a coded mint, so supply grows every week whether or not anyone acts, and a large project reserve that is spent at the team's discretion rather than on a published calendar. For CFG the mint is the smaller line — about **0.73%** of total supply per quarter — and the discretionary release is the bigger one, around **22M to 34M CFG** a quarter over the last year.

Against chains whose emission pays validators, the CFG mint sits differently: it goes to a project treasury, and whether it reaches the market depends on how that treasury spends. It has reached the market in every recent quarter. And unlike exchange tokens or fee-burning chains, CFG has nothing pulling supply back down — no buyback, no burn, no buy side at all — so every CFG the mint and the reserves release stays in the float.

## What to watch in the next 90 days

First, **CP172**, the token-to-equity plan that passed its Snapshot vote on **Sep 10 2026** with **73.29M CFG** for and **0.99M** against: one CFG would buy one share in a restructured Centrifuge company. No conversion window date is set yet. Centrifuge says the 3% CFG inflation stops once conversion is complete, and that a burn of the CFG handed in is being considered — if that burn is confirmed with a size and date, it becomes the first CFG buy row. Second, the release line: the forward column holds **21.72M CFG**, the lowest quarter of the last year; a pace like this window's would push the net well above **+7.06%**. Third, the mint backlog — seven weeks were owed on **Sep 18 2026**, so one trigger could add a lump of several million CFG at once. Fourth, the **116.07M CFG** foundation wallet, which has already sent **27M** to the treasury since **Aug 4 2026**.

## Summary

The MrNasdog Pressure Framework reads CFG at **+9.67% net** over the trailing 90 days and **+7.06%** over the next 90, with zero on every buy row. The structural mechanism is a coded Centrifuge mint of about 3% a year into a treasury that spends everything it receives, plus a **116.07M CFG** foundation reserve that feeds that treasury. The key risk is that the reserve spend is discretionary and unscheduled, so the largest line on the page can jump in any quarter — it ranged from about **22M** to **34M CFG** a quarter over the last year. CFG has no supply cap; the one planned change to that is CP172, where the mint stops only after an equity conversion that has no date yet.

---

*MrNasdog Pressure Framework analysis of CFG, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 18 2026.*

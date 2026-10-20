---
title:         "POL Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description:   "POL supply is roughly steady: a 2% mint made 52.27M POL in 90 days while a fee burn destroyed 100M, so supply fell 0.45%. Next 90 days: about +0.29%."
canonical_url: "https://mrnasdog.com/research/pol/inflation"
tags:          ["crypto", "pol", "polygon", "layer2"]
published:     true
---
> Originally published at **[mrnasdog.com/research/pol/inflation](https://mrnasdog.com/research/pol/inflation)** by MrNasDog.

<!-- main-page -->
The Polygon coin page has the score, the price drivers and every question answered — [mrnasdog.com/research/pol](https://mrnasdog.com/research/pol). Below: supply, line by line.

POL supply is roughly steady, and it swings with the base-fee burn. In the 90 days to Oct 15 2026 the Polygon 2% yearly mint created **52.27M POL** while one batch burn of saved base fees destroyed **100M POL**, so the coins on the market fell by **0.45%**. For the next 90 days we count **52.53M POL** of new mint against a **21.62M POL** burn that can start on Dec 22 2026, which points to growth of about **0.29%**. POL has no supply cap and no vesting left; the mint and the burn are the whole story.

## The verdict, in one paragraph

Our ledger reads POL at **−0.45%** over the last 90 days and **+0.29%** over the next 90. The independent supply monitor reads **−0.45%** for the last 90 days as well, a gap of **0.01** percentage points, far inside our 0.5-point tolerance, so no warning chip is shown. Both readings agree because Polygon counts every minted POL as circulating except the coins sent to the dead address, which is exactly how we count it too. The label that fits: **a steady 2% mint against a lumpy fee burn**.

## Sell pressure: where new POL comes from

**Protocol inflation is the only source of new POL: 52.27M POL in 90 days.** Once a day the Polygon emission contract on Ethereum mints new POL at a fixed rate of 2% a year, compounded. Every mint is split in half. One half goes to the Polygon staking contract, which pays validators and the people who delegate POL to them; the other half goes to the Polygon Community Treasury. We added up all 90 mints in the window and checked the sum against total supply at both ends; the two numbers match to a fraction of a coin. At today's supply the same 2% rate gives about **52.53M POL** in the next 90 days.

A governance change, PIP-92, raised staking rewards from about 3% to about 7.7% a year between Oct 1 and Dec 1 2026. That extra pay comes from **27.33M POL** of saved priority fees that were already in circulation, so it creates no new POL and does not change the mint.

**Vesting unlocks are zero.** The old MATIC schedules for the team, the sale and the foundation ended years ago, unlock trackers show POL as fully unlocked, and circulating supply equals total supply. **Foundation and unscheduled unlocks are zero**, because every Polygon wallet is already counted as circulating; when the treasury spends POL, coins change hands but no new supply appears. **Long-term locked or bankruptcy releases are zero**: no court case, estate or long lock holds POL.

## Buy pressure: where new POL goes

**The base-fee burn removed 100M POL in this window.** Every transaction on Polygon pays a base fee in POL. Those fees are not destroyed at once; they are saved in a burn wallet on Polygon and destroyed later on Ethereum. A new burn contract now releases them in batches: anyone can start a burn, at most once every 90 days, and each batch can take up to 100M POL. The first batch ran on Sep 23 2026. The saved fees left Polygon through the bridge to Ethereum and were sent to the dead address in one transaction of exactly **100,000,000 POL**. We read the dead-address balance at both ends of the window and it rose by the same amount.

The next batch can start on **Dec 22 2026**, inside the next 90 days. The burn wallet holds **21.62M POL** today, and that is the amount we count. Another **62.88M POL** of base fees sits in a fee wallet run by a Polygon Labs multisig; it only becomes burnable when its signers forward it to the burn wallet, so we do not count it yet. Under PIP-82, part of those fees (up to $1M worth) is paid back to payment apps as gas rebates until Dec 31 2026.

**Programmatic buyback is zero**: no contract or team buys POL back, and a forum idea to replace the mint with treasury buybacks has had no vote. **Foundation buy is zero**: we found no purchase of POL by Polygon Labs or the treasury. **New long-term lock is zero**: about 3.77B POL is staked on Ethereum, including **100.7M POL** the Community Treasury moved into staking on Oct 14 2026, but staked POL still counts as circulating, so staking takes nothing off the market.

## Foundation and overhang

All the POL that Polygon-linked wallets hold is already counted as circulating, so none of it can add new supply; it can only change hands. We still track it. The **Community Treasury** receives half of every mint; on Oct 14 2026 it sent **100.7M POL** through a multisig into staking and was left with about 18,700 POL. On Polygon itself the burn wallet holds **21.62M POL** and the multisig fee wallet **62.88M POL**, both made of saved base fees. A fee account for stakers held about 8.70M POL of priority fees. The MATIC swap contract holds **373.99M POL** for MATIC that holders have not yet converted. Polygon Labs' own operating wallets are not published. We read these balances on every rebuild; if any of them falls between rebuilds, we trace where the coins went at the next refresh, and a move into the dead address is booked as a burn.

## How POL compares to other EVM chains

POL sits between Ethereum and BNB in how it handles supply. Like ETH, POL has no hard cap and pays stakers with newly minted coins, and like ETH it destroys the base fee of every transaction. The difference is timing: Ethereum burns the base fee in the same block, every block, while Polygon saves base fees and burns them in batches up to 90 days apart. So the ETH burn shows up smoothly, and the POL burn shows up as a step.

BNB also burns in quarterly batches, but BNB has a fixed target supply and no ongoing mint, so every batch makes the supply smaller. POL keeps a steady 2% yearly mint, about 52M POL a quarter, so a batch only shrinks POL when it is bigger than the mint. In the last 90 days it was (100M against 52.27M); in the next 90 days the coins already waiting to be burned are smaller (21.62M against 52.53M).

Many proof-of-stake chains mint 5% or more a year for stakers and burn little. Next to them POL's 2% rate is low, though half of it goes to a treasury instead of to stakers. Whether POL shrinks or grows over a full year comes down to one question: do Polygon's fees burn more than about 215M POL a year?

## What to watch in the next 90 days

**Dec 22 2026**: the burn contract's 90-day wait ends and anyone can start the next batch. If the multisig fee wallet forwards its **62.88M POL** to the burn wallet before then, the batch could be far larger than the 21.62M we count.

**Dec 1 2026**: the PIP-92 boost to staking rewards ends. A follow-up proposal, PIP-93, is meant to pay a share of fees to stakers automatically; watch whether it changes the 2% mint or only redirects fees.

**Dec 31 2026**: the PIP-82 gas-rebate program for payment apps ends, after which all base fees go back to the burn path.

**The 2% mint debate**: a forum proposal to cut or end the mint and add treasury buybacks was revived in August 2026. Any vote that lowers the mint would cut the sell side directly.

## Summary

POL is a mixed-flows coin with supply roughly steady: Polygon mints new POL at 2% a year, about **52.27M POL** every 90 days, and burns saved base fees in batches up to 90 days apart. The first batch destroyed **100M POL** on Sep 23 2026, so supply fell **0.45%** in the last 90 days; with only **21.62M POL** waiting for the next batch on Dec 22 2026, we expect growth of about **0.29%** in the next 90. The key risk is that fees stay too small to match the mint, because POL has no supply cap and no vesting left to end.

---

*MrNasDog Pressure Framework analysis of POL, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 15 2026.*

---
title:         "AVAX Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "AVAX supply grows 0.86% in 90 days: staking mints 2.18M and a Foundation unlock adds 1.67M, while fee burns remove 46K. Helicon trims rewards from Sep 22 2026."
canonical_url: "https://mrnasdog.com/research/avax/inflation"
tags:           ["crypto", "avax", "avalanche", "proofofstake"]
published:     true
---

Originally published at [AVAX Inflation Analysis · September 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/avax/inflation).

# AVAX Inflation Analysis · September 2026 · Supply growing · projected to keep growing

AVAX supply is growing and is projected to keep growing. Avalanche staking rewards minted **2.18M AVAX** over the last 90 days and a quarterly Foundation unlock added **1.67M AVAX**, while the Avalanche fee burn removed only **46.0K AVAX**, for a net of **+0.86%** now and **+0.82%** projected as the Helicon upgrade trims staking rewards. The inflation monitor reads **+2.69%**, but that figure includes a one-day catch-up of older supply. Avalanche has a **720M AVAX** supply cap, and about **245M AVAX** of it is still left to mint.

## The verdict, in one paragraph

Against a circulating base of **442.9M AVAX**, the Pressure Framework books **3.85M AVAX** of sell pressure and **0.046M AVAX** of buy pressure over the trailing 90 days, a net of **+0.86%**, and projects **+0.82%** for the next 90 days. The inflation monitor reads **+2.69%** for the same window, a gap of **1.84 percentage points**. That is over the framework's 0.5-point tolerance, so the AVAX overview carries a monitor-gap warning. The gap is fully explained. The monitor's AVAX supply figure sat near **431.8M** from February to **Sep 11 2026**, then jumped **10.74M** on **Sep 12 2026**. Rebuilt from the Avalanche chain, tradable supply was already **439.1M AVAX** on **Jun 24 2026**, so about **7.7M AVAX** of that jump, **1.80 points**, is supply that arrived before this window. The label for AVAX is **a capped proof-of-stake chain whose staking mint outruns its fee burn**.

## Sell pressure: where new AVAX comes from

Most of it is minted. Protocol inflation, Sell #1, is **2.18M AVAX**. Avalanche launched with **360M AVAX** and keeps the other **360M** of its 720M cap as a staking-reward budget. Each time a validator or delegator stakes, the P-Chain sets aside the reward that stake can earn, and that new AVAX is counted in supply from that moment. The network's own supply counter rose from **472.47M** on **Jun 24 2026** to **474.65M** on **Sep 22 2026**, about **24K AVAX a day**. We checked it a second way: we added up every validator and every delegation that started in the window, more than **900,000** delegation records across **688** nodes, and the rewards they reserved matched the counter within **0.14%**. Rewards actually paid out in the window came to **2.72M AVAX**, close enough to confirm the pace.

The next 90 days are different, because the Avalanche Helicon upgrade activates on **Sep 22 2026** at 15:00 UTC. One of its six proposals, ACP-285, lowers the minimum staking-reward rate from **10%** to **7.5%** in a straight line over 90 days, while the one-year maximum stays at **12%**. We ran every live stake through the reward rules with that ramp and kept staking behaviour unchanged. New rewards reserved in the next window fall by about **6.8%**, so Sell #1 is projected at **2.03M AVAX**. The trailing 90 days stay as measured.

Vesting unlocks, Sell #2, are **1.67M AVAX** in each window. Only the Avalanche Foundation's allocation is still vesting, and its schedule is written into the chain's genesis file: **1,666,800 AVAX** every quarter until 2030. One unlock landed on **Aug 10 2026** and the next is due on **Nov 8 2026**. These coins were created at launch; the unlock moves them from locked to tradable. Sell #3, Foundation and unscheduled unlocks, is **0**: nothing outside that schedule was released. Sell #4, long-term locked or bankruptcy, is also **0**, because no estate or trustee holds AVAX.

## Buy pressure: where new AVAX goes

Very little leaves. Programmatic buyback, Buy #1, is **0**. Avalanche runs no buyback, and the tokenomics plan the Avalanche Foundation presented in September 2026 is still a proposal, not a live programme.

The protocol fee burn, Buy #2, is **0.046M AVAX**. Avalanche burns every fee, tip included, on all three of its chains. On the C-Chain, where smart contracts run, fees go to a burn address with no owner. That address held **5,025,688 AVAX** at the start of the window and **5,069,145 AVAX** at the end, so **43.5K AVAX** burned there. The P-Chain and X-Chain burn fees directly and added about **2.5K AVAX**. The burn is real, but it is small next to the staking mint: about one AVAX burned for every **47** minted. Helicon also brings a new minimum C-Chain gas price voted by validators. It could lift the burn, but it has no record yet, so the forecast keeps the measured rate.

Foundation buy, Buy #3, is **0**. The Avalanche Foundation bought no AVAX on the market; its known deals run the other way, selling AVAX to treasury companies at a discount. New long-term lock, Buy #4, is **0**. About **203.4M AVAX** is staked, but staked AVAX already counts as circulating, so staking removes nothing from this reading. Helicon also shortens the minimum stake to **48 hours**, which makes staked AVAX easier to free.

## Foundation and overhang

The largest overhang is the Avalanche Foundation's locked allocation: **26.67M AVAX** today, falling to **25.0M** after the **Nov 8 2026** unlock. It is exactly the gap between total supply and circulating supply, to within **171 AVAX**, so no other hidden bucket sits outside the float. It releases on a fixed schedule, so there is no decision to watch, only a date.

Two listed companies hold AVAX as their main asset. Avalanche Treasury Company reported about **15.3M AVAX** at the end of June 2026, and AVAX One reported **14.1M AVAX** in August 2026, about 95% of it staked. Both positions, and the Foundation's unlocked AVAX, already count as circulating. If one of them sold, the coins would move inside the market, not into it, so they do not add to the sell rows. They are still worth watching for price, and they are refreshed from company filings at every rebuild. If the Foundation's locked balance falls faster than its schedule between refreshes, the extra outflow enters Sell #3 at the next refresh.

## How AVAX compares to other capped proof-of-stake chains

AVAX sits between two families. Like Bitcoin, it has a fixed supply cap, 720M AVAX, set in protocol code. Unlike Bitcoin, the pace of new coins is not a halving clock. Avalanche pays staking rewards from the unminted part of the cap, and the reward rate shrinks as supply gets closer to the cap. So AVAX issuance slows over time, but smoothly, and it depends on how much AVAX is staked and for how long.

Compared with uncapped proof-of-stake chains, where a staking emission of several percent a year has no end date, AVAX has a real ceiling. Its current mint, about **0.5%** of circulating supply per quarter, is modest for a staking chain. Compared with Ethereum, which also burns fees, Avalanche burns far less than it mints: the burn offsets about 2% of new AVAX. A fee burn only turns supply flat when network activity pays fees at the scale of the staking mint, and the Avalanche C-Chain is not near that level today.

The Helicon upgrade moves AVAX in the direction of lower issuance. ACP-285 cuts short-stake rewards while keeping one-year rewards, so the network pays less for short, easy-to-exit staking. Avalanche's own estimate is that yearly inflation falls by 0.5 to 1 point once stakers adjust.

## What to watch in the next 90 days

First, the Helicon activation on **Sep 22 2026** and the ACP-285 ramp that runs to about **Dec 21 2026**: if the rise in the P-Chain supply counter does not fall from about **24K AVAX**, stakers are choosing longer stakes faster than modelled. Second, the Avalanche Foundation unlock of **1,666,800 AVAX** on **Nov 8 2026**, the only dated supply event in the window. Third, the new validator-voted minimum gas price on the C-Chain, the one change that could lift the fee burn above **43.5K AVAX** a quarter. Fourth, the Avalanche Foundation's tokenomics plan: any vote that sends network income into buybacks or burns would open a new buy row. Fifth, the treasury companies' next filings, since a forced sale of pledged AVAX would move price even though it adds no new supply.

## Summary

The MrNasdog Pressure Framework reads AVAX at **+0.86%** over the trailing 90 days and **+0.82%** projected: supply growing, projected to keep growing. The driver is the Avalanche staking mint, **2.18M AVAX** a quarter, plus a **1.67M AVAX** quarterly Foundation unlock, against a fee burn of only **46.0K AVAX**. The key risk is that this is steady and built into the protocol: it runs every day whatever the price, and the burn offsets about one coin in 47. The ceiling is the **720M AVAX** cap, and the Sep 22 2026 Helicon upgrade slows the pace toward it.

MrNasdog Pressure Framework analysis of AVAX, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 22 2026.

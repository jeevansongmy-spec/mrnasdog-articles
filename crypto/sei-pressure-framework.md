---
title: "SEI Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description: "MrNasdog Pressure Framework read of Sei (SEI): the mint added 43.5M over 90 days, but a monthly cliff the chain cannot see released 318.3M. No burn, no buyback. Net +5.37%."
canonical_url: "https://mrnasdog.com/research/sei/inflation"
tags: ["crypto", "sei", "cosmos", "layer1"]
published: true
---

*Originally published at [mrnasdog.com/research/sei/inflation](https://mrnasdog.com/research/sei/inflation).*

# SEI Inflation Analysis · September 2026 · Supply growing, projected to keep growing

The Pressure Framework reads SEI at **+5.37%** over the trailing 90 days and **+5.33%** over the next 90. Only a small slice of that is Sei minting coins: the chain's token release schedule paid **43.5M SEI** in the window. The rest — **318.3M SEI** — is a monthly allocation cliff that settles between ordinary Sei wallets and never touches the chain's own supply figure at all. Buy pressure is **0**: Sei burns no fee and runs no buyback. The ceiling is a hard **10,000M SEI**, and the chain is still 2,483.0M short of filling it.

## The verdict, in one paragraph

Against a circulating base of **6,733M SEI**, the framework books **361.8M SEI** of sell pressure and **0** of buy pressure over the trailing 90 days — a net of **+5.37%** — and projects **+5.33%** for the next 90 days, the small decline coming entirely from a mint step-down that landed on **Aug 15 2026**. The inflation monitor reads **+0.00%** for the same window, a gap of **5.37 percentage points**, which is far over the framework's 0.5pp tolerance and therefore ships with a monitor-gap warning on the overview page. That gap has a single, checkable cause: the aggregated float figure the monitor divides by has been pinned at **6,733,333,333 SEI** since **Feb 13 2026**, while an independent float count now reads **7,460,000,000**. The label for SEI is a **capped chain whose float is filled by a calendar, not by a rate**: nothing about SEI's issuance is fast, and almost none of its dilution is issuance.

## Sell pressure: where new SEI comes from

**Sell #1, protocol inflation, is 43.5M SEI**, and it is unusually easy to verify because Sei does not mint at a rate at all. Sei's mint module carries a token release schedule of ten annual tranches totalling **1,500M SEI**, and it pays one tranche divided by **364** once per calendar date. The tranche running to **Aug 14 2026** paid **494,505 SEI** a date; the one that started **Aug 15 2026** pays **453,297 SEI**. Sixty-five dates at the old rate and twenty-five at the new one give **43,475,275 SEI**, and the chain confirms the count itself: its live mint record shows exactly twenty-five payments since the step, to the millionth of a coin. Because the step-down landed inside the window, the forward column is re-based to the post-step rate alone — **40.8M SEI** — which is why the two columns of this page differ rather than repeating one number. Sei runs at roughly **0.43 seconds** a block against a 0.4-second nominal, and governance reset its consensus timeouts mid-window, but neither touches issuance: the mint is indexed to the calendar, not to blocks.

**Sell #2, vesting unlocks, is 318.3M SEI**, and this is the row that decides the page. Sei's genesis created no lock accounts. **9,216.3M** of the **10,000M** ceiling already exists on chain, sitting in ordinary wallets, so when a tranche unlocks the coins simply move between two accounts the chain's supply figure already counts. Reading Sei's bank module at both ends of the window and finding it moved only by the mint is not evidence that nothing was released — that surface could not have shown a release either way. The published calendar runs a cliff on the **13th** of each month: **55.6M SEI** to private-sale buyers, **42.2M SEI** to the team and **8.3M SEI** to a strategic tranche, **106.1M SEI** together. Three fired inside this window — **Jun 13 2026**, **Jul 14 2026** and **Aug 13 2026** — and three more fire in the next 90 days.

**Sell #3, Foundation and unscheduled unlocks, is 0.** The two large discretionary pools on Sei — a **2,700.0M SEI** ecosystem reserve and a **900.0M SEI** foundation tranche — were both released in full at launch and neither has a release calendar of its own, so there is capacity but no observed firing to book. **Sell #4, long-term locked or bankruptcy, is 0**: SEI has no bankruptcy estate, no trustee and no court-ordered distribution attached to it.

## Buy pressure: where new SEI goes

Nowhere. **Buy #1, programmatic buyback, is 0** — Sei runs no programme that spends treasury money repurchasing SEI on the open market, and none was announced or executed inside the window. **Buy #2, protocol fee burn, is also 0**, and here the reason is stronger than a flat reading: Sei's own developer documentation states that the chain does not burn a base fee and that transaction fees accrue to validators. The framework still read both places a SEI could be destroyed. The two unspendable addresses on Sei hold **1,384.1 SEI** and **18.7 SEI** between them — everything ever sent there since launch, and about two hundredths of a thousandth of one percent of circulating supply. And the count of SEI in existence moved by exactly what the release schedule paid: **4,532,967.032960 SEI** across the ten days to **Sep 8 2026**, against ten payments of **453,296.703296 SEI**, closing to **0.000000**. Had a fee burn been quietly running, that identity would not close.

**Buy #3, Foundation buy, is 0.** No entity behind Sei bought SEI on the market in this window, and the community pot the chain itself controls holds **0.5 SEI**, because the share of staking pay routed to it is set to zero. **Buy #4, new long-term lock, is 0** as well. Staked SEI stands at **4,171.8M** with a further **109.9M** unbonding, and the 21-day exit queue is a delay rather than a lock — but the decisive point is the denominator: the float count this reading divides by already treats staked SEI as tradable, so bonding a coin moves it inside the same bucket and removes nothing.

## Foundation and overhang

Sei's overhang is large and, unusually, almost entirely unaddressed on chain. The dominant items are the **2,700.0M SEI** ecosystem reserve and the **900.0M SEI** foundation tranche, both released at launch into project-controlled wallets and neither on any published release calendar since. Behind them sit **1,745.0M SEI** still due on the monthly cliff — **986.7M** to the team, **666.7M** to private-sale buyers and **91.7M** to the strategic tranche — plus **783.7M SEI** the mint module has not created yet. What the framework cannot do is point at an address: the top-thirty holder walk this session returned staking module accounts and exchange wallets only, and the largest single non-module holder, at **885.0M SEI**, maps to a known exchange hot wallet and is excluded because it belongs to depositors, not to the project. No Sei address is publicly labelled as a project treasury, so these pools are watched through the calendar and the aggregated float count rather than through a balance.

The trigger sentence still applies to each of them: if the ecosystem reserve's or the foundation tranche's balance falls between refreshes, that outflow enters Sell #3 at the next refresh. The honest caveat is that on Sei this is a web walk rather than a chain read, and the next rebuild should re-test whether any of these pools has acquired a public address label.

## How SEI compares to other capped proof-of-stake L1s

SEI sits in the small group of proof-of-stake Layer 1s with a hard, on-chain supply ceiling. That already separates it from the uncapped Cosmos L1s, where a bonded-ratio-targeting mint prints somewhere between 5% and 15% a year forever and the ceiling is a policy rather than a number. Sei's issuance is not only capped, it is scheduled: **1,500M SEI** across ten named annual tranches ending in **2033**, stepping down every August, with no dependence on how much SEI is staked. On the pure issuance axis Sei is stricter than almost any of its peers — **43.5M SEI** a quarter is about **0.65%** of circulating a year.

And yet the page reads **+5.37%**. That is the whole lesson of the comparison, and it is the same lesson a halving-model chain teaches from the other direction: a hard cap constrains total supply, not tradable float. Sei is far closer in shape to a recently-launched token working through an investor and team vest than to a mature capped chain. The difference from a smooth vest is that Sei's arrives as a dated cliff on the 13th rather than by the second, so there is something to trade around — and, unlike a chain that enforces its vest in a lock contract, Sei enforces its by contract alone, which means no on-chain surface confirms the release and no on-chain surface would confirm a change to it either.

The last comparison is to exchange tokens that run quarterly buybacks and burns. Those offset issuance with a usage-linked removal and can read genuinely negative. Sei has none of that machinery — no buyback contract, no auction burn, no fee destruction — so nothing on the buy side of this ledger can grow with adoption. For the burn side to matter here, Sei would have to destroy on the order of **361.8M SEI** a quarter, more than 5% of circulating supply, using a mechanism it has explicitly chosen not to build.

## What to watch in the next 90 days

First, the three dated cliffs: **Sep 13 2026**, **Oct 13 2026** and **Nov 13 2026**, each **106.1M SEI**, and each the single largest supply event on this chain. Second, the private-sale leg, which has **666.7M SEI** and twelve monthly payments left and therefore stops around **Sep 2027** — the first date on which this page's number falls materially. Third, the mint step, which will not move again until **Aug 15 2027**, when the tranche drops from **165M** to **135M** a year. Fourth, the aggregated float count: if it un-freezes from **6,733,333,333 SEI** and catches up to the roughly **7,460,000,000** an independent count already reads, this page's denominator changes and the monitor gap closes on its own. Fifth, Sei governance, which passed only chain upgrades and network toggles inside this window and nothing supply-affecting — but the mint schedule is a chain parameter and a vote is all it would take to change it.

## Summary

The MrNasdog Pressure Framework reads SEI at **+5.37%** over the trailing 90 days and **+5.33%** projected forward: supply growing, projected to keep growing. The structural mechanism is almost all unlock and almost no inflation — Sei's mint paid **43.5M SEI** on a fixed calendar while a monthly allocation cliff released **318.3M SEI** that the chain itself cannot see, because Sei holds those coins in ordinary wallets rather than in lock accounts. The key risk is that this is contractual and dated: it repeats on the **13th** of every month regardless of price, with **1,745.0M SEI** still to come, and there is no burn or buyback anywhere in the design to offset it. The ceiling is the one genuine comfort — **10,000M SEI**, on chain, with the mint module the only path to it and that path fully scheduled to **2033**.

---

*MrNasdog Pressure Framework analysis of SEI, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 8 2026.*

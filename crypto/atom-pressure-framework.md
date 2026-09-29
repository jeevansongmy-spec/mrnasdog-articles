---
title: "ATOM Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description: "Supply growing, projected to keep growing: ATOM reads +3.04% over 90 days. Cosmos Hub minted 16.21M ATOM at a real 12.7% rate and burned only 1.9K by slashing."
canonical_url: "https://mrnasdog.com/research/atom/inflation"
tags: ["crypto", "atom", "cosmos", "staking"]
published: true
---

*Originally published at [https://mrnasdog.com/research/atom/inflation](https://mrnasdog.com/research/atom/inflation)*

# ATOM Inflation Analysis · September 2026 · Supply growing · projected to keep growing

ATOM, the native coin of the Cosmos Hub, is clearly inflationary: the Cosmos Hub pays its stakers in newly minted ATOM every block, and that mint created **16.21M ATOM** in the last 90 days, while only **1,938 ATOM** were destroyed, all of it by validator slashing. Net supply grew **+3.04%** in 90 days, and the Pressure Framework expects about **+3.17%** in the next 90. ATOM has no supply cap, no fee burn and no buyback, so nothing on the chain today works against the mint.

## The verdict, in one paragraph

For the 90-day window from **Jul 1 2026** to **Sep 29 2026**, the Pressure Framework reads **ATOM at +3.04% net**: the sell side added **16.21M ATOM**, the buy side removed **1,938 ATOM**, against a circulating supply of **533.16M ATOM**. The inflation monitor reads **+3.14%** for the same stretch, a gap of **0.10 percentage points**. That is inside our 0.5-point tolerance, so no warning chip is shown; the small difference comes from the monitor measuring growth against the smaller supply of 90 days ago. For the next 90 days the reading is **+3.17%**. In one line: the Cosmos Hub is **built to inflate, with a mint running faster than its own setting**.

## Sell pressure: where new ATOM comes from

Protocol inflation is the only live sell row, and it is large: **16.21M ATOM** were minted in 90 days. The Cosmos Hub mint module sets a yearly rate between a floor of 7% and a ceiling of 10%, and pushes it up whenever less than 67% of ATOM is staked. About **63%** is staked today, so the rate sits at the **10% ceiling**, where it stayed through the whole window.

The detail that matters: ATOM is minted per block, and the mint assumes about **4.36M blocks a year**, one every 7.2 seconds. The Cosmos Hub actually makes a block every **5.7 seconds**, so it produces about 27% more blocks than the setting expects, and each one pays the full reward. The real pace is about **12.7% a year**, not 10%. This window even included a 25-hour halt from Sep 22 to Sep 23 2026, when validators stopped the chain after the Neutron governance attack; no ATOM was minted during it. The next 90 days should bring about **16.91M ATOM**, because each block pays 10% of a supply that keeps getting bigger, and no halt is assumed.

Vesting unlocks are **zero**. The 2017 fundraiser and the founding allocations were released years ago, and circulating supply sits within about 24K ATOM of total supply, so there is no locked bucket left to open. Foundation and unscheduled unlocks are also **zero**: the Interchain Foundation and the community pool hold large amounts of ATOM, but those coins are already counted as circulating, so selling or spending them moves coins inside the market rather than adding new ones. Long-term locks and bankruptcy releases are **zero** as well. There is no estate or trustee holding ATOM, and staked ATOM, which takes 21 days to unbond, never left the circulating count.

## Buy pressure: where new ATOM goes

The Cosmos Hub has no programmatic buyback, so that row is **zero**. A redesign of ATOM tokenomics is being researched, but no vote to add a buyback or a fee burn has reached the chain. An article in August 2026 said a buyback and burn had gone live; the chain shows no such proposal, the mint is unchanged, and nothing beyond slashing was destroyed.

The protocol fee burn is also **zero**. The Cosmos Hub fee market collects its base fee in a module wallet instead of destroying it; that wallet grew from about 57.4K to **60.8K ATOM** this window. Foundation buying is **zero**, and a new long-term lock is **zero**, because staked ATOM stays inside the circulating count.

The only thing that removes ATOM is the slashing burn, booked as its own row: **1,938 ATOM** in 90 days. When a validator misses too many blocks, a small slice of the ATOM staked with it is destroyed. That happened on eleven separate days between Jul 9 and Sep 28 2026, with the largest amounts on Sep 3 and Sep 9. Against 16.21M ATOM of new supply, the slashing burn offsets about one ATOM in every 8,400 minted.

## Foundation and overhang

Four large pots of ATOM are tracked. The **Interchain Foundation** reported **14.93M ATOM** in its treasury on Jun 30 2026, close to the 15.01M it reported a year earlier; its July and August reports have not been published, so we check that figure by hand every two weeks. The **community pool**, which only a passing governance vote can spend, grew from **10.50M** to **11.38M ATOM** in the window, fed by a 2% cut of staking rewards. A **4-of-6 recovery wallet** holds about **1.23M ATOM** taken back from the Neutron attacker on Sep 23 2026. The fee collector holds **60.8K ATOM**. The chain pots are read every day.

All four sit inside the circulating count, so none of them can add new supply to the market; they can only move coins that are already counted. We still watch them: if any of these balances falls between checks, the outflow is written into the Foundation row at the next check.

## How ATOM compares to other proof-of-stake Layer 1 chains

ATOM belongs to the group of uncapped, continuous-emission proof-of-stake chains, but it sits at the high end of that group. Ethereum also pays stakers in new coins and has no cap, yet it destroys the base fee of every transaction, so heavy use can pull net issuance down. The Cosmos Hub parks its base fee instead of burning it, so ATOM has no usage-driven brake on supply at all.

Solana follows a schedule that cuts its inflation rate every year toward a low long-term floor, so its dilution shrinks by design over time. ATOM has no such taper: its rate is set by the staking ratio, and at today's ratio it stays at the ceiling, with the fast block time pushing the real pace above it. Bitcoin, with a fixed cap and halvings, sits at the opposite end of the map.

The practical difference for an ATOM holder is simple. Staking roughly keeps pace with the mint, but unstaked ATOM loses about **3%** of its share of supply every 90 days. Among large proof-of-stake coins, that is one of the steepest dilution rates we track.

## What to watch in the next 90 days

First, the **tokenomics Phase 2 report**: on Sep 24 2026 the Hub team said it had sent feedback on an early draft and is waiting for the final version, and any change to the mint, a fee burn or a buyback would need a governance vote before it touches the ledger; no vote date exists yet. Second, proposal **1056**, voting until **Sep 30 2026**, asks for about **1.72M ATOM** from the community pool; even if it passes, those coins are already circulating, so it would not change the supply reading. Third, the **staking ratio**: if more than 67% of ATOM is staked, the rate starts to fall from 10% toward 7%. Fourth, a community draft posted on Sep 21 2026 to limit ATOM inflation to a 4–8% band is still only a forum discussion. Fifth, the Interchain Foundation's next treasury report, which would show whether its 14.93M ATOM has started to shrink.

## Summary

ATOM supply grew **+3.04%** in the 90 days to Sep 29 2026 and is projected to grow about **+3.17%** in the next 90, because the Cosmos Hub mints new ATOM every block at its 10% ceiling and its fast blocks lift the real pace to about 12.7% a year. The only offset is a slashing burn of **1,938 ATOM**; there is no fee burn, no buyback and no vesting. The main risk for holders is continued dilution with no cap; the main thing that could change it is a governance vote on new tokenomics, which has not been scheduled.

*MrNasdog Pressure Framework analysis of ATOM, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

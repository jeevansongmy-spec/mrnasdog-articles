---
title:         "GRT Inflation Analysis · October 2026 · Supply growing · projected to keep growing"
description:   "GRT supply keeps growing: 72.6M new GRT and a 38.75M Foundation unlock against a 63K burn give +1.02% over 90 days and +1.07% next. No buyback, no cap."
canonical_url: "https://mrnasdog.com/research/grt/inflation"
tags:          ["crypto", "grt", "the-graph", "infrastructure"]
published:     true
---
Originally published at [GRT Inflation Analysis · October 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/grt/inflation).

# GRT Inflation Analysis · October 2026 · Supply growing · projected to keep growing

<!-- main-page -->
➜ Start with the The Graph coin page for the short answer (should you buy GRT?) and its price drivers: [mrnasdog.com/research/grt](https://mrnasdog.com/research/grt)

The MrNasdog Pressure Framework reads GRT at **+1.02% net** over the last 90 days and **+1.07%** over the next 90. The Graph minted **72.60M GRT** of new issuance and the Graph Foundation drew **38.75M GRT** from its vesting lock, while the protocol burned only **63,251 GRT**. GRT has no supply cap: issuance runs at a fixed 120.73 GRT per Ethereum block, and the Foundation lock keeps opening every month until December 2030.

## The verdict, in one paragraph

Over the 90 days from Jul 11 to Oct 9 2026, new GRT reaching the market added up to **111.35M GRT** against **63,251 GRT** destroyed, a net change of **+1.02%** on a circulating supply of **10.94B GRT**. For the next 90 days we project **116.68M GRT** of new supply and the same small burn, or **+1.07%**. Our inflation monitor reads **+1.32%** for the same window, a gap of **0.30 percentage points**, inside our 0.5-point tolerance, so no warning chip is shown. The Graph is inflationary by design: a steady issuance stream and a scheduled Foundation unlock, with a burn too small to matter.

## Sell pressure: where new GRT comes from

Protocol inflation is the largest source. The Graph's issuance contract on Arbitrum mints **120.73 GRT** for every Ethereum block, roughly **317M GRT** a year, or about 2.7% of today's supply. Counted mint by mint on the Arbitrum GRT token, **72.60M GRT** of new issuance appeared in the window: 63.30M to the subgraph service that pays indexers, 6.44M to the new Innovation Allocation and 2.87M to a reclaim contract. The full rate works out to about **77.93M GRT** per 90 days; the realised figure was lower because indexers claim rewards when they close allocations, not as they accrue. Since Sep 1 2026 the mint rate has run within 1% of the full rate, so the next 90 days use **77.93M GRT**.

Vesting unlocks add **38.75M GRT**. The Graph Foundation's 1.55B GRT allocation sits in a lock contract on Ethereum that frees one slice of **12.92M GRT** a month across 120 months, from December 2020 to December 2030. The Foundation withdrew three slices in this window, on Jul 24, Aug 25 and Sep 23 2026, and the lock fell from 697.50M to 658.75M GRT. Three more slices vest on Oct 17, Nov 17 and Dec 17 2026. This lock is the only GRT still outside the circulating count, so every slice is new supply for the market.

Foundation and unscheduled unlocks book zero: no other team pile released coins in the window. Long-term locks and bankruptcy book zero too. The early team, the backers and Edge & Node all finished their vesting schedules years ago, and no estate or court process holds GRT.

## Buy pressure: where new GRT goes

There is no programmatic buyback. No contract and no treasury buys GRT back; a holder asked on the governance forum on Sep 5 2026 for revenue-funded burns, but no proposal has gone to a vote.

The protocol fee burn is real but tiny. The Graph destroys a 1% tax on query fees and a tax charged when curators signal on a subgraph. In the window those burned **41,835 GRT** and **21,156 GRT**, and another 259 GRT was sent to dead addresses, for a total of **63,251 GRT**. That is less than 0.1% of the GRT minted in the same 90 days. We keep the same burn for the next 90 days.

Foundation buying is zero: the Foundation receives and spends GRT, and nothing on-chain or in its posts shows it buying. New long-term locks are zero as well. About 1.94B GRT is staked by indexers and delegators, down 139M over the window, but staked GRT still counts as circulating, so staking removes nothing from the float.

## Foundation and overhang

Four team-controlled piles are tracked. The largest is the Graph Foundation lock, with **658.75M GRT** left, which releases on the monthly schedule above and is read on-chain every rebuild. The Innovation Allocation contract, funded by 20% of issuance since GIP-0089 went live on Sep 1 2026, held **2.79M GRT** on Oct 9 2026 after paying out 3.65M. The reclaim contract that collects rewards indexers fail to earn held **2.87M GRT** and has paid out nothing. The Foundation safe that receives each monthly slice held 150K GRT, because it passes the slices on.

The two contracts hold freshly minted coins that are already counted in protocol inflation, so spending them later adds nothing new. We read all four balances at each rebuild; if any of them falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How GRT compares to other utility-token networks

GRT belongs to the group of work tokens that pay service providers with new issuance and have no hard cap. Its 120.73-per-block rate is fixed in tokens, not as a share of supply, so the yearly percentage slowly falls as supply grows. That is a gentler path than chains whose issuance is a fixed percentage forever, and a heavier one than capped coins with a halving schedule, where new supply shrinks on a timetable.

The real difference is the burn. Networks with an EIP-1559-style fee burn can offset part or all of their issuance when usage is high. GRT's burn is a 1% tax on query fees plus a curation tax, and at today's usage it removes less than one GRT for every thousand minted. Until query fees grow by orders of magnitude, or governance changes the burn, GRT's supply behaves like a pure emission schedule.

GRT also differs from most networks of its age in still carrying a monthly unlock. Most 2020-era tokens finished vesting long ago; The Graph Foundation's 10-year lock adds about 155M GRT a year until December 2030, roughly a third of the yearly pressure, on top of issuance.

## What to watch in the next 90 days

**Oct 17, Nov 17 and Dec 17 2026:** the Foundation lock vests its 70th, 71st and 72nd slices of 12.92M GRT; watch when the Foundation withdraws them.

**GIP-0090:** a proposal from Sep 23 2026 would send 0.1% of issuance to a community group. It moves coins inside the same 120.73-per-block budget and does not raise total issuance.

**Query fees after Oct 8 2026:** the Foundation moved staging traffic for BNB Chain and Polygon subgraphs onto the decentralized network on Oct 8 2026. More paid queries mean more of the 1% tax is burned; watch whether the burn rises from today's 63,251 GRT per 90 days.

**Innovation Allocation spending:** 24.146 GRT per block now flows to a Foundation-run fund. Watch its balance and how fast it is paid out.

## Summary

The MrNasdog Pressure Framework reads GRT as inflationary: **+1.02%** net over the last 90 days and **+1.07%** projected for the next 90, against an inflation monitor reading of +1.32%. The supply grows from two sources, indexing issuance of 120.73 GRT per Ethereum block and a Graph Foundation lock that frees 12.92M GRT a month until December 2030. The burn from query and curation taxes removes only about 63,000 GRT per 90 days, so it barely dents the new supply. GRT has no supply cap, and the key risk for holders is that issuance keeps outrunning real usage of The Graph.

---

*MrNasdog Pressure Framework analysis of GRT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 9 2026.*

---
title:         "GRT Inflation Analysis · July 2026 · Issuance burned almost back to flat"
description:   "The Graph mints ~3% a year for indexing rewards but burns most of it back via query-fee, curation and delegation taxes. Framework +0.25% net; monitor +0.25%. Uncapped, fully vested."
canonical_url: "https://mrnasdog.com/research/grt/inflation"
tags:          ["crypto", "grt", "the-graph", "infrastructure"]
published:     true
---

*Originally published at [mrnasdog.com/research/grt/inflation](https://mrnasdog.com/research/grt/inflation)*

# GRT Inflation Analysis · July 2026 · Issuance burned almost back to flat, supply roughly steady

The Graph mints new GRT at about **3% a year** as indexing rewards — roughly **79.9M GRT** over 90 days on a ~10.80B circulating base — but its query-fee, curation and delegation burns destroy about **53.0M GRT** over the same window, leaving net supply barely positive. The Pressure Framework reads **+0.25% net**, and our inflation monitor reads **+0.25%** too — a gap near **zero percentage points**, so no data-conflict chip. GRT is an uncapped, fully-vested token whose burns hold net inflation close to neutral.

## The verdict, in one paragraph

For the 90-day window the framework reads **GRT at +0.25% net** — technically inflationary, but only just. The Graph is an uncapped token: it mints roughly **79.9M new GRT** as indexing rewards over the window, and that is the entire sell side, because vesting is finished and there is no Foundation cliff or bankruptcy estate. Against that, protocol burns remove about **53.0M GRT**, so the two flows very nearly cancel. Our inflation monitor reads **+0.25%** over the same window; the gap is close to **zero percentage points**, well inside tolerance, so no monitor-gap chip ships. The Graph is a work token whose 3% issuance is almost fully burned back — structurally near-neutral rather than deflationary, and dependent on query demand to stay that way.

## Sell pressure: where new GRT comes from

Almost all of the sell side is a single line. **Protocol inflation** is booked at **~79.9M GRT**: The Graph mints new GRT at a target rate of about **3% a year** and pays it to Indexers and Delegators as indexing rewards for serving subgraph data, which on a ~10.80B base is roughly 79.9M over 90 days. This is the only source of genuinely new GRT. **Vesting unlocks** are zero — the early-team, advisor, backer, Edge & Node and Graph Foundation allocations have all finished their multi-year linear vesting since the December 2020 launch, and unlock trackers show GRT fully unlocked, so no cliff falls inside the next 90 days. **Foundation and unscheduled unlocks** are zero as a market flow: the Graph Foundation and Edge & Node still hold treasuries, but they are unlocked with no published release schedule and no discretionary sale to market was observed in the window. **Long-term locked or bankruptcy** is zero — no bankruptcy estate holds or distributes GRT.

## Buy pressure: where new GRT goes

The buy side is what keeps The Graph near neutral. **Protocol fee burn** is booked at **~53.0M GRT** and covers three separate mechanisms: **1% of all query fees** paid to the network are burned, a **1% curation tax** is burned whenever Curators signal on a subgraph, and a **0.5% delegation tax** is burned whenever Delegators delegate to an Indexer. The Graph documents this combined burn at about 1% of supply a year "and increasing as network activity grows"; with query-fee volume hitting record highs on Arbitrum and net supply having grown only from 10.0B at genesis to about 10.8B over five and a half years, the burn now runs closer to 2% a year — roughly 53M over the window, offsetting most of the 3% issuance. **Programmatic buyback** is zero: The Graph runs no token repurchase, because its deflationary lever is the burn, not open-market buying. **Foundation buy** is zero — there is no Foundation accumulation programme. **New long-term lock** is zero — no newly-deployed lockup contract with an announced quantum, and staked or delegated GRT is not removed from supply.

## Foundation and overhang

The team-controlled overhang is the **Graph Foundation** (a roughly **19.6%** genesis allocation) together with **Edge & Node** (about **7.7%**), the core development entities. Both are now fully unlocked, held in their own treasuries, with no published release schedule — so they are capacity rather than cadence: large claims on the float that have not been firing into the market. No discretionary sale was observed in the window, so the row reads zero, but the balance is tracked each refresh. If either treasury's balance were to fall between refreshes — a Foundation deployment, a grant sale, an ecosystem funding round settled to market — that outflow would enter Sell #3 at the next refresh. Until then, the overhang is a watched store, not an active seller, and the reading rests on issuance versus burn.

## How GRT compares to other uncapped work-token chains

GRT belongs to the family of **uncapped work tokens** — protocols that mint new supply continuously to pay the operators who do the network's work, in The Graph's case Indexers and Delegators serving queries. That puts it in a different structural bucket from a hard-capped, halving-schedule coin: there is no fixed ceiling, and total supply rises every day as indexing rewards are minted. The distinguishing feature is that The Graph pairs its issuance with a **fee burn**, so the honest way to read it is issuance net of burn, not the gross 3% headline.

The closest mechanical analogue is a fee-burning smart-contract chain like Ethereum, where EIP-1559 burns base fees against staking issuance and net supply hovers near flat when activity is high. The Graph works the same way in miniature: **3% issuance** against a demand-driven burn, netting near zero when query volume is strong. The difference from an exchange token like BNB is the source of the deflation — BNB buys back and burns with company revenue on a fixed schedule, whereas The Graph's burn is a byproduct of real protocol usage (queries, curation, delegation), so it scales with adoption rather than with a treasury decision. Against a pure continuous-emission Layer 1 with no burn, GRT is the tighter asset, because a large share of its issuance is destroyed rather than left to dilute holders.

The trade-off is that this near-neutrality is **contingent on demand**. A halving coin's scarcity is guaranteed by code; The Graph's is earned by query volume. If usage falls, the burn shrinks while the 3% issuance keeps minting, and net inflation would widen back toward the gross rate. That is why the framework labels GRT roughly steady rather than structurally deflationary — the burn is doing the work, but it is a demand-linked burn, not a protocol-guaranteed cap.

## What to watch in the next 90 days

Four things move the reading. First, **query-fee volume** — the burn scales with usage, so a strong quarter tightens net supply and a soft one widens it. Second, **GIP-0086**, the passed Rewards Manager and Subgraph Service upgrade wiring the Issuance Allocator and Rewards Eligibility Oracle: it changes how issuance is distributed and gated, and if the eligibility oracle trims effective issuance below the 3% target, net inflation falls further. Third, the **Horizon** rollout through 2026, which adds new data services and could lift both query fees (more burn) and reward demand (more issuance). Fourth, the **Foundation and Edge & Node treasuries** — any move to deploy or sell those unlocked balances would flip the overhang into real Sell #3 pressure. All four are visible on The Graph's governance forum and network dashboards.

## Summary

GRT is an uncapped, fully-vested work token that mints about **3% a year** in indexing rewards — roughly **79.9M GRT / 90D** — and burns most of it back through query-fee, curation and delegation taxes worth about **53.0M GRT / 90D**. The framework reads **+0.25% net** against a monitor reading of **+0.25%** — a near-zero gap, no chip — making The Graph roughly supply-neutral rather than deflationary. The key risk is that the offset is demand-linked: if query volume falls, the burn shrinks while issuance keeps minting, so GRT's near-neutrality is earned by usage, not guaranteed by a cap.

---

*MrNasdog Pressure Framework analysis of GRT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 8 2026.*

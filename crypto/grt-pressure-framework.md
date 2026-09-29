---
title:         "GRT Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "GRT supply keeps growing: 70.6M new GRT and a 38.8M Foundation unlock against a 59K burn give +1.00% over 90 days and +1.07% next. No buyback, no cap."
canonical_url: "https://mrnasdog.com/research/grt/inflation"
tags:          ["crypto", "grt", "the-graph", "infrastructure"]
published:     true
---

Originally published at [GRT Inflation Analysis · September 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/grt/inflation).

# GRT Inflation Analysis · September 2026 · Supply growing · projected to keep growing

The MrNasdog Pressure Framework reads GRT at **+1.00% net** over the last 90 days and **+1.07%** over the next 90: The Graph created **70.58M GRT** of new issuance and its Foundation vesting lock released **38.75M GRT**, while protocol burns removed only **59,127 GRT**. The structural mechanism is an uncapped reward of **120.73 GRT** per Ethereum block, now split between indexers and a Foundation fund, plus a ten-year lock that pays out every month until Dec 2030. GRT has no supply cap and no buyback, so its supply keeps growing unless governance lowers the issuance rate.

## The verdict, in one paragraph

Over the trailing 90 days (Jul 1 to Sep 29 2026) GRT sell pressure came to **109.33M GRT** against buy pressure of **59,127 GRT**, a net of **+1.00%** of the **10.94B GRT** circulating supply. For the next 90 days the framework projects **116.68M GRT** of sell pressure against the same burn, or **+1.07%**. Our supply monitor reads **+1.32%** for the same trailing window, a gap of **0.32 percentage points**, small enough that no data-conflict flag is shown. The Graph is inflationary by design on its float: two steady streams of new GRT, and a burn that removes less than one GRT for every thousand it adds.

## Sell pressure: where new GRT comes from

Protocol inflation is the largest row. The Graph mints **120.73 GRT** for every Ethereum block, and all of it now happens on Arbitrum One, where the protocol runs. We read every mint on Arbitrum across the window and removed the coins that only crossed the bridge from Ethereum: **70.58M GRT** was genuinely new. Of that, **63.25M** paid indexers and their delegators for serving subgraphs, **4.70M** went to the new Foundation innovation fund and **2.63M** went to a contract that now collects rewards indexers cannot claim.

That split changed inside the window. Since Sep 1 2026, one fifth of GRT issuance, **24.146 GRT** per block, is minted straight to the Foundation fund whether or not any indexer claims, and since late August 2026 rewards that used to be dropped are minted to the reclaim contract instead. Before Sep 1 about **746,000 GRT** a day was created; since then about **871,000 GRT** a day, which is the full protocol rate. The forward column therefore uses the full rate, **77.93M GRT** in 90 days, rather than the lower trailing figure.

Vesting unlocks are the second row. One lock from the December 2020 launch is still paying out: the Graph Foundation's ten-year allocation, which releases **12.92M GRT** a month. It paid on Jul 24, Aug 25 and Sep 23 2026, **38.75M GRT** in all, and still holds **658.75M GRT**. That lock is exactly the part of GRT the market does not count as circulating, so every release adds to the float. Three more releases, on Oct 17, Nov 17 and Dec 17 2026, give the same **38.75M GRT** for the next 90 days.

The Foundation and unscheduled row is **0**: the two Foundation funds hold coins that were already counted as new issuance when they were minted, so spending them does not add supply a second time. The long-term locked or bankruptcy row is also **0**: The Graph has no estate, no court schedule, and the early team, backer and Edge & Node allocations have finished vesting.

## Buy pressure: where new GRT goes

There is no programmatic buyback. No contract or treasury buys GRT on the market on Ethereum or Arbitrum, and a Sep 5 2026 forum post asking for a buy-and-burn had no sponsor and no vote, so the buyback row is **0**.

The protocol fee burn is real but tiny. The Graph burns 1% of query fees and a 1% tax on new curation signal. Read burn by burn on Arbitrum, those removed **59,127 GRT** in 90 days: **42,057** from query payments and **17,070** from curation. That is less than a tenth of one percent of the GRT minted in the same window. The forward column holds the same figure. Query traffic now served by the Foundation's own staging service moves onto the paid network from Oct 8 2026, which could lift the burn, but even ten times more fees would still leave the burn far below issuance.

The Foundation buy row is **0**: the Foundation receives and spends GRT and showed no market purchases in the window. The new long-term lock row is also **0**. About **1.93B GRT** is staked by indexers and delegators, but staked GRT stays inside the counted supply and can be withdrawn after a waiting period, so staking removes nothing from the float.

## Foundation and overhang

The largest team-controlled overhang is the Foundation vesting lock itself: **658.75M GRT** with 51 monthly releases left, already booked in the vesting row. Next is the new innovation fund created by the Sep 1 2026 governance change. It received **4.70M GRT** this window; the Foundation took **3.65M** out and **1.05M** is waiting. The reclaim contract holds **2.63M GRT** with nothing taken out yet, and the Foundation safe that receives each monthly release holds about **150,000 GRT**, because it passes the coins on. We read all four on-chain at every check.

We deliberately leave out exchange wallets and large unlabelled holders, which belong to depositors or to no identified group, and the Ethereum bridge escrow, which only backs GRT that already exists on Arbitrum. If any of the tracked Foundation balances falls between refreshes, the outflow enters the Foundation row at the next refresh.

## How GRT compares to other data-network tokens

GRT belongs to the class of work tokens for data and compute networks: operators stake the token to do work, and new tokens pay them for it. Livepeer pays its orchestrators the same way with an uncapped issuance, but ties the rate to how much of the supply is staked. GRT uses a fixed per-block amount instead, so the reward does not shrink when more GRT is staked, and it now diverts part of that amount to a Foundation fund, which a stake-linked design does not do.

Against burn-and-mint designs such as Render, where users burn the token to pay for work and new tokens are minted to operators, GRT's burn is only a 1% cut of fees, so usage barely touches supply. Against fixed-supply data tokens such as Chainlink, where supply growth comes only from releasing a pre-minted treasury, GRT has both kinds of pressure at once: a pre-minted Foundation lock still releasing, and a protocol that keeps minting. That combination is why GRT reads inflationary in this window and the next.

## What to watch in the next 90 days

The Foundation lock releases **12.92M GRT** on Oct 17, Nov 17 and Dec 17 2026; a late or skipped claim would move that month's release into the next window. From Oct 8 2026 query traffic on BNB Chain and Polygon moves from the Foundation's own service to the paid network, the first real test of whether fees and the burn can grow. A proposal from Sep 23 2026 would give a further 0.1% of issuance to a community group; it would not change total issuance, only who receives it. The planned split of 6 GRT per block to indexing agreements works the same way. A governance vote to lower the 120.73 GRT per block rate, or a change to the burn percentages, would change the reading; none is scheduled.

## Summary

GRT, the token of The Graph, is inflationary: supply grew **+1.00%** over the last 90 days and the framework projects **+1.07%** for the next 90, with **77.93M GRT** of new issuance and **38.75M GRT** of Foundation vesting against a burn of about **59,127 GRT**. The structural mechanism is a fixed, uncapped reward of 120.73 GRT per Ethereum block, a fifth of which has gone to a Foundation fund since Sep 1 2026. The key risk for holders is that nothing on the buy side is large enough to offset it: there is no buyback and the fee burn is under a tenth of one percent of issuance. The ceiling is set only by governance, since GRT has no supply cap and the Foundation lock keeps releasing until Dec 2030.

---

*MrNasdog Pressure Framework analysis of GRT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

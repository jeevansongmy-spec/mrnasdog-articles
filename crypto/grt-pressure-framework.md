---
title:         "GRT Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "GRT supply grows 0.99% over 90 days: 70.2M minted for indexing rewards and 38.8M released from a 2020 lock, against only 0.06M burned by protocol taxes."
canonical_url: "https://mrnasdog.com/research/grt/inflation"
tags:          ["crypto", "grt", "the-graph", "infrastructure"]
published:     true
---

Originally published at [GRT Inflation Analysis · September 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/grt/inflation).

# GRT Inflation Analysis · September 2026 · Supply growing · projected to keep growing

GRT supply is growing and is projected to keep growing. The Pressure Framework books **70.2M GRT** of freshly minted indexing rewards and **38.8M GRT** released from a single vesting lock against only **0.06M GRT** destroyed by protocol taxes, a net of **+0.99%** over the last 90 days and **+0.99%** projected forward, while the inflation monitor reads **+1.32%**. The Graph has no maximum supply, so the only brake on GRT is a burn that is currently about **450 times** smaller than the widely repeated one-percent-a-year claim.

## The verdict, in one paragraph

Against a circulating base of **10,941.3M GRT**, The Graph adds **108.9M GRT** of sell pressure and removes **0.06M GRT** of buy pressure over the trailing 90 days — a net of **+0.99%** — and projects the same **+0.99%** forward, because both mechanisms are running on unchanged settings. The inflation monitor reads **+1.32%** for the same window, a gap of **0.32 percentage points**, which sits inside the framework’s 0.5-point tolerance and therefore ships without a warning chip on the GRT overview. The label for GRT is an **uncapped work token with two live supply taps and a token burn that has not scaled with the network**: The Graph mints continuously to pay indexers, a decade-long lock keeps handing coins to the market every month, and the curation, delegation and query-fee burns are too small to matter yet.

## Sell pressure: where new GRT comes from

The larger tap is protocol issuance, and **Sell #1 is 70.2M GRT**. GRT is the ERC-20 work token of The Graph, but the live protocol and every reward mint now run on Arbitrum One, so the Ethereum contract’s total supply read **10,800,262,816.048214 GRT** at both ends of the window, flat to the wei, while the Arbitrum side did all the moving. Sweeping every mint event on Arbitrum across the window returns **141.4M GRT** created in total, of which **71.3M GRT** were bridge deposits — coins that already existed on Ethereum — leaving **70.2M GRT** of genuinely new issuance. Of that, **69.1M GRT** passed through the subgraph service contract to indexers and **1.07M GRT** went to a new innovation allocation that has not spent a coin.

A governance change landed inside the window and is worth stating precisely, because it looks like a cut and is not one. From **Sep 1 2026**, The Graph routes a fifth of protocol issuance — **24.146 GRT per block** — through an issuance allocator to the Foundation’s innovation allocation, leaving the rewards manager issuing **96.584 GRT per block** instead of the full **120.73 GRT per block**. Total GRT issuance did not change; only its destination split. That is why the framework does not re-base the forward projection. The scheduled rate would have minted **78.1M GRT** over the window against the **70.2M GRT** actually minted, because indexing rewards on The Graph only mint when an indexer closes an allocation, and work that fails the rewards eligibility check earns nothing.

The second tap is vesting, and **Sell #2 is 38.8M GRT**. A single Graph token lock wallet funded with **1,550M GRT** at the Dec 2020 token generation event pays out **12.92M GRT** a month on a 120-month straight line that ends **Dec 17 2030**. Three payouts landed inside the window, on **Jun 26 2026**, **Jul 24 2026** and **Aug 25 2026**, and the contract balance fell from **710.4M GRT** to **671.7M GRT** to match. No GRT is minted by a vesting unlock; the coins existed already. What matters is that this one contract is the entire non-circulating bucket — the classified float excludes **671.68M GRT** and the lock holds **671.67M GRT** — so every coin it releases crosses into the tradable market for the first time and counts exactly once.

**Sell #3, Foundation and unscheduled unlocks, is 0**: no identified project wallet released GRT beyond the monthly schedule, and the largest candidates sat still. **Sell #4, long-term locked or bankruptcy, is 0** as well — GRT has no estate, no trustee and no court-ordered distribution.

## Buy pressure: where new GRT goes

**Buy #1, programmatic buyback, is 0.** The Graph has never run one. The project’s own token documentation describes issuance and burns and nothing else, no repurchase contract exists on Ethereum or Arbitrum One, and no buyback proposal was open in the window. Pages on blogging platforms advertising a “GRT buyback and burn” programme are not project surfaces and were rejected.

**Buy #2, protocol fee burn, is 0.06M GRT**, and this is the row that deserves the most attention, because the gap between the mechanism’s reputation and its measured size is enormous. The Graph burns GRT in three places: about one percent of query fees, the one-percent curation tax a curator pays when signalling a subgraph, and the half-percent delegation tax. Measured across the whole window, those three destroyed **59,683 GRT** — **44,194 GRT** from payments, **15,488 GRT** from curation, and under one coin from delegation. Annualised that is roughly **0.0022%** of supply, against the frequently quoted figure of about one percent a year. Both destruction surfaces were checked at both window ends, because a burn is not always a supply-reducing call: the dead address on Arbitrum held nothing at either end, and the burn shows up instead as a fall in the token’s own total supply, so it is booked once rather than twice.

**Buy #3, Foundation buy, is 0** — no project wallet bought GRT on the open market. **Buy #4, new long-term lock, is 0** too. The staking contract holds **1,929.7M GRT**, which is nearly three times the entire non-circulating bucket, and that size test settles it: staked GRT is already counted inside the tradable float, so neither staking nor unstaking adds or removes supply in this reading. A liquid staking product announced on **Aug 25 2026** wraps the same stake and does not change it.

## Foundation and overhang

The dominant overhang is the vesting lock itself, holding **671.7M GRT** and releasing **12.92M GRT** a month until **Dec 17 2030**. It is read directly on-chain and refreshed every rebuild. Behind it sit three smaller pools. A project multi-signature wallet on Ethereum held **97.0M GRT** at both ends of the window without moving a single coin, and has no published release schedule. The Foundation’s new innovation allocation contract on Arbitrum One held **1.07M GRT**, every coin of it minted since **Sep 1 2026** and none of it spent. And the small safe the monthly release passes through held **83.3K GRT** at the start and **133.3K GRT** at the end while **38.8M GRT** flowed straight through it, which is what a pass-through looks like rather than an accumulation.

One balance that is deliberately not treated as overhang is the **2,562.1M GRT** sitting in the Ethereum-side bridge escrow. Those coins back GRT that already exists and already trades on Arbitrum One; counting them would double-count the network. The trigger rule for everything above is the same: if one of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How GRT compares to other uncapped work tokens

GRT belongs to the uncapped, continuous-issuance family, not the halving family. A halving-model chain with a hard cap can tell a holder exactly how much new supply exists in ten years. The Graph cannot, by design: it has no maximum supply and mints a roughly three-percent annual issuance to pay indexers for indexing subgraphs, reviewable downward by governance but not bounded by code. That makes GRT closer in shape to a staking-rewards L1 than to a fixed-supply settlement coin, and the comparison should be made on mechanism rather than on price.

Where GRT differs from most uncapped work tokens is that it advertises a burn, and where it differs from the exchange tokens that run quarterly auto-burns is that its burn is usage-linked rather than revenue-linked. An exchange token burning a fixed share of profits removes a predictable quantum every quarter regardless of on-chain activity. The Graph burns a slice of query fees, curation deposits and delegation deposits, so the burn only scales when subgraph queries and curation scale. Right now they have not, which is why **70.2M GRT** minted against **0.06M GRT** burned — a ratio of more than a thousand to one.

The second difference is the vesting tail. Many 2020-vintage tokens have finished their unlock schedules; three widely used unlock trackers even report GRT as fully unlocked. The chain disagrees, and the chain wins: a 120-month lock from Dec 2020 still has **52 months** to run. For a holder, that means GRT carries both an uncapped mint and a scheduled release at the same time, and the release is the more predictable of the two.

## What to watch in the next 90 days

Watch the monthly vesting payout, expected around **Oct 17 2026**, **Nov 17 2026** and **Dec 17 2026**, each about **12.92M GRT**; a missed month or a doubled claim is the single clearest signal in this ledger. Watch whether the innovation allocation contract starts spending its balance, because a distribution turns a parked **1.07M GRT** into live float. Watch the burn: a community proposal filed on **Sep 5 2026** asks The Graph Council to dedicate a quarter of qualifying protocol revenue to buying and burning GRT, which would be the first real buy-side mechanism this token has ever had — it has no sponsor and no vote yet. Watch the rewards eligibility oracle, since tighter enforcement lowers realised issuance below the scheduled **120.73 GRT per block**. And watch the **97.0M GRT** project multi-signature wallet, which has been motionless and has no published schedule.

## Summary

The Pressure Framework reads GRT at **+0.99%** over the trailing 90 days and **+0.99%** projected forward, against an inflation monitor reading of **+1.32%**. The mechanism is two simultaneous supply taps — **70.2M GRT** of indexing rewards minted on Arbitrum One and **38.8M GRT** released from a Dec 2020 vesting lock — against a protocol burn of just **0.06M GRT**. The key risk is that The Graph has no maximum supply, so the burn has to grow with query demand for the arithmetic to ever turn, and today it is more than a thousand times too small. The ceiling that does exist is the vesting lock: **671.7M GRT** remaining, **12.92M GRT** a month, finished **Dec 17 2030**.

MrNasdog Pressure Framework analysis of GRT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 20 2026.

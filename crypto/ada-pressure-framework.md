---
title:         "ADA Inflation Analysis · September 2026 · Supply was growing · trend cooling"
description:   "ADA supply grew 0.74% in 90 days: 112.6M ADA of reserve rewards plus 184.2M of voted treasury grants, less 19.9M returned. Next 90 days about +0.30%, no burn."
canonical_url: "https://mrnasdog.com/research/ada/inflation"
tags:          ["crypto", "ada", "cardano", "layer1"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/ada/inflation](https://mrnasdog.com/research/ada/inflation)*

# ADA Inflation Analysis · September 2026 · Supply was growing · trend cooling

**Cardano (ADA) supply grew about 0.74% in the last 90 days** and is on track to grow about **0.30%** in the next 90. Two flows did the work: the protocol reserve paid **112.6M ADA** to stakers, and holder-voted treasury grants released **184.2M ADA**, while **19.9M ADA** was sent back to the treasury. Nothing vests, nothing is burned, and ADA can never pass its **45B** maximum.

## The verdict, in one paragraph

Between Jun 28 2026 and Sep 26 2026 — the last 18 five-day epochs — Cardano added **296.8M ADA** of new circulating supply and took back **19.9M ADA**, a net of **276.9M ADA**, or **+0.74%** of the **37.54B ADA** in circulation. Our inflation monitor reads **+0.77%** for the same 90 days, a gap of **0.03** percentage points — well inside the half-point tolerance, so no warning chip is needed. For the next 90 days we book only the reserve rewards, **+0.30%**, because no treasury grant is close to passing. ADA is a slowly inflating proof-of-stake coin whose supply growth doubles in any quarter the treasury pays out.

## Sell pressure: where new ADA comes from

Protocol inflation is the steady flow. Cardano started with a fixed **45B ADA**, and the part not handed out at launch sits in a protocol reserve. Every epoch the reserve releases 0.3% of what it holds, scaled by how many blocks were made. A fifth of that goes straight to the treasury, and the part that cannot be paid — because not all ADA is staked and many pools are small — goes back into the reserve. What reaches pools and delegators came to **112.6M ADA** in 90 days, about **6.26M ADA** per epoch. That flow eases a little each epoch as the reserve shrinks: about 6.4M early in the window, about 6.1M now. The reserve still holds **6.10B ADA**, so this row keeps running for many years at a falling rate.

Vesting unlocks are **zero** and will stay zero. The 2017 sale and the allocations to the founding groups were all handed out at launch; every ADA outside the circulating count sits in either the reserve or the treasury, and the two together match the gap exactly.

Treasury grants were the bigger flow this window: **184.2M ADA** left the on-chain treasury after holder votes. The largest was **120M ADA** on Aug 17 2026 for a 12-month DeFi growth program; **25.4M ADA** went to Intersect, **18.3M ADA** to core infrastructure work on Jul 3 2026, and the rest to wallets, node software and other tools. Once the treasury pays, those coins count as circulating, even while they wait in contracts that release money step by step. For the next 90 days we book **zero** here: the only live request, **11.8M ADA**, has about 2% support against the two-thirds it needs.

Long-term locks and bankruptcy releases are **zero**. No estate, trustee or time-lock holds ADA waiting to be released.

## Buy pressure: where new ADA goes

Cardano has no buyback and no fee burn, so the usual buy rows are **zero**. Transaction fees are not destroyed: they join the epoch reward pot, most flows back to stakers, and a fifth goes to the treasury — about **0.13M ADA** this window, already netted inside the reserve row. No foundation or company bought ADA for the network this window. Staking removes nothing either: about **21.4B ADA** is staked, but staked ADA has no lock and stays inside the circulating count.

The one real buy-side flow is money going back. On Jul 2 2026 a treasury-funded contract returned **19.50M ADA** to the treasury, and about **0.42M ADA** more came back in smaller amounts — **19.9M ADA** in all. Coins sent back to the treasury leave the float until holders vote to spend them again. No further return is scheduled, so the next 90 days book zero.

## Foundation and overhang

The largest overhang is the treasury itself: **1.37B ADA**, outside the circulating count, spent only by holder vote. Its spending is capped: holders agreed a limit of **500M ADA** for Feb 13 2026 to about Jul 3 2027, and about **457.4M** of it is already used, leaving **42.6M ADA**. The reserve, **6.10B ADA**, is the source of the protocol inflation above and pays out on its fixed rule, not by anyone's choice.

Coins already paid out are inside the float and add nothing when they move. Contracts holding treasury grants that are still being paid to builders hold about **198M ADA**, and the Cardano Foundation reported **561M ADA** at the end of 2025 — fewer than a year earlier. We read the treasury and the reserve at every epoch boundary and walk the vote list by hand. If the treasury balance falls between our checks because a new grant is paid, that outflow enters the treasury-grant row at the next refresh.

## How ADA compares to other proof-of-stake Layer 1s

Among proof-of-stake Layer 1s, Cardano is unusual in two ways. First, it has a hard maximum: new ADA only comes out of a reserve that was set at launch, so issuance falls every epoch and stops at **45B**. Ethereum and most other staking chains have no cap and pay stakers from coins created on demand; Ethereum answers that with a fee burn, which Cardano does not have. Bitcoin also has a cap, but it cuts new supply in steps at each halving, while Cardano's reserve drains smoothly by a fixed share each epoch.

Second, Cardano runs an on-chain treasury that is funded from every epoch and spent only by holder vote. That makes its supply growth lumpy in a way a pure emission chain is not: in a quiet quarter ADA grows about **0.3%**, but in a quarter with large grants, like this one, the treasury can more than double that. A chain with a foundation that sells from its own wallet moves coins already counted; Cardano's treasury moves coins that were never counted, so each passed vote is real new supply.

What Cardano lacks is a sink. With no burn and no buyback, the only thing that takes ADA out of circulation is money returned to the treasury, which is rare and small. The mix is a falling, capped emission plus voted spending, with almost nothing on the buy side.

## What to watch in the next 90 days

The 11.8M ADA OpenZeppelin treasury request closes on Oct 11 2026; it has about 2% support today, and if it passed it would add about 0.03% to supply. Any new treasury request would take about a month of voting and would have to fit under the 42.6M ADA left in the current spending cap. Watch the 2027 budget talks, which opened in September 2026 with public debates on how to split treasury money; large 2027 grants would need a new cap and are more likely next year. The 120M ADA DeFi growth program reaches its month-four checkpoint around mid-December 2026: about 90M ADA of it is held back until its overseers approve the next stage, and if they do not, that money is due back in the treasury within 30 days, which would take it out of circulation. The next hard fork, which opens the Dijkstra era, has an early window of Dec 5 2026 to Jan 4 2027; nothing announced changes the reserve rate. A proposal to raise the target number of stake pools from 500 to 1,000 is being polled; it would change who earns rewards, not how many are paid.

## Summary

ADA supply grew **0.74%** in the last 90 days: **112.6M ADA** of reserve rewards plus **184.2M ADA** of voted treasury grants, less **19.9M ADA** returned to the treasury. The next 90 days look like **+0.30%**, because the reserve keeps paying and no grant is close to passing. The key risk is the treasury: **1.37B ADA** sits outside the float and every passed vote adds to supply, though the current cap leaves only 42.6M ADA until mid-2027. Supply can never pass **45B ADA**, and nothing is burned.

---

*MrNasdog Pressure Framework analysis of ADA, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

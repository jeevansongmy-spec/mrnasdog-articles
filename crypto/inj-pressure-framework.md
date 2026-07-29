---
title: "INJ Inflation Analysis · July 2026 · Supply growing, projected to keep growing"
description: "A MrNasdog Pressure Framework read of Injective (INJ): 1.32M INJ minted in 90 days at the 4.4% ceiling against only 0.14M burned. Framework +1.18% net; monitor +0.05%."
canonical_url: "https://mrnasdog.com/research/inj/inflation"
tags: ["crypto", "inj", "injective", "staking"]
published: true
---

> Originally published at **[mrnasdog.com/research/inj/inflation](https://mrnasdog.com/research/inj/inflation)** by MrNasdog.

Injective markets a burn, and the burn is real — but it is much smaller than the mint. Staking rewards minted about **1.32M INJ** over the last 90 days at the protocol's **4.4%** maximum rate, while the monthly Community BuyBack removed only about **0.14M INJ**, roughly a ninth as much. The Pressure Framework reads **+1.18% net** — mildly inflationary, not deflationary. Our supply monitor reads **+0.05%**, a gap of **1.13 percentage points**, because the market-data supply feed it uses is frozen at **100.0M INJ** while the chain has actually minted to **121.85M**.

## The verdict, in one paragraph

For the 90-day window ending Jul 30 2026, the Pressure Framework reads **INJ at +1.18% net**. Sell pressure is **1.32M INJ** of staking issuance, buy pressure is **0.14M INJ** of buy-and-burn, against a circulating base of **100M INJ**. Our supply monitor reads only **+0.05%**, a gap of **1.13 percentage points**, so a **monitor gap** chip ships on the INJ overview. The gap is not a disagreement about mechanism — it is a frozen data feed: the monitor derives supply from market cap over price, and that figure has been pinned near **100M INJ** across every daily snapshot in the window, even though the chain minted staking rewards at its 4.4% ceiling the whole time. Reading Injective's own nodes, total supply is **121.85M INJ** and rising. INJ is best characterised as **mildly inflationary on the real chain supply, with a genuine but out-matched burn** — the opposite of the "deflationary by design" label the buyback branding invites.

## Sell pressure: where new INJ comes from

Sell #1, protocol inflation, is **1.32M INJ**, and it is the entire sell side. Injective's mint module targets a bonded ratio of **60%**: when less INJ than that is staked, the inflation rate climbs toward its maximum; when more is staked, it falls toward its **2.2%** floor. Reading the chain directly, **57.15M INJ** of the **121.85M** total is bonded — a ratio of **46.9%** — so the rate has been pinned at the **4.4%** ceiling and cannot go higher. At the reported annual issuance of **5.36M INJ**, that works out to about **1.32M INJ** created over the 90-day window. Because the bonded ratio sat well below target for the whole period, the rate did not step during the window, so the trailing pace and the live pace are the same.

The remaining sell rows are all **zero**, and for structural reasons. Sell #2, vesting unlocks, is zero because Injective's unlock calendar is exhausted: INJ launched in **October 2020** on a four-year schedule, and the team, ecosystem and seed allocations finished releasing around **2024**, so no cliff falls inside this window. Sell #3, foundation and unscheduled unlocks, is zero because nothing was released — the tracked overhangs, the on-chain community pool and the Injective Foundation and ecosystem wallets, showed no outflow event in the trailing year. Sell #4, long-term locked or bankruptcy, is zero: there is no Injective estate, no trustee and no court-ordered INJ distribution.

## Buy pressure: where new INJ goes

Buy #1, programmatic buyback, is **0.14M INJ**, and it is the mechanism Injective is best known for. A slice of protocol revenue funds a monthly Community BuyBack — successor to the older weekly burn auction — that purchases INJ on the open market and permanently burns it. The rounds inside this window were about **$315,000** on **Jun 3 2026**, the largest to date, and about **$246,000** on **Jul 1 2026**; converted at prevailing prices and cross-checked against reported per-round burns of 37,000 to 55,000 INJ, that removes roughly **0.14M INJ** over 90 days. The tokens are destroyed rather than parked in a wallet, so there is no accumulation overhang to track. The decisive fact is scale: this real burn is about **a ninth** of the 1.32M INJ the mint added, so it softens the inflation but nowhere near cancels it.

The other three buy rows are **zero**. Buy #2, protocol fee burn, is zero because Injective has no separate EIP-1559-style base-fee burn — its exchange and trading-fee revenue is precisely what funds the Community BuyBack above, so counting a fee burn here would double-count the same money. Buy #3, foundation buy, is zero because no Injective Foundation open-market purchase distinct from the revenue-funded buyback has been disclosed. Buy #4, new long-term lock, is zero because staking is not a lock: bonded INJ can be withdrawn after a **21-day** unbonding period and stays inside the circulating figure the entire time.

## Foundation and overhang

Two team-controlled overhangs are tracked on Injective. The first is the on-chain **community pool**, a protocol treasury that accrues a share of activity and can only be spent by a passing governance vote; no INJ-denominated spend cleared it in this window. The second is the **Injective Foundation and ecosystem wallets**, which hold INJ earmarked for grants and growth and are monitored through disclosures rather than a single readable balance. Both are re-read on every rebuild, and if either balance falls between refreshes, the outflow enters Sell #3 at the next refresh. Neither has fired, which is why Sell #3 is zero rather than a projected number.

## How INJ compares to other proof-of-stake L1s

The first comparison is cap versus control loop. Halving-model chains with a hard ceiling have a sell side that shrinks on a published schedule; Injective has neither a fixed cap under INJ 3.0 nor a schedule. Its issuance is a control loop tied to how much INJ is bonded, and because bonding sits at 46.9%, well under the 60% target, the loop has parked at its 4.4% maximum. Like the uncapped Cosmos-family chains it descends from, INJ's inflation does not decay with time — it decays only if staking participation rises.

The second comparison is burn versus no burn, and this is where INJ stands apart from a plain staking chain. Unlike a network that returns every fee to stakers, Injective routes protocol revenue into a buy-and-burn, so activity genuinely removes supply. The catch is magnitude: the burn is real but it is roughly a ninth of the mint, so it does not flip the sign. That places INJ between the pure-mint proof-of-stake chains, which have nothing on the buy side, and the exchange tokens whose quarterly buybacks are large enough to print net-negative supply. INJ has the mechanism of the second group at the scale of the first.

The third comparison is what the market data shows. Many tokens carry heavy non-circulating buckets whose release calendar is the main risk; INJ's risk is subtler. Its published circulating figure has frozen at its old 100M cap while the chain quietly minted past 121.85M, so an observer trusting the headline supply would read INJ as flat when it is in fact growing. The framework reads the chain, not the frozen feed, which is the whole reason the two numbers disagree by more than a point.

## What to watch in the next 90 days

First, the bonded ratio: at **46.9%** against a **60%** target, the mint is stuck at its ceiling, and only a sustained rise in staking participation starts pulling issuance toward the 2.2% floor. Second, the monthly Community BuyBack size — rounds have climbed from around **$156,000** in the spring to **$315,000** in June, and a sustained step up in protocol revenue is the only thing on this ledger that could close the gap between mint and burn. Third, whether the widely-quoted circulating figure un-freezes from **100M**; the day the market data catches up to the real **121.85M**, the monitor gap on this page collapses on its own. Fourth, any governance proposal that changes the inflation band or the auction cadence, which would re-base both sides of this reading. Fifth, the community pool — the first INJ-denominated spend proposal is what would put a non-zero number in Sell #3.

## Summary

Injective (INJ) is mildly inflationary, not deflationary: staking rewards minted about **1.32M INJ** over 90 days at the protocol's **4.4%** ceiling, while the monthly buy-and-burn removed only about **0.14M INJ**, giving a framework reading of **+1.18% net** against a monitor reading of **+0.05%**. The rate is pinned at its maximum because the bonded ratio of **46.9%** sits below the **60%** target, and the burn — real and rising — is still about a ninth of the mint. The key risk to the reading is a data one: the widely-quoted circulating figure is frozen at **100M INJ** while the chain has minted to **121.85M**, so the market's headline understates how much INJ is actually being created.

---

*MrNasdog Pressure Framework analysis of INJ, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 30 2026.*

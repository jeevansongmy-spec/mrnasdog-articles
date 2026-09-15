---
title: "BTW Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description: "Bitway mints no BTW, yet its lock contracts released 508.1M BTW in 90 days against zero buyback and zero burn. Net +18.76% trailing, +11.26% next."
canonical_url: "https://mrnasdog.com/research/btw/inflation"
tags: ["crypto", "btw", "bitway", "defi"]
published: true
---

> Originally published at **[mrnasdog.com/research/btw/inflation](https://mrnasdog.com/research/btw/inflation)** by MrNasdog.

Bitway creates no new BTW — the token has no mint function and the count of BTW in existence read 10,000M at both ends of the last 90 days — yet the Pressure Framework reads BTW at **+18.76%** over the trailing 90 days and **+11.26%** over the next 90. All of it comes from one mechanism: monthly vesting unlocks out of on-chain lock contracts, which released **508.1M BTW** on **Aug 8 2026** and are scheduled to release **101.6M BTW** on the 2nd of every month. Sell pressure is **508.1M BTW**, buy pressure is **0**, and **7,291.9M BTW** of the fixed 10,000M supply is still locked.

## The verdict, in one paragraph

Against a circulating base of **2,708.1M BTW**, the framework books **508.1M BTW** of sell pressure and **0** of buy pressure over the trailing 90 days — a net of **+18.76%** — and projects **+11.26%** for the next 90 days from the unlock dates already written into the lock contracts. The inflation monitor reads **+23.75%** for the same window, a gap of **4.98 percentage points**, which is over the framework's 0.5pp tolerance and therefore ships with a monitor-gap warning on the overview page. The gap decomposes completely: **4.46pp** is base convention, because the monitor divides its supply change by the supply of 90 days ago while the framework divides by today's, and the remaining **0.52pp** is the monitor's market-derived supply estimate, whose starting base sits 11.9M BTW under the 2,200M launch float. The label for BTW is **a fixed-supply token in its unlock phase**: nothing is minted, but the tradable float is still being handed out.

## Sell pressure: where new BTW comes from

It does not come from minting. The BTW token on BNB Chain was created once, 10,000M BTW, and its code carries a burn function but no mint function; the supply figure lives in ordinary storage and read exactly 10,000M at both window ends, so the flat reading is a real measurement rather than a constant. **Sell #1, protocol inflation, is 0.** Bitway's own Proof-of-Stake chain, Bitway Ledger, keeps a separate native balance with a staking emission, but no path links it into the traded BTW token, and that chain has produced no blocks since **Aug 16 2026**. Because the token still has an owner key, the row is watched rather than closed.

The supply story is **Sell #2, vesting unlocks, at 508.1M BTW**. Every locked BTW sits in four lock contracts on Ethereum — Community, Ecosystem, Team and Backers — and each contract carries its own monthly unlock calendar, the same one Bitway's whitepaper publishes. The Community pool releases 60.2M BTW a month and the Ecosystem pool 41.5M BTW a month, starting Apr 2 2026. Bitway did not claim them monthly: it claimed five months at once on **Aug 8 2026**, pulling **508.1M BTW** out of the locks, bridging it to BNB Chain and parking it in one project wallet, where it has not moved since. The locks' combined balance fell by exactly that amount, to the token. The framework counts tokens that have left a readable lock, so the whole 508.1M enters this row. The Sep 2 2026 tranche of 101.6M BTW has already unlocked but has not been claimed yet.

**Sell #3, Foundation and unscheduled unlocks, is 0.** No BTW left a locked pool beyond the vesting release above. Project wallets did send 2.4M BTW to outside addresses during the window, mostly in reward payouts on Jul 21 and Sep 15 2026, but those coins were already counted as circulating supply, so the payouts move BTW inside the float rather than adding to it. The same goes for the 200M BTW the project brought back from Ethereum into its multisig on Jul 22 2026. **Sell #4, long-term locked or bankruptcy, is 0**: BTW has no bankruptcy estate and no court-ordered distribution.

## Buy pressure: where new BTW goes

Nowhere, this window. **Buy #1, programmatic buyback, is 0** — Bitway earns management, performance and lending fees, but no programme spends that revenue buying BTW, and none was announced or executed. **Buy #2, protocol fee burn, is 0.** The framework read both burn surfaces at both window ends: the count of BTW in existence did not move, and the dead address gained less than one BTW. BTW sent to the token contract itself rose to 1.4M, but those coins were moved, not destroyed. The fall in BTW supply on Ethereum is the bridge sending coins back to BNB Chain, not a burn.

**Buy #3, Foundation buy, is 0**: no project wallet bought BTW on the market. **Buy #4, new long-term lock, is 0**, and staking went the other way — BTW held in Bitway Earn's staking vaults fell from **7.0M** to **0.6M**. The August and September 2026 staking campaigns pay yield on stablecoins, so they lock no BTW.

## Foundation and overhang

The Bitway overhang is large and almost entirely in the project's own hands. The biggest item is the lock contracts themselves: **7,291.9M BTW**, of which the Team pool holds 2,000M and the Backers pool 1,633.2M, both locked until **Mar 2 2027**. Next is the project multisig with **1,202.4M BTW**, then the project wallet still holding the **508.1M BTW** claimed in August, then five distribution wallets holding **337.2M BTW** between them, plus the unclaimed Sep 2 2026 tranche of **101.6M BTW**. All of them are read from the chain at every rebuild. There is no buyback wallet to track and no bankruptcy residual.

What matters about this overhang is that the release dates are written into contracts, but the claiming and the spending are not. Bitway can let tranches pile up and claim them together, as it did in August, and a claimed tranche can sit in a project wallet for weeks. The trigger rule applies to every item: if the lock contracts, the multisig, the project wallet or the distribution wallets fall between refreshes by more than the schedule and internal moves account for, that outflow enters Sell #3 at the next refresh.

## How BTW compares to other newly launched vesting tokens

BTW belongs to the largest class on the market: a token launched with a fixed supply and a small float, where most of the supply is released to the community, ecosystem, team and investors over four years. On the issuance axis BTW is strict — no mint function, no staking emission on the traded token — which puts it closer to a hard-capped coin than to a continuous-emission layer 1 that pays stakers 5% to 20% a year in new coins. On the float axis it is the opposite: only 27% of all BTW is circulating, so every monthly tranche is large against the float.

Compared with a mature capped coin like Bitcoin, which adds a fraction of a percent a quarter, BTW adds double digits, and the reason is unlock, not inflation. Compared with other recent launches, the BTW schedule has one feature worth knowing: its unlocks are claimed in batches rather than on the calendar date, so a quarter can show a large one-day release after several quiet months. The bigger step comes on **Mar 2 2027**, when the Team and Backers pools begin releasing about 123.6M BTW a month on top of the Community and Ecosystem tranches.

Against exchange-style tokens that run quarterly buybacks and burns, BTW has nothing on the buy side. Bitway's products earn fees, but none of that revenue is routed into BTW, so there is no removal mechanism that scales with usage to offset the unlocks.

## What to watch in the next 90 days

First, the three scheduled tranches of **101.6M BTW** on **Oct 2 2026**, **Nov 2 2026** and **Dec 2 2026** — they unlock in the lock contracts on those dates whether or not Bitway claims them the same day. Second, the unclaimed Sep 2 2026 tranche, which can be claimed at any time. Third, the project wallet holding the **508.1M BTW** claimed on Aug 8 2026: if it starts paying out, those coins move from the project into other hands. Fourth, the project multisig at **1,202.4M BTW**, which has no calendar of its own. Fifth, the lock contracts are upgradeable and their owners can change the schedules, so any change to the unlock calendar would move this reading directly.

## Summary

The MrNasdog Pressure Framework reads BTW at **+18.76%** over the trailing 90 days and **+11.26%** projected forward: supply growing, projected to keep growing. The mechanism is not minting but vesting — Bitway's token cannot be minted, while lock contracts on Ethereum release 101.6M BTW a month and released 508.1M BTW in one claim on Aug 8 2026. The key risk is the size of the remaining overhang: 7,291.9M BTW still locked and more than 2,000M BTW in project wallets, against a buy side of zero. The ceiling is a fixed 10,000M BTW, and the Team and Backers pools stay locked until Mar 2 2027.

*MrNasdog Pressure Framework analysis of BTW, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 15 2026.*

---
title:         "FIL Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description:   "Filecoin put 35.26M FIL on the market in 90 days; the mint was 5.42M. Vesting 16.84M, collateral 13.00M, burn 649.1K. Net +4.18%, next +2.74% as vesting ends."
canonical_url: "https://mrnasdog.com/research/fil/inflation"
tags:          ["crypto", "fil", "filecoin", "storage"]
published:     true
---

> Originally published at **[mrnasdog.com/research/fil/inflation](https://mrnasdog.com/research/fil/inflation)** by MrNasdog.

Filecoin's FIL supply is growing, and new coins are the smallest part of it. The MrNasdog Pressure Framework reads FIL at **+4.18%** over the trailing 90 days and **+2.74%** over the next 90: **35.26M FIL** of sell pressure — launch vesting, storage collateral handed back and the block-reward mint — against **649.1K FIL** burned and no buyback. The six-year launch vest ends on **Oct 14 2026**, which is why the forward number falls, and the whole supply sits under a hard protocol cap of **2,000M FIL**.

## The verdict, in one paragraph

Against a circulating base of **827.8M FIL**, the framework books **35.26M FIL** of sell pressure and **649.1K FIL** of buy pressure over the trailing 90 days — a net of **+4.18%** — and projects **+2.74%** for the next 90 days. The inflation monitor reads **+4.72%** for the same window, a gap of **0.54 percentage points**, just over the framework's 0.5pp tolerance, so the overview page carries a monitor-gap warning. The gap splits cleanly: **0.20pp** is base convention, because the monitor divides by the supply of 90 days ago while the framework divides by today's, and **0.34pp** is the monitor's supply estimate rising **2.7M FIL** faster than the chain's own circulating figure. The label for FIL is **a capped chain still paying out its launch allocation and its storage collateral**: the mint is shrinking, but the float is not.

## Sell pressure: where new FIL comes from

Sell #1, protocol inflation, is **5.42M FIL**. Filecoin mints new FIL every 30 seconds as block rewards for the storage providers who prove they are holding data. The chain's reward pot paid out exactly that much between Jun 20 2026 and Sep 18 2026, and the pace fell in every two-week slice of the window as total network storage shrank. A provider receives a quarter of each reward at once; the other three quarters unlock day by day over 180 days, and that locked part reaches the market through Sell #4 when it frees up.

Sell #2, vesting unlocks, is the largest tap at **16.84M FIL**. At launch Filecoin set aside **409.8M FIL** for Protocol Labs, its team and the Filecoin Foundation, vesting in a straight line over six years. That works out to **187.1K FIL** a day, and the chain's own vested figure rose by exactly the scheduled amount over the window, to the coin. Vested FIL counts as tradable the moment it vests, so later moves between team wallets add nothing. The schedule ends on **Oct 14 2026** (the project's own post says Oct 15), with only **4.92M FIL** still to come.

Sell #3, Foundation and unscheduled unlocks, is 0: the Filecoin mining reserve did not move a single coin, and no other team pot has a release on record this window. Sell #4, long-term locked or bankruptcy, is **13.00M FIL**. Storage providers lock FIL as collateral for every sector they store and get it back when the sector ends. Locked FIL fell from **76.95M** to **63.95M** as capacity retired — network storage power fell about 18% and the count of active storage providers dropped from **617** to **499**. That release arrived in bursts, with **5.61M FIL** between Jul 20 and Aug 4 2026 alone. Filecoin has no bankruptcy estate.

## Buy pressure: where new FIL goes

Buy #1, programmatic buyback, is 0. Nothing in the Filecoin protocol spends storage revenue buying FIL, and neither the Filecoin Foundation nor Protocol Labs runs a repurchase programme. A website advertising an official Filecoin buyback at many times the market price is not a project channel, and the framework ignores it.

Buy #2, protocol fee burn, is **649.1K FIL**. Network fees, per-sector fees and penalties for dropped storage all go to a burn account nobody can spend from, and it rose from **42.31M** to **42.96M FIL** across the window. That is one sink read one way, so it is counted once. It offsets about an eighth of the new mint and under 2% of everything arriving. Buy #3, Foundation buy, is 0. Buy #4, new long-term lock, is 0: providers did lock fresh collateral, but less than they got back, so the net release is booked once, in Sell #4.

## Foundation and overhang

The largest overhang is the Filecoin mining reserve, **282.9M FIL**, unchanged at both ends of the window. It sits outside the float and can only be spent through a network upgrade; a community proposal to burn it instead is still an open discussion with no proposal number. The second is the seven launch vesting wallets of Protocol Labs and the Filecoin Foundation, which hold **12.9M FIL**, **3.6M** of it not yet vested. They paid **14.85M FIL** out to other team wallets this window — already counted as float when it vested, so not a new release. Both are read from the chain at every rebuild. If either balance falls between refreshes by more than the schedule accounts for, that outflow enters Sell #3 at the next refresh.

## How FIL compares to other capped, collateral-heavy chains

FIL has a hard cap of **2,000M FIL**, like Bitcoin, but it does not release it like Bitcoin. Bitcoin mints on a halving clock and has nothing locked, so its inflation reading is small and falls on a known date. Filecoin mints on a decaying curve tied partly to network storage, and it adds two taps Bitcoin lacks: a launch vest and a large collateral pool that grows when storage is added and flows back when it leaves. Right now the collateral tap runs outward, because network storage is shrinking.

Against staking chains, the collateral works the other way round. On a proof-of-stake chain, locking coins is a choice, and new stake usually grows with the price. On Filecoin, locking is a cost of storing data, so it follows the storage business rather than the market, and it is falling as storage leaves. Against exchange tokens with buybacks, Filecoin's burn is small: it removes fees and penalties, and does not grow with revenue.

The accepted Solstice upgrade (FIP-0118) would change that. It splits each block reward between storage providers, a service fund and a burn, with the burn share rising over about nine quarters unless paid storage demand reaches its targets.

## What to watch in the next 90 days

First, the end of launch vesting on **Oct 14 2026**: after the last **4.92M FIL**, Sell #2 is zero for good. Second, the Solstice upgrade, with a planned mainnet start of **Oct 12 2026** that is not yet final. Its first quarter burns nothing extra, but it makes every new sector count at ten times its raw size, which could raise the collateral new storage must lock. Third, collateral returns, which ran at **13.00M FIL** this window and move in bursts. Fourth, the mining reserve at **282.9M FIL**, where any move would be a network upgrade. Fifth, the burn account, which a larger burn share would start to fill faster.

## Summary

The MrNasdog Pressure Framework reads Filecoin's FIL at **+4.18%** over the trailing 90 days and **+2.74%** projected: supply growing, projected to keep growing. The mint is the smallest tap at **5.42M FIL**; launch vesting added **16.84M** and returned storage collateral **13.00M**, against a **649.1K FIL** burn and no buyback. The key risk is the collateral tap, which has no end date and grows as network storage shrinks. The comfort is the calendar and the cap: launch vesting ends on **Oct 14 2026**, and total FIL can never pass **2,000M**.

---

*MrNasdog Pressure Framework analysis of FIL, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 18 2026.*

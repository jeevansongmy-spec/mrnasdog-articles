---
title:         "CC Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description:   "Canton mints 1.92B CC per 90 days and burns 1.25B paying network traffic. The Pressure Framework reads +1.84% net — an uncapped burn-and-mint token whose mint still leads."
canonical_url: "https://mrnasdog.com/research/cc/inflation"
tags:          ["crypto", "cc", "canton", "rwa"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/cc/inflation](https://mrnasdog.com/research/cc/inflation)*

# CC Inflation Analysis · August 2026 · Supply growing, projected to keep growing

Canton Coin is an **uncapped burn-and-mint token** with no pre-mine and no vesting: over the 90 days to **Aug 23 2026** the Canton Network minted **1.92B CC** as activity rewards, governance voted a further **93M CC** out of the unminted reward pool, and **1.25B CC** was burned paying Global Synchronizer traffic. Net of a **34M CC** new lock, that is **+1.84%** on a **39.41B CC** base. The governance vote that would have switched app rewards to traffic-based measurement on **Aug 18 2026** was **voted down** — the mint runs on exactly the mechanism it ran on before.

## The verdict, in one paragraph

For the 90-day window ending **Aug 23 2026**, the MrNasdog Pressure Framework reads Canton Coin at **+1.84% net** — a sell side of **2.01B CC** against a buy side of **1.29B CC**, leaving **724M CC** of new float on a circulating base of **39.41B CC**. Our independent supply monitor reads the same window at **+2.03%**, a gap of **0.20 percentage points** — inside tolerance, so no monitor-gap flag ships. The framework figure is built from the Canton Network's own mining-round record, and the core identity closes to the coin: mint minus burn over the window is **665M CC**, and the chain's cumulative supply series moved by exactly the same **665M CC**. Canton Coin is **structurally inflationary while the mint leads the burn**, and the whole question is whether institutional traffic on the Canton Network can close a gap of roughly **720M CC** a quarter.

## Sell pressure: where new CC comes from

Sell #1 — protocol inflation — is the bulk of the sell side at **1.92B CC** over 90 days. The Canton Network mints fresh Canton Coin in mining rounds roughly every ten minutes and pays it to whoever did measured work. The split is the story: **1.41B CC** went to application providers, **257M CC** to Super Validators and **248M CC** to validators, so nearly three quarters of new Canton Coin lands with the apps generating transactions rather than with infrastructure. The issuance curve caps how fast this runs — **40B CC** a year at genesis, **20B** from six months, **10B** from eighteen months, **5B** from year five and **2.5B** from year ten. Canton Network sits in the **10B CC** tranche until **Jun 26 2029**, which allows **2.47B CC** in a 90-day window; only **78%** of that was actually created, because unearned budget is never minted.

Sell #3 — Foundation and unscheduled unlocks — is the row that changed this quarter, at **93M CC**. Reward entitlement nobody claimed accumulates in an unminted pool, and Super Validators can vote slices of it into circulation when a partner completes a published milestone. Fourteen such votes landed inside the window: **25.4M CC** on **Aug 22 2026**, **19.6M CC** on **Aug 12 2026**, **19.2M CC** on **Jul 31 2026** and eleven smaller ones. This is genuinely new float — coins crossing out of a non-circulating pool and into the market — and it reconciles the two supply reads: the live circulation figure sits **99.5M CC** above the reward-only series, which these milestone mints plus one day of net supply account for almost exactly.

The remaining two sell rows are **zero**. Sell #2, vesting unlocks, is zero because Canton Coin had a fair launch — no pre-mine, no venture allocation, no team cliff — so there is no locked allocation for a calendar to release. Sell #4, long-term locked or bankruptcy, is zero because no estate, trustee schedule or frozen tranche touches Canton Coin, and none can be created.

## Buy pressure: where new CC goes

Buy #2 — protocol fee burn — is almost the whole buy side, at **1.25B CC** over 90 days, every coin of it from traffic purchases on the Global Synchronizer. Canton Network fees are quoted in dollars but settled by destroying Canton Coin outright: there is no fee recipient anywhere in the model. Two properties make this burn unusual. It scales with institutional settlement rather than speculation, and because the fee is dollar-denominated, a falling CC price burns **more** coins for the same activity. The burn is also accelerating inside the window — **12.8M CC** a day across the first month, **15.6M CC** a day across the last two weeks — and it currently erases **65%** of the mint.

Buy #4 — new long-term lock — is **34.1M CC**, and it is where the framework parts company with the headlines. Since **May 20 2026** a featured app must post **5M CC** per identity, or **25M CC** if it issues assets, to keep earning rewards, unwinding at only one-sixtieth a day. Press coverage reports more than **1B CC** locked with 85-plus apps compliant. Reading the lock contracts directly on **Aug 23 2026** returns something else: across **121** featured-app identities and every wallet named for locking, genuine on-chain locks total **34.1M CC** spread over **8** parties, all of them created inside this window. A further **119M CC** sits in segregated lock-named wallets as ordinary spendable balance — designated, not locked. Against a floor of **605M CC** for 121 apps, that is real compliance of about **6%**. Only the verified locks are booked. Buy #1, programmatic buyback, and Buy #3, Foundation buy, are both **zero**: Canton Network destroys fees rather than recycling them into purchases, and no discretionary open-market buying was disclosed or observed.

## Foundation and overhang

Canton Coin has an unusually thin overhang for a token of its size, because there was never an allocation table to hang one on. The largest by far is the **unminted reward pool** — entitlement the issuance curve allowed but nobody earned. It grew by **548M CC** over these 90 days against **242M CC** drawn from it by governance since **Feb 2026**, so it is filling faster than it drains, and it is refreshed from the governance record on every rebuild. Second, the Global Synchronizer Foundation's own wallets, holding about **25.6M CC** with nothing locked. Third, the featured-app lock pool described above, refreshed by direct contract read. Two further parties hold **1.33B CC** and **1.30B CC** respectively, but both are custodial third parties rather than project-controlled reserves, so they are watched and not booked. If any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How CC compares to other uncapped burn-and-mint chains

Canton Coin belongs to the burn-and-mint family rather than the hard-cap family — the same structural class as an uncapped smart-contract L1 with a fee burn, and the opposite of a halving chain whose supply path is fixed in advance regardless of usage. In a hard-cap chain the schedule is the answer; in Canton Coin's design the schedule is only the ceiling and usage decides, which is why the mint came in at **78%** of its allowance rather than at 100%.

Against other fee-burn L1s, Canton Coin's burn is far larger in relative terms — it destroys about **3.2%** of circulating supply every 90 days while returning about **5.1%** as rewards — but its mint is also far larger, because Canton Network pays apps directly rather than only validators. Against exchange tokens that buy and burn from profit, the difference is that Canton Coin's burn needs no discretionary decision and no treasury: it is a byproduct of settlement. And against the fair-launch tail-emission coins, the resemblance is the absence of investor unlocks — no vesting cliff can ever hit this token, which is why its sell side is two live rows rather than four.

The structural verdict follows from the arithmetic. Canton Coin turns deflationary only when the traffic burn passes the live mint: that burn runs near **1.25B CC** a quarter, or **5.1B** annualised, against a **7.8B** annualised mint plus the governance draw. Closing the gap needs roughly a **55%** rise in on-chain fee activity — or the next issuance step-down, which is years away. The long-run model settles near **2.5B CC** a year from year ten, a level today's burn would already clear twice over.

## What to watch in the next 90 days

The clearest near-term item is **Aug 29 2026**, when Super Validators vote on removing featured-app status from an app that failed the locking rule — enforcement is live, and every removal releases posted capital back toward the float. The traffic-based app-reward switch is the larger swing: it was rejected **3-7** on **Aug 18 2026** and now runs in dry-run only, with no activation date announced, so the day it passes is the day the forward mint must be re-based off a post-change run rate. The milestone-mint stream is the third watch line — it has fired fourteen times in 90 days and each vote publishes its quantum on the governance record before it lands, so Sell #3 is forecastable rather than a surprise. The tokenized settlement expansion targeted for **Oct 2026** is the largest potential burn catalyst, because settlement volume converts directly into destroyed Canton Coin. Finally, the burn has climbed every month inside this window while the mint has barely moved; a quarter where burn passes **1.7B CC** would be the first real sign of the equilibrium arriving.

## Summary

The MrNasdog Pressure Framework reads Canton Coin at **+1.84% net supply growth** over the last 90 days and the same rate over the next 90, against an independent monitor read of **+2.03%** — a **0.20 percentage point** gap, well inside tolerance. The structural mechanism is a usage-metered mint of **1.92B CC** a quarter, plus **93M CC** voted out of the unminted reward pool, set against the largest fee burn in crypto at **1.25B CC** — with no vesting, no foundation stockpile and no bankruptcy estate anywhere in the ledger. The key risk is that the burn depends on institutional traffic that has not yet scaled to match the reward schedule, and the widely-repeated claim that over **1B CC** is locked by apps does not survive a direct contract read. The ceiling is the protocol's own issuance curve — **10B CC** a year until 2029, then **5B**, then **2.5B** — so Canton Coin's path to deflation runs through usage, not through scarcity.

---

*MrNasdog Pressure Framework analysis of CC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 23 2026.*

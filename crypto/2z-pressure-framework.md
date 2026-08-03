---
title: "2Z Inflation Analysis · August 2026 · Supply growing, projected to grow sharply"
description: "DoubleZero mints no 2Z under its 10B cap, but a ~1,620M 2Z cliff unlocks Oct 2 2026. Framework +0.85% net trailing, ~+48% forward; monitor reads flat."
canonical_url: "https://mrnasdog.com/research/2z/inflation"
tags: ["crypto", "2z", "doublezero", "depin"]
published: true
---

*Originally published at [mrnasdog.com/research/2z/inflation](https://mrnasdog.com/research/2z/inflation)*

DoubleZero mints no new **2Z** — the full **10,000,000,000 2Z** was created at the October 2025 launch, the on-chain supply is actually net-burning, and no lockup wallet moved for most of the window. Over the trailing 90 days the only supply that reached the market was about **30M 2Z** from a single foundation deployment on **Jul 17 2026**, leaving the framework at **+0.85%** net. But a first-anniversary vesting cliff of about **1,620M 2Z** unlocks on **Oct 2 2026**, inside the next window, against a float of only **~3,470M 2Z** and a buy side of essentially **0.5M** — pushing the forward reading to roughly **+47.5%** net.

## The verdict, in one paragraph

For the 90-day window opening **Aug 3 2026**, the MrNasdog Pressure Framework reads **2Z at +47.5% net** forward, a dramatic step up from the **+0.85%** it measured over the trailing 90 days. The difference is one dated event: the **Oct 2 2026** first-anniversary unlock releases about **1,620M 2Z** — nearly half the current float — from cliff-vesting lockups. Our supply monitor reads the trailing window at about **0.00%**, a gap of roughly **0.85 percentage points**, outside the framework's 0.5-point tolerance, so a monitor-gap chip ships on the 2Z overview. The deep walk reconciled it cleanly: the framework counts the **30M 2Z** that left the foundation vault on **Jul 17 2026** as supply reaching the market, while the classifier feeding the monitor already treats unmoved foundation holdings as circulating, so a transfer out of the vault changes nothing on its side. Both are internally correct; they measure different things. 2Z is best characterised as **a fixed-supply token sitting quiet on a thin float directly ahead of a very large cliff unlock**.

## Sell pressure: where new 2Z comes from

Sell #1 — protocol inflation — is **zero**. All **10,000,000,000 2Z** were minted at the October 2025 token generation event, and the on-chain supply reads **9,998,220,695** — below the launch mint, because the token has net-burned about **1.78M 2Z** since. DoubleZero has published plans for network-reward inflation to pay validators and fiber contributors, but that mint is scoped to a staking layer that is not yet live, so no fresh 2Z is being created. Every token that reaches the market is a coin that already exists, simply unlocking.

Sell #2 — vesting unlocks — was **zero** over the trailing 90 days: the lockup wallets have been static since launch, and an on-chain read this rebuild confirmed the largest holder, a **1,750M 2Z** wallet, has not moved since 2024. But DoubleZero uses cliff vesting on a four-year Standard Lockup, and the first-anniversary cliff on **Oct 2 2026** releases about **1,620M 2Z** at once — the first 25% of every locked bucket, itemised as roughly **574M** Jump Crypto, **350M** Malbec Labs, **300M** Institutions, **250M** Team and the balance to Contributors and Builders, and cross-checked against a **1.66B** aggregator headline. Because a future cliff has not yet released, the framework books the scheduled quantum for the forward window and flags it. Against a **~3,470M** float, that is why the forward net jumps to **+47.5%**.

Sell #3 — foundation and unscheduled unlocks — is **30M 2Z**, the only discretionary move on-chain this window. The DoubleZero Foundation and Ecosystem vault sent about **30M 2Z** out on **Jul 17 2026**, dropping its balance to **1,269,606,501**, and a similar pace is projected forward. Behind it sits an enormous overhang: about **6,530M 2Z**, roughly two-thirds of the supply, is still locked across **Jump Crypto (~2,800M)**, **Malbec Labs (~1,400M)**, the Foundation treasury, **Institutions (~1,200M)** and **Team (~1,000M)**. Most of it is on the four-year calendar, and the part leaving on Oct 2 is counted under vesting above. Sell #4 — long-term locked or bankruptcy — is **zero**: there is no bankruptcy estate, and the remaining lockups run to 2029.

## Buy pressure: where new 2Z goes

Buy #1 — programmatic buyback — books **zero**, and the reason is a funding change. DoubleZero converts network revenue into open-market 2Z buys, distributing **90%** to infrastructure contributors and permanently burning **10%**. That buyback used to be funded by a **5%** validator block-reward fee worth roughly **$3.5M** a year, but that fee was eliminated at epoch 939 earlier in 2026. Its replacement, DoubleZero Edge — a paid Solana market-data subscription service — earns only about **$205K** annualised from a handful of test seats, and no purchase wallet is published. With a single unconfirmed figure and no on-chain trace, Buy #1 stays zero and monitored.

Buy #2 — protocol fee burn — is **0.5M 2Z**, small but real. It is measured directly from the mint's on-chain supply falling below the **10,000,000,000** launch figure — the network's integrity burn plus the 10% slice of whatever buyback runs. At about **0.5M** over 90 days it removes nowhere near enough to offset the vesting on the sell side. Buy #3 — foundation buy — is **zero**: no discretionary open-market 2Z buying outside the revenue-funded buyback. Buy #4 — new long-term lock — is **zero** as well; supply is moving out of lockups on the vesting calendar, not into new ones, and 2Z staking is not yet live.

## Foundation and overhang

The team-controlled overhang is the defining fact about 2Z. Around **6,530M 2Z** — about two-thirds of everything that will ever exist — has not yet reached the float, and it is concentrated in a few identifiable buckets: **Jump Crypto** at 28% of supply, **Malbec Labs** at 14%, the **Foundation and Ecosystem** treasury at 29%, **Institutions** at 12% and the **Team** at 10%. The Foundation vault at **1,269,606,501 2Z** is the only pool that has fired so far, and every balance is read on-chain each rebuild. If any of them leaves its lockup into the market ahead of schedule between refreshes, the outflow enters Sell #3 at the next refresh.

## How 2Z compares to other DePIN infrastructure tokens

2Z belongs to the venture-backed **DePIN infrastructure** class — physical-network tokens like the decentralized-wireless and compute projects — and within that class it sits at the fixed-cap, cliff-heavy end. Unlike a proof-of-work chain that mints genuinely new coins forever, DoubleZero will never create a ten-billion-and-first 2Z; its dilution has a hard ceiling and an end date on the vesting calendar. What separates it from a smoothly-emitting network is the shape of the release: a large share of supply is held by a few backers — **Jump Crypto**, **Malbec Labs** and institutions — behind discrete anniversary cliffs rather than a gentle, steady drip.

That cliff structure is why the framework reading swings so hard between windows. A continuous-emission L1 or a linear-vesting governance token would show a steady few-percent inflation every quarter; 2Z shows a near-flat **+0.85%** trailing and then a single **+47.5%** forward window when the **Oct 2 2026** cliff enters view. The comparison to an exchange token running a quarterly buy-and-burn is also unflattering for now: those tokens convert real cash flow into a shrinking supply, whereas DoubleZero's buyback lost its main funding at epoch 939 and its Edge replacement has yet to earn at scale.

On timing, 2Z is very early on its curve — roughly two-thirds of the supply is still unreleased, so the vesting row will dominate its inflation profile for years, front-loaded by the anniversary cliffs. The honest reading is that 2Z's inflation is fully knowable from the schedule and, on the forward window, clearly and heavily positive. The open question is whether Edge revenue can grow the buyback into anything large enough to matter against unlocks measured in the billions.

## What to watch in the next 90 days

The single event that dominates everything is the **Oct 2 2026** first-anniversary cliff of about **1,620M 2Z** — watch both the exact quantum that actually unlocks on-chain and how much of it moves to exchanges afterward, because tradable and sold are not the same. Watch the Foundation vault, whose **Jul 17 2026** deployment set the trailing sell number; any further outflow lands in Sell #3 at the next refresh. Watch DoubleZero Edge subscription revenue, since the whole buyback-and-burn is now funded by it and only a real ramp can lift the buy side above a rounding error. And watch for any activation of the planned network-reward inflation, which would turn Sell #1 from a structural zero into a live emission.

## Summary

DoubleZero is a fixed-supply, zero-mint DePIN token whose float barely moved over the trailing 90 days — only about **30M 2Z** left a foundation vault on **Jul 17 2026**, for a framework net of **+0.85%**, while the supply monitor reads a flat **0.00%** because it already counts unmoved foundation holdings as circulating. But the calm ends on **Oct 2 2026**, when a first-anniversary cliff releases about **1,620M 2Z** — close to half the **~3,470M** float — pushing the forward reading to roughly **+47.5%** net against a burn of just **0.5M**. The buyback that might have absorbed some of that lost its validator-fee funding at epoch 939, and its Edge-revenue replacement is not yet material. Until Edge scales, 2Z's inflation is governed almost entirely by a cliff-heavy vesting calendar, and the next 90 days carry its first big step.

*MrNasdog Pressure Framework analysis of DoubleZero (2Z), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated August 3, 2026.*

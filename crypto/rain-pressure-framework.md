---
title: "RAIN Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description: "Supply growing, projected to keep growing: RAIN reads +12.21% over 90 days. Rain Protocol mints nothing, but its lockup released 93,706M RAIN into the float."
canonical_url: "https://mrnasdog.com/research/rain/inflation"
tags: ["crypto", "rain", "prediction-markets", "arbitrum"]
published: true
---

> Originally published at **[mrnasdog.com/research/rain/inflation](https://mrnasdog.com/research/rain/inflation)** by MrNasdog.

Rain Protocol mints no new RAIN — the one mint switch in the token contract has never been used — and yet the Pressure Framework reads RAIN at **+12.21%** over the trailing 90 days and **+10.02%** over the next 90. Almost all of it comes from one mechanism: a Sablier lockup that released **93,706M RAIN** in the window into the project's own wallets, which sit inside the circulating float. Sell pressure is **94,017M RAIN**, buy pressure is **7,447M RAIN**, and the lockup still holds **424,738M RAIN**, all of it scheduled out by **Sep 9 2027**.

## The verdict, in one paragraph

Against a circulating base of **709,230M RAIN**, the framework books **94,017M RAIN** of sell pressure and **7,447M RAIN** of buy pressure over the trailing 90 days — a net of **+12.21%** — and projects **+10.02%** for the next 90 days on the lockup's own on-chain schedule. The inflation monitor reads **+13.77%** for the same window, a gap of **1.56 percentage points**, over the 0.5pp tolerance, so the overview page ships with a monitor-gap warning. The gap decomposes completely: both sides book the same flow, but the monitor divides by the supply of 90 days ago. Over that older base the framework's own numerator reads **+13.90%**, so **1.70pp** is base convention and **-0.13pp** is the monitor's own supply estimate. The label for RAIN is a **token that mints nothing but is still working through a multi-billion-coin unlock**, and the burns so far offset less than a tenth of it.

## Sell pressure: where new RAIN comes from

It does not come from minting. Sell #1, protocol inflation, is **0**. RAIN was minted once, **1,150,000M** at launch, and the count of RAIN in existence fell by exactly the coins burned over the window, with no mint in between. The token does carry a mint switch that Rain Protocol's public white paper does not describe: the owner, a project multisig, can create 10% of whatever was burned since its last use and send it to the treasury. It has never been used. About **759.1M RAIN** could be minted in one call today, so the row is watched, not closed.

The whole supply story is Sell #2, vesting unlocks, at **94,017M RAIN**. A Sablier lockup holds six Rain Protocol streams, each paying the project wallet that funded it. Over the window it released **93,706M RAIN** in thirteen withdrawals, and its balance fell from **518,444M** to **424,738M RAIN**. Presale buyers claimed another **311.0M RAIN** from the 1% presale bucket. Both flows leave supply that sat outside the circulating float and put it inside, which is exactly what the framework measures. The receiving project wallets have sent almost none of it on yet, but a coin in a multisig can move in one transaction, and a coin in a lockup cannot. Next 90 days the streams release **70,778M RAIN** on their on-chain schedule, and presale claims add about **309.6M**.

Sell #3, Foundation and unscheduled unlocks, is **0**. Project wallets did pay **445.2M RAIN** to outside addresses this window, including **26.1M RAIN** sent straight to an exchange, but those coins were already inside the float after their release, so counting them again would book the same coin twice. Sell #4, long-term locked or bankruptcy, is **0**: RAIN has no bankruptcy estate and no trustee.

## Buy pressure: where new RAIN goes

Buy #1, programmatic buyback, is **27.6M RAIN**. Rain Protocol prediction markets route a share of trading fees into a swap for RAIN on the open market, and the bought RAIN is burned in the same transaction, so nothing is parked. Most of it fired in July. After Rain SDK v2 replaced the old trading version on **Aug 27 2026**, the buyback-and-burn slowed to **0.056M RAIN** in 19 days, so the forward column uses that pace: about **0.26M RAIN** over the next 90 days.

Buy #2, protocol fee burn, is **0** because the fee burn is the Buy #1 buyback, counted once. Both burn surfaces were read: the RAIN supply fell by exactly the coins sent to the zero address, and the dead address took in only 414 RAIN of dust.

Buy #3, Foundation buy, is **7,419M RAIN**. After the first Rain DAO vote on the Credit Refund program, the Rain Foundation paid **$23M** in cash at $0.0031 per RAIN for Credit Refund allocations and burned **7,419M RAIN** on **Aug 25 2026**, from a project wallet inside the float. Buy #1 and Buy #3 together equal the fall in RAIN supply to the last unit. It was a one-off settlement, so the next 90 days carry 0. Buy #4, new long-term lock, is **0**: the lockup took in no new RAIN and there is no staking lock.

## Foundation and overhang

Two kinds of overhang sit behind RAIN. The first is still locked: the Sablier lockup holds **424,738M RAIN**, of which **32,981M** has already vested but not been withdrawn, and a new 230,000M stream starts on **Mar 9 2027**. That is scheduled supply and it lands in Sell #2 as it leaves. The second is already released but held by the team: four project multisigs hold **421,304M RAIN**, a strategic-sale wallet **100,470M RAIN**, a liquidity wallet **5,350M RAIN**, and the presale wallet **8,440.7M RAIN**. All but the liquidity wallet share a signer with the token's owner, and the liquidity wallet shares three signers with the main team wallets. A listed company also holds an option to buy **271,372M RAIN** from the Rain Foundation at **$0.0033** until **Dec 31 2027**. All balances are refreshed from chain at every rebuild; if a team wallet's balance falls in a way the schedule does not explain, that outflow enters Sell #3 at the next refresh.

## How RAIN compares to other vesting-heavy governance tokens

RAIN belongs with young governance tokens working through a large, linear unlock, not with capped chains. A halving-model chain like Bitcoin mints on every block at a slowing rate and reads a fraction of a percent a quarter. RAIN mints nothing, yet reads **+12.21%**, because a hard launch supply does not stop locked coins from becoming tradable. What makes RAIN unusual is that its lockup pays only project multisigs, so the release and any later sale are two separate events controlled by one group of signers.

Against exchange tokens with revenue-funded buybacks, Rain Protocol has the same mechanism on paper: fees buy RAIN and burn it. It removed **27.6M RAIN** in 90 days and now runs near **0.26M RAIN** a quarter, against a lockup releasing about **70,778M**. The only burn that mattered this window was the one-off **7,419M RAIN** DAO settlement. For burns to offset the unlock, Rain Protocol would need fee volume far beyond anything it has run so far.

And unlike a fixed-code cap, RAIN's ceiling of 1,150,000M is a policy: the owner mint switch exists, even if it has never been pressed.

## What to watch in the next 90 days

First, the Sablier streams, which release about **70,778M RAIN** by **Dec 14 2026** and keep the next reading near **+10.02%**. Second, the four project multisigs holding **421,304M RAIN**: coins sent from them to exchanges are the difference between tradable and actually sold. Third, the owner mint switch, with **759.1M RAIN** available in a single call. Fourth, the buyback-and-burn under Rain SDK v2, which would need to return far above July's pace to matter. Fifth, the option on **271,372M RAIN** from the Foundation and any new Rain DAO vote touching supply.

## Summary

The MrNasdog Pressure Framework reads RAIN at **+12.21%** over the trailing 90 days and **+10.02%** projected forward: supply growing, projected to keep growing. The mechanism is unlock, not issuance — Rain Protocol minted nothing, while a Sablier lockup released **93,706M RAIN** into the float and burns removed **7,447M RAIN**, almost all in one DAO settlement. The key risk is that the lockup still holds **424,738M RAIN** and runs until **Sep 9 2027**, while the fee burn has nearly stopped. The ceiling is the 1,150,000M launch supply, held by policy rather than code.

*MrNasdog Pressure Framework analysis of RAIN, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 15 2026.*

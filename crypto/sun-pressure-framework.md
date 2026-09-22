---
title:         "SUN Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "SUN supply is roughly steady: nothing can mint it, and a SUN.io buyback burned 9.03M SUN in 90 days for a net of -0.05%. Full Pressure Framework analysis."
canonical_url: "https://mrnasdog.com/research/sun/inflation"
tags:                    ["crypto", "sun", "sunswap", "defi"]
published:     true
---

Originally published at [SUN Inflation Analysis · September 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/sun/inflation).

# SUN Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

SUN supply is roughly steady and edging down. The SUN token on TRON has no function that can mint a new coin, so sell pressure is **0**, while the SUN.io buyback-and-burn programme destroyed **9.03M SUN** in the last 90 days. That gives a net of **−0.05%** over the trailing 90 days and **−0.02%** projected for the next 90, against a monitor reading of **−0.12%**. The hard ceiling is the **19,900.7M SUN** minted once in 2021, which no one can raise.

## The verdict, in one paragraph

Against a circulating base of **19,222.2M SUN**, the Pressure Framework books **0** of sell pressure and **9.03M SUN** of buy pressure over the trailing 90 days, a net of **−0.05%**, and projects **−0.02%** for the next 90 days from one dated buyback round. The inflation monitor reads **−0.12%** for the same window, a gap of **0.08 percentage points**. That is inside the framework's 0.5-point tolerance, so the overview ships with no warning. Both readings agree on the direction: SUN supply is not growing, and the only thing moving it is the buyback burn. The label for SUN is **a fixed-supply DeFi token with a slow, revenue-funded burn**.

## Sell pressure: where new SUN comes from

Nowhere. Protocol inflation is **0**, and here that zero is permanent rather than a current setting. The SUN contract on TRON exposes eleven functions: the standard token transfers, approvals and read-outs, and nothing else. There is no mint function, no burn function, no owner and no upgrade path, and the deployed code contains no instruction that could write the total supply after the contract was created. The **19,900.7M SUN** in existence were made once, when SUN was redenominated at 1:1000 in May 2021, and the total supply has read that same figure ever since.

Vesting unlocks are **0** as well. SUN.io describes a distribution with no team allocation, no private sale and no pre-mine, plus a large Sun DAO governance allocation that vested in a straight line over four years. What decides this row is where the coins sit. The circulating figure used for SUN counts every wallet except the TRON burn address, and it matches total supply minus the burn address to within 3 SUN. So a coin leaving any reserve wallet is moving from one counted pocket to another. It adds nothing to the float, however large the transfer.

Foundation and unscheduled unlocks are **0** for the same reason, and long-term locked or bankruptcy releases are **0** because SUN has no bankruptcy estate, trustee or court-ordered distribution.

## Buy pressure: where new SUN goes

Into the TRON burn address, in rounds. Programmatic buyback is **9.03M SUN**. SUN.io takes revenue from three products, the SunSwap V2 exchange, the SunPump meme-coin launchpad and the SunX perpetuals exchange, and uses it to buy SUN on the open market. The bought SUN collects in an executor contract and is then sent to the burn address, where no one holds the key. Round 51 closed on **Jul 25 2026** with a single transfer of **9,025,027 SUN**, and it was the only transfer into the burn address in the whole 90-day window. SUN.io's published running total moved from **669.5M** to **678.5M SUN** burned on the same day, which matches the on-chain transfer to four decimals.

Protocol fee burn is **0**, and this is on purpose. The SunSwap V2 fee share is not burned on its own. It is turned into SUN and joins the same buyback round, so counting it here as well would book one burn twice. A burn on TRON can show up in two places: a rising burn-address balance, or a falling total supply. Both were checked. The burn address rose by exactly the round 51 transfer. The total supply cannot fall at all, because the SUN contract has no function that lowers it. That leaves one flow, booked once.

Foundation buy is **0**: no foundation or treasury bought SUN outside the buyback rounds. New long-term lock is **0**. The SUN.io vote-lock vault holds **486.7M SUN**, but locked SUN still counts as circulating, so locking removes nothing from this reading.

## Foundation and overhang

The overhang on SUN is large in size but already inside the float. The biggest item is concentration: eight large unlabelled wallets hold **14,921.2M SUN** between them, about three quarters of all circulating SUN. Seven of the eight did not move a single SUN in this window; the eighth sent out **6.1M SUN**. None carries a public label. They are listed here because a sale from them would move the market without moving this page's number, since the float already counts them.

The second item is the SUN.io vote-lock vault at **486.7M SUN**. Locks expire one by one on their own dates. The third is the buyback executor itself, holding **2.93M SUN** already bought and waiting for round 52. Its owner can withdraw from it before a burn, so that balance is watched rather than counted as burned in advance. All three are read from the chain at every rebuild. If any of these balances falls between refreshes by more than a burn accounts for, the outflow enters the foundation row at the next refresh.

## How SUN compares to other fixed-supply buyback tokens

SUN sits in a small class: tokens whose supply was fixed at launch and can only shrink. That is a stronger promise than a halving schedule. A halving chain like Bitcoin still mints on every block, just at a falling rate, so its reading stays positive. SUN mints nothing, so its sell side is a flat, permanent zero. It is also stronger than most DeFi governance tokens, which usually keep an emission stream for liquidity mining or a team vest that unlocks over years.

The better comparison is with exchange tokens that burn from revenue, and there the difference is size. Those programmes can take 1% or more of supply off the market every quarter. SUN.io's buyback took **0.05%** in this window. The mechanism is the same shape, revenue in and coins burned, but at current revenue it moves SUN supply only slowly. Over more than four years it has burned about **678.5M SUN**, around 3.4% of everything ever made.

The last difference is concentration. Many fixed-supply tokens spread their float widely. On SUN, a handful of wallets hold most of it, and they sit inside the float. That does not change the inflation reading, but it is the main supply risk a holder carries.

## What to watch in the next 90 days

First, buyback round 52, expected around **Oct 25 2026** if the three-month rhythm of the last two rounds holds. The executor already holds **2.93M SUN** for it, and more purchases before that date would make the burn larger. Second, the rhythm itself: the round before last took five months, and a similar delay would push round 52 past **Dec 22 2026**, which would leave the next 90 days at zero. Third, the eight large wallets holding **14,921.2M SUN**, where any large transfer to an exchange would matter to price even though it does not change this reading. Fourth, any SUN DAO vote that changes how revenue is split between buybacks and other uses, since that sets the size of every future burn.

## Summary

The MrNasdog Pressure Framework reads SUN at **−0.05%** over the trailing 90 days and **−0.02%** projected forward: mixed flows, supply roughly steady. SUN cannot be minted, and its only supply mechanism is a SUN.io buyback that burned **9.03M SUN** on Jul 25 2026 out of a fixed **19,900.7M SUN**. The key risk is not new supply but concentration, with about three quarters of the float in eight unlabelled wallets. The ceiling is the strongest part: no function in the SUN contract can ever create another coin.

MrNasdog Pressure Framework analysis of SUN, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 23 2026.

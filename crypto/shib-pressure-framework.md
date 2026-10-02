---
title: "SHIB Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description: "SHIB supply is frozen: no mint, no unlocks, and 4.26B SHIB burned in 90 days, about −0.0007% net. Next 90 days: about −0.0002% as one app burn drops out."
canonical_url: "https://mrnasdog.com/research/shib/inflation"
tags: ["crypto", "shib", "shiba-inu", "memecoin"]
published: true
---

> Originally published at **[mrnasdog.com/research/shib/inflation](https://mrnasdog.com/research/shib/inflation)** by MrNasdog.

# SHIB Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

Shiba Inu (SHIB) is a fixed-supply meme token whose supply only goes one way: down, and very slowly. From Jul 4 to Oct 2 2026 no new SHIB was created and nothing unlocked, while apps and holders burned **4.26B SHIB**. Against **589.24T SHIB** in circulation that is a net change of about **−0.0007%**, and about **−0.0002%** is expected for the next 90 days. Our supply monitor reads **−0.03%** for the same stretch, close enough that no warning is needed.

## The verdict, in one paragraph

Over the last 90 days the Shiba Inu ledger shows **0 SHIB** of sell pressure and **4,255.80M SHIB** of buy pressure, all of it burns. Divided by 589.24T circulating SHIB, the net is **−0.0007%**, which rounds to **−0.00%** on the coin page. The next 90 days project **1,143.79M SHIB** of burns and the same zero issuance, for **−0.0002%**. Our supply monitor, which tracks the market-wide circulating figure, reads **−0.03%** for the window. The gap is **0.03 percentage points**, well inside the 0.5-point line, so no warning chip is shown. In one line: SHIB is a **frozen-supply token with a slow, voluntary burn**.

## Sell pressure: where new SHIB comes from

Protocol inflation is **0 SHIB**, and it can never be anything else. The SHIB token contract on Ethereum has only the standard send, approve and balance functions plus a burn. It has no mint function, no owner, no upgrade path and no way to call out to other code, and the total supply number in its storage is only ever written by the burn. So the SHIB supply can fall but cannot rise. In this window the contract's own burn removed 423,255 SHIB.

Vesting unlocks are **0 SHIB**. Shiba Inu launched in Aug 2020 with all 1 quadrillion SHIB split between a trading pool and Vitalik Buterin, who later sent most of his half to a dead wallet. There was no team allocation, no investor round and no sale tranche, so there is no vesting calendar at all; unlock trackers list SHIB as fully unlocked. About **99.96%** of the SHIB that still exists already circulates.

Foundation and unscheduled unlocks are **0 SHIB**. The Shiba Inu team does not publish a treasury address, and the known early wallets did not move. Long-term locked or bankruptcy supply is also **0 SHIB**: a US-government wallet from the FTX and Alameda case moved its **54.90B SHIB** to a new wallet on Jul 15 2026 and still holds them. Those coins were already part of the circulating SHIB supply, so even a sale would shift coins between owners rather than add new SHIB.

## Buy pressure: where new SHIB goes

There is no programmatic buyback (**0 SHIB**): no Shiba Inu contract or treasury buys SHIB on the market. The protocol fee burn row is also **0 SHIB** for Ethereum, even though Shibarium, the Shiba Inu layer-2 network, burned **131.37M SHIB** from its fees this window. Those burns hit the layer-2 copy of SHIB, and the bridge balance on Ethereum stayed flat at 90.95M SHIB, so no Ethereum SHIB left the market because of them. There was no foundation buy (**0 SHIB**), and no new long-term lock (**0 SHIB**): the main SHIB staking vault actually shrank from 3.54T to 3.47T SHIB, and staked SHIB counts as circulating either way.

All of the real SHIB buy pressure is the fifth row, burns by apps and holders: **4,255.80M SHIB** in 90 days. Most of it went to the classic dead wallet that also holds Vitalik Buterin's 2021 burn, smaller amounts went to a second dead wallet, some SHIB was sent by mistake to the token contract itself, where it can never be moved again, and the rest was burned through the contract. One app's fee splitter, which sends a fixed share of its fees to the dead wallet, accounts for **3,112.02M SHIB**, nearly all of it on Jul 25–28 2026, with only small amounts after that and the last on Sep 3 2026. Because that app follows no schedule, the next-90-day figure leaves it out and keeps only the steady background burn of **1,143.79M SHIB**, roughly 380M SHIB a month.

## Foundation and overhang

Shiba Inu has an unusually thin overhang, because there was never a team pile to begin with. The coins counted outside the float are almost all stuck for good: **255.42B SHIB** sitting in the SHIB token contract itself, plus 809.55M SHIB in the BONE token contract and 191.78M SHIB in the LEASH token contract, all sent there by mistake. About **0.78B SHIB** of the outside-the-float figure could not be traced to a holder; it is the only slice that might one day return. The original deployer wallet holds 50.50M SHIB and an early wallet holds 2.25M SHIB, and neither moved. The fund paying back victims of the Sep 2025 Shibarium bridge hack has no public address.

We re-read these wallets on chain at every rebuild and watch the team's posts for the repayment fund. If any of these balances falls between refreshes and the coins reach the market, that outflow enters the SHIB ledger as a foundation or unscheduled unlock at the next refresh.

## How SHIB compares to other meme coins

Meme coins split into two supply designs. The first is the mined meme coin, like Dogecoin, which pays miners a fixed amount of new coins every block forever, so its supply grows by a steady few percent a year whatever the community does. The second is the fixed-supply token, like SHIB, where every coin was created on day one and the contract has no way to add more. SHIB sits firmly in the second group: its ledger has zero issuance, and the only thing that changes the count is coins being destroyed.

Among fixed-supply meme tokens, SHIB is unusual for how big its past burn was and how small its present one is. More than 41% of the original 1 quadrillion SHIB sits in a dead wallet from the 2021 burn, which is why circulating supply is 589.24T rather than 1 quadrillion. Today's burns are a different scale: 4.26B SHIB in 90 days is less than one-thousandth of one percent of supply. Unlike exchange tokens that burn a set share of profits each quarter, SHIB has no programme behind its burn, so the pace depends on which apps and holders choose to burn, and it swings from week to week.

For supply, that makes SHIB close to flat. A meme coin with mining rewards adds new coins that must be bought every day; SHIB adds none. But a flat supply also means the price depends almost entirely on demand, because neither a buyback nor a meaningful burn is taking SHIB off the market.

## What to watch in the next 90 days

First, the app fee splitter that burned 3,112.02M SHIB in late July: if it fires again on that scale, the SHIB burn for the quarter could triple, though even then the net would stay far below 0.01%.

Second, the US-government wallet holding 54.90B SHIB from the FTX and Alameda case, moved on Jul 15 2026: a sale would add selling on exchanges, but not new supply.

Third, Shibarium: its validator staking has been halted since Apr 2026 and the network finished a fix for block reorgs in late Sep 2026. A busier Shibarium burns more SHIB on the layer-2 copy, which does not reach Ethereum unless the bridge balance moves.

Fourth, the 0.78B SHIB outside the float that we could not trace to a holder, and any address published for the bridge-hack repayment fund. Either moving to the market would show up as an unscheduled unlock.

## Summary

Shiba Inu (SHIB) has a frozen supply: the token contract cannot mint, nothing vests, and 99.96% of existing SHIB already circulates. Over Jul 4 to Oct 2 2026, burns by apps and holders removed **4.26B SHIB**, a net change of about **−0.0007%**, with about **−0.0002%** expected next as one large app burn drops out. The key risk is not new supply but existing holders, such as the 54.90B SHIB government wallet, selling coins already in the float. The ceiling is fixed: SHIB supply can never rise above today's level.

*MrNasdog Pressure Framework analysis of SHIB, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 2 2026.*

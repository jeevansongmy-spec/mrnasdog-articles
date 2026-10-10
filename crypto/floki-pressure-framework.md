---
title:         "FLOKI Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description: "FLOKI supply shrinks slowly: no new FLOKI can be made, and staking-penalty burns plus a locker buyback removed 4.88B FLOKI in 90 days, −0.05% net, same next."
canonical_url: "https://mrnasdog.com/research/floki/inflation"
tags: ["crypto", "floki", "tokenomics", "ethereum"]
published: true
---
Originally published at [FLOKI Inflation Analysis · October 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/floki/inflation).

# FLOKI Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

<!-- main-page -->
The Floki coin page has the score, the price drivers and every question answered — [mrnasdog.com/research/floki](https://mrnasdog.com/research/floki). Below: supply, line by line.

The MrNasdog Pressure Framework reads FLOKI as very slightly deflationary: supply fell **0.05%** over the last 90 days and is on course to fall about **0.05%** again over the next 90. No new FLOKI can be made, and **4.88B FLOKI** was burned — **4.84B** from early-unstake staking penalties and **38.05M** from locker-fee buy-and-burn. The monitor reads **−0.07%**, so the two readings agree.

## The verdict, in one paragraph

Over the 90 days to Oct 10 2026 the FLOKI ledger booked **0 FLOKI** of sell pressure and **4.88B FLOKI** of buy pressure on a circulating supply of **9.64T FLOKI**, a net change of **−0.05%**, with the same **−0.05%** projected for the next 90 days. The inflation monitor reads **−0.07%** over the same stretch, a gap of **0.02 percentage points**, well inside the 0.5-point line, so no warning chip is shown. The one-line label: FLOKI is a fixed-supply meme token with a slow staking-penalty burn.

## Sell pressure: where new FLOKI comes from

Protocol inflation is **0 FLOKI**, and it cannot change. FLOKI lives on two chains, Ethereum and BNB Chain, and each chain's FLOKI contract created **10T FLOKI** once, at launch. We read the contract code on both chains: it has no function that creates coins, its only balance changes are ordinary transfers, and its owner key was handed to a dead address, so nobody can swap in new rules. The FLOKI not used on each chain sits in a dead wallet, which is why only **9.64T** of the 20T ever created circulates.

Vesting unlocks are **0 FLOKI**. FLOKI never had a team or investor vesting calendar, and every FLOKI outside the dead wallets already counts as circulating, so there is no locked tranche left to open.

Foundation and unscheduled unlocks are **0 FLOKI**, but this row needs a closer look than the zero suggests. The Floki treasury on Ethereum sent **38.19B FLOKI** to a market maker in three batches, on Jul 27, Aug 27 and Sep 28 2026. A market maker uses coins to quote buy and sell orders, so some of this FLOKI may reach buyers over time. Those coins were already counted as circulating while they sat in the treasury, so moving them adds nothing new to the FLOKI supply count.

Long-term locked or bankruptcy supply is **0 FLOKI**. No court estate or trustee holds FLOKI. The staking pools hold about **1.69T FLOKI**, but those are holders' own coins that already count as circulating.

## Buy pressure: where new FLOKI goes

The largest buy-side mechanism is the staking penalty burn: **4.84B FLOKI** in 90 days. FLOKI staking locks coins for 3, 12, 24 or 48 months, and a holder who leaves early pays a penalty of 5% to 20% of the stake, which the staking pool sends straight to the dead wallet. That burned **2.61B FLOKI** on Ethereum and **2.23B FLOKI** on BNB Chain. All burns together came to 3.79B FLOKI in the 90 days before this window, so the penalty burn picked up as more holders left staking.

The programmatic buyback added **38.05M FLOKI**. A quarter of the fees from Floki's token locker is used to buy FLOKI on the open market and send it to the dead wallet: **23.48M FLOKI** on Ethereum and **14.58M FLOKI** on BNB Chain in this window. Next to the penalty burn it is small.

The protocol fee burn is **0 FLOKI**. FLOKI charges a 0.3% tax on DEX buys and sells, but that tax pays the treasury; it is not destroyed. A few holders sent about 15.4K FLOKI to the dead wallet by hand, too little to count.

The Foundation buy is **0 FLOKI**. On Aug 17 2026 the treasury pulled 250B FLOKI out of an exchange on BNB Chain and sent 200B back the next day, but those coins were already circulating, so it is not a purchase. The new long-term lock row is also **0 FLOKI**: staking locks FLOKI for months, but staked coins still count as circulating, and the pools actually shrank by 55.3B FLOKI this window.

Every burned FLOKI is visible on-chain: we read the dead wallet on both chains at both ends of the window and matched every transfer into it, so the 4.88B FLOKI figure closes to the coin.

## Foundation and overhang

Team-controlled wallets hold about **228.1B FLOKI**, roughly 2.4% of circulating supply. The treasury Safes hold **22.41B FLOKI** on Ethereum and **74.69B FLOKI** on BNB Chain; a second team Safe on Ethereum holds **114.65B FLOKI** after sending 50B to an exchange on Aug 14 2026; a wallet set aside by a DAO vote for a FLOKI exchange-traded product holds **16.31B FLOKI** across both chains and did not move; and a FlokiFi treasury holds about 78M FLOKI. The tax handlers pass small amounts to the treasury every day.

All of these balances already count as circulating, so they cannot add to the FLOKI supply count — but they can add to selling. We read each wallet on-chain at every rebuild. If one of these balances falls between refreshes, the outflow is checked at the next refresh and booked in Sell #3 only if it brings coins from outside the float into the market; a treasury batch to a market maker stays a watch item.

## How FLOKI compares to other meme coins

Among meme coins, FLOKI sits in the fixed-supply group. Dogecoin is the opposite design: a proof-of-work chain that pays miners a fixed number of new DOGE in every block with no cap, so its supply grows every day. FLOKI, like Shiba Inu and Pepe, is a token with a set supply created at launch and no way to mint more, so its supply can only stay flat or shrink.

What separates FLOKI inside that group is where its burn comes from. Many fixed-supply meme tokens burn only when holders or the team choose to send coins to a dead wallet, which makes the burn lumpy and hard to forecast. FLOKI has two built-in burns: the staking penalty, paid by holders who leave staking early, and a buy-and-burn funded by fees from its token locker. That gives FLOKI a steadier burn than most meme coins, though at about 0.05% of supply per 90 days it is still small.

FLOKI also differs in its treasury. It charges a 0.3% tax on DEX trades that funds a DAO treasury, and that treasury holds a large FLOKI balance it can sell or hand to market makers. Meme coins with no tax and no treasury carry less of that kind of team overhang, while FLOKI's treasury pays for products, marketing and liquidity.

## What to watch in the next 90 days

Around Oct 27, Nov 27 and Dec 27 2026: the treasury sent FLOKI to a market maker near the end of each of the last three months (14.42B, 9.77B and 14.00B FLOKI). If that pattern continues, about 38B more FLOKI could reach market-making desks by the end of 2026.

The staking pools: they shrank from about 1.75T to 1.69T FLOKI in 90 days. A faster exit from staking means a bigger penalty burn; a calm period means a smaller one.

The locker buyback: the keeper runs these buys every few weeks; a busier token locker would raise the 38.05M FLOKI figure.

Governance: the last FLOKI DAO vote closed in March 2026. Any new vote on the tax, the treasury or the exchange-traded product wallet would show up here before it moves supply.

## Summary

The MrNasdog Pressure Framework reads FLOKI at **−0.05%** over the last 90 days and **−0.05%** over the next 90: no new FLOKI can be made, and **4.88B FLOKI** was burned, almost all of it from early-unstake staking penalties. FLOKI's supply on Ethereum and BNB Chain is fixed in code, so it can only shrink, and it shrinks slowly. The key risk is not new supply but the **228.1B FLOKI** held by the team, including the monthly batches the treasury sends to a market maker. The ceiling is the 9.64T FLOKI already circulating; the burn has a long way to go before it changes that number much.

---

*MrNasdog Pressure Framework analysis of FLOKI, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 10 2026.*

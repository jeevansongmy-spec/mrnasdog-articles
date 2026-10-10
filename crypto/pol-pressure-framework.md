---
title:         "POL Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description:   "POL supply is roughly steady: a 100M POL fee burn beat the 52.24M POL mint, so POL fell 0.45% in 90 days. Only a promised 25M burn is counted next: +0.26%."
canonical_url: "https://mrnasdog.com/research/pol/inflation"
tags:          ["crypto", "pol", "polygon", "layer2"]
published:     true
---
> Originally published at **[mrnasdog.com/research/pol/inflation](https://mrnasdog.com/research/pol/inflation)** by MrNasdog.

<!-- main-page -->
The Polygon coin page has the score, the price drivers and every question answered — [mrnasdog.com/research/pol](https://mrnasdog.com/research/pol). Below: supply, line by line.

POL supply is roughly steady, and over the last 90 days it actually shrank. Polygon mints new POL every day at a fixed **2% a year**, which made **52.24M POL** in the window, but on Sep 23 2026 the network burned **100.0M POL** of saved base fees in one go. Net, supply fell by **0.45%**; the monitor reads **−0.40%**. For the next 90 days the mint keeps running while only a promised **25M POL** burn is counted, so we project about **+0.26%**. POL has no supply cap.

## The verdict, in one paragraph

Over the 90 days from Jul 6 to Oct 4 2026, POL supply changed by **−0.45%** on our ledger: **52.24M POL** minted against **100.0M POL** burned, on a circulating supply of **10.63B POL**. The monitor, which reads circulating supply day by day, shows **−0.40%** for nearly the same window. The gap is **0.05 percentage points**, well inside our 0.5-point tolerance, so no warning chip is shown. Looking ahead, the Polygon mint adds about **52.50M POL** and we count only the **25M POL** burn the founder has promised, for a projected **+0.26%**. In one line: POL is a low-inflation Polygon token whose fee burns come in big, irregular batches.

## Sell pressure: where new POL comes from

Protocol inflation is the only source of new POL. The POL emission contract on Ethereum mints once a day at a compounded **2% a year**, and every mint splits evenly: half goes to the Polygon staking contract that pays validators and delegators, and half to the Polygon Community Treasury. In this window the chain made 90 mints, one a day, worth **52.24M POL**, about 580,000 POL a day. We counted every mint event and the total matches the rise in POL total supply to the last coin. Because the rate is fixed by time, not by blocks, the faster Polygon PoS block times of 2026 do not change it; the next 90 days print about **52.50M POL**.

Vesting unlocks are **zero**. POL replaced MATIC one for one, and every team, sale and foundation schedule from the MATIC years ended long ago, so there is no locked pile left to open.

Foundation and unscheduled unlocks are **zero**. Every POL that exists, except the coins sitting at the dead address, already counts as circulating, so the Community Treasury, the fee collectors and any Polygon Foundation wallet can move or sell coins without adding new supply to the market.

Long-term locked or bankruptcy supply is **zero**. No estate or trustee holds POL, and the coins still waiting to swap from MATIC belong to MATIC holders and are already counted.

## Buy pressure: where new POL goes

There is **no programmatic buyback**. No contract or treasury buys POL on the market, and a forum proposal to fund one from the treasury never reached a vote.

The protocol fee burn is the whole buy side. On Polygon PoS the base fee of each transaction is not destroyed on the spot; it is collected in a fee wallet on the chain. On Sep 23 2026 the first community-triggered burn sent **100.0M POL** through a bridge contract to a dead address on Ethereum, almost twice the new coins of the whole window. Anyone can now start a burn; nobody needs the Polygon Foundation to sign. After that burn, about **79.5M POL** was still waiting in the two Polygon fee wallets, and base fees add roughly 0.42M POL a day. On Sep 27 2026 Polygon co-founder Sandeep Nailwal said another **25M POL** will be burned soon, with no date. Our next-90-day ledger counts only that 25M, the smallest number the evidence names.

Foundation buying is **zero**: no announcement or on-chain flow shows the Polygon Foundation, Polygon Labs or the treasury buying POL. New long-term locks are also **zero**. About 3.45B POL is staked, and stakers earn a higher reward from Oct 1 to Dec 1 2026, but staked POL still counts as circulating, so staking removes nothing from the float.

## Foundation and overhang

The largest tracked pile is the Polygon Community Treasury, which held **97.52M POL** on Oct 4 2026. It grew by 26.12M POL in the window, exactly its half of the mint, and paid nothing out. The Polygon PoS base-fee collector holds **21.62M POL** and its routing wallet holds **57.84M POL**; both are waiting for future burns. A pool of **27.33M POL** of saved priority fees is being paid to stakers between Oct 1 and Dec 1 2026 under a governance proposal known as PIP-92. Polygon Foundation and Polygon Labs wallets are not published. We read the on-chain balances at every rebuild. If any of these balances falls between refreshes and the coins reach the market, that outflow enters the foundation row of the sell ledger at the next refresh; a fall in the fee wallets that lands at the dead address enters the burn row instead.

## How POL compares to other uncapped proof-of-stake chains

POL sits in the same family as Ethereum and other uncapped proof-of-stake chains: new coins pay for security, and a fee burn pulls coins back out. The difference is the shape of the two flows. Ethereum issues new ETH every epoch in proportion to the stake and burns its base fee in every block, so its net supply moves smoothly. POL mints on a fixed 2% clock that ignores the stake, and its base fees pile up for months before a single large burn, so the ledger swings from deeply negative in a burn quarter to mildly positive in a quiet one.

Against exchange tokens with scheduled quarterly burns, such as BNB, POL has a burn that is quarterly in intent but not yet in practice: one burn has happened, and the next has no date. Against capped chains such as Avalanche, which also burn every fee, POL has no ceiling at all; the 2% mint runs until governance changes it, and a forum push to end it has not reached a vote.

Against Layer-2 tokens such as Arbitrum or Optimism, whose supply grows mostly through scheduled team and investor unlocks, POL carries almost no unlock risk. Its supply story is the mint versus the burn, and both are visible on chain.

## What to watch in the next 90 days

The next POL fee burn is the main event. The founder has promised **25M POL** soon, and a quarterly rhythm would point to a burn around late December 2026; a larger burn of the full **79.5M POL** waiting would turn the next 90 days negative.

The PIP-92 staker payout runs from Oct 1 to Dec 1 2026. It pays out existing fees, not new coins, so it moves no supply, but the reward rate falls back after Dec 1 2026.

PIP-93, a planned upgrade to share priority fees with stakers automatically, and any vote on the forum idea to cut the 2% mint would change the sell side. Neither had a vote date on Oct 4 2026.

Base-fee income itself has been slowing through the window, from about 0.6M POL a day in July to about 0.42M POL a day in late September, which sets the size of every future burn.

## Summary

POL supply is roughly steady: Polygon mints **52.24M POL** every 90 days at a fixed 2% a year, and a **100.0M POL** base-fee burn on Sep 23 2026 more than offset it, for a **−0.45%** change against a monitor reading of **−0.40%**. The next 90 days project about **+0.26%**, counting only the promised 25M POL burn. The key risk is timing: burns come in batches with no fixed date, while the mint never stops. There is no supply cap, so the long-run number depends on fee income keeping pace with the 2% mint.

---

*MrNasdog Pressure Framework analysis of POL, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 4 2026.*

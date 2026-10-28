---
title:         "ETH Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description:   "ETH burn rate today, live from the chain on our page, plus the 90-day view: 264K ETH of new issuance vs a 4.67K ETH fee burn, +0.21% net. No unlocks, no cap."
canonical_url: "https://mrnasdog.com/research/eth/inflation"
tags:          ["crypto", "eth", "ethereum", "staking"]
published:     true
---
*Originally published at [https://mrnasdog.com/research/eth/inflation](https://mrnasdog.com/research/eth/inflation)*

<!-- main-page -->
➜ Start with the Ethereum coin page for the short answer (should you buy ETH?) and its price drivers: [mrnasdog.com/research/eth](https://mrnasdog.com/research/eth)

# ETH Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

Ethereum (ETH) supply is growing slowly: **+0.21%** over the 90 days from Jul 22 to Oct 20 2026, and about **+0.21%** again over the next 90 days. Validators were paid **264,339 ETH** of new issuance, while the EIP-1559 fee burn destroyed **4,670 ETH**, so the burn cancelled less than 2% of new supply. ETH has no supply cap, no vesting and no unlocks, so validator pay and the fee burn are the only two forces that move it.

## ETH burn rate today

The page now opens with a live "ETH burn rate today" box, read from the chain once a day: ETH burned in the last 24 hours, new ETH paid to validators a day (about **2,937 ETH**, the 90-day pace), and the net change. On a normal day the burn cancels only a few percent of new issuance, so ETH supply keeps growing a little. For today's numbers, see [mrnasdog.com/research/eth/inflation](https://mrnasdog.com/research/eth/inflation).

## The verdict, in one paragraph

Over the last 90 days Ethereum's supply rose from **121.88M ETH** to **122.14M ETH**, a net **+0.21%**. Our projection for the next 90 days is the same **+0.21%**, because both forces run every block and no rule change is scheduled in that time. Other trackers show **+1.23%** for the same 90 days, a gap of **1.02 points**, so the coin page carries a warning note. That gap is not new ETH: the supply figure those trackers use sat near **120.68M ETH** until Sep 2 2026 and then jumped **1.33M ETH** in a single day on Sep 3 2026 to catch up with the chain. It should clear on its own around Dec 2 2026. The on-chain reading stands: ETH is mildly inflationary on a staking budget, with a fee burn too small to offset it.

## Sell pressure: where new ETH comes from

Protocol inflation is the only source of new ETH. Ethereum pays validators in freshly created ETH every epoch, and between Jul 22 and Oct 20 2026 that came to **264,339 ETH**, roughly **2,940 ETH a day**. The size of this pay depends on how much ETH is staked: the more stake, the more ETH is issued in total, though each validator earns a smaller share. On Oct 20 2026 about **43.76M ETH** was actively staked, a record, and another **1.31M ETH** was waiting in the entry queue. As that queue clears, Ethereum issuance creeps up a little further.

Vesting unlocks are zero. Ethereum's 2014 token sale and its genesis allocations have been fully liquid since the chain launched in July 2015, so there is no locked team or investor pile and no unlock cliff to wait for. Every ETH that exists already counts as circulating.

Foundation and unscheduled unlocks are zero as well. The Ethereum Foundation sells ETH from time to time to pay for research and grants, and its main wallet paid out **3,000 ETH** in this window, but those coins were already circulating. Moving them to an exchange or a grant recipient changes who holds them, not how many ETH exist. Long-term locked or bankruptcy supply is also zero: no court or bankruptcy estate holds a pile of ETH waiting to be released.

## Buy pressure: where new ETH goes

The protocol fee burn is the only force that removes ETH. Since EIP-1559, the base fee of every transaction is destroyed, and since 2024 the blob fee that rollups pay to post data is destroyed too. Across all **645,521 blocks** in the window, the burn removed **4,670 ETH**, about **52 ETH a day**. Blob fees made up only **6.7 ETH** of that, because rollups now have far more blob space than they use and the blob price stays near its floor. More than half of the 90-day burn came in the last 30 days, as main-chain activity picked up, but even that busier stretch burned only a small slice of what validators were paid.

There is no programmatic buyback: no contract or treasury buys ETH back on the network's behalf. There is no foundation buy either; the Foundation is a seller, not a buyer. Spot ETH funds and listed treasury companies do buy ETH, and the largest company holder now owns more than **6M ETH**, but they buy coins that already circulate, so the supply count does not change. New long-term locks are zero too: staked ETH still counts as circulating, so the record stake removes nothing from supply. The one proposal that would have burned part of validator pay, EIP-8363, was withdrawn from the next upgrade in early October 2026.

## Foundation and overhang

The only team-controlled holder that matters is the Ethereum Foundation. Its four known wallets held about **94,273 ETH** on Oct 20 2026: the main wallet with **5,774 ETH** after a 3,000 ETH payout in the window, a multi-signature safe with **68,188 ETH** that grew slightly from staking rewards, a DeFi wallet with **20,176 ETH** that did not move, and a small wallet with 134 ETH. The Foundation also stakes roughly **70,000 ETH** under its treasury staking plan. Together that is about 0.13% of all ETH.

Because Ethereum counts every coin as circulating, none of this is hidden supply. When the Foundation sells, the coins change hands inside the market that already exists. There is no reserve outside the circulating count, no DAO treasury and no buyback wallet to track. We check these wallets at each rebuild; if a balance that sits outside the circulating count ever appears and starts to fall, those coins would show up here as new supply.

## How ETH compares to other proof-of-stake Layer 1 chains

Among large proof-of-stake chains, Ethereum sits at the low end for issuance. Its pay to validators is set by how much ETH is staked, not by a fixed yearly percentage, which gives an issuance rate of roughly 0.9% a year today. Solana and Cardano follow a set yearly schedule instead: Solana's inflation steps down each year toward a long-run floor, and Cardano pays rewards out of a shrinking reserve. Those designs usually put more new coins into the market each year than Ethereum does, though Ethereum has no fixed end point either.

The fee burn is what most sets Ethereum apart. BNB Chain and Avalanche also burn fees, and in busy periods Ethereum's burn has been larger than its issuance, which made ETH supply shrink for long stretches in 2022 and 2023. Today the burn covers less than 2% of issuance, because most everyday transactions moved to cheaper rollups that pay the main chain very little. Bitcoin is the other point of comparison: it has a hard cap of 21M coins and halvings, while Ethereum has no cap and relies on staking economics and the burn to keep growth slow.

## What to watch in the next 90 days

Oct 26 2026: the Glamsterdam upgrade goes live on the Hoodi test network, with a 200M gas limit. Its changes reprice gas and change how blocks are built, but none of them alter validator pay.

The Glamsterdam mainnet date. Developers have not set one; once Hoodi runs cleanly they are expected to pick it on their regular calls. A bigger, cheaper chain could raise main-chain activity, and with it the fee burn.

The staking entry queue, now about **1.31M ETH**. Each ETH that joins the stake lifts total issuance a little, so a long queue means slightly faster supply growth into January 2027.

The issuance debate. After EIP-8363 was withdrawn in early October 2026, its authors said they would take the idea of cutting validator pay to a separate discussion starting in November 2026. Any change still needs a future hard fork.

Around Dec 2 2026, other trackers' 90-day reading should drop back toward ours, once their one-day supply jump of Sep 3 2026 leaves the window.

## Summary

Ethereum's supply grew **+0.21%** over the 90 days to Oct 20 2026 and is set to grow about the same over the next 90 days. Validators received **264,339 ETH** of new issuance, while the EIP-1559 fee burn destroyed **4,670 ETH**; ETH has no vesting, no unlocks, no buyback and no supply cap. The key risk is that issuance keeps rising with the record stake while the burn stays small; the upside case is a busier main chain after Glamsterdam, or a future change to validator pay. Until either happens, ETH supply keeps growing slowly, at well under 1% a year.

---

*MrNasDog Pressure Framework analysis of ETH, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 20 2026.*

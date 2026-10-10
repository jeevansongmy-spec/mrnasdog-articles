---
title:         "ETH Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description:   "ETH is mildly inflationary: 263K ETH of validator issuance against a 4.66K fee burn gives +0.21% net over 90 days, the same next. No vesting, no unlock, no cap."
canonical_url: "https://mrnasdog.com/research/eth/inflation"
tags:          ["crypto", "eth", "ethereum", "staking"]
published:     true
---
*Originally published at [https://mrnasdog.com/research/eth/inflation](https://mrnasdog.com/research/eth/inflation)*

<!-- main-page -->
➜ Start with the Ethereum coin page for the short answer (should you buy ETH?) and its price drivers: [mrnasdog.com/research/eth](https://mrnasdog.com/research/eth)

# ETH Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

ETH supply is growing slowly and steadily. Over the 90 days to Oct 10 2026, Ethereum paid validators **263,305 ETH** of new issuance and its EIP-1559 fee burn destroyed **4,661 ETH**, so net supply rose **+0.21%**, and the MrNasdog Pressure Framework projects about **+0.21%** for the next 90 days. Staking drives the number: the bigger the stake, the more new ETH the protocol creates, and nothing caps the total.

## The verdict, in one paragraph

Our ledger reads ETH at **+0.21%** net over the last 90 days and **+0.21%** over the next 90. The inflation monitor reads **+1.19%**, a gap of **0.98 percentage points**, which is above our 0.5-point limit, so the coin page carries a ⚠ monitor gap note. We walked the gap back to its source: the supply figure the monitor reads sat near 120.68M ETH from Jan 1 to Sep 2 2026 and then jumped by 1.33M ETH on Sep 3 2026 to catch up with the chain. That jump is a recount of ETH that already existed, not new coins, so our on-chain number stays. In one line: Ethereum is **mildly inflationary by design**, because validator pay is far larger than the fee burn.

## Sell pressure: where new ETH comes from

The only source of new ETH is protocol issuance, the reward Ethereum pays its validators every epoch. It came to **263,305 ETH** in the window, about **2,926 ETH a day**. We measured it by reading total supply at both ends of the 90 days and adding back what the burn destroyed. The protocol math agrees: with **43.75M ETH** staked across 851,105 validators, perfect participation would pay about 3,012 ETH a day, and real validators earn a little less because some miss duties and the stake was smaller at the start of the window.

Issuance follows the square root of the stake, so it keeps creeping up as more ETH is staked. Holders deposited **3.94M ETH** into staking during these 90 days, and another **1.37M ETH** is waiting in the entry queue. When that queue clears, issuance per day rises a little further.

Vesting unlocks are **zero**. Ethereum launched in 2015 with its crowdsale coins and its early team share free to move, so there is no locked allocation left to open, and circulating supply equals total supply. Foundation and unscheduled unlocks are also **zero** as new supply: the Ethereum Foundation does spend and sell ETH, but every coin it holds is already counted as circulating, so a sale only changes who holds it. Long-term locks and bankruptcy releases are **zero**: no court estate or trustee is paying out ETH.

## Buy pressure: where new ETH goes

The one force that removes ETH is the EIP-1559 fee burn. Every transaction pays a base fee, and rollups pay a blob fee to post their data; both are destroyed the moment they are paid. Added up block by block across all 645,485 blocks in the window, the burn came to **4,661 ETH**, about 52 ETH a day. Blob fees were only 6.6 ETH of that, because rollup data space is cheap since the blob capacity increases of the past year.

The burn is growing. It destroyed 995 ETH in the first 30 days of the window, 1,161 ETH in the next 30 and **2,504 ETH** in the last 30, as blocks filled up and the base fee rose. No fork or fee rule changed, so we keep the 90-day rate for the forecast. Even at the latest pace, though, the burn would cover well under a tenth of issuance.

There is no programmatic buyback (**zero**): nothing in the protocol or any treasury buys ETH back. There is no Foundation buy (**zero**). And there is no new long-term lock (**zero**): staking locks ETH behind an exit queue, but staked ETH still counts as circulating, so a bigger stake takes nothing out of the float. It only raises issuance.

## Foundation and overhang

The Ethereum Foundation is the one team holder we track. Its four known wallets held about **94,205 ETH** on Oct 10 2026: 68,120 ETH in its main Safe, 20,176 ETH in a multisig, 5,774 ETH in its oldest wallet and 134 ETH in another. It also stakes about 70,000 ETH in its own validators, with the rewards going back to its treasury. During the window its oldest wallet sent out 4,000 ETH, and in early October it sold ETH over the counter to a listed company that holds ETH.

Because ETH has no locked bucket, all of these coins are already inside the circulating count. A Foundation sale therefore adds selling in the market but no new supply to our ledger. We read these balances from the chain at every rebuild; if any of them moved into a bucket outside the float and then back out, that outflow would enter Sell #3 at the next refresh. Today no such bucket exists.

## How ETH compares to other smart-contract Layer 1s

Against Bitcoin, the difference is the cap. Bitcoin has a fixed 21M limit and a reward that halves every four years, so its issuance only falls. ETH has no cap: its issuance is set by how much is staked, not by a calendar, and the fee burn is the only brake. Right now ETH and Bitcoin add new supply at a similar pace, about 0.2% per 90 days, but Bitcoin's rate is locked to fall while Ethereum's will drift up with the stake unless the rules change.

Against other proof-of-stake Layer 1s such as Solana, Cardano or Avalanche, ETH sits at the low end. Solana runs a falling inflation schedule that still adds several percent a year; Cardano pays rewards from a shrinking reserve; Avalanche burns all fees but issues staking rewards on top. Ethereum's issuance is lower because its reward falls per validator as the stake grows, and it burns the base fee like Avalanche, but the burn is small because most everyday transactions now run on cheaper rollups built on top of Ethereum.

The one way ETH supply could shrink again is a much busier main chain. In 2022 and 2023 the burn often beat issuance; today it covers less than 2% of it.

## What to watch in the next 90 days

**Glamsterdam mainnet date.** The upgrade went live on the Sepolia test network on Oct 6 2026, aiming for much bigger blocks. A second test network and the mainnet date are not set yet; if it ships, more block space could change how much the base fee burns.

**The issuance debate.** A proposal to burn part of validator rewards as the stake grows (EIP-8363) was pulled from the next upgrade on Oct 1 2026. Its authors plan a separate issuance forum at Devcon in November 2026. Any rule that cuts validator pay would lower Sell #1 directly.

**The staking queue.** 1.37M ETH is waiting to join the stake. As it clears, issuance per day rises slightly.

**The burn trend.** The last 30 days burned 2,504 ETH, more than half the 90-day total. If that pace holds, the next rebuild will show a larger burn, but still far below issuance.

**The monitor gap.** The monitor's 90-day reading passes the Sep 3 2026 jump around Dec 2 2026; after that, the two numbers should agree again.

## Summary

The MrNasdog Pressure Framework reads Ethereum (ETH) at **+0.21% net** over the last 90 days and the next 90: **263,305 ETH** of validator issuance against a **4,661 ETH** EIP-1559 fee burn, with no vesting, no unlocks, no buyback and no supply cap. Issuance rises with the stake, which is still growing with 1.37M ETH in the queue, while the burn depends on how busy the main chain is. The key risk is that issuance keeps climbing while the burn stays small; the upside case is a busier chain after Glamsterdam that burns more. Until the burn catches up or Ethereum changes how validators are paid, ETH supply keeps growing slowly.

---

*MrNasdog Pressure Framework analysis of ETH, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 10 2026.*

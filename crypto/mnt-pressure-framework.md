---
title:         "MNT Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description:   "MNT supply held flat: -0.01% net over 90 days and 0.00% next. No mint, no unlock, no burn; 291,000 MNT went back to the 2.92B MNT Mantle Treasury."
canonical_url: "https://mrnasdog.com/research/mnt/inflation"
tags:          ["crypto", "mnt", "mantle", "layer-2"]
published:     true
---
*Originally published at [https://mrnasdog.com/research/mnt/inflation](https://mrnasdog.com/research/mnt/inflation)*

<!-- main-page -->
**Main page:** the full MNT coin page — signal, price drivers and the buy/sell questions → [mrnasdog.com/research/mnt](https://mrnasdog.com/research/mnt)

# MNT Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

MNT supply held flat this quarter. Over the 90 days to Oct 13 2026, Mantle minted **0 MNT**, released nothing from vesting or from its treasury, and burned nothing, while one team wallet sent **291,000 MNT** back into the Mantle Treasury, so the circulating count eased **−0.01%**; the next 90 days read **0.00%**. The real question for MNT is not new coins but the **2,917.3M MNT** treasury that sits outside the market and only moves when the Mantle DAO votes a budget.

## The verdict, in one paragraph

Our ledger reads MNT at **−0.01%** net over the last 90 days (291,000 MNT taken out of a circulating supply of **3,302.0M MNT**) and **0.00%** over the next 90. The inflation monitor reads **−0.02%**, a gap of **0.01 percentage points**, well inside our 0.5-point line, so no warning chip is needed: both readings agree that the Mantle float did not grow. MNT is a quiet-supply token with a large parked treasury: nothing is printed, nothing is burned, and the only thing that can change the float is a treasury decision.

## Sell pressure: where new MNT comes from

Protocol inflation was **0 MNT**. The MNT token on Ethereum reported a total supply of **6,219,316,795 MNT** at both ends of the window. The token contract does contain a mint function for its owner, capped at 2% of supply once a year, but the cap is set to zero today; when we asked the contract to mint a single MNT on the owner's behalf, it refused with its own "amount too large" error. So the mint is switched off, not removed, and a governance step would be needed to switch it on.

Vesting unlocks were **0 MNT**. The BitDAO-era and Mantle allocations finished unlocking in 2023, and unlock trackers show no Mantle unlock still to come.

Foundation and unscheduled unlocks were **0 MNT**. The Mantle Treasury keeps **2,917.3M MNT** in 11 published wallets on Ethereum and Mantle that are left out of the circulating count, and the main wallet, holding **2,900.0M MNT**, did not send or receive a single MNT in 90 days. Team budget wallets did pay out about 3.0M MNT on Ethereum and 2.3M MNT on Mantle to contributors and partners, but those wallets already count as circulating, so the payments moved coins between holders and added nothing new to the float.

Long-term locked or bankruptcy supply was **0 MNT**. No court estate or trustee holds MNT, and no long lock is due to open.

## Buy pressure: where new MNT goes

Programmatic buyback was **0 MNT**. Mantle does not buy MNT back. On Sep 18 2026 a holder group opened a forum discussion asking the DAO to study buybacks paid from ecosystem revenue, and earlier ideas for a phased treasury burn were archived without a vote, so nothing is running.

Protocol fee burn was **0 MNT**. Users pay gas on the Mantle network in MNT, but the fees collect in the network's fee wallets instead of being destroyed; total supply did not fall, and the burn address on Ethereum gained just 1 MNT.

Foundation buy and new long-term lock were both **0 MNT**. The treasury did not buy MNT on the market, and staked MNT still counts as circulating, so staking takes nothing off the market.

The one buy-side flow was coins returned to the treasury: **291,000 MNT** on Oct 1 2026, sent by a team wallet that counts as circulating into a treasury wallet on Mantle. It is a one-off with no schedule, so the next 90 days carry nothing for it.

## Foundation and overhang

The Mantle Treasury is the whole story of MNT supply. Its 11 published wallets hold **2,917.3M MNT**, about 47% of all MNT, and the treasury's full list of wallets holds about 2,972M MNT once budget and operating wallets are added. The rest of the treasury is BTC, ETH and stablecoins. Spending of treasury MNT is set by DAO budgets: the last one, covering July 2025 to June 2026, allowed up to 200M MNT a year plus a three-month extension that ran out at the end of September 2026, and a new budget has not been posted yet. We read the treasury wallets on-chain at every rebuild. If the treasury's balance falls between refreshes, the outflow enters Sell #3 at the next refresh. The owner's switched-off mint, worth up to about 124M MNT a year if it were ever turned on, is the second thing we watch.

## How MNT compares to other Ethereum layer-2 tokens

Most Ethereum layer-2 tokens, such as ARB and STRK, still release team and investor coins on monthly unlock schedules, so their float grows every month by design. MNT is different: its vesting is over, nothing is minted, and the coins that are not yet circulating sit in a DAO treasury with no release calendar. That makes MNT's supply quieter month to month, but less predictable over a year, because one budget vote can move more MNT than a quarter of unlocks would.

Like most layer-2 networks, Mantle keeps its gas fees instead of burning them, so MNT has nothing like Ethereum's fee burn working against new supply. Compared with exchange tokens that burn coins every quarter, MNT has no burn at all; the only way coins leave the market is when they are sent back to the treasury, as the 291,000 MNT were on Oct 1 2026.

The useful comparison is therefore custody, not emission: about half of all MNT sits with the Mantle Treasury, a larger share than most layer-2 projects keep under one roof. Mantle publishes those wallets, which makes the overhang easy to track, but it also means the market float of MNT depends on treasury decisions more than on any protocol rule.

## What to watch in the next 90 days

First, the fourth Mantle budget vote: the last budget and its extension ended in September 2026, and a new proposal would set how much treasury MNT can be spent through mid-2027. Second, the Sep 18 2026 buyback discussion on the Mantle forum: if it becomes a formal proposal and passes, it would add a buyback row for the first time. Third, the token's mint limit, which is zero today; any change to it would show up on-chain before a single MNT is minted. Fourth, the treasury's main wallet of 2,900.0M MNT, which has not moved this window; any outflow from it goes straight into the sell ledger. Fifth, the mStocks tokenized-stock product that Bybit plans to launch with Mantle in November 2026, which would bring more use to the Mantle network but does not change MNT supply.

## Summary

The MrNasdog Pressure Framework reads Mantle (MNT) at **−0.01% net** over the last 90 days and **0.00%** over the next 90: no MNT was minted, nothing vested, nothing was burned, and the only flow was **291,000 MNT** returned to the Mantle Treasury on Oct 1 2026. The structure is simple: a fully unlocked token, a mint switched off at zero, and a **2,917.3M MNT** treasury outside the circulating count. The key risk is a treasury budget or a switched-on mint that puts new MNT on the market; the upside case is a buyback or burn funded by revenue, which today is only a discussion. Until the DAO votes, MNT supply stays where it is.

---

*MrNasdog Pressure Framework analysis of MNT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 13 2026.*

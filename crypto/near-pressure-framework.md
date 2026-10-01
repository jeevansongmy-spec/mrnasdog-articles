---
title:         "NEAR Inflation Analysis · October 2026 · Supply growing · projected to keep growing"
description:   "NEAR supply is growing: 8.01M NEAR minted for stakers against a 66.1K gas burn gives +0.61% net over 90 days, the same next. No cap; buybacks are held."
canonical_url: "https://mrnasdog.com/research/near/inflation"
tags:          ["crypto", "near", "near-protocol", "layer1"]
published:     true
---

*Originally published at [mrnasdog.com/research/near/inflation](https://mrnasdog.com/research/near/inflation)*

NEAR is a coin whose supply grows on purpose. In the 90 days to Oct 1 2026 the NEAR Protocol minted **8,005,124 NEAR** for validators, stakers and the protocol treasury, and gas fees burned **66,109 NEAR**, so net supply rose about **+0.61%**. The next 90 days should look the same. NEAR has no supply cap: the protocol may print up to **2.5%** of supply a year, and the gas burn takes back less than 1% of that.

## The verdict, in one paragraph

Over the last 90 days NEAR supply grew by **+0.61%** net: **8.01M NEAR** of new coins against a **66.1K NEAR** gas-fee burn, measured on **1.31B NEAR** in circulation. Our supply monitor, which reads the market's circulating figure every day, shows **+0.85%** for the same 90 days. The gap is **0.25 percentage points**, inside our 0.5-point limit, so no warning flag is needed. The next 90 days project to the same **+0.61%**, because the mint and the burn both run every day with no dated change. In one line: NEAR is a staking chain that is inflationary by design, with a burn too small to matter.

## Sell pressure: where new NEAR comes from

**Protocol inflation is the whole sell side: 8,005,124 NEAR in 90 days.** NEAR mints new coins once per epoch, a period of 43,200 blocks that lasted about 7.4 hours this window. We read the supply at all 294 epoch starts in the window, and each one added about **26,500 NEAR**. The cap on this mint is **2.5%** of supply a year, set in October 2025 when NEAR cut it in half from 5%. Validators that miss blocks lose part of their reward, and that unpaid part is never minted, so the real rate ran just under the cap. Of the new NEAR, 90% goes to validators and the people who stake with them, and 10% (**804,749 NEAR** this window) goes to the protocol treasury.

**Vesting unlocks are zero.** The founding team says the NEAR supply is fully unlocked, and the circulating figure equals the total supply, so no locked pile is waiting to open. A few old Foundation lockup contracts still exist, but their coins already count as circulating.

**Foundation and unscheduled unlocks are zero.** The protocol treasury, the NEAR Foundation wallets and the buyback wallets all hold coins that the market already counts as circulating. When they move or sell, no new NEAR enters the market, so these moves add nothing to the ledger. We still track their balances in the overhang section below.

**Long-term locked or bankruptcy is zero.** No court estate, trustee or failed company holds NEAR waiting to be paid out.

## Buy pressure: where new NEAR goes

**The programmatic buyback books zero, even though it is real.** Since early 2026, fees from NEAR Intents, NEAR's cross-chain swap service, buy NEAR on the open market. Three buyback wallets went from **2.46M** to **3.66M NEAR** in this window, a gain of **1.20M NEAR**. But the bought NEAR is held, not burned, and it still counts as circulating. Holding coins in a wallet the market already counts does not shrink supply, so the buyback row stays at zero. It does take coins off exchanges for now, which is why we watch these wallets closely.

**The protocol fee burn removed 66,109 NEAR.** Every NEAR transaction pays gas, and the gas is destroyed, except the 30% of contract execution gas that NEAR pays to the contract's owner. We measured the burn as the gap between what was minted and how much supply actually grew, and it matches about 82% of all gas fees paid in the window, as the rule predicts. That is about **735 NEAR a day**. The burn rose late in the window as blocks got busier, but it is still less than 1% of the mint.

**Foundation buy is zero.** We found no announcement or wallet flow showing the NEAR Foundation or the treasury buying NEAR this window; the buying is done by the buyback wallets.

**New long-term lock is zero.** About **551.0M NEAR**, roughly 42% of supply, is staked with 408 validators, and the new Bitwise NEAR ETF stakes all of the NEAR it holds. Staked NEAR can be unstaked and still counts as circulating, so more staking does not take coins out of the float.

## Foundation and overhang

The NEAR Protocol treasury wallet holds **1.25M NEAR**, up from 0.45M at the start of the window because it receives 10% of every mint. The forum puts the wider protocol treasury at about **30M NEAR** once staked coins are counted, and NEAR's co-founder has proposed turning it into a Sovereign Fund; that is still a discussion with no vote. The three buyback wallets hold **3.66M NEAR**. The NEAR Foundation's payments wallet holds **14,248 NEAR**, and an older Foundation wallet paid out about 309,000 NEAR this window. We read these balances from the chain at every rebuild. If any of them falls between refreshes, that outflow is the first thing we check, and it enters the Foundation row at the next refresh.

## How NEAR compares to other proof-of-stake Layer 1s

NEAR sits in the group of proof-of-stake Layer 1 chains with no hard cap, where new coins pay for security. Its design is simple: one yearly ceiling of **2.5%**, minted per epoch, with a small part sent to a treasury. Ethereum works differently: its issuance rises and falls with the amount staked, and part of every fee is burned, so in busy times the burn can match the issuance. Solana prints new coins on a schedule that falls each year toward a long-term floor and burns part of its fees. NEAR's rate is lower than many young Layer 1s, but its gas fees are tiny, so the burn cannot offset the mint the way it sometimes does on Ethereum.

The other difference is where fee money goes. On NEAR, most of the real income comes from NEAR Intents, and that money buys NEAR and holds it instead of burning it. A chain that burns its buybacks shrinks supply directly; a chain that holds them builds a pile that is out of the order books today but could be spent tomorrow. Capped chains with fixed schedules, like Bitcoin, sit at the other end: their new supply is known years ahead and falls in steps. NEAR's supply only gets tighter when its community votes to change the rate, as it did in 2025.

## What to watch in the next 90 days

**The 1.6% issuance vote.** On Sep 30 2026 a House of Stake proposal asked to lower the yearly cap from 2.5% to 1.6%, step by step every epoch over 24 months, with a vote expected by Oct 11 2026. Even if it passes, a 90-day grace period and a protocol upgrade come first, so it should not change the next 90 days.

**The full gas burn.** An approved change ends the 30% gas rebate to contract owners, so all gas would be burned. It is in nearcore 2.14, which reached test releases on Sep 16 2026 and Sep 28 2026 but has no mainnet date yet. Even then the burn would stay far below the mint.

**The buyback wallets and the treasury.** These now hold **3.66M** and **1.25M NEAR**. Any sale or transfer out would put held coins back in play, and any burn would finally make the buyback count on the buy side.

**The Bitwise NEAR ETF.** It began trading on Sep 29 2026 and stakes all of its NEAR. Its buying happens inside the float, so it does not change supply, but large flows would raise the share of NEAR that is staked.

## Summary

NEAR supply is growing: **8.01M NEAR** were minted in the last 90 days against a **66.1K NEAR** gas burn, for **+0.61%** net, and the next 90 days project the same. The mint is capped at 2.5% of supply a year and goes to stakers and the protocol treasury; there is no vesting left and no hard cap on total supply. NEAR Intents buybacks collected 1.20M NEAR this window but hold it rather than burn it, so they do not reduce supply. The main thing that could tighten NEAR's supply is the vote to cut the cap to 1.6%, which would phase in slowly over two years.

---

*MrNasdog Pressure Framework analysis of NEAR, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 1 2026.*

---
title:         "SOL Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "SOL supply is growing: 4.99M SOL of staking issuance plus 5.51M SOL of stake-lock releases against a 74.6K fee burn give +1.74% net in 90 days, +1.31% next."
canonical_url: "https://mrnasdog.com/research/sol/inflation"
tags:          ["crypto", "sol", "solana", "layer1"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/sol/inflation](https://mrnasdog.com/research/sol/inflation)*

# SOL Inflation Analysis · September 2026 · Supply growing · projected to keep growing

Solana's circulating supply grew by a net **+1.74%** over the last 90 days, and the MrNasdog Pressure Framework projects about **+1.31%** for the next 90. Two things drive it: staking issuance, which added **4.99M SOL** to the circulating count, and stake accounts whose lockups ran out, which released another **5.51M SOL**. Against that, the Solana fee burn destroyed only **74.6K SOL** and new locks took **209.2K SOL** out of the count — Solana has no supply cap, and its inflation rate keeps falling by 15% a year toward a 1.5% floor.

## The verdict, in one paragraph

Across the 90 days to Sep 29 2026, SOL sell pressure came to **10.49M SOL** and buy pressure to **283.8K SOL**, a net **+1.74%** of the **587.85M SOL** circulating. The monitor, which reads circulating supply from market data, shows **+1.20%** over the same 90 days, a gap of **0.54 percentage points** — just over the 0.5-point tolerance, so the page carries a warning chip. The monitor's supply series rises on the same days Solana's stake locks opened, but it also fell 3.62M SOL in one day on Jul 29 2026; we found no on-chain flow that size into the locked accounts that day, and without that one step the monitor would read about +1.82%. Our number stays. The next 90 days project **+1.31%**: issuance continues at about 59,000 SOL a day, and fewer locked coins fall due. Solana is structurally inflationary on its circulating float: new coins every epoch, locked coins opening every month, and a burn far too small to offset either.

## Sell pressure: where new SOL comes from

Protocol inflation is the largest row, at **4.99M SOL**. Solana mints new SOL at the start of every epoch and pays it to stake accounts and, as commission, to validators; the yearly rate reads **3.63%** today, set by an 8% starting rate that falls 15% a year. Summed block by block, rewards came to **5.48M SOL** in 90 days, about 61,000 a day. About **9.1%** of that was paid into stake accounts that are still locked or held in reserve, so it does not count as circulating yet; the rest, 4.99M SOL, did.

The window held an unusual change. Solana cut its slot time three times — to 350 milliseconds on Aug 19 2026, to 300 on Aug 25 and to 250 on Sep 18 — so each 432,000-slot epoch now lasts about 32 hours instead of two days. The upgrade raised the chain's “slots per year” figure by the same ratio, so each epoch now pays less and the amount of new SOL per day stays close to where it was. Slots have run a little slower than target at every stage, so the realised rate since the 250-millisecond stage is about 59,000 SOL a day, and that is the rate the next-90-day figure uses: **4.83M SOL**.

Vesting unlocks come second, at **4.31M SOL**. Solana has no vesting contract; instead, some SOL sits in stake accounts with a lockup date, and the chain counts it as circulating once the date passes. One group of about 34 accounts releases about 637,000 SOL on the 7th of every month; three large accounts of **875,000**, **625,000** and **625,000 SOL**, locked since 2024, opened in August; and 14 accounts of 12,499 SOL each opened in mid-September. The next 90 days hold about **2.32M SOL** of these releases, most of it the three monthly tranches on Oct 7, Nov 7 and Dec 7 2026.

The Foundation row reads **594.3K SOL**. On Aug 26 2026 the Foundation split 587,871 SOL into a new stake account and two minutes later handed it to an owner key outside the Foundation's listed keys, which moves it into the circulating count; about 6,500 SOL was also withdrawn early from locked accounts. There is no published schedule for more, so the next 90 days carry 0. The bankruptcy row reads **605.6K SOL**: a bankruptcy estate holds locked SOL that opens one month at a time on the 11th, about 201,000–203,000 SOL each time, and it moves each release out within days. Three more releases, about **609.0K SOL**, fall on Oct 11, Nov 11 and Dec 11 2026.

## Buy pressure: where new SOL goes

There is no programmatic buyback: no contract or treasury buys SOL off the market for the network. The protocol fee burn destroys half of the base fee on every signature — 2,500 of the 5,000 lamports — while priority tips go in full to the block producer. Read from 200 blocks spread across the window, the Solana fee burn came to **74.6K SOL** in 90 days, about 830 a day and roughly 1.4% of new issuance. In August a governance vote on a new fee that would have burned far more SOL failed to reach the two-thirds it needed, so the next 90 days hold the same rate.

There was no Foundation buy. The one real buy-side flow besides the burn is new long-term locks: holders moved **209.2K SOL** into 73 newly created stake accounts locked for a year or more, the largest 160,000 SOL on Jul 7 2026, which takes those coins out of the circulating count. With no schedule behind it, the next 90 days carry 0. Ordinary staking does not count as a lock here — about 441M SOL is staked, and staked SOL stays inside the circulating count.

## Foundation and overhang

About **47.07M SOL** sits outside the circulating count, and all of it was read account by account. The largest part, **27.22M SOL** across 2,270 stake accounts, belongs to keys the validator software lists as Foundation-controlled; it has no release schedule, and one account from it left in August. Another **17.65M SOL** sits in 757 stake accounts with a lockup still in force — the monthly tranches, the bankruptcy estate's releases and custody locks running into 2027 and 2028 — and **2.19M SOL** sits in 97 named reserve accounts. The Foundation buckets are watched at every refresh from the chain itself: if the Foundation or reserve balance falls between refreshes, the outflow enters the Foundation row at the next refresh.

## How SOL compares to other proof-of-stake Layer 1s

Solana belongs to the uncapped, continuous-emission class of proof-of-stake chains. Like Ethereum it pays stakers in new coins and burns part of the fee, but the balance is very different: Ethereum's issuance rises and falls with the amount staked, while SOL's rate follows a fixed disinflation curve, 3.63% today and falling 15% a year. Solana's burn is also far smaller relative to issuance, because its fees are tiny per transaction and half of the base fee — and none of the priority tip — is destroyed.

The second difference is custody-style locks instead of a vesting contract. Chains like Aptos or Sui release team and investor tokens from dedicated unlock schedules; on Solana the equivalent is thousands of individual stake accounts with lockup dates, which is why its unlocks arrive as monthly steps. Compared with capped, halving-model coins such as Bitcoin, SOL has no maximum supply: the floor rate of 1.5% continues forever once the curve reaches it.

## What to watch in the next 90 days

The three monthly stake-lock releases on Oct 7, Nov 7 and Dec 7 2026, about 637,000 SOL each, are the biggest dated supply events. The bankruptcy estate's releases on Oct 11, Nov 11 and Dec 11 2026, about 203,000 SOL each, are the second. SIMD-0550, which doubles the disinflation rate from 15% to 30% a year, passed its vote on Aug 28 2026 but still has no activation date; once live it lowers issuance gradually, not in one step. Mainnet feature activations resume under the next client release window from Nov 9 2026, and the last slot-time stage, 200 milliseconds, would again leave issuance per day unchanged by design. Any further Foundation account leaving its listed keys would add to the Foundation row.

## Summary

SOL supply is growing: the MrNasdog Pressure Framework reads a net **+1.74%** over the last 90 days and projects **+1.31%** for the next 90, against a monitor reading of **+1.20%**. The structure is staking issuance of about 59,000 SOL a day plus stake-account lockups that open on set dates, while the fee burn removes only about 1.4% of what is minted. The key risk is the 47.07M SOL still outside the circulating count, most of it with no release schedule. Solana has no supply cap; its inflation rate only falls, 15% a year today, toward a permanent 1.5%.

---

*MrNasdog Pressure Framework analysis of SOL, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

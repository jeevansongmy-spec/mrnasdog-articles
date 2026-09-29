---
title:         "BONK Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "BONK supply is roughly steady: no new BONK can be made, and burns removed 342.9M BONK in 90 days, −0.0004% of 87.99T. No vesting, no unlocks, the same next."
canonical_url: "https://mrnasdog.com/research/bonk/inflation"
tags:          ["crypto", "bonk", "solana", "memecoin"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/bonk/inflation](https://mrnasdog.com/research/bonk/inflation)*

# BONK Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

BONK, the best-known meme coin on Solana, has a supply that cannot grow: the BONK mint authority is empty, so no new BONK can ever be created, and every allocation from the 2022 launch has already been released. Over the last 90 days burns removed **342.9M BONK** and nothing was added, which the MrNasdog Pressure Framework reads as **−0.0004%** net — a supply that is, for practical purposes, flat. The supply monitor reads **+0.07%**, a gap of **0.07 percentage points**, inside tolerance. With about **87.99T BONK** circulating, the burns are far too small to shrink the float in any way a holder would notice, and the next 90 days project the same.

## The verdict, in one paragraph

BONK supply moved by **−0.0004%** over the 90 days to Sep 29 2026, and the framework projects about **−0.0002%** for the next 90 days. The supply monitor reads **+0.07%** for the same stretch, a gap of **0.07 percentage points** — under the 0.5-point line, so no warning chip is shown. The small difference is day-to-day noise in how the monitor turns market value and price into a supply count; on-chain, the BONK supply only went down. On the framework's scale BONK is a **fixed-supply meme coin with token-level burns too small to matter**: no inflation, and no real deflation either.

## Sell pressure: where new BONK comes from

There is no protocol inflation. BONK is a plain Solana token, and its mint authority — the one key that could create more BONK — was removed. On Solana that removal is final, so Sell #1 is **0** and stays 0. BONK pays no staking rewards and no block rewards; nothing in the design creates new coins.

Vesting unlocks are also **0**. The launch split BONK between airdrops to Solana users, NFT holders and developers, early contributors, the BONK DAO and marketing, and all of those buckets have finished releasing. Unlock trackers show BONK as fully unlocked, the circulating count equals total supply, and no vesting contract sits among the largest BONK holders.

Foundation and unscheduled unlocks are **0**, and this is the row where BONK had its most dramatic event of the year. On Jul 6 2026 an attacker who had bought just over 1% of the BONK supply pushed a governance proposal through a low-turnout vote and moved about **4.43T BONK** out of the DAO treasury. It looked like a flood of new supply, but the treasury coins were already counted as circulating, so the drain changed who held them, not how many BONK were on the market. Today the DAO treasury account and the attacker's accounts are empty — the coins have spread into the float. Long-term locks and bankruptcy estates are **0** too: no estate, trustee or long lock is releasing BONK.

## Buy pressure: where new BONK goes

The buy side is where BONK actually moves, although only slightly. The programmatic buyback row is **154.8M BONK**: one wallet, funded in dollars by a team multisig, bought BONK on the market and burned it twice — **107.3M BONK on Jul 11 2026** and **47.5M BONK on Sep 21 2026**, about $600 in total. Those BONK are destroyed and gone from supply. Because the two firings came 72 days apart with no published schedule, the framework counts none for the next 90 days.

The protocol fee burn is **0**. BONK has no built-in burn: Solana network fees are paid and burned in SOL, and the BONK token charges no fee on transfers. The foundation-buy row is **0** as well — the DAO did not buy BONK this window, and the listed treasury company that buys and sells BONK on the open market only moves coins inside the float. New long-term locks are **0**: staked or pooled BONK still counts as circulating.

The largest buy row is an extra one, holder and app burns: **188.1M BONK**. Every day many wallets burn small amounts of BONK, often leftovers when closing token accounts, and now and then a larger single burn lands, such as **40.3M BONK on Aug 31 2026**. Read from the BONK total supply at both ends of the window, less the buyback above, those burns came to **181.9M BONK**, and another **6.2M BONK** was sent to an address no one can spend from. That is about 2.1M BONK a day, and the framework holds that rate for the next 90 days. Added together, the buy side took **342.9M BONK** out of supply — worth only about $1,200 at today's price.

## Foundation and overhang

BONK has no foundation with a locked reserve, but several known holders could sell. The largest is the listed treasury company, which reported about **2.47T BONK** held with a custodian at the end of June 2026, sold some digital assets in the first half of the year, and has warned that its cash is running low. An old launchpad burn wallet holds **217.2B BONK** that were never burned; it has not moved since Apr 10 2026. A partner company reported buying about **219.7B BONK** in January 2026. The DAO treasury itself is now empty after the July attack.

None of these holdings is new supply: every one of those BONK is already inside the circulating count, so a sale would move coins from one holder to another rather than add to the float. We re-check the chain accounts at every refresh and the company filings every two weeks. If any of these balances fell and the coins left for good — to a burn — the burn would enter the buy side; if a truly locked bucket ever appeared and opened, the outflow would enter Sell #3 at the next refresh.

## How BONK compares to other fixed-supply meme coins

BONK sits in the same family as other large meme tokens whose supply was minted once at launch and can never grow. Against coins that still pay out new tokens — staking-reward chains or tokens with vesting schedules — BONK has no sell-side mechanism at all, which is why its Sell ledger is empty. Its supply story is written entirely by burns.

Among fixed-supply meme coins, the difference is how serious the burn is. Some peers route a large share of trading or app revenue into regular buy-and-burn programs that remove a visible slice of supply every quarter. BONK used to send part of its launchpad revenue to buy-and-burn, but that share was switched in December 2025 to buying BONK for a listed company's treasury, which keeps the coins. What remains is holder burns and occasional small buybacks, adding up to **0.0004%** of supply in 90 days.

Against a proof-of-work coin with a fixed cap, the comparison is closer than it looks: both have supplies that barely move, but for opposite reasons. A capped coin still issues on a schedule; BONK issues nothing and loses a sliver to burns. For BONK, supply is a settled question — price moves come from demand, not from new coins.

## What to watch in the next 90 days

First, the **Oct 7 2026** withdrawal deadline on the Korean exchange that stopped BONK trading on Sep 7 2026: coins leaving that exchange move within the float and add nothing, but the flow is worth watching. Second, the casino partner that launched on Aug 26 2026 says 10% of its fees buy and burn BONK; if those burns appear on-chain at a steady pace, the holder-and-app burn rate would rise. Third, the long-promised burn of **1T BONK** tied to reaching one million holders has no date; if it fires, it would remove about 1.1% of supply in one step, far more than a year of today's burns. Fourth, the listed treasury company's next quarterly filing, which will show whether its **2.47T BONK** stayed put or was sold. Fifth, any new DAO governance vote now that the treasury has been emptied.

## Summary

BONK is a fixed-supply Solana meme coin: its mint authority is gone, nothing vests, and no new BONK can ever be made. Over the last 90 days burns removed **342.9M BONK** — a buyback-and-burn of 154.8M and 188.1M of holder and app burns — for a net of **−0.0004%**, against a supply monitor reading of **+0.07%**. The main supply risk is not new coins but selling by known holders, led by a listed treasury company with about 2.47T BONK, and those coins are already counted. The ceiling is simple: the BONK supply can only stay flat or fall.

---

*MrNasdog Pressure Framework analysis of BONK, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

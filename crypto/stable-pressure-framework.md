---
title:         "STABLE Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "STABLE reads 0.00% over 90 days: 82.0B locked tokens stayed put, nothing was minted or burned, and the new Universal Lock delays releases to Dec 8 2027."
canonical_url: "https://mrnasdog.com/research/stable/inflation"
tags:                    ["crypto", "stable", "layer1", "tokenomics"]
published:     true
---

Originally published at [STABLE Inflation Analysis · September 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/stable/inflation).

# STABLE Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

The MrNasdog Pressure Framework reads STABLE at **0.00%** over the trailing 90 days and **0.00%** over the next 90: on the Stable chain, the team, investor, Foundation and validator wallets holding **82,001.1M STABLE** did not move by a single coin between **Jun 24 2026** and **Sep 22 2026**, and no STABLE was minted or burned. Sell pressure is **0**, buy pressure is **0**, and the monitor's **+10.78%** comes from counting an old Foundation release schedule whose coins never left the wallet. The supply is fixed at **100,000M STABLE**, and the new Universal Lock starts its first release on **Dec 8 2027**.

## The verdict, in one paragraph

Against a circulating base of **26,538.1M STABLE**, the framework books **0** of sell pressure and **0** of buy pressure over the trailing 90 days, a net of **0.00%**, and projects **0.00%** for the next 90 days. The inflation monitor reads **+10.78%** for the same window, a gap of **10.78 percentage points**, far over the framework's 0.5-point tolerance, so the overview ships with a monitor-gap warning. The gap has one cause, and it was checked wallet by wallet: the monitor adds about **29.2M STABLE a day**to the float because the Stable Foundation's original 36-month schedule says those coins are unlocked, while the Foundation's locked wallet held exactly **21,000M STABLE** at both ends of the window. Coins that never leave the wallet never reach the market. The label for STABLE is a **paper unlock that never moved**: the release existed on a calendar, not on the chain.

## Sell pressure: where new STABLE comes from

Protocol inflation is **0**. All **100,000M STABLE** were issued in one event on **Dec 8 2025**, and the count of STABLE in existence read the same at both ends of the window. STABLE lives in the Stable chain's bank module, and a test call asking it to mint new STABLE is refused with the chain's own message that minting the governance token is not allowed. Validators and delegators on Stable are paid from gas fees, and those fees are paid in USDT0, so securing the network creates no new STABLE. A chain upgrade could in principle change the rule, so the row is watched rather than closed for good.

Vesting unlocks are **0**, and this is the row the whole page turns on. STABLE's locked supply sits in four places on the Stable chain: two wallets of **25,000M STABLE**each for the team and for investors and advisors, the Stable Foundation's locked ecosystem wallet at **21,000M**, and the staking pool holding the **11,000M** validator allocation plus about 1.1M of outside delegations, for **82,001.1M**in total. Every one of them held the same balance on Jun 24 2026 and on Sep 22 2026. Under the original terms, the Foundation's locked 32,000M was meant to release over 36 months, which would have been about **2,627.7M STABLE** in these 90 days. None of it moved. The framework counts what reaches the market, not what a calendar allows, so the row is zero, and the scheduled figure is logged beside it for the next rebuild.

The forward column is also **0**. Stable's whitepaper, revised in August 2026, replaces every earlier vesting plan with a single Universal Lock over all **82,000M** locked STABLE, effective **Oct 5 2026**. Its first floor starts on **Dec 8 2027** and the last release lands on **Dec 8 2029**. The old one-year cliff for the team and investors, which would have fallen on **Dec 8 2026**, is gone.

Foundation and unscheduled unlocks are **0**. The Foundation's day-one wallet, which already counts as tradable, held **7,538.85M STABLE** at both ends and sold nothing. Long-term locked or bankruptcy supply is **0** too: STABLE has no bankruptcy estate, trustee or court-ordered distribution.

## Buy pressure: where new STABLE goes

Programmatic buyback is **0**. Stable runs no programme that buys STABLE on the open market. Gas income arrives in USDT0 and is passed to validators and stakers in USDT0. A fee switch that would route part of that income to STABLE holders has been discussed in public, but nothing has been decided.

Protocol fee burn is **0**, and it was checked from both sides. The count of STABLE in existence stayed at **100,000M**, and the usual dead addresses hold nothing. A test call to burn STABLE is refused by the chain itself. Because fees are paid in USDT0, using the Stable network never destroys STABLE.

Foundation buy is **0**: the Foundation's wallets held the same balances at both ends of the window. New long-term lock is **0** as well. Staked STABLE held at **11,001.1M**on both dates. The Oct 5 2026 relock covers Foundation coins that were unlocked on paper but never left the Foundation's wallet, so it takes nothing out of the market and is not booked as buy pressure.

## Foundation and overhang

The overhang on STABLE is large, fully named and, for now, frozen. The team wallet and the investor wallet hold **25,000M STABLE** each, the Stable Foundation's locked wallet holds **21,000M**, and the validator allocation of **11,000M** is staked. Together they are the **82,000M**Universal Lock pool, and none of it has moved since the first days of December 2025. The Foundation's day-one wallet adds **7,538.85M STABLE** of already-tradable supply that did not move in the window. All five balances are read straight from the Stable chain at every rebuild.

One detail matters most before Oct 5 2026. Part of the Foundation's locked wallet is already unlocked under the old schedule, so until the relock takes effect the Foundation could in principle spend it. The wallet has never sent a single coin. If any of these balances falls between rebuilds by more than the Universal Lock allows, that outflow enters Sell #3 at the next refresh.

## How STABLE compares to other fixed-supply governance tokens

STABLE sits in a small group: a staking and governance token on a chain where gas is paid in something else. On most proof-of-stake chains, validators are paid in new units of the native token, so a yearly emission of several percent is normal. Stable pays its validators in USDT0 gas income, which is why the STABLE supply can stay at exactly 100,000M while the network runs. On the issuance axis that is stricter than a Bitcoin-style halving chain, which still mints on every block at a falling rate.

The real risk for a token like this is unlocks, not minting. Many recently launched tokens release team and investor coins on a one-year cliff and then month by month, and the tradable float jumps on known dates. STABLE's Universal Lock is a different shape: one pro-rata calendar for team, investors and Foundation, seven floors from Dec 8 2027, each released day by day over about six months, and a price floor that delays a floor by three months if the 30-day average price is under $0.025. It pushes supply growth later, but it does not shrink it: by Dec 8 2029 all 82,000M locked STABLE are scheduled to be released.

Exchange tokens with regular buybacks and burns can show a shrinking supply. STABLE has no such mechanism today, and its governance token cannot be burned through the bank module at all. Until a fee switch is approved, STABLE's best case is what this window shows: a flat float.

## What to watch in the next 90 days

First, **Oct 5 2026**, when the Universal Lock takes effect and the Foundation's paper-unlocked coins are relocked; the monitor's counted float may drop when that happens, even though no coin moves. Second, **Dec 8 2026**, the date of the old team and investor cliff, which the new lock replaced; the two **25,000M STABLE** wallets should stay still. Third, the Foundation's locked wallet at **21,000M STABLE** and its day-one wallet at **7,538.85M**, the only large balances with a spender rather than a schedule. Fourth, Stable governance: the only vote passed in the window was the v1.8.0 chain upgrade on **Aug 26 2026**, which did not touch supply, but a fee switch or a change to the bank module would. Fifth, the 30-day average price against the **$0.025** safety floor, which only matters from late 2027 but can already delay the first release.

## Summary

The MrNasdog Pressure Framework reads STABLE at **0.00%** over the trailing 90 days and **0.00%** projected forward: mixed flows, supply roughly steady. Nothing was minted, nothing was burned, and the **82,001.1M STABLE** in the team, investor, Foundation and validator wallets did not move. The key risk is timing, not rate: the Universal Lock only delays the release of 82,000M locked STABLE, which starts on **Dec 8 2027** and ends on **Dec 8 2029**. The ceiling is a fixed **100,000M STABLE** that the chain refuses to mint beyond.

MrNasdog Pressure Framework analysis of STABLE, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 22 2026.

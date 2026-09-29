---
title:         "NEAR Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "NEAR supply is growing: a 2.5% yearly epoch mint of 7.98M NEAR against a 63.6K gas burn gives +0.61% net over 90 days, the same next. Fully unlocked, no cap."
canonical_url: "https://mrnasdog.com/research/near/inflation"
tags:          ["crypto", "near", "near-protocol", "layer1"]
published:     true
---

*Originally published at [mrnasdog.com/research/near/inflation](https://mrnasdog.com/research/near/inflation)*

NEAR Protocol is mildly inflationary. Over the 90 days to Sep 29 2026 the NEAR epoch mint created **7.98M NEAR** while the gas burn destroyed **63.6K NEAR**, so NEAR supply grew a net **+0.61%** — and the same mint rate points to about **+0.61%** again over the next 90 days. NEAR has no supply cap: the 2.5% yearly mint runs forever unless a vote changes it, and the fees that buy NEAR back are held rather than burned.

## The verdict, in one paragraph

Our ledger reads NEAR supply up **+0.61%** over the last 90 days (7,980,727 NEAR minted, less 63,617 NEAR burned, on a circulating base of 1.31B NEAR). The inflation monitor, which reads supply from market-data snapshots, shows **+0.41%** for the same stretch. The gap is **0.20 percentage points** — inside our 0.5-point tolerance, so no warning chip is shown and no deeper check was needed; the monitor's supply series moves around a little from day to day, while ours is read block by block from the NEAR chain itself. The next 90 days project the same **+0.61%**, because nothing dated changes the mint or the burn. NEAR is a steady, uncapped-emission Layer-1: inflationary by design at a low, predictable rate, with almost nothing on the other side of the ledger.

## Sell pressure: where new NEAR comes from

All new NEAR comes from one place: protocol inflation. At the first block of every epoch — an epoch is 43,200 blocks, about **7.4 hours** at NEAR's current block time of about 0.61 seconds — the NEAR protocol creates new coins at a rate of **2.5% a year** of total supply. About 90% goes to validators and the people who stake with them, and about 10% goes to the protocol treasury. We read the NEAR supply at each of the **293** epoch starts in the window and added up the new coins: **7,980,727 NEAR**, or about 88,700 NEAR a day. That lands within half a percent of what the 2.5% rate predicts; the small shortfall is reward that validators forfeit when they miss blocks.

The 2.5% rate is new. NEAR ran a 5% yearly inflation rate from its 2020 launch until a validator vote cut it in half; the change went live on **Oct 30 2025**, well before this 90-day window. The mint was flat inside the window — about 2.66M NEAR in each 30-day third — so the forward figure simply holds the trailing amount.

The other three sell rows are zero. NEAR vesting unlocks are over: the 2020 lockups for early backers, the team and the NEAR Foundation have run out, an unlock tracker lists NEAR as fully unlocked, and the circulating count equals total supply to within 4 NEAR. Foundation and unscheduled unlocks are zero for the same reason — every team wallet already sits inside the circulating count, so moving or selling those coins adds nothing new to it. There is no bankruptcy estate and no long lock releasing NEAR.

## Buy pressure: where new NEAR goes

One row takes NEAR off the market: the protocol fee burn. Every NEAR transaction pays gas, and **70%** of that gas is destroyed; the other 30% is paid to the smart contract that was called. There is no burn address — burned gas simply leaves the NEAR supply total. Supply at both ends of the window, with the minted coins added back, gives a burn of **63,617 NEAR**, about 707 NEAR a day; a sample of 1,500 blocks read the other way lands within 1% of it. The mint is about **125 times** larger than the burn, so the burn trims NEAR inflation by less than 1% of itself.

The programmatic buyback books zero, and this needs care. Since Feb 23 2026, fees from NEAR Intents — NEAR's cross-chain swap service — are used to buy NEAR on the open market. That buying is real: the buyback wallet grew from about 0.49M to about **1.82M NEAR** in this window. But the bought NEAR is held, not burned, and a held coin stays inside the circulating count. So the NEAR buyback supports the price without shrinking the float, and our supply ledger counts it as zero.

Foundation buying is zero: nothing this window shows the NEAR Foundation buying NEAR for itself. New long-term locks are zero too. About **539M NEAR** is staked with validators and holders lock more to vote in NEAR governance, but staked and vote-locked NEAR stays in the circulating count and can be withdrawn within days, so it removes nothing from the float.

## Foundation and overhang

Five team-controlled NEAR balances are tracked. The protocol treasury holds about **1.23M NEAR** liquid, up from 0.43M at the start of the window as its 10% slice of each epoch mint arrived. The NEAR Intents buyback wallet holds about **1.82M NEAR**, and a front-end revenue wallet about **1.80M NEAR**. A NEAR Foundation payments wallet holds about 84K NEAR, and the Foundation's wider reserve was last disclosed publicly in 2023. A proposed sovereign fund of about 30M NEAR, built from the protocol treasury and swap revenue, is still a forum discussion with no vote. We read the on-chain wallets every day and check the Foundation's disclosures every two weeks.

Every one of these balances already counts as circulating, so none of them can add new NEAR to the float. What they can do is sell into it. If any of these balances falls between our checks, the outflow will show up in the Foundation and unscheduled unlocks row at the next refresh.

## How NEAR compares to other proof-of-stake Layer-1s

NEAR sits in the uncapped, continuous-emission group of proof-of-stake Layer-1 chains. Unlike Bitcoin, which halves a fixed block reward toward a hard cap, NEAR mints a fixed percentage of supply every epoch with no end date. At 2.5% a year, NEAR now issues less than many stake-heavy chains that pay 5% or more, and roughly half of what NEAR itself paid before October 2025.

The burn is where NEAR differs from Ethereum. Ethereum also pays validators in new coins, but its fee burn can match the new issuance when the chain is busy. NEAR's gas is cheap and part of each fee goes to contract owners, so the burn removes well under 1% of what the mint creates. Most of NEAR's fee income comes from NEAR Intents swaps rather than gas, and that money buys and holds NEAR instead of burning it — a treasury model, closer to a company buying its own shares and keeping them than to a burn.

NEAR has no vesting overhang left, which sets it apart from younger Layer-1 chains still releasing team and investor tokens every month. The whole NEAR sell side is one visible, rules-based mint.

## What to watch in the next 90 days

**The gas-rebate removal.** NEAR governance voted on Jul 3 2026 to end the 30% gas payment to contracts and burn the full fee. It ships in the next NEAR node version, which has been on test builds since Sep 16 2026 but has no mainnet date yet. Even if it went live today, it would add only about 27K NEAR a quarter to the burn.

**A move away from the fixed mint.** A forum proposal posted on Sep 11 2026 asks NEAR to cut issuance step by step as protocol revenue grows. It is a discussion, not a vote; a passed vote would change the protocol inflation row.

**The sovereign fund.** A proposal from Aug 3 2026 would pool the protocol treasury and swap revenue, about 30M NEAR, into a fund. If it passes, what the fund does with that NEAR — hold, stake or spend — is what matters for sell pressure.

**The buyback wallet.** Watch whether NEAR bought back with swap fees keeps being held, gets burned, or is paid out. A burn would turn the buyback into real buy pressure; a payout would add sell pressure.

## Summary

NEAR Protocol is mildly inflationary: a 2.5% yearly epoch mint added **7.98M NEAR** in 90 days against a **63.6K NEAR** gas burn, for net NEAR supply growth of **+0.61%**, projected to repeat over the next 90 days. There are no unlocks left and every team wallet is already counted, so the whole sell side is the protocol mint itself. The NEAR Intents buyback is real buying, but it holds the coins rather than burning them, so it does not shrink supply. With no cap, the one thing that can change NEAR's inflation is a governance vote to cut the mint or to burn what the buyback holds.

---

*MrNasdog Pressure Framework analysis of NEAR, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

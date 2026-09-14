---
title: "LINK Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description: "Supply growing: Chainlink mints no LINK, but a 21.0M reserve release on Jun 19 2026 outweighed 1.66M bought and held by the Chainlink Reserve. Net +2.59%."
canonical_url: "https://mrnasdog.com/research/link/inflation"
tags: ["crypto", "link", "chainlink", "oracles"]
published: true
---

> Originally published at **[mrnasdog.com/research/link/inflation](https://mrnasdog.com/research/link/inflation)** by MrNasdog.

LINK, the token of the Chainlink oracle network, can never be minted — the LINK supply is fixed at **1B** and the token contract has no function that creates a coin. LINK supply still reaches the market, because Chainlink releases LINK from a **251.90M** team reserve at a stated pace of **7%** of supply a year: one release of **21.0M LINK** landed on **Jun 19 2026**. Against it, the Chainlink Reserve bought **1.66M LINK** with fee income and holds it. The MrNasdog Pressure Framework reads LINK at **+2.59% net** over the last 90 days against a supply-monitor reading of **+2.81%** — a gap of **0.22 percentage points**, inside tolerance. LINK is capped, but mildly inflationary on its tradable float until the reserve runs out.

## The verdict, in one paragraph

For the 90-day window ending **Sep 14 2026**, the Pressure Framework reads **LINK at +2.59% net**: **21.0M LINK** left the Chainlink reserve wallets while the Chainlink Reserve lifted **1.66M LINK** back off the market. The independent supply monitor reads the realised 90-day change at **+2.81%**. The gap is **0.22 percentage points**, inside the framework's half-point tolerance, so LINK ships with **no data-conflict flag** — and the gap has a known cause: the monitor still counts the LINK held by the Chainlink Reserve as circulating, and that balance grew by almost exactly the difference. The forward column reads **+2.12%**, because the next LINK reserve release is expected by **Oct 9 2026** at about **17.5M LINK**. The label for LINK is **capped but diluting by reserve release**: a token with no mint whose float still grows every few months.

## Sell pressure: where new LINK comes from

Sell #1, protocol inflation, is **zero**, and permanently so. Every LINK was created at launch in 2017 and the LINK token contract on Ethereum has no mint, no owner and no upgrade path. That was checked in the contract code rather than taken from the supply figure, because the LINK supply number is written into the code as a constant and would read 1B even if a mint existed — the code carries only transfer, approval, balance and label functions, so no route to a new LINK exists. Sell #2, vesting unlocks, is **zero**: LINK has no vesting calendar, no cliff and no lock contract releasing coins on a schedule.

Sell #3, foundation and unscheduled unlocks, is the whole LINK sell side: **21.0M LINK**. Chainlink publishes 33 reserve wallets that sit outside the LINK circulating count, and every one was read at both ends of the window. Together they fell from **272.90M** to **251.90M LINK**, and subtracting the end balance from the 1B supply reproduces the circulating LINK count to the coin, so no reserve wallet was missed. The whole move was one LINK release on **Jun 19 2026**: **18.375M LINK** went through a pass-through address to an exchange wallet the same evening, and **2.625M LINK** went to a team payout wallet. Chainlink states the pace as 7% of supply a year, and the chain agrees exactly — the last four LINK releases, on **Oct 10 2025**, **Dec 19 2025**, **Apr 3 2026** and **Jun 19 2026**, add up to **70M LINK**, 7% of the cap. The releases are lumpy, from **11.25M** to **21.0M**, and arrive 70 to 112 days apart, so the forward column books one dated release rather than a smoothed rate. Sell #4, long-term locked or bankruptcy supply, is **zero**: no estate or trustee holds LINK.

## Buy pressure: where new LINK goes

Buy #1, the programmatic buyback, is the Chainlink Reserve at **1.66M LINK**. Chainlink's payment system lets customers pay for Chainlink services in other assets; that income is converted into LINK on decentralized exchanges and a share is deposited into the Chainlink Reserve once a week. Thirteen weekly deposits took the Chainlink Reserve from **4.21M** to **5.86M LINK**, an addition of **1,655,398 LINK**, and not one LINK left it. The source of that LINK was traced rather than assumed. The contract that feeds the Chainlink Reserve also pays node operators, and it is funded from two directions — LINK bought on exchanges, and LINK sent from team payout wallets. Week by week, its deposit into the Chainlink Reserve equals its exchange-bought LINK exactly, and its payouts to operators equal its team-wallet funding exactly, so the LINK in the Chainlink Reserve came off the market. The weekly LINK amount is falling — from about **154K** in late June to about **91K** in September as the LINK price rose — so the coin count fell faster than the dollar income behind it.

Buy #2, the protocol fee burn, is **zero**: LINK has no burn, and the dead address gained less than 1 LINK of stray transfers. Buy #3, foundation buying, is **zero** — the team payout wallets only send LINK out. Buy #4, new long-term locks, is **zero**: Chainlink staking holds **42.53M LINK**, but the community pool sat full at its **40.875M** cap all window and the operator pool shrank from **1.73M** to **1.66M LINK**, so no new LINK was locked.

## Foundation and overhang

The headline LINK overhang is the reserve itself: **251.90M LINK** across the 33 published wallets, a quarter of the entire cap and about three and a half years of releases at the stated pace. Three further balances sit inside the circulating count and are watched on every refresh. The team payout wallet holds **9.56M LINK** and passes about 500K a month toward node-operator pay. The staking reward pool holds **2.81M LINK**; it received one **607,500 LINK** top-up on **Jun 24 2026** and paid slightly more than that out to stakers. The Chainlink Reserve holds **5.86M LINK**; Chainlink has said it expects no withdrawals for multiple years, and any withdrawal must wait out a multi-day delay. Chainlink has no DAO treasury and no bankruptcy residual. If any of these balances falls between refreshes without the LINK landing in another tracked wallet, the outflow enters Sell #3 at the next refresh — and a sale from the Chainlink Reserve would turn the largest buy line into a sell line.

## How LINK compares to other capped utility tokens

LINK sits in the class of tokens with a hard cap and no emission, which separates it cleanly from proof-of-stake Layer 1s. An uncapped chain token pays validators in newly minted coins, so its float grows by protocol design; LINK pays node operators and stakers out of a supply that already exists, so the dilution is a release of old coins rather than the creation of new ones. That makes LINK's end point visible — once the 251.90M reserve is spent, LINK sell pressure from the reserve ends — but it also means the pace is set by a team decision, not by code.

Against tokens that burn, the distinguishing feature is where the Chainlink buyback goes. A burn removes coins for good; the Chainlink Reserve holds what it buys, so LINK gets the market bid without the permanent supply cut, and the Chainlink Reserve becomes a new overhang of its own. Against exchange tokens that destroy reserve coins on a quarterly schedule, LINK runs the other way round: its scheduled flow adds LINK to the market, and its buyback is the smaller, continuous offset. At the current pace the Chainlink Reserve absorbs roughly **8%** of what the LINK reserve releases.

## What to watch in the next 90 days

First, the next LINK reserve release: the gap since **Jun 19 2026** has reached 87 days, the longest gap on record is 112, so a release of roughly **17.5M LINK** is expected by **Oct 9 2026**; a second release before **Dec 13 2026** would lift the forward reading toward **+4.5%**. Second, the size of that release, which has ranged from **11.25M** to **21.0M LINK**. Third, the Chainlink Reserve's weekly deposit, which fell to about **91K LINK** by **Sep 10 2026**; Chainlink said on **Jun 26 2026** that more commercial income will be converted to LINK, which could lift it. Fourth, Chainlink staking: the community pool is full, and a larger cap would open Buy #4 for the first time.

## Summary

The MrNasdog Pressure Framework reads LINK at **+2.59% net** over the trailing 90 days and **+2.12%** over the next 90. The structural mechanism is a fixed 1B LINK supply with no mint, diluted by releases from a 251.90M team reserve at 7% of supply a year and partly offset by the Chainlink Reserve, which buys LINK with fee income and holds it. The key risk is timing and size set by the team rather than by code, plus the Chainlink Reserve itself, whose 5.86M LINK would become sell pressure if it were ever spent. The cap on future dilution is the reserve: when those 251.90M LINK are gone, the release side of the LINK ledger ends.

---

*MrNasdog Pressure Framework analysis of LINK, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 14 2026.*

---
title: "LINK Inflation Analysis · September 2026 · Mixed last 90D, projected to grow"
description: "Mixed last 90D, projected to grow: Chainlink mints no LINK, but 30.0M LINK of team-reserve releases are due by Dec 18 2026, taking LINK from 0.00% to +4.01%."
canonical_url: "https://mrnasdog.com/research/link/inflation"
tags: ["crypto", "link", "chainlink", "oracles"]
published: true
---

> Originally published at **[mrnasdog.com/research/link/inflation](https://mrnasdog.com/research/link/inflation)** by MrNasdog.

Chainlink's LINK token has a fixed supply of **1B LINK** and no mint, so new LINK never comes from issuance — it comes from **251.90M LINK** held in 33 team reserve wallets, which Chainlink releases at a stated **7% of supply a year**. No release landed in the 90 days to **Sep 25 2026**, nothing was burned, and the Chainlink Reserve's buying stayed inside the counted float, so the MrNasdog Pressure Framework reads LINK at **0.00% net** against a supply-monitor reading of **−0.03%**. The next 90 days are different: two LINK releases totalling **30.0M LINK** are due, which puts the forward reading at **+4.01%**.

## The verdict, in one paragraph

For the 90-day window ending **Sep 25 2026**, the Pressure Framework reads **LINK at 0.00% net**: every sell row and every buy row is zero, because all 33 LINK reserve wallets held exactly the same balance at both ends of the window. The independent supply monitor reads the realised 90-day change at **−0.03%**. The gap is **0.03 percentage points**, far inside the framework's half-point tolerance, so LINK ships with **no data-conflict flag**. The flat reading is a matter of timing, not of policy: the last LINK release, **21.0M LINK** on **Jun 19 2026**, came eight days before the window opened, and the forward column books the next two by date — **18.75M** in the autumn and **11.25M** on **Dec 18 2026** — for **+4.01%** of circulating supply. The label for LINK is **fixed supply, released in steps**: a token that can never mint, whose float grows on a published yearly rate from team-held reserves.

## Sell pressure: where new LINK comes from

Sell #1, protocol inflation, is **zero**, and this was proven rather than read off a flat number. The LINK token contract returns the same **1B** total every time because that total is written into its code, so a steady reading on its own proves nothing. What settles it is the contract's own list of functions: transfer, approve, the transfer-and-call hook Chainlink uses for payments, and the standard read functions — no mint, no burn, no owner and no upgrade path. Chainlink node operators and LINK stakers are paid in LINK that already exists. Sell #2, vesting unlocks, is **zero** because LINK has no dated vesting calendar at all: the team's share was never put on a cliff schedule, and no unlock tracker carries a live dated LINK schedule.

Sell #3, foundation and unscheduled unlocks, is where all LINK supply growth lives. Chainlink publishes the 33 wallets it counts as non-circulating, and their balances add up to **251.90M LINK** — exactly the gap between the fixed **1B** supply and the **748.10M LINK** circulating figure, to the last unit. That closure matters: it shows the published cluster is the whole of the excluded supply, so a LINK coin counts as new supply at one moment only, when it leaves one of those 33 wallets. None of them moved in this window, so the row reads **0** for the last 90 days. Their history is unusually regular. Since mid-2023 LINK releases have run in a fixed four-step rotation — **21.0M**, **18.75M**, **11.25M** and **19.0M**, **70.0M** a year, matching the stated **7%** — each on a Friday, usually the third Friday of the last month of a quarter, and sent mostly to one exchange deposit address. The autumn release, **18.75M**, came on **Oct 10** last year and has not come yet; the December release, **11.25M**, has landed on Dec 15, Dec 20 and Dec 19 in the last three years, and **Dec 18 2026** falls inside the forward window. Sell #4, long-term locked or bankruptcy supply, is **zero**: no estate or trustee distributes LINK.

## Buy pressure: where new LINK goes

Buy #1, programmatic buyback, is **zero** on the ledger, even though a real buyer exists. The Chainlink Reserve converts fees the Chainlink network earns into LINK and adds it every week; it took in **1.54M LINK** this window, rising to **6.05M LINK**, and it has never paid anything out. But the Reserve is not one of the 33 excluded wallets, so the circulating LINK figure already counts it. A purchase into it moves LINK from a seller to another holder inside the same float and takes nothing off the market, so it books zero — and the Reserve is watched as a LINK holder instead.

Buy #2, protocol fee burn, is **zero**: Chainlink routes the fees paid for data feeds and cross-chain messages to node operators and the Reserve, and no part of them is destroyed. Both surfaces were read — the fixed total supply, and the dead address, which collected less than one stray LINK this window. Buy #3, foundation buying, is **zero**: the team does not buy LINK for its own wallets. Buy #4, new long-term locks, is **zero**: Chainlink staking is capped, the community staking pool sat full at **40.88M LINK** for the whole window, and the operator pool shrank slightly to **1.65M LINK**. Staked LINK is counted as circulating in any case, so a larger stake would not reduce the float.

## Foundation and overhang

The one LINK overhang that decides the reading is the team reserve itself: **251.90M LINK** across 33 published wallets, about **34%** of circulating supply, released at **70.0M LINK** a year. At that stated rate the reserve runs for roughly three and a half more years. Three further team-linked LINK balances are watched although they already sit inside the float: a team wallet that takes a slice of each release and pays out about **0.5M LINK** a month, now **9.56M LINK**; the Chainlink Reserve at **6.05M LINK**; and the staking reward vault at **2.78M LINK**. All are on-chain and re-read at every refresh. If any of the 33 reserve wallets falls between refreshes, the outflow enters Sell #3 at the next refresh; moves out of the three inside balances change who holds LINK, not how much LINK is on the market.

## How LINK compares to other fixed-supply infrastructure tokens

LINK sits in a different class from both of the common L1 shapes. An uncapped proof-of-stake chain mints new coins every block to pay validators, so its float rises smoothly and a fee burn is the only offset. A capped proof-of-work coin issues a block subsidy that halves on a timetable until the cap is reached. LINK does neither: its supply was minted in full at launch, and its float rises only when the team moves LINK out of reserve wallets — in steps, on dates, at a published yearly rate. That makes the LINK sell side lumpy rather than continuous, which is why one quarter can read flat and the next read above four percent.

Against tokens with investor vesting cliffs, the difference is that LINK's release is discretionary in timing but has been steady in size, and the reserve wallets are published, so every release is visible the day it happens. Against exchange tokens that burn a slice of revenue, LINK's buyer works the other way: the Chainlink Reserve buys LINK with network fees and holds it rather than destroying it, so it adds steady demand without shrinking the counted supply. The Reserve's buying — about **1.54M LINK** a quarter — is small next to a single LINK release, so for now the reserve schedule, not the buyer, sets the direction of LINK supply.

## What to watch in the next 90 days

First, the autumn LINK release of about **18.75M LINK**: it is already past its usual third-Friday slot of **Sep 18 2026**, and last year it came on **Oct 10**. Second, the December LINK release of about **11.25M LINK**, expected on **Dec 18 2026**; if it slips past **Dec 24 2026** the forward reading falls to about **+2.51%**. Third, any change to Chainlink's stated **7%** yearly release rate, which would move every future LINK row at once. Fourth, the Chainlink Reserve at **6.05M LINK**: Chainlink has said it does not expect withdrawals for years, and any outflow would show up on the next refresh. Fifth, a new Chainlink staking version with a larger cap, which would lock more LINK but still leave it inside the counted float.

## Summary

The MrNasdog Pressure Framework reads LINK at **0.00% net** over the trailing 90 days and **+4.01%** over the next 90, with a supply monitor at **−0.03%** and no data-conflict flag. The structural mechanism is a fixed **1B LINK** supply with no mint and no burn, whose float grows only as Chainlink releases a **251.90M LINK** team reserve at **7%** of supply a year in four steps. The key risk is timing: two releases, **30.0M LINK** in all, are due before the end of the year, while the Chainlink Reserve's weekly buying stays inside the float and does not offset them. The ceiling is the **1B** cap itself — once the reserve is spent, in roughly three and a half years at the stated rate, LINK supply stops growing.

*MrNasdog Pressure Framework analysis of LINK, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 25 2026.*

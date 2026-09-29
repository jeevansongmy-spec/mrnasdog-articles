---
title:         "AAVE Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "AAVE supply is roughly steady: +0.13% over 90 days, +0.14% next. No mint, no burn; one DAO reserve paid 19.3K AAVE to stakers and grants, buyback paused."
canonical_url: "https://mrnasdog.com/research/aave/inflation"
tags:                    ["crypto", "aave", "defi", "tokenomics"]
published:     true
---

Originally published at [AAVE Inflation Analysis · September 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/aave/inflation).

# AAVE Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

The MrNasdog Pressure Framework reads AAVE at **+0.13% net** over the trailing 90 days and **+0.14%** over the next 90: the Aave DAO’s Ecosystem Reserve paid out **19,295 AAVE** — **14,889 AAVE** of Safety Module staking rewards and **4,406 AAVE** of grant streams — while nothing was bought back or burned. AAVE supply is fixed at **16M** and the token has no mint, so every new tradable AAVE comes from one reserve that still holds **570,145 AAVE**. The AAVE buyback has been paused since **Apr 19 2026**, which leaves the reserve drip with nothing on the other side.

## The verdict, in one paragraph

AAVE’s circulating supply grew **+0.13%** in the 90 days to Sep 29 2026, and the framework projects **+0.14%** for the 90 days to Dec 28 2026. The inflation monitor reads **+1.67%** for the same window, a gap of **1.55 percentage points**, which is over the half-point line, so the page carries the ⚠ monitor-gap chip. Almost all of that gap is one recount: on Jul 19 2026 the circulating count the monitor reads jumped by about **236K AAVE** in a single day with no matching move on-chain, which fits the DAO buyback wallet’s flat **240.5K AAVE** being counted as circulating from that day. The on-chain reading stands. AAVE is a **fixed-supply governance token with a slow reserve drip**: a small, steady leak with no buyer turned on.

## Sell pressure: where new AAVE comes from

Sell #1, protocol inflation, is **14,889 AAVE**. AAVE has no mint function and its total supply read exactly 16,000,000 at both ends of the window, so the only “new” AAVE is paid out of the Ecosystem Reserve to people who stake in the Aave Safety Module. The main stkAAVE pot earns **150 AAVE a day**, the rate the DAO set in May 2026 when it cut emissions from 220 a day. Three older staking pots (the AAVE/wstETH pool token, the first AAVE/ETH pool token and staked GHO) now earn nothing but still pay out rewards earned earlier. Stakers claimed a little more than 150 a day because an August 2026 top-up of the reserve’s spending limit let a backlog of unclaimed rewards be paid; every claim was matched against the reserve balance, which fell by exactly the amount paid out.

Sell #2, vesting unlocks, is **4,406 AAVE** over the last 90 days and **7,089 AAVE** for the next 90. Three grants stream AAVE out of the reserve by the second. The largest is the **75,000 AAVE** grant to Aave Labs approved under the “Aave Will Win” vote, streaming over four years from Apr 13 2026 at about 51 AAVE a day. Two service-provider grants of **5,000 AAVE** each run for one year at about 14 AAVE a day each; one of them has not been drawn at all yet. Grantees withdraw in lumps, so the last 90 days counts what they actually took, and the next 90 days counts what the streams will earn. In total **78,087 AAVE** is still owed on the three streams.

Sell #3, foundation and unscheduled unlocks, is zero: the Ecosystem Reserve is the only AAVE outside the circulating count, and every coin that left it is already booked in Sell #1 and Sell #2. Sell #4, long-term locked or bankruptcy, is zero: no estate or long lock holds AAVE, and the old LEND-to-AAVE swap contract that created most of the supply is empty.

## Buy pressure: where new AAVE goes

Buy #1, programmatic buyback, is zero. The Aave DAO bought AAVE on the open market from April 2025, but it stopped on Apr 19 2026 after a bridge exploit pushed unbacked rsETH into Aave markets, and the DAO later put **25,000 ETH** toward restoring that backing. An automatic “Aavenomics 3.0” buyback was announced on Jun 25 2026; as of Sep 29 2026 it has not started, and holders on the governance forum are still asking for a date. Even the AAVE bought earlier removes nothing today: the buyback wallet holds **240,502 AAVE** as deposits in Aave itself and is counted as circulating, and nothing flowed back into the reserve this window.

Buy #2, protocol fee burn, is zero. Aave fees go to the DAO treasury, not to a burn address, and only dust reached the dead address. Buy #3, foundation buy, is zero: no team or DAO wallet bought AAVE into a balance outside the float. Buy #4, new long-term lock, is zero even though the Safety Module grew from **2.16M** to **2.49M AAVE** staked this window — staked AAVE can leave after a two-day cooldown and is counted as circulating, so a bigger stake takes nothing off the market.

## Foundation and overhang

The one overhang that matters is the Aave **Ecosystem Reserve**, the DAO’s store of **570,145 AAVE**, down from 589,440 at the start of the window. It funds staking rewards and the three grant streams, and a new grant or a higher staking rate would raise the Sell rows directly. The DAO also holds AAVE that is already counted as circulating: the buyback wallet at **240,502 AAVE** (unchanged all window), the treasury at about **6,591 AAVE** and an old claims contract at **7,512 AAVE**. Aave Labs holds about 5,596 AAVE from its stream and has not sold it. We read these balances on-chain at every rebuild. If the reserve’s balance falls between refreshes by more than the staking rewards and streams explain, the outflow enters Sell #3 at the next refresh.

## How AAVE compares to other DeFi governance tokens

Among DeFi governance tokens, AAVE sits in the fixed-cap, reserve-funded group. Like Compound’s COMP, its whole supply already exists and new tradable coins only appear when a DAO reserve pays them out, so AAVE inflation is a spending decision rather than a mining schedule. That is very different from uncapped emission tokens, where a protocol mints new coins every block and the float grows whether or not anyone votes.

The split is on the buy side. Some lending and exchange tokens now run a live fee-funded buyback or burn, so revenue removes coins every week. Aave has the revenue — under the “Aave Will Win” framework all Aave-branded revenue goes to the DAO — but its AAVE buyback is paused and nothing is burned, so today it looks more like a fixed-cap token with a small leak than a deflationary one. At **+0.14%** for the next 90 days, AAVE’s supply growth is low next to most emission-funded DeFi tokens; the open question is whether and when a buyer returns.

## What to watch in the next 90 days

The Aave community call in October 2026, where holders expect an update on the Aavenomics 3.0 buyback; a live buyback into a burn or into the reserve would add a real Buy #1 row. The next quarterly Safety Module allowance update, which decides how much of the roughly 37,875 AAVE reward backlog can be claimed. Any change to the 150 AAVE-a-day staking rate, which moves Sell #1 directly. Any new AAVE grant stream out of the Ecosystem Reserve, which would add to Sell #2. And the Aave V4 rollout, including the equities market that opened on Base on Sep 25 2026, which moves fees but not AAVE supply.

## Summary

AAVE is a fixed-supply token of **16M** with no mint and no burn, and the MrNasdog Pressure Framework reads its supply as roughly steady: **+0.13%** over the last 90 days and **+0.14%** projected for the next 90. All of that growth is the Aave DAO’s Ecosystem Reserve paying **14,889 AAVE** to stakers and **4,406 AAVE** to grants, led by a 75,000 AAVE four-year stream to Aave Labs. The key risk is that the buyback, paused since Apr 19 2026, stays off while the reserve keeps paying. The ceiling is the **570,145 AAVE** left in the reserve — the most that can ever reach the market beyond today’s float.

*MrNasdog Pressure Framework analysis of AAVE, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

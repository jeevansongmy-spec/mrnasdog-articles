---
title:         "ENA Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "Supply growing: ENA reads +7.94% over 90 days and +19.55% next. Ethena mints nothing, but its vesting calendar frees 801.6M ENA and 1,406.3M lands Oct 5 2026."
canonical_url: "https://mrnasdog.com/research/ena/inflation"
tags:          ["crypto", "ena", "ethena", "stablecoins"]
published:     true
---

Originally published at [ENA Inflation Analysis · September 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/ena/inflation).

# ENA Inflation Analysis · September 2026 · Supply growing · projected to keep growing

Ethena's ENA supply is growing and is projected to keep growing, much faster. Ethena mints no new ENA and burns none, yet the Pressure Framework reads **+7.94%** over the last 90 days and **+19.55%** over the next 90, against a monitor reading of **+8.67%**. All of it comes from one vesting calendar: **801.6M ENA** of sell pressure last quarter, **0** of buy pressure, and a single **1,406.3M ENA** investor unlock on **Oct 5 2026**. The 15,000M ENA total is a policy of the owner key, not a hard cap.

## The verdict, in one paragraph

Against a circulating base of **10,095.3M ENA**, the framework books **801.6M ENA** of sell pressure and **0** of buy pressure over the trailing 90 days, a net of **+7.94%**, and projects **+19.55%** for the next 90 days on the dated calendar. The inflation monitor reads **+8.67%** for the same window, a gap of **0.73 percentage points**. That is over the 0.5-point tolerance, so the overview carries a monitor-gap warning. The gap is fully explained: **0.69 points** is base convention, because the monitor divides by the 90-day-old supply of 9,291.6M ENA while the framework divides by today's, and **0.04 points**is the monitor's supply series moving 3.9M ENA more than the calendar. The label for ENA is a non-minting governance token with a heavy unlock calendar that is about to accelerate.

## Sell pressure: where new ENA comes from

It does not come from minting. Sell #1, protocol inflation, is **0**. The ENA contract on Ethereum read **15,000M ENA** in existence at both ends of the window, and that figure sits in ordinary contract storage that a mint or burn would change, so the flat reading is a real measurement. The contract does carry a mint function: the owner key may create up to 10% of supply once a year. Its last-use timestamp still equals the launch date in March 2024, so Ethena has never used it. Because it still works, this row is watched rather than closed, and ENA has no hard cap in the strict sense.

The whole supply story is Sell #2, vesting unlocks, at **801.6M ENA**. All ENA was created at launch and held back under a published schedule. The team (30%) and investors (25%) had a one-year, 25% cliff and then 36 monthly steps: **93.75M ENA** for the team and **78.1M ENA** for investors each month. The foundation releases **40.6M ENA** a month and the ecosystem allocation **54.7M ENA**, together **267.2M ENA** a month. Three rounds fell inside the window, in July, August and September 2026. The check is exact: the 4,904.7M ENA still counted as locked equals 18 team steps, 18 investor steps and 19 foundation-plus-ecosystem steps, to the last token.

The next 90 days are much heavier. On Aug 27 2026 the Ethena Foundation collapsed every remaining investor step into one release on **Oct 5 2026**: **1,406.3M ENA**, about 14% of today's float, arriving the same day as a team step. With the team, foundation and ecosystem steps in October, November and December, Sell #2 for the next 90 days is **1,973.4M ENA**. No release contract holds these coins on chain; they sit with custodians, and an unlock lifts a restriction on coins that already exist. So the framework counts the dated schedule, and the direction of error is high: a holder who receives coins does not have to sell them.

Sell #3, Foundation and unscheduled unlocks, is **0**: nothing was released outside the calendar. Sell #4, long-term locked or bankruptcy, is **0**, because ENA has no bankruptcy estate, trustee or court-ordered distribution.

## Buy pressure: where new ENA goes

Nowhere, this window. Buy #1, programmatic buyback, is **0**. Ethena holders approved a fee switch on **Sep 2 2026** by 17.8M ENA to none. It sends a rising share of protocol revenue, from 5% to 25%, into ENA purchases, but only once the USDe synthetic dollar reaches **$7.5B** in supply. USDe on Ethereum grew from about $4.5B to $4.9B across the window, still far short, so nothing was bought.

Buy #2, protocol fee burn, is **0**. ENA has no burn mechanism, and both places a burn could appear were read at both ends: the count in existence stayed at 15,000M ENA and the unspendable address held the same 2.6 ENA. Buy #3, Foundation buy, is **0**. In August the Foundation bought locked ENA privately from early investors who had been selling, but those coins were still locked, so no float was absorbed; the amount and price were not disclosed. Buy #4, new long-term lock, is **0**. Staked ENA rose from 1,056.8M to 1,255.0M, but staking can be undone, staked ENA is already counted as circulating, and the staking share price did not move.

## Foundation and overhang

The largest overhang is the calendar itself: **4,904.7M ENA** still locked, of which 1,406.3M leaves on Oct 5 2026 and the rest runs to April 2028. It is refreshed from the published schedule and the circulating count at every rebuild. The second item is StablecoinX, a Nasdaq-listed ENA treasury company holding about **3,029.0M ENA**, roughly 20% of all ENA. Those coins are already counted as circulating, so they add nothing to this reading, but their lockup ends on **Oct 5 2026**, and after that only Foundation consent stands between them and the market. The third is the investor ENA the Foundation bought in August, size undisclosed, which unlocks into Foundation hands on the same day. The fourth is an unlabelled wallet holding **839.3M ENA** that did not move a single token across the window.

The treasury wallets are read on chain at every rebuild, and the Foundation's holdings through its disclosures. The trigger rule applies to each: if any of these balances falls between refreshes by more than the calendar accounts for, that outflow enters Sell #3 at the next refresh.

## How ENA compares to other governance tokens with vesting calendars

ENA sits in the class of governance tokens that minted their full supply at launch and release it on a team-and-investor vest. That is a different shape from an uncapped proof-of-stake chain, which pays validators new coins every block, and from a halving-model chain like Bitcoin, which still mints but on a shrinking, known clock. Ethena's issuance reading is a flat zero; its float grows only because locked coins become tradable. The monitor and the framework agree on that flow; they differ only on what to divide it by.

Against other vesting tokens, two things stand out. First, the size: 267.2M ENA a month is about 2.6% of the float, and the Oct 5 2026 release alone is about 14%. Most vesting calendars smooth their final years; Ethena has done the opposite and pulled 17 months of investor steps into one day. Second, the demand side is still a promise. Exchange tokens with running buybacks can read negative, because revenue removes coins every quarter. Ethena has voted in the same kind of mechanism, but it cannot spend a dollar until USDe grows about 50%, and the vote did not confirm that bought ENA will be burned rather than held.

## What to watch in the next 90 days

First, **Oct 5 2026**: 1,406.3M ENA of investor tokens and a 93.75M team step unlock together, and the StablecoinX lockup ends the same day. Second, the monthly steps on **Oct 2**, **Nov 2** and **Dec 2 2026** (foundation and ecosystem, 95.3M ENA each) and on **Nov 5** and **Dec 5 2026**(team, 93.75M ENA each). Third, USDe supply: the buyback switches on at $7.5B, the one event that could put ENA's buy side above zero. Fourth, any Foundation disclosure of how much investor ENA it bought, and whether it will hold, lock or burn it. Fifth, the owner key's yearly mint, unused since March 2024; any use would show at once in the count of ENA in existence.

## Summary

The MrNasdog Pressure Framework reads Ethena's ENA at **+7.94%** over the trailing 90 days and **+19.55%** projected forward: supply growing, projected to keep growing. The mechanism is unlock, not minting: 801.6M ENA came off the vesting calendar last quarter, nothing was burned or bought back, and 1,406.3M ENA of investor tokens release in a single day on Oct 5 2026. The key risk is that the forward reading is mechanical and front-loaded, while the buyback meant to offset it cannot start until USDe reaches $7.5B. The ceiling is 15,000M ENA, held by an owner key that has never minted but still can.

MrNasdog Pressure Framework analysis of ENA, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 23 2026.

---
title:         "CRO Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "CRO supply grows 7.44% over 90 days as the re-created 70B reserve unlocks 3.50B tokens. Read the Pressure Framework ledger, burn checks and pending burn vote."
canonical_url: "https://mrnasdog.com/research/cro/inflation"
tags:          ["crypto", "cro", "cronos", "tokenomics"]
published:     true
---

Originally published at [CRO Inflation Analysis · September 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/cro/inflation).

# CRO Inflation Analysis · September 2026 · Supply growing · projected to keep growing

CRO supply is growing and is projected to keep growing: the Pressure Framework reads Cronos at **+7.44%** over the last 90 days and **+7.36%** over the next 90, against a monitor reading of **+8.14%**. Almost all of it comes from one mechanism — the 70,000M CRO Strategic Reserve, re-created in 2025 after the 2021 burn, which unlocked **3,500.0M CRO** in three monthly slices, on top of **200.0M CRO** of staking emission. Buy pressure was just **0.0045M CRO**, and the only ceiling is a 100,000M cap that is still far above today's supply.

## The verdict, in one paragraph

Against a circulating base of **49,738.0M CRO**, the framework books **3,700.0M CRO** of sell pressure and **0.0045M CRO** of buy pressure over the trailing 90 days, a net of **+7.44%**, and projects **+7.36%** for the next 90 days on the same unlock calendar. The inflation monitor reads **+8.14%** for the same window, a gap of **0.70 percentage points**, which is over the framework's 0.5-point tolerance and so ships with a monitor-gap warning on the overview. The gap is fully explained. About **0.60 points** is base convention: the monitor divides the same increase by the smaller float at the start of the window. About **0.10 points** is the monitor's market-based supply estimate running slightly off the chain's own count. CRO is a **reserve-unlock chain**: its float grows every month because a governance reserve keeps releasing coins, not because of runaway minting.

## Sell pressure: where new CRO comes from

Protocol inflation is **200.0M CRO**. Cronos POS mints new CRO every block to pay validators and stakers, and 15% of each block's reward goes to the community pool. A May 2026 upgrade added a decay of 6.8% a month on top of the mint rate, so the rate fell from **0.92%** a year at the start of the window to **0.75%** at the end. The count of CRO in existence rose from **98,738.0M** to **98,938.0M**, which the chain's own mint settings confirm to within a few thousand CRO. With the decay continuing, the next 90 days should mint about **163.1M CRO**.

Vesting unlocks are the whole story, at **3,500.0M CRO**. In 2021 Crypto.com burned 70,000M CRO. In March 2025 a Cronos governance vote re-created exactly that amount inside a single reserve account, set to unlock **1,166.7M CRO** about every 30 days over 60 months, ending in Mar 2030. Three slices unlocked in this window, on **Jul 17**, **Aug 17** and **Sep 16 2026**, and the locked balance fell from **52,500M** to **49,000M CRO**. The coins that actually left the account add up to the same 3,500.0M. Each slice counts as circulating the moment it unlocks, so the wallets that later receive it do not count a second time.

Foundation and unscheduled unlocks are **0**. Every Cronos-controlled wallet that holds unlocked reserve coins already sits inside the circulating count, so a later transfer or sale from one of them moves no new CRO into the float. Long-term locked or bankruptcy supply is also **0**: CRO has no bankruptcy estate, trustee or court-ordered distribution, and the one long lock is the reserve itself.

## Buy pressure: where new CRO goes

Programmatic buyback is **0**. No buyback ran in the window. A signalling vote closing on **Oct 3 2026** would commit all revenue from the Ult trading app and Cronos Launch to monthly open-market buy-and-burns of CRO, with the Strategic Reserve funding staking rewards instead. The burn contract is still being built and no revenue figure is published, so the row stays at zero until coins are actually bought and burned.

Protocol fee burn is **0.0045M CRO**. Cronos burns CRO by sending it to a dead address that never counts as circulating, and it can also cut total supply directly, so the framework read both at both ends of the window. The dead address grew by only about 4,500 CRO, and total supply only rose. The community-pool burn that removed 50M CRO four times last fired in Mar 2025. A fifth, much larger burn of **228M CRO** is in a governance vote that closes on **Oct 3 2026**; it is not counted until it passes. The Cronos EVM chain collects its gas fees rather than burning them.

Foundation buy is **0**. Cronos Labs bought no CRO on the market, and the one large planned buyer left: Trump Media, Crypto.com and Yorkville ended their planned CRO treasury company on **Aug 7 2026**. New long-term lock is **0** as well. Staked CRO rose from **14,284.7M** to **14,482.1M**, and new 1-, 2- and 4-year staking locks went live, but staked and lock-staked CRO both still count as circulating, so neither takes supply off the market.

## Foundation and overhang

The biggest overhang on CRO is the reserve account itself: **49,000M CRO** still locked, on a fixed schedule of 1,166.7M a month until Mar 2030. The account also held **1,166.7M CRO** that had unlocked on Sep 16 2026 but had not yet moved out. Unlocked slices are swept to Cronos-controlled wallets: the main one held **11,450M CRO** at the end of the window, up from 8,450M, after passing 500M onward on Sep 13 2026; an older one held **5,833M CRO** and did not move; a third held the **500M** it had just received. The community pool held **232.3M CRO**, the fuel for the pending burn, and a staking-bonus pot held **48.0M**.

Outside the team, Trump Media holds **684.4M CRO**, of which about **68.4M**became sellable from Aug 26 2026. None has a published sale schedule; all are refreshed from the chain at every rebuild. If the reserve account's locked balance falls faster than its schedule, or any of these wallets falls between refreshes in a way that moves coins from outside the circulating count into it, that outflow enters the Foundation row at the next refresh.

## How CRO compares to other capped staking chains

CRO sits in an unusual spot. On paper it has a hard 100,000M cap, which puts it next to capped coins like Bitcoin rather than uncapped Cosmos staking chains that mint 5% to 10% a year with no limit. Its mint is also small and shrinking: 0.75% a year and falling 6.8% a month, which is gentler than a typical Cosmos chain and on track to fade to almost nothing within a few years.

But the cap is not what drives CRO's number. A halving-model chain like Bitcoin adds a fraction of a percent a quarter and has no locked reserve waiting to be released. CRO adds more than 7% a quarter because of a governance decision: a burned supply was brought back to life and handed to a reserve that releases it on a clock. In shape, CRO looks more like a young token working through a monthly vest than a mature capped coin: easy to predict, hard to avoid.

Exchange tokens with regular buybacks and burns can go net negative because the burn scales with usage. Cronos has that mechanism in pieces — a community-pool burn and a proposed revenue buy-and-burn — but neither fired in this window. To offset the reserve alone, Cronos would need to burn about **3,500M CRO** a quarter, more than fifteen times the pending 228M community burn.

## What to watch in the next 90 days

First, the reserve unlocks on **Oct 17**, **Nov 16** and **Dec 16 2026**, each worth **1,166.7M CRO** — they alone keep the next reading near +7%. Second, the two governance votes that close on **Oct 3 2026**: the 228M CRO community-pool burn, which would be the largest CRO burn since 2021, and the revenue buy-and-burn plan, which only matters once real revenue flows. Third, the main Cronos-controlled wallet at 11,450M CRO, whose outbound transfers show where unlocked coins go. Fourth, the mint rate, which should drop from 0.75% toward about 0.61% a year by Dec 22 2026 if the decay setting is left alone. Fifth, Trump Media's 684.4M CRO, part of which is now sellable.

## Summary

The MrNasdog Pressure Framework reads CRO at **+7.44%** over the trailing 90 days and **+7.36%** projected forward: supply growing, projected to keep growing. The driver is not staking emission, which is small and decaying, but the 70,000M CRO Strategic Reserve re-created in 2025, which releases 1,166.7M CRO every month and still holds **49,000M CRO** locked. The key risk is that this release is fixed until Mar 2030 and no burn or buyback of meaningful size has fired against it. The ceiling is a 100,000M cap, but with 98,938.0M CRO already in existence the cap limits new minting, not the unlocks.

MrNasdog Pressure Framework analysis of CRO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 23 2026.

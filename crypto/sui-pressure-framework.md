---
title: "SUI Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description: "SUI supply is growing: 67.34M SUI unlocked in 90 days and only 0.14M left the float, as nothing is burned. Framework reads +1.64% net, +1.54% next 90 days."
canonical_url: "https://mrnasdog.com/research/sui/inflation"
tags: ["crypto", "sui", "layer1", "vesting"]
published: true
---

> Originally published at **[mrnasdog.com/research/sui/inflation](https://mrnasdog.com/research/sui/inflation)** by MrNasdog.

# SUI Inflation Analysis · September 2026 · Supply growing, projected to keep growing

SUI, the native coin of the Sui layer-1, is still unlocking: all **10B SUI** were created at launch, but only **4.10B** circulate, and the rest reaches the market on a published monthly schedule plus a staking subsidy paid from a fund set aside at launch. Over the last 90 days that added **67.34M SUI** — **26.36M** of subsidy and **40.98M** of monthly releases — while only **0.14M SUI** left the float for good, so the MrNasdog Pressure Framework reads SUI at **+1.64% net** against a supply-monitor reading of **+1.33%**, a gap of **0.31 percentage points**. Nothing on Sui is burned, and the Sui Foundation buyback hands its coins back out, so SUI supply growth is capped only by the **10B** ceiling and the shrinking pace of the schedule.

## The verdict, in one paragraph

For the 90-day window ending **Sep 14 2026**, the Pressure Framework reads **SUI at +1.64% net**: the sell side added **67.34M SUI** and the buy side removed **0.14M**. The independent supply monitor reads the realised 90-day change at **+1.33%**. The gap is **0.31 percentage points**, inside the framework's half-point tolerance, so SUI ships with **no data-conflict flag**; the framework sits higher because the monitor's latest reading sits about **13.6M SUI** below the published circulating figure, which already includes the Sep 1 2026 release. The forward column reads **+1.54%**, a little softer, because the Sui staking subsidy is cut by another **10%** on **Oct 14 2026** and the monthly releases keep stepping down. The label for SUI is **structurally inflationary on an unlocking float**: a capped layer-1 whose circulating supply rises every month and has no burn to push against it.

## Sell pressure: where new SUI comes from

Sell #1, protocol inflation, is **26.36M SUI**. Sui mints nothing new — the SUI supply object was destroyed at genesis — but it pays stakers a subsidy out of a fund created at launch, and every SUI paid out joins the circulating float. The fund paid **313,811 SUI** per daily epoch until **Jul 16 2026**, when a scheduled 10% step cut it to **282,430 SUI**. Summed epoch by epoch across the window, that is **26,360,090 SUI**, and the fund's own balance fell by exactly the same amount, from **263.60M** to **237.24M SUI**. The forward figure is **23.72M**, built from the post-cut rate plus the next cut on **Oct 14 2026**, not from the blended trailing average.

Sell #2, vesting unlocks, is **22.77M SUI**: the early-contributor allocation releases on the first of every month, and the **Jul 1**, **Aug 1** and **Sep 1 2026** releases came to **7.65M**, **7.65M** and **7.46M SUI**. SUI investor vesting finished in May 2026, which is why the monthly Sui release fell from about 52M to about 24M between May and June. Sell #3, foundation and scheduled treasury releases, is **18.21M SUI**: the Sui Foundation community reserve releases **4.00M** and the Mysten Labs treasury **2.07M SUI** on each of those same dates. The locked SUI sits with outside custodians under no published wallet labels, so there is no public escrow contract to read at both ends; the published Sui schedule is the measure, and it matches the dated bucket reports for Aug 1 and Sep 1 to the coin. Sell #4, long-term locked or bankruptcy supply, is **zero**: no estate distributes SUI, and the listed company that bought SUI from the Sui Foundation in 2025 accepted transfer limits that run past the next 90 days.

## Buy pressure: where new SUI goes

Buy #1, the programmatic buyback, is **zero**, and that is a classification, not an oversight. The Sui Foundation buys SUI on the open market every day with yield from Sui stablecoin reserves — **676.4K SUI** for about **$492.7K** between **Jun 22** and **Sep 13 2026**. But the Sui Foundation distributes those coins to DeFi apps, validators and ecosystem partners and states that total supply is unchanged by the buyback. SUI bought from the market and handed back to the market is a loop, not a sink.

Buy #2 is **0.14M SUI**, and it is not a burn. Sui destroys no fees: computation fees go to validators and stakers, and storage fees go to the Sui storage fund. When stored data is deleted, users get **99%** of the storage fee back, and the remaining share moves into a non-refundable balance that the storage fund contract never pays out. That balance rose **138,716 SUI** across the window, read from chain state at both ends; the refundable **29,588 SUI** that users can still reclaim is left out. The total SUI supply read **10B** at both ends, as it must on a chain with no burn. Buy #3, foundation buying, is **zero** beyond the redistributing buyback, and Buy #4, new long-term locks, is **zero**: nothing new was locked with a stated size, and staked SUI stays inside the circulating count.

## Foundation and overhang

The overhang is the defining fact of SUI supply. **5.90B SUI** — **59%** of the cap — is not yet circulating. Of that, **686.26M SUI** is on the published Sui schedule through May 2030, and **5.22B SUI** has no release date at all before 2030; both are re-checked against the Sui schedule on every refresh. The staking subsidy fund at **237.24M SUI** is on-chain and read directly each refresh, and it can only drain at the protocol's fixed per-epoch rate. The buyback holds no standing balance, because bought SUI is redistributed. If any of these balances falls faster than its schedule between refreshes, the outflow enters Sell #3 at the next refresh.

## How SUI compares to other smart-contract layer-1 chains

Most proof-of-stake layer-1 chains grow supply by minting: an inflation rate pays validators in new coins, and a fee burn may offset part of it. SUI grows differently. Nothing is minted after genesis, so the SUI ceiling is hard at **10B**, and supply growth comes from the release of coins that already exist — a finite subsidy fund and a vesting calendar. That makes SUI inflation front-loaded and self-ending in a way an uncapped emission curve is not: the subsidy shrinks **10%** every 90 epochs and the monthly Sui release has already fallen from about 52M to about 22M SUI this year. Against a chain whose issuance runs forever, SUI dilution has a visible end; against a fully unlocked chain with no reserve, SUI still carries a far larger unreleased float.

The second contrast is the absence of any burn. Chains that destroy a share of fees can turn deflationary when activity is high; Sui routes computation fees to stakers and storage fees into the storage fund, so Sui activity never cancels issuance. The Sui fee base is also small next to the release: Sui users paid about **211.6K SUI** of gas over the window, roughly **$153K**, while the subsidy alone paid out **26.36M SUI** — about 125 times more. Annualised, Sui gas fees come to about two hundredths of a percent of a **$2.97B** market capitalisation, the quiet end of the chains the framework tracks. The buyback is the Sui answer to that gap, but because the Sui Foundation redistributes what it buys, SUI gets flow support without float reduction.

## What to watch in the next 90 days

First, the **Oct 1 2026** release of about **13.26M SUI**, followed by about **13.15M** on **Nov 1** and **12.97M** on **Dec 1 2026** — any change to the published Sui schedule would move the largest rows on the page. Second, the scheduled Sui staking subsidy cut on **Oct 14 2026**, from **282,430** to **254,187 SUI** per epoch, already built into the forward **23.72M**. Third, the Sui Foundation buyback: if bought SUI starts to be held or burned instead of redistributed, it would open a real Buy #1 row, at a current pace near **8,900 SUI** a day. Fourth, the **5.22B SUI** with no release date: any announcement that schedules part of it would add a new Sell #3 line.

## Summary

The MrNasdog Pressure Framework reads SUI at **+1.64% net** over the trailing 90 days and **+1.54%** over the next 90. The structural mechanism is a capped layer-1 still releasing coins created at launch — a staking subsidy of **26.36M SUI** and monthly releases of **40.98M** — against a removal side of just **0.14M SUI** of non-refundable storage fees, because nothing on Sui is burned and the buyback redistributes. The key risk is the **5.90B SUI** still locked, **5.22B** of it with no release date. The ceiling is the **10B SUI** cap: supply cannot pass it, and the pace of SUI dilution falls with every subsidy cut and every smaller monthly release.

*MrNasdog Pressure Framework analysis of SUI, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 14 2026.*

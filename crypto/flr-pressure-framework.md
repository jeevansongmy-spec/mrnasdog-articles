---
title: "FLR Inflation Analysis · July 2026 · Supply still growing, but cooling"
description: "A MrNasdog Pressure Framework read of Flare (FLR): ~636M / 90D of protocol inflation at the new 3% rate vs a ~75M fee burn. Framework +0.65% net going forward; monitor +1.20% realized."
canonical_url: "https://mrnasdog.com/research/flr/inflation"
tags: ["crypto", "flr", "flare", "oracles"]
published: true
---

> Originally published at **[mrnasdog.com/research/flr/inflation](https://mrnasdog.com/research/flr/inflation)** by MrNasdog.

Flare mints about **636M FLR** over the next 90 days at a newly reduced **3%** yearly rate, while a raised base network fee now burns roughly **75M** back out. The mint still leads, so the Pressure Framework reads about **+0.65%** net going forward — down from the **+0.77%** the last 90 days ran at. Our supply monitor reads **+1.20%** realized for that window, a small and expected gap.

## The verdict, in one paragraph

For the 90-day window ending July 14 2026, the MrNasdog Pressure Framework reads **FLR at about +0.65% net** on the forward view, driven by capped protocol inflation that still out-issues the new fee burn. Over the last 90 days the framework reads **+0.77%**, versus our supply monitor's **+1.20%** realized change for the same window — a gap of about **0.43 percentage points**, inside the tolerance band, so no data-conflict flag is raised. The remaining difference is post-distribution wrapped and reward FLR still landing in the circulating float, not fresh issuance. The one-line read: **supply growing, projected to keep growing**, but at a clearly cooling pace after a late-April reform cut the mint and switched on a burn.

## Sell pressure: where new FLR comes from

Sell #1 — protocol inflation — is effectively the whole sell side, at about **636M FLR** over the next 90 days. Flare issues new FLR on a capped yearly schedule and pays it to FLR stakers, price-feed delegators and data agents. The FIP.16 tokenomics reform approved on **April 24 2026** cut the annual rate from **5% to 3%** and the yearly issuance cap from 5B to 3B FLR, calculated on the roughly 86B FLR already distributed — gross issuance of about **2.58B FLR** a year. Because the last 90 days straddled the old 5% rate for its first days before the cut took hold, that window minted closer to **683M**; the forward window sits fully at the lower 3% rate.

Sell #2 — vesting unlocks — is now **zero**. For three years the FlareDrop distribution had been moving previously-locked FLR into circulation each month, roughly 670M FLR at a time; it finished on schedule on **January 30 2026**, so nothing lands from vesting in this window. Sell #3 — foundation and unscheduled unlocks — is also zero: there is no dated discretionary release pending, and the remaining unissued supply is governed by the capped inflation schedule rather than a cliff. Sell #4 — long-term locked or bankruptcy — is zero, since no estate or court distribution applies to FLR.

## Buy pressure: where new FLR goes

Buy #2 — the protocol fee burn — is the active offset, at about **75M FLR** over 90 days. FIP.16 raised the base network fee about **20×**, from 25 to 500 gwei, and that base fee is burned as coins are spent, so at current activity roughly **300M FLR** leaves supply each year. The fee-burn hard fork executed in late June 2026, so the last-90-day window carried almost none of it — the offset is new and now live. Buy #1 — a programmatic buyback — is carried at zero: FIP.16 created FIRE, the Flare Income Reinvestment Entity, to capture network revenue and captured block value, but it recycles that into the ecosystem incentive pool rather than buying back and destroying FLR, so it removes nothing from supply. Buy #3 — foundation buy — and Buy #4 — new long-term lock — are both zero, with nothing announced in the window.

## Foundation and overhang

FLR's overhang picture just got simpler. The multi-year FlareDrop that had been releasing locked FLR every month is finished, so the largest scheduled source of new float is gone. The remaining team-controlled overhang is the **Flare Foundation and Flare VC Fund** holdings — a non-voting allocation on the order of **a fifth of supply** — with no published release schedule; the rest of the undistributed reserve enters only through the capped inflation schedule, which is largely paid to participants who stake or delegate rather than to a stockpile waiting to sell. The framework books no discretionary release beyond that inflation and re-checks the schedule, the fee burn and any FIRE activity on a roughly bi-weekly walk; if a Foundation balance falls faster than the schedule, the outflow enters Sell #3 at the next refresh.

## How FLR compares to other uncapped proof-of-stake chains

FLR belongs to the class of **uncapped, capped-inflation proof-of-stake L1s** — coins with no hard supply ceiling but a fixed annual issuance cap that shrinks the effective rate over time. Unlike a halving-model coin with a fixed maximum, FLR has no ceiling; unlike an uncapped continuous-emission chain with no brake, its yearly mint is bounded and now falling, and it pairs the mint with a fee burn that scales with network use. The result sits between the two: net inflation is positive but low, and trending down as the 3% rate cut and the fee burn both take hold.

The contrast worth drawing is with chains that burn aggressively enough to go net-deflationary. FLR's fee burn is real and newly meaningful — on the order of a tenth of the gross mint at current activity — so it slows dilution rather than reversing it. For an inflation lens specifically, that means FLR reads as mildly inflationary with a clear cooling trend: the smaller mint is the dominant force, and the burn is a growing brake that could matter more if network activity rises.

## What to watch in the next 90 days

Watch the fee burn as activity moves — the ~75M-per-90-day pace assumes current throughput, so a busier network burns more and a quiet one burns less. Watch FIRE, the new revenue entity: if it ever routes captured revenue or MEV into an on-chain buyback-and-burn rather than the incentive pool, the first published amount would move Buy #1 off zero. Note that the mint is now at the lower 3% rate for the whole forward window, so gross issuance steps down from last quarter. And expect the framework to keep tracking close to our supply monitor now that the FlareDrop distribution has ended and the biggest one-off float source is gone.

## Summary

FLR is the native coin of an uncapped, capped-inflation data-and-oracle chain whose supply grows on a bounded yearly schedule. The FIP.16 reform cut the mint from 5% to 3% and switched on a base-fee burn: Flare now issues about 636M FLR over 90 days while the raised fee burns roughly 75M back out, leaving the framework at about +0.65% net going forward, down from +0.77% over the last 90 days. Our supply monitor reads +1.20% realized, a small and expected gap from post-distribution float still settling. With the three-year FlareDrop finished, FLR stays mildly inflationary but on a clearly cooling path — the smaller mint leading, the fee burn slowing it.

---

*MrNasdog Pressure Framework analysis of Flare (FLR), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 14 2026.*

---
title: "XMR Inflation Analysis · July 2026 · A fixed tail reward and almost no new supply"
description: "A MrNasdog Pressure Framework read of Monero (XMR): a fixed 0.6-per-block tail emission (~0.039M / 90D, +0.21%) with no buyback or burn. Framework +0.2% net; monitor +1.71%, the gap a hidden-ledger estimate artifact."
canonical_url: "https://mrnasdog.com/research/xmr/inflation"
tags: ["crypto", "xmr", "monero", "privacy-coins"]
published: true
---

> Originally published at **[mrnasdog.com/research/xmr/inflation](https://mrnasdog.com/research/xmr/inflation)** by MrNasdog.

**Monero mints a fixed 0.6 XMR per block, forever — about 0.039M XMR over 90 days, or roughly +0.21%. There is no buyback, no burn and nothing was ever premined, so the MrNasdog Pressure Framework reads about +0.2% net. Our supply monitor reads +1.71% — a gap that comes from Monero's hidden ledger, where circulating supply is estimated and the prior baseline was later re-based.**

## The verdict, in one paragraph

For the 90-day window ending **July 1 2026**, the MrNasdog Pressure Framework reads **XMR at about +0.2% net**, almost flat. The entire flow is one number: a fixed tail reward of **0.6 XMR per block** that mints roughly **0.039M XMR** a quarter. There is no vesting, no foundation reserve, no buyback and no burn, so nothing pushes the other way. Our supply monitor reads the realized last-90-day change at **+1.71%** — a gap of about **1.5 percentage points** that ships a **monitor-gap flag**. The gap is a measurement artifact, not new coins: at 0.6 XMR per block the protocol can physically mint only about **0.039M XMR** in 90 days, yet the monitor booked roughly **0.315M** — about eight times more than the reward allows. Monero hides its ledger, so circulating supply is estimated, and the 90-day-ago estimate was low and later re-based upward. The fixed mining reward is kept as primary, and XMR is best read as **near-flat by design**, with a small, permanent, and slowly-falling inflation rate.

## Sell pressure: where new XMR comes from

Sell #1 — protocol inflation — is the whole story, and it is tiny. Monero reached **tail emission** at the end of May 2022: after the original mining schedule ran down, the block reward settled at a fixed **0.6 XMR** per block and stays there permanently. With a block roughly every two minutes, that is about **720 blocks a day**, or **~0.039M XMR** minted over 90 days — about **+0.21%** against the ~18.8M coins already in circulation. Because the reward is a fixed amount rather than a percentage, the same ~0.039M is minted every quarter forever, so the percentage rate slowly falls as the supply grows; annualized it is about **0.84%** a year and easing.

Sell #2 — vesting unlocks — is **zero**. Monero launched in April 2014 as a fair launch: no premine, no instamine, no founder allocation and no slice of the block reward routed to a treasury. Nothing was ever locked, so no cliff can ever reach the market. Sell #3 — Foundation and unscheduled unlocks — is also zero, because there is no foundation reserve of XMR held from launch; the entire supply is mined into the open market by whoever runs the hardware. Sell #4 — long-term locked or bankruptcy — is zero, with no estate or court distribution applying to XMR.

## Buy pressure: where XMR goes

There is none to count. Buy #1 — programmatic buyback — is **zero**: Monero has no protocol revenue and no mechanism that buys XMR back from the market. Buy #2 — protocol fee burn — is also zero, because transaction fees are paid to miners, not destroyed, so no coins leave the supply. Buy #3 — foundation buy — and Buy #4 — new long-term lock — are both zero, with no treasury to fund open-market buying and no new escrow announced in the window. Monero is a pure-issuance coin: a small, fixed mint, and no offset whatsoever.

## Foundation and overhang

XMR has the cleanest overhang profile in crypto: there isn't one. There is no team allocation, no investor lock-up, no foundation multisig holding a launch reserve, and no buyback wallet quietly accumulating. Development is funded by a voluntary community crowdfunding system — donations, not a stockpile of XMR that the project holds and sells — so there is no team-controlled supply that could ever be released into the market. That is the direct result of the 2014 fair launch, and it is the reason the framework books exactly one sell row and three structural zeros. There is simply no discretionary supply to monitor; if any identified overhang ever appeared, its outflow would enter Sell #3 at the next refresh.

## How XMR compares to other proof-of-work coins

XMR belongs to the class of **proof-of-work coins with a fixed perpetual tail emission** — but unlike Bitcoin, it never reaches a hard cap. Bitcoin halves toward a fixed 21M ceiling and zero issuance; Monero instead chose a permanent **0.6 XMR per block** to keep paying miners after the main emission ended, deliberately trading a hard cap for a small, never-zero security budget. The result is the opposite trade-off: Bitcoin's inflation trends to zero but its long-run miner pay relies entirely on fees, while Monero's inflation never reaches zero but its miners always have a base reward.

For an inflation lens, that makes XMR one of the lowest-issuance coins outside the hard-capped set. The mint is fixed in coins, so the percentage rate falls every year as supply grows — currently under 1% a year and easing. There is no burn to make it deflationary and no unlock schedule to make it spiky; it is just a small, steady, predictable drip that gets relatively smaller over time. Where a privacy chain like Zcash also runs continuous issuance, Monero's difference is that every coin goes to miners with no founders' reward, so there is no separate emission stream to track.

## What to watch in the next 90 days

There is very little to watch, which is the point. The tail reward is a protocol constant, so barring a hard fork that changes it — none is proposed — the ~0.039M-per-90-days mint is locked in. The FCMP++ upgrade landing around mid-2026 and the later Seraphis and Jamtis work are privacy and functionality changes; none of them alter issuance. The one thing to keep an eye on is our supply monitor: because Monero hides its ledger, circulating supply is an estimate, and trackers disagree by hundreds of thousands of coins, which is exactly what produced this window's +1.71% reading against a true mint of about +0.21%. Expect the framework to keep reading near flat while the monitor occasionally jumps on estimate revisions; those jumps are measurement, not issuance.

## Summary

XMR is a fair-launch proof-of-work privacy coin with a fixed tail reward of 0.6 XMR per block. That mints about 0.039M XMR over 90 days, roughly +0.21%, with no vesting, no foundation reserve, no buyback and no burn — so the framework reads about +0.2% net, almost flat. Our supply monitor reads +1.71% realized, but that gap is a measurement artifact: the protocol can only mint about 0.039M XMR in 90 days, and Monero's hidden ledger forces circulating supply to be estimated, with a low prior baseline later re-based upward. The fixed mining reward is kept as primary. XMR stays near-flat, with a small, permanent inflation rate that slowly falls as the supply grows.

---

*MrNasdog Pressure Framework analysis of Monero (XMR), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 1, 2026.*

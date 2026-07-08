---
title: "TAO Inflation Analysis · July 2026 · Supply growing, projected to keep growing"
description: "A MrNasdog Pressure Framework read of Bittensor (TAO): ~324K TAO/90d of halving-schedule emission vs a ~56K registration recycle. Framework +2.79% net; monitor −0.27%, against a 21M hard cap."
canonical_url: "https://mrnasdog.com/research/tao/inflation"
tags: ["crypto", "tao", "bittensor", "ai"]
published: true
---

> Originally published at **[mrnasdog.com/research/tao/inflation](https://mrnasdog.com/research/tao/inflation)** by MrNasdog.

Bittensor mints new TAO on every block. Since the December 2025 halving the reward is 0.5 TAO per block — about **324K TAO** over 90 days — and registration recycling only claws back about **56K**, so roughly **268K** net new TAO were issued on-chain. Against a 9.60M circulating float that is about **+2.79%** net. Our supply monitor reads the tradable float flat at **−0.27%**, a gap of about **3 percentage points** that ships a ⚠ monitor-gap chip, because the new supply is being classed as staked and non-circulating even though on-chain issuance clearly rose.

## The verdict, in one paragraph

For the 90-day window ending Jul 8 2026, the MrNasdog Pressure Framework reads **TAO at +2.79% net**, driven entirely by protocol block emission on the Bittensor halving schedule, offset only lightly by registration recycling. Our supply monitor reads the realized last-90-day change in the circulating float at **−0.27%** — essentially flat — so the gap is about **3.06 percentage points**, well outside tolerance, and a **⚠ monitor-gap chip** ships. The divergence is not an error on either side: on-chain issued TAO rose to **11.10M** (52.85% of the 21M cap) from about **10.83M** in early April, so roughly 268K new TAO were minted, but the aggregator classifies that new supply as staked and non-circulating, holding its float count flat. TAO is **structurally inflationary on the halving schedule**, at a low-single-digit 90-day pace, under a hard 21M ceiling.

## Sell pressure: where new TAO comes from

The entire sell side sits in Sell #1 — protocol inflation — at about **324K TAO** over 90 days. Bittensor pays a block reward to subnet miners, validators and stakers on every block. The first halving on **Dec 12 2025** cut that reward from 1.0 to **0.5 TAO per block**; at roughly 7,200 blocks a day that is about **3,600 TAO a day**, or 324K over the window. Like Bitcoin, the rate is not a governance decision — it is fixed by the halving schedule and will not change again until 15.75M TAO have been issued, several years out at the current pace. This is genuine new supply entering the hands of participants who sell TAO to cover compute and operating costs, which is why the framework books it as the dominant sell force.

The other three sell rows are zero, and each for a clean structural reason. Sell #2 — vesting unlocks — is **zero** because TAO was a fair launch: no premine, no ICO, no investor or team allocation, and therefore no vesting schedule cliffing coins into the market. Sell #3 — Foundation and unscheduled unlocks — is **zero** in the window: the Opentensor Foundation holds TAO from early mining and donations but publishes no release schedule and was not observed distributing. Sell #4 — long-term locked or bankruptcy — is **zero**, with no estate or court-ordered distribution tied to TAO.

## Buy pressure: where new TAO goes

Bittensor has one supply-removing mechanism, and it is modest. Buy #2 — protocol fee burn — is about **56K TAO** over 90 days: the TAO spent on subnet and neuron registrations, plus deregistrations and cold-key swaps, is recycled back into the un-issued supply rather than staying in circulation. That recycle is what separates gross emission from net issuance — 324K minted less roughly 268K net new TAO leaves about 56K recycled — and it is the reason the halving timeline keeps stretching. But it offsets only about a sixth of emission, so it does not turn supply deflationary.

The remaining buy rows are zero. Buy #1 — programmatic buyback — is **zero**: there is no protocol or foundation mechanism that buys TAO back on the open market. Buy #3 — Foundation buy — is **zero**: the Opentensor Foundation does not purchase TAO. Buy #4 — new long-term lock — is **zero**: no new multi-year escrow was announced, and while staking locks TAO, it is liquid and withdrawable, so the framework does not count it as a supply-removing lock. With only the small registration recycle opposing a 324K emission, the net read stays firmly positive.

## Foundation and overhang

The overhang on TAO is not a dated cliff but a classification bucket. The roughly **1.5M TAO** gap between the 11.10M issued on-chain and the 9.60M counted as circulating is made up of staked TAO and subnet reserves that the aggregator treats as non-circulating. On top of that sits the Opentensor Foundation's own holdings from early mining and donations, which have no published release schedule. Neither is a scheduled release, so both stay at value zero in Sell #3 and are tracked as overhang rather than booked as flow. The framework re-checks these on a roughly bi-weekly walk; if the Foundation's balance or the non-circulating stake pool drains into the tradable float faster than emission alone would explain, that extra outflow enters Sell #3 at the next refresh.

## How TAO compares to other hard-capped halving chains

TAO belongs to the small class of **hard-capped, halving-schedule assets** — the Bitcoin model — where supply is set by a block reward that halves on a fixed rule and tops out at a permanent ceiling, here 21M. Unlike an uncapped proof-of-stake chain that can mint indefinitely, TAO's issuance is bounded and decelerating: each halving cuts the block reward in half, so today's 3,600 TAO a day becomes 1,800 at the next halving near 15.75M issued. That makes its long-run inflation path predictable in exactly the way the framework rewards.

The difference from Bitcoin is Bittensor's recycle and its supply classification. Bitcoin has no fee recycle that returns coins to un-issued supply; TAO does, through registration burns, which slows the march toward each halving. And where Bitcoin's circulating count tracks mined supply almost exactly, TAO's freely-tradable float diverges from issued supply because so much TAO is staked into subnets — the reason our monitor reads the float flat while on-chain issuance rose. Against an exchange token that buys back and burns its way to net-deflation, TAO is the opposite structure: no buyback, a small recycle, and a block reward that keeps supply growing until the cap.

## What to watch in the next 90 days

Watch the on-chain issued-supply figure climb past **11.10M** — it is the single number that confirms the roughly 3,600 TAO-a-day mint is still running and that the framework's inflationary read, not the flat float count, matches reality. Watch the registration recycle rate: a surge in new subnet and neuron registrations would lift the recycle above 56K and cool the net read, while quiet registration activity lets emission run closer to gross. Watch the progress toward the second halving at **15.75M** issued, still several years out but the eventual step that halves the sell force again. And watch whether the aggregator reclassifies staked TAO as circulating, which would close the monitor gap by lifting the float count toward issued supply.

## Summary

TAO is a fair-launch, hard-capped halving coin that still mints on every block: about 324K new TAO over 90 days at 0.5 TAO per block since the December 2025 halving, against a 21M ceiling. Registration recycling claws back only about 56K, so roughly 268K net new TAO were issued and the framework reads about +2.79% net — supply growing, projected to keep growing. Our supply monitor reads the tradable float flat at −0.27%, a ~3-point gap that ships a ⚠ monitor-gap chip, because the new supply is being classed as staked and non-circulating even though on-chain issuance clearly rose to 11.10M. The key variable is the recycle rate; the ceiling is the fixed 21M cap and the next halving that will one day halve the mint again.

*MrNasdog Pressure Framework analysis of Bittensor (TAO), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 8 2026.*

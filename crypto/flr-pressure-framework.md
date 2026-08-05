---
title: "FLR Inflation Analysis · August 2026 · Supply growing slowly, the airdrop era over"
description: "A MrNasdog Pressure Framework read of Flare (FLR): ~636M FLR/90D minted at 3% inflation vs a ~74M base-fee burn. Framework +0.65% net; monitor +0.898% (gap 0.25pp, no flag)."
canonical_url: "https://mrnasdog.com/research/flr/inflation"
tags: ["crypto", "flr", "flare", "oracles"]
published: true
---

> Originally published at **[mrnasdog.com/research/flr/inflation](https://mrnasdog.com/research/flr/inflation)** by MrNasdog.

Flare is an uncapped chain that mints new FLR to fund rewards, so its supply keeps growing — but far more slowly than in the airdrop era. Over the last 90 days protocol inflation minted about **636M FLR** while the transaction-fee burn removed about **74M FLR**, for a net of **+0.65%** against a circulating base of **86.8B FLR**. Our supply monitor reads **+0.898%** — a gap of just **0.25 percentage points**, inside tolerance, so no monitor-gap flag ships. With the FlareDrops airdrop and the multi-year ecosystem burn both finished, FLR is now a simple two-sided ledger: **3%** inflation on one side, a fee burn on the other.

## The verdict, in one paragraph

For the 90-day window ending **Aug 5 2026**, the Pressure Framework reads **FLR at +0.65% net**. Sell pressure is **636M FLR**, entirely protocol inflation, and buy pressure is **74M FLR**, entirely the fee burn, against a circulating base of **86,803.46M FLR**. Our supply monitor reads the realised change at **+0.898%**, a gap of **0.25 percentage points**, comfortably inside tolerance, so no monitor-gap chip ships. The monitor sits slightly higher mainly because reward FLR minted just before the window is being claimed inside it, plus ordinary price-and-market-cap snapshot noise. Both the last-90-day and next-90-day readings land just above half a percent, so the verdict reads **supply growing, projected to keep growing** — Flare is best characterised as **a still-inflationary, uncapped Layer-1 whose issuance is now offset only by a fee burn**.

## Sell pressure: where new FLR comes from

The defining fact about Flare is that it has **no maximum supply**. Unlike a hard-capped chain, Flare genuinely mints new FLR every reward epoch — roughly every three and a half days — to pay data-provider, staking and system rewards, and total supply is observed rising on-chain toward and past **106.3B FLR**. That makes Sell #1, protocol inflation, the whole of the sell side. Following the tokenomics overhaul approved **Apr 24 2026**, the annual inflation rate was cut from **5%** to **3%** and hard-capped at **3B FLR** a year, calculated on the distributed supply. That comes to about **2.58B FLR** a year, or roughly **636M FLR** over 90 days, all newly minted and reaching the market as holders claim their rewards. Because the rate is measured against a supply that itself keeps growing, the effective inflation drifts steadily lower over time, but within a single quarter the mint is essentially flat.

The other three sell rows are **zero**, and the reason each is zero is the more interesting story. Sell #2, vesting unlocks, is zero because Flare's big scheduled distribution — the 36-month **FlareDrops** to wrapped-FLR and staked holders — concluded on **Jan 30 2026**, alongside a separate multi-year ecosystem burn that also ran its course by then; the early-backer voluntary vesting extension ended in the first quarter of 2026, and the founding-team lockup expired back in 2024. No dated unlock cliff remains inside or beyond the window. Sell #3, Foundation and unscheduled unlocks, is zero because although the Flare Foundation controls most of the roughly **19.5B FLR** that is minted but not yet circulating, it funds rewards through inflation rather than by selling reserve, and no discretionary reserve sale was observed this window. Sell #4, long-term locked or bankruptcy, is zero because there is no Flare estate, trustee or court-ordered distribution.

## Buy pressure: where new FLR goes

Flare has exactly one live buy-side mechanism, and it is Buy #2, the protocol fee burn. Every transaction fee on Flare is destroyed, and the same overhaul raised the base fee twenty-fold — from **60** to **1,200 gwei** — which the network expects to burn about **300M FLR** a year at current activity, or roughly **74M FLR** over 90 days. That offsets a little over a tenth of the new inflation, so it softens the growth without reversing it.

Buy #1, programmatic buyback, is **zero** for now, but it is the row to watch. The reform stood up a treasury — the Flare Income Reinvestment Entity, or **FIRE** — that takes protocol revenue from data-connector fees, FAssets and captured MEV, buys FLR on the open market and burns it. It went live on **Apr 24 2026**, but the revenue behind it is still small and no purchase amount has been disclosed, so its realised buy-and-burn is immaterial this window; the destination is the burn address, and any real activity lands here at the next refresh. Buy #3, foundation buy, is zero because no entity has disclosed an open-market FLR purchase. Buy #4, new long-term lock, is zero because staking on Flare — both liquid sFLR and P-chain staking — leaves FLR fully tradable and removes nothing from supply.

## Foundation and overhang

The one large team-controlled overhang on Flare is the **Flare Foundation and ecosystem reserve** — the bulk of the roughly **19.5B FLR** gap between the **86.8B** circulating float and the **106.3B** total, with the Foundation and ecosystem funds allocated about **22.5%** of supply. There is no published release schedule for it, but unlike a foundation that funds itself by selling reserve, Flare pays its rewards by minting inflation, so this balance has not been a direct source of market sales. Alongside it sits a smaller residual of team and early-backer tokens that continues to vest, but only drips under a voluntary cap of **0.5%** of 30-day average volume. All of it is re-read on every rebuild, and if the Foundation reserve balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How FLR compares to other uncapped Layer-1s

The first comparison is cap versus emission. A hard-capped chain reaches a fixed ceiling and stops minting, so its float can only grow by releasing reserve. Flare is the opposite: there is **no cap** at all, and the sell side is a live issuance rate that never reaches zero — the same shape as other uncapped proof-of-stake Layer-1s that pay ongoing staking rewards. What FLR shares with the better-run ones is a declining rate: the **3%** is measured against a growing base and steps down over time, and the reform cut it by two-fifths in one move.

The second comparison is burn versus no burn. Flare belongs to the family of fee-burning chains — like the large EVM networks that destroy their base fee — where heavy usage can meaningfully offset issuance. The difference is scale: at **3%** inflation and a fee burn worth only about **300M FLR** a year, Flare's burn recovers a little over a tenth of new supply, not the majority, so activity alone cannot turn FLR deflationary the way it can on a chain with a much larger fee base relative to issuance.

The third comparison is who controls the tap. On a halving-model chain the emission schedule is fixed in code. On Flare the inflation rate, the fee level and the new buy-and-burn treasury are all governance parameters — the community just cut inflation, hiked the fee twenty-fold and launched FIRE in a single proposal. That makes FLR's supply unusually responsive to governance, which cuts both ways: the same mechanism that just slowed issuance could accelerate a burn if FAssets and MEV revenue scale.

## What to watch in the next 90 days

First, **FIRE** — whether the buy-and-burn treasury starts reporting real FLR purchases as FAssets and MEV revenue grows; the first disclosed quantum would move Buy #1 off zero. Second, the fee burn — the **300M FLR**-a-year figure assumes current activity, so a rise or fall in Flare transactions changes how much of the inflation is offset. Third, network usage on FAssets and the data-connector, which is the revenue base behind both the burn story and FIRE. Fourth, any follow-up governance proposal, given how much the community changed in one vote. Fifth, the inflation rate itself, which keeps drifting down as the distributed supply it is measured against grows.

## Summary

Flare (FLR) is an uncapped EVM Layer-1 whose float still grows on protocol inflation, now that the FlareDrops airdrop and the multi-year ecosystem burn both concluded in January 2026. Over the last 90 days inflation minted about **636M FLR** and the fee burn removed about **74M**, a framework reading of **+0.65% net** against a monitor reading of **+0.898%**. The June 2026 overhaul cut inflation from 5% to **3%**, hiked the base fee twenty-fold and launched a buy-and-burn treasury, so the trend is toward slower growth. The key risk is that FLR has no cap and the burn recovers only about a tenth of issuance, so it stays mildly inflationary — and the swing factor is whether the new burn mechanisms can scale enough to close that gap.

---

*MrNasdog Pressure Framework analysis of Flare (FLR), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 5 2026.*

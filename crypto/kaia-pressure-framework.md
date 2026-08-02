---
title: "KAIA Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description: "A MrNasdog Pressure Framework read of Kaia (KAIA): 74.6M KAIA minted in 90 days at a fixed 9.6 per one-second block against only 0.05M burned. Framework +1.17% net; monitor +8.94%."
canonical_url: "https://mrnasdog.com/research/kaia/inflation"
tags: ["crypto", "kaia", "klaytn", "layer1"]
published: true
---

> Originally published at **[mrnasdog.com/research/kaia/inflation](https://mrnasdog.com/research/kaia/inflation)** by MrNasdog.

Kaia is an uncapped L1 that mints a fixed **9.6 KAIA** every block, and with one-second blocks that is a steady stream: about **74.6M KAIA** was created over the last 90 days, roughly **5.2%** a year. Almost nothing offsets it — the base-fee burn removed only about **0.05M KAIA** and there is no buyback — so the Pressure Framework reads **+1.17% net**, mildly inflationary. Our supply monitor reads **+8.94%**, a gap of **7.77 percentage points**, because the market-data supply feed jumped **519M KAIA** in a single day on **Jul 29 2026** — a recount, not real issuance.

## The verdict, in one paragraph

For the 90-day window ending **Aug 2 2026**, the Pressure Framework reads **KAIA at +1.17% net**. Sell pressure is **74.6M KAIA** of block-reward issuance, buy pressure is a negligible **0.05M KAIA** base-fee burn, against a circulating base of **6.38B KAIA**. Our supply monitor reads **+8.94%**, a gap of **7.77 percentage points**, so a **⚠ monitor gap** chip ships on the KAIA overview. The gap is not a disagreement about mechanism — it is a data step. The monitor derives supply from market cap over price, and that figure sat flat at about **5.86B KAIA** for the entire window before jumping **519M** in one day on **Jul 29 2026**. A fixed 9.6-per-block mint is a smooth **0.83M KAIA a day** and can never produce a half-billion one-day step; that step is a circulating recount, most likely post-merger migrated supply folded into the headline figure. KAIA is best characterised as **steadily inflationary on a fixed, uncapped emission**.

## Sell pressure: where new KAIA comes from

Sell #1, protocol inflation, is **74.6M KAIA**, and it is the entire sell side. Kaia's reward module mints a fixed **9.6 KAIA** per block, and blocks arrive about once a second — measured on the chain, block time is **1.0002 seconds** — so over the 90-day window the protocol created roughly **74.6M KAIA**, an annualised pace near **5.2%** on an uncapped token. Half of each block reward goes to stakers and the other half is split between the Kaia Ecosystem Fund and the Kaia Infrastructure Fund; because those funds spend roughly what they receive rather than hoard it, the full mint reaches the market and is booked here. The rate is protocol-encoded and did not change inside the window, so the trailing pace and the live pace are the same.

The remaining sell rows are all **zero**, and for structural reasons. Sell #2, vesting unlocks, is zero because Kaia's unlock calendar is exhausted: after the **2024** Klaytn and Finschia merger the old KLAY and FNSA allocations finished migrating, and trackers report every token already in circulation with nothing scheduled to release beyond the block rewards. Sell #3, foundation and unscheduled unlocks, is zero because nothing was net-released — the tracked funds are a pipe, not a reservoir. Sell #4, long-term locked or bankruptcy, is zero: there is no Kaia estate, no trustee and no court-ordered KAIA distribution.

## Buy pressure: where new KAIA goes

Buy #2, protocol fee burn, is the only non-zero buy row, and it is small: about **0.05M KAIA**. Since the Kore hardfork Kaia burns most of the KIP-71 base fee on every transaction, permanently removing KAIA from supply. The mechanism is genuine, but Kaia's gas activity is light and the base fee sits at its **25 gwei** floor, so the burn over 90 days is under a fifteen-hundredth of the mint — it barely dents the inflation. There is no accumulation wallet to track, because burned tokens are destroyed outright.

The other three buy rows are **zero**. Buy #1, programmatic buyback, is zero because Kaia runs no buyback — there is no contract or programme that uses revenue to purchase KAIA. Buy #3, foundation buy, is zero because no Kaia Foundation open-market purchase of KAIA has been disclosed. Buy #4, new long-term lock, is zero because staking is not a lock: staked KAIA can be withdrawn after an unbonding delay and counts as circulating the entire time, so it removes nothing from supply.

## Foundation and overhang

Two team-controlled overhangs are tracked on Kaia. The first is the **Kaia Ecosystem Fund**, roughly **11.6%** of supply, which funds grants, incentives and liquidity. The second is the **Kaia Infrastructure Fund**, roughly **10.8%** of supply, which funds core development and operations. Both receive a quarter each of every block reward and are already counted inside the circulating figure, and both spend at roughly the rate they receive, so their combined balance stays broadly flat rather than building a release overhang. They are re-read on every rebuild, and if either balance falls between refreshes, the outflow enters Sell #3 at the next refresh. Neither showed a net drawdown this window, which is why Sell #3 is zero rather than a projected number.

## How KAIA compares to other uncapped L1s

The first comparison is cap versus no cap. Halving-model chains with a hard ceiling have a sell side that shrinks on a published schedule; Kaia has neither a cap nor a schedule, only a fixed **9.6 KAIA** per block that runs forever. Unlike the bonded-ratio control loops of many Cosmos-family chains, Kaia's rate does not float with staking participation — it is a flat per-block constant, so issuance in absolute KAIA is steady and the percentage rate slowly falls only as the denominator grows.

The second comparison is burn versus no burn. Chains with an EIP-1559-style base-fee burn can turn heavy on-chain activity into real supply removal, and exchange tokens with quarterly buybacks can print net-negative supply. Kaia has the burn mechanism — most of the base fee is burned since Kore — but not the activity to make it matter, so the burn is a rounding error against the mint. That places Kaia among the pure-emission L1s in practice: the buy side is structurally too small to change the sign.

The third comparison is what the market data shows. Many tokens carry a release calendar as their main risk; Kaia's risk is subtler and is really about data. Its published circulating figure held flat for the whole window and then stepped up half a billion KAIA in a single day, which is a recount of already-existing supply rather than a burst of issuance. An observer trusting that headline would misread a one-day reclassification as an **8.94%** inflation spike, when the chain has in fact been minting at a steady, much smaller pace the entire time.

## What to watch in the next 90 days

First, the **GP-21 tokenomics reform**: Kaia's Permissionless Kaia roadmap targets around **Sep 2026** for ending the Proposal Reward and introducing a Contribution Reward, under which inflation not earned through measurable contribution is burned — if it activates and bites, it could pull the effective mint below the current **9.6**-per-block pace, so it is the single biggest lever on this reading. Second, whether the circulating figure steps again — the **Jul 29 2026** jump of **519M** shows the headline supply is still catching up to the merger, and another recount would move the monitor without changing real issuance. Third, on-chain gas activity: a sustained rise would make the base-fee burn large enough to actually offset part of the mint. Fourth, any change to the fixed **9.6 KAIA** block reward through governance, which would re-base the whole sell side. Fifth, any first net drawdown from the Ecosystem or Infrastructure funds, which is what would put a non-zero number in Sell #3.

## Summary

Kaia (KAIA) is mildly inflationary on a fixed, uncapped emission: the protocol minted about **74.6M KAIA** over 90 days at a steady **9.6 KAIA** per one-second block, roughly **5.2%** a year, while the base-fee burn removed only about **0.05M KAIA** and there is no buyback — a framework reading of **+1.17% net**. Our supply monitor reads **+8.94%** because the market-data feed stepped up **519M KAIA** in one day on **Jul 29 2026**, a recount of post-merger supply rather than new issuance. The key risk to the reading is a data one: the headline circulating figure is still catching up to the 2024 merger, and until it settles the monitor will overstate how much KAIA is actually being created.

---

*MrNasdog Pressure Framework analysis of KAIA, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 2 2026.*

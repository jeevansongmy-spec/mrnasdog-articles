---
title: "FLR Inflation Analysis · October 2026 · Supply growing · projected to keep growing"
description: "FLR supply grew 1.03% in 90 days: 623M FLR of staking rewards and 306M of rFLR and escrow unlocks against 26M burned or set aside. About the same next."
canonical_url: "https://mrnasdog.com/research/flr/inflation"
tags: ["crypto", "flr", "flare", "oracles"]
published: true
---
Originally published at [FLR Inflation Analysis · October 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/flr/inflation).

# FLR Inflation Analysis · October 2026 · Supply growing · projected to keep growing

<!-- main-page -->

**FLR** supply is growing: it rose **+1.03%** in the 90 days to Oct 27 2026 and should rise about **+1.05%** in the next 90, against **+0.76%** on other trackers. Flare mints new FLR at **3%** a year for stakers and data providers and keeps vesting reward FLR (rFLR) out of a **17.17B** FLR incentive pool, with no supply cap. Holders received **929.94M FLR** while burns and the new fee wallet took back only **25.89M**.

## The verdict, in one paragraph

Between Jul 29 and Oct 27 2026, **929.94M FLR** reached holders and **25.89M FLR** left the count, so the circulating supply of **87.62B FLR** grew a net **+1.03%**. Other trackers show **+0.76%** for the same 90 days, a gap of **0.27** points, small enough that the coin page carries no warning note. For the next 90 days the same flows point to **+1.05%**. Flare is a steady issuer: inflationary by design, with burns that so far cancel less than 3% of the new FLR.

## Sell pressure: where new FLR comes from

**Protocol inflation is the largest source.** Flare pays validators, stakers and the providers who post price data and data proofs in newly minted FLR. Since the FIP.16 vote passed on Apr 24 2026, the yearly rate is **3%** instead of 5%, with a ceiling of 3B FLR a year, and the lower rate has applied since May 14 2026. In these 90 days holders claimed **623.43M FLR** of those rewards, about 6.9M a day. Rewards nobody claims within three months are burned before they ever reach a wallet, so they never count.

**Vesting unlocks are the second source.** Flare's incentive program pays rewards as rFLR, which vests over 12 months. Holders withdrew **302.07M FLR** of rFLR in the window, and anyone who withdraws early gives up half, which is burned. The 2023 sale escrow added **4.44M FLR** more. The escrow finished vesting in early 2026, and these were late claims by people who had not collected yet. Together the row is **306.51M FLR**. For the next 90 days we count only the rFLR flow, **302.07M FLR**, since late escrow claims come at random.

**Foundation and unscheduled unlocks are zero.** The large pools held outside circulation did not release anything beyond the steady rFLR flow already counted. **Long-term locks and bankruptcy are zero** too: no court or estate holds FLR waiting to be paid out.

## Buy pressure: where new FLR goes

**The programmatic buyback is still only a fee wallet.** FIP.16 created FIRE, a pool meant to buy FLR on the market and burn it. Since Aug 18 2026, 90% of the fees paid for Flare's data requests go to a Foundation-held fee wallet that now holds **4.31M FLR**. Those coins are out of circulation, so they count here. The wallet has not bought or burned any FLR yet. It adds about 1.35M FLR a month, about **4.05M** in the next 90 days.

**The gas burn is real but small.** All gas on Flare is burned. The Jul 14 2026 upgrade raised the minimum gas price 20 times, to 500 gwei, and about **4.58M FLR** was burned this way in 90 days. Most traffic on the chain is price data from providers, and they get their gas back. FIP.16 hoped the higher fee could burn about 300M FLR a year. At this pace the gas burn is closer to 19M FLR a year.

**The Foundation buys nothing, and staking locks nothing.** Staking rose from about 16B to 21.5B FLR after the July upgrade, but staked FLR still counts as circulating. The extra row is **multisig reward burns**. One large multisig collects its staking rewards and burns them about once a month. It burned **12.00M FLR** on Aug 13 2026 and **5.00M** on Sep 8 2026, **17.00M FLR** in all. With no schedule and no burn since Sep 8 2026, we count none for the next 90 days.

## Foundation and overhang

The biggest pile is the **incentive pool**, with **17.17B FLR**. It moves about 4.85M FLR a day into the rFLR program, which is the flow counted above. The **rFLR contract** itself holds **828.14M FLR** backing rewards that have not vested. The old **sale escrow** still holds **200.07M FLR** that its owners can claim at any time. Reward pots hold about **231M FLR** waiting to be claimed or burned. Wallets listed by the Foundation hold **4.39M FLR**, almost all of it the new fee wallet. All of these sit outside circulation today. The burning multisig holds **15.29M FLR** inside circulation. We read every one of these balances on-chain at each rebuild. If any of them falls by more than its known flow between rebuilds, the extra outflow enters the foundation and unscheduled unlocks row at the next rebuild.

## How FLR compares to other proof-of-stake Layer 1 chains

Like **Ethereum**, **Flare** has no supply cap and pays its security budget in new coins. The difference is the burn. Ethereum destroys the base fee of every transaction, which can cancel a real share of issuance on a busy day. On Flare, most activity is price data whose gas is refunded, so the gas burn cancels well under 1% of new FLR. **Avalanche**, the code Flare's chain is built from, burns all fees and caps supply at 720M AVAX. Flare kept the fee burn but not the cap.

What sets FLR apart from most proof-of-stake chains is the second stream. On top of staking pay, the rFLR program draws on a pre-minted pool of 17.17B FLR, adding about half as much again as the staking pay each quarter. Chains like **Solana** lower their rate on a fixed schedule toward a floor. Flare cut its rate by vote (FIP.16). Its plan is for fees, MEV capture and FIRE buybacks to cut supply over time, but those buybacks have not started.

## What to watch in the next 90 days

**Nov 2 2026:** Coincheck in Japan stops handling FLR, and holders there must move their coins out before then. This moves no supply, but it changes where some FLR sits.

**The first FIRE buyback:** the fee wallet holds 4.31M FLR and has never bought or burned. A first purchase and burn would move the buy side for the first time.

**MEV capture:** FIP.16 plans a single block builder chosen by FIRE, with its MEV earnings going to the pool. A start date would be the first sign of real buyback money.

**The multisig burn:** it burned about monthly for over a year, and its last burn was on Sep 8 2026. A new burn would add to the buy side.

**The rFLR flow:** about 4.85M FLR a day leaves the incentive pool. A governance change to that program would move the biggest flow after staking pay.

## Summary

FLR supply grew **+1.03%** in the 90 days to Oct 27 2026 and should grow about **+1.05%** in the next 90 days. Flare pays **3%** a year in new FLR to stakers and data providers, and it keeps vesting rFLR out of a 17.17B FLR incentive pool, which brought about 930M FLR to holders in one quarter. The gas burn, a monthly multisig burn and the new FIRE fee wallet took back only 25.89M FLR, under 3% of that. FLR has no supply cap, so supply keeps growing unless fees and FIRE buybacks grow many times over.

*MrNasDog Pressure Framework analysis of FLR, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 27 2026.*

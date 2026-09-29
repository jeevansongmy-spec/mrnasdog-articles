---
title:         "HBAR Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "HBAR supply grows with no minting: the Hedera Council released 341.8M HBAR from its reserve in 90 days, +0.78% net, about +0.68% next. No buyback, no fee burn."
canonical_url: "https://mrnasdog.com/research/hbar/inflation"
tags:          ["crypto", "hbar", "hedera", "layer1"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/hbar/inflation](https://mrnasdog.com/research/hbar/inflation)*

# HBAR Inflation Analysis · September 2026 · Supply growing · projected to keep growing

HBAR supply is growing, and none of the growth comes from minting. Over the last 90 days the Hedera Council released **341.8M HBAR** from its reserve into the market, while nothing was bought back or burned, so circulating HBAR rose **+0.78%**. We expect about **+0.68%** in the next 90 days. The ceiling is set by the Council’s own rules: **50B HBAR** exist, **43.83B** are released, and the **6.17B** still in Council accounts is the most that can reach the market unless every Council member votes to change the total.

## The verdict, in one paragraph

Over the trailing 90 days (Jul 1 to Sep 29 2026) HBAR’s circulating supply grew by **+0.78%**, from **43.49B** to **43.83B** HBAR. Our monitor, which reads the same supply series independently, shows **+0.84%** for its latest 90-day window — a gap of just **0.06 percentage points**, well inside our 0.5-point tolerance, so no warning chip is shown. Every one of the 341.8M new HBAR can be traced to a named Council reserve account paying out on a known date, and the reserve balances add back to the released supply to the last tinybar. For the next 90 days we project another **298.3M HBAR**, or **+0.68%**. HBAR is a coin with no issuance at all whose supply still grows steadily: **a treasury-release chain**, where the only question is how fast the Council empties its reserve.

## Sell pressure: where new HBAR comes from

Protocol inflation on Hedera is **0**. The network has no block reward and no way to mint HBAR; all 50B coins were created at launch, and the total can change only if every Hedera Council member votes for it. Stakers are still paid about **445K HBAR a day**, but that money comes out of a staking reward account that was filled in advance. This window that account paid out and shrank from **182.8M** to **136.3M HBAR**. Its coins were already counted as circulating, so HBAR staking rewards move coins inside the market rather than add new ones.

Vesting unlocks come from Hedera’s old contributor coin plan, which pays out at each quarter turn: 16.43M HBAR on Jan 2 2026, 17.32M on Apr 1 and 16.64M on Jun 30. The Jun 30 payment landed a few hours before this window opened, so only a **14.7K HBAR** straggler on Aug 28 2026 fell inside it. The next payment, about **16.8M HBAR**, is due around Sep 30 2026 and sits in our next-90-day count.

The Foundation and unscheduled unlocks row carries almost all of HBAR’s sell pressure: **341.8M HBAR** this window. On Jul 2 2026 the Council moved **300M HBAR** out of two reserve accounts, in two 150M transfers, to outside accounts for its own operating reserves. On Aug 15 2026 it released **40M HBAR** in ecosystem grants to an account that still holds every coin, staked. Small monthly payouts from a separate reserve account added **1.8M HBAR** on Jul 15, Aug 15 and Sep 18. Council operating releases have come in every one of the last four quarters — 370.8M, 301.2M, 151.5M and 302.7M HBAR — so we project the quarterly average, **281.5M HBAR**, for the next 90 days.

Long-term locks and bankruptcy releases are **0**. No estate, trustee or long lockup holds HBAR, and the funds and exchanges that hold large amounts bought coins that were already in the market.

## Buy pressure: where new HBAR goes

Every buy-side row for HBAR is **0**. There is no programmatic buyback: neither the Hedera Council nor the network buys HBAR off the market. There is no protocol fee burn either. Hedera charges fees fixed in US dollars and paid in HBAR — our samples this week ranged from about **3,500** to **27,000 HBAR a day** — and every fee is swept every day to the nodes, the staking reward account and the node reward account. Nothing is destroyed, and the released supply rose by exactly the reserve releases, which confirms that no HBAR left the market.

There was no Foundation buy: the only coins that flowed back into Council accounts this window were a few thousand HBAR of dust. And staking is not a lock. About **11.48B HBAR** is staked, but Hedera staking has no lock-up period — a staked balance stays liquid at all times — so staked HBAR stays spendable and stays in the circulating count. The new long-term lock row is therefore **0** as well.

## Foundation and overhang

The whole HBAR overhang is the Hedera Council reserve: **6.17B HBAR** spread across the Council’s numbered treasury accounts, down from 6.51B at the start of the window. About **3.86B** sits in the accounts the Council calls unallocated storage and **2.31B** in its allocated accounts; the largest single account holds 599.9M HBAR. We read every one of these balances from the chain at each rebuild.

The item to watch inside it is the ecosystem grant line. The Council’s own treasury report, with data as of Sep 3 2026, still forecasts **3.54B HBAR** of ecosystem releases for the third quarter of 2026, of which only the 40M paid on Aug 15 has moved. The same line was forecast for late 2025, early 2026 and mid-2026, and each time little or nothing was paid: 208.8M HBAR on Jan 28 2026, and nothing in the second quarter. With one day of the quarter left, the account that paid the earlier grants holds just 101.3M HBAR. We therefore treat the roughly **3.5B HBAR** as capacity, not a schedule, and keep it out of the forecast. If it were paid in the next 90 days, HBAR supply would grow about **8.7%** instead of 0.68%. Outside the reserve, the staking reward account holds 136.3M HBAR; it is already in the market, but a top-up from the reserve would count as a release. If any reserve balance falls between our refreshes, that outflow enters the Foundation and unscheduled unlocks row at the next refresh.

## How HBAR compares to other treasury-release Layer 1s

HBAR belongs to the group of Layer 1 coins with a fixed total created at launch and handed out over time by a company, council or foundation, rather than issued as a block reward. XRP is the closest match: its total is also fixed, nothing is mined, and new supply reaches the market only when the issuer releases coins from its own holdings. Both coins pay network fees without adding coins, and both have a known ceiling on future supply — for HBAR, the 6.17B still held by the Hedera Council.

The contrast with staking chains is sharp. On Ethereum, Solana or Cardano, validators are paid in new coins every epoch, so supply grows with the stake and never stops. Hedera pays stakers from a pre-filled account, so staking adds no supply at all; the growth comes entirely from the Council deciding to release. That makes HBAR’s supply growth lumpy and decision-driven — 300M in one day on Jul 2 2026, almost nothing for weeks after — instead of smooth.

Unlike fee-burning chains such as Ethereum or BNB Chain, Hedera destroys nothing, so there is no buy-side offset however busy the network gets. And unlike capped proof-of-work coins such as Bitcoin, the release pace is set by people, not code: the reserve could run out in a few years at today’s pace, or much faster if the 3.5B ecosystem grant is finally paid.

## What to watch in the next 90 days

First, the quarterly coin plan payment of about **16.8M HBAR**, due around Sep 30 2026 — it should show up as a jump in released supply at the quarter turn. Second, whether the **3.54B HBAR** ecosystem release forecast for the third quarter happens at all; the next Council treasury report, likely in early December 2026, will show whether it moved or was pushed into the next quarter again. Third, the size of the next Council operating release — the last four quarters ranged from 151.5M to 370.8M HBAR. Fourth, the staking reward account: its unreserved balance was **124.6M HBAR** on Sep 29 2026 against an 85M floor set by the network, and at today’s pace it gets close by around mid-December 2026, which could mean lower staking rewards or a top-up from the reserve.

## Summary

HBAR is inflationary on the market float even though no HBAR is ever minted: the Hedera Council released **341.8M HBAR** in the last 90 days, supply grew **+0.78%**, and we project about **+0.68%** for the next 90 days, with no buyback or burn to offset it. All new supply comes from Council reserve accounts, which still hold **6.17B HBAR**. The key risk is the roughly **3.5B HBAR** ecosystem grant the Council keeps forecasting; if it moves, supply jumps about 8.7% in one step. The ceiling is hard: HBAR can never exceed its **50B** total without a unanimous Council vote.

---

*MrNasdog Pressure Framework analysis of HBAR, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

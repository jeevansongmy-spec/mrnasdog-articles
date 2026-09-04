---
title:         "LTC Inflation Analysis · September 2026 · Mixed flows, supply roughly steady"
description:   "Mixed flows, supply roughly steady: a 6.25 LTC subsidy minted 0.322M LTC in 90 days into an empty buy ledger. Net +0.41% on Litecoin, no burn or buyback."
canonical_url: "https://mrnasdog.com/research/ltc/inflation"
tags:          ["crypto", "ltc", "litecoin", "payments"]
published:     true
---

# LTC Inflation Analysis · September 2026 · Mixed flows, supply roughly steady

*Originally published at [https://mrnasdog.com/research/ltc/inflation](https://mrnasdog.com/research/ltc/inflation)*

Litecoin (LTC) minted **0.322M LTC** over the last 90 days from a fixed proof-of-work block subsidy of 6.25 LTC, and the Litecoin protocol offset none of it — no buyback, no fee burn, no staking lock, no burn built into the design anywhere. The MrNasdog Pressure Framework reads **+0.41% net** against a **77.57M** circulating base under an 84M hard cap, with the independent supply monitor at **+0.10%** — a gap of **0.31 percentage points**, inside tolerance. About 92% of all Litecoin is already mined, and no halving falls inside the window behind or the window ahead: the next Litecoin halving lands at block 3,360,000, roughly **Jul 2027**.

## The verdict, in one paragraph

For the 90-day window ending **Sep 4 2026**, the framework reads **LTC at +0.41% net inflation**: clockwork mining emission against a buy ledger that is completely empty. The independent supply monitor reads **+0.10%** over the same window — a gap of **0.31 percentage points**, inside the half-point tolerance, so no monitor-gap warning is raised on the Litecoin reading. The residual is snapshot noise rather than disagreement about mechanism: the monitor infers Litecoin supply from market data, so its start point sits slightly off the exact block height the framework measured, while the framework counted the blocks themselves. Litecoin is a **quiet chain with a predictable, decaying issuance curve** — fifteen years of proof-of-work mining edging toward a fixed ceiling, with nothing discretionary anywhere in the supply picture.

## Sell pressure: where new LTC comes from

One row carries the entire Litecoin sell ledger. **Protocol inflation is 0.322M LTC**, and it is the block subsidy and nothing else: the Litecoin coinbase pays **6.25 LTC** to the miner of every block, and the chain sealed **51,449** blocks between the two window ends. That block count is counted, not assumed, and the distinction matters on Litecoin. The published Litecoin target is a 150-second block; the chain actually ran at **151.14 seconds** across the window. Because the Litecoin subsidy is paid per block and no protocol constant rescales it for a slow interval, running slow does not merely delay the halving — it directly reduces issuance. Taking the 2.5-minute target at face value would have implied 51,840 blocks and 324,000 LTC, **over-stating real Litecoin issuance by 0.76%**.

The other three sell rows are structural zeros, and each is zero for a different reason. **Vesting unlocks are 0** because Litecoin was fair-launched in October 2011 with no premine, no investor allocation and no team tranche — there is no vesting contract on Litecoin and no unlock calendar that could ever fire. **Foundation and unscheduled unlocks are 0** because the Litecoin Foundation holds no protocol allocation; none was ever created, so there is nothing to release. And **long-term locked or bankruptcy is 0** because no estate, trustee or court-ordered distribution schedule holds LTC. A coin with one live sell row and three permanent zeros is an unusually legible supply object.

## Buy pressure: where new LTC goes

Nowhere. All four buy rows on Litecoin read **0**, and the burn row in particular is an evidenced zero rather than an assumed one — it was checked on both surfaces a burn can appear on. On the destruction side, the one community sink address on Litecoin has taken in **0.18 LTC** across its entire life since 2018 and has never spent an output, confirming it is a true sink; its last receipt landed in April 2026, before this window opened, so its balance moved by **zero** across the 90 days. On the supply side, Litecoin's issued total rose by exactly the block subsidy and never fell. Either surface could have moved without the other, so they are independent readings rather than two views of one flow — and both are flat.

The reason is design, not neglect. Every Litecoin block pays its subsidy **plus its transaction fees** to the miner; nothing is forfeited, and Litecoin has no fee-burn rule of the kind later chains adopted. **Programmatic buyback is 0** because Litecoin captures no protocol revenue and keeps no treasury, so nothing exists that could fund one. **Foundation buy is 0** with no public evidence of a purchase in the window. And **new long-term lock is 0** because Litecoin has no staking, no bonding and no lock contract — proof-of-work security is paid for out of the subsidy, not out of locked coins.

## Foundation and overhang

Three Litecoin overhangs are tracked, and none of them released supply into this window. The **Litecoin Foundation** is donation-funded, publishes no treasury wallet, and — because Litecoin had no premine — holds no protocol allocation at all, which makes it an unusually small overhang for a chain of this age. The largest identified holder is a Nasdaq-listed Litecoin treasury company that held **819,070 LTC** on Jul 17 2026, down from 894,298 LTC at the end of March, a drawdown of roughly **700 LTC** a day funding its own share repurchases. That flow is real, but it is not framework sell pressure: those coins were bought on the open market and already sit inside the circulating base, so a sale moves them between holders rather than adding supply — the same reason exchange-held balances are excluded. Third, **85,034 LTC** sits frozen at the consensus level following the recovery of a privacy-layer validation bug in March 2026, and cannot move at all. If any of these three balances falls between refreshes in a way that adds supply, the outflow enters the Foundation row at the next refresh.

## How LTC compares to other capped halving-model chains

Litecoin belongs to the capped, halving-model proof-of-work family, and inside it Litecoin sits at the conservative end. Bitcoin runs the same shape at a quarter of the speed — a 10-minute target against Litecoin's 2.5-minute one, and a 21M cap against Litecoin's 84M — with both chains cutting the subsidy on a fixed block interval that no vote can move. Bitcoin Cash is the same mechanism again with a different block size. What separates Litecoin from all of them is not the cap but the emptiness of the other side of its ledger: Litecoin has never added a burn, a buyback or a lock, so its net reading is always its gross issuance, and the only thing that ever changes it is a halving.

The sharpest contrast is with the chain Litecoin is merge-mined with. Dogecoin has been secured by the same Scrypt hashpower as Litecoin since 2014 — a miner works both chains at once — yet the two run opposite supply policies. Litecoin is capped at 84M and halves; Dogecoin is uncapped and pays a flat 10,000 DOGE per block forever. Identical security model, opposite scarcity model, which is exactly the kind of comparison the framework is built to surface. On fee economy the ordering is worth stating precisely, because it is easy to get backwards: measured this window, Litecoin's miner fees run about **0.0031% to 0.0038%** of market cap a year — roughly **2,400 to 2,960 LTC**, on the order of **$122,000 to $151,000** against a **$3.96B** cap. That places Litecoin **above Dogecoin** at about 0.0022% and **below Bitcoin** at about 0.0059%. Litecoin is mid-field, not at the floor — and the leg carrying that verdict is a tiny absolute fee take, so the point is proportion, not size.

## What to watch in the next 90 days

Nothing dated moves the Litecoin ledger inside the forward window, which is itself the finding. The **next Litecoin halving** is the only scheduled change to issuance and it lands at block 3,360,000 around **Jul 2027**, cutting the subsidy from 6.25 to 3.125 LTC and roughly halving this page's sell row when it fires. Second, the **realised block interval** is worth re-measuring every build: it has now run slow two windows running, and a sustained drift moves both the issuance figure and the halving date. Third, the Nasdaq-listed Litecoin treasury company's annual report is expected around **Sep 2026** and will give the first hard balance since Jul 17 2026 — the number that says whether its drawdown is accelerating. Fourth, the privacy-layer soft fork that activated at block 3,154,440 on **Aug 4 2026** changed Litecoin validation rules only and left the subsidy untouched; any further consensus release should be checked against the same test. Fifth, a Litecoin layer-2 is slated for later in 2026, which would change where LTC is used without changing how much of it exists.

## Summary

The MrNasdog Pressure Framework reads Litecoin at **+0.41% net supply growth** over the trailing 90 days and the same again projected forward: **0.322M LTC** mined across **51,449** measured blocks at a 6.25 LTC subsidy, against a buy ledger of exactly zero confirmed on both a dead-address read and a supply read. The structural mechanism is the plainest in coverage — proof-of-work issuance under a fixed **84M** cap with roughly 92% already mined, no vesting, no treasury, no burn and no lock — and the key risk is simply that nothing offsets the mining, so Litecoin's net reading can only improve when the protocol itself cuts the subsidy. That cut is scheduled, not discretionary, and it arrives around **Jul 2027**.

---

*MrNasdog Pressure Framework analysis of LTC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 4 2026.*

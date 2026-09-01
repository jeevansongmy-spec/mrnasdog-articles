---
title: "XLM Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description: "Stellar has minted nothing since 2019, yet the XLM float still grows +2.86% per 90 days as the Foundation releases 991.4M XLM from thirteen mandate wallets. Monitor +2.82%."
canonical_url: "https://mrnasdog.com/research/xlm/inflation"
tags: ["crypto", "xlm", "stellar", "payments"]
published: true
---

*Originally published at [https://mrnasdog.com/research/xlm/inflation](https://mrnasdog.com/research/xlm/inflation)*

Stellar (XLM) added **+2.86%** to its tradable supply over the last 90 days and is projected to add the same **+2.86%** over the next 90 — even though the Stellar network has not minted a single lumen since **2019**. The entire increase comes from one place: the Stellar Development Foundation released **991.4M XLM** from its thirteen mandate wallets into circulation, against a fee pool that quietly absorbed just **601K XLM**. XLM is a fixed-supply asset with a discretionary float — the cap is real at **50.00B** lumens, but the pace at which the remaining **15,037.7M** reaches the market is a Foundation decision, not a protocol rule.

## The verdict, in one paragraph

The Pressure Framework reads XLM at **+2.86%** net supply growth over the last 90 days and **+2.86%** projected over the next 90, against a circulating base of **34.69B** lumens. Our independent supply monitor reads **+2.82%** for the same window — a gap of **0.03** percentage points, well inside tolerance, so no data-conflict flag is raised on this coin. Sell pressure totals **991.4M XLM** and buy pressure totals **601K XLM**, a ratio of roughly 1,650 to one. The cite-able label for Stellar is this: a hard-capped chain with a **committee-paced float**. Nothing is minted, nothing is burned, and the number that matters is how fast one non-profit chooses to spend its own treasury.

## Sell pressure: where new XLM comes from

Protocol inflation on Stellar is **0**. The 1%-a-year lumen mint was switched off by validator vote on **Oct 28 2019**, and the inflation operation itself now refuses to execute. The proof is arithmetic rather than editorial: the Stellar ledger's own coin count read exactly **105,443,902,087.3472865** at both ends of this window, identical to the last decimal. Not one lumen came into existence. That figure is a stored constant — Stellar has no destroy operation, so the famous 2019 burn never reduced it — and the published total supply of **50.00B** is that constant net of the **55.44B** lumens parked in a keyless address.

Vesting unlocks are also **0**, and by structure rather than by luck. XLM was never a venture-vested token: the three dated release escrows from the 2019 plan hold **2 XLM** each — account minimum, nothing more — and the Stellar Development Foundation mandate in force today publishes no escrow, no release calendar and no dated cliff. There is no unlock schedule to beat, and no unlock tracker carries one. Long-term locked or bankruptcy supply is **0** for the plainest reason available: no XLM estate has ever gone into administration, so there is no creditor queue waiting to be repaid in lumens.

That leaves one row carrying the entire sell side. Foundation and unscheduled unlocks came to **991.4M XLM** over the 90-day window, measured wallet by wallet across all thirteen Stellar Development Foundation mandate accounts at both window ends. The mandate aggregate fell from **16,029.1M** to **15,037.7M**, and transfers between Foundation wallets cancel inside that aggregate, so the figure is genuine outflow into the float rather than internal shuffling. On a **34.69B** base that single row is **2.86%** of circulating supply per quarter.

## Buy pressure: where new XLM goes

There is no programmatic buyback on Stellar — no contract, no announced programme, none proposed — so Buy #1 is **0**. Foundation buying is **0** for the same structural reason: the Stellar Development Foundation funds its operations by selling lumens, and has never been a market buyer of the asset it distributes. New long-term locks are **0** as well: Stellar has no staking, no bonding and no new lockup contract, and the 2015 network-migration escrow holding **258.9M XLM** moved by a fraction of one lumen all window.

The one live buy mechanism is the fee pool, and it is small. Every operation fee on Stellar drops into a ledger-level pool that belongs to no account and has no key; the only path that ever paid it out was the inflation operation deleted in 2019, so the balance only rises. It took **601K XLM** off the float over the window — a steady 5.7K to 8.0K lumens a day, with no step change — bringing the pool to **10.5M XLM** in total. That offsets about **0.06%** of what the Foundation released. Annualised at the current lumen price the whole Stellar fee base is worth roughly **0.007%** of the network's market value — hundreds of thousands of dollars a year against a multi-billion-dollar capitalisation. A fee burn of that size cannot offset a treasury release of that size, and on the measured numbers it does not come close.

One trap is worth naming, because a careless read gets it backwards. Stellar is famous for burning **55.44B** lumens once, in 2019. That burn was a transfer to an address with no signers, not a destruction — the keyless account still holds every one of them, and it took in **0.0001 XLM** across this window. Neither the keyless balance nor the ledger coin count moved, so no burn is booked. Stellar runs no ongoing burn at all.

## Foundation and overhang

The Stellar Development Foundation still holds **15,037.7M XLM** across thirteen wallets in four published buckets: SDF Development **2,057.4M**, Stellar Growth **5,857.2M**, Product and Innovation **3,707.9M**, and Assets and Liquidity **3,415.2M**. Every one of those balances is read on-chain at each rebuild. Alongside them sits the 2015 network-migration escrow at **258.9M XLM**, claimable one-for-one by holders of the pre-2015 network token but carrying no release date and showing no movement, and the keyless **55.44B** burn balance, which is gone rather than held. Together the non-circulating side is **15,307.0M XLM**, about **31%** of total supply.

None of it carries a published release schedule, which is exactly why the forward number on this coin is a behavioural forecast rather than a protocol constant. If any of these balances falls between refreshes, the outflow enters the Foundation and unscheduled unlocks row at the next refresh — that is the single trigger that moves the XLM inflation reading.

## How XLM compares to other fixed-supply payment chains

Against a halving-model chain with a hard cap, XLM looks similar on paper and behaves differently in practice. A halving chain's new supply is paid to miners on a schedule written into the protocol: anyone can compute the next 90 days exactly, and no committee can change it. Stellar has the harder cap — issuance is not merely slowing, it is switched off — yet its float grows faster, because the supply that reaches the market is released by decision rather than by block. The cap constrains the destination, not the pace.

Against uncapped continuous-emission L1s, the comparison inverts. Those chains mint every block and usually pair the mint with a fee burn, so their net figure is the difference between two protocol rules. Stellar has neither side of that equation: no mint, and a fee sink measured at **0.007%** of market value a year. That makes the Stellar reading unusually clean to derive — one row does all the work — and unusually hard to forecast, because a single organisation can change the answer without a governance vote.

The closest structural analogue is a genesis-minted chain whose growth is a foundation or council moving reserve onto the float — Hedera is the clearest example. Both have no protocol mint, no fee burn worth booking, and a large identified treasury as the sole driver. The distinction is pace and shape: reserve-release chains of that kind have recently run near **+1%** per 90 days in lumps, while Stellar ran at **+2.86%** as a near-continuous drain. Same mechanism class, roughly three times the intensity.

## What to watch in the next 90 days

First, the thirteen mandate wallet balances themselves — they are the only input that moves this reading, and they are read directly on-chain at every rebuild. Second, the Stellar Development Foundation's quarterly report, which is the surface on which any change to spending pace or mandate structure would be announced. Third, any amendment to the published mandate: a release calendar, a spending cap, or a new bucket would convert this row from a behavioural estimate into a scheduled one. Fourth, a validator vote touching issuance — the 2019 change was deliberately written so that inflation could be turned back on, so the zero in the protocol row is a policy state, not a permanent one. Fifth, the fee pool: a genuine step change in Stellar transaction volume is the only way the buy side stops being a rounding error, and nothing in the day-to-day pace over this window suggested one.

## Summary

The MrNasdog Pressure Framework reads Stellar (XLM) as supply growing and projected to keep growing, at **+2.86%** per 90 days against an independent monitor reading of **+2.82%** — a gap of **0.03** percentage points. The structural mechanism is unusual and easy to misread: Stellar mints nothing, burns nothing on an ongoing basis, and holds a hard cap of **50.00B** lumens, yet its tradable float still expands close to three percent a quarter because the Stellar Development Foundation released **991.4M XLM** from its mandate wallets into circulation. The key risk is that this pace is discretionary — no vesting schedule binds it and no burn absorbs it, so the forward number is a forecast of behaviour rather than of code. The ceiling is genuine: **15,037.7M XLM** remains in Foundation custody, and once that is spent the float can only grow again if Stellar validators vote issuance back into the protocol.

---

*MrNasdog Pressure Framework analysis of XLM, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 1 2026.*

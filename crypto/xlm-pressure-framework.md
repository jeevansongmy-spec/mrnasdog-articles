---
title: "XLM Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description: "Stellar mints nothing, yet XLM supply grew +2.90% in 90 days as the Foundation released 1.01B XLM and fees removed 657K. Monitor +2.96%, so no conflict."
canonical_url: "https://mrnasdog.com/research/xlm/inflation"
tags: ["crypto", "xlm", "stellar", "tokenization"]
published: true
---

Originally published at [https://mrnasdog.com/research/xlm/inflation](https://mrnasdog.com/research/xlm/inflation) by MrNasdog.

# XLM Inflation Analysis · September 2026 · Supply growing, projected to keep growing

XLM, the native asset of the Stellar network, has not had a single new lumen created since Stellar validators switched network inflation off in **2019**, and no XLM vesting schedule exists. The XLM float still grows, because the Stellar Development Foundation spends the lumens it has held since launch: its accounts released **1.01B XLM** into circulation over the last 90 days, while the Stellar fee pool took only **657K XLM** back out. The MrNasdog Pressure Framework therefore reads XLM at **+2.90% net** over 90 days against a supply-monitor reading of **+2.96%** — a gap of **0.06 percentage points**, which is agreement, not conflict. The limit is the Foundation's remaining **14.79B XLM**: once it is spent, the XLM float stops growing.

## The verdict, in one paragraph

For the 90-day window ending **Sep 24 2026**, the Pressure Framework reads **XLM at +2.90% net**: **1,013,504,522 XLM** left the Stellar Development Foundation's accounts for the open float, and **657,258 XLM** of transaction fees left the float for the fee pool. The independent supply monitor reads the realised 90-day change at **+2.96%**. The gap is **0.06 percentage points**, far inside the framework's half-point tolerance, so XLM ships with **no data-conflict flag**. The forward column reads the same **+2.90%**, because Foundation spending has run out of its accounts in every month measured and nothing published says the pace will change. The label for XLM is **a fixed-supply coin with a foundation-driven float**: the protocol adds nothing, and one organisation's spending decides how fast XLM supply reaches the market.

## Sell pressure: where new XLM comes from

Sell #1, protocol inflation, is **zero**. Stellar once added 1% a year to XLM supply through an inflation operation; Stellar validators voted it off in 2019, and the protocol the network runs today refuses that operation outright. That was checked this window, not assumed: the ledger's own count of existing lumens read the same at both ends of the window to the last decimal, and because that same field did grow in the years when inflation ran, a new lumen would have shown up there. Stellar activated two protocol upgrades inside the window, Zipper on **Jul 8 2026** and Adapter on **Sep 17 2026**; neither touched issuance, and the base fee read **100 stroops** at both ends. Sell #2, vesting unlocks, is **zero**: the escrow accounts that ran Stellar's 2019 lumen give-away programmes hold 2 XLM each and nothing more, and no unlock calendar exists for XLM.

Sell #3, foundation and unscheduled unlocks, carries the whole XLM sell side at **1.01B XLM**. The Stellar Development Foundation holds its lumens in **15** named accounts, and published XLM circulating supply is defined as total supply minus exactly those accounts, a network upgrade reserve and the fee pool. So a lumen counts once, at the moment it leaves a Foundation account for any address outside that set. Across the window those accounts sent **1.11B XLM** out and received **96.6M XLM** back, a net release of **1,013,504,522 XLM**, and every 30-day slice was an outflow — **270M**, **403M**, then **340M**. Transfers between the Foundation's own accounts, which moved far larger sums, cancel out and add nothing. The Foundation says it sells lumens from its development account on public exchanges, and it publishes no release schedule, so the pace is a decision rather than a rule. The measurement was closed against the Foundation's own published holdings at three dates, to the last fraction of a lumen. Sell #4, long-term locked or bankruptcy supply, is **zero**: no estate or long-dated lock holds XLM.

## Buy pressure: where new XLM goes

Almost nowhere. Buy #1, programmatic buyback, is **zero**: Stellar has no buyback contract and none has been proposed, and the Stellar Development Foundation funds itself by spending lumens, not buying them. Buy #2, the protocol fee burn, is the only XLM sink: every Stellar transaction fee lands in a fee pool that belongs to no account and has had no payout path since inflation ended, and published XLM circulating supply excludes it. The pool grew by **657,258 XLM** over the window, about **7,300 XLM** a day, and an independent fee series agrees with that reading to within five percent. The 2019 burn account took in only a fraction of one lumen, so there is no ongoing XLM burn beyond the fee pool. Buy #3, foundation buying, is **zero**: the **96.6M XLM** that came back into Foundation accounts arrived by plain transfer and is already netted inside the release. Buy #4, new long-term locks, is **zero**: Stellar has no staking, because its validators are neither paid nor bonded, and the small minimum balance every account must keep stays inside the circulating count.

## Foundation and overhang

The Stellar Development Foundation's **14.79B XLM** is the one XLM overhang that matters — about **42%** of circulating supply, held in four buckets: Development **1.94B**, Growth **5.83B**, Product and Innovation **3.63B**, and Assets and Liquidity **3.40B**. Every account is on-chain and readable, so the balances are re-read at each refresh rather than taken on trust, and they fell across the whole window. The second XLM overhang is the network upgrade reserve at **258.9M XLM**, set aside for holders of the pre-2015 network; it did not move in the window and has no release date. Exchange custody wallets and unlabelled large holders are excluded by rule, and every account a public directory tags to the Foundation with a real balance is already inside the fifteen. If any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How XLM compares to other payment and settlement chains

Most proof-of-stake Layer 1s grow their float by minting staking rewards and hope a fee burn offsets part of it. Stellar has neither half: no mint, because inflation was voted off, and no staking reward, because Stellar consensus pays its validators nothing. That makes XLM supply growth a custody question rather than a protocol question — the XLM float rises only as fast as the Stellar Development Foundation chooses to spend. Against a coin such as BNB, whose supply falls through scheduled burns, XLM sits on the other side of the ledger: its one sink, the fee pool, is real but tiny next to the Foundation's release.

Against other payment-focused chains whose float grows through releases by a single organisation, the XLM difference is the absence of any published calendar: the Foundation's release is observed after the fact on-chain, not read from a schedule in advance. The fee base underneath is small. Stellar's fee pool took in roughly **$537,000** a year at today's pace against a market capitalisation near **$7.07B**, about **0.008%** — real paid demand, but far too small to offset a release measured in billions of lumens.

## What to watch in the next 90 days

First, the pace of the Stellar Development Foundation's release: the forward reading holds the trailing **1.01B XLM**, and a quarter about **35M XLM** faster would carry XLM past three percent net. Second, the Foundation's next quarterly report, which states how many lumens each mandate bucket deployed; the Q2 2026 report put that at roughly **648M XLM**-equivalent for April to June, and the Foundation says it is updating how its lumens are allocated across its mandate. Third, Stellar protocol upgrades: Adapter went live on **Sep 17 2026** without touching issuance or the **100 stroop** base fee, and any future proposal that changes the fee pool or the inflation operation would move a zero row. Fourth, the **258.9M XLM** upgrade reserve: any outflow would open a new line in Sell #3.

## Summary

The MrNasdog Pressure Framework reads XLM at **+2.90% net** over the trailing 90 days and the same **+2.90%** over the next 90. The structural mechanism is plain: Stellar mints nothing and has no vesting, yet the XLM float grows because the Stellar Development Foundation released **1.01B XLM** from its accounts while the fee pool absorbed only **657K XLM**. The key risk is that the pace is discretionary — no schedule binds it, so the forward figure forecasts behaviour rather than code, and it can speed up or slow down without an announcement. The ceiling is the **14.79B XLM** still in Foundation custody; once that is spent, the XLM float can only grow again if Stellar validators vote issuance back into the protocol.

*MrNasdog Pressure Framework analysis of XLM, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 24 2026.*

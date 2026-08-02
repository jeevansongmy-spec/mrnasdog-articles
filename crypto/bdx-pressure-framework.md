---
title:         "BDX Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description:   "Beldex mints just 1.62M BDX a quarter but releases a fixed 130.68M from its ecosystem reserve, against 0.89M burned. Framework +1.67% net, monitor +1.71%."
canonical_url: "https://mrnasdog.com/research/bdx/inflation"
tags:          ["crypto", "bdx", "beldex", "privacy"]
published:     true
---

*Originally published at [mrnasdog.com/research/bdx/inflation](https://mrnasdog.com/research/bdx/inflation)*

Beldex mints only about **1.62M BDX** from mining over 90 days, but a fixed **130.68M BDX** release from the Ecosystem reserve wallet lands every quarter — and one lands inside every 90-day window — so the real supply force is the reserve, not the miner. Against that, only a small **0.89M BDX** fee burn pushes back. The net is about **+1.67%** to market, and our supply monitor reads **+1.71%** for the same window — a gap of **0.04 percentage points**, well inside tolerance, so no warning chip ships. BDX is a quiet privacy chain whose inflation is set almost entirely by a calendar, not by its emission curve.

## The verdict, in one paragraph

For the 90-day window ending **Aug 2 2026**, the MrNasdog Pressure Framework reads **BDX at +1.67% net**, both realised over the last 90 days and projected forward, because a **130.68M BDX** quarterly reserve release sits in both windows. Our supply monitor reads **+1.71%** for the trailing window, a gap of **0.04 percentage points** — far under the framework's 0.5-point tolerance, so no **monitor gap** chip is attached. The two numbers agree because the monitor's own daily supply series is flat for months and then steps once by about **130M** at the quarter close, which is exactly the shape the published Ecosystem release predicts and far too large to be mining. Beldex reads as **structurally inflationary on a fixed calendar** — a coin whose dilution is scheduled, predictable, and dominated by one recurring event.

## Sell pressure: where new BDX comes from

Sell #1 — protocol inflation — is the mining coinbase, and read live from the chain on **Aug 2 2026** it is a flat **6.25 BDX** per block at roughly one block every 30 seconds. Across about 259,200 blocks that comes to **1.62M BDX** over 90 days. Beldex is a CryptoNote-lineage privacy layer-1 in the Monero to Loki and Oxen tradition, running masternode proof-of-stake, and its emission is an uncapped tail with no halving, so this stream is steady quarter after quarter. Importantly, the 6.25 figure is the whole coinbase — not just the masternode share — so there is no hidden governance emission stacked on top of it.

Sell #2 — vesting unlocks — is the entire story, at **130.68M BDX**. The Ecosystem Development reserve wallet releases a fixed 130.68M every quarter-end, and the eighteenth such release fired on **Jun 30 2026**, entirely from that wallet, with the Seed and VC wallet releasing nothing. Because the reserve is readable, the framework books what actually left the wallet rather than a paper entitlement, and here the released amount equals the scheduled amount — the full tranche reached the market. The next release lands **Sep 30 2026**, inside the forward window, so the row carries 130.68M on both the trailing and forward views. That is roughly eighty times the size of mining, which is why Beldex's inflation is set by a calendar.

Sell #3 — Foundation and unscheduled unlocks — is **zero** as a booked value, because every reserve release runs on the published quarterly calendar already captured in Sell #2; there is no evidence of an off-schedule deployment in the window. Sell #4 — long-term locked or bankruptcy — is **zero** because Beldex has no bankruptcy estate, trustee schedule or court-ordered distribution. The overhang those reserve wallets represent is real and large, and it is enumerated in the Foundation section below rather than forecast into a row.

## Buy pressure: where new BDX goes

Buy #2 — protocol fee burn — is the only non-zero buy row, at about **0.89M BDX** over 90 days. Beldex Name Service registration and renewal fees, together with flash-transaction fees, are sent to an address whose key is unknown and are permanently destroyed; the all-time burn counter stood at about **11.48M BDX** on **Aug 2 2026**. It is a genuine deflationary mechanism, and the BNS Marketplace launched in May 2026 should slowly lift it, but at 0.89M it is a rounding error against the 130.68M reserve release — it offsets less than one percent of the quarter's new float.

The other three buy rows are empty. Buy #1 — programmatic buyback — is **zero**; an old 2023 buyback-and-burn promotion left no open-market buying in this window, and the project's own Q2 2026 recap lists burns only. Buy #3 — Foundation buy — is **zero** because the team releases reserve supply into the market rather than accumulating from it. Buy #4 — new long-term lock — is **zero** because masternode collateral of 10,000 BDX unlocks on exit and is treated as liquid stake, not a lock that removes supply. With only a sub-1M burn on the buy side, nothing in the design can offset the quarterly release.

## Foundation and overhang

Beldex carries a large, clearly identified team-controlled overhang. After the **Jun 30 2026** release the Ecosystem Development reserve wallet still held about **1,607.76M BDX**, and the Seed and VC wallet held about **214.5M BDX**; beyond those two published addresses there is a further roughly **246.68M BDX** of non-circulating supply that the project classifies as circulating but the market data does not. Together that is more than **2,000M BDX**, or over a quarter of the current float, sitting in reserve. The Ecosystem wallet drains on the published quarterly calendar at 130.68M per release, and both reserve wallets are refreshed on the official quarterly post and a bi-weekly wallet walk. The trigger to watch is simple: if either reserve wallet's balance falls between refreshes by more than the scheduled tranche, that extra outflow enters Sell #3 at the next refresh.

## How BDX compares to other privacy coins

BDX belongs to the **privacy-coin** class — the CryptoNote family that runs from Monero through Oxen to Beldex — but its supply profile is unusual within it. Monero has no premine and no foundation reserve; its inflation is pure tail emission, a small, permanent, uncapped subsidy with nothing scheduled behind it. Beldex shares the uncapped tail, but its emission is tiny, and its real dilution comes from a premined reserve released on a fixed quarterly calendar. In inflation terms that makes Beldex look less like Monero and more like a **scheduled-unlock token**: a coin whose float grows in large, dated steps from a treasury rather than smoothly from a block reward.

Against exchange tokens with quarterly buyback-and-burn programmes, Beldex is the mirror image. Those coins use a revenue stream to remove supply on a schedule and can run net-deflationary; Beldex uses a reserve to add supply on a schedule and runs net-inflationary, with only a small BNS fee burn pushing the other way. Against uncapped proof-of-stake L1s that mint forever to pay stakers, Beldex's mining is far gentler — 1.62M over 90 days is a fraction of a percent — but the reserve release more than makes up the difference. The honest read is that Beldex's inflation is not an emission-curve story at all; it is a treasury-release story, and it will stay that way until the Ecosystem wallet is exhausted.

## What to watch in the next 90 days

First and most important, the **Sep 30 2026** quarterly Ecosystem release: if it fires at the usual 130.68M it holds the net near +1.67%, and any change to the quantum would move the whole reading. Second, the reserve balances reported in the next official quarterly post — a release larger than 130.68M, or an unexpected Seed and VC release, would push value into Sell #3. Third, the live block reward, which should stay at **6.25 BDX**; any deviation would mean the emission code changed at a hard fork. Fourth, the BNS burn pace, which the May 2026 marketplace launch should lift — a materially faster burn is the only near-term force that could soften the net. Fifth, whether the gap between the chain's classification and the market's circulating figure keeps holding, since that is the denominator this page divides by.

## Summary

The MrNasdog Pressure Framework reads BDX at about **+1.67%** net over the next 90 days, from roughly **1.62M BDX** of mining plus a fixed **130.68M BDX** quarterly reserve release, against only a **0.89M BDX** fee burn. The structural mechanism is not the emission curve but the calendar: a premined Ecosystem reserve drips 130.68M into the float every quarter, and one release lands in every window, so dilution is scheduled and predictable. The key risk is the remaining reserve — more than **2,000M BDX** still to release over future quarters — which will keep the coin structurally inflationary until it runs dry. Beldex is uncapped, but its near-term supply story is dominated by a treasury on a fixed release schedule, lightly offset by a growing but still small BNS burn.

*MrNasdog Pressure Framework analysis of BDX, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 2 2026.*

---
title: "BSV Inflation Analysis · July 2026 · Mixed flows, supply roughly steady"
description: "MrNasdog Pressure Framework read of Bitcoin SV (BSV): ~40.3K BSV / 90D of mining, no buyback and no burn. Framework +0.20% net, monitor +0.22% — 95.5% of the cap mined."
canonical_url: "https://mrnasdog.com/research/bsv/inflation"
tags: ["crypto", "bsv", "bitcoin-sv", "proof-of-work"]
published: true
---

> Originally published at **[mrnasdog.com/research/bsv/inflation](https://mrnasdog.com/research/bsv/inflation)** by MrNasdog.

# BSV Inflation Analysis · July 2026 · Mixed flows, supply roughly steady

Bitcoin SV (BSV) mints about **40.3K BSV** every 90 days from a fixed proof-of-work block subsidy of **3.125 BSV**, and absorbs none of it — the BSV buy ledger is empty. Framework reading: **+0.20% net** on a **20.06M** circulating base against Bitcoin SV's **21M** hard cap, with **95.5%** of all BSV that will ever exist already mined.

## The verdict, in one paragraph

For the 90-day window ending July 2026, the framework reads **BSV at +0.20% net inflation**, and projects the same **+0.20%** over the next 90 days — the Bitcoin SV block subsidy does not change again until the halving near block 1,050,000 in 2028. The inflation monitor reads **+0.22%** over the same window, a gap of just **0.02 percentage points**, far inside the half-point tolerance, so no monitor-gap chip is shown. Bitcoin SV is a quiet chain: one mint, no offset, no discretion, and almost nothing left to issue.

## Sell pressure: where new BSV comes from

There is exactly one source. Sell #1 (protocol inflation) booked **~40.3K BSV**. Bitcoin SV pays a **3.125 BSV** coinbase subsidy per block, the fifth halving era that began at block 840,000, and the framework does not take the nominal ten-minute block target on trust — it counts the blocks Bitcoin SV miners actually found. Over the window the chain moved from block 946,703 to block 959,600, which is **12,897 blocks** in exactly 90.0 days, or about **143.3 blocks per day** against the 144 nominal. That is a half-percent shortfall, not a surplus: realised BSV issuance came in slightly under the schedule, at 40.3K rather than the 40.5K a nominal reading would have booked. Block pacing was stable throughout — 142.9, 143.4 and 144.0 blocks per day across the three thirty-day segments — so the forward projection carries the same rate.

The other three sell rows are zero, and each for a structural reason. Sell #2 (vesting unlocks) is **0** permanently: Bitcoin SV split from Bitcoin Cash on Nov 15 2018 as a fair-launch fork, so every BSV in existence came from a block subsidy — there was no premine, no token sale, no team allocation and therefore no vesting schedule to unlock. Sell #3 (Foundation and unscheduled unlocks) is **0**: the BSV Association is a Swiss non-profit funded by its backers rather than by a protocol coin allocation, and it publishes no BSV treasury wallet, so there is no reserve with a release cadence. Sell #4 (long-term locked or bankruptcy) is **0** as a flow, though it is the one row on the Bitcoin SV page carrying a real overhang, covered below.

## Buy pressure: where new BSV goes

Nowhere. The Bitcoin SV buy ledger is empty by design, and this build confirmed the most important zero on-chain rather than assuming it. Buy #2 (protocol fee burn) is **0**: reading a recent Bitcoin SV coinbase directly showed a single output of **3.1250641 BSV** — the 3.125 subsidy plus that block's transaction fees, paid together to the miner. Bitcoin SV destroys nothing; there is no base-fee burn, and because BSV fees run at roughly a satoshi per byte, they are a rounding error against the subsidy in any case. Buy #1 (programmatic buyback) is **0**: Bitcoin SV has no protocol revenue stream and no treasury contract that could fund one. Buy #3 (Foundation buy) is **0** — no accumulation programme has been announced by the BSV Association or any related entity. Buy #4 (new long-term lock) is **0**: Bitcoin SV is pure proof-of-work, with no staking, no masternode collateral, and no lockup contract that could take BSV off the market. Nothing in the mechanism can make the BSV reading negative.

## Foundation and overhang

There is no team-controlled treasury to enumerate for Bitcoin SV — the fair-launch fork left no premine, no ICO wallet and no foundation allocation. One overhang does exist, and it sits outside the project entirely: the **Mt. Gox rehabilitation estate** holds roughly **142,846 BSV**, duplicated from the estate's 142,846 Bitcoin Cash when the November 2018 fork created Bitcoin SV. The trustee's rehabilitation plan honours claims in fiat, Bitcoin and Bitcoin Cash, and states that other crypto assets are to be liquidated into cash — which makes the estate's BSV a disposal candidate rather than a distribution. No dated BSV sale has been disclosed, the repayment deadline currently runs to **Oct 31 2026**, and that date falls outside the next 90 days, so the framework books the row at zero and tracks it. The position is opaque: there is no published estate address to read, so it is monitored through trustee announcements. If that holding moves between refreshes, the outflow enters Sell #4 at the next refresh.

## How BSV compares to other hard-cap PoW chains

Bitcoin SV shares its monetary policy exactly with Bitcoin: 21 million coins, a subsidy halving every 210,000 blocks, a ten-minute block target. The difference that matters to an inflation reading is how far along the curve each chain sits. Bitcoin SV has mined **95.5%** of its cap with roughly 939K BSV left, so its issuance is already down to about a fifth of a percent per quarter and will keep stepping down. Litecoin, on a similar fair-launch hard-cap model, is around 92% mined and runs closer to half a percent per quarter; Dash, at roughly two-thirds mined, runs hotter still. Among hard-cap proof-of-work chains, Bitcoin SV is at the quiet end of the curve — the halving model has already done most of its work.

The sharper contrast is with uncapped or fee-burning chains. An Ethereum-style base-fee burn can push a chain net-negative when activity is high; Bitcoin SV has no burn at all, so its reading can never go below zero no matter how many transactions the chain processes — and Bitcoin SV processes a lot of them, which raises miner fee revenue without removing a single coin. Exchange tokens that run quarterly buybacks can manufacture deflation from revenue; Bitcoin SV has no revenue to buy with. Against tail-emission chains like Monero, which mint a small fixed amount forever, Bitcoin SV is the opposite trade: a firm ceiling, but an issuance rate that is still positive today and only reaches zero decades out. The honest label for Bitcoin SV is structurally, permanently mildly inflationary, with the rate on a fixed downward staircase.

## What to watch in the next 90 days

First, the Mt. Gox trustee: the repayment deadline stands at **Oct 31 2026**, and any announcement of how the estate's 142,846 BSV is disposed of would be the single largest supply event this page could book — that quantum is more than three times a full quarter of Bitcoin SV mining. Second, Bitcoin SV block pacing: hashrate on a small SHA-256 chain can drift, and a sustained move away from 143 blocks per day would move the realised issuance a few percent either way. Third, node software: the Chronicle upgrade activated Apr 7 2026 at block 943,816 and changed script limits, not issuance, and the Teranode rollout is a throughput programme — but any Bitcoin SV consensus change should be re-read for monetary effects. Fourth, the halving at block 1,050,000 remains roughly 90,000 blocks and 21 months away, around 2028, so it is a calendar note rather than a watch item. Nothing else on the Bitcoin SV surface can move this reading.

## Summary

Bitcoin SV is a fair-launch, hard-capped proof-of-work chain emitting **~40.3K BSV per 90 days** from a **3.125 BSV** block subsidy, with an empty buy ledger and no project-controlled treasury. The framework reads **+0.20% net** for the last 90 days and the same for the next 90; the inflation monitor agrees at **+0.22%**, a 0.02-point gap. The key risk is external rather than protocol-level: the Mt. Gox estate's ~142,846 BSV is earmarked for liquidation with no published date. With **95.5%** of the 21M BSV cap already mined and no burn, buyback or lock anywhere in the mechanism, Bitcoin SV supply drifts up slowly, predictably, and with almost nothing left to give.

---

*MrNasdog Pressure Framework analysis of BSV, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 27 2026.*

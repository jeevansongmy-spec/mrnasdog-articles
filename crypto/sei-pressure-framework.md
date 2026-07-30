---
title: "SEI Inflation Analysis · July 2026 · Supply growing, projected to keep growing"
description: "A MrNasdog Pressure Framework read of Sei (SEI): a release schedule mints 44.5M SEI in 90 days at 494,505 a day, with no buyback and no burn. Framework reads +0.66% net."
canonical_url: "https://mrnasdog.com/research/sei/inflation"
tags: ["crypto", "sei", "sei-network", "layer1"]
published: true
---

*Originally published at [mrnasdog.com/research/sei/inflation](https://mrnasdog.com/research/sei/inflation).*

Sei has one supply engine and no brake. Its release schedule mints exactly **494,505 SEI** once per day — **180M SEI** a year — to pay staking rewards, adding about **44.5M SEI** over the last 90 days, while there is **no buyback and no burn** to remove any of it. The Pressure Framework reads **+0.66% net** — mildly inflationary at a steady scheduled pace. Our supply monitor reads about **+0.01%**, a gap of roughly **0.65 percentage points**, because the market-data supply feed it uses is frozen at **6.733B SEI** while the chain has actually minted to **9.198B**.

## The verdict, in one paragraph

For the 90-day window ending Jul 31 2026, the Pressure Framework reads **SEI at +0.66% net**. Sell pressure is **44.5M SEI** of scheduled minting, buy pressure is **zero**, against a circulating base of **6.733B SEI**. Our supply monitor reads only about **+0.01%**, a gap of roughly **0.65 percentage points**, so a **monitor-gap** flag ships on the SEI overview. The gap is not a disagreement about mechanism — it is a frozen data feed: the monitor derives supply from market cap over price, and that figure has been pinned at exactly **6.733B SEI**, two-thirds of the 10B cap, across every daily snapshot in the window, even though the release schedule minted new SEI the whole time. Reading Sei's own nodes, total supply is **9.198B SEI** and rising by **494,505 SEI** every day. SEI is best characterised as **steadily inflationary by schedule, with no burn to offset it** — a slow, predictable drift rather than a cliff.

## Sell pressure: where new SEI comes from

Sell #1, protocol inflation, is **44.5M SEI**, and it is the entire sell side. Sei mints new SEI through a release schedule that funds staking rewards and hands out the ecosystem reserve. The important detail is timing: reading the chain block by block, supply is flat on every block except one daily step of exactly **494,505 SEI**. That daily amount times **364** is **180M SEI** a year — the release fires once per day, not per block, a distinction that trips up any reading that multiplies a daily figure by the block rate. Over the 90-day window that daily mint adds about **44.5M SEI**, and because the rate held constant across the whole window, the trailing pace and the live pace are the same.

The remaining sell rows are all **zero**. Sell #2, vesting unlocks, is zero as a realised figure even though Sei's team, investor and foundation allocations vest into **2029**. Unlock trackers quote a scheduled release of roughly **55.56M SEI** a month per two-billion bucket — about **262.8M SEI** of team-and-investor vesting over 90 days — but on the chain itself, total supply rose only by the daily mint above, with no separate monthly cliff. Those tokens were minted long ago and unlock inside the existing supply, so the framework counts the realised on-chain flow rather than the calendar entitlement; the still-locked buckets are tracked as overhang instead. Sell #3, foundation and unscheduled unlocks, is zero because no discretionary open-market sale was observed. Sell #4, long-term locked or bankruptcy, is zero: there is no Sei estate, no trustee and no court-ordered SEI distribution.

## Buy pressure: where new SEI goes

Every buy row is **zero**, and that is the defining fact about SEI supply. Buy #1, programmatic buyback, is zero because Sei runs no buyback — the foundation has floated the idea in community discussion, but nothing is live and nothing removed SEI during the window. Buy #2, protocol fee burn, is zero because Sei has no burn built into the protocol: every transaction fee is paid out to validators rather than destroyed, so activity on the network does not shrink the supply the way an EIP-1559-style base-fee burn would. Buy #3, foundation buy, is zero because no Sei Foundation open-market purchase has been disclosed. Buy #4, new long-term lock, is zero because staking is a delay, not a lock: bonded SEI can be withdrawn after an unbonding period and counts as circulating the whole time. With nothing on the buy side, the daily mint runs unopposed.

## Foundation and overhang

Sei's tracked overhang is large but slow. The first piece is the **ecosystem reserve** still to be minted toward the 10B cap — roughly **0.8B SEI** — which is exactly what the daily release is drawing down. The second is the pre-minted but still-locked **team, investor and foundation** buckets, together the scheduled **262.8M SEI** of 90-day vesting, held in accounts that unlock on a calendar into 2029. Both are re-read on every rebuild, and if a discretionary balance falls between refreshes — a foundation wallet selling, or an unlock actually reaching the market as new float — the outflow enters Sell #3 at the next refresh. Neither showed a discretionary sale in the trailing year, which is why Sell #3 is zero rather than a projected number.

## How SEI compares to other uncapped-emission L1s

The first comparison is schedule versus control loop. Some proof-of-stake chains set issuance with a bonded-ratio target, so the inflation rate floats with how much is staked; Sei does not. Its release is a fixed calendar — a set number of SEI every day regardless of staking participation — which makes the sell side unusually predictable but also immune to the kind of self-correction a target-bonded model provides. The pace does not fall because more people stake; it falls only when the schedule itself steps down.

The second comparison is burn versus no burn. Chains like the fee-burning smart-contract platforms or the exchange tokens with quarterly buybacks have a real mechanism pulling supply back down, and on a busy day they can print net-negative supply. Sei has neither: fees go entirely to validators and there is no protocol burn. That places SEI firmly in the pure-emission camp, where the only thing that can offset new supply is a future governance decision to add a burn or a buyback — capacity that later throughput upgrades could enable, but which does not exist today.

The third comparison is what the market data shows. Many tokens carry heavy vesting calendars whose monthly cliffs are the headline risk; SEI's subtler issue is that its published circulating figure has frozen at exactly two-thirds of the cap, **6.733B SEI**, while the chain quietly minted past **9.198B**. An observer trusting the headline supply would read SEI as flat when it is in fact drifting up every day. The framework reads the chain, not the frozen feed, which is the whole reason the two numbers disagree by more than half a point.

## What to watch in the next 90 days

First, whether any governance proposal adds a buyback or a burn — the only thing on this ledger that could turn the buy side non-zero and start offsetting the daily mint. Second, whether the release schedule steps down at a period boundary; the daily **494,505 SEI** is constant within a schedule period, and a documented step would re-base the forward reading. Third, the team and investor vesting into **2029** — if those unlocks begin visibly reaching the market as new float rather than sitting locked, that flow enters Sell #3. Fourth, whether the widely-quoted circulating figure un-freezes from **6.733B**; the day the market data catches up to the real **9.198B**, the monitor gap on this page collapses on its own. Fifth, any foundation transparency post disclosing a discretionary SEI sale.

## Summary

The Pressure Framework reads SEI at **+0.66% net** over 90 days and projects the same for the next 90. The structure is simple: a fixed release schedule mints **494,505 SEI** once per day, about **44.5M SEI** a quarter, and there is **no buyback and no burn** to remove any of it, so supply drifts steadily upward. The key risk is not a vesting cliff but the absence of any offset — SEI is inflationary by schedule until governance adds a brake — and the ceiling is the **10B** hard cap the chain is minting toward, now at **9.198B**. The market-data supply feed, frozen at **6.733B**, understates all of this, which is why our monitor reads near flat while the chain is not.

*MrNasdog Pressure Framework analysis of SEI, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 31 2026.*

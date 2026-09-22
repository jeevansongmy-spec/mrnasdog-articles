---
title:         "SKY Inflation Analysis · September 2026 · Supply was growing · trend cooling"
description:   "SKY supply was growing, trend cooling: +0.53% in 90 days as the Sky treasury paid stakers 204.2M SKY and bought back 80.5M. Next 90 days read −0.03%."
canonical_url: "https://mrnasdog.com/research/sky/inflation"
tags:                    ["crypto", "sky", "makerdao", "defi"]
published:     true
---

Originally published at [SKY Inflation Analysis · September 2026 · Supply was growing · trend cooling](https://mrnasdog.com/research/sky/inflation).

# SKY Inflation Analysis · September 2026 · Supply was growing · trend cooling

SKY supply was growing and the trend is cooling. Sky mints no new SKY, yet the Pressure Framework reads SKY at **+0.53%** over the last 90 days, because the Sky treasury paid stakers **204.2M SKY** while the Smart Burn Engine bought back only **80.5M SKY**. After the Sep 13 2026 governance change, the buyback outpaces the staking payouts, so the next 90 days read **−0.03%**. The total SKY supply is capped by governance rather than code, and it fell for the first time in over a year on Sep 13 2026.

## The verdict, in one paragraph

Against a circulating base of **23,425.0M SKY**, the framework books **204.2M SKY** of sell pressure and **80.5M SKY** of buy pressure over the trailing 90 days, a net of **+0.53%**, and projects **−0.03%** for the next 90 days. The inflation monitor reads **+0.60%** for the same window, a gap of **0.07 percentage points**, well inside the framework's 0.5-point tolerance, so the overview ships with no warning. The two agree because the counted SKY float is total supply minus one wallet, the Sky treasury. The label for SKY is **a buyback-funded staking token whose float growth has just stalled**.

## Sell pressure: where new SKY comes from

It does not come from minting. The SKY token contract created no new SKY in the window; total supply went from **23,462.7M SKY** to **23,459.8M SKY**, down, not up, and the two contributor vesting streams that are allowed to mint SKY both ended before the window opened. The mint function is still live and held by Sky governance, so the ceiling is a policy, not a fixed number in the code.

Sell #1, protocol inflation, is **204.2M SKY**: the SKY staking reward. Stakers in the Sky staking engine earn SKY paid out of the Sky treasury, the only balance kept out of the circulating count, so each payout lands in the float for the first time. The treasury sent 18 transfers to the reward pool over the window, on a stream governance resets every month. The latest reset, executed on **Sep 13 2026**, set it at **143.2M SKY** per 90 days, below July's pace of **286.7M SKY** per 90 days but above August's **96.9M SKY**, and that is the forward figure.

Sell #2, vesting unlocks, is **0**: there is no team or investor vesting left on SKY. Sell #3, Foundation and unscheduled unlocks, is **0**, because the only pot outside the float is the treasury, and every coin it released is already counted in Sell #1. Sell #4, long-term locked or bankruptcy, is **0**: SKY has no bankruptcy estate. The MKR to SKY upgrade sits as Sell #5 at **0**. Old MKR holders swapped **5,454 MKR** for **125.5M SKY** in the window, at 24,000 SKY per MKR minus a late-upgrade penalty that rose from 4% to 5% on Sep 13 2026. That SKY already sits in the upgrade pool and is already counted as circulating, so an upgrade adds nothing.

## Buy pressure: where new SKY goes

Buy #1, programmatic buyback, is **80.5M SKY**. The Sky Smart Burn Engine takes a share of USDS protocol revenue and buys SKY in small clips from the main SKY/USDS pool, **1,226** purchases this window. Every clip lands in the Sky treasury, outside the counted float. The pace rose twice. On Aug 17 2026 governance cut the gap between purchases from about 3.8 hours to about one hour, and on Sep 13 2026 cut it again to about 42 minutes. The new pace spends about **10.2M USDS** per 90 days and has bought SKY at a rate of **150.1M SKY** per 90 days since the change, the forward figure.

Buy #2, protocol fee burn, is **0**, and this row needs care, because a burn did happen. On **Sep 13 2026** Sky destroyed **2.86M SKY**, the first fall in SKY total supply in over a year. Under Sky's new treasury rules, 45 parts of each 55 bought go to stakers and 10 parts are burned. But the burned SKY came from the treasury, from coins the buyback had already taken off the market. Counting it again would count the same SKY twice.

Buy #3, Foundation buy, is **0**: no Foundation or team wallet bought SKY. Buy #4, new long-term lock, is **0**. Staked SKY rose from **10,035.4M** to **10,320.1M SKY**, but staked SKY can be withdrawn and is already counted as circulating, so staking removes nothing from the float.

## Foundation and overhang

The main overhang is the Sky treasury itself, which held **34.9M SKY** at the end of the window, down from **161.4M SKY** at the start. The buyback fills it and the staking rewards drain it, and it is read on chain at every rebuild. The second item is the pool of collected MKR upgrade penalties, **37.5M SKY** sitting in the upgrade contract. It is already counted as circulating and has not been spent or burned; burning it would be a real removal. If the treasury balance or the penalty pool falls between refreshes by more than the published streams explain, that outflow enters Sell #3 at the next refresh.

## How SKY compares to other buyback tokens

SKY sits with the revenue-funded buyback tokens, next to exchange tokens and perp-DEX tokens that route fees into open-market purchases. Those usually burn or lock what they buy, so their readings can go clearly negative. Sky buys SKY into its treasury and pays most of it back out as staking rewards, so the effect on the float is only the gap between the two. That is why SKY reads near zero even though its buyback runs every 42 minutes.

A proof-of-stake chain pays stakers with newly minted coins at a set rate, sell pressure whatever happens to revenue. SKY pays stakers with coins bought from revenue and sized each month, so the reward shrinks when revenue falls.

The weak point of the loop is timing. The monthly reward is sized in SKY using the prior month's average price, while the buyback spends a set amount of USDS at today's price. When SKY rises, the buyback gets fewer SKY and the payout stays the same, so the loop leaks into the float. At about **$0.0716** per SKY the two would match exactly.

## What to watch in the next 90 days

First, the monthly Sky settlement vote, which resets both the staking-reward stream and the buyback pace from the prior month's revenue; the October vote will replace the **143.2M SKY** stream. Second, **Dec 12 2026**, when the current reward stream runs out if no vote renews it first; **132.1M SKY** of it is still to be paid. Third, the next treasury burn after the Sep 13 2026 burn of **2.86M SKY**. Fourth, the MKR to SKY upgrade penalty, due to rise from 5% to 6% around **Dec 2026**, with **84,771 MKR** still not upgraded. Fifth, the SKY price, since a price above **$0.0716** tips the forward reading back to positive.

## Summary

The MrNasdog Pressure Framework reads SKY at **+0.53%** over the trailing 90 days and **−0.03%** projected forward: supply was growing, and the trend is cooling. Sky mints no new SKY; the float grew because the Sky treasury paid **204.2M SKY** in staking rewards while its buyback brought in only **80.5M SKY**. Since the Sep 13 2026 change the buyback slightly outpaces the payouts, but the balance depends on monthly votes and on the SKY price. The ceiling is governance, not code: the mint function is live, and the treasury that funds the rewards now holds only **34.9M SKY**.

MrNasdog Pressure Framework analysis of SKY, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 23 2026.

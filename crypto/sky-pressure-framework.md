---
title:         "SKY Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "SKY supply is roughly steady: the Sky treasury paid stakers 196.66M SKY while buybacks took back 84.91M, +0.48% net in 90 days, +0.07% next. No SKY is minted."
canonical_url: "https://mrnasdog.com/research/sky/inflation"
tags:                    ["crypto", "sky", "makerdao", "defi"]
published:     true
---

Originally published at [SKY Inflation Analysis · September 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/sky/inflation).

# SKY Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

The MrNasdog Pressure Framework reads SKY, the staking and governance token of Sky (formerly MakerDAO), at **+0.48% net** over the last 90 days and **+0.07%** for the next 90 — mixed flows, supply roughly steady. No new SKY is minted: the Sky treasury paid stakers **196.66M SKY** while the Smart Burn Engine bought **84.91M SKY** back into that same treasury, and since the Sep 13 2026 executive vote the two flows almost cancel. The inflation monitor reads **+0.53%**, a gap of **0.06 percentage points**, so no warning chip is needed.

## The verdict, in one paragraph

Over the 90 days from Jul 1 to Sep 29 2026, the SKY float grew by a net **111.75M SKY**, or **+0.48%** of the **23.43B SKY** counted as circulating. The inflation monitor, which reads the same classified float, shows **+0.53%** over its own 90 days; the gap of **0.06pp** is well inside the half-point tolerance, so the page carries no ⚠ chip. For the next 90 days the reading falls to **+0.07%**: the treasury is set to pay stakers **143.21M SKY**, and buybacks at the current pace would pull about **126.38M SKY** back at today's price. SKY is a **treasury-recycling token**: its supply moves only when the treasury pays out faster than the buyback refills it.

## Sell pressure: where new SKY comes from

Protocol inflation — the staking reward — is the one row that carries weight, at **196.66M SKY** over 90 days. Sky does not mint SKY for stakers. It pays them from the protocol treasury, a wallet the circulating count leaves out, through a vesting stream that feeds the SKY staking rewards once a week. Because the treasury sits outside the count, every SKY it pays out is new to the market even though total supply does not rise. The stream is reset at each monthly executive vote from the previous month's revenue; the Sep 13 2026 reset set it to **143.21M SKY per 90 days**, about **1.59M SKY a day**, and that rate carries the forward column.

Vesting unlocks are **0**. The contributor vesting streams from the Maker years have all run out, the one SKY stream that could mint new tokens finished in June 2025, and no mint happened anywhere in the window. The foundation and unscheduled unlocks row is also **0**: the treasury is the only balance outside the count, and its scheduled payout is already the staking reward. The long-term locked or bankruptcy row is **0** — there is no estate, and the **10.32B SKY** in the staking engine can leave with no exit fee but was always counted as circulating.

A fifth row covers the MKR to SKY upgrade, at **0**. Each old MKR still becomes **24,000 SKY**, minus a late-upgrade penalty that rose from 4% to **5%** on Sep 13 2026. In the window **5,728 MKR** was upgraded and **131.78M SKY** paid out, but that SKY was created in advance and already sits inside the circulating count, so the upgrade adds nothing new to the market. About **84,456 MKR** has not upgraded yet.

## Buy pressure: where new SKY goes

The programmatic buyback is the only buy row with a value: **84.91M SKY** bought with **5.40M USDS** of protocol income over 90 days, in 1,394 small purchases on the open market. The Smart Burn Engine sends every coin it buys to the treasury, outside the circulating count, so each purchase takes SKY off the market. Its pace was raised twice in the window, on Aug 17 and Sep 13 2026; since the second change it spends about **108,650 USDS a day**, which buys about **126.38M SKY** over the next 90 days at today's price of **$0.0774**. A higher SKY price means fewer coins bought for the same dollars.

The protocol fee burn books **0**, although a real burn happened. On Sep 13 2026 the treasury burned **2.86M SKY**, the first cut to SKY's total supply in more than a year, and burns now follow each monthly vote at **10/55** of the month's buyback. Those coins were already bought back and counted when they left the market, so burning them removes nothing more from the float. Foundation buy is **0** — all buying runs through the engine. New long-term lock is **0**: staking grew by **232.31M SKY** this window, but staked SKY stays inside the circulating count and can leave without a wait.

## Foundation and overhang

The Sky treasury is the one tracked overhang that matters. It held **147.49M SKY** on Jul 1 2026 and holds **32.88M SKY** now — the payouts ran ahead of the buybacks for most of the window. It is both the buyback's destination and the source of every staking reward, and at the current reward rate its balance alone covers about three weeks of payouts; the rest must come from new buybacks. The upgrade contract holds **37.83M SKY** of collected upgrade penalties plus about **2.03B SKY** reserved for MKR that has not upgraded; both are inside the circulating count, and moving the penalties to the treasury or burning them would count as a buy. The two staking reward pots hold **117.27M SKY** and **19.57M SKY** waiting to be claimed, also inside the count. We read each balance from the chain at every rebuild. If the treasury's balance falls between rebuilds by more than its scheduled reward payout, that extra outflow enters the foundation row at the next rebuild.

## How SKY compares to other DeFi governance tokens

Most proof-of-stake tokens pay stakers by minting new coins, so their supply rises every block. Ethereum, for example, created about 261K ETH for validators over a recent 90 days against a fee burn near 3K ETH. SKY pays stakers the same way on the surface — a steady reward stream — but funds it from a treasury the buyback keeps refilling, so its total supply does not rise at all and the float grows only when payouts outrun purchases.

Against governance tokens with a pure buyback-and-burn, SKY keeps less of what it buys off the market. In the old Maker design, surplus bought MKR and destroyed it. Today only **10/55** of the SKY bought stays out of the market for good; the other **45/55** goes back to stakers. That makes the buyback mostly a way to pay stakers in SKY instead of a supply cut, which is why the net reading sits near zero instead of falling.

Against tokens that share revenue only in stablecoins, SKY does both: **45%** of the capital that reaches the Smart Burn Engine step goes to stakers as USDS, and **55%** buys SKY. The USDS half never touches SKY's supply, which leaves the SKY half as the only lever on the float.

## What to watch in the next 90 days

The Oct 8 2026 executive vote resets the staking reward stream and the buyback pace from September's revenue; a larger reward than buyback tips the forward reading back up.

The same vote burns the September share of the buyback — about **6.95M SKY** on purchases so far — which cuts total supply but books 0 here, because those coins are already outside the count.

The treasury balance of **32.88M SKY** is thin against a payout of about **1.59M SKY a day**; if buybacks slowed, the payouts would run it down within weeks.

An Atlas change merged on Sep 17 2026 lets the split between SKY and USDS staking rewards move to keep the two rates equal; a shift toward SKY rewards would raise the sell side.

The late-upgrade penalty on MKR steps up by one point every three months, next to about 6% around December 2026, and the current reward award ends on Dec 12 2026 unless renewed.

## Summary

The MrNasdog Pressure Framework reads SKY at **+0.48% net** over the trailing 90 days and **+0.07%** over the next 90: the Sky treasury paid stakers **196.66M SKY** and the Smart Burn Engine bought back **84.91M SKY**, with no new SKY minted and no vesting left. The structural mechanism is a recycling loop — protocol income buys SKY into a treasury outside the float, and the treasury pays most of it back out to stakers, burning only a tenth-share each month. The key risk is balance: a larger reward stream, a higher SKY price that buys fewer coins, or a drop in protocol income would push the float up again. SKY has no coded supply cap — governance can still mint — but nothing has been minted since June 2025, total supply stands at **23.46B SKY**, and each monthly burn lowers it a little more.

*MrNasdog Pressure Framework analysis of SKY, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

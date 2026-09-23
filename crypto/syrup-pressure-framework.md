---
title:         "SYRUP Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "SYRUP supply roughly steady: 0.00% net over 90 days. No mint, no burn, and Maple's 4.03M SYRUP buyback stays counted. 22.0M earned SYRUP is still unclaimed."
canonical_url: "https://mrnasdog.com/research/syrup/inflation"
tags:          ["crypto", "syrup", "maple", "defi"]
published:     true
---

Originally published at [SYRUP Inflation Analysis · September 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/syrup/inflation).

# SYRUP Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

SYRUP supply held steady over the last 90 days and is projected to stay steady over the next 90. The Pressure Framework records **0** SYRUP of sell pressure and **0** of buy pressure, a net of **0.00%** both ways, while the monitor reads **−2.15%**. Maple Finance minted nothing, burned nothing, and the one wallet left out of the circulating count did not move; the Maple buyback of **4.03M SYRUP** sits in a wallet that is still counted. The one open risk is **22.0M SYRUP** already earned by the emission schedule and not yet claimed.

## The verdict, in one paragraph

Against a circulating base of **1,167.27M SYRUP**, the framework books **0** of sell pressure and **0** of buy pressure over the 90 days to **Sep 23 2026**, a net of **0.00%**, and projects **0.00%** for the 90 days to **Dec 22 2026**. The inflation monitor reads **−2.15%** for the same window, a gap of **2.15 percentage points**, which is over the 0.5-point line, so the overview carries a monitor-gap warning. The gap is fully explained, and it is not a flow. Total SYRUP was **1,244.68M** at both ends of the window. On **Jun 25 2026** the monitor’s circulating count left out about **51.5M SYRUP**; today it leaves out **77.41M**, which is Maple’s strategic fund wallet, and that wallet did not send or receive a single SYRUP in the window. The same coins simply read **25.7M** lower. The label for SYRUP this quarter is a governance token with a quiet float and a pending treasury claim.

## Sell pressure: where new SYRUP comes from

Sell #1, protocol inflation, is **0**. SYRUP is minted by an emission module that earns new tokens for Maple every second and releases them only when Maple claims them. The module has run three rate windows since October 2024; the current one pays about **52.3M SYRUP a year**, and a fourth window already set on chain drops the rate to zero from **Oct 1 2026**. No claim happened in this window: total supply read **1,244.68M SYRUP** at both ends, no mint was logged, and the module’s last claim is still **Apr 22 2026**, when **28.55M SYRUP** was minted. The supply figure is a live number, not a constant — it moved by exactly that amount on that day. What remains is a claim in waiting: **22.0M SYRUP** is earned and unclaimed today, rising to **23.2M** when the schedule stops. Maple has claimed six times since January 2025, with gaps of 55 to 189 days and no published date, so the framework does not project a date. When the claim comes, the coins land in the Maple treasury contract, which the circulating count includes, and that single event would add about **1.9%** to the float.

Sell #2, vesting unlocks, is **0**. SYRUP has no investor or team unlock left on a calendar, and the old MPL to SYRUP conversion closed on **May 21 2025**; the conversion contract holds no SYRUP, and MPL supply did not change. Contributor grants are paid through a vesting contract holding **15.77M SYRUP**, but that contract already counts as circulating, so claims from it do not add to the float.

Sell #3, Foundation and unscheduled unlocks, is **0**, and this is the row where the denominator matters most. Maple’s DAO safe received the April claim from the treasury on **Jun 26 2026** and then passed **9.0M SYRUP** to its operations wallet, which paid contributors and topped up the grant vesting contract. Across all its wallets, Maple sent about **11.4M SYRUP** outward this quarter. None of it crossed the line the framework measures, because every one of those wallets is already inside the circulating count. Sell #4, long-term locked or bankruptcy, is **0**: SYRUP has no bankruptcy estate, trustee or court order.

## Buy pressure: where new SYRUP goes

Buy #1, programmatic buyback, is **0** — and a buyback did run. Maple bought **2.5M SYRUP** in June, **0.85M** in July and **0.68M** in August, **4.03M SYRUP** in all, and the MIP-021 vote that passed in July 2026 now sets the buyback at 10% to 30% of monthly revenue for six months. The bought SYRUP was not burned. It arrived in a Maple fund wallet that the circulating count still includes, so the purchase moved coins from one counted balance to another and took nothing out of the measured float. That fund wallet holds **2.33M SYRUP** today.

Buy #2, protocol fee burn, is **0**. SYRUP has no fee burn, and both places a burn could appear were read at both ends: total supply did not fall, and the two burn addresses held the same tiny balances on **Jun 25 2026** and **Sep 23 2026**. Buy #3, Foundation buy, is **0**: the strategic fund wallet that sits outside the count received nothing. Buy #4, new long-term lock, is **0**. Staking rewards ended in November 2025 and stakers are leaving: staked SYRUP fell from **210.50M** to **160.36M**. Staked SYRUP counts as circulating either way.

## Foundation and overhang

The only SYRUP outside the circulating count is Maple’s strategic fund cold wallet, holding **77.36M SYRUP**, unchanged since December 2025. It is read from the chain at every rebuild. Inside the count, but under Maple’s control, sit the DAO safe at **23.09M**, a reserve safe at **48.62M**, the buyback wallet at **2.33M**, the operations wallet at **2.68M**, a grants safe at **0.68M** and the grant vesting contract at **15.77M**; the treasury contract itself is nearly empty. The largest overhang is the unclaimed **22.0M SYRUP** in the emission module. If the strategic fund cold wallet’s balance falls between refreshes, that outflow enters Sell #3 at the next refresh; if the emission claim lands, it enters Sell #1.

## How SYRUP compares to other buyback governance tokens

SYRUP sits among governance tokens whose protocol earns real revenue and returns part of it through buybacks. The strongest members of that group burn what they buy, or send it to a wallet outside the float, so every purchase shows up as supply leaving the market. Maple does neither. Its buyback is real and rules-based, but the tokens stay in a counted wallet, so the buyback supports price without shrinking the measured float. A token that burns its buyback would read negative in a quarter like this one; SYRUP reads flat.

On issuance, SYRUP is closer to a DeFi token with a finite emission tail than to a proof-of-stake chain with open-ended inflation. Its emission is not paid per block to validators; it accrues to one treasury and is minted in lumps when Maple decides to claim. That makes SYRUP’s supply look perfectly flat for months and then step up in a day. The schedule on chain ends on **Oct 1 2026**, which is a stricter end point than most uncapped chains offer, although governance could add new windows later.

## What to watch in the next 90 days

First, the emission claim: **22.0M SYRUP** is earned and unclaimed, and a claim before **Dec 22 2026** would add about 1.9% to the float in one day. Second, **Oct 1 2026**, when the current schedule sets issuance to zero; any new window added by a governance vote would restart it. Third, the monthly MIP-021 buybacks, and whether Maple ever burns them or moves them out of the counted fund wallet. Fourth, the strategic fund cold wallet at **77.36M SYRUP**, the only balance whose movement would change this reading directly. Fifth, the monitor’s own circulating count, which has changed four times since May 2026 without a single matching coin movement.

## Summary

The MrNasdog Pressure Framework reads SYRUP at **0.00%** over the trailing 90 days and **0.00%** projected forward: mixed flows, supply roughly steady. Maple Finance minted nothing, burned nothing and kept its **4.03M SYRUP** buyback in a wallet that is still counted, while the one wallet outside the count did not move. The key risk is the **22.0M SYRUP** the emission schedule has already earned, which Maple can claim at any time. The ceiling is the schedule itself, which stops new issuance on **Oct 1 2026** unless governance adds more.

MrNasdog Pressure Framework analysis of SYRUP, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 23 2026.

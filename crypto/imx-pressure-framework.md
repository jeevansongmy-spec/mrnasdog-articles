---
title:         "IMX Inflation Analysis · October 2026 · Supply growing · projected to keep growing"
description:   "IMX is inflationary on its float: no new coins, but the Immutable treasury released 33.0M IMX in 90 days, +3.65% net, about +3.34% next. No buyback."
canonical_url: "https://mrnasdog.com/research/imx/inflation"
tags:          ["crypto", "imx", "immutable", "gaming"]
published:     true
---
*Originally published at [mrnasdog.com/research/imx/inflation](https://mrnasdog.com/research/imx/inflation)*

<!-- main-page -->
This is the long supply read. For the signal, the price drivers and the questions people ask about Immutable, see [mrnasdog.com/research/imx](https://mrnasdog.com/research/imx).

# IMX Inflation Analysis · October 2026 · Supply growing · projected to keep growing

IMX is inflationary on its tradable float even though no new IMX can ever be created. The Immutable treasury paid out **33.0M IMX** in the last 90 days, nothing was bought back or burned, and the float grew by **+3.65%**; at the treasury's 12-month pace the next 90 days add about **30.21M IMX**, or **+3.34%**. The ceiling is the **2B** hard cap, and **1.10B IMX** still sit in two treasury Safes.

## The verdict, in one paragraph

Over the 90 days from Jul 16 to Oct 14 2026, IMX supply in the market grew by **+3.65%**: **33.0M IMX** came out of the treasury and **0** went the other way, against **904.47M IMX** circulating. The monitor reads **+7.36%** for the same stretch, a gap of **3.71 percentage points**, so a ⚠ monitor gap note ships on the coin page. The reason is known: the supply figure the monitor reads sat near 842.4M IMX from Mar 31 to Aug 1 2026, then reset on Aug 13 2026 and counted in about **29.0M IMX** that had left the treasury before this window. Those were old payouts, not new coins, so our number stays at **+3.65%**, with **+3.34%** projected next. In one line: Immutable is a fixed-cap token whose float grows by treasury payouts.

## Sell pressure: where new IMX comes from

Protocol inflation is **0**. The IMX token on Ethereum has a hard cap of 2,000,000,000 coins and every one of them already exists. We called the mint function on the token contract: it refused a normal caller, and even when we gave the caller the minting role in a simulated call, the contract refused again because the cap was reached. Immutable Chain, the gaming network where IMX pays for gas, pays no block rewards, and the IMX used there is bridged from the same 2B coins.

Vesting unlocks are **0**. The IMX vesting schedules from the 2021 token launch are over. The two contracts that moved coins into the Immutable treasury in 28-day steps are empty, and the last step, about **11.03M IMX**, landed on Mar 30 2026. Unlock trackers show no scheduled IMX unlock left.

Foundation and unscheduled unlocks are the whole story: **33.0M IMX** in this window. The larger Immutable treasury Safe sent **3M IMX** on Jul 22, **5M IMX** on Aug 11 and **25M IMX** on Sep 29 2026 to Immutable's payout wallet, and its balance fell by exactly that amount. The payout wallet counts as circulating, so the coins enter the float the moment they leave the Safe. Over the last 12 months the two Immutable treasury Safes paid out **122.5M IMX**, and the larger Safe paid out in every quarter of that year. That steady pattern is why the next 90 days carry about **30.21M IMX**, the 12-month pace, rather than zero.

Long-term locked or bankruptcy supply is **0**. No court estate, trustee or long lock holds IMX. A reserve of about **1.90B IMX** on Immutable Chain exists only to back coins bridged from Ethereum, and it did not move during the window.

## Buy pressure: where new IMX goes

The programmatic buyback is **0**. Immutable runs no IMX buyback. Part of the platform's trading fees is collected in IMX and paid to IMX stakers, but those coins move from users to stakers and stay in the market.

The protocol fee burn is **0**. Gas on Immutable Chain is paid in IMX, but only the base fee is destroyed, and the base fee is 49 wei, so a full day of blocks burns far less than one IMX. The tips go to the block producer. The IMX token on Ethereum has no burn function at all.

The Foundation buy is **0**: neither Immutable treasury Safe received a single IMX in the window. The new long-term lock is also **0**. IMX staking and the bridge contract, which grew by **3.15M IMX** to **80.02M IMX**, hold coins that still count as circulating, so they take nothing out of the float. Total buy pressure: **0 IMX**.

## Foundation and overhang

The IMX overhang is large and easy to see. Two Immutable treasury Safes on Ethereum hold the coins that do not count as circulating: **721.51M IMX** in the larger Safe, which pays out every few weeks, and **374.01M IMX** in the second Safe, which last paid out on Feb 10 2026. Together they are **1.10B IMX**, more than the whole circulating supply. We read both balances on-chain at every rebuild. Immutable's payout wallet holds **24.08M IMX**, but it already counts as circulating, so its spending adds nothing new. The **1.90B IMX** reserve on Immutable Chain is a bridge mirror, which we also read at each rebuild. If either treasury Safe's balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How IMX compares to other gaming tokens

Most gaming tokens still carry new supply from two sources: a vesting calendar for teams and investors, and an emission stream for players or stakers. IMX has neither. Its vesting ended, its cap is reached, and it pays no staking emission; stakers are paid from fees. On that measure IMX looks like a finished-supply coin, much like a hard-capped chain whose last coin is already mined.

The difference is custody. A capped coin is only as fixed as the share already in the market, and for IMX that share is about **45%**. The other 55% belongs to Immutable, and the company decides when it moves. That makes IMX closer to a treasury-funded network token than to a mined coin: supply growth follows the company's spending, not a schedule. Tokens with ongoing monthly unlocks, such as Arbitrum's ARB, at least publish their dates; IMX payouts come on no calendar, which is why we project them from their 12-month pace.

IMX also has no buyer of last resort. Chains with a fee burn, like Ethereum, destroy part of every fee; IMX gas fees are so small and the base fee so low that nothing meaningful is burned. With no buyback and no burn, every coin the treasury releases has to be absorbed by market buyers.

## What to watch in the next 90 days

First, the larger Immutable treasury Safe: it paid out on Jul 22, Aug 11 and Sep 29 2026, and a payout bigger than the **25M IMX** of Sep 29 would push the next reading above our projection. Second, the second Safe, quiet since Feb 10 2026: any outflow from its **374.01M IMX** would be new float on top of the run rate. Third, Immutable's move toward its AI marketing product after the game-studio cuts reported in June 2026: if the company funds that work by spending more IMX, the treasury pace rises. Fourth, the reserve on Immutable Chain: it should only change when coins cross the bridge, so any other movement would matter. Fifth, any announcement of an IMX buyback or burn, which would open the first real buy-side row.

## Summary

IMX is inflationary on its float even with a fixed 2B cap: the Immutable treasury released **33.0M IMX** in 90 days, supply in the market grew **+3.65%**, and the 12-month pace points to about **+3.34%** over the next 90 days. Nothing is minted, nothing vests and nothing is burned or bought back, so treasury payouts are the only moving part. The key risk is the **1.10B IMX** still held in two Immutable treasury Safes, released on no public calendar. The ceiling is hard: circulating supply can never pass 2B.

MrNasdog Pressure Framework analysis of IMX, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 14 2026.

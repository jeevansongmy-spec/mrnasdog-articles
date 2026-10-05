---
title: "ETHFI Inflation Analysis · October 2026 · Supply growing · projected to keep growing"
description: "ETHFI supply is growing: no new ETHFI can be minted, but the last ether.fi team grant unlocks 17.65M ETHFI every 90 days, +1.83% net and the same next."
canonical_url: "https://mrnasdog.com/research/ethfi/inflation"
tags: ["crypto", "ethfi", "etherfi", "defi"]
published: true
---

Originally published at [ETHFI Inflation Analysis · October 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/ethfi/inflation).

# ETHFI Inflation Analysis · October 2026 · Supply growing · projected to keep growing

**ETHFI**, the governance token of **ether.fi**, is mildly inflationary on its tradable float even though no new ETHFI can ever be minted. Over the 90 days to Oct 5 2026 the last core-contributor grant released about **17.65M ETHFI** into a float of **965.35M**, while buybacks and burns removed **0**, for a net of **+1.83%**, and the next 90 days should look the same. The monitor reads **+4.09%**; the difference comes from a circulating count that was recounted twice, not from new coins. The ceiling is hard: supply is fixed at 1B, already burned down to 998,535,999, and the grant stops unlocking on Mar 18 2027.

## The verdict, in one paragraph

The MrNasdog Pressure Framework puts ETHFI's 90-day net supply change at **+1.83%** (sell 17.65M, buy 0, over 965.35M circulating), with the same **+1.83%** projected for the next 90 days. The inflation monitor reads **+4.09%** for the same stretch, a gap of **2.26 percentage points**, which is more than our 0.5-point limit, so a ⚠ monitor gap note ships on the coin page. We walked the gap: the circulating count behind the monitor jumped about 44.3M on Jul 17 2026 and 45.1M on Aug 17 2026, briefly showing more ETHFI than exist, then was cut back to about 965.3M on Aug 27 2026, while on-chain supply never moved. Our number stays. In one line: **a fixed-supply token whose float still grows from one vesting team grant**.

## Sell pressure: where new ETHFI comes from

**Protocol inflation is 0, permanently.** The ETHFI contract created all 1,000,000,000 coins once, at launch, and has no mint function at all; it is a plain, non-upgradeable ERC-20 with a burn function. So every coin that will ever exist already exists, and supply can only go down. It has gone down: earlier ether.fi buybacks in 2025 burned 1,464,001 ETHFI, leaving 998,535,999 on chain at both ends of this window.

**Vesting unlocks are 17.65M ETHFI in 90 days**, and they are the whole sell side. ether.fi set aside **214.7M ETHFI** (21.47%) for core contributors on a 3-year schedule with a 1-year cliff from the Mar 18 2024 launch. One third came free at the cliff in March 2025; the other two thirds, 143.13M, unlock in a straight line until **Mar 18 2027** — about **196,073 ETHFI a day**, or 17,646,575 every 90 days. No on-chain vesting contract holds the rest: the grant was paid out to holder wallets in February and April 2025, so the published schedule is what decides the release. A check backs it up: on-chain supply minus the circulating count leaves 33.19M not yet counted as circulating, and the grant's unvested remainder on Oct 5 2026 is 32.16M — the same pile, 3% apart. The much larger investor grant (33.74%) finished unlocking on Mar 18 2026, when the last monthly payouts landed.

**Foundation and unscheduled unlocks are 0.** The ether.fi treasury moved coins this window — 20M ETHFI on Oct 4 2026 into the Safe that holds the new rewards buffer, and 1M on Oct 2 2026 from a second treasury Safe — but treasury coins already count as circulating, so a move between them adds no new float. **Long-term locked or bankruptcy is 0**: there is no estate, trustee or long lock behind ETHFI.

## Buy pressure: where new ETHFI goes

**The programmatic buyback books 0, though it is real.** In a vote that closed on Sep 3 2026, ether.fi holders approved weekly ETHFI purchases funded by card, swap and staking revenue, about **$1.33M a month** when it was proposed, with lending and perps revenue to be added later. The bought ETHFI is kept in the Foundation treasury, paid to stakers or sent to users as card cashback. Every one of those places is inside the circulating float, so the buying moves coins from sellers to the treasury or to users without taking them out of circulation.

**The protocol fee burn is 0 for this window.** We read supply and the dead address at both ends: 998,535,999 and 0.66 ETHFI both times. The 2025 burns proved the burn path works; the current program simply keeps what it buys. **Foundation buy is 0**: a separate treasury program of up to $50M, approved in November 2025 and active only below $3, reported no spending this quarter. **New long-term lock is 0**: staked ETHFI rose by 9.23M to 110.6M, helped by card memberships that reward staking, but staked ETHFI can be withdrawn and still counts as circulating.

## Foundation and overhang

We track six ETHFI piles that the team side controls. The DAO treasury Safe holds **153.2M ETHFI**, down from 173.2M after the Oct 4 2026 transfer; the Safe that received it now holds **20.0M**, the rewards buffer the Sep 3 2026 vote allowed for cashback when bought ETHFI falls short. A second treasury Safe holds **12.9M**. The largest team-grant wallet holds **101.5M** and has never moved since February 2025. A small operating Safe holds **2.1M**, and the staking pot that receives buyback payouts holds **110.6M**. All of them already count as circulating, so none adds to the ledger today. We read every one of these balances on chain at each rebuild; if any of them falls between refreshes, the outflow goes into the Foundation and unscheduled unlocks row at the next refresh.

## How ETHFI compares to other DeFi governance tokens

ETHFI sits in the group of fixed-supply DeFi governance tokens: one mint at launch, no staking rewards paid in new coins, and a float that grows only while insider grants unlock. Lido's LDO is the closest older example — also a fixed 1B supply, but its insider vesting ended years ago, so its float barely grows. ETHFI is still in the tail of that phase: one grant left, about 32.2M ETHFI, and then the sell side should drop toward zero after Mar 18 2027.

The contrast with emission-funded tokens is the mechanism, not the price. Many staking and restaking tokens pay holders in newly minted coins, so their supply grows every year with no end date. ETHFI pays its stakers and card users with coins bought on the market, which moves coins around inside the float but creates none.

The contrast with buy-and-burn tokens matters too. Some DeFi tokens destroy what they buy, which shrinks supply and shows up as a negative number in this framework. ETHFI did that in 2025, burning 1.46M, but its 2026 program keeps the coins in the treasury or hands them to users. Until the bought ETHFI is burned or locked away, the buyback supports demand without lowering the supply count.

## What to watch in the next 90 days

**The grant keeps unlocking every day** through Jan 3 2027, about 17.65M ETHFI in the window, with the final day on Mar 18 2027.

**The buyback dashboard**, promised with the Sep 3 2026 vote, will show ETHFI bought versus ETHFI paid out as rewards; if the program switches to burning, the burn row turns negative.

**The 20M rewards buffer**, moved into its own Safe on Oct 4 2026: it stays inside the float, but a fast drain would show heavy cashback selling.

**The circulating count itself**: it has not moved since Aug 27 2026 while the grant unlocked, so a catch-up step of a few million ETHFI is possible, and we will check it against the chain.

## Summary

ETHFI is a fixed-supply token — 1B created once, no mint function, 998,535,999 left after past burns — yet its tradable float still grows about **+1.83% every 90 days** because the last core-contributor grant unlocks about 196,073 ETHFI a day until Mar 18 2027. ether.fi's weekly buybacks are real but book 0 here, because the coins stay in the treasury or go to stakers and card users instead of being burned. The key risk is that grant: about 32.2M ETHFI is still to come. The ceiling is fixed — once the grant ends, new supply from the token itself goes to zero.

*MrNasdog Pressure Framework analysis of ETHFI, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 5 2026.*

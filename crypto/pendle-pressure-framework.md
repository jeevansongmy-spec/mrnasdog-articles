---
title:         "PENDLE Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "PENDLE supply grows with no new minting: treasury wallets and expiring vote-locks released 2.48M PENDLE in 90 days, +1.43% net, and the buyback removed none."
canonical_url: "https://mrnasdog.com/research/pendle/inflation"
tags:                    ["crypto", "pendle", "defi", "inflation"]
published:     true
---

Originally published at [PENDLE Inflation Analysis · September 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/pendle/inflation).

# PENDLE Inflation Analysis · September 2026 · Supply growing · projected to keep growing

**PENDLE supply is growing without any new minting.** Over the 90 days to Sep 29 2026, **2.48M PENDLE** left wallets that sit outside the circulating count — pool rewards paid by the governance treasury, a treasury send to an exchange, a team payment and expiring vote-locks — while the fee-funded buyback of **952,552 PENDLE** removed nothing, because every bought coin goes to stakers. Net supply rose **+1.43%**, and the next 90 days project **+1.22%**. The one ceiling is the treasury itself: about 43.64M PENDLE sits in three team-run wallets, and 63.55M more waits in the old vote-lock.

## The verdict, in one paragraph

The MrNasdog Pressure Framework reads PENDLE at **+1.43%** net over the last 90 days: 2.48M PENDLE of sell pressure and 0 of buy pressure against 173.62M circulating. The inflation monitor, which measures the change in circulating supply from outside, reads **+1.56%** over the same stretch. The gap is **0.14 percentage points**, inside the 0.5-point tolerance, so no warning chip is shown and the ledger stands as read. For the next 90 days the ledger projects **2.11M PENDLE** of new float, **+1.22%**. Pendle is a **zero-mint token with a leaking treasury**: the supply cap never moved, but the float grows every month as coins held outside it are spent.

## Sell pressure: where new PENDLE comes from

**Protocol inflation — about 900,000 PENDLE.** The PENDLE token still carries a weekly emission schedule, now at a terminal rate of about 2% a year, but nobody has claimed it since Mar 24 2025. Total supply read 281.53M PENDLE at both ends of the window, and the token's own emission counter did not move. Pool rewards under the Algorithmic Incentive Model are paid instead from the governance treasury, which sent 400,000 PENDLE on Jul 20 2026 and 500,000 on Sep 13 2026 to the wallet that funds the reward pools. Because the treasury is outside the circulating count, those 900,000 coins are new float, and the forward column holds the same rate.

**Vesting unlocks — 0.** Every team and investor allocation finished vesting in September 2024, and unlock trackers list Pendle as fully unlocked. What the team still holds sits in its own wallet and is counted in the next row.

**Foundation and unscheduled unlocks — about 670,000 PENDLE.** The governance treasury sent 600,000 PENDLE to an exchange on Sep 8 2026, the same size as its May 13 2026 send, and the team wallet paid out 70,000 on Aug 26 2026. The exchange sends come roughly every four months, so the next one would land after this window; the team payments have come every 61 or 62 days, so two more of about 70,000 are expected, around late October and late December — **140,000 PENDLE** forward.

**Long-term locked — 906,616 PENDLE.** vePENDLE, the old two-year vote-lock, stopped taking new locks on Jan 29 2026 when staked PENDLE replaced it. Each old lock ends on a date written into the contract. In this window 965,095 PENDLE reached its end date and holders withdrew 906,616, about 94%. The same schedule puts **1.07M PENDLE** due in the next 90 days, led by 644,616 on Dec 24 2026 and 205,008 on Nov 12 2026. There is no bankruptcy estate.

## Buy pressure: where new PENDLE goes

**Programmatic buyback — 0 net, 952,552 PENDLE bought.** Since the sPENDLE launch, 80% of Pendle's yield and swap fees buy PENDLE on the open market every hour. The buyback contract took in 952,552 PENDLE this window and passed every coin to the staking contract, where it is paid to stakers as sPENDLE. Staked PENDLE can be withdrawn in 14 days and is counted as circulating, so the buyback moves coins from sellers to stakers without taking them out of the float. It is real buying — it just does not shrink supply.

**Protocol fee burn — 0.** Burning is switched off in the PENDLE contract, total supply did not fall, and no coins reached a dead address. **Foundation buy — 0.** The treasury, team and ecosystem wallets only sent PENDLE out; none received any. **New long-term lock — 0.** The old vote-lock takes no new coins, and sPENDLE, now 35.36M PENDLE, sits inside the float.

## Foundation and overhang

Five pools of PENDLE could still reach the market. The **governance treasury** holds 19.75M PENDLE and pays both the pool rewards and the exchange sends. The **ecosystem fund** holds 16.12M; it last moved on Apr 30 2026 and did not move this window. The **team wallet** holds 7.77M and pays out every two months. The **old vote-lock** holds 63.55M, of which about 1.99M has already reached its end date but has not been withdrawn; its last lock ends in March 2028. And the token can still **mint about 9.62M PENDLE** of unclaimed weekly emissions at any moment, growing by about 110,500 a week. The last time that happened, on Mar 24 2025, the new coins went straight into the governance treasury, so a mint would enlarge the treasury first and reach the float only when spent.

Every one of these balances is read from the chain at each rebuild. If any of them falls between refreshes, the outflow enters the Foundation and unscheduled unlocks row at the next refresh.

## How PENDLE compares to other DeFi governance tokens

Most DeFi governance tokens that turned on buybacks did so to shrink supply. Pendle made a different choice: the PENDLE it buys is paid to stakers, so the buyback works like a dividend in coins rather than a burn. A DEX token that burns what it buys, or sends it to a wallet outside the float, books that buying as a real cut in supply; Pendle books zero, even though it bought nearly a million PENDLE in 90 days.

On the sell side, Pendle looks less like an uncapped emission chain and more like a treasury-run project. Its token contract has not minted in 18 months, so the headline supply is flat, but the float still grows because treasury, team and vote-lock balances outside the float are spent or released. Tokens whose rewards come from a fresh mint show the growth in total supply; Pendle shows it only in the circulating count, which is why the old vote-lock and the treasury matter more here than the emission schedule.

## What to watch in the next 90 days

**Nov 12 2026 and Dec 24 2026:** the two largest vote-lock expiry weeks in the window, 205,008 and 644,616 PENDLE, followed by 1.13M on Dec 31 2026 just after it. **Late October and late December 2026:** the team wallet's next two payments if its 61-day rhythm holds. **Around January 2027:** the next treasury send to an exchange if the four-month rhythm holds; an earlier send would raise the forward figure. **Any call to claim the unminted emissions** — about 9.62M PENDLE today — which would enlarge the treasury in one step. And the fee level: lower fees mean a smaller buyback, though the buyback does not change the supply reading either way.

## Summary

PENDLE is inflationary on its float, not on its cap: total supply sat at 281.53M PENDLE for the whole window, yet **2.48M PENDLE** left the treasury, team wallet and old vote-lock, lifting circulating supply **+1.43%** in 90 days, with **+1.22%** projected next. The fee-funded buyback bought 952,552 PENDLE but pays it to stakers who still count as circulating, so it offsets none of that growth. The key risk is the treasury's pace and the 9.62M PENDLE of unclaimed emissions it can mint; the ceiling on the slow leak is the 43.64M held in the three team-run wallets plus the 63.55M still in the vote-lock.

*MrNasdog Pressure Framework analysis of PENDLE, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

---
title:         "LDO Inflation Analysis · September 2026 · Supply was shrinking · trend softening"
description:   "LDO supply was shrinking: −1.04% in 90 days as a Lido DAO buyback moved 8.68M LDO into a treasury outside the float. −0.27% next; 48.9M unlocks Jan 1 2027."
canonical_url: "https://mrnasdog.com/research/ldo/inflation"
tags:                    ["crypto", "ldo", "lido", "defi"]
published:     true
---

Originally published at [LDO Inflation Analysis · September 2026 · Supply was shrinking · trend softening](https://mrnasdog.com/research/ldo/inflation).

# LDO Inflation Analysis · September 2026 · Supply was shrinking · trend softening

LDO supply was shrinking and the shrink is softening. The Pressure Framework reads the Lido DAO token at **−1.04%** over the last 90 days and **−0.27%** projected for the next 90, against a monitor reading of **−1.00%**. Sell pressure was **0**: no LDO was minted, unlocked or paid out of the treasury. Buy pressure was **8.68M LDO**, almost all of it a holder-approved buyback that swaps treasury stETH for LDO and keeps the LDO in the Lido DAO treasury — a wallet that sits outside the counted float, so every bought LDO genuinely leaves the market. The constraint is a fixed **1,000M LDO** supply that only a DAO vote can raise, and a **48.9M LDO** contributor lock that opens on **Jan 1 2027**.

## The verdict, in one paragraph

Against a circulating base of **834.2M LDO**, the framework books **0** of sell pressure and **8.68M LDO** of buy pressure over the trailing 90 days, a net of **−1.04%**, and projects **−0.27%** for the next 90 days from the one buyback delivery that is already bought and dated. The inflation monitor reads **−1.00%** for the same window, a gap of **0.04 percentage points**, well inside the framework's 0.5pp tolerance, so the LDO overview carries no monitor-gap warning. The two readings agree because the Lido DAO treasury, where the buyback LDO lands, is outside the counted float: the circulating figure is total supply minus the treasury minus locked contributor vestings, and that identity rebuilt from named wallets closes to the last unit. The label for LDO is **a governance token shrinking by treasury buyback, with a dated unlock waiting behind it**.

## Sell pressure: where new LDO comes from

Sell #1, protocol inflation, is **0**. LDO has no emission schedule. Total supply read exactly **1,000M LDO** at both ends of the window, and the token's own supply record — a list that gains a new entry every time LDO is minted or burned — held the same six entries at both ends. That record is live storage, not a constant in the code, so a flat reading here is a real measurement. New LDO can still be minted: the Lido DAO Voting contract holds the mint permission, and the record last changed on **Dec 25 2025**, when 48.9M LDO was burned and minted back in a single step to re-lock contributor tokens. Because a vote could mint, this row is watched rather than closed.

Sell #2, vesting unlocks, is **0**, and this is the row most summaries get wrong. The 2020 launch vesting of LDO finished long ago, and unlock trackers list LDO as fully unlocked. They miss a newer lock. In December 2025 a DAO-enabled re-vesting contract re-locked contributor LDO, and in January 2026 **48.9M LDO** was placed under vesting across ten contributor wallets. The circulating figure excludes it. On chain, every one of those ten vestings starts on Jan 1 2026 and fully unlocks at a single moment, **Jan 1 2027** — no gradual release before it. Nothing unlocked in this window, and the locked balance was identical at both ends. The unlock lands ten days after the next 90-day window closes, so it is outside both numbers on this page, but when it opens it adds about **5.9%** to the tradable LDO float in one day.

Sell #3, Foundation and unscheduled unlocks, is **0**. The Lido DAO treasury sent out no LDO in 90 days; every transfer in and out of it was traced and the sum matches its balance change exactly. The contributor grant committee, which used to draw LDO from the treasury every month or two, last did so on **Mar 2 2026**. Sell #4, long-term locked or bankruptcy, is **0**: there is no estate, trustee or court-ordered distribution attached to LDO.

## Buy pressure: where new LDO goes

Buy #3, the Foundation buy, carries almost everything at **8.62M LDO**. In April 2026 Lido DAO holders approved spending up to **10,000 stETH** from the treasury to buy LDO, in rounds of 1,000 stETH executed by the Lido Growth Committee through the Lido Ecosystem Foundation, each under a published LDO/ETH price cap. Two deliveries landed in the window: **6.47M LDO on Jul 8 2026** and **2.15M LDO on Aug 25 2026**. The bought LDO is not burned; it is sent back to the Lido DAO treasury. On most tokens that would make a buyback a within-float shuffle, but here the treasury is outside the circulating figure, so each delivery removes LDO from the market one for one. The third round filled only 320 of its 1,000 stETH in its first window because the Growth Committee will not pay above its cap.

Buy #1, the programmatic buyback, is **0.006M LDO**. NEST, Lido's automatic buyback, went live in August 2026 in treasury mode: it spends half of staking revenue above about **$40M a year**, up to **$50K a day** and **$10M a year**, and sends the LDO to the treasury. It filled one order, 1 stETH for 6,354 LDO on Aug 13 2026. Revenue has run below that bar since, and its budget now reads about **−$554K**, so it cannot spend until revenue recovers. Buy #5, a revoked grant returned, adds **0.057M LDO**: on Jul 31 2026 a contributor vesting contract was cancelled and its unvested LDO went back to the treasury.

Buy #2, protocol fee burn, is **0**. LDO has no burn, and both places one could appear stayed flat: total supply at 1,000M and the dead address at 5.2 LDO. Buy #4, new long-term lock, is **0**: LDO has no staking or vote-lock, and the contributor re-lock predates the window and did not grow.

## Foundation and overhang

The largest LDO overhang is the Lido DAO treasury itself, holding **116.9M LDO**, up from 108.2M at the start of the window purely from buyback deliveries. It is read on chain at every rebuild. The second is the **48.9M LDO** contributor lock, which is not discretionary at all: it opens on a fixed date, Jan 1 2027. The third is the Growth Committee's buying wallet, which holds **2.26M LDO** already bought in the current round and due back to the treasury when the round closes on Sep 29 2026. The fourth is new: on **Sep 22 2026** holders approved a market-making loan of up to **7.5M LDO** from the treasury to keep LDO listed on centralized exchanges. It is contingent, not yet switched on, and when drawn it would move treasury LDO into the float. If the treasury balance falls between refreshes — through that loan, a grant draw or any other payment — the outflow enters Sell #3 at the next refresh.

## How LDO compares to other treasury-buyback governance tokens

Most governance-token buybacks do less than they appear to. A buyback that burns, like an exchange token's quarterly auto-burn, removes supply outright. A buyback that parks coins in a team wallet the market already counts removes nothing from the float, however large the headline. LDO sits in a third, less common group: Lido DAO buys and holds, but it holds in a treasury the circulating figure has always excluded. So LDO gets the float effect of a burn without destroying anything, and the DAO keeps the option to spend those coins later. That option is the catch. A burn cannot be undone; a treasury balance can be lent to a market maker or granted to contributors, and the Sep 22 2026 market-making vote shows it can happen.

On issuance, LDO is stricter than uncapped staking tokens that mint several percent a year, and closer to a fixed-supply token: nothing is minted on a schedule and the ceiling is 1,000M. It is looser than a token with mint rights renounced, because the Lido DAO vote can still mint. And compared with a token still working through a team vest, LDO's remaining lock is small but concentrated: 48.9M LDO on one date instead of a monthly drip, which makes Jan 1 2027 the single most important date for LDO supply in the coming year.

## What to watch in the next 90 days

First, **Sep 29 2026**, when the third buyback round closes and the 2.26M LDO already bought should return to the treasury; any extra fill before then adds to the buy side. Second, whether the Growth Committee publishes a fourth 1,000-stETH round — about 7,000 stETH of the approved budget would remain, and none of it is in the forward number. Third, the market-making loan of up to 7.5M LDO approved on Sep 22 2026: if it is switched on, that LDO leaves the treasury and counts as sell pressure. Fourth, NEST: its budget must climb back above zero before it buys again, which needs staking revenue above about $40M a year. Fifth, the **Jan 1 2027** unlock of 48.9M LDO, just past this window, which will dominate the following reading.

## Summary

The MrNasdog Pressure Framework reads LDO at **−1.04%** over the trailing 90 days and **−0.27%** projected forward: supply was shrinking, trend softening. The mechanism is a holder-approved Lido DAO buyback that swaps treasury stETH for LDO and keeps it in a treasury outside the counted float, while no LDO is minted, burned or unlocked. The key risk is that the removal is reversible and dated: the treasury can lend or grant its LDO, and a **48.9M LDO** contributor lock opens on Jan 1 2027. The ceiling is a fixed **1,000M LDO** that only a DAO vote can raise.

MrNasdog Pressure Framework analysis of LDO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 23 2026.

---
title:         "PYTH Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "PYTH supply is flat: 0.00% net over 90 days and next. No PYTH can be minted, the final 2.125B cliff opens May 20 2027, and DAO buybacks stay in the float."
canonical_url: "https://mrnasdog.com/research/pyth/inflation"
tags:          ["crypto", "pyth", "solana", "oracle"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/pyth/inflation](https://mrnasdog.com/research/pyth/inflation)*

# PYTH Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

PYTH supply is roughly steady: the MrNasdog Pressure Framework reads a net change of **0.00%** over the last 90 days and **0.00%** for the next 90, against **+0.02%** on the inflation monitor. Pyth Network can never mint another PYTH, no vesting cliff falls inside either window, and the **3.62M PYTH** the Pyth DAO bought back stays inside the circulating count. The one large supply event left is the final **2.125B PYTH** cliff on **May 20 2027**.

## The verdict, in one paragraph

Over the 90 days to Sep 29 2026, PYTH sell pressure was **0** and buy pressure that left the market was **22,093 PYTH** of holder burns, so the framework net is **0.00%** of the **7.87B PYTH** in circulation, and the forward reading is also **0.00%**. The inflation monitor, which estimates supply from market value and price, reads **+0.02%**. The gap is **0.02 percentage points**, well inside the 0.5-point line, so no data-conflict flag is shown. Pyth Network is a capped token between cliffs: a quiet float today, with one scheduled wall of supply in May 2027.

## Sell pressure: where new PYTH comes from

Protocol inflation is **0**, and it is permanent. The PYTH mint on Solana has no mint authority left: the right to create new tokens was removed on-chain, and the token program has no way to give it back. Total supply can only stay at 10B or fall. Pyth Network once paid staking rewards to holders who backed data publishers, but those rewards are paused, and the unused reward pool of about 849K PYTH was sent back to the DAO Treasury on Jul 23 2026 — coins that already existed, not new ones.

Vesting unlocks are **0** in both windows. At launch on Nov 20 2023, 1.5B PYTH was liquid and 8.5B was locked, to open in four equal cliffs of **2.125B** at 6, 18, 30 and 42 months. The third cliff fired on May 20 2026, before this window opened, which brought the unlocked supply to 7.875B. The fourth and last cliff lands on May 20 2027, well after the next 90 days end.

Foundation and unscheduled unlocks are **0**. The Pyth DAO Treasury took in coins this window and sent none out, and every wallet the DAO or its councils use holds coins that are already unlocked and already counted as circulating. Long-term locks and bankruptcy are **0**: there is no estate, trustee or court schedule anywhere in the PYTH supply.

## Buy pressure: where new PYTH goes

The programmatic buyback is real but books **0**. Each month the Pyth DAO sends a share of its network revenue to a council multisig, which buys PYTH on the open market and returns it to the DAO Treasury. In this window the treasury received **1.80M PYTH** on Jul 6, **1.14M** on Aug 3 and **0.67M** on Sep 2 — **3.62M PYTH** in total. The DAO keeps those coins and is not allowed to sell them without a new vote, but it does not burn them either. Because the treasury sits inside the circulating count, the buyback moves coins from sellers to the DAO without taking any out of the float. The monthly buys have also been shrinking: about 2.75M PYTH in March 2026, 1.80M in June, 1.14M in July and 670K in August.

The burn row is **22,093 PYTH**, and none of it comes from fees. Pyth Network collects its fees in dollars, SOL and PYTH and keeps them; nothing in the protocol destroys PYTH. What does get destroyed is PYTH that holders burn from their own wallets. Read burn by burn across the window, **317** burns removed 22,093 PYTH, and two single burns on Aug 7 and Aug 27 2026 made up 20,271 of it. That is about 0.0003% of supply, and the forward column holds the same amount. Since launch, holders have burned **40,638 PYTH** in total.

Foundation buying is **0**: outside the DAO programme, no foundation or company buys PYTH for the project. The company that sells Pyth's paid data service paid the DAO its revenue share in PYTH twice this window, 7.67M on Jul 3 and 7.66M on Aug 4, but those were coins it already held. New long-term locks are **0**: staked PYTH and publisher rewards held in one-year lock accounts are still counted as circulating.

## Foundation and overhang

The largest overhang by far is the final vesting tranche: **2.125B PYTH**, 21.25% of all supply, which is the only balance outside the circulating count and opens on May 20 2027. When it opens it will add about 27% to the 7.87B float in a single day, the same shape as the May 2024, May 2025 and May 2026 cliffs. The Pyth DAO Treasury holds **38.51M PYTH** — its buybacks plus revenue paid in PYTH — and none of it moved out in the window; it is checked from the chain at every rebuild. About **84.8K PYTH** is still in the old staking reward pool. A DAO vote opened on Sep 24 2026 would let **5.46M PYTH** of May and June 2026 publisher rewards open one year after payout instead of over three years; those coins are already counted, and the new dates fall in May and June 2027. If the DAO Treasury's balance falls between refreshes, the outflow enters the Foundation and unscheduled unlocks row at the next refresh.

## How PYTH compares to other oracle and cliff-vesting tokens

Among oracle tokens, PYTH has the simplest supply engine: a hard cap of 10B, no mint and no staking emission. Chainlink also has a fixed cap, but LINK reaches the market through steady releases from a large project-held reserve rather than dated cliffs, so its float grows a little every quarter. PYTH does the opposite: nothing for eleven months, then one big step. A 90-day reading of PYTH is therefore either close to zero or very large, depending on whether a May cliff falls inside the window.

Its buyback also works differently from a burn-based token. Coins bought by a burn programme leave supply for good; the PYTH Reserve holds what it buys in a DAO treasury that is still counted as circulating. That makes PYTH closer to a treasury-accumulation model than to a deflationary one: the DAO becomes a large holder, and the float only shrinks if the DAO later votes to burn or lock those coins. Proposals to burn part of the reserve were raised on the forum in June 2026 but never passed.

## What to watch in the next 90 days

The vote on the Strategic Reserve V2 plan, opened Sep 24 2026, would turn all of the DAO's revenue share into PYTH without monthly votes, starting with about 323K USDC and 90 SOL; the coins would still be held, not burned. The tenth monthly purchase, approved in September with about 162K USDC and 45 SOL, should be reported in early October. The vote on shortening publisher-reward vesting, opened Sep 24 2026, moves 5.46M PYTH into May and June 2027. Any DAO decision to burn or lock reserve coins would be the first thing to move this reading off zero. The next scheduled supply event is the final 2.125B cliff on May 20 2027.

## Summary

PYTH supply is roughly steady at **0.00%** over the last 90 days and the next 90, because Pyth Network cannot mint new tokens and no vesting cliff falls inside either window. The Pyth DAO bought back **3.62M PYTH** with network revenue in the window, but it keeps the coins inside the circulating count, so the buyback does not shrink supply. The key risk is the final **2.125B PYTH** cliff on May 20 2027, about 27% of today's float, after which the 10B cap is fully unlocked.

*MrNasdog Pressure Framework analysis of PYTH, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

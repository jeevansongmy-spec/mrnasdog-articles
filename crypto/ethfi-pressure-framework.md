---
title:         "ETHFI Inflation Analysis · July 2026 · Supply growing, projected to keep growing"
description:   "No protocol mint: ether.fi released ~141.5M ETHFI from vesting last quarter while a buyback pays stakers instead of burning. Framework +14.5% net (monitor +17.01%, denominator gap)."
canonical_url: "https://mrnasdog.com/research/ethfi/inflation"
tags:          ["crypto", "ethfi", "etherfi", "defi"]
published:     true
---

*Originally published at [mrnasdog.com/research/ethfi/inflation](https://mrnasdog.com/research/ethfi/inflation)*

**TL;DR.** ETHFI is a fully-minted, hard-capped 1,000,000,000 token on Ethereum with no mint function, so its inflation is not emission but vesting release. Over the last 90 days roughly **141.5M ETHFI** actually left vesting and reached the market — the locked pool fell from about 168M to about 25M — while the ether.fi buyback removed **no supply**, because it hands bought-back tokens to stakers rather than burning them. That is **+14.5% net** on the current float, versus our supply monitor at **+17.01%**, a gap that is entirely a denominator convention on the same release. Only about **25M ETHFI** is left to unlock, so this number collapses next quarter.

## The verdict, in one paragraph

For the 90-day window ending Jul 29 2026 the Pressure Framework reads **ETHFI at +14.5% net**. Sell pressure is **141.5M ETHFI** of realised vesting release, buy pressure is **zero** in supply terms, against a circulating base of **973.5M ETHFI**. Our supply monitor reads the realised change at **+17.01%**, a gap of **2.48 percentage points**, which is outside tolerance and ships a monitor-gap chip on the ETHFI overview. The deep walk settles it and it is not a hidden flow: both readings agree the release is about 141.5M ETHFI, and they differ only in base — the monitor divides by the 90-day-ago supply (141.5 / 831.97 = 17.01%) while the framework divides by current circulating (141.5 / 973.47 = 14.53%), and the difference is exactly the gap. ETHFI is best characterised as a **capped restaking token finishing a heavy vesting run**.

## Sell pressure: where new ETHFI comes from

Sell #1, protocol inflation, is **zero**, and it will stay zero for good. The ETHFI contract was fully minted at a fixed 1,000,000,000 cap; there is no mint function, no staking emission and no block reward, so no new ETHFI can ever be created. Every unit of ETHFI supply pressure is therefore vesting — already-minted tokens leaving lock — which is Sell #2. That row is **141.5M ETHFI**, and it is the whole story. Reading the realised on-chain outflow rather than the calendar: the non-circulating pool fell from about 168M to about 25M over the window, arriving in three discrete monthly steps of roughly **44M** on **May 17 2026**, **Jun 17 2026** and **Jul 17 2026**, flat in between. The large investor tranche of **337.4M ETHFI** completed its two-year vest on **Mar 18 2026**, which is why the pool drained so fast this quarter. Sell #3, Foundation and unscheduled unlocks, is **zero**: the ether.fi treasury (about 216M ETHFI) and the remaining core-contributor allocation did not sell discretionary supply beyond the scheduled vesting. Sell #4, long-term locked or bankruptcy, is zero — there is no ether.fi estate, trustee or court distribution.

## Buy pressure: where new ETHFI goes

Buy #1, the programmatic buyback, is where ETHFI looks stronger than it is for a supply framework. ether.fi does run a genuine buyback — roughly **5%** of protocol revenue buys ETHFI each month, and a treasury program approved in October 2025 can deploy up to **$50M** whenever ETHFI trades below $3 (it trades near $0.41, so the trigger is live). But the destination is decisive: the bought-back ETHFI is **remitted directly to sETHFI stakers**, not sent to a burn address and not locked. Because the tokens stay in circulating supply and simply change hands from the treasury to stakers, the buyback removes **no supply** — it is real price support but it does not offset the vesting inflation, so Buy #1 books at zero for this metric. Buy #2, protocol fee burn, is zero: ether.fi burns no ETHFI at all. Buy #3, Foundation buy, is zero — the only project buying is the revenue buyback already described. Buy #4, new long-term lock, is zero: staking into sETHFI has a short exit, so staked ETHFI stays effectively liquid.

## Foundation and overhang

Two team-controlled pools are tracked. The **ether.fi treasury** holds about **216M ETHFI**, 21.62% of supply, and it funds the buyback; it has no published schedule to sell into the market, so it is unscheduled capacity rather than active sell pressure. The **core-contributor allocation** is the only bucket still vesting — about **25M ETHFI** remains locked, running into 2027, and it is the source of the forward tail in Sell #2. That 25M is also the hard ceiling on every future ETHFI unlock: once it clears, the token is fully circulating and vesting inflation ends permanently. Each balance is re-read every rebuild, and if the treasury or the remaining locked allocation releases between refreshes, that outflow enters Sell #3 at the next refresh.

## How ETHFI compares to other capped vesting tokens

The mechanism comparison that matters is emission versus vesting. Uncapped Layer-1s and many DeFi tokens keep minting — staking curves, liquidity incentives and uncapped treasuries mean their sell side never ends. ETHFI is the opposite: the 1,000,000,000 cap is enforced by the contract, not by policy, so its worst case is bounded and countable. What made this quarter look violent is that ETHFI is a young token — token generation was March 2024 — running the back half of a front-loaded unlock schedule, so a large fraction of total supply hit the float in a single quarter. That is a one-time transition, not a recurring emission, and it is nearly over.

The second comparison is burn versus redistribute. Exchange tokens that run buybacks send the purchased supply to a burn address, so the reduction is permanent and shows up in every supply feed. ether.fi buys and **redistributes**: the ETHFI it purchases is handed to sETHFI stakers, which rewards holders and supports price but keeps the tokens in circulating supply. For a price-and-yield thesis that is a feature; for a supply-and-inflation thesis it means the buyback cannot be counted as a burn, and ETHFI has no structural mechanism that shrinks its float. So ETHFI's best long-run case is flat — vesting finished, buyback recycling — not deflationary.

## What to watch in the next 90 days

First, the core-contributor vesting tail: about **25M ETHFI** remains locked and roughly **13M** of it is expected to release over the next 90 days, most likely as a monthly step around **Aug 17 2026**, after which the unlock pool is nearly exhausted. Second, whether the buyback's destination ever changes — a governance move to burn bought-back ETHFI instead of paying stakers would flip Buy #1 from zero to a real supply removal and could turn the reading net-negative. Third, whether the $50M below-$3 treasury buyback is actually drawn while ETHFI sits near $0.41. Fourth, any treasury decision to sell from the ~216M DAO holding, which is the only large unscheduled overhang left. Fifth, the point where circulating supply meets total supply and vesting inflation ends outright.

## Summary

ether.fi's ETHFI is a fully-minted, hard-capped token with no mint function, so its inflation is vesting release rather than emission. Over the last 90 days about 141.5M ETHFI actually left vesting and reached the market as the locked pool drained from roughly 168M to 25M, driven by the completion of a 337.4M investor tranche in March 2026. The revenue buyback that might have offset it removes no supply, because bought-back ETHFI is paid to stakers rather than burned. That leaves the framework at +14.5% net, with our supply monitor at +17.01% purely because the two use different denominators on the same release. The key structural fact is the ceiling: only about 25M ETHFI is left to unlock, so this is the last heavy quarter of ETHFI vesting and the number is set to collapse toward +1.3% and then to flat.

---

*MrNasdog Pressure Framework analysis of ether.fi (ETHFI), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 30 2026.*

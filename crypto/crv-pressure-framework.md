---
title: "CRV Inflation Analysis · July 2026 · Supply growing, projected to keep growing"
description: "A MrNasdog Pressure Framework read of Curve DAO (CRV): ~28.5M / 90D of declining gauge emission with no buyback and no burn. Framework +1.85% net; monitor +2.28%, gap +0.44pp — inside tolerance."
canonical_url: "https://mrnasdog.com/research/crv/inflation"
tags: ["crypto", "crv", "curve", "defi"]
published: true
---

> Originally published at **[mrnasdog.com/research/crv/inflation](https://mrnasdog.com/research/crv/inflation)** by MrNasdog.

Curve DAO's CRV grows on a preset, declining schedule and nothing else. The token is hard-capped at **3,030,303,031 CRV**, and its only new supply is an on-chain gauge emission to liquidity providers running at a fixed **316,563 CRV a day** — about **28.5M CRV** over the last 90 days. There is no buyback and no burn to offset it, so the Pressure Framework reads **+1.85% net** against our supply monitor at **+2.28%**, a gap inside tolerance. CRV is best understood as a **capped token that inflates in one direction only, on a rate that halves every four years**.

## The verdict, in one paragraph

For the 90-day window ending Jul 31 2026, the Pressure Framework reads **CRV at +1.85% net**. Sell pressure is **28.5M CRV** of gauge emission, buy pressure is **zero**, against a circulating base of **1.54B CRV**. Our supply monitor reads the realised change at **+2.28%**, a gap of **0.44 percentage points** — inside the half-point tolerance, so no monitor-gap chip ships. The small residual is the monitor's circulating feed catching up on already-emitted gauge CRV as it is claimed, not new issuance beyond the fixed schedule; both readings agree supply is growing. CRV is **inflationary by design, on a preset and declining emission**, with the next annual step-down due Aug 12 2026.

## Sell pressure: where new CRV comes from

Sell #1, protocol inflation, is **28.5M CRV**, and it is the entire supply story. Curve's token contract mints CRV to liquidity gauges at a rate read directly on-chain as **3.6639 CRV per second**, or **316,563 CRV a day**, and that rate is constant across a one-year mining epoch. Over the 90-day window that is 28.5M CRV of new supply, all of it flowing to liquidity providers who claim their gauge rewards. The rate is not discretionary and cannot be changed by any team or multisig — it is fixed in code and steps down by **2^-1/4**, roughly **15.9%**, on each anniversary. The current epoch began Aug 12 2025; the next cut, epoch 6, is due Aug 12 2026, which trims the forward 90 days to about **24.6M CRV**.

Every other sell row is **zero**. Sell #2, vesting unlocks, is zero because Curve's original 2020 distribution is fully released: the 30% to the team and investors, the 3% to employees, the 5% to pre-CRV liquidity providers and the community-reserve vest all ran on linear schedules that ended on the fourth anniversary, **Aug 13 2024**. There is no unlock calendar left. Sell #3, Foundation and unscheduled unlocks, is zero: the Curve DAO community reserve of roughly **151M CRV** is governance-controlled with no published release schedule and did not distribute into the market this window. Sell #4, long-term locked or bankruptcy, is zero — there is no Curve estate, no trustee and no court-ordered distribution.

## Buy pressure: where new CRV goes

There is no buy pressure at all, and that is the defining structural fact about CRV. Buy #1, programmatic buyback, is **zero**: Curve does not repurchase CRV. Buy #2, protocol fee burn, is **zero**: CRV has no burn mechanism and no token is ever destroyed. This is the point most often misread — Curve does distribute real revenue, but it pays trading and crvUSD fees to vote-locked holders in **stablecoin** (crvUSD and 3CRV), not by buying or burning CRV. That is a yield to lockers, not a bid under the token, so it does not enter the framework as buying power.

Buy #3, Foundation buy, is **zero**: no foundation or DAO entity has disclosed an open-market CRV purchase, and the treasury exists to fund grants rather than to support the token. Buy #4, new long-term lock, is also **zero** for the framework, and this needs a careful distinction. More than **40%** of CRV is vote-locked into veCRV for terms up to four years, which is a huge amount of supply taken out of active trading. But locked CRV is still counted as **circulating supply** — veCRV is a lock, not a redemption — so vote-locking does not shrink the denominator the framework divides by and cannot register as a removal. No new external lockup contract with an announced quantum was deployed in the window either.

## Foundation and overhang

CRV's team-controlled overhang is unusually small for a token this age, because its vesting is finished. The one tracked pool is the **Curve DAO community reserve**, about **151M CRV** or 5% of the hard cap, controlled by veCRV governance with no published release rate; it showed no distribution into the market this window. Beyond that, the only supply still to appear is the **625M CRV** of headroom between the current minted supply and the cap — and that is released solely through the scheduled gauge emission already counted in Sell #1, not by any discretionary unlock. The community reserve is re-checked every rebuild, and if its balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How CRV compares to other capped-emission tokens

The mechanism CRV most resembles is Bitcoin's: a hard cap with a preset emission that halves on a fixed clock. Where Bitcoin halves its block subsidy every four years in one step, CRV tapers by about **15.9%** every single year, which compounds to the same halving every four years but as a smoother glide path. Like Bitcoin, the schedule is immutable and no governance vote can accelerate or refill it. Unlike Bitcoin, CRV started from a large pre-mined allocation, so it is already **2.40B of 3.03B** minted — most of the emission is behind it, and the remaining supply arrives ever more slowly.

The sharper contrast is with the buyback-driven DeFi tokens it is often grouped with. Exchange and lending tokens that run quarterly buybacks or fee burns push their net supply toward zero or negative, so their inflation reading is offset by a structural bid. CRV has no such offset by design: fees route to vote-lockers in stablecoin, so the token carries its full emission with nothing on the buy side. That makes CRV cleaner to model — there is exactly one supply input and it is deterministic — but it also means the framework reading stays positive as long as the gauge emission runs, and only the passage of time and the annual cuts bring it down. A capped, no-buyback token is not deflationary; it is inflationary at a rate that shrinks on a known schedule.

## What to watch in the next 90 days

First and most concrete, the **Aug 12 2026** epoch-6 emission cut: it drops the mint by about 15.9%, from 316,563 to roughly 266,197 CRV a day, and pulls the forward reading from +1.85% toward **+1.6%** on its own. Second, the Curve DAO community reserve — any governance vote to deploy part of the 151M CRV reserve would open Sell #3, so its balance is the main watch line. Third, any change to Curve's fee model: the fees stay in stablecoin today, but a governance decision to route value through CRV itself would be the first buy-side mechanism the token has ever had. Fourth, veCRV lock trends: while locking does not change circulating supply, a large wave of expiries returning CRV to active float would be visible in market behaviour even if the framework denominator is unchanged.

## Summary

Curve DAO's CRV is a hard-capped token whose only new supply is a preset, on-chain gauge emission to liquidity providers — about 28.5M CRV over the last 90 days at a fixed 316,563 a day, with no buyback and no burn to offset it because fees are paid to vote-lockers in stablecoin instead. That leaves the framework at +1.85% net, in line with our supply monitor at +2.28%. The key structural fact is that this emission is deterministic and declining: it steps down about 15.9% every year, with the next cut due Aug 12 2026, and the remaining 625M CRV to the 3.03B cap arrives only through that shrinking schedule. The key risk is simply that there is nothing on the buy side to turn the reading negative — CRV inflates in one direction, and only time reduces the rate.

*MrNasdog Pressure Framework analysis of Curve DAO (CRV), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 31 2026.*

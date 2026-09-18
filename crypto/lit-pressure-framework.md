---
title:         "LIT Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "Mixed flows, supply roughly steady: LIT reads +0.04% over 90 days and flat next. Lighter's buyback coins stay in the market, and its July burn hit the reserve."
canonical_url: "https://mrnasdog.com/research/lit/inflation"
tags:          ["crypto", "lit", "lighter", "perpdex"]
published:     true
---

> Originally published at **[mrnasdog.com/research/lit/inflation](https://mrnasdog.com/research/lit/inflation)** by MrNasdog.

LIT is flat: the Pressure Framework reads Lighter's token at **+0.04%** over the trailing 90 days and **0.00%** over the next 90, against a monitor reading of **−0.03%**. Lighter buys LIT back every day with its trading fees, but the bought coins stay inside the **250M LIT** tradable supply, and the **15.64M LIT** burned on Jul 10 2026 came from the ecosystem reserve, which was never tradable. The only new LIT to reach the market was **0.10M** of staking rewards from that reserve. The supply is capped at **1,000M LIT**, and half of it, **500M** for the team and investors, stays locked until a cliff in late December 2026.

## The verdict, in one paragraph

Against a circulating base of **250M LIT**, the framework books **0.10M LIT** of sell pressure and **0** of buy pressure over the trailing 90 days — a net of **+0.04%** — and **0** on both sides for the next 90 days, a net of **0.00%**. The inflation monitor reads **−0.03%** for the same window, a gap of **0.07 percentage points**, inside the framework's 0.5pp tolerance, so the overview page carries no monitor-gap warning. The two readings agree because the arithmetic closes: the whole non-tradable supply is the team and investor coins plus the ecosystem reserve, and the tradable supply grew by exactly the **0.10M** the reserve sent out. The label for LIT is a buyback token whose buyback has not yet left the market: the buying is real, but the coins it buys are still tradable.

## Sell pressure: where new LIT comes from

It does not come from minting. Sell #1, protocol inflation, is **0**: Lighter created a fixed **1,000M LIT** at launch, and the count of LIT in existence read exactly the same at both ends of the window. That count is kept in a stored value the contract can change, not a number written into its code, so an unchanged reading is a real measurement rather than a constant. Sell #2, vesting unlocks, is also **0**. The team holds 26% and investors 24%, together **500M LIT**, behind a one-year cliff from the Dec 30 2025 launch. The framework read all **262** wallets that received those coins: together they held exactly **500M LIT** at both ends of the window, so not a single insider coin reached the market.

Sell #3, Foundation and unscheduled unlocks, is **0.10M LIT**: one batch of staking rewards sent from the ecosystem reserve on Jul 3 2026. Lighter said on Jun 30 2026 that staking would now be paid from that reserve, but since mid-July the weekly rewards have come from a different place — a project wallet holding the LIT bought back in the spring. That wallet has paid out **3.03M LIT** to stakers, partners and trading campaigns and still holds **12.61M LIT**. Those payouts add nothing new, because the coins were already part of the tradable supply when they were bought and never left it. Sell #4, long-term locked or bankruptcy, is **0**: LIT has no bankruptcy estate and no court-ordered distribution.

## Buy pressure: where new LIT goes

Buy #1, programmatic buyback, is **0**, even though the buying is real. Lighter's docs say trading-fee revenue buys LIT in daily 24-hour purchases, and the coins collect in one exchange account: **2.20M LIT** on Sep 18 2026, rising while it was being read, or about **2.64M LIT** bought inside the window. But that account, and the wallet that received the spring's **15.64M LIT** pot, both sit inside the **250M** tradable count. The arithmetic proves it: the team and investor coins plus the reserve make up the entire **750M** that is not tradable, so there is no room for these wallets outside it. Coins that move from buyers to Lighter and back out to stakers never leave the market.

Buy #2, protocol fee burn, is **0**, even though a burn happened. The dead address rose from **0** to **15.64M LIT**, and it is the only place the burn shows, because the count of LIT in existence did not fall. But the burned coins came from the ecosystem reserve, and the bought-back coins went to the project wallet instead, so the tradable supply was left exactly as it was. Buy #3, Foundation buy, is **0**: the older route that bought LIT on the market to pay stakers stopped in early July. Buy #4, new long-term lock, is **0**: staked LIT can be withdrawn after three days, so staking does not remove coins for long.

## Foundation and overhang

The overhang on LIT is large, and most of it has no release calendar. The ecosystem reserve holds **234.26M LIT**, down from nearly **250M** at the start of the window, almost all of it because of the July burn; Lighter says it will fund staking, future points seasons and partnerships from it. The project wallet holding the bought-back coins has **12.61M LIT** left and is paying out every week, and the buyback account holds **2.20M LIT** waiting to be burned; both already count as tradable. A campaign pool of about **11M LIT** has been reported for trading through Robinhood Chain. Behind all of it sit the **500M** insider coins, which start to unlock in late December 2026 at about **13.9M LIT** a month for three years. Every one of these balances is read at each rebuild. If the reserve's balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How LIT compares to other perpetuals exchange tokens

LIT belongs to a growing class: exchange tokens whose trading fees buy the token on the open market. On paper, Lighter's version is one of the strongest — the docs point trading-fee revenue at daily buybacks, and since Jun 30 2026 the stated destination is a burn. That makes LIT look like the tokens of exchanges that buy and destroy, where the inflation reading can go clearly negative whenever trading is busy.

The chain shows something closer to a buy-and-hold model. The coins that were burned came from a reserve that was never tradable, while the coins that were bought went into a spending wallet and are being paid out as rewards. A buyback only shrinks the market when the bought coins end up somewhere they can never come back from. Until Lighter sends bought coins, rather than reserve coins, to the dead address, LIT reads flat, like a token that pays its stakers out of its own buybacks.

The bigger difference from mature exchange tokens is the calendar. Many of them finished their insider vesting long ago. LIT has not started: **500M** insider coins, twice today's tradable supply, begin unlocking in late December 2026 at about **13.9M LIT** a month — more than **5%** of today's tradable supply every month.

## What to watch in the next 90 days

First, the next burn: the **2.20M LIT** in the buyback account is due to be burned, and a burn of those bought coins — not reserve coins — would be the first time Lighter's buyback actually took LIT off the market. Second, the ecosystem reserve at **234.26M LIT**: any new release from it, for staking once the project wallet runs down or for a new points season, enters the sell side. Third, the Robinhood Chain trading campaign and whether it is paid from the reserve or from coins already in the market. Fourth, the buyback pace itself, which follows trading revenue. Fifth, the insider cliff: it falls just after this window, around Dec 27 2026, and each monthly unlock of about **13.9M LIT** after it equals more than **5%** of today's tradable supply.

## Summary

The MrNasdog Pressure Framework reads LIT at **+0.04%** over the trailing 90 days and **0.00%** projected forward: mixed flows, supply roughly steady. Lighter's daily fee buyback is real, but the coins it buys stay inside the tradable supply, and the **15.64M LIT** burned on Jul 10 2026 came from a reserve that was never tradable — so the only new LIT to reach the market was **0.10M** of staking rewards. The key risk is the calendar rather than the buyback: **500M** insider coins start unlocking in late December 2026, and **234.26M LIT** more sits in a reserve with no release schedule. The ceiling is a fixed **1,000M LIT** that did not change.

---

*MrNasdog Pressure Framework analysis of LIT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 18 2026.*

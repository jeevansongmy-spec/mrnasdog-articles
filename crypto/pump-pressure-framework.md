---
title: "PUMP Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description: "Supply growing, projected to keep growing: PUMP reads +25.86% over 90 days. Team wallets released 144.9B PUMP after the July cliff; the buyback burned 23.8B."
canonical_url: "https://mrnasdog.com/research/pump/inflation"
tags: ["crypto", "pump", "pumpfun", "solana"]
published: true
---

> Originally published at **[mrnasdog.com/research/pump/inflation](https://mrnasdog.com/research/pump/inflation)** by MrNasdog.

The MrNasdog Pressure Framework reads Pump.fun's PUMP at **+25.86%** over the trailing 90 days and **+0.99%** over the next 90, against an inflation monitor reading of **+34.92%**. The mechanism is an insider unlock, not issuance: after the one-year cliff on the team and investor allocations ended on **Jul 12 2026**, **144.9B PUMP** left locked team wallets and joined the tradable supply, while the buyback that spends half of Pump.fun's revenue burned **23.8B PUMP**. The constraint runs in PUMP's favour: the mint authority is null, so no new PUMP can ever be created and the **834.0B** supply can only fall.

## The verdict, in one paragraph

Against a circulating base of **468.5B PUMP**, the framework books **144.9B PUMP** of sell pressure and **23.8B PUMP** of buy pressure over the trailing 90 days — a net of **+25.86%** — and projects **+0.99%** for the next 90 days, when the unlock falls back to its published monthly size. The inflation monitor reads **+34.92%** for the same window, a gap of **9.05 percentage points**, which is over the framework's 0.5pp tolerance and ships with a monitor-gap warning on the overview page. The gap decomposes completely: **9.02pp** is base convention, because the monitor divides the rise by the circulating supply of 90 days ago, when the float was far smaller, and **0.03pp** is snapshot timing. The two readings agree on what moved: the rise in tradable PUMP plus the burn matches the framework's count of PUMP leaving locked wallets to under a thousand tokens. The label for PUMP this quarter is **a burning token swamped by its own insider unlock**.

## Sell pressure: where new PUMP comes from

It does not come from minting. PUMP is a Token-2022 mint on Solana whose mint authority and freeze authority both read null, so no wallet, contract or vote can create another PUMP. All 1T PUMP were created at launch in July 2025, and the count has only fallen since. Sell #1, protocol inflation, is **0**, and it is the one row on this page that can never change.

Sell #2, vesting unlocks, is **144.9B PUMP**, and it is the whole supply story. Pump.fun's team holds 20% of PUMP and its existing investors 13%, both behind a 12-month cliff that ended on **Jul 12 2026**, after which the published schedule releases **6.875B PUMP** a month until **Jul 2029**. The framework does not trust that calendar; it follows the tokens, and it counts each PUMP once, at the moment it leaves a locked wallet and becomes tradable. The launch custody wallet, which received the whole 1T supply at launch, moved **136.2B PUMP** into two payout wallets on **Jun 25**, **Sep 8** and **Sep 13 2026**. A team vesting wallet that pays one forty-eighth of its allocation a month released another **8.7B PUMP** on **Aug 26** and **Sep 12**. Together that is **144.9B PUMP**, and it matches the rise in tradable PUMP plus the burn almost to the token. What happened next does not add to the count: the payout wallets handed **123.3B PUMP** to insider wallets on **Jul 14**, **Aug 14** and **Sep 14**, and two older team wallets released **11.7B PUMP**, part of it into an exchange hot wallet within minutes — but those tokens were already tradable when they moved. The calendar alone called for **96.3B PUMP** in this window; the realised unlock ran **48.7B** ahead of it. No PUMP is created by any of this — the tokens already existed — but it is exactly the supply the Pressure Framework measures: PUMP that could not trade before and can now.

Sell #3, Foundation and unscheduled unlocks, is **0**: every PUMP that left a locked team wallet in the window is already counted in the vesting row above. Sell #4, long-term locked or bankruptcy, is **0** as well — Pump.fun is an operating company with no bankruptcy estate, trustee or court-ordered distribution.

## Buy pressure: where new PUMP goes

Into a burn. Buy #1, programmatic buyback, is **23.8B PUMP**. On **Apr 28 2026** Pump.fun burned every PUMP it had bought back over the previous nine months and replaced its old policy with a contract that locks **50%** of net revenue into buying PUMP on the open market and burning it, for one year. Over these 90 days the buyback spent about **$58.0M** against **$114.8M** of revenue and destroyed **23.8B PUMP**. The burn is visible where it should be, in the supply itself: **857.9B PUMP** existed on **Jun 17 2026** and **834.0B** exist now. The two wallets that receive bought PUMP hold none — they are emptied into the burn every day — so there is no buyback-and-hold stockpile waiting to return to the market. Looking forward, the buyback is set in dollars, not in PUMP, and PUMP now trades well above its average price in the window, so the same revenue retires about **16.0B PUMP** over the next 90 days.

Buy #2, protocol fee burn, is **0**, because Pump.fun has no separate fee burn: platform fees fund the buyback and burning is where the buyback ends, so booking it twice would count one flow twice. Buy #3, Foundation buy, is **0** — Pump.fun keeps its half of revenue in stablecoins and SOL and made no open-market PUMP purchase of its own, and the Holder Rewards it launched on **Sep 12 2026** share launchpad-coin fees with holders rather than buying PUMP. Buy #4, new long-term lock, is **0**: PUMP has no staking, no vote-escrow and no lock programme.

## Foundation and overhang

The overhang on PUMP is large, and almost all of it sits with the team. Still locked: the launch custody wallet holds **229.3B PUMP**, carrying the rest of the team and investor schedule plus a community allocation that has no published release date at all, and a team vesting wallet holds **21.3B PUMP** that it pays out monthly. Already tradable but still in team hands: the two payout wallets hold **22.9B PUMP** they have not handed out, and two older team vesting wallets hold **28.3B PUMP**. These last two are already inside the circulating count, so they cannot add to the reading again, but where they go is the clearest sign of whether insiders are selling. All of these balances are read from the chain at every rebuild. There is no buyback accumulation wallet to watch, because bought PUMP is burned on arrival, and there is no Foundation treasury in PUMP or bankruptcy residual. The trigger applies to the locked items: if the custody wallet or the vesting wallet falls between refreshes by more than the schedule accounts for, that outflow enters Sell #3 at the next refresh.

## How PUMP compares to other buyback-and-burn tokens

PUMP belongs to the class of revenue tokens that turn platform income into supply removal. On mechanism it is one of the strictest: the mint authority is null, so unlike an uncapped proof-of-stake chain where a staking emission of several percent a year is normal, PUMP has no issuance to offset at all, and its burn is funded by fees rather than by a treasury decision each quarter. A perp-DEX token that routes fee revenue into buybacks and parks the tokens in a wallet leaves a stockpile that can come back; PUMP destroys what it buys, which is the harder commitment.

And yet PUMP reads **+25.86%** this quarter, because a burn only removes what revenue can afford, while an unlock releases whatever the calendar — or the custody wallet — says. At **23.8B PUMP** a quarter, the buyback retired about a sixth of what left the locked team wallets. That makes PUMP, for now, closer in shape to a recently launched token working through a four-year team and investor vest than to a mature exchange token whose quarterly burn outweighs everything else. The difference from a typical vest is that PUMP releases in large blocks from a custody wallet, and in this window those blocks arrived early and large.

The comparison flips on the forward view. Once the unlock settles at **6.875B PUMP** a month, the published calendar puts **20.6B PUMP** on the market over the next 90 days against about **16.0B PUMP** burned, a net of **+0.99%**. A modest rise in Pump.fun's revenue, or delivery that stays on the calendar instead of ahead of it, is the gap between a quarter of heavy dilution and a token whose supply is roughly flat.

## What to watch in the next 90 days

First, the monthly team and investor tranches on **Oct 12**, **Nov 12** and **Dec 12 2026**, **6.875B PUMP** each on the published schedule — and whether releases stay on that size, because in this window they ran **48.7B** ahead. Second, the launch custody wallet at **229.3B PUMP**: its September releases came in blocks of **20.0B** and **54.0B**, and any further block moves the reading immediately. Third, the **22.9B PUMP** sitting in the two payout wallets, already counted as tradable and one transfer away from insiders. Fourth, Pump.fun's revenue, because the buyback is half of it and is the only thing that can offset the unlock. Fifth, the buyback contract's one-year term, which ends in **Apr 2027**; any announcement about renewing or changing it is the single largest swing factor for PUMP's supply after this quarter.

## Summary

The MrNasdog Pressure Framework reads Pump.fun's PUMP at **+25.86%** over the trailing 90 days and **+0.99%** projected forward: supply growing, projected to keep growing. The structural mechanism is an insider unlock — **144.9B PUMP** released from locked team wallets after the **Jul 12 2026** cliff — set against a 50%-of-revenue buyback that burned **23.8B PUMP**. The key risk is that releases have run well ahead of the published **6.875B PUMP** monthly schedule while **229.3B PUMP** still sits in the launch custody wallet. The ceiling is the genuine comfort: the mint authority is null, so PUMP's **834.0B** supply can never grow, only shrink.

---

*MrNasdog Pressure Framework analysis of PUMP, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 15 2026.*

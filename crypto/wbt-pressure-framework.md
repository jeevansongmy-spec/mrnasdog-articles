---
title:         "WBT Inflation Analysis · August 2026 · Mixed last 90D, projected to shrink"
description:   "WBT has no mint instruction at all, and twelve buy-and-burn rounds destroyed 639,475 WBT in 90 days. Framework reads −0.33% net, monitor −0.38%."
canonical_url: "https://mrnasdog.com/research/wbt/inflation"
tags:          ["crypto", "wbt", "whitebit", "exchange"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/wbt/inflation](https://mrnasdog.com/research/wbt/inflation)*

# WBT Inflation Analysis · August 2026 · Mixed last 90D, projected to shrink

WhiteBIT Coin created no new supply in the last 90 days and destroyed **639,475 WBT** across **twelve** buy-and-burn rounds funded by exchange revenue. Against that, a single large holder released **0.25M WBT** to an exchange wallet on **Aug 6 2026**. The MrNasdog Pressure Framework reads WBT at **−0.33% net** over the trailing window and **−0.54%** forward, against a supply-monitor reading of **−0.38%**. WBT is capped at **400M** and, unusually for a large token, its contract contains no instruction that can create more — the supply is a one-way ratchet downward.

## The verdict, in one paragraph

Over the last 90 days the MrNasdog Pressure Framework reads WhiteBIT Coin at **−0.33% net**: **0.25M WBT** of discretionary release against **0.64M WBT** destroyed by the buyback-and-burn, on a circulating base of **117.96M WBT**. The supply monitor reads the same trailing window at **−0.38%**, a gap of **0.05 percentage points** — comfortably inside tolerance, so this build ships **no monitor-gap chip** and needed no reconciliation walk. The two agree because there is very little for them to disagree about: WBT has no emission schedule to model, no vesting calendar left to run, and the burn is a change in the total itself rather than a movement between wallets, so both readings are measuring the same subtraction. Forward, the framework reads **−0.54%**, because the burn continues and the one-off release does not. WBT is **deflationary by structural buyback** — an exchange token whose only supply mechanism points down.

## Sell pressure: where new WBT comes from

Sell #1 — protocol inflation — is **zero** on WhiteBIT Coin, and this build settles it from the contract rather than from the tokenomics page. WBT was issued exactly twice: **300M** on Ethereum in the deploy transaction and **100M** on Tron in 2022, together the full **400M** ceiling. Reading the verified Ethereum source this session, the only supply instruction the contract exposes to the outside world is the one that destroys coins; the instruction that creates them is internal and is called once, in the constructor. There is no owner mint, no minter role and no cap-raising path. A full scan of the token's creation events over the window returns nothing at all. WBT does not have low inflation — it has no inflation mechanism.

Sell #2 — vesting unlocks — is **zero**, and this is the change that quietly reshaped WBT's tokenomics this year. The staged release that governed WhiteBIT Coin's early years, including the treasury tranches that backed the total, finished during 2026. The supply is now fully unlocked, which means there is no cliff, no linear stream and no calendar entry that can land inside this window or any window after it. Some unlock trackers still render partial "locked" figures for WBT behind a paywall; the visible numbers are incoherent against a 400M supply and were not used.

Sell #3 — foundation and unscheduled unlocks — carries the entire sell side at **0.25M WBT**, and it is one dated event rather than a rate. On **Aug 6 2026** a large holding wallet sent **250,000 WBT** through an intermediate address into the exchange's own deposit hub, all inside the same day. That is the only release of any size the window contains. The same wallet's previous move was **900,000 WBT** on **Mar 31 2026** — two firings, five months apart, at very different sizes, which is a pattern too thin to project from. The forward value for this row is therefore **zero**, not a run-rate. Sell #4 — long-term locked or bankruptcy — is **zero**: WhiteBIT Coin has no bankruptcy estate, no trustee schedule and no court-ordered distribution.

## Buy pressure: where new WBT goes

Buy #1 — programmatic buyback — is the whole buy side at **0.64M WBT**, and it is the cleanest row on this page. WhiteBIT commits a fixed share of its own income to buying WBT on the open market and destroying it: **33%** of trading-fee income plus **5%** of income from every other exchange activity, with the stated long-term aim of taking total supply down toward **200M**. Twelve rounds fired inside the window. Read directly from the chain, total WBT supply fell from **166,245,492** to **165,606,017** — a destruction of **639,475 WBT** — and the twelve individual burn events sum to that same figure to the coin. The largest was **58,836** in early July; the most recent was **44,810** on **Aug 24 2026**.

Because published burn figures and realised burns often disagree for exchange tokens, this build checked both and expected a divergence. There is none: WhiteBIT's own published burn history lists the same twelve amounts on the same dates as the chain does. The announced **639,475** and the realised **639,475** are the same number. That is worth stating plainly, because it is not the normal result — and it means the buyback destination question answers itself. The coins are not parked in a treasury that could sell them back later; they go to an address that removes them from the total permanently, and the total moved with them.

Buy #2 — protocol fee burn — is **zero**, and that is a bookkeeping decision rather than an absence. WBT is the gas coin of Whitechain, and those transaction fees pay the people running the network rather than being destroyed. Everything destroyed in this window came from the buyback described above, so it is counted once, in Buy #1, and not twice. Buy #3 — foundation buy — is **zero**: no discretionary accumulation wallet grew during the window. Buy #4 — new long-term lock — is **zero** as well, because WhiteBIT Coin has no vote-lock, no staking contract that holds coins and no announced lockup, so nothing left the tradable float that way.

## Foundation and overhang

The overhang on WhiteBIT Coin is large, concentrated, and — for this window — completely still. Eleven addresses hold **164.65M** of the **165.61M** WBT that exists on Ethereum. The two biggest hold **60.00M** and **30.00M**, followed by two of **12.00M**, two of **6.00M** and three of **3.00M**. Read at both ends of the window, every one of those nine balances is identical to the coin — not a single WBT moved in 90 days.

Two addresses in that group deserve separate naming. The tenth, holding **4.65M**, is the wallet behind the Aug 6 release already counted in Sell #3; it started the window at **4.90M**. The eleventh holds exactly **25.00M WBT** at an address nobody can ever sign for, so that supply is unspendable rather than merely held — it is tracked, but it is never credited as buy pressure, because crediting a balance that has not moved would flatter the reading. If any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How WBT compares to other exchange tokens

WBT sits in the exchange-token class, where the defining question is what the exchange does with its revenue. Tokens in this family split three ways. Some run a periodic buyback-and-burn against a fixed cap, which converts revenue directly into permanent supply reduction. Some run a buyback that accumulates rather than destroys, parking coins in a treasury wallet that remains an overhang and can be sold back. And some pay revenue out to holders as yield, which is excellent for a holder and worth nothing as buy pressure, because not one unit of that revenue becomes a purchase or a burn. WhiteBIT Coin is firmly in the first group, and the chain confirms it rather than the marketing: total supply falls, week after week, by the amount the exchange says it destroyed.

Against continuous-emission proof-of-stake chains the contrast is total. Those chains mint new supply every block to pay validators, and their buy side has to work uphill just to reach neutral. WBT has no uphill: the sell side of the ledger is empty by construction now that the vesting calendar has expired, so anything the burn removes lands straight on the net. That is why a burn of only **0.54%** of circulating supply per quarter produces a clean deflationary reading, where the same quantum on an emitting chain would barely register.

The honest caveat is concentration, and it is the mirror image of the strength. Because **117.96M** of a **293.61M** total is counted as circulating, roughly **60%** of the supply sits outside the tradable float in a small number of very large, very quiet wallets. The framework books what moved, and almost nothing moved. But an exchange token whose float is this concentrated depends on those wallets continuing to sit still, in a way that a widely distributed chain does not. The burn is the mechanism; the stillness is the assumption.

## What to watch in the next 90 days

First, the weekly burn rate itself. It ran between **44,810** and **58,836 WBT** per round this window and drifted downward toward the end — because the buyback is funded by a fixed share of revenue and denominated in coins, a rising WBT price buys fewer coins for the same money. A sustained high price mechanically shrinks the burn in coin terms even when exchange revenue is flat, which is the single most likely reason the forward **−0.54%** would come in softer than it reads today. Second, the **60.00M** and **30.00M** wallets: they have not moved at all, and any release from either would dwarf a full quarter of burning. Third, the wallet behind the **Aug 6 2026** release, which has now fired twice in five months. Fourth, Whitechain's move from a standalone chain to an Ethereum layer-2, announced **Aug 18 2026** with mainnet targeted later in the year; WhiteBIT states that supply and core tokenomics carry over unchanged with full balance continuity, so the framework books nothing for it — but a migration snapshot is exactly the kind of event where a supply figure gets restated, and it is worth confirming it does not. Fifth, the stated goal of reducing total supply toward **200M**: at the current pace that is decades of burning, so any announced acceleration would be a genuine change to this reading.

## Summary

The MrNasdog Pressure Framework reads WhiteBIT Coin as deflationary and getting slightly more so — **−0.33%** over the last 90 days, **−0.54%** forward, against a monitor reading of **−0.38%** that agrees within **0.05 percentage points**. The structural mechanism is a revenue-funded buyback-and-burn that destroyed **639,475 WBT** in twelve rounds, sitting on top of a supply that has no mint instruction and no vesting calendar left to run, so the burn is not fighting anything. The key risk is not issuance but concentration: about **60%** of the **293.61M** total supply sits outside the counted float in a handful of wallets that held perfectly still this quarter, and a single release from the largest of them would outweigh a year of burning. The ceiling is **400M WBT**, set once and unraisable, and the total has already fallen well below it and continues to fall.

---

*MrNasdog Pressure Framework analysis of WBT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 27 2026.*

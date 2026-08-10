---
title:         "CC Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description:   "MrNasdog Pressure Framework reads Canton Coin at +1.70% net — ~2.0B CC minted vs ~1.33B burned. The largest fee burn of any chain, but the mint still runs ahead."
canonical_url: "https://mrnasdog.com/research/cc/inflation"
tags:          ["crypto", "cc", "canton", "l1"]
published:     true
---

*Originally published at [mrnasdog.com/research/cc/inflation](https://mrnasdog.com/research/cc/inflation)*

Canton Coin is an **uncapped burn-and-mint token**: the Canton Network minted about **2.0B CC** over the last 90 days to reward network activity, and destroyed about **1.33B CC** paying network fees. That leaves the framework at **+1.70% net**, holding near **+1.65%** over the next 90 days. Canton Coin runs the **largest fee burn of any chain** — yet a mint that scales with the reward schedule still runs ahead of it, so supply keeps growing.

## The verdict, in one paragraph

For the 90-day window ending Aug 10 2026, the MrNasdog Pressure Framework reads **Canton Coin at +1.70% net** — about **2.0B CC** minted against **1.33B CC** burned, roughly **+670M CC** of net new supply on a **39.3B** circulating base. Our independent supply monitor reads the same window at **+2.08%**, a gap of just **0.38 percentage points**, which is inside tolerance — no monitor-gap flag ships, and the two independent reads of the mint and the burn reconcile with the monitor. Realised minting is still about four-fifths of the schedule, and the fee burn is still the largest of any chain. Canton Coin is **structurally inflationary while the mint leads the burn**.

## Sell pressure: where new CC comes from

Sell #1 — protocol inflation — is the entire sell side, at about **2.0B CC** over the last 90 days. The Canton Network mints fresh CC in discrete mining rounds roughly every ten minutes and pays it to the participants doing measurable work: application providers, Super Validators and validators. The protocol's issuance curve steps down over the network's life — **40B CC** a year at genesis, **20B** from the six-month mark, **10B** from the eighteen-month mark, **5B** from year five and a flat **2.5B** from year ten. The Canton Network is now in the **10B CC** a year tranche, which would be **2.47B CC** across a 90-day window. About **2.0B** was actually minted — roughly **81%** of the allowance — because per-transaction reward caps mean the budget only mints when someone earns it, and unclaimed reward coupons expire after **36 hours**.

Because the reward coupons are denominated in CC, the mint is stable in coin terms even as the token price moves — an issuance read of about **$2.55M a day** at the prevailing price works out to roughly **22M CC a day**, or about **2.0B** across the window. Sell #2 — vesting unlocks — is **zero** and structurally so: Canton Coin had a fair launch with no pre-mine, no venture allocation and no team or seed schedule, so no cliff exists to unlock. Sell #3 — Foundation and unscheduled unlocks — is **zero**, because there was no token sale to build a foundation stockpile from, and the protocol development fund takes no cut of new emissions. Sell #4 — long-term locked or bankruptcy — is **zero**, because no bankruptcy estate or court-ordered distribution applies to Canton Coin.

## Buy pressure: where new CC goes

Buy #2 — protocol fee burn — is the whole buy side, at about **1.33B CC** over 90 days. Every fee on the Canton Network's Global Synchronizer is priced in dollars but settled by destroying CC at the on-chain rate, so activity converts directly into supply destruction. Traffic purchases, preapproval burns, setup burns, dust expiry, holding fees and sender-change fees are all destroyed rather than collected — there is no fee recipient. Over the window that came to roughly **$172M** of fees, which converts to about **1.33B CC** destroyed, and the current rate is around **15M CC** a day. The scale is the point: Canton's **30-day chain fees are the highest of any chain**, and because the fee is priced in dollars, the CC destroyed holds up even when settlement value eases or the token price falls — a burn that is anti-fragile to Canton Coin's own drawdowns. It still offsets only about **two-thirds** of the mint, so supply grows.

Buy #1 — programmatic buyback — is **zero**: no treasury bids for Canton Coin on the open market, because the model destroys fees outright instead of recycling them into buying. Buy #3 — Foundation buy — is **zero**, with no discretionary open-market buying observed. Buy #4 — new long-term lock — is **zero** in the ledger despite two live locking programmes, and this is the most important thing to watch. **CIP-0105** makes Super Validators lock **70%** of their lifetime earned rewards to keep full governance weight, and **CIP-0116**, which activated **May 20 2026**, requires featured apps to lock CC to keep earning — **25M CC** per issuer and **5M** per non-issuer. Neither is readable on chain yet, so the framework books nothing and monitors instead.

## Foundation and overhang

Canton Coin's team-controlled overhang is unusual because there is no allocation to overhang from. The largest identified concentration is the **Super Validator balance**: under CIP-0105, Super Validators lock **70%** of their lifetime-earned rewards to keep full voting weight, and ecosystem disclosures now put **nearly half of all CC** as locked across validators and apps. That commitment is irreversible by design and exists to buy governance weight, so it is a lock rather than a queue of sell pressure — but it is disclosed off chain, so it is refreshed by hand on a bi-weekly walk rather than read from a contract. The second identified overhang is the **protocol development fund**, whose emission share reads as unset in every tranche of the issuance curve. A third watch line is the **featured-app lock pool** under CIP-0116 and the third-party locking-as-a-service that launched **Jun 23 2026**. If any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How CC compares to other burn-and-mint chains

Canton Coin belongs to the small class of chains where issuance and destruction are both first-class protocol mechanisms rather than one being an afterthought. Ethereum is the closest structural cousin: both mint to reward the participants securing and using the network, and both destroy a usage-denominated fee. The difference is the denominator. Ethereum's base fee burn is priced in ETH and collapses when blockspace is cheap. Canton's fee is priced in dollars, so the CC destroyed scales with settlement value and holds up when the token price falls — a burn that is anti-fragile to the token's own drawdowns, and one that is already the largest of any chain by fee revenue.

Against hard-capped chains like Bitcoin, Canton Coin looks worse on paper and more dynamic in trend. Bitcoin's supply growth is fixed and falling on a halving schedule nobody can change, while Canton Coin is uncapped and could in principle mint 10B CC a year. But Canton Coin's issuance curve steps down on its own schedule to **2.5B** a year by year ten, and its realised mint runs below the allowance because the protocol only creates coins that were earned. Compared with exchange tokens that buy back and burn from profits, Canton Coin's destruction is not discretionary — no committee votes on the quarterly quantum, and no treasury can pause it. Compared with uncapped continuous-emission L1s that have no burn at all, Canton Coin already offsets about two-thirds of its issuance. The honest framing is that Canton Coin is **the only chain whose burn is funded by the largest fee revenue in the industry** — but at current activity the mint still leads, so the net remains inflationary.

## What to watch in the next 90 days

First, the realisation rate: the mint tracks how much of the 10B-a-year allowance activity actually claims, so the single biggest swing factor is whether featured-app and settlement activity climbs back toward the **2.47B CC** quarterly ceiling or keeps cooling. Second, the crossover: watch whether the daily burn near **15M CC** can close on the mint. Third, the CIP-0105 locking framework moves to its second phase when the on-chain locking contracts deploy, at which point Super Validator commitments become readable and the framework can book Buy #4 for the first time. Fourth, CIP-0116 featured-app locking should begin reporting real locked balances now that the rule has been live since **May 20 2026**. Fifth, the **DTCC** broader tokenisation rollout slated for **Oct 2026** is the single biggest input into the burn side.

## Summary

The MrNasdog Pressure Framework reads Canton Coin at **+1.70%** net supply growth over the last 90 days and **+1.65%** over the next 90, on a **39.3B CC** circulating base. The mechanism is a burn-and-mint model in which the Canton Network minted about **2.0B CC** to reward measured activity and destroyed about **1.33B CC** paying dollar-priced network fees — a burn funded by the highest fee revenue of any chain. The key risk is that Canton Coin has **no supply cap** and the mint scales up with activity: as institutional usage grows, more of the 10B-a-year allowance is claimed, so supply keeps growing even as the burn sets records. The ceiling is the protocol's own issuance curve, which allows **10B CC** a year today and steps down to **2.5B** by year ten.

---

*MrNasdog Pressure Framework analysis of CC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 10 2026.*

---
title:         "PYTH Inflation Analysis · July 2026 · Supply was growing, trend cooling"
description:   "Pyth's ~2.13B annual unlock landed May 19 2026 and the next isn't until May 2027, so the forward window is quiet. Framework ~-0.06% net; monitor +36.96%."
canonical_url: "https://mrnasdog.com/research/pyth/inflation"
tags:          ["crypto", "pyth", "pythnetwork", "oracle"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/pyth/inflation](https://mrnasdog.com/research/pyth/inflation)*

Pyth Network mints no PYTH — all **10,000,000,000 PYTH** exist from genesis and the only supply engine is a once-a-year unlock cliff. That cliff, about **2.13B PYTH**, already landed on **May 19 2026**, inside the trailing 90-day window; the next and final cliff is not until **May 2027**. So the forward window carries **no new supply**, and against a small revenue-funded buyback of roughly **5M PYTH** per 90 days the MrNasdog Pressure Framework reads PYTH at about **-0.06%** net forward — essentially flat, a shade deflationary — with **~7.87B** of the **10B** cap now circulating.

## The verdict, in one paragraph

For the 90-day window opening **Jul 31 2026**, the framework reads **PYTH at about -0.06% net** forward — no unlock is due, so the only moving part is the buyback, which takes a little supply back. Over the trailing 90 days the framework measured **+26.92%**, because the annual unlock sits inside that window. Our supply monitor reads **+36.96%**, a gap of **10.04 percentage points**, well outside the framework's 0.5-point tolerance, so a monitor-gap chip ships on the PYTH overview. The deep walk found the reason and it is not a data conflict: the monitor sizes the same **~2.13B** unlock on the pre-cliff base of about **5.75B** PYTH (**+36.96%**), while the framework sizes it on the current, larger base of about **7.87B** (**+26.92%**). Same one-time cliff, different denominator base. PYTH is best characterised as **a fixed-supply oracle token whose annual dilution has just fired and whose next 90 days are structurally quiet**.

## Sell pressure: where new PYTH comes from

Sell #1 — protocol inflation — is **zero**, and structurally so. PYTH is an oracle token, not a chain base asset: all **10,000,000,000 PYTH** were minted at genesis on **Nov 20 2023** and there is no mint function, so the protocol creates nothing new. The one emission route that ever paid new PYTH into hands — Oracle Integrity Staking rewards — was switched off in 2026 when a governance proposal set the reward rate to zero before its finite pool depleted. Staking and slashing remain live, but they distribute nothing, and the monitor's 30-day reading of **+0.0015%** confirms the float has been flat since the May cliff.

Sell #2 — vesting unlocks — is the entire supply story, and it is a cliff, not a stream. Eighty-five percent of PYTH was locked at launch and unlocks in four equal tranches at six, eighteen, thirty and forty-two months — every May. The thirty-month tranche released about **2.13B PYTH** on **May 19 2026**, and the framework confirmed the release reached the market rather than sitting in escrow: circulating supply rose from about **5.75B** to about **7.87B** across the window, a change of **2.13B** that matches the scheduled quantum almost exactly, so there is no undrawn overhang to carry forward. Because that cliff sits inside the trailing 90 days, the framework books **~2.13B** for the last window and **zero** for the next — the final tranche does not unlock until about **May 20 2027**, well outside the forward window. There is no monthly drip anywhere in the schedule.

Sell #3 — Foundation and unscheduled unlocks — is **zero** this window but not empty of risk. About **2.13B PYTH** remains locked for the May 2027 cliff, spread across the Ecosystem Growth, Publisher Rewards, Private Sales and Protocol Development buckets, and the Pyth DAO treasury holds more still. None of it has a release path other than the published cliff already counted in Sell #2, and no off-calendar distribution fired in the window, so the row stays at zero and the balances are carried as tracked overhangs. Sell #4 — long-term locked or bankruptcy — is **zero** permanently: Pyth is a live project with no bankruptcy estate and no trustee schedule.

## Buy pressure: where new PYTH goes

Buy #1 — programmatic buyback — is **non-zero**, and it is the reason the forward reading tips deflationary rather than sitting exactly at flat. The PYTH Reserve buys PYTH on the open market every month, deploying roughly a third of the DAO treasury balance and funded by real product revenue from Pyth Pro, Pyth Core, Entropy, Express Relay and the data marketplace. Since the Reserve launched in **Dec 2025** it has acquired about **12M PYTH** on-chain, which is roughly **5M** over a 90-day window and rising as revenue grows — the paid Pyth Core data model went live on **Jul 31 2026**, routing new subscription revenue straight into the Reserve. Bought-back PYTH is held in the Reserve on-chain, not burned, so it is booked as accumulation that takes supply off the tradable float.

Buy #2 — protocol fee burn — is **zero**: Pyth burns nothing, because product revenue is routed into the buyback rather than into a burn address. Buy #3 — Foundation buy — is **zero** as a separate line, because the Reserve buyback is the only accumulation programme and is already counted in Buy #1; there is no second open-market purchase to add. Buy #4 — new long-term lock — is **zero**: roughly **1B PYTH** is staked for oracle integrity, but stakers can unbond and withdraw at any time and the reward stream is now zero, so staking is holder-driven behaviour, not an announced lock of a fixed size that removes float.

## Foundation and overhang

The overhang on PYTH is large but fully scheduled. About **2.13B PYTH** — the difference between the **7.87B** circulating today and the **10B** cap — is still locked, and essentially all of it releases on the single final cliff of about **May 20 2027**: the Ecosystem Growth, Publisher Rewards, Private Sales and Protocol Development allocations. Alongside them sits the Pyth DAO treasury, which now both receives protocol revenue and funds the Reserve buyback out of it. None of these balances has a discretionary release path inside the current window, so the framework carries them at zero. If any of these overhangs' balances falls between refreshes and the PYTH leaves protocol control ahead of the scheduled cliff, the outflow enters Sell #3 at the next refresh.

## How PYTH compares to other fixed-supply oracle and utility tokens

PYTH belongs to the fixed-cap utility-token class, and within it to the sub-group whose only dilution is investor and ecosystem vesting rather than any protocol mint. Against an uncapped continuous-emission layer-1, the comparison flatters PYTH: a proof-of-stake base asset mints new coins every block on a schedule nobody controls, whereas PYTH mints nothing and its **10B** is an absolute ceiling with a defined end date to dilution — the May 2027 cliff, after which the vesting row goes permanently to zero. The cost of that structure is lumpiness: instead of a smooth few-percent-a-year drip, PYTH delivers its dilution in one **~2.13B** jump each May, which is exactly why the trailing-window monitor reads a dramatic **+36.96%** while the forward window reads flat.

The more interesting comparison is with exchange and infrastructure tokens that run a revenue-funded buyback. Like those, PYTH now converts real product revenue into open-market purchases through the Reserve rather than relying on a fee burn. But it is early and small — about **12M PYTH** bought since **Dec 2025** against a **7.87B** float — so unlike a mature buyback-and-burn token, the buy side does not yet come close to offsetting a cliff year. What it does do is set the direction of travel: once the final unlock clears in 2027, the buyback is the only structural flow left, and it points the token gently deflationary rather than flat.

## What to watch in the next 90 days

Watch the Reserve buyback, which is the only live flow in this window: with the paid Pyth Core data model live from **Jul 31 2026**, the monthly purchase should grow above its **~5M PYTH** per-quarter run rate, and a visible step-up would move the forward net further into deflationary territory. Watch Pyth Pro revenue, reported through the DAO, since it is the fuel for that buyback and the clearest read on how fast the buy side scales. Watch the Pyth DAO governance forum for any proposal that changes the buyback allocation away from the current third of treasury, or that would reintroduce staking rewards. And watch the horizon date — the final vesting cliff of about **2.13B PYTH** around **May 20 2027** — which is the next time this page's sell ledger moves off zero, and the last time it ever should.

## Summary

PYTH is a fixed-supply, zero-mint oracle token whose only dilution is an annual vesting cliff — and that cliff, about **2.13B PYTH**, already landed on **May 19 2026**. With the next unlock not due until **May 2027**, the forward 90 days carry no new supply, and a small revenue-funded Reserve buyback of roughly **5M PYTH** tips the framework to about **-0.06%** net — essentially flat, a shade deflationary. Our monitor reads **+36.96%**, a **10.04-point** gap that is not a conflict but a denominator-base artifact: it sizes the same one-time cliff on the pre-unlock **5.75B** base while the framework sizes it on the current **7.87B** base. The key thing to hold in mind is that PYTH's dilution is lumpy and finite — one jump a year, ending in 2027 — and that after it a growing on-chain buyback is the only structural flow left.

---

*MrNasdog Pressure Framework analysis of Pyth Network (PYTH), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 31 2026.*

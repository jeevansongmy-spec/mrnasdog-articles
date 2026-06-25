---
title: "Jupiter (JUP) Inflation Analysis: A Revenue Buyback Against a Switched-Off Sell Side"
description: "A MrNasdog Pressure Framework read of Jupiter (JUP): a 50%-of-revenue buyback buys ~24M JUP / 90D while emissions are switched off. Framework reads −0.72%; monitor −4.92% is a reclassification, not flow (gap ⚠)."
canonical_url: "https://mrnasdog.com/research/jup/inflation"
tags: ["crypto", "jupiter", "solana", "defi"]
published: true
---

> Originally published at **[mrnasdog.com/research/jup/inflation](https://mrnasdog.com/research/jup/inflation)** by MrNasdog.

Jupiter buys back JUP with 50% of protocol revenue — about **24M JUP** every 90 days — while emissions are switched off. The framework reads **−0.72% net** on a ~6.86B effective cap. The supply monitor reads −4.92%, but that drop is an accounting re-tag, not market flow — so the framework keeps the on-chain buyback rate and flags a **monitor gap**.

## The verdict, in one paragraph

For the 90-day window ending June 26 2026, the framework reads **JUP at −0.72% net inflation** — deflationary on the documented revenue-buyback rate of **~24M JUP** against a structurally zero sell side. The supply monitor reads **−4.92%**, observing roughly **172M JUP** removed from the circulating count over the trailing window — a **4.20-percentage-point gap** that triggers the ⚠ monitor-gap chip. That 172M cannot be entity buying or selling: the only real market flow in the window is the ~24M buyback (which removes supply) and the ~200M final Jupuary distribution (which adds it). A net 172M drop in circulating is therefore an aggregator reclassification of non-market buckets — the buyback trust and the Jupuary multisig — not behaviour the framework should book. JUP is structurally deflationary by buyback, with emissions switched off by governance.

## Sell pressure: where new JUP comes from

JUP is a Solana SPL token with no callable mint function. The 10B genesis cap is now an effective ~6.86B after the **Fresh Start** Litterbox burn destroyed roughly **130M JUP** on November 26 2025. Sell #1 (protocol inflation) is permanently zero — no new JUP can be created.

Sell #2 (vesting unlocks) is zero because emissions were switched off by governance. Team vesting is paused under a credit-accounting model, and the final Jupuary — Jupiter's annual community distribution — was cut from a planned 700M to roughly **200M JUP** (about 175M to fee-paying users and 25M to stakers, snapshotted around January 30 2026 and distributed near May 2026). No scheduled vesting cliff lands inside the June 2026 window, and no further annual distribution is scheduled.

Sell #3 (Foundation discretion) is zero by design. Any token a team member wishes to sell is bought back one-for-one through the same protocol-revenue stream, so net team flow nets to zero. The roughly 500M un-distributed Jupuary allocation was returned to the community multisig and carries no published release schedule — it is a tracked overhang, not an active sell. Sell #4 (bankruptcy estate) is zero; no entity holding JUP is in bankruptcy distribution.

## Buy pressure: where new JUP goes

The dominant — and only active — buy flow is the protocol-revenue **buyback**. Under the structural design, 50% of Jupiter protocol revenue routes to an on-chain trust that buys JUP on the open market and accumulates it. Cumulative repurchases reached about **123M JUP** by mid-May 2026, with the 2026 monthly pace running roughly 7–9M JUP a month (about **24M JUP** over 90 days). That is the rate the framework books for Buy #1.

Buy #2 (protocol fee burn) is zero: there is no continuous block-by-block burn, and the single ~130M burn was a one-off governance event in November 2025, outside this window. Buy #3 (Foundation buy) is zero — the revenue buyback is the single structural mechanism, with no separate accumulation alongside it. Buy #4 (new long-term lock) is zero; no new staking-lock programme launched, and under the Fresh Start reset the unstake period was actually shortened to 7 days.

## Foundation and overhang

Two team-controlled overhangs are worth watching. The first is the **buyback trust** (a public Solana address) holding roughly 123M JUP of accumulated repurchases — the wallet balance is read on each refresh, and an outflow would enter Sell #3. The second is the **community multisig** holding the ~500M un-distributed Jupuary allocation with no published schedule. Both are tracked as overhangs rather than projected forward as sells. If either balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How JUP compares to other revenue-buyback tokens

Among revenue-buyback governance tokens, JUP runs one of the most single-directional designs in coverage — every flow points buy-side. Hyperliquid's HYPE has a comparable revenue-buyback structure but still carries some live vesting, so its net sits a touch deeper negative on a larger float. Exchange tokens that buy back and burn quarterly (rather than continuously accumulate) remove supply in lumps tied to a calendar; JUP's buyback accrues continuously as swap fees come in. The structural distinction that matters for the framework is custody versus market float: JUP's switched-off emissions plus a continuous revenue buyback mean the only thing moving supply on the active float is the buyback itself.

The economic logic is straightforward — Jupiter is signalling that platform revenue should accrue to the token rather than fund continued emissions. Whether that posture persists depends on the next governance cycle, including a live discussion to raise the buyback share from 50% to 70%.

## What to watch in the next 90 days

Three things move the framework reading. First, the live forum proposal to raise the buyback allocation from **50% to 70%** (posted May 30 2026, still in discussion as of late June 2026) — if it passes, the buyback rate steps up and the net reads more deeply negative. Second, the **buyback trust wallet** — a direct on-chain enumeration of its in-window inflow would tighten the ~24M estimate, and any outflow would flip into Sell #3. Third, **Jupiter protocol revenue** — the buyback scales linearly with revenue, so a meaningful change in swap volume changes the buyback pace.

## Summary

JUP is a Solana governance token whose only active supply flow is a buyback funded by 50% of protocol revenue, against a sell side switched off by governance (paused team vesting, a reduced ~200M final Jupuary). The framework reads **−0.72% net** for the trailing 90 days on a documented ~24M-JUP buyback. The supply monitor reads −4.92%, but that 172M circulating drop is a reclassification of non-market buckets rather than entity flow, so the framework keeps the on-chain rate and ships the ⚠ monitor-gap chip. JUP is structurally deflationary by buyback, with a 70% allocation proposal as the key upside catalyst.

---

*MrNasdog Pressure Framework analysis of Jupiter (JUP), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jun 26 2026.*

---
title:         "JUP Inflation Analysis · July 2026 · Net Deflationary"
description:   "Net deflationary: a revenue buyback buys ~30M JUP / 90D while emissions run net-zero. Framework reads −0.90%; monitor −6.50% is a reclassification (gap ⚠)."
canonical_url: "https://mrnasdog.com/research/jup/inflation"
tags:          ["crypto", "jup", "jupiter", "solana"]
published:     true
---

*Originally published at [mrnasdog.com/research/jup/inflation](https://mrnasdog.com/research/jup/inflation)*

# JUP Inflation Analysis · July 2026 · Net Deflationary

Jupiter buys back JUP with 50% of protocol revenue — about **30M JUP** every 90 days — while emissions run net-zero by governance. The framework reads **−0.90% net** on a ~6.86B effective supply. The supply monitor reads −6.50%, but that drop is an accounting re-tag, not market flow — so the framework keeps the on-chain buyback rate and flags a **monitor gap**.

## The verdict, in one paragraph

For the 90-day window ending July 6 2026, the framework reads **JUP at −0.90% net inflation** — deflationary on the documented revenue-buyback rate of **~30M JUP** against a structurally zero sell side. The supply monitor reads **−6.50%**, observing roughly **231M JUP** removed from the circulating count over the trailing window — a **5.60-percentage-point gap** that triggers the ⚠ monitor-gap chip. That 231M cannot be entity buying or selling: the only real market flow in the window is the ~30M buyback that removes supply, and no scheduled unlock added any. A net 231M drop in circulating is therefore an aggregator reclassification of non-market buckets — the buyback trust and the returned community treasury — not behaviour the framework should book. JUP is structurally deflationary by buyback, with emissions switched to net-zero by governance.

## Sell pressure: where new JUP comes from

JUP is a Solana SPL token with no callable mint function. The 10B genesis cap has been cut to a **~6.86B** effective supply through community-approved supply reductions and burns, including the **~134M JUP** Litterbox burn. Sell #1 (protocol inflation) is permanently zero — no new JUP can be created.

Sell #2 (vesting unlocks) is zero because emissions were switched to net-zero by governance. Under the **Going Green** DAO outcome (passed February 2026 with 75.3% support), team vesting concluded early — the last team unlock was **January 27 2026** — and the Jupuary reserve was cancelled and returned to the community treasury. The unlock trackers now read JUP **fully unlocked**, with no upcoming unlock events and no vesting cliff inside the July–October 2026 window. Active Staking Rewards of roughly 50M JUP a quarter continue, but they are designed to be supply-neutral — drawn from already-counted allocations rather than new mint.

Sell #3 (Foundation discretion) is zero by design. Any token a team member wishes to sell is bought back one-for-one through the same protocol-revenue stream, so net team flow nets to zero. Two overhangs are tracked rather than booked: the on-chain buyback trust (~145M JUP, held as a reserve) and the community treasury holding the returned Jupuary allocation (~500M-plus, no published schedule). Sell #4 (bankruptcy estate) is zero; no entity holding JUP is in bankruptcy distribution.

## Buy pressure: where new JUP goes

The dominant — and only active — buy flow is the protocol-revenue **buyback**. Under the structural design, 50% of Jupiter protocol revenue routes to an on-chain trust that buys JUP on the open market and locks it away. A direct on-chain read of the trust shows about **145M JUP** accumulated by July 6 2026, up from roughly 111M in mid-April — a 2026 pace of about 9–11M JUP a month, or roughly **30M JUP** over 90 days. That is the rate the framework books for Buy #1.

Buy #2 (protocol fee burn) is zero: there is no continuous block-by-block burn, and the single ~134M burn was a one-off governance event outside this window. Buy #3 (Foundation buy) is zero — the revenue buyback is the single structural mechanism, with no separate accumulation alongside it. Buy #4 (new long-term lock) is zero; no new staking-lock programme launched, and the unstake period is a short 7 days.

## Foundation and overhang

Two team-controlled overhangs are worth watching. The first is the **buyback trust** (a public Solana address) holding roughly 145M JUP of accumulated repurchases — the wallet balance is read on each refresh, and an outflow would enter Sell #3. The second is the **community treasury** holding the ~500M-plus returned Jupuary allocation with no published schedule. Both are tracked as overhangs rather than projected forward as sells. If either balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How JUP compares to other revenue-buyback tokens

Among revenue-buyback governance tokens, JUP runs one of the most single-directional designs in coverage — every flow points buy-side. Hyperliquid's HYPE has a comparable revenue-buyback structure but still carries some live vesting, so its net sits a touch deeper negative on a larger float. Exchange tokens that buy back and burn quarterly (rather than continuously accumulate) remove supply in lumps tied to a calendar; JUP's buyback accrues continuously as swap fees come in. The structural distinction that matters for the framework is custody versus market float: JUP's net-zero emissions plus a continuous revenue buyback mean the only thing moving supply on the active float is the buyback itself.

The economic logic is straightforward — Jupiter is signalling that platform revenue should accrue to the token rather than fund continued emissions. Whether that posture strengthens depends on the next governance cycle, including live proposals to raise the buyback share from 50% to 70% and to switch the trust from accumulation to direct burn.

## What to watch in the next 90 days

Three things move the framework reading. First, the live forum proposals to raise the buyback allocation from **50% to 70%** (posted May 30 2026) and to lower staking rewards while switching the trust to a direct burn (posted June 22 2026) — both under discussion; if either passes, the buyback rate steps up and the net reads more deeply negative. Second, the **buyback trust wallet** — its balance is read on-chain each refresh, and any outflow would flip into Sell #3. Third, **Jupiter protocol revenue** — the buyback scales linearly with revenue, so a meaningful change in swap volume changes the buyback pace.

## Summary

JUP is a Solana governance token whose only active supply flow is a buyback funded by 50% of protocol revenue, against a sell side switched to net-zero by governance (concluded team vesting, a returned Jupuary reserve, fully-unlocked trackers). The framework reads **−0.90% net** for the trailing 90 days on a documented ~30M-JUP buyback. The supply monitor reads −6.50%, but that 231M circulating drop is a reclassification of non-market buckets rather than entity flow, so the framework keeps the on-chain rate and ships the ⚠ monitor-gap chip. JUP is structurally deflationary by buyback, with the 70% buyback and direct-burn proposals as the key upside catalysts.

---

*MrNasdog Pressure Framework analysis of Jupiter (JUP), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 6 2026.*

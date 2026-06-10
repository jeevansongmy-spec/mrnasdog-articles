---
title: "Jupiter (JUP) Inflation Analysis: Net-Zero Emissions Zeroed Every Sell Row"
description: "A MrNasdog Pressure Framework read of Jupiter (JUP): Litterbox Trust buyback ~28M / 90D against zeroed sell side after Net-Zero Emissions vote. Framework reads −0.85%, monitor −5.12% (gap ⚠ — on-chain reality likely more deflationary)."
canonical_url: "https://mrnasdog.com/research/jup/inflation"
tags: ["crypto", "jupiter", "solana", "defi"]
published: true
---

> Originally published at **[mrnasdog.com/research/jup/inflation](https://mrnasdog.com/research/jup/inflation)** by MrNasdog.

Jupiter's Litterbox Trust buys ~28M JUP every 90 days from protocol revenue. Vesting is paused under the Net-Zero Emissions vote. Framework reading: **−0.85% net** on a ~6.86B effective cap. The aggregator monitor reads −5.12% — a much larger decrease that suggests fee revenue may have scaled materially.

## The verdict, in one paragraph

For the 90-day window ending June 10 2026, the framework reads **JUP at −0.85% net inflation** — deflationary on the documented Litterbox buyback rate of ~28.2M JUP / 90D against a structurally zero sell side following the February 15 2026 Net-Zero Emissions DAO vote. The aggregator monitor reads **−5.12%**, observing roughly 179M JUP removed from circulation over the trailing window. That is ~6× the documented Litterbox pace. The framework keeps the documented rate per anti-fabrication; the next refresh should re-derive the buyback rate via direct on-chain enumeration of the Litterbox Trust wallet outflow to reconcile the gap.

## Sell pressure: zeroed by Net-Zero Emissions

JUP is a Solana SPL token with no callable mint function. The 10B genesis cap is now effectively ~6.86B after burns plus Net-Zero Emissions adjustments. Sell #1 (protocol inflation) is permanently zero — no new JUP can be created.

Sell #2 (vesting unlocks) is also zero, but the structural reason is unusual. The **Net-Zero Emissions DAO vote** ratified February 15 2026 postponed Jupuary distributions for the remainder of 2026, paused team vesting via a credit-accounting mechanism, and concluded Mercurial vesting with a final accelerated unlock on February 25 2026 (which falls inside the trailing window edge). The Mercurial final tranche was the last scheduled cliff event; no further scheduled unlocks land in the window. Future Jupuary rounds from 2027 onward depend on a new DAO vote.

Sell #3 (Foundation discretion) is zero by design under Net-Zero. Team allocations switched to an accounting-credit model: any team sales are offset 1:1 by open-market buybacks routed through the same revenue stream. So even if the team transacts, the net effect on circulating supply is zero. Sell #4 (bankruptcy estate) is zero; the 700M Jupuary tokens that were originally allocated for the 2026 round were returned to the Community Cold Multisig under the Net-Zero vote and are now long-term locked rather than selling.

## Buy pressure: the Litterbox Trust

The dominant — and only — buy flow is the **Litterbox Trust**. Under the structural design, 50% of Jupiter protocol revenue routes to the Litterbox, which buys JUP on the open market and locks the purchased tokens for 3 years. The April 2026 documented accumulation rate was ~9.4M JUP per month, which at face value gives ~28.2M JUP per 90 days. That number is what the framework currently books.

The aggregator monitor's −179M / 90D reading suggests the Litterbox is running at a meaningfully higher pace than the April baseline — potentially driven by Jupiter's DEX aggregator volume scaling in Q2 2026 or new product launches. Without a fresh on-chain enumeration of the Litterbox Trust wallet's inflow over the window, the framework declines to reset the rate (per the anti-fabrication rule against back-deriving row values from monitor delta). The chip warns of the ⚠ gap. Buy #2 (fee burn) is zero; Litterbox holds, doesn't burn. Buy #3 (Foundation buy) is zero — Litterbox is the structural mechanism. Buy #4 (new long-term lock) is conceptually relevant since Litterbox locks for 3 years, but in the framework's row taxonomy this counts as Buy #1.

## The Net-Zero Emissions vote

The February 15 2026 DAO vote is the load-bearing structural event for JUP's current ledger shape. Before Net-Zero, JUP carried active team and investor cohort vesting, a scheduled annual Jupuary distribution to community wallets, and a continuing Mercurial vesting tail. After Net-Zero, every scheduled sell flow was either paused, postponed, or converted to a credit-accounted offset that nets to zero against buybacks. The result is a token where every sell-side row reads zero by governance choice, leaving only the Litterbox accumulation on the active ledger.

Whether Net-Zero persists past 2026 depends on a future DAO vote. The 2027 Jupuary round (if any) would activate a sell-side flow again.

## How JUP compares to other revenue-share governance tokens

Among revenue-share governance tokens, JUP under Net-Zero is the most aggressive single-direction design — every flow points buy-side. Hyperliquid's HYPE has a comparable structure but with active vesting at ~1M/90D, so HYPE reads −0.876% rather than −0.85%. Sky's SBE buys but the protocol also mints staking rewards in parallel, so net stays mildly inflationary. Curve's veCRV model differs entirely — emission continues while locked stake grows. JUP's Net-Zero is novel: no other major token zeros every sell row by governance choice while keeping the buyback active.

The economic logic is straightforward: Jupiter is signaling that platform revenue should accrue to token holders rather than fund continued emissions. Whether that signal persists past the next DAO vote cycle is the structural question.

## What to watch in the next 90 days

Three things move the framework reading. First and most important, the **Litterbox Trust wallet inflow** — if the next refresh enumerates the on-chain buyback rate as substantially higher than 28M/90D, the framework reading would shift more deeply negative. Second, any **DAO proposal to renew Jupuary** for 2027 — even if not executed in window, a ratified proposal would activate a future Sell #1 + Sell #3. Third, **Jupiter protocol revenue** — the Litterbox flow scales linearly with revenue, so a meaningful change in DEX volume changes the buyback pace.

## Summary

JUP is a Solana governance token with a 50%-of-revenue Litterbox buyback as its only active flow following the February 2026 Net-Zero Emissions DAO vote. The framework reads −0.85% net for the trailing 90 days on the documented buyback rate; the aggregator monitor reads −5.12%, suggesting the on-chain reality is materially more deflationary than the April baseline. The next refresh should re-derive the buyback rate via direct Litterbox wallet enumeration. Until then, the ⚠ chip carries the gap. JUP under Net-Zero is the most structurally deflationary design in coverage by governance choice.

---

*MrNasdog Pressure Framework analysis of Jupiter (JUP), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 10, 2026.*

---
title: "JTO Inflation Analysis · July 2026 · Supply growing, no buyback offset yet"
description: "Capped but still growing: JTO mints nothing, yet a multi-year vest adds ~35.3M JTO/90d with no live buyback offset. Framework reads +7.15% net (monitor +7.70%)."
canonical_url: "https://mrnasdog.com/research/jto/inflation"
tags: ["crypto", "jito", "solana", "jto"]
published: true
---

> Originally published at **[mrnasdog.com/research/jto/inflation](https://mrnasdog.com/research/jto/inflation)** by MrNasdog.

Jito's JTO is a **capped 1B-supply** Solana governance token with **no protocol emission** — yet its float is still growing, because roughly half the supply is locked in a multi-year vest that keeps releasing. The linear vest of team, investor and ecosystem allocations adds about **35.3M JTO** to the open market every 90 days, and there is no live buy-side offset, leaving the framework at about **+7.15% net**. Our supply monitor reads **+7.70%** over the same window; the **0.55-point** gap is only the denominator base, so the page carries a small monitor-gap note.

## The verdict, in one paragraph

For the 90-day window ending July 14 2026, the MrNasdog Pressure Framework reads **JTO at about +7.15% net** — clearly inflationary on the active float. All of that pressure is one mechanism: the multi-year linear **vesting unlock** of already-minted JTO, adding roughly **35.3M JTO** to the market over the window. There is no protocol emission and, so far, no buy-side offset. Our supply monitor reads the realized change at **+7.70%**, a gap of about **0.55 percentage points** — just over the 0.5-point line, so JTO ships with a **monitor-gap note**. The gap is not a disagreement about the flow: both sides see the same ~35.3M vest. It is purely the denominator — the monitor divides by the **90-day-ago float (458.4M → +7.70%)**, the framework by the **current float (493.9M → +7.15%)**. JTO is **structurally inflationary on the float** until either the vest thins out or the new buyback starts absorbing coins.

## Sell pressure: where new JTO comes from

The important thing to understand about JTO is that no **new** coins are created at all. Sell #1 — protocol inflation — is **zero**. JTO has a fixed **1B** max supply, entirely minted at the December 2023 launch, and the Jito network pays no block reward or staking reward in JTO. So every coin that reaches the market is an already-minted allocation coming out of a lock, not fresh issuance.

That makes Sell #2 — vesting unlocks — the entire story, at about **35.3M JTO** over 90 days. JTO's allocations (community growth 34.29%, ecosystem development 25%, core contributors 24.5%, investors 16.21%) sat behind a **one-year cliff** that ended in December 2024, and have vested on a multi-year linear schedule since. Gross monthly unlocks run higher — on the order of **18.6M JTO a month** — but a chunk of each unlock routes into ecosystem and DAO reserves that are not counted as open float, so the net amount actually landing in the market is about **35.3M** per quarter. Because the vest is smooth and continuous, that same rate is the best read for the next 90 days. Sell #3 — Foundation and unscheduled unlocks — is zero as a flow: the **250M** ecosystem-development reserve and the community-growth reserve hold the unlocked-but-not-yet-circulating JTO, and no discrete dated dump falls in the window. Sell #4 — long-term locked or bankruptcy — is zero, with no estate or court distribution applying to JTO.

## Buy pressure: where new JTO goes

For now, almost nowhere — which is why the net reads so hot. Buy #1 — programmatic buyback — is **zero** in practice, even though the mechanism now formally exists. In **JIP-38**, passed on **Jul 13 2026**, the Jito DAO committed 100% of its share of trading-terminal (JTX) revenue to open-market JTO **buyback-and-burn** through **Q4 2027**, executed programmatically via the Rev Splitter with per-epoch disclosure. But JTX is a brand-new product and its revenue is still small, so no material buyback has hit the market yet. We book it at zero and watch it.

Buy #2 — protocol fee burn — is also **zero**: JTO has no automatic per-transaction burn, and the burn half of JIP-38 depends on the same nascent revenue, so no coins are being destroyed on any recurring basis today. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero, with no discretionary open-market buying outside the published program and no new escrow of circulating JTO in the window; staking is liquid and does not count as a lock.

## Foundation and overhang

JTO's overhang is unusually large because roughly **half the 1B supply** is still not circulating. Two governed reserves hold most of it. The first is the **ecosystem-development** allocation, 25% of supply (**250M JTO**), released on a 48-month linear schedule. The second is the **community-growth** allocation, 34.29% of supply, vesting over several years. Alongside those sit the still-vesting **core-contributor (24.5%)** and **investor (16.21%)** tranches, whose monthly linear release is exactly the Sell #2 flow. The Jito DAO treasury — funded mainly by JitoSOL and MEV-tip fees, worth well over $100M — is a third pool, though it holds little JTO directly. None of these is on a discrete dated cliff, so the framework books no Sell #3 flow and re-walks the on-chain supply, the unlock schedule and the treasury on a roughly bi-weekly cadence. If any reserve's balance falls into the float faster than the smooth vest between refreshes, that outflow enters Sell #3 at the next refresh.

## How JTO compares to other capped-but-vesting tokens

JTO sits in a specific class: **hard-capped tokens with no emission but a long vesting tail**. That is very different from an uncapped proof-of-stake L1 like Solana itself, which mints new coins as staking rewards every epoch. JTO issues nothing — its 1B cap is fixed and its mint is effectively spent — so its inflation is not monetary expansion at all; it is the mechanical release of coins that already exist but were locked. On an inflation lens, the two look similar (float grows either way), but the ceiling is completely different: JTO's float growth **stops** once the vest completes, while an emission chain keeps issuing forever.

Against other governance tokens with fee-funded buybacks, JTO is at an earlier stage. Exchange and DEX tokens that already run mature buyback-and-burn programs turn real revenue into net-deflationary pressure that offsets or beats their unlocks. JTO has just **authorized** that machinery in JIP-38 but has not yet built the revenue to power it — so today it reads like a token carrying the unlock tail without the offset. The comparison that matters over the next year is whether JTX revenue grows fast enough for the buyback-and-burn to bite into the ~35M-a-quarter vest. Until it does, JTO is structurally the more dilutive of the two profiles.

## What to watch in the next 90 days

Watch the **JIP-38 per-epoch buyback disclosures** — the DAO committed to publishing JTX revenue, buyback and burn figures every epoch, and the first meaningful numbers will show whether the offset is real or still theoretical. Watch **JTX adoption and revenue**, since 100% of the DAO's share funds the buyback; a fast ramp is the only thing that turns the net down. Watch the **monthly linear unlocks** (the vest releases around the 7th of each month), which keep the ~35.3M/90d flow steady. Watch the **ecosystem and community reserves**, the two pools that could push Sell #3 above zero if they deploy into the float faster than the smooth vest. And expect the framework to keep tracking our supply monitor closely — with no mint to argue about, the two readings move together aside from the denominator base.

## Summary

JTO is a capped 1B-supply Solana governance token with no protocol emission, but its float is still growing because a multi-year linear vest keeps releasing already-minted team, investor and ecosystem coins — about 35.3M JTO to the market over 90 days. There is no live buy-side offset: the JIP-38 buyback-and-burn passed Jul 13 2026 but its trading-terminal revenue source is nascent, so it is not yet absorbing supply. That leaves the framework at about +7.15% net, against our supply monitor's +7.70% realized read — a 0.55-point gap that is purely the denominator base, so the page ships with a small monitor-gap note. The key risk is the vest running with no offset; the key ceiling is the fixed 1B cap, which means this inflation ends when the vest does.

*MrNasdog Pressure Framework analysis of Jito (JTO), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 14, 2026.*

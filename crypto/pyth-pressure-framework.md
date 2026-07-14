---
title: "PYTH Inflation Analysis · July 2026 · Big cliff behind it, quiet 90 days ahead"
description: "A MrNasdog Pressure Framework read of Pyth Network (PYTH): the ~2.13B May 2026 cliff is past, the next is May 2027, and only a small buyback moves supply. Framework -0.07% net; monitor +36.6% is the same past cliff on a smaller base."
canonical_url: "https://mrnasdog.com/research/pyth/inflation"
tags: ["crypto", "pyth", "pyth-network", "oracle"]
published: true
---

> Originally published at **[mrnasdog.com/research/pyth/inflation](https://mrnasdog.com/research/pyth/inflation)** by MrNasdog.

Pyth Network's PYTH is a **fixed 10B-supply** Solana oracle token with **no protocol emission** — new supply appears only on annual May vesting cliffs. The big **~2.13B** cliff already unlocked on **May 19 2026**, and the next and final one is not until **May 19 2027**, so the forward 90 days carry **no new vesting at all** — just a small monthly DAO buyback of about **5.4M PYTH**. That leaves the framework at about **-0.07% net** looking forward. Our supply monitor reads **+36.6%** over the trailing window, but that is the past cliff: the **~9.7-point** gap is only the denominator base, so the page carries a monitor-gap note.

## The verdict, in one paragraph

For the window ending July 14 2026, the MrNasdog Pressure Framework reads **PYTH at about -0.07% net** on a forward basis — effectively flat, tilting very slightly deflationary. The reason is timing: the only mechanism that adds PYTH is a **vesting cliff**, and the last one (**~2.13B PYTH**) fired on **May 19 2026**, while the next does not arrive until **May 19 2027**. With no cliff in the forward window and a small **~5.4M PYTH** DAO buyback removing coins, forward supply barely moves. Our supply monitor still shows **+36.6%** over its trailing 90-day window — but that reads the May cliff that is already behind us. The **~9.7 percentage-point** gap between the monitor's trailing figure and the framework's trailing read is not a disagreement about the flow; both sides count the same ~2.13B unlock. It is purely the denominator — the monitor divides by the **90-day-ago float (~5.76B → +36.6%)**, the framework by the **current float (~7.88B → +27.0%)**. PYTH is best characterised as a **capped oracle token between cliffs**: loud once a year, quiet the rest of it.

## Sell pressure: where new PYTH comes from

The key fact about PYTH is that no **new** coins are ever created. Sell #1 — protocol inflation — is **zero**. PYTH has a fixed **10B** max supply, all minted at the November 2023 launch, and Pyth Network pays no block reward or staking reward in PYTH. Every coin that reaches the market is an already-minted allocation coming out of a lock, not fresh issuance.

That leaves Sell #2 — vesting unlocks — as the entire supply story, and for the forward 90 days it is **zero**. PYTH's locked allocations release on four annual cliffs at TGE+6, +18, +30 and +42 months — May 2024, May 2025, May 2026 and May 2027. The **~2.13B** TGE+30-month cliff unlocked on **May 19 2026** (roughly 1.13B to ecosystem growth, ~537M to publisher rewards, the rest to protocol development). Because the framework reads cliffs by date rather than as a trailing average, that unlock counts only in the window it fired — and the next and final cliff is **May 19 2027**, well outside the forward window. So the next 90 days carry no vesting supply. Sell #3 — Foundation and unscheduled unlocks — is zero as a flow: the DAO and ecosystem reserves hold the unlocked-but-undeployed PYTH, but no dated release falls in the window. Sell #4 — long-term locked or bankruptcy — is zero; the ~2.13B still locked simply sits on the published May 2027 cliff, and there is no bankruptcy estate.

## Buy pressure: where new PYTH goes

The one active buy-side mechanism is Buy #1 — programmatic buyback — at about **5.4M PYTH** over 90 days. Under **OP-PIP-115**, approved on **May 13 2026**, the Pyth DAO spends one third of its treasury on open-market PYTH every month through the **PYTH Reserve**, executed by the Pythian Council. The June 2026 on-chain report showed about **1.8M PYTH** bought (~$58K), so at that run-rate roughly 5.4M PYTH is taken off the market per quarter. Crucially, the coins are returned to the DAO treasury and **held in reserve, not burned** — so they are removed from the trading float but not destroyed.

Buy #2 — protocol fee burn — is **zero**: PYTH has no automatic per-transaction burn, and because bought-back coins are held rather than destroyed, nothing is permanently removed from supply. Buy #3 — Foundation buy — is zero, since there is no discretionary open-market buying outside the published monthly program. Buy #4 — new long-term lock — is zero; Pyth's oracle-integrity staking is liquid and is not counted as a lock, and no new escrow of circulating PYTH was announced in the window.

## Foundation and overhang

PYTH's overhang is large and worth naming precisely. The 10B supply is split across **Ecosystem Growth (52%, 5.2B)**, **Publisher Rewards (22%, 2.2B)**, **Protocol Development (10%, 1B)**, **Private Sales (10%, 1B)** and **Community & Launch (6%, 600M)**. Three team-controlled pools carry the watch weight. First, the **DAO / ecosystem-growth treasury**, which holds the unlocked-but-undeployed PYTH from past cliffs — the May 2026 unlock alone routed ~1.13B into ecosystem growth. Second, the **~2.13B still locked**, which is scheduled to unlock on the final May 19 2027 cliff. Third, the **PYTH Reserve**, where the monthly buyback accumulates. None of these is on a discrete dated release inside the window, so the framework books no Sell #3 flow and re-walks the on-chain supply, the unlock schedule and the DAO reports on a roughly bi-weekly cadence. If any of these balances falls into the float faster than expected between refreshes, that outflow enters Sell #3 at the next refresh.

## How PYTH compares to other capped-but-vesting tokens

PYTH sits in the class of **hard-capped tokens with no emission but a staged vesting tail**. That is very different from an uncapped proof-of-stake L1 like Solana itself, which mints new coins as staking rewards every epoch. PYTH issues nothing — its 10B cap is fixed and its mint is spent — so its supply growth is not monetary expansion; it is the mechanical release of coins that already exist but were locked. And unlike a smoothly vesting token, PYTH releases in a few big annual **cliffs** rather than a daily drip, which is why the framework reading swings between a loud month and quiet quarters. On any given 90-day window the answer is almost binary: a cliff is inside it or it is not.

Against exchange and DEX tokens that run mature **buyback-and-burn** programs, PYTH is at an earlier and gentler stage. Those tokens turn real revenue into net-deflationary pressure that can offset or beat their unlocks. PYTH now runs a revenue-funded buyback too, but it **holds rather than burns** and the monthly size (~1.8M PYTH) is tiny against a 7.88B float — so it barely moves the needle today. The comparison that matters over the next year is whether Pyth's data-product revenue scales the buyback fast enough to absorb a meaningful share of the ~2.13B May 2027 cliff. Until then, PYTH is a capped token whose inflation is entirely a calendar question.

## What to watch in the next 90 days

Watch the **monthly PYTH Reserve buyback reports** — the DAO publishes on-chain purchase figures, and a rising monthly size is the only thing that turns forward supply more deflationary. Watch **Pyth's data-product revenue** (Pyth Pro, Core, Entropy, Express Relay), since one third of the treasury funds the buyback and revenue growth directly sizes it. Watch for any **governance proposal to alter the May 19 2027 cliff** — a delay or restructuring of that final ~2.13B unlock would change the one-year picture. Watch the **ecosystem and publisher-reward pools**, the two reserves that could push Sell #3 above zero if they deploy into the float early. And expect the framework to keep tracking our supply monitor: with no mint to argue about, the two readings converge once the May cliff rolls out of the trailing window.

## Summary

PYTH is a fixed 10B-supply Solana oracle token with no protocol emission, so its supply grows only on annual May vesting cliffs. The big ~2.13B cliff already landed on May 19 2026, and the next and final one is not until May 19 2027 — so the forward 90 days carry no new vesting, only a small ~5.4M PYTH monthly DAO buyback that is held in reserve rather than burned. That leaves the framework at about -0.07% net, effectively flat and tilting slightly deflationary. Our supply monitor's trailing +36.6% reads the May cliff that is already behind us; the ~9.7-point gap is purely the denominator base, so the page ships with a monitor-gap note. The key risk is the May 2027 cliff a year out; the key ceiling is the fixed 10B cap, which means PYTH's inflation is a calendar event, not a permanent drip.

*MrNasdog Pressure Framework analysis of Pyth Network (PYTH), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 14 2026.*

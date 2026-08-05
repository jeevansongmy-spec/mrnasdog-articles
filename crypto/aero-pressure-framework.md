---
title: "AERO Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description: "A MrNasdog Pressure Framework read of Aerodrome Finance (AERO): ~55.9M minted per quarter with no cap, no burn and no booked buyback, against 21.5M of vote-locking. Net +3.55%, monitor +4.22%."
canonical_url: "https://mrnasdog.com/research/aero/inflation"
tags: ["crypto", "aero", "aerodrome", "base"]
published: true
---

> Originally published at **[mrnasdog.com/research/aero/inflation](https://mrnasdog.com/research/aero/inflation)** by MrNasdog.

Aerodrome mints a heavy weekly AERO emission, but its vote-escrow lock absorbs most of it before it reaches the market. Over the 90 days to **Aug 5 2026**, on-chain AERO supply grew **55.9M** while the amount locked as veAERO grew **21.5M**, leaving a net **34.4M** reaching the tradable float. On a circulating base of **968.6M AERO** the Pressure Framework reads **+3.55%** net, against our supply monitor's **+4.22%** — a gap of about **0.67 percentage points**, which ships a monitor-gap flag. AERO is a **structurally inflationary, uncapped ve(3,3) emitter** whose float grows far slower than its mint.

## The verdict, in one paragraph

For the 90-day window ending **Aug 5 2026**, the MrNasdog Pressure Framework reads **AERO at about +3.55% net**: sell pressure of **55.9M AERO** in fresh emission against buy pressure of **21.5M AERO** in net new vote-escrow locking, on a circulating base of **968.6M AERO**. Our supply monitor reads **+4.22%** for the same window, a gap of about **0.67 percentage points** — just outside the half-point tolerance, so a monitor-gap flag ships with this page. The gap is a denominator artifact, not a missing flow: reading Aerodrome's AERO token and its veAERO contract on-chain at both ends of the window accounts for every coin — total supply rose from **1,894.0M** to **1,949.9M** (a **55.9M** mint, with no burn), veAERO-locked AERO rose from **959.8M** to **981.3M**, and circulating (defined as total minus veAERO) rose from **934.2M** to **968.6M**. The monitor simply divides that same float growth by a slightly lower 90-day-ago supply base. AERO is best labelled **structurally inflationary on the active float, with vote-escrow locking as the only brake**.

## Sell pressure: where new AERO comes from

It comes from one place: weekly emission. Sell #1 — protocol inflation — is **55.9M AERO** over 90 days, minted by Aerodrome's Minter contract at roughly **4.3M AERO** a week as liquidity-pool rewards. AERO is **uncapped**, and the weekly rate is no longer a fixed decay curve: since the Aero Fed handover, veAERO voters set the emission each epoch within a band of **0.01%** to **1%** of total supply per week, and they have steered it down to about **0.22%** a week. Because AERO has no burn mechanism, the on-chain total-supply increase over the window is exactly the gross emission — there is nothing being destroyed to offset it. That makes AERO a genuine, continuous new-supply engine, in contrast to a capped token that has stopped issuing.

Every other sell row is zero, and each for a clean reason. Sell #2 — vesting unlocks — is **zero** because Aerodrome has no investor or team cliff calendar: the launch allocation was placed into time-locked veAERO at genesis rather than a dated vesting schedule, so nothing unlocks into the market on a fixed date, and the lock expiries that do occur flow through the veAERO contract and are already captured in the net-lock figure. Sell #3 — Foundation and unscheduled unlocks — is **zero** in value: the Aerodrome team takes a share of each week's emission, but those coins are already counted as new supply the instant they are minted, so booking the treasury again would double-count it. Sell #4 — long-term locked or bankruptcy — is **zero**: AERO has no estate, no trustee and no court distribution, and while roughly half of all AERO sits in multi-year veAERO locks, a lock is not a pending sell.

## Buy pressure: where new AERO goes

AERO's only offset is locking, and it is large. Buy #4 — new long-term lock — is **21.5M AERO** over 90 days: the net growth in AERO held by the veAERO vote-escrow contract, where holders lock for up to four years in exchange for voting power over emissions and a share of trading fees. Two flows feed it — new user locks, and the weekly rebase, which is minted straight into existing locks to protect lockers from dilution. Together they absorbed **21.5M** of the **55.9M** minted, so only **34.4M** reached the tradable float. This is the defining feature of the ve(3,3) design: emission and locking run at once, and the net supply that actually reaches the market is the gross mint minus what the lock swallows.

The other three buy rows are zero. Buy #1 — programmatic buyback — is **zero**: Aerodrome runs no buyback, because **100%** of its trading fees are routed to veAERO voters rather than used to buy AERO off the market. Buy #2 — protocol fee burn — is **zero** for the same structural reason: there is no burn, fees are distributed, not destroyed. The Predictive Allocation change launched **Jul 26 2026** does add gauge caps that skip minting some unneeded emissions, but that trims issuance at the source rather than burning existing supply, so it belongs to the emission side, not a burn row. Buy #3 — Foundation buy — is **zero**: there is no discretionary open-market buying of AERO by the team.

## Foundation and overhang

AERO's overhang is unusual: the largest off-float pool is not a team treasury but the **veAERO** lock itself, which holds **981.3M AERO** — about **half** of the **1,949.9M** total supply — in time-decaying locks of up to four years. That is a holder-elected brake rather than a team overhang, and it is growing, not draining. Beyond it, the identifiable team-controlled supply is the emission share the Aerodrome team receives each epoch, which is counted as new supply at the moment of minting and carries no published discretionary-release schedule. There is no vesting contract, no bankruptcy estate and no separate investor unlock calendar.

The rule that governs the team pool is the same one applied everywhere: if the team or treasury balance falls between refreshes in a way not already captured by emission, the outflow enters Sell #3 at the next refresh. The lock side is fully transparent — veAERO holdings are read on-chain each rebuild from the vote-escrow contract, and they stood at **981.3M AERO** on **Aug 5 2026**. Because that pool is locked rather than liquid, it is a monitored brake on supply rather than a wallet that could sell into the market tomorrow.

## How AERO compares to other ve(3,3) DEX tokens

The right comparison class for AERO is the vote-escrow DEX tokens descended from the Solidly ve(3,3) design — the uncapped, continuously emitting exchange tokens where locking, not burning, is the supply brake. What separates them from a token like a capped buyback-and-burn exchange coin is three mechanism choices: whether supply is capped, whether new issuance still runs, and whether fees are used to remove tokens or to reward lockers. AERO sits firmly at the inflationary end. It is **uncapped**, it mints heavily every week, and it burns nothing — its fees go to veAERO voters. The only thing holding its float in check is that about half the supply is locked and net locking keeps pace with a good share of the mint.

Contrast that with a capped exchange token that funds a revenue buyback-and-burn: that token destroys more than it mints and its float shrinks, the mirror image of AERO, whose float grows. AERO is closer to its own lineage — the vote-escrow DEX tokens on other chains that emit continuously and rely on lock rates to soak up issuance. Among those, the honest way to read AERO is that its supply pressure is a race between emission and locking: while about half of AERO stays locked, the net float growth is roughly a third of the gross mint, which is why the framework reads a moderate **+3.55%** rather than the double-digit figure the raw emission would imply. The risk is directional — if lock rates fall, more of that **55.9M**-per-quarter mint reaches the market, and the rebase formula deliberately pays lockers more when locking declines, precisely to prevent that.

## What to watch in the next 90 days

First, the veAERO lock rate. With about half of supply locked, the single biggest swing factor is whether that share rises or falls — a drop pushes more of the weekly mint onto the float and lifts the net reading, a rise suppresses it. Second, the Aero Fed emission votes: veAERO voters reset the weekly emission each epoch within the **0.01%**–**1%** band, so a run of votes to raise or cut issuance changes Sell #1 directly. Third, the **Predictive Allocation** rollout that went live **Jul 26 2026** — its gauge caps that skip minting unneeded emissions could quietly lower the effective mint over the coming quarter, which would be structurally deflationary for the float. Fourth, the announced Aerodrome–Velodrome protocol consolidation — worth watching for any token-migration mechanics, though AERO's on-chain supply showed no migration spike through this window. Fifth, large lock expiries, which would return locked AERO to the float in lumps.

## Summary

AERO is a structurally inflationary, uncapped ve(3,3) token whose growth is tempered by locking rather than burning. Aerodrome mints about **55.9M AERO** a quarter as liquidity rewards and has no buyback or burn, but net vote-escrow locking of about **21.5M** over the same window keeps most of that supply off the market, leaving a net **+3.55%** change in the float and a projected **+3.55%** for the next 90 days. That reads slightly softer than our supply monitor's **+4.22%**, a **0.67-point** gap that is a denominator artifact rather than a missing flow. The key risk is not a hidden unlock but the lock rate itself: with no cap and no burn, AERO's float stays contained only for as long as roughly half of it remains locked.

---

*MrNasdog Pressure Framework analysis of AERO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 5 2026.*

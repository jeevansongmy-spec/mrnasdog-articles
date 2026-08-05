---
title:         "NEXO Inflation Analysis · August 2026 · Supply flat, projected to stay flat"
description:   "Net flat: a fixed 1B supply with no mint, vesting or unlocks, and a revenue buyback that sat idle this window. Framework 0.00% / 90D; monitor -0.004%."
canonical_url: "https://mrnasdog.com/research/nexo/inflation"
tags:          ["crypto", "nexo", "cefi", "exchange-token"]
published:     true
---

> Originally published at **[mrnasdog.com/research/nexo/inflation](https://mrnasdog.com/research/nexo/inflation)** by MrNasdog.

**TL;DR.** Nexo Token has one of the cleanest supply profiles in the Pressure Framework. NEXO is a fixed **1,000,000,000** token supply, minted in full at genesis, with no mint function and no vesting calendar left to run down. Over the last 90 days the framework reads **0.00% net** — nothing added and nothing removed — against a supply monitor at **-0.004%**, a gap of just **0.004 percentage points**. The one mechanism that could have moved the number, Nexo's well-known open-market buyback, did not fire this window: the reserve where repurchased tokens accumulate held the same balance at both ends of the period, unchanged since 2023. NEXO is a fixed, fully-circulating supply with no live inflation and a currently-dormant buyback.

## The verdict, in one paragraph

For the 90-day window from **May 7 2026** to **Aug 5 2026**, the Pressure Framework reads **NEXO at 0.00% net**: sell pressure of **zero** against buy pressure of **zero**, on a tradable base of **1,000,000,000 NEXO**. Our supply monitor reads **-0.004%** for the same period — a gap of just **0.004 percentage points**, well inside the framework's half-point tolerance, so the page ships clean with no conflict flag. Both readings describe the same thing: a supply that does not move. Nexo Token has no issuance, no vesting cliff and no unlock schedule, and the one mechanism that could change the picture — the open-market buyback — sat idle. NEXO is best labelled a **fixed-supply exchange token, fully circulating, with no live inflation**.

## Sell pressure: where new NEXO comes from

Sell #1 — protocol inflation — is **zero**, and it is a hard structural zero. Nexo Token has no mint function: there is no chain paying validators in NEXO, no staking curve that issues new NEXO, and no inflation rule anywhere in its design. The token was distributed from a fixed allocation of **1,000,000,000**, and the on-chain total supply reads exactly that figure and cannot change. On a page whose entire question is how much new supply reaches the market, NEXO answers it at the source: none is created.

Sell #2 — vesting unlocks — is also **zero**, and unlike most tokens this is not a quiet zero waiting on a schedule. There is no vesting schedule. The full **1B NEXO** was unlocked at launch, every unit already circulates, and independent tokenomics coverage describes NEXO as having no vesting overhang and no future dilution — one of the cleanest supply profiles among top-100 assets. No cliff exists to push new NEXO to the market in the next 90 days or ever. Sell #3 — foundation and unscheduled unlocks — is **zero** on observed behaviour, with the tracked reserve enumerated below. Sell #4 — long-term locked or bankruptcy — is **zero**: Nexo is a going concern, and no estate, trustee schedule or court-ordered distribution touches NEXO.

## Buy pressure: where new NEXO goes

Buy #1 — programmatic buyback — is the mechanism NEXO is known for, and it reads **zero** this window because the buyback did not fire. Nexo's Board runs a discretionary, revenue-funded open-market repurchase, and past programmes were sizeable — a **$12M** buyback in 2020, a **$100M** programme in 2021 and a further **$50M** in 2022. Repurchased NEXO lands in a reserve wallet the framework reads directly. That reserve held about **114.8M NEXO** at the start of the window and the identical balance at the end, and it has been unchanged since 2023, so no NEXO was bought off the market in the last 90 days. A live buyback would show NEXO flowing into that reserve; nothing did.

The remaining buy rows are zero for structural reasons. Buy #2 — protocol fee burn — is **zero**: NEXO has no fee burn, no chain charges NEXO for gas, and there is no burn function in the token. Repurchased NEXO is held in the reserve and recycled into interest payouts, never destroyed, so even when the buyback runs it removes nothing permanently. Buy #3 — foundation buy — is **zero**: Nexo's own purchases are exactly the buyback in row one, which did not fire, and no other Nexo purchase into a counted wallet is disclosed. Buy #4 — new long-term lock — is **zero**: Nexo's loyalty and earn products pay out of existing balances, and no new escrow or lockup contract was created for NEXO this window.

## Foundation and overhang

Nexo Token carries one clearly identified on-chain reserve, holding about **114.8M NEXO** and read on-chain at every rebuild. It is where the buyback accumulates repurchased tokens, and it has been static since 2023 — its balance did not move across this 90-day window, and cross-checking older blocks shows it grew from about **51.6M NEXO** in mid-2022 to its current level by early 2023 and has not changed since. Two things make it a reserve rather than a supply threat. First, it already sits **inside** the counted circulating supply, because the framework's classifier counts the full **1B NEXO** as circulating; a different data provider excludes company-held tokens and counts only about **646M**, but on the figure this framework uses those tokens are already in the denominator. Second, the reserve's historical use is recycling NEXO into interest payouts, not dumping it on an order book. If that reserve's balance ever falls toward the open market between refreshes, the outflow enters Sell #3 at the next refresh — but this window it did not move.

## How NEXO compares to other exchange tokens

The natural peer group is exchange and platform tokens with buyback programmes, and NEXO sits at the passive end of it. The classic exchange-token model is a revenue-funded buyback-and-burn: the venue takes a slice of profit, buys the token on the open market, and destroys what it buys, so the burn is both a bid and a permanent supply cut. NEXO's buyback is different in two ways — it accumulates rather than burns, holding repurchased tokens in a reserve that later recycles into interest payouts, and this window it did not run at all. That makes NEXO neither a deflation story nor a dilution story: there is no burn shrinking the float and no issuance expanding it.

Against the fee-burn chains, the contrast is sharper still. A base-fee-burning Layer 1 removes a circulating balance with every block and can genuinely shrink supply; NEXO has no fee burn and no live issuance either way, so its supply simply holds at a fixed billion. And unlike an uncapped continuous-emission chain, NEXO cannot dilute holders even slightly, because there is nothing to emit. So Nexo Token is best read as a fixed, fully-distributed supply whose only supply-side variable is a discretionary buyback that is currently dormant — closer to a capped, mint-less asset than to either a deflationary burner or an inflating L1.

## What to watch in the next 90 days

First, whether the buyback restarts — a new tranche would show NEXO flowing into the reserve, and the number to watch is how much and whether those tokens are held or eventually recycled. Second, that reserve's balance of about **114.8M NEXO**, read on-chain each rebuild, and any move out of it toward a trading venue, which would turn Sell #3 non-zero. Third, the Coinbase listing review Nexo entered in **May 2026**, which affects liquidity and demand rather than supply but could change how the token trades. Fourth, any EU/MiCAR compliance or corporate-structure change that touches how company-held NEXO is classified — a reclassification could move the circulating figure without a single token changing hands. Fifth, any first-ever vesting or lock announcement, which there is currently no sign of.

## Summary

The MrNasdog Pressure Framework reads Nexo's NEXO at **0.00%** net supply change over the last 90 days and projects the same for the next 90 — flat, not deflationary. NEXO has no mint function, no vesting schedule and no unlocks, so the full **1B NEXO** already circulates and sell pressure is a hard zero. Its discretionary open-market buyback — the one mechanism that could bend the number — did not fire this window: the reserve where repurchased tokens accumulate held steady at about **114.8M NEXO**, unchanged since 2023. With our monitor reading **-0.004%** against the framework's **0.00%**, the two agree that NEXO's supply does not move. The thing to watch is not inflation, which is absent, but whether the buyback ever wakes up.

---

*MrNasdog Pressure Framework analysis of NEXO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 5 2026.*

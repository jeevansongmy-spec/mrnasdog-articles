---
title: "FET Inflation Analysis · August 2026 · Supply barely growing on a migration tail"
description: "A MrNasdog Pressure Framework read of FET (ASI Alliance): no protocol inflation on a fixed 2.71B cap, ~7.5M/90d migration unlocks, no burn and no buyback. Framework +0.34% net; monitor -1.28%."
canonical_url: "https://mrnasdog.com/research/fet/inflation"
tags: ["crypto", "fet", "fetch-ai", "ai"]
published: true
---

> Originally published at **[mrnasdog.com/research/fet/inflation](https://mrnasdog.com/research/fet/inflation)** by MrNasdog.

FET, the token of the Artificial Superintelligence Alliance, is a capped, fully-merged asset with almost no supply pressure left. Over the 90 days to **Aug 9 2026** the only new supply is a leftover merger-migration drip of about **7.5M FET**, against no burn and no buyback, on a circulating base of **2.23B FET**. The Pressure Framework reads **+0.34%** net, versus our supply monitor's **-1.28%** — a gap of about **1.62 percentage points** that ships a monitor-gap flag. FET is a **fixed-cap AI token whose float barely moves**: no new minting, no burn, and a merger unlock schedule that is nearly complete.

## The verdict, in one paragraph

For the 90-day window ending **Aug 9 2026**, the MrNasdog Pressure Framework reads **FET at about +0.34% net**: sell pressure of roughly **7.5M FET** in scheduled merger-migration unlocks against zero structural buy pressure, on a circulating base of **2.23B FET** and a fixed maximum of **2,714,384,546 FET**. Our supply monitor reads **-1.28%** for the same window, a gap of about **1.62 percentage points** — well outside the half-point tolerance, so a monitor-gap flag ships with this page. The gap is a classification artifact, not a missing flow: FET's total supply is pinned to its cap with no mint and no burn, so a monitor reading that shows circulating **falling** can only reflect the market's supply classification shifting float into staked and locked buckets, not tokens being destroyed. FET is best labelled **a fixed-cap, post-merger token with a near-flat float**.

## Sell pressure: where new FET comes from

Almost nowhere. Sell #1 — protocol inflation — is **zero**, and that is the defining fact about FET. The Artificial Superintelligence Alliance raised FET's maximum supply exactly once, to accommodate the merger of Fetch.ai with AGIX and OCEAN, and that ceiling is now a hard **2,714,384,546 FET**. On-chain total supply has reached the cap, so the Fetch.ai mainnet mints no new FET; staking rewards, earned by the roughly **20%** of supply delegated on the mainnet, are paid out of already-issued tokens rather than freshly minted ones. There is no continuous emission engine here at all.

The only live sell row is Sell #2 — vesting unlocks — at about **7.5M FET** over 90 days. This is the tail of the merger migration: holders still converting AGIX and OCEAN into FET at their fixed swap ratios draw down the remaining locked allocation at roughly **2.5M FET** a month, with the next cliff of **2.51M FET** scheduled for **Aug 28 2026**. Against a **2.23B** float this is a trickle. Sell #3 — Foundation and unscheduled unlocks — is **zero** in value: the locked remainder of about **483M FET** sits in the Foundation, founder, mining-reserve and Future-Releases pools, none of which fired an observed release this window. Sell #4 — long-term locked or bankruptcy — is **zero**: AGIX, OCEAN and CUDOS folded into FET by fixed-ratio swaps, not through any insolvency, so there is no estate distributing tokens.

## Buy pressure: where new FET goes

There is no structural buy pressure, and this is the other half of why FET's float is so quiet. Buy #1 — programmatic buyback — is **zero**: the Alliance runs no buyback and does not spend revenue or reserves to repurchase FET on the open market. Buy #2 — protocol fee burn — is **zero**: FET has no burn mechanism, and Fetch.ai mainnet transaction fees are routed to validators and stakers rather than destroyed. That absence matters — with no burn, the fixed cap is the only ceiling, and nothing pulls supply back down once it is out.

Buy #3 — Foundation buy — is **zero**: there is no evidence of discretionary open-market FET buying by the Foundation or team. Buy #4 — new long-term lock — is **zero** as well: staking does lock FET on the mainnet, but there is no announced program committing a fixed quantum of new locks, so nothing is being pulled off the tradable float on a schedule. In net terms, the buy ledger is empty, and the small migration drip on the sell side has nothing offsetting it — which is exactly why the framework reads a faint positive rather than a flat zero.

## Foundation and overhang

FET's overhang is the roughly **483M FET** — about **18%** of the **2,714,384,546** cap — that is still locked. The **Future-Releases** reserve, near **7.6%** of supply, vests linearly over 60 months into Foundation control rather than straight to the market; the Foundation and founder allocations, each close to **8.8%**, and a mining reserve near **6.6%**, round out the identified team-controlled pools. All four are tracked as overhangs, and all four showed no discretionary firing in this window, which is why each sits at a value of zero rather than a projected number.

The rule that governs these pools is the same one applied everywhere: if any of the Foundation, founder, mining-reserve or Future-Releases balances falls between refreshes in a way not already captured by the migration schedule, that outflow enters Sell #3 at the next refresh. For now the schedule is dominated by the merger-migration tail, which is nearly exhausted — the network is roughly **97%** unlocked — so the overhang is a slow-drip watch item, not an imminent supply event.

## How FET compares to other capped AI tokens

The right comparison class for FET is capped, fixed-supply utility tokens — assets whose issuance is finished and whose supply moves only as pre-allocated locks vest, in contrast to the uncapped, continuously emitting Layer-1s and DEX tokens that mint fresh supply every block or every week. On that axis FET sits at the calm end. It is **capped** at **2.71B**, its merger mint is complete, and with roughly **97%** of supply already unlocked, the scheduled drip left is tiny. Where an uncapped emitter has to lock or burn aggressively just to hold its float steady, FET holds steady by default because nothing new is being made.

What makes FET distinct even among capped tokens is that it carries no burn and no buyback, so it has no deflationary lever either — it is capped-but-flat rather than capped-and-shrinking like a revenue buyback-and-burn exchange token. Its supply story is also unusually consolidated: three separate token emissions (Fetch.ai's FET, SingularityNET's AGIX, and Ocean Protocol's OCEAN, with CUDOS joining later) were merged into one fixed cap, so the combined unlock calendar is what to read, not three overlapping ones. The honest way to characterise FET is that its inflation is essentially spent: the pressure that remains is a thin migration tail and whatever the Foundation chooses to deploy from its reserves, not a mechanical emission.

## What to watch in the next 90 days

First, the merger-migration cliffs: the next is **2.51M FET** on **Aug 28 2026**, with similar releases around Sep 28 and Oct 28 2026 — small, but the clearest scheduled supply events. Second, the Future-Releases reserve, which vests toward Foundation control on a 60-month linear schedule and would move into Sell #3 the moment any of it is deployed to the market. Third, the ongoing **Ocean vs Fetch** dispute over the OCEAN Foundation's allocated ASI tokens — a governance and treasury fight that has not touched the FET contract with any mint or burn, but that is worth watching for any forced token movement. Fourth, any Alliance announcement of a buyback, burn or new staking-lock program, which would be the first structural buy row FET has ever carried. Fifth, shifts in the staked share, since a large move in and out of staking is what pushes the monitor's classification-driven reading around.

## Summary

FET is a fixed-cap, post-merger AI token whose supply is essentially spent. The Artificial Superintelligence Alliance raised the maximum to **2,714,384,546 FET** once for the merger and mints nothing beyond it, and with no burn and no buyback, the float moves only on a thin merger-migration drip of about **7.5M FET** a quarter — leaving a net **+0.34%** read and the same projected for the next 90 days. That runs above our supply monitor's **-1.28%**, a **1.62-point** gap that is a classification artifact rather than a real burn, since FET has no mechanism to destroy tokens. The key risk is not emission but discretion: with roughly **483M FET** still in Foundation and reserve pools, what to watch is deployment, not minting.

*MrNasdog Pressure Framework analysis of FET (Artificial Superintelligence Alliance), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 9 2026.*

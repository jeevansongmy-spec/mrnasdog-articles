---
title: "KITE Inflation Analysis · August 2026 · The cliff just moved inside the window"
description: "Kite is hard-capped and mints nothing, yet four on-chain escrows released ~161M KITE and the Nov 3 2026 cliff now lands inside the forward window. Framework +6.73% last, +44.29% next; monitor +5.52%."
canonical_url: "https://mrnasdog.com/research/kite/inflation"
tags: ["crypto", "kite", "ai-payments"]
published: true
---

*Originally published at [mrnasdog.com/research/kite/inflation](https://mrnasdog.com/research/kite/inflation)*

Kite is a hard-capped **10B** AI-payments Layer-1 that mints no new coins — yet its tradable float grew about **+6.73%** over the last 90 days, and the Pressure Framework projects about **+44.29%** for the next 90. The driver is vesting, not emission: four on-chain Kite escrows released about **161M KITE** to the market between **May 12 2026** and **Aug 10 2026**, and the twelve-month team and investor cliff of **800M KITE** on **Nov 3 2026** now falls inside the forward window. There is **no buyback** and **no fee burn** — Kite gas is paid in stablecoins — so nothing offsets it. Our monitor reads **+5.52%** for the same historical window, a gap of **1.21 percentage points**, so a monitor-gap flag ships. KITE is a thin-float young Layer-1 whose unlock calendar, not its cap, is the entire supply story.

## The verdict, in one paragraph

For the 90 days to **Aug 10 2026** the Pressure Framework reads KITE at **+6.73%** net supply growth and projects **+44.29%** for the next 90 days. Our monitor reads **+5.52%** for the historical window, a gap of **1.21 percentage points**, which is over tolerance and triggers the flag. The gap is a timing difference, not a dispute about facts: the four Kite vesting escrows drain continuously on-chain, while the classified float moves in monthly steps and last stepped on **Jul 1 2026**, with no August step posted yet. The forward number is the one that matters. Kite's team and investor allocations sit behind a twelve-month cliff dated **Nov 3 2026**, five days inside a window that closes **Nov 8 2026**, and that cliff releases **800M KITE** onto a float of only **2.39B**. KITE is best labelled a **hard-capped, cliff-driven Layer-1** whose dilution is entirely a vesting schedule.

## Sell pressure: where new KITE comes from

Kite has no protocol inflation at all. KITE is **hard-capped at 10B** and every unit was created at the **Nov 3 2025** launch, so the Kite chain issues nothing new — on-chain total supply held flat across the window, and the **protocol inflation** row is zero. Even the staking and module rewards Kite pays to validators, module owners and delegators come out of allocations that already exist rather than from a mint, so they surface as vesting rather than as emission.

That makes **vesting unlocks** the entire sell story. Only about **24%** of KITE circulates, and the Ecosystem & Community and Modules allocations release a slice each month. The published Kite calendar bills roughly **328M** for a 90-day window, but the tokens sit in readable on-chain escrows, and the calendar overstates what actually leaves them. Reading the four Kite escrow contracts at both ends of the window shows a realised release of about **161M KITE** — the honest figure, because tokens that vested on paper but never left the contract are not on the market yet.

The shape of that release matters as much as its size. The four escrows were completely still from the **Nov 3 2025** launch until **Jun 16 2026** — six weeks after Kite mainnet and Agent Passport went live on **Apr 30 2026** — and have drained almost every few days since, at about **2.9M KITE** a day. That post-launch pace, not the dormant first half of the window, is what the framework carries into the next 90 days, giving roughly **259M** of ordinary monthly release.

On top of it sits the cliff: Kite puts team and investors on a one-year cliff with a four-year unlock, and a quarter of that **3.2B** pool — **500M** for the team and **300M** for investors — becomes claimable on **Nov 3 2026**. That is **800M**, not the whole 3.2B pool, and it is the single number that changes this quarter's reading. Together with the continuous release it is **1,059M KITE** of forward vesting supply.

The remaining two sell rows are empty. **Foundation and unscheduled unlocks** is zero because nothing discretionary fired: no Kite wallet outside the scheduled escrows moved a token in the window. **Long-term locked or bankruptcy** is zero because Kite launched in late 2025 and there is no estate, no trustee and no court-supervised seller anywhere in its history.

## Buy pressure: where new KITE goes

Nowhere. All four buy rows on the Kite ledger read zero, and three of them are structural rather than circumstantial. **Programmatic buyback** is zero: Kite describes an option to swap AI-service commissions for KITE on the open market, but no buyback contract has executed, no dashboard reports one and no dated amount has ever been disclosed — the ability to buy is not the same as buying, so the row stays at zero and stays watched.

**Protocol fee burn** is zero by design and is the single most important structural fact on the buy side: Kite denominates and charges network gas in **stablecoins**, not in KITE, precisely so agents face predictable costs. That choice is good for the payment product and bad for the token's supply, because it means no amount of Kite network activity ever destroys a single KITE the way a base-fee burn does on a gas-token chain.

**Foundation buy** is zero as well — the Kite foundation is a holder and distributor of supply, not a buyer, and no open-market purchase has been observed on-chain or disclosed. **New long-term lock** is also zero: staking KITE secures modules on the new Kite mainnet and does lock tokens for as long as they are staked, but no lock-up programme, staking cap or dedicated lock contract with a stated size was announced in the last 90 days, and a rolling staking balance is not a lock event with a quantum. The practical consequence is that KITE's ledger is one-sided. Whatever the vesting escrows release reaches the float in full, because the protocol has built nothing on the other side of the trade.

## Foundation and overhang

The overhang is the dominant fact about KITE, and it is unusually legible because every pool is a readable address. The Kite investor vault holds exactly **1,200M KITE** — the full 12% investor allocation — and has never moved a single token since launch. Three cliff-locked team wallets hold **800M**, **500M** and **500M**, and are equally still; together with the investor vault they are exactly **3,000M KITE**, all of it behind the **Nov 3 2026** cliff. Separately, the four distribution escrows that feed the monthly release still hold **3,035M KITE** between them, down from **3,196M** at the start of the window. And because the realised release is running under the published calendar by roughly **69M** a quarter, an undrawn backlog is quietly accumulating inside those same escrows rather than draining away.

None of that is booked as sell pressure today, because the framework books flow and not capacity. All of it is tracked. The chain balances are re-read on every rebuild, and the rule is simple: if any of these Kite balances falls between refreshes, the outflow enters the Foundation and unscheduled unlocks row at the next refresh. Set against a circulating float of **2.39B**, the identified overhang is more than **6,000M KITE** — roughly two and a half times everything that trades today.

## How KITE compares to other fixed-cap chains

KITE looks superficially like the strongest class of supply story: a hard cap, no emission curve, no perpetual block reward. Bitcoin has that shape, and so do the capped exchange tokens. But a cap only constrains the endpoint; it says nothing about the path. Bitcoin's cap arrives alongside a fully distributed float, so the cap and the tradable supply are nearly the same number. Kite's cap arrives with only about a quarter of supply in circulation, which means the binding constraint on KITE is not the 10B ceiling but the schedule that walks the remaining **7.6B** toward it. Against a halving-model chain, KITE's dilution is far larger in the near term and zero in the long term; against an uncapped continuous-emission Layer-1, KITE is more diluting today and materially cleaner in a decade.

The sharper comparison is against fixed-cap chains that burn. A gas-token Layer-1 with a base-fee burn converts network usage directly into supply destruction, so growth in activity partially self-funds the token. Kite deliberately gives that up: charging gas in stablecoins removes fee volatility for AI agents, which is the right product decision for a payments chain, but it severs the link between Kite network usage and KITE supply. The exchange tokens that run quarterly buy-and-burn programmes sit at the opposite pole — capped, and actively shrinking. KITE is capped and actively growing. Among young Layer-1s launched in the last year, the closest structural analogues are the other thin-float, cliff-heavy launches whose first anniversary is the real event; the useful lesson from that class is that the twelve-month cliff, not the token design, is what the market prices.

## What to watch in the next 90 days

The single dated event that dominates everything is **Nov 3 2026**, when the twelve-month cliff makes **800M KITE** claimable across the team and investor allocations — watch whether the investor vault that has held exactly **1,200M** since launch moves at all in the days after. Before that, three ordinary monthly escrow releases land on **Sep 1 2026**, **Oct 1 2026** and **Nov 1 2026**, each around **86M KITE** at the current realised pace.

Watch whether that pace holds: it has been accelerating, with about **54M** leaving the escrows in the single week to **Aug 3 2026**, and a sustained step up would push the forward reading higher still. Watch, too, whether the gap between the calendar and the realised release keeps widening, because a draining backlog and an accumulating one imply very different next quarters. Finally, watch for any Kite announcement that turns the commission-swap option into an actual buyback with a published address and a dated amount — that is the only thing on the roadmap that could put a number in the buy column.

## Summary

The MrNasdog Pressure Framework reads KITE at **+6.73%** net supply growth over the last 90 days and projects **+44.29%** for the next 90, against a monitor reading of **+5.52%** and a monitor-gap flag for the **1.21 percentage point** difference. The mechanism is unusually clean: Kite mints nothing, so all of that growth is locked supply being released, measured directly from four readable on-chain escrows that put about **161M KITE** on the market in the historical window. The key risk is a date, not a trend — the **Nov 3 2026** twelve-month cliff releases **800M KITE** onto a **2.39B** float, with no buyback and no fee burn on the other side because Kite charges gas in stablecoins. The ceiling is real and permanent at **10B**, but with more than **6,000M KITE** of identified overhang still locked, that ceiling is a promise about the end of the decade rather than a constraint on the next year.

---

*MrNasdog Pressure Framework analysis of KITE, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 10 2026.*

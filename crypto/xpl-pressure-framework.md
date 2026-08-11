---
title:         "XPL Inflation Analysis · August 2026 · Six weeks from a 1.67B cliff"
description:   "Plasma mints nothing, yet the framework reads +77.07% net for the next 90 days — a 1.67B team and investor cliff lands Sep 25 2026 against a float of 2.69B, with no buyback, no staking sink and a burn that destroys under one XPL a quarter."
canonical_url: "https://mrnasdog.com/research/xpl/inflation"
tags:          ["crypto", "xpl", "plasma", "stablecoin"]
published:     true
---

*Originally published at [mrnasdog.com/research/xpl/inflation](https://mrnasdog.com/research/xpl/inflation)*

Plasma does not mint XPL. All **10,000,000,000 XPL** were created at mainnet beta on **Sep 25 2025**, and the validator reward inflation written into the design has never been switched on. Every unit of supply pressure on XPL is therefore a release calendar — and that calendar is about to do something extreme. Three monthly ecosystem tranches added **266.7M XPL** in the 90 days to **Aug 11 2026** against zero buy-side absorption, and the next 90 days schedule **2.07B XPL**, including the one-year cliff on **Sep 25 2026** that frees **1.67B XPL** of team and investor tokens in a single day. The MrNasdog Pressure Framework reads net supply at **+9.92%** for the trailing window and **+77.07%** for the forward one, against a supply-monitor reading of **+7.16%**.

## The verdict, in one paragraph

For the 90 days to **Aug 11 2026** the framework reads **XPL at +9.92% net**, and projects **+77.07%** for the 90 days to **Nov 9 2026**. The supply monitor reads **+7.16%** for the trailing window, so the gap is **2.75 percentage points** — past the framework's half-point tolerance, and the XPL overview therefore carries a monitor-gap chip. That gap is arithmetic, not disagreement about the mechanism: the classified-supply series over-counted three monthly tranches earlier in 2026 and reversed **128.0M XPL** of it on **Jun 11 2026**, so one full tranche of this window's release had already been booked before the window opened, and a further half-point comes from the two readings dividing by different points in the supply series. XPL is best characterised as **a zero-issuance chain that is nonetheless one of the most inflationary tokens in coverage**, because its float is unlock-driven and nothing on the other side absorbs it.

## Sell pressure: where new XPL comes from

The first thing to establish about Plasma inflation is that no XPL is being created. The protocol's own tokenomics states that validator rewards begin at **5%** annual inflation and step down half a point a year to a **3%** baseline, and that this only activates once external validators and stake delegation go live. They have not. The node-operator documentation still describes consensus participation as something that begins after mainnet, with no fixed timeline available. Sell #1, protocol inflation, is therefore **zero** — and that is the single most misread fact about XPL, because a token can carry a headline inflation rate of nearly ten percent a quarter without a mint function ever firing.

Sell #2, vesting unlocks, carries the entire ledger at **266.7M XPL** for the trailing window and **2.07B XPL** for the forward one. The mechanics are simple. Plasma's Ecosystem and Growth allocation is 40% of supply — 4B XPL — of which 800M was free at launch and the remaining 3.2B releases monthly across three years, which works out to **88,888,889 XPL** on the 25th of every month. Three of those landed inside this window, on **May 25 2026**, **Jun 25 2026** and **Jul 25 2026**. Three more land in the forward window.

That tranche figure was corrected in this build, and it is worth showing the working, because an earlier read had the monthly step near 64M and the whole page turns on it. Three independent proofs agree on 88.9M. First, arithmetic: 1,800,000,000 free at launch plus ten monthly tranches of 88,888,889 equals 2,688,888,890 — reproducing the published circulating figure of **2,688.89M** to eight significant figures, which a 64M step cannot do. Second, the chain: the on-chain balance series steps down by **88.7M** and **91.3M** on the tranche dates themselves, not by two thirds of that. Third, contemporaneous coverage of the next scheduled tranche quotes 88.89M. The monthly release is 88.9M, and the trailing window contains exactly three of them.

Then comes the cliff. Team and Investors hold 25% each, and one third of both allocations unlocks on the one-year anniversary of mainnet beta, **Sep 25 2026**. That is **833.3M XPL** from the team side and **833.3M XPL** from the investor side, released together — roughly **62%** of everything currently trading. The remaining two thirds of both allocations then begin monthly release, adding **138.9M XPL** on **Oct 25 2026** before the window closes.

Sell #3, foundation and unscheduled unlocks, is **zero**, but not because there is nothing to watch. Reading Plasma's largest holders at both ends of the window shows exactly the calendar and nothing else: the main treasury fell from 2.83B to **2.65B XPL**, a second distribution wallet fell from 1.73B to **1.48B XPL**, and a third wallet holding precisely **2.50B XPL** — one whole 25% allocation — has not moved a single token since launch. Those outflows are the tranches already booked in Sell #2, and counting them again would invent pressure. Sell #4, long-term locked or bankruptcy, is **zero** as well: Plasma launched in September 2025 with a clean cap table, there is no estate distributing tokens, and no lock contract exists on the chain.

## Buy pressure: where new XPL goes

Every buy row on XPL is **zero**, and that is the finding that turns a normal unlock schedule into an extreme reading. Buy #1, programmatic buyback, is zero: Plasma has never announced or funded a buyback, and no wallet on the chain is repurchasing XPL. Buy #3, foundation buy, is zero for the same reason and one better — both large treasury wallets only sent XPL out during this window, and neither received an inbound transfer. Buy #4, new long-term lock, is zero because there is nothing to lock into: staking and delegation are not open, so a holder who wants to take XPL off the market has no contract to deposit it in.

Buy #2, protocol fee burn, is the interesting zero. Plasma does burn base fees, exactly as Ethereum does — the base fee on every transaction is destroyed rather than paid to a validator. But reading the chain across this window, the base fee sits at single-digit units of the smallest denomination, and the blocks that do carry heavy gas still burn a vanishing amount. A full quarter of Plasma blocks destroys well under one XPL. The reason is the product itself: Plasma's flagship feature is gas-sponsored stablecoin transfers, so the users generating the most activity never bid the base fee up. The burn is live, correctly implemented, and removes nothing.

## Foundation and overhang

Four team-controlled pools are tracked on XPL, and together they hold most of what has not yet reached the market. The main treasury holds **2.65B XPL** and released 184.5M in this window. A distribution wallet holds **1.48B XPL** and released 248.5M. A third wallet holds an untouched **2.50B XPL**. A fourth reserve holds **555.6M XPL** and has never moved. Critically, none of these is a lock contract — Plasma's locked supply sits in ordinary wallets, so the release calendar is enforced by custody rather than by code, and nothing on-chain would prevent the Sep 25 2026 cliff from arriving in full.

Where the tokens went is worth watching too: of the 433.0M that left the two treasuries this window, 150.0M was bridged off Plasma entirely through a cross-chain adapter, and 191.7M landed in a freshly created wallet that has not moved since. If any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How XPL compares to other stablecoin-settlement chains

Plasma competes directly with the incumbent stablecoin-settlement chains, and its supply structure is the mirror image of theirs. The established stablecoin rail burns a meaningful share of the fees its transfers generate, because those transfers are not sponsored — users pay, and the payment partially destroys supply. Plasma made the opposite product choice: sponsored transfers are the reason to use the chain, which is defensible as a growth strategy and fatal as a supply mechanism. The burn cannot scale with usage if usage is free.

Against uncapped continuous-emission Layer 1s, XPL looks better on paper and worse in practice. Those chains mint constantly, but they mint slowly and predictably, and most of them pair issuance with a staking contract that locks a large fraction of the float back up. XPL mints nothing at all, yet its float is scheduled to grow by more than three quarters in a single quarter, with no staking sink to catch any of it. Against hard-capped halving-model coins the contrast is starker still: a fixed cap only helps if the coins are already distributed, and XPL has **73%** of its supply still to release. The right structural comparison for XPL today is not another chain at all — it is a recently listed token in the middle of its first insider vest, where the only question that matters is how much of the unlocked supply the recipients choose to sell.

## What to watch in the next 90 days

**Aug 25 2026** — the next monthly ecosystem release, **88.9M XPL**, the routine baseline against which the cliff should be judged. **Sep 25 2026** — the one-year cliff, **1.67B XPL** of team and investor tokens plus the month's **88.9M** ecosystem tranche; whether the recipient wallets move or sit still is the single most important observation on this token. **Oct 25 2026** — the first post-cliff monthly release, **227.8M XPL** across all three schedules combined, which sets the new running rate through 2028. Any date — the activation of external validators and stake delegation, which would switch on **5%** annual issuance for the first time but would also, for the first time, give XPL a staking contract capable of absorbing float. And on an ongoing basis, whether Plasma announces any buy-side mechanism at all; today there is none.

## Summary

The MrNasdog Pressure Framework reads Plasma (XPL) as **supply growing, projected to keep growing**: **+9.92%** net over the 90 days to **Aug 11 2026** and **+77.07%** projected to **Nov 9 2026**. The mechanism is unusual — no mining, no staking issuance, no mint function firing at all — so all of that growth comes from a published unlock calendar releasing pre-created supply, and none of it is offset, because XPL has no buyback, no staking lock, and a base-fee burn made immaterial by gas-sponsored stablecoin transfers. The key risk is concentrated on one date: **Sep 25 2026**, when **1.67B XPL** of team and investor tokens come free at once against a float of **2.69B**. The ceiling is fixed at **10B XPL** and cannot rise, but **73%** of that ceiling is still to be distributed, which makes the cap far less protective than it sounds.

---

*MrNasdog Pressure Framework analysis of XPL, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 11 2026.*

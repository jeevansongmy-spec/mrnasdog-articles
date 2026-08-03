---
title: "CHZ Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description: "Chiliz Chain minted 156.1M CHZ in 90 days and drained a 58.9M project reserve into the market against a 28.9M buyback-burn. Framework reads +1.78% net, monitor +1.19%, forward +1.23%."
canonical_url: "https://mrnasdog.com/research/chz/inflation"
tags: ["crypto", "chz", "chiliz", "fantokens"]
published: true
---

> Originally published at **[mrnasdog.com/research/chz/inflation](https://mrnasdog.com/research/chz/inflation)** by MrNasdog.

Chiliz runs an uncapped, inflationary supply, and this window it ran hotter than its own mint. Over the last 90 days CHZ added **215M** of sell-side supply: **156.1M** freshly minted by the Chiliz Chain block reward, plus **58.9M** of pre-minted reserve draining out of the two project allocation wallets. Against that, a revenue-funded buyback destroyed **28.9M CHZ**. The framework reads **+1.78% net** versus a supply monitor at **+1.19%**, a gap of **0.59 percentage points** that is the reserve drawdown — a float event the monitor cannot see. The block reward stepped down **16.5%** to **55.33 CHZ** a block on **Jun 17 2026**, so issuance is easing.

## The verdict, in one paragraph

For the 90-day window ending **Aug 3 2026**, the Pressure Framework reads **CHZ at +1.78% net**. Sell pressure is **215.0M CHZ**, buy pressure is **28.9M CHZ**, against a circulating base of **10.47B CHZ**. Our supply monitor reads **+1.19%**, so a monitor-gap note ships on the CHZ overview — and the deep walk explains it cleanly. The monitor derives supply as market cap divided by price, so it only sees **net new supply**: mint of **156.1M** minus burns of about **29M** is roughly **+1.21%**, almost exactly the monitor's figure. The extra **0.56 points** is the **58.9M** reserve that drained out of Chiliz's own wallets — total supply does not change when a project wallet empties, so no supply monitor can detect it, but the tokens are just as much on the market. Looking forward, with the reserve nearly spent and the mint lower, the next 90 days project **+1.23%**. Chiliz is best characterised as **a mildly inflationary utility chain whose float, not its mint, drove this window**.

## Sell pressure: where new CHZ comes from

Sell #1, protocol inflation, is **156.1M CHZ**. Chiliz Chain is uncapped and mints new CHZ every block on a schedule introduced by the Dragon8 upgrade in 2024, which decays year over year toward a **1.88%** floor. The current annual rate is roughly **5.5%**, and the per-block reward stepped down **16.5%** — from **66.28** to **55.33 CHZ** a block — at block **34,977,246** on **Jun 17 2026**. Because that cut landed mid-window, the last-90-day figure is a blend of the two rates and the forward figure is re-based on the lower one: the next 90 days project **143.1M CHZ**. This is real, permanent issuance — with no hard cap, the mint eases but never stops.

Sell #3, foundation and unscheduled unlocks, is **58.9M CHZ**, and it is the reason CHZ reads hotter than its mint. Thirty-five percent of every block's reward routes to two published Chiliz wallets — a community vault (**0x8DE8…2ADb**) and an ecosystem-and-operations wallet (**0xe447…2cDb**). Sell #1 already books all of that mint, so this row counts only the **net drawdown** of the wallets, to avoid double-counting. A standing reserve that sat above **100M** earlier in 2026 was released into the market: the two wallets fell from **63.1M** combined on **May 5 2026** to **4.2M** on **Aug 3 2026**. They are now near-empty and simply pass the current mint through, so the forward figure for this row is **zero** — there is no reserve left to drain.

The other two sell rows are **zero**. Sell #2, vesting unlocks, is zero because the original 2018 CHZ allocation finished vesting in 2022 and the token has been fully unlocked ever since — there is no cliff calendar. Sell #4, long-term locked or bankruptcy, is zero because Chiliz has no estate, no trustee and no court-ordered distribution.

## Buy pressure: where new CHZ goes

Buy #1, the programmatic buyback, is **28.9M CHZ** and is the only meaningful offset. Chiliz routes **10%** of monthly fan-token revenue into open-market CHZ purchases and burns them by sending them to the zero address. This window caught a football-boosted stretch: about **4.7M** burned on **May 26 2026**, then two burns totalling **24.3M** executed on **Jul 29 2026** covering the World Cup period, when fan-token trading spiked. All of it is verifiable on-chain at the burn address, whose balance rose from **20.1M** to **49.1M** across the window. As the tournament boost fades, the buyback reverts to its pre-tournament baseline of roughly **4.7M** a month, so the next 90 days project about **14M**.

The other three buy rows are **zero**. Buy #2, the protocol fee burn, is effectively dormant: Chiliz Chain's base-fee burn reads **zero** per block and removed under **1M CHZ** across the whole window, too small to register. Buy #3, foundation buy, is zero because no open-market purchase beyond the buyback-and-burn was disclosed. Buy #4, new long-term lock, is zero because no new lock-up contract or staking cap with a committed quantum was announced in the window.

## Foundation and overhang

The team-controlled overhang for CHZ is the pair of inflation-allocation wallets, and this window they went from a genuine overhang to nearly empty. The community vault (**0x8DE8…2ADb**) fell from **23.8M** to **2.7M**, and the ecosystem-and-operations wallet (**0xe447…2cDb**) fell from **39.3M** to **1.5M** — a combined **58.9M** reaching the market on top of the fresh mint. Both are read on-chain at every rebuild. There is no separate DAO treasury (Chiliz Chain governance is validator-based), no bankruptcy estate, and no genesis vesting pool, because that schedule closed in 2022. The buyback executor holds nothing — it is a pass-through to the burn address, not an accumulation wallet. If either allocation wallet's balance falls further between refreshes, that outflow enters Sell #3 at the next refresh; but with only **4.2M** left between them, the reserve story is essentially over.

## How CHZ compares to other revenue-burn Layer 1s

The natural comparison class for CHZ is app-specific Layer 1s that fund a token buyback-and-burn from their own revenue. The defining difference is that CHZ's burn is small relative to its mint. The **28.9M** destroyed this window — and it was an unusually large window, lifted by the World Cup — is under a fifth of the **156.1M** minted. On chains where the buyback consistently exceeds issuance, supply shrinks; on Chiliz, the buyback softens an uncapped mint but does not reverse it. The burn is also tied to a seasonal revenue driver, so it swells during major tournaments and shrinks between them, which makes the net reading move with the football calendar rather than with the protocol.

Against ordinary uncapped proof-of-stake Layer 1s, CHZ looks similar on the mint alone. Its roughly **5.5%** annual issuance, decaying toward **1.88%**, is squarely in the normal band for a staking chain, and the **16.5%** step-down on **Jun 17 2026** is the schedule doing exactly what it promises. What sets this window apart is not the mint but the float: most PoS chains do not have a discretionary reserve emptying **58.9M** of pre-minted supply into the market at the same time. That is a one-off, and it is why the framework and the supply monitor disagree.

Against hard-capped assets, the contrast is starkest. CHZ has **no maximum supply** — the chain's own counters show issued supply rising continuously, and the only thing removing CHZ is a revenue-driven burn that has to outrun issuance to matter. It has not, so CHZ's supply is a slowly rising line with a seasonal offset, not a fixed ceiling.

## What to watch in the next 90 days

Watch the two allocation wallets first: with **4.2M** left between them, they can no longer drive the reading, and confirming they stay near-empty is what turns Sell #3 off for good. Watch the monthly buyback-and-burn as the World Cup boost rolls off — a return toward the **4.7M**-a-month baseline is the assumption behind the **+1.23%** forward reading, and a sustained higher burn would pull it lower. Watch the block reward: the next annual step-down is not due until **Jun 2027**, so issuance holds at **55.33** a block through this window. And watch for any governance move on the burn mechanism or the EIP-1559 base-fee burn, which currently reads **zero** and would only matter if network activity rose enough to make it bite.

## Summary

The MrNasdog Pressure Framework reads Chiliz at **+1.78%** net supply growth over the last 90 days and **+1.23%** projected for the next 90, against a supply monitor at **+1.19%**. The structural mechanism is an uncapped, decaying per-block mint — **156.1M CHZ** this window at a reward that stepped down to **55.33** a block on **Jun 17 2026** — partly offset by a **28.9M** revenue-funded buyback-and-burn. The key wrinkle is a one-off: a **58.9M** reserve drained out of Chiliz's two allocation wallets, which is why the framework reads hotter than the monitor and why the forward number is lower once that reserve is gone. The lasting risk is simple — CHZ has no cap, so absent a burn that consistently outruns issuance, supply keeps rising.

---

*MrNasdog Pressure Framework analysis of CHZ, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 3 2026.*

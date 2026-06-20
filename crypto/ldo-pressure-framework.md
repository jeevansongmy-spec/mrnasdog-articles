---
title:         "LDO Inflation Analysis · June 2026 · Supply shrinking, projected to keep shrinking"
description:   "Lido DAO's LDO is fully vested with no mint or burn — but a live DAO buyback is shrinking supply. Framework reads −0.83% net; monitor −0.77%."
canonical_url: "https://mrnasdog.com/research/ldo/inflation"
tags:          ["crypto", "ldo", "lido", "staking"]
published:     true
---

*Originally published at [mrnasdog.com/research/ldo/inflation](https://mrnasdog.com/research/ldo/inflation)*

Lido DAO's **LDO** is a fully-vested, 1B fixed-cap governance token with no mint and no burn — so every sell row is zero. The only active mechanism is a DAO-approved buyback that removed **~6.5M LDO** last quarter and is projected to remove **~7M LDO** next. The Pressure Framework reads **−0.83% net** over the next 90 days against a monitor reading of **−0.77%** for the trailing window — mildly deflationary, driven entirely by the buyback.

## The verdict, in one paragraph

For the trailing 90-day window the framework books **LDO at −0.77% net**, and projects **−0.83%** for the next 90 days: no sell row carries any value, and the single buy row — the buyback — removes supply. The inflation monitor reads **−0.77%** over the trailing window, a gap of just **0.006 percentage points** versus the framework's realized figure, far inside the 0.5-point tolerance, so no warning chip is raised. The monitor's measured supply decline and the framework's buyback row describe the same event. LDO is a **fully-vested governance token that is deflationary by active buyback** — not by protocol design.

## Sell pressure: where new LDO comes from

Nothing creates new LDO. **Protocol inflation** is zero — LDO is a fixed 1B ERC-20 with no mint function, verified on-chain; the Lido protocol issues stETH and wstETH to stakers, never new LDO. **Vesting unlocks** are zero because the entire token is already unlocked: the team (40%), investor (35%) and treasury (25%) allocations all finished their linear vesting by 2024, leaving no cliffs to release. **Foundation and unscheduled unlocks** are zero in flow, though the DAO treasury holds a real overhang — the Aragon Agent carries **~108.23M LDO** on-chain with no published deployment schedule, and it is growing rather than shrinking because the buyback returns tokens to it. **Long-term locked or bankruptcy** is zero: there is no bankruptcy estate and nothing sits on a trustee release schedule.

## Buy pressure: where new LDO goes

The buy side is where LDO's story lives. **Programmatic buyback** is the one active mechanism: Lido DAO approved a buyback of roughly **22M dollars** (about 10,000 stETH) in a vote that concluded Apr 13 2026, and execution began Apr 20 2026 in 1,000-stETH tranches run by the Growth Committee. It removed **~6.5M LDO** from circulation over the trailing 90 days and is projected to remove **~7M LDO** over the next 90 at the same tranche-gated pace. Bought-back LDO returns to the DAO treasury, where it is held governance-disabled — supply is taken off the market without being destroyed. **Protocol fee burn** is zero: there is no burn function in the LDO contract; staking fees accrue to the protocol treasury, not to a token burn. **Foundation buy** is zero today — a separate automated annual buyback of roughly 10M dollars, funded from staking rewards, is planned for 2026 but not yet live, activating only above set ETH-price and revenue thresholds. **New long-term lock** is zero — there is no native LDO staking lock and no new lockup programme.

## Foundation and overhang

LDO's defining overhang is the **DAO treasury**, held by the Lido Aragon Agent, which carries **~108.23M LDO** on-chain — roughly 13% of circulating supply. There is no published schedule for deploying it, so the framework watches it on a daily chain refresh rather than projecting a release. Importantly, the buyback feeds this same treasury: repurchased LDO is parked here and cannot vote while held, so the balance trends up, not down. That makes the treasury a watched overhang in the strict sense — capacity exists, but the recent direction of travel is accumulation, not distribution. If this treasury's balance falls between refreshes, the outflow enters Sell #3 at the next refresh; until then it sits as scope, not flow.

## How LDO compares to other governance tokens

Among large-cap governance tokens, LDO sits in the fully-vested, fixed-cap camp — closer to a token like UNI than to an emission-heavy Layer 1. Where an uncapped staking chain mints new units continuously to pay validators, LDO mints nothing: the Lido protocol rewards stakers in stETH, and the governance token's supply has been frozen at its 1B cap since vesting completed. That removes the usual sell-side pressure entirely. The mechanism that separates LDO from a passive governance token is the buyback. Unlike an exchange token that burns its repurchases — permanently destroying supply — Lido returns bought-back LDO to its treasury, governance-disabled. The market effect over a 90-day window is similar (supply leaves the float), but the accounting differs: a burn is irreversible, while a treasury can in principle redistribute. For the framework's purposes the distinction is about reversibility, not about the current reading.

It is worth being explicit about why LDO reads deflationary at all, given a fixed cap. A capped-but-flat token tops out at neutral — no new coins, but none removed. LDO clears that bar because real tokens are actively leaving the float through the buyback. The reading is therefore a finding about behaviour, not structure: if the DAO paused the buyback tomorrow, LDO would revert to a flat, fully-vested token reading zero. The deflation is a policy, executed in tranches, and each tranche requires its own tokenholder approval — so the pace is a governance variable, not a protocol constant.

## What to watch in the next 90 days

Three things move the reading. First, the **buyback tranches** — each 1,000-stETH batch needs separate tokenholder approval and public reporting, so the next-90-day figure rises or falls with how many tranches clear through about Oct 2026. Second, the **automated annual buyback** — if the DAO switches on the planned ~10M-dollar program (conditional on ETH price and protocol revenue), it would add a second, rule-based buy mechanism on top of the one-off. Third, the **DAO treasury** — any on-chain deployment of the ~108.23M LDO Aragon Agent balance would register as Sell #3 at the next daily refresh and could flip the reading from deflationary to inflationary in a single event.

## Summary

LDO is a fully-vested, 1B fixed-cap governance token with no mint and no burn, so its supply pressure comes entirely from a single discretionary mechanism: a DAO-approved buyback that removed ~6.5M LDO last quarter and is projected to remove ~7M next. The Pressure Framework reads **−0.83% net** over the next 90 days against a monitor reading of **−0.77%** for the trailing window — a 0.006-point gap, no chip. The key risk is reversibility: the deflation is a tranche-gated governance policy, not protocol code, and the ~108.23M LDO treasury that receives the repurchases could one day redistribute it.

---

*MrNasdog Pressure Framework analysis of LDO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 20, 2026.*

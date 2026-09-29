---
title:         "PONS Inflation Analysis · September 2026 · Supply shrinking · projected to keep shrinking"
description:   "PONS is shrinking: no new coins, and 317.45M PONS burned since launch — 202.86M by a fee-funded buyback. Net −46.51% in 90 days, about −5.70% projected next."
canonical_url: "https://mrnasdog.com/research/pons/inflation"
tags:          ["crypto", "pons", "launchpad", "tokenburn"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/pons/inflation](https://mrnasdog.com/research/pons/inflation)*

# PONS Inflation Analysis · September 2026 · Supply shrinking · projected to keep shrinking

The MrNasdog Pressure Framework reads PONS as shrinking: **0 PONS** of new supply against **317.45M PONS** burned since the token launched on Jul 13 2026, a net change of **−46.51%** of the circulating supply over the trailing 90 days and about **−5.70%** projected for the next 90. The mechanism is simple: Pons, the busiest coin launchpad on Robinhood Chain, spends 80% of its own fees buying PONS on the open market and sending it to the burn address, and the PONS contract has no way to create new coins. The limit on the burn is the launchpad’s fee income, measured in dollars, so a higher PONS price means fewer coins burned for the same fees.

## The verdict, in one paragraph

Over the last 90 days the PONS ledger books **0** on the sell side and **317.45M PONS** on the buy side against a circulating supply of **682.61M PONS**, so supply fell by **46.51%**. For the next 90 days we project a fall of about **5.70%**, all of it from the fee-funded buyback. Our supply monitor has no 90-day reading for PONS yet, because the token is only 77 days old, so there is no gap to measure and no warning flag on the page; over the last 30 days the monitor read **−4.34%** against our on-chain **−3.81%**, and the small difference comes from its starting count lagging the chain. In one line: PONS is a fixed-supply token with a live buy-and-burn, deflationary by structural buyback.

## Sell pressure: where new PONS comes from

Protocol inflation is **0 PONS**. All 1,000M PONS were created in a single transfer when the token launched on Jul 13 2026, and nothing has been created since: we swept every creation event on Robinhood Chain and found that one alone. We also listed every function the PONS contract exposes. They are the standard token functions plus read-only launch details, with no mint, no owner and no upgrade path, so the zero cannot change unless PONS moves to a new contract.

Vesting unlocks are **0**. Pons launched its own token through its own launchpad with no team, investor or treasury allocation, and the whole supply went into the launch pool on day one. There is no locked bucket, so there is nothing left to unlock. Foundation and unscheduled unlocks are also **0**: every PONS that has not been burned already counts as circulating, so no project wallet can add new supply by selling. Long-term locked or bankruptcy supply is **0**, because no estate, trustee or lock holds PONS.

## Buy pressure: where new PONS goes

The programmatic buyback is the engine. Pons charges a fee on trades of the coins launched on it; the protocol’s share is split 80% to a PONS buyback and 20% to infrastructure and the team. Since launch the buyback has burned **202.86M PONS**, worth about **$20.4M** at the price of each day. Until Sep 2 2026 a team wallet ran it in about 1,500 hand-sent burns; since that day an automated contract buys PONS in small slices and burns it at once, more than 12,000 times so far. Most of the coins were bought in July, when PONS cost cents, which is why the token count is so large next to the dollars spent.

For the next 90 days we hold the dollars, not the coins: the same $20.4M at today’s price of about **$0.52** buys about **38.90M PONS**. That is close to the recent pace; the week of Sep 21 2026 burned about 2.59M PONS. The protocol fee burn is **0**, since gas on Robinhood Chain is paid in ETH and PONS transfers carry no fee that destroys coins.

The foundation buy is **10.74M PONS**, a one-off: the wallet that deployed PONS bought 11.74M in the first minutes of the launch, passed 1.00M to the buyback wallet and burned the rest on Jul 14 2026. It has held nothing since, so it counts 0 going forward. New long-term locks are **0**, because PONS has no staking and no lock contract. A fifth row covers **103.85M PONS** that holders burned themselves, nearly all of it in launch week, when one wallet sent 71.65M to the burn address between Jul 13 and Jul 15 2026. These burns faded to almost nothing by September, so they count 0 for the next 90 days.

## Foundation and overhang

PONS has no team treasury of any size. The PONS count that is not burned is all circulating, so every wallet below is already inside the float and can only move coins, not add them. The project-side balances are small: the old hand-run buyback wallet holds about **229K PONS**, a launch-week wallet that burned 15.89M still holds about **3.10M PONS**, another launch-week wallet holds about **127K PONS**, and the deploying wallet holds nothing. The automated buyback contract holds **0**, because it burns what it buys in the same step. The protocol’s 20% share of fees is kept in the currency the fees are paid in, not in PONS. We read these balances on-chain at every rebuild; if any of them falls between refreshes, the outflow enters the foundation row at the next refresh.

## How PONS compares to other launchpad tokens

PONS belongs to a new group: tokens of coin launchpads that turn trading fees into buybacks. The mechanism detail that matters is where the bought coins go. PONS sends every bought coin to the burn address, so each purchase leaves the circulating count for good. Some launchpad tokens instead buy back and keep the coins in a project wallet; that looks the same in a headline, but the coins stay in the count and can come back, so on our ledger such a buyback removes nothing.

Its closest rival on the same chain, the StonkFun launchpad, routes about 60% of its platform revenue into buying and burning its STONK token, against 80% of protocol fees for PONS; by Sep 11 2026 STONK had burned 14.4% of its supply against about 29% for PONS at the end of August. Both have fixed supplies, so neither has new coins to fight. That puts them in a different class from proof-of-stake chains, which pay stakers in new coins every day and need a large fee burn just to stand still.

The weak point of the group is also shared: the burn is only as large as fee income, and launchpad fees swing hard. Pons’s fees peaked in the first week of September 2026 and have fallen sharply since, so the next 90 days depend far more on how many people launch and trade coins on Robinhood Chain than on anything in the PONS contract.

## What to watch in the next 90 days

First, the end of free gas: Robinhood Chain’s 90-day gas subsidy ends on Sep 29 2026, and if trading on new coins slows once users pay gas in ETH, the PONS buyback shrinks with it. Second, the fee split: the 80% share of protocol fees for the buyback is stated as policy, not yet fixed in code, so any change to it would move the forward figure at once. Third, the newer launch design: coins launched on the new version send their own optional buybacks into five-year vaults for that coin, not into PONS, so the share of Pons’s income that reaches PONS is worth checking at each rebuild. Fourth, trust in launches: a report on Sep 27 2026 tied about $18.4M taken from 53 memecoin launches to one group, most of them launched on the new version, and a loss of trust would cut launch volume. Fifth, the monitor’s first 90-day reading for PONS, due around Oct 20 2026, which will give this page its first outside cross-check.

## Summary

PONS, the token of the Pons launchpad on Robinhood Chain, has a fixed supply of 1,000M with no way to mint more, no vesting and no team allocation, and **317.45M PONS** have been burned since the Jul 13 2026 launch, **202.86M** of them by a buyback funded with 80% of the launchpad’s fees. The MrNasdog Pressure Framework reads supply down **46.51%** over the trailing 90 days and projects about **−5.70%** for the next 90 days, as today’s higher price means the same fee dollars burn fewer coins. The key risk is income: the buyback depends on launchpad fees that have already fallen from their September peak, and on a fee split the team can still change. There is no supply cap to worry about on the upside; the only question for PONS is how fast it keeps shrinking.

*MrNasdog Pressure Framework analysis of PONS, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

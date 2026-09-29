---
title:         "JST Inflation Analysis · September 2026 · Supply shrinking · projected to keep shrinking"
description:   "JST supply is shrinking: −4.34% in 90 days as JustLend DAO burned 355.0M JST and minted none. About 166.9M more burns in October, for −2.04% next."
canonical_url: "https://mrnasdog.com/research/jst/inflation"
tags:                    ["crypto", "jst", "just", "defi"]
published:     true
---

Originally published at [JST Inflation Analysis · September 2026 · Supply shrinking · projected to keep shrinking](https://mrnasdog.com/research/jst/inflation).

# JST Inflation Analysis · September 2026 · Supply shrinking · projected to keep shrinking

JST, the governance token of JUST and JustLend DAO on TRON, is **deflationary**. Nothing created new JST in the last 90 days, while JustLend DAO's buyback-and-burn round on Jul 17 2026 destroyed **355.02M JST** — **4.34%** of the **8.19B** circulating supply. The next quarterly burn, due around Oct 15 2026 with about **$21.55M** planned, should remove roughly **166.9M JST**, or **2.04%** more.

## The verdict, in one paragraph

Over the last 90 days the JST supply moved by **−4.34%**, and our projection for the next 90 days is **−2.04%**. The inflation monitor, which measures the change in circulating supply against the supply of 90 days ago, reads **−4.15%**. The gap is **0.18 percentage points**, inside our 0.5-point tolerance, so no warning chip is shown: the monitor divides the same 355.02M JST by the larger supply it saw before the burn, which accounts for the difference. JST is a **zero-emission token that shrinks by quarterly buyback-and-burn**.

## Sell pressure: where new JST comes from

Protocol inflation is **0**. JST pays no block reward and no staking reward. All **9.9B JST** were minted once, in April 2020, and the JST event log shows no mint since. The JST contract still has a working mint function that only its owner can call — so the supply is not fixed by code — but the owner has never used it after launch, and total supply only went down this window.

Vesting unlocks are **0**. The JST release plan ran from Apr 30 2020 to Mar 30 2023 and is complete. Every JST that has not been destroyed already counts as circulating, so there is no locked bucket left to open.

Foundation and unscheduled unlocks are **0**. Team-linked JST wallets exist, but all of their coins already sit inside the circulating count, so moving or selling them would add nothing new to the float. Long-term locked or bankruptcy supply is also **0**: there is no estate, court schedule or long lock that releases JST.

## Buy pressure: where new JST goes

The programmatic buyback removed **248.36M JST** in the window. Under the JST Buyback & Burn proposal that JustLend DAO holders approved on Oct 21 2025, all of JustLend DAO's net income, plus USDD revenue above $10M, is used to buy JST on the market and burn it. A $59.09M historical reserve was split too: 30% went into the first burn, and the other 70% is being spent in four quarterly slices of about $10.34M. On Jul 17 2026 the fourth round spent **$20.6M** — $10.28M of Q2 2026 net income plus one reserve slice — and sent 248,357,799 JST to the TRON burn address. That address now holds **1.60B JST**.

The protocol fee burn removed **106.66M JST**. Borrowers of the old USDJ stablecoin paid their stability fees in JST, and those coins piled up in a fee contract for years. On Jul 17 2026 the whole pile was destroyed through the token's own burn function — the only time the JST total supply itself has fallen, from 9.9B to **9.79B**. The fee contract is now empty and has received nothing since November 2025, so this row is **0** for the next 90 days.

Foundation buying is **0**: no team wallet buys JST to hold it, and every purchase ends in the burn. New long-term locks are **0**: JST wrapped for voting or supplied to the lending market can be withdrawn at any time and still counts as circulating.

For the next 90 days the buyback is the only buy row. The Q2 2026 report put the Q3 buyback budget at about **$21.55M**, which is also the last reserve slice plus about one quarter of net income. At today's JST price near $0.129, that buys about **166.9M JST**. It is fewer coins than in July because JST now costs more, not because less money is being spent.

## Foundation and overhang

The wallet that carries out every JustLend DAO buyback round holds about **500M JST**, up from 300M at the start of the window as 200M-coin voting parcels moved in and out; the July round passed through it straight to the burn address in minutes. About **700M JST** sits wrapped for governance voting and about **90M JST** is supplied to the JST lending market. The contract owner that can mint holds no JST, and the old USDJ fee contract is empty. We re-read all of these balances from the TRON chain at every refresh. Large unlabelled wallets and exchange wallets are left out, because their coins belong to depositors or to no identified group. If the buyback wallet's balance falls between refreshes, or the owner ever mints, the outflow enters Sell #3 at the next refresh.

## How JST compares to other DeFi revenue-buyback tokens

Most DeFi governance tokens that buy back with revenue fall into one of two groups. Some buy and hold: the coins go to a treasury that still counts as circulating, so the float does not shrink until the treasury burns them or locks them away. Others buy back with one hand and pay new tokens to stakers or liquidity providers with the other, so the buyback is partly cancelled by emissions. JST sits in neither group. It has no emission at all, and every JST bought is burned, so each JustLend DAO buyback round takes coins off the market one for one.

The closest match in shape is a quarterly exchange-token burn such as BNB's Auto-Burn: a fixed date each quarter, no new issuance, and a burn that shrinks supply step by step. The difference is the funding. The BNB burn is set by price and block count; the JST burn is set in dollars by JustLend DAO's lending income, so it buys fewer coins when JST rises and more when it falls. Against uncapped Layer 1 coins, whose validator rewards add supply every block, JST's sell side is empty — the only way supply could grow is if the owner used its mint power.

The size is unusual too: four rounds since October 2025 have destroyed **1.71B JST**, about 17.3% of the original 9.9B. Each round is visible on the TRON chain as a transfer to the burn address, so the whole record can be checked.

## What to watch in the next 90 days

The Q3 2026 buyback and burn, expected around Oct 15 2026: we will check the burn amount against the $21.55M budget and today's estimate of about 166.9M JST. It also spends the last slice of the historical reserve, so from January 2027 the rounds depend only on quarterly income.

The Q3 2026 JustLend DAO quarterly report, likely in late October 2026, which should give the next quarter's buyback budget. JustLend DAO income is the one input that sets how fast JST shrinks.

The offboarding of the USD1 lending market announced on Sep 16 2026, and any other market changes, which could move JustLend DAO income. Also any JST mint event from the contract owner, which would land in the sell rows at once.

## Summary

JST is a deflationary TRON governance token: no JST was created in the last 90 days, and JustLend DAO's buyback-and-burn destroyed **355.02M JST**, taking supply down **4.34%**, within 0.18 points of the monitor's −4.15%. The next round, about **$21.55M** around Oct 15 2026, should cut roughly **2.04%** more. The key risk is that the burn is only as big as JustLend DAO's income, and that the contract owner can still mint, even though it has not since 2020. With 1.71B JST already burned, the ceiling is the original 9.9B supply, and the float has been getting smaller every quarter.

*MrNasdog Pressure Framework analysis of JST, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

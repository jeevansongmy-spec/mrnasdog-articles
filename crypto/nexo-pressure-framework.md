---
title:         "NEXO Inflation Analysis · September 2026 · Mixed flows, supply roughly steady"
description:   "NEXO supply is steady: net 0.00% over 90 days. No mint, no burn, vesting ended in 2022, and 768M NEXO in Nexo's own wallets barely moved. Full analysis."
canonical_url: "https://mrnasdog.com/research/nexo/inflation"
tags:          ["crypto", "nexo", "cefi", "exchange-token"]
published:     true
---

> Originally published at **[mrnasdog.com/research/nexo/inflation](https://mrnasdog.com/research/nexo/inflation)** by MrNasdog.

# NEXO Inflation Analysis · September 2026 · Mixed flows, supply roughly steady

The Pressure Framework reads NEXO at **0.00%** over the trailing 90 days and **0.00%** over the next 90: sell pressure is **0**, buy pressure is **0**, and the inflation monitor agrees within **0.06** percentage points. The reason is structural — the NEXO token contract on Ethereum has no function that can mint or burn, its built-in vesting schedule ran out in **2022**, and the roughly **768M NEXO** Nexo holds in its own wallets barely moved. The ceiling is a hard **1,000M NEXO**, and every one of them already counts as circulating.

## The verdict, in one paragraph

Against a circulating base of **1,000M NEXO**, the framework books **0** of sell pressure and **0** of buy pressure over the trailing 90 days — a net of **0.00%** — and projects **0.00%** for the next 90 days, because no schedule, burn or buyback is running. The inflation monitor reads **-0.06%** for the same window, a gap of **0.06 percentage points**, well inside the framework's 0.5pp tolerance, so no monitor-gap warning ships on the overview page. The small negative reading is the monitor's market-derived supply estimate wobbling around a total that the chain shows fixed at exactly 1,000,000,000 at both ends of the window. The label for NEXO is **a fixed-supply company token standing still**: nothing is created, nothing is destroyed, and the large company holdings are parked rather than flowing.

## Sell pressure: where new NEXO comes from

Nowhere. Sell #1, protocol inflation, is **0**, and it is the one row on this page marked permanent. NEXO is an Ethereum ERC-20 token, not a chain: there is no block reward, no validator subsidy and no staking emission. All **1,000M NEXO** were created once, when the contract was deployed in **April 2018**. The framework did not take that on trust. Every function in the deployed NEXO contract was listed and identified — the standard token functions, ownership transfer, a rescue function for other tokens, and the 2018 vesting withdrawals — and none of them can create a coin or change the stored total. The total itself lives in ordinary contract storage and read exactly **1,000,000,000** at both ends of the window. The contract is not upgradeable, so no new mint function can be added later.

Sell #2, vesting unlocks, is **0**. The NEXO contract carries its own release schedule for investors, team, advisers, community and the overdraft pool. The longest of those streams — the team's, sixteen quarterly steps from the April 2018 launch — finished in **2022**. Nothing is left on any calendar, so no NEXO unlocks in this window or the next.

Sell #3, Foundation and unscheduled unlocks, is **0**: none of Nexo's identified wallets released coins to the market in the window, and the next section walks each one. Sell #4, long-term locked or bankruptcy, is **0** as well — Nexo is an operating company with no bankruptcy estate, no trustee and no court-ordered distribution tied to NEXO.

## Buy pressure: where new NEXO goes

Also nowhere, this window. Buy #1, programmatic buyback, is **0**. Nexo has run NEXO buyback rounds before — a first round in **December 2020**, a larger "Buyback 2.0" round from **November 2021**, and a top-up in **August 2022** — but those coins were never burned. Nexo's own terms send them to a public Investor Protection Reserve, where they vest for a year and can then fund NEXO interest payouts. That reserve holds **114.8M NEXO**, read the same at both ends of the window, and its last incoming transfer was in **March 2023**. No new round was announced. A buyback-and-hold into this reserve would not register here in any case, because the reserve already counts as circulating supply — coins moving from the market into it are a move within the float, not a removal.

Buy #2, protocol fee burn, is **0**. NEXO has no burn function and no fee burn. The framework read both places a burn could appear: the total count of NEXO stayed at **1,000M**, and the Ethereum dead address held the same **10.7 NEXO** at both ends of the window, as it has for years. Neither moved, so nothing was destroyed.

Buy #3, Foundation buy, is **0**. Nexo has no foundation, and its corporate treasury and reserve wallets took in no NEXO over the window. Buy #4, new long-term lock, is **0**. Nexo's loyalty tiers and in-app voting use NEXO that stays in the user's own account and can be withdrawn at any time, so neither takes supply off the market.

## Foundation and overhang

The overhang on NEXO is very large, and so far completely still. The framework identifies about **768M NEXO** — more than three-quarters of all NEXO — in wallets Nexo controls. The biggest pieces are four release buckets that still sit inside the NEXO token contract, holding **353.9M NEXO** between them; these finished vesting years ago, and the contract owner can withdraw them at will. Next is Nexo's corporate treasury at **213.2M NEXO**, which sent out just **2,000 NEXO** in the window. Then the Investor Protection Reserve at **114.8M NEXO**, and the contract owner's own wallet at **86.1M NEXO**. Except for that small treasury transfer, every one of these balances was identical at both ends of the window and a year earlier.

What makes this overhang unusual is how it is counted. Circulating supply for NEXO equals total supply, so all of these wallets are already inside the float the framework divides by. If Nexo withdrew or sold from them, that would be a move within the float rather than new supply — yet it is still the thing to watch, because it is the only NEXO with a spender and no schedule. Each balance is read from the chain at every rebuild, and if any of them falls between refreshes, that outflow enters Sell #3 at the next refresh.

## How NEXO compares to other exchange and platform tokens

NEXO sits in the class of company-issued platform tokens: a fixed pre-mint, rewards paid out of company holdings, and buybacks run at the company's discretion. What separates tokens in this class is what happens to the bought-back coins. Exchange tokens that buy back and burn — sending coins to a dead address or cutting the recorded total — can post genuinely negative readings, because every round shrinks supply. NEXO's buyback does the opposite: it parks coins in a reserve that stays inside the float, so on the framework's measure a NEXO buyback is buying demand, not removing supply.

Against capped proof-of-work chains, NEXO is stricter on issuance. A halving-model chain like Bitcoin still mints on every block, just at a falling rate, so its reading stays slightly positive for decades. NEXO mints nothing at all, and has no code path to do so. Against uncapped staking chains, where yearly emission of several percent is normal, NEXO's zero is a hard zero rather than a policy.

The risk in NEXO is concentration rather than issuance. A token whose supply is fixed but whose issuer holds three-quarters of it is only as steady as that issuer's decisions. Nexo pays interest and rewards in NEXO; if those payouts ever run down the treasury or the reserve faster than users buy, the float reshuffles even with a fixed total.

## What to watch in the next 90 days

First, the four release buckets inside the NEXO contract at **353.9M NEXO** — a withdrawal by the contract owner is the single largest move this token can make, and it would show at the next rebuild. Second, the corporate treasury at **213.2M NEXO**, the wallet most likely to fund interest and reward payouts. Third, the Investor Protection Reserve at **114.8M NEXO**: any new buyback round would land there, and any outflow would mean the reserve is being spent. Fourth, any new tokenomics news tied to Nexo's return to the United States and its Coinbase listing-roadmap entry from **May 7 2026** — a burn announcement would be the one event able to push the reading negative. Fifth, the dead address at **10.7 NEXO**, the only place a burn could show.

## Summary

The MrNasdog Pressure Framework reads NEXO at **0.00%** over the trailing 90 days and **0.00%** projected forward: mixed flows, supply roughly steady. The structural mechanism is a fixed pre-mint — the NEXO contract has no mint or burn function, its vesting ended in **2022**, and its buyback parks coins in a reserve instead of burning them. The key risk is concentration: about **768M NEXO** sits in Nexo's own wallets with no release calendar, and while none of it moved this window, it is the only source of change this token has. The ceiling is hard: **1,000M NEXO**, fixed in code since **April 2018**.

*MrNasdog Pressure Framework analysis of NEXO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 18 2026.*

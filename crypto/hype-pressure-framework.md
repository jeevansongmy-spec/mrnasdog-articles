---
title:         "HYPE Inflation Analysis · June 2026 · Net Deflationary"
description:   "Net deflationary: the Assistance Fund buys ~3.9M HYPE / 90D from platform fees, more than staking rewards plus the team claim. Framework reads −0.171% on a 1B fixed cap."
canonical_url: "https://mrnasdog.com/research/hype/inflation"
tags:          ["crypto", "hype", "hyperliquid", "defi"]
published:     true
---

*Originally published at [mrnasdog.com/research/hype/inflation](https://mrnasdog.com/research/hype/inflation)*

# HYPE Inflation Analysis · June 2026 · Net Deflationary

Hyperliquid issues roughly **2.4M HYPE** in staking rewards and the team claims about **1.1M** over 90 days, while the Assistance Fund buys back about **3.9M HYPE** from platform fees. Framework reading: **−0.171% net** on a 1B fixed cap. The buyback just edges out new supply.

## The verdict, in one paragraph

For the 90-day window ending June 24 2026, the MrNasdog Pressure Framework reads **HYPE at −0.171% net inflation** — slightly deflationary, driven by the Assistance Fund buying back HYPE faster than staking rewards plus the team claim add it. Our monitor reads **−6.867%**, a **6.69-percentage-point** gap below the framework reading, so the page carries a monitor-gap flag. The gap is mechanism, not a market sell: on-chain the buyback wallet (system address 0xfefe…fefe) only grew over the window, and Hyperliquid's own total supply held near 999M with no burn transaction, while the upstream aggregator keeps excluding the fund's growing buyback inventory from circulating supply following the December 24 2025 validator burn-recognition vote. Hyperliquid is best characterised as a **revenue-funded buyback that runs slightly ahead of issuance**.

## Sell pressure: where new HYPE comes from

HYPE has a 1B fixed maximum supply, and Hyperliquid's own on-chain data shows total supply at roughly 999M with a future-emissions reserve of about 413.8M HYPE. Sell #1 — protocol inflation — is the staking-reward stream paid out of that future-emissions reserve. At about **2.37%** a year near 400M staked, and with roughly **436.3M HYPE** currently staked, that is about **26,837 HYPE per day** moving into the circulating float — roughly **2.4M HYPE per 90 days**. It is reserve issuance, not new mint above the cap, but it does expand circulating supply, so the framework counts it.

Sell #2 — vesting unlocks — is the Core Contributors claim, and here the load-bearing convention matters. The authorized ceiling is about **9.92M HYPE per month**, but Hyperliquid runs a discretionary structure: the team announces a specific claim on the 6th of each month and it has stayed far below the maximum — roughly 140K in February, 173K in March, about 330K announced in April. The framework counts actual on-chain claim behaviour, not the ceiling, so Sell #2 sits at about **1.1M HYPE per 90 days**. This is the single most-misreported HYPE number: headlines treat the full 9.92M monthly unlock as supply hitting the market, but the actual claimed amount is a fraction of it.

Sell #3 — Foundation discretion and unscheduled — is zero, with the four team-controlled overhangs fully enumerated: the future-emissions reserve ~413.8M (only the staking stream in Sell #1 flows out), the Core Contributors bucket ~238M (only the ~1.1M/90d in Sell #2 flows out), the Hyper Foundation budget ~60M (slow grant deployment, no firings observed), and the Assistance Fund itself ~45.4M (only accumulates, never sells). Sell #4 (long-term locked or bankruptcy) is zero — there is no bankruptcy estate, and neither reserve dumps a cliff inside this window.

## Buy pressure: where new HYPE goes

The dominant buy flow is the **Assistance Fund** (Buy #1). The fund routes about **97% of platform fees** into daily open-market HYPE buys, held at one on-chain system address. The observed rate is about **43,321 HYPE per day** — roughly **3.9M HYPE per 90 days**, comfortably above the combined staking issuance and team claim. The wallet only accumulates: its on-chain balance was **45.4M HYPE on June 24 2026**, up from over 40M in early February, so every HYPE bought is effectively removed from market float.

Buy #2 — protocol fee burn — is zero. Hyperliquid has no EIP-1559-style fee burn; fees are spent on the buyback and held, not destroyed at the protocol level. The December 2025 "burn" was a governance recognition of the buyback wallet, not a separate burn engine. Buy #3 (Foundation buy) is zero — all protocol-led buying flows through the Assistance Fund. Buy #4 (new long-term lock) is zero — staking unbond is about 7 days, which is operational rather than a long-term lock, and no new lockup programme was announced in window.

## Foundation and overhang

The four team-controlled overhangs are tracked but not in the active ledger. The largest is the **future-emissions reserve ~413.8M HYPE** — it funds staking rewards gradually (the Sell #1 stream) and would only become a larger inflation risk if the emission curve changed. The **Core Contributors bucket ~238M** is where the team claims from; only the actual ~1.1M/90d claim flows out, the remainder is structural overhang. The **Hyper Foundation budget ~60M** is a slow grant deployer with no observed firings in window, and the **Assistance Fund ~45.4M** is the cumulative buyback inventory. If any of these wallets' balances fall between refreshes, the outflow enters Sell #3 at the next refresh.

## How HYPE compares to other revenue-funded tokens

Among revenue-funded tokens, HYPE's design is unusually aggressive in routing platform fees back into the token. Roughly 97% of fees flow to the Assistance Fund for HYPE buybacks, a far higher share than most exchange or DeFi tokens dedicate. The fund does not burn — it accumulates — so the buyback inventory grows indefinitely as long as Hyperliquid usage continues, and the December 2025 governance vote then formally recognised that inventory as out of supply.

The closest structural analogue is BNB's quarterly burn: both are revenue-linked, but BNB burns at quarter end (lumpy and permanent on-chain), while HYPE buys continuously and holds. The key difference from a pure no-burn L1 is that HYPE has a real, large, daily structural bid funded by fees, which is why a token that issues ~2.4M in staking rewards every 90 days still nets slightly deflationary — the buyback is bigger than the issuance. The risk is symmetric: the buyback scales with trading volume, so a sustained fee slowdown would shrink the bid and could flip the net positive.

## What to watch in the next 90 days

Three things move the framework reading. First, **Hyperliquid platform fee revenue** — the buyback rate tracks directly with trading volume, and a sustained drop would compress the buyback below issuance. Second, the **monthly Core Contributors claim on Jul 6 2026** — the announced amount has stayed far below the ~9.92M ceiling, but a larger-than-usual claim would lift Sell #2. Third, watch the **staking participation rate** — staking rewards are paid from the future-emissions reserve, so a rising staked balance changes the issuance flowing into Sell #1. Any Assistance Fund deployment (the fund's stated purpose includes acting as a backstop) would also change the buy reading.

## Summary

HYPE is a 1B fixed-cap token whose only new supply is staking rewards from a pre-allocated emissions reserve (~2.4M per 90 days) plus a discretionary, far-below-ceiling team claim (~1.1M), against a revenue-funded Assistance Fund buyback of about 3.9M per 90 days. The framework reads −0.171% net for the trailing 90 days — slightly deflationary because the buyback edges out issuance. Our monitor reads −6.867%, with the 6.69-percentage-point gap explained by the aggregator excluding the fund's growing buyback inventory after the December 2025 burn-recognition vote — mechanism, not a market sell. HYPE in mid-2026 is a clean example of a fee-funded buyback structure that runs just ahead of supply growth.

---

*MrNasdog Pressure Framework analysis of Hyperliquid (HYPE), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 24, 2026.*

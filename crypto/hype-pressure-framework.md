---
title:         "HYPE Inflation Analysis · July 2026 · Supply Edges Up"
description:   "Supply edges up +0.58%: the Assistance Fund buys ~2.50M HYPE / 90D from fees, a shade under staking rewards plus the team claim. Framework reads +0.58% on a 1B cap."
canonical_url: "https://mrnasdog.com/research/hype/inflation"
tags:          ["crypto", "hype", "hyperliquid", "defi"]
published:     true
---

*Originally published at [mrnasdog.com/research/hype/inflation](https://mrnasdog.com/research/hype/inflation)*

Hyperliquid issues about **2.45M HYPE** in staking rewards and Core Contributors actually claim roughly **1.35M** over 90 days, while the Assistance Fund buys back about **2.50M HYPE** from platform fees. Framework reading: **+0.58% net** on a 1B fixed cap — the buyback nearly, but not quite, offsets new supply. Our monitor reads **−6.7%**, a gap the on-chain data explains as aggregator reclassification of the buyback wallet, not a market flow.

## The verdict, in one paragraph

For the 90-day window ending July 14 2026, the Pressure Framework reads **HYPE at +0.58% net inflation** — slightly inflationary, because staking issuance plus the discretionary team claim edge just past the Assistance Fund buyback. Our monitor reads **−6.66%**, a **7.25-percentage-point** gap below the framework reading, so the page carries a monitor-gap flag. The gap is mechanism, not a market sell: on-chain the buyback wallet (Assistance Fund system address 0xfefe…fefe) grew from about 43.3M to 45.8M HYPE over the window, and Hyperliquid's own total supply held near 999M with no burn transaction, while the upstream aggregator keeps excluding the fund's growing buyback inventory from circulating supply following the December 24 2025 validator burn-recognition vote. Hyperliquid is best characterised as a **revenue-funded buyback that runs neck-and-neck with issuance**.

## Sell pressure: where new HYPE comes from

HYPE has a 1B fixed maximum supply, and Hyperliquid's own on-chain data shows total supply at roughly 999M with a large future-emissions reserve. Sell #1 — protocol inflation — is the staking-reward stream paid out of that future-emissions reserve. The reward rate falls as more HYPE is staked (it scales with the inverse square root of the staked total), landing near **2.3% a year** with about **439.2M HYPE** currently staked. That is roughly **2.45M HYPE per 90 days** moving from the reserve into holder balances. It is reserve issuance, not new mint above the cap, but it does expand circulating supply, so the framework counts it.

Sell #2 — vesting unlocks — is the Core Contributors claim, and here the load-bearing convention matters. The authorized schedule vests about **9.92M HYPE per month** on the 6th, and headlines report the full 9.92M "released" on May 6 and June 6. But the actual committed release is far smaller: unlock trackers put it near **0.20% of float** per tranche — roughly **0.45M HYPE**, a fraction of the ~$682M the whitepaper schedule implies — because the tokens vest to Core Contributor wallets that overwhelmingly stake rather than sell (total staked, about 439M, exceeds the entire 222M circulating float). The framework counts actual market-entering claims, not the ceiling, so counting the three tranches inside this window — **May 6, June 6 and July 6 2026** — Sell #2 sits at about **1.35M HYPE per 90 days**. This is the single most-misreported HYPE number: the 9.92M monthly unlock is a paper ceiling, and the circulating denominator actually fell over the window, confirming that most of it never reaches the market.

Sell #3 — Foundation discretion and unscheduled — is zero, with the four team-controlled overhangs fully enumerated: the future-emissions reserve ~414M (only the staking stream in Sell #1 flows out), the Core Contributors bucket ~238M (only the ~1.35M/90d in Sell #2 flows out), the Hyper Foundation budget ~60M (slow grant deployment, no firings observed), and the Assistance Fund itself ~45.8M (only accumulates, never sells). Sell #4 (long-term locked or bankruptcy) is zero — there is no bankruptcy estate, and neither reserve dumps a cliff inside this window.

## Buy pressure: where new HYPE goes

The dominant buy flow is the **Assistance Fund** (Buy #1). The fund routes about **99% of core platform fees** into daily open-market HYPE buys, held at one on-chain system address. Read directly on-chain, the wallet's balance grew from about **43.3M to 45.8M HYPE** over this window — roughly **2.50M HYPE bought and held per 90 days**, a shade below the combined 3.80M of staking issuance and the team claim. A revenue cross-check agrees: window revenue of about **$145M** at an average price near **$56** implies about 2.6M HYPE. The wallet only accumulates and is recognized as burned: every HYPE bought is effectively removed from market float.

Buy #2 — protocol fee burn — is zero. Hyperliquid has no EIP-1559-style fee burn; fees are spent on the buyback and held, not destroyed at the protocol level. The December 2025 "burn" was a governance recognition of the buyback wallet, not a separate burn engine. Buy #3 (Foundation buy) is zero — all protocol-led buying flows through the Assistance Fund. Buy #4 (new long-term lock) is zero — staking unbond is about 7 days, which is operational rather than a long-term lock, and no new lockup programme was announced in window.

## Foundation and overhang

The four team-controlled overhangs are tracked but not in the active ledger. The largest is the **future-emissions reserve ~414M HYPE** — it funds staking rewards gradually (the Sell #1 stream) and would only become a larger inflation risk if the emission curve changed. The **Core Contributors bucket ~238M** is where the team vests from; only the actual ~1.35M/90d claim flows out, the remainder is structural overhang. The **Hyper Foundation budget ~60M** is a slow grant deployer with no observed firings in window, and the **Assistance Fund ~45.8M** is the cumulative buyback inventory. If any of these wallets' balances fall between refreshes, the outflow enters Sell #3 at the next refresh.

## How HYPE compares to other revenue-funded tokens

Among revenue-funded tokens, HYPE's design is unusually aggressive in routing platform fees back into the token. Roughly 99% of core fees flow to the Assistance Fund for HYPE buybacks, a far higher share than most exchange or DeFi tokens dedicate. The fund does not burn — it accumulates — so the buyback inventory grows indefinitely as long as Hyperliquid usage continues, and the December 2025 governance vote then formally recognised that inventory as out of supply.

The closest structural analogue is BNB's quarterly burn: both are revenue-linked, but BNB burns at quarter end (lumpy and permanent on-chain), while HYPE buys continuously and holds. The key difference from a pure no-burn L1 is that HYPE has a real, large, daily structural bid funded by fees — which is why a token that issues ~2.45M in staking rewards plus a ~1.35M team claim every 90 days still nets only **+0.58%**: the buyback almost matches the new supply. The risk is symmetric: the buyback scales with trading volume, so a sustained fee slowdown would shrink the bid and widen the net positive, while a volume surge would tip it back toward flat or deflationary.

## What to watch in the next 90 days

Three things move the framework reading. First, **Hyperliquid platform fee revenue** — the buyback rate tracks directly with trading volume, and the recent softening in fees is exactly what let issuance edge past the buyback. Second, the **monthly Core Contributors vest on Aug 6 2026** — the actual claimed amount has stayed far below the ~9.92M ceiling, but a larger-than-usual claim would lift Sell #2. Third, watch the **staking participation rate** — staking rewards are paid from the future-emissions reserve, so a rising staked balance changes the issuance flowing into Sell #1. Any Assistance Fund deployment (the fund's stated purpose includes acting as a backstop) would also change the buy reading.

## Summary

HYPE is a 1B fixed-cap token whose only new supply is staking rewards from a pre-allocated emissions reserve (~2.45M per 90 days) plus a discretionary, far-below-ceiling team claim (~1.35M), against a revenue-funded Assistance Fund buyback of about 2.50M per 90 days. The framework reads +0.58% net for the trailing 90 days — slightly inflationary, because the buyback nearly but not fully offsets issuance. Our monitor reads −6.66%, with the 7.25-percentage-point gap explained by the aggregator excluding the fund's growing buyback inventory after the December 2025 burn-recognition vote — mechanism, not a market sell. HYPE in mid-2026 is a clean example of a fee-funded buyback structure that runs neck-and-neck with supply growth.

*MrNasdog Pressure Framework analysis of Hyperliquid (HYPE), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 14 2026.*

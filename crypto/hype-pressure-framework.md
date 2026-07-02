---
title:         "HYPE Inflation Analysis · July 2026 · Net Roughly Flat"
description:   "Net roughly flat: the Assistance Fund buys ~3.78M HYPE / 90D from platform fees, just cancelling staking rewards plus the team claim. Framework reads −0.06% on a 1B fixed cap."
canonical_url: "https://mrnasdog.com/research/hype/inflation"
tags:          ["crypto", "hype", "hyperliquid", "defi"]
published:     true
---

*Originally published at [mrnasdog.com/research/hype/inflation](https://mrnasdog.com/research/hype/inflation)*

# HYPE Inflation Analysis · July 2026 · Net Roughly Flat

Hyperliquid issues about **2.45M HYPE** in staking rewards and the team claims roughly **1.2M** over 90 days, while the Assistance Fund buys back about **3.78M HYPE** from platform fees. Framework reading: **−0.06% net** on a 1B fixed cap — the buyback just cancels out new supply. Our monitor reads **−6.7%**, a gap the on-chain data explains as aggregator reclassification, not a market sell.

## The verdict, in one paragraph

For the 90-day window ending July 3 2026, the Pressure Framework reads **HYPE at −0.06% net inflation** — essentially flat, a shade deflationary, because the Assistance Fund buyback edges just past staking rewards plus the discretionary team claim. Our monitor reads **−6.69%**, a **6.63-percentage-point** gap below the framework reading, so the page carries a monitor-gap flag. The gap is mechanism, not a market sell: on-chain the buyback wallet (Assistance Fund system address 0xfefe…fefe) only grew over the window, and Hyperliquid's own total supply held near 999M with no burn transaction, while the upstream aggregator keeps excluding the fund's growing buyback inventory from circulating supply following the December 24 2025 validator burn-recognition vote. Hyperliquid is best characterised as a **revenue-funded buyback that runs neck-and-neck with issuance**.

## Sell pressure: where new HYPE comes from

HYPE has a 1B fixed maximum supply, and Hyperliquid's own on-chain data shows total supply at roughly 999M with a large future-emissions reserve. Sell #1 — protocol inflation — is the staking-reward stream paid out of that future-emissions reserve. The reward rate falls as more HYPE is staked (it scales with the inverse square root of the staked total), landing near **2.3% a year** with about **438.3M HYPE** currently staked. That is roughly **2.45M HYPE per 90 days** moving from the reserve into holder balances. It is reserve issuance, not new mint above the cap, but it does expand circulating supply, so the framework counts it.

Sell #2 — vesting unlocks — is the Core Contributors claim, and here the load-bearing convention matters. The authorized ceiling is about **9.92M HYPE per month**, but Hyperliquid runs a discretionary structure: the team announces a specific claim on the 6th of each month and it has stayed far below the maximum — roughly 140K in February, 173K in March, about 330K announced in April, and a June 6 claim near $38M. The framework counts actual on-chain claim behaviour, not the ceiling, so counting the three claims inside this window — **May 6, June 6 and July 6 2026** — Sell #2 sits at about **1.2M HYPE per 90 days**. This is the single most-misreported HYPE number: headlines treat the full 9.92M monthly unlock as supply hitting the market, but the actual claimed amount is a small fraction of it.

Sell #3 — Foundation discretion and unscheduled — is zero, with the four team-controlled overhangs fully enumerated: the future-emissions reserve ~414M (only the staking stream in Sell #1 flows out), the Core Contributors bucket ~238M (only the ~1.2M/90d in Sell #2 flows out), the Hyper Foundation budget ~60M (slow grant deployment, no firings observed), and the Assistance Fund itself ~45.6M (only accumulates, never sells). Sell #4 (long-term locked or bankruptcy) is zero — there is no bankruptcy estate, and neither reserve dumps a cliff inside this window.

## Buy pressure: where new HYPE goes

The dominant buy flow is the **Assistance Fund** (Buy #1). The fund routes about **99% of platform fees** into daily open-market HYPE buys, held at one on-chain system address. Platform fees over this window were about **$199.6M**, so roughly **$197.6M** of buying at an average price near $52 — about **3.78M HYPE per 90 days**, a shade above the combined staking issuance and team claim. The wallet only accumulates: its on-chain balance was **45.6M HYPE on July 3 2026**, so every HYPE bought is effectively removed from market float.

Buy #2 — protocol fee burn — is zero. Hyperliquid has no EIP-1559-style fee burn; fees are spent on the buyback and held, not destroyed at the protocol level. The December 2025 "burn" was a governance recognition of the buyback wallet, not a separate burn engine. Buy #3 (Foundation buy) is zero — all protocol-led buying flows through the Assistance Fund. Buy #4 (new long-term lock) is zero — staking unbond is about 7 days, which is operational rather than a long-term lock, and no new lockup programme was announced in window.

## Foundation and overhang

The four team-controlled overhangs are tracked but not in the active ledger. The largest is the **future-emissions reserve ~414M HYPE** — it funds staking rewards gradually (the Sell #1 stream) and would only become a larger inflation risk if the emission curve changed. The **Core Contributors bucket ~238M** is where the team claims from; only the actual ~1.2M/90d claim flows out, the remainder is structural overhang. The **Hyper Foundation budget ~60M** is a slow grant deployer with no observed firings in window, and the **Assistance Fund ~45.6M** is the cumulative buyback inventory. If any of these wallets' balances fall between refreshes, the outflow enters Sell #3 at the next refresh.

## How HYPE compares to other revenue-funded tokens

Among revenue-funded tokens, HYPE's design is unusually aggressive in routing platform fees back into the token. Roughly 99% of fees flow to the Assistance Fund for HYPE buybacks, a far higher share than most exchange or DeFi tokens dedicate. The fund does not burn — it accumulates — so the buyback inventory grows indefinitely as long as Hyperliquid usage continues, and the December 2025 governance vote then formally recognised that inventory as out of supply.

The closest structural analogue is BNB's quarterly burn: both are revenue-linked, but BNB burns at quarter end (lumpy and permanent on-chain), while HYPE buys continuously and holds. The key difference from a pure no-burn L1 is that HYPE has a real, large, daily structural bid funded by fees, which is why a token that issues ~2.45M in staking rewards plus a ~1.2M team claim every 90 days still nets roughly flat — the buyback just matches the new supply. The risk is symmetric: the buyback scales with trading volume, so a sustained fee slowdown would shrink the bid and could tip the net clearly positive.

## What to watch in the next 90 days

Three things move the framework reading. First, **Hyperliquid platform fee revenue** — the buyback rate tracks directly with trading volume, and a sustained drop would compress the buyback below issuance. Second, the **monthly Core Contributors claim on Jul 6 2026** — the announced amount has stayed far below the ~9.92M ceiling, but a larger-than-usual claim would lift Sell #2. Third, watch the **staking participation rate** — staking rewards are paid from the future-emissions reserve, so a rising staked balance changes the issuance flowing into Sell #1. Any Assistance Fund deployment (the fund's stated purpose includes acting as a backstop) would also change the buy reading.

## Summary

HYPE is a 1B fixed-cap token whose only new supply is staking rewards from a pre-allocated emissions reserve (~2.45M per 90 days) plus a discretionary, far-below-ceiling team claim (~1.2M), against a revenue-funded Assistance Fund buyback of about 3.78M per 90 days. The framework reads −0.06% net for the trailing 90 days — essentially flat, a shade deflationary, because the buyback just cancels out issuance. Our monitor reads −6.69%, with the 6.63-percentage-point gap explained by the aggregator excluding the fund's growing buyback inventory after the December 2025 burn-recognition vote — mechanism, not a market sell. HYPE in mid-2026 is a clean example of a fee-funded buyback structure that runs neck-and-neck with supply growth.

---

*MrNasdog Pressure Framework analysis of Hyperliquid (HYPE), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 3, 2026.*

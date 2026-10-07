---
title:         "SPX Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description:   "SPX supply is flat: no mint, no owner, no vesting. 0 new SPX against a 5,722 SPX burn in 90 days gives −0.00% net and 0.00% next. 6.9% of all SPX is burned."
canonical_url: "https://mrnasdog.com/research/spx/inflation"
tags:          ["crypto", "spx", "spx6900", "memecoin"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/spx/inflation](https://mrnasdog.com/research/spx/inflation)*

# SPX Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

**SPX6900 (SPX)** has a supply that cannot grow: the Ethereum contract has no mint, so no new SPX was made in the last 90 days (**0 SPX** sold into the market from new supply) and none can be made in the next 90. The only flow was a small burn of **5,722 SPX** to the dead address, which puts net supply at **−0.00%** over 90 days against **930.99M SPX** in circulation. Our monitor reads **+0.01%**, close enough that no warning is needed.

## The verdict, in one paragraph

Over the 90 days to Oct 7 2026, SPX supply moved by **−0.0006%**, which shows as **−0.00%** on the coin page, and the next 90 days are projected at **0.00%**. The monitor, which works out supply from market value and price, reads **+0.01%**. The gap is **0.01 percentage points**, far inside our 0.5-point tolerance, so no ⚠ chip is shown and no deep walk was needed. SPX6900 is a **fixed-supply meme coin**: its float can only stay the same or shrink, and in practice it barely moves at all.

## Sell pressure: where new SPX comes from

**Protocol inflation is 0 SPX.** The SPX6900 token on Ethereum was created once, in August 2023, with exactly 1,000,000,000 coins. Its supply figure is fixed in the code, and the contract has no mint function: we listed every function in the deployed code and matched all 24 of them to the published source, and none of them can add coins. The owner key was also given up, so no one can change the rules later.

SPX also lives on Solana, Base, BNB Chain and Avalanche, but those copies do not add supply. Each one is a wrapped copy backed by real SPX locked on Ethereum. A bridge lockbox on Ethereum holds **109.20M SPX**, which covers the **82.96M** on Solana, the **26.12M** on Base and the small BNB Chain copy; a separate adapter holds the **62.04K** behind the Avalanche copy. Every SPX is counted once, on Ethereum.

**Vesting unlocks are 0 SPX.** SPX6900 was a fair launch with no team, investor or advisor share, so there is no unlock calendar at all. The wallet that launched SPX sent **68.78M SPX** to the dead address in August 2023 and holds nothing today. **Foundation and unscheduled unlocks are 0 SPX** because there is no foundation or reserve, and **long-term locked or bankruptcy supply is 0 SPX** because no estate, trustee or time lock holds SPX.

## Buy pressure: where new SPX goes

**Programmatic buyback is 0 SPX**: SPX6900 has no revenue and no team, so nothing buys coins back. **Protocol fee burn is 0 SPX**: transfers pay no fee, the launch tax was set to zero for good, and with the owner key gone a fee can never be switched back on. **Foundation buy is 0 SPX** and **new long-term lock is 0 SPX**, because there is no treasury and no staking contract.

The one live buy-side flow is **burns to the dead address: 5,722 SPX** in 90 days. We read the dead address at both ends of the window, rising from 69,007,090 to 69,012,813 SPX, and the list of transfers into it adds up to the same figure. Almost all of it came from a new token launchpad on Ethereum, live since Jul 27 2026, that pairs every new token with SPX and burns all the SPX fees its pools earn. Its own counter shows **5,720 SPX** burned: about 5,574 in its first week (Jul 27 to Aug 3), 147 on Sep 1–3 2026, and nothing since. A fan-built auto-buy app burned the last 1.7 SPX. Because the launchpad burn faded so fast and has no schedule, we count **0 SPX** for the next 90 days. In total, **69.01M SPX**, or 6.9% of the 1B, has been burned since launch.

## Foundation and overhang

SPX6900 has no foundation, no lab and no DAO treasury, so the overhang list is short. The first item is the SPX token contract itself, which holds **63.75K SPX** from old launch taxes and coins people sent to it by mistake; only the launch wallet can sell them. The second is the bridge lockbox with **109.20M SPX** and the Avalanche adapter with **62.04K SPX**, which back the copies on other chains and belong to their holders, not to any team. All three balances already count as circulating, because the only coins outside the float are the 69.01M in the dead address. We read these balances on-chain at every rebuild: if any of them falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How SPX compares to other meme coins

Among meme coins, SPX6900 sits in the strictest supply group: a **fixed supply with no mint**, like most Ethereum meme tokens launched in 2023. That is very different from **Dogecoin**, which is mined and adds 10,000 new DOGE with every block forever, so its supply grows every day by design. For DOGE the question is how fast new coins arrive; for SPX that question has a fixed answer of zero.

The other split is the burn. Some meme coins run a **steady burn** through a fee or a burn program that removes coins every week. SPX has no such engine. Its burns come from outside apps that choose to destroy SPX, and they are small and come in bursts: 5,722 SPX in 90 days is about 0.0006% of the float. So SPX is not deflationary in any meaningful way; it is simply flat.

The trade-off is about who holds the coins rather than how many exist. A fixed, fully circulating supply means no unlock will ever hit the market, but it also means every large holder is already free to sell. For a fair-launch meme coin like SPX6900, supply risk is close to zero and the price depends almost entirely on demand.

## What to watch in the next 90 days

No dated supply event falls between Oct 8 2026 and Jan 5 2027: there is no unlock, no scheduled burn and no vote. The first thing to watch is the launchpad burn. If new tokens launch against SPX and trade again, SPX fees will be burned once more; a steady run would show up as a live burn rate at the next rebuild. The second is the bridge lockbox: its 109.20M SPX should always match the copies on Solana, Base and BNB Chain, and a gap would point to a bridge problem rather than new supply. The third is the token contract's 63.75K SPX, which only the launch wallet can sell. None of these can create new SPX.

## Summary

SPX6900 (SPX) has a fixed supply of 1B coins, a contract with no mint, no owner and no vesting, and **930.99M SPX** in circulation after 69.01M were burned. Over the last 90 days the only flow was a **5,722 SPX** burn from a third-party launchpad, giving **−0.00%** net supply, with **0.00%** projected next. The main supply risk is not new coins but large free holders, and the main upside is any new burn source. On supply alone, SPX is about as steady as a coin can be.

*MrNasdog Pressure Framework analysis of SPX, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 8 2026.*

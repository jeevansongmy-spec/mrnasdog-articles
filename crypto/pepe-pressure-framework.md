---
title: "PEPE Inflation Analysis · September 2026 · Mixed flows, supply roughly steady"
description: "PEPE supply is flat at 0.00%: no mint function, no owner, no unlocks. Holders burned 118.34M PEPE in 90 days, 0.00003% of 420.69 trillion. Full reading."
canonical_url: "https://mrnasdog.com/research/pepe/inflation"
tags: ["crypto", "pepe", "memecoin", "ethereum"]
published: true
---

> Originally published at **[mrnasdog.com/research/pepe/inflation](https://mrnasdog.com/research/pepe/inflation)** by MrNasdog.

PEPE is flat: the MrNasdog Pressure Framework reads Pepe at **0.00%** net supply change over the trailing 90 days and **0.00%** over the next 90. The Pepe contract on Ethereum has no mint function and no owner, so no new PEPE can ever be created, and nothing is on a vesting or unlock schedule. Sell pressure is **0**; buy pressure is **118.34M PEPE** of voluntary holder burns, which is **0.00003%** of a fixed **420.69 trillion** supply.

## The verdict, in one paragraph

Against a circulating base of **420.69 trillion PEPE**, the framework books **0** of sell pressure and **118.34M PEPE** of buy pressure over the 90 days to **Sep 18 2026** — a net of **0.00%** — and projects **0.00%** for the next 90 days. The inflation monitor reads **+0.18%** for the same window, a gap of **0.18 percentage points**, which sits inside the framework's 0.5pp tolerance, so the overview page ships with no monitor-gap warning. The monitor estimates supply from market data rather than reading the Pepe contract, and a tiny price quoted to few digits moves that estimate more than anything happening on chain. The label for PEPE is a **fixed-supply memecoin with a flat float**: nothing can be added, and almost nothing is being removed.

## Sell pressure: where new PEPE comes from

Nowhere, and that is provable rather than promised. **Sell #1, protocol inflation, is 0.** All 420.69 trillion PEPE were created in one step when the Pepe contract was deployed on Ethereum in April 2023. The deployed code contains no mint function of any kind, its owner address reads empty, and the code never calls out to another contract — so there is no upgrade path, no hidden hook and no admin who could switch issuance on. The count of PEPE in existence actually fell across this window, from **420,689,899,646,442** to **420,689,899,645,099**, because some holders destroyed coins. The row carries a permanent tag for that reason: PEPE issuance is not paused, it is impossible.

**Sell #2, vesting unlocks, is 0.** Pepe had no investor round and no vesting schedule. At launch, 93.1% of the supply went into the Uniswap trading pool, whose liquidity tokens were burned, and 6.9% went to a team wallet. No lockup contract holds PEPE on a release calendar, so there is no unlock cliff in this window or the next.

**Sell #3, Foundation and unscheduled unlocks, is 0.** One wallet that descends from the original 6.9% team reserve still holds about **2.12 trillion PEPE**, around 0.5% of supply, and it did not move a single coin across the window. Even if it sold, it would add nothing to this reading: the published circulating supply already counts all 420.69 trillion PEPE as tradable, so a sale from that wallet moves coins within the float rather than into it. **Sell #4, long-term locked or bankruptcy, is 0** as well — PEPE has no bankruptcy estate, no trustee and no court-ordered distribution.

## Buy pressure: where new PEPE goes

**Buy #1, programmatic buyback, is 0.** Pepe has no company, no revenue and no treasury income, so there is nothing to fund a buyback, and none was announced. **Buy #2, protocol fee burn, is also 0** and permanently so: PEPE charges no tax on transfers, and with an empty owner address and no outside code the contract can reach, a fee can never be added. **Buy #3, Foundation buy, is 0** — there is no foundation, labs company or DAO — and **Buy #4, new long-term lock, is 0**, because PEPE has no staking and pays nothing for being locked.

The one live mechanism is an extra row, **Buy #5, holder burns, at 118.34M PEPE**. PEPE can be destroyed two independent ways, and the framework read both at both ends of the window. Holders sent **118,335,161 PEPE** to the dead address, which nobody can spend from, and put a further **1,343 PEPE** through the contract's own burn function, which lowers the count in existence. Every one of those transfers was enumerated and the totals match the balance changes exactly. **99.6%** of it came from a single contract in one burst on **Jul 27 2026**. Against 420.69 trillion, the whole burn is **0.00003%** of supply, worth about **$434**. Burns in the three quarters before this one ranged from about **6M** to **301M PEPE** with no schedule behind them, so the framework counts none for the next 90 days.

## Foundation and overhang

Pepe has no foundation, so the overhang is one wallet. The 6.9% team allocation passed from the launch wallet to the pepecexwallet.eth multisig in May 2023; roughly 16 trillion PEPE left that multisig for exchanges in **Aug 2023**, the rest moved to a new wallet, **6.9 trillion PEPE** was burned from it in **Oct 2023**, and about **3.21 trillion** went on to a multisig in **Dec 2023**. That multisig holds **2.12 trillion PEPE** today and has paid out only small amounts since, the last in **Dec 2025**. The launch wallet, the pepecexwallet.eth multisig and the wallet in between all hold zero. The reserve multisig balance is read from the chain at every rebuild, and if it falls between refreshes, that outflow enters Sell #3 at the next refresh — though, as above, it cannot raise the net reading while every PEPE is already counted as circulating.

## How PEPE compares to other fixed-supply memecoins

PEPE belongs to the strictest supply class there is: a token minted once, with the mint removed. That is a harder guarantee than a hard cap enforced by a schedule. Bitcoin is capped, but it still issues new coins with every block on a halving schedule, so its inflation reading is small and positive. Dogecoin has no cap at all and adds a fixed number of coins every minute, which keeps its reading positive forever. PEPE issues nothing, so its sell side is a flat zero rather than a small number.

Compared with memecoins that do burn, PEPE's burn is voluntary and tiny. Tokens with a transfer tax or a fee burn remove supply every time the coin is used, so their readings can turn genuinely negative. PEPE has no tax, so it only shrinks when a holder chooses to throw coins away, and that removed **0.00003%** this quarter. Compared with newer memecoins still working through team and investor unlocks, PEPE has no pending release at all: the float it has now is the float it will have.

The result is one of the flattest readings in the framework. The Pressure Framework does not grade PEPE on price, hype or demand; on supply alone, PEPE neither dilutes holders nor meaningfully rewards them through scarcity.

## What to watch in the next 90 days

First, the team-linked reserve multisig at **2.12 trillion PEPE**: a large transfer out would not change the net reading, but it would be the first sign the last piece of the original 6.9% is being spent. Second, holder burns — a single burst like the one on **Jul 27 2026** can land at any time, and the dead address and the count in existence are both read at every rebuild. Third, the spot PEPE exchange-traded fund filed by Canary Capital on **Apr 8 2026**, whose review is expected to run to about **Dec 2026**; approval would change who holds PEPE, not how many exist. Fourth, anything claiming a new PEPE burn programme or supply change: the contract cannot carry one, so any such plan would have to run through wallets, and it would show up in the burn reading.

## Summary

The MrNasdog Pressure Framework reads PEPE at **0.00%** over the trailing 90 days and **0.00%** projected forward: mixed flows, supply roughly steady. The structural fact is that the Pepe contract on Ethereum has no mint function and no owner, so the **420.69 trillion** supply created in 2023 is a ceiling nobody can raise, and there are no unlocks left. The only live flow is voluntary holder burns, **118.34M PEPE** this quarter, far too small to move the number. The main risk is not dilution but distribution: a team-linked multisig still holds **2.12 trillion PEPE**, and while its sale would not change the supply reading, it would change who holds the coins.

---

*MrNasdog Pressure Framework analysis of PEPE, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 18 2026.*

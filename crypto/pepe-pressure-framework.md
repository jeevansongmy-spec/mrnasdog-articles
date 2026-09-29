---
title: "PEPE Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description: "PEPE supply is flat: no mint, no vesting, all 420.69T PEPE minted in 2023. Holders burned 118M PEPE in 90 days for a net −0.00%, and 0.00% projected next."
canonical_url: "https://mrnasdog.com/research/pepe/inflation"
tags: ["crypto", "pepe", "memecoin", "ethereum"]
published: true
---

> Originally published at **[mrnasdog.com/research/pepe/inflation](https://mrnasdog.com/research/pepe/inflation)** by MrNasdog.

# PEPE Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

PEPE supply is flat. The **420.69T PEPE** on Ethereum were all created at launch in April 2023, the token contract has no mint function and its owner key was given up, so no new PEPE can appear. Over the last 90 days new supply was **0**, while holders burned **117.98M PEPE** — a net change of **−0.00%** (about −0.00003%), and **0.00%** projected for the next 90 days. Our monitor reads **−0.19%**, well within range.

## The verdict, in one paragraph

Over the 90 days to Sep 29 2026, PEPE added **0 PEPE** of new supply and lost **117.98M PEPE** to voluntary holder burns, for a net supply change of **−0.00%** of the **420.69T** circulating. For the next 90 days the framework projects **0.00%**: nothing can be minted, nothing is left to unlock, and holder burns have no schedule. Our supply monitor, which estimates supply from market value and price, reads **−0.19%** for the same window — a gap of **0.19 percentage points**, inside our 0.5-point tolerance, so no data-conflict warning is shown. The monitor's small swing comes from rounding a very low price, not from real coins moving. PEPE is a fixed-supply meme coin with a frozen float.

## Sell pressure: where new PEPE comes from

**Protocol inflation is 0.** PEPE is a plain ERC-20 token on Ethereum. The full supply was minted once, in the contract's constructor, in April 2023. We read the live contract code: it has a burn function but no mint function, it makes no calls to other contracts, and its owner address is empty, so the few owner-only switches (a blacklist and a holding limit used at launch) can no longer be touched. PEPE has no validators, no miners and no staking rewards to pay, so there is no issuance of any kind.

**Vesting unlocks are 0.** PEPE never had a vesting contract. At launch 93.1% of the supply went into the trading pool, whose pool tokens were burned, and 6.9% went to a team wallet meant for exchange listings and bridges. Both were spendable from day one, no unlock tracker lists any remaining release, and the circulating count equals total supply.

**Foundation and unscheduled unlocks are 0.** Pepe has no foundation. The team wallet that remains — a multisig holding about **2.12T PEPE** — did not move at all this window. And because PEPE's circulating count already includes every coin, a sale from that wallet would move coins inside the market rather than add new ones.

**Long-term locked or bankruptcy supply is 0.** No estate, trustee or time lock holds PEPE. The roughly 16T PEPE that three former team members pulled from the team multisig in August 2023 went straight to exchanges at the time and has long been part of the market.

## Buy pressure: where new PEPE goes

**Programmatic buyback is 0.** PEPE has no revenue and no treasury programme. Nothing buys coins off the market on the project's behalf.

**Protocol fee burn is 0.** Transfers pay no tax, and the contract has no fee path, so using PEPE destroys nothing. This is the key difference from coins whose every transaction burns a little supply.

**Foundation buy is 0** and **new long-term lock is 0.** No team or treasury bought PEPE this window, and PEPE has no staking or lock contract. Large wallets did accumulate during the September rally, and a planned spot fund would hold PEPE if approved, but those coins come from inside the market and leave total supply unchanged.

**Holder burns removed 117.98M PEPE.** Some holders send PEPE to a dead address that no one can spend from. This window **117,978,957 PEPE** went there across 55 transfers — most in one burst in late July — and another **1,371 PEPE** was destroyed through the contract's own burn function. At today's price that is about **$490**, or 0.00003% of supply. The last four quarters ranged from **6.1M** to **300.6M** burned with no plan behind them, so the framework books **0** for the next 90 days until a burn actually happens. Talk of a large community burn has circulated this year, but no official source or on-chain programme backs it. The dead address now holds **6.92T PEPE**, almost all from one team burn of 6.9T in October 2023.

## Foundation and overhang

PEPE has one team-linked overhang. Its lineage is traceable on-chain: the 6.9% launch allocation moved to the team exchange-listing multisig, then to a second wallet that sent the 6.9T burn in October 2023, and in December 2023 about 3.21T passed from that wallet to the multisig that holds **2.12T PEPE** today. Its last outgoing transfer was in December 2025, and its balance was identical at both ends of this window. A second multisig holds about **2.95T PEPE**, also unchanged; we found no link from it to the team, so it is watched rather than counted as team money. The original launch wallet and the listing multisig are empty. We read these balances from the chain at every rebuild. If the team multisig's balance falls between checks, the outflow is recorded in the foundation row at the next refresh — though with every PEPE already counted as circulating, a sale would change who holds the coins, not how many exist.

## How PEPE compares to other meme coins

Among large meme coins, PEPE sits at the most fixed end. Dogecoin is the opposite model: it has no cap and mints a fixed number of new coins every year to pay miners, so its supply grows every quarter by design. PEPE has no miners and no mint, so its supply can only stay the same or shrink.

Shiba Inu is the closer cousin — also an ERC-20 meme coin with its whole supply created at launch — but it adds burn tools and a layer-2 network whose fees feed small burns. PEPE has none of that machinery: its only burns are holders choosing to destroy coins, which this window came to less than a thousandth of a percent. Newer meme coins on fast chains often launch with large team or investor allocations on vesting schedules; PEPE has no vesting and no investor tranche at all.

The result is a coin whose price depends almost entirely on demand. There is no new supply for buyers to absorb, and no burn big enough to shrink the float, so the supply side of PEPE is steady and simple to read.

## What to watch in the next 90 days

**The team multisig.** Any drop from its **2.12T PEPE** balance would be the first team outflow since December 2025 — a move inside the market, but a signal worth watching.

**The spot PEPE fund.** A registration for a US fund that would hold PEPE directly was filed on Apr 8 2026 and has no fixed decision date. Approval would add a new buyer, but the coins would come from the existing float.

**Holder burns.** A repeat of the July burst, or any organised community burn, would show up at the dead address. The framework counts it only after it lands.

**Big-wallet flows.** Exchange withdrawals by large holders, like those around the Sep 22 2026 rally, change who holds PEPE but not how much exists.

## Summary

PEPE is a fixed-supply meme coin: all **420.69T PEPE** were minted at launch in 2023, the contract cannot mint more, and nothing vests. Over the last 90 days new supply was **0** and holders burned **117.98M PEPE**, a net **−0.00%**, with **0.00%** projected for the next 90 days. The main thing to watch is a team-linked multisig holding **2.12T PEPE**, which would move coins already in the market rather than add new ones. With supply frozen, PEPE's price rests on demand alone.

---

*MrNasdog Pressure Framework analysis of PEPE, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

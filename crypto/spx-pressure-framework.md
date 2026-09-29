---
title:         "SPX Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "SPX supply is flat: no mint, no owner, no vesting. 0 new SPX against 5,723 SPX burned in 90 days gives 0.00% net, the same next. 6.9% of all SPX is burned."
canonical_url: "https://mrnasdog.com/research/spx/inflation"
tags:          ["crypto", "spx", "spx6900", "memecoin"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/spx/inflation](https://mrnasdog.com/research/spx/inflation)*

# SPX Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

SPX6900 (SPX) has a supply that cannot grow. Over the last 90 days the framework counts **0 SPX** of new supply against **5,722.8 SPX** sent to the dead address, a net change of **−0.0006%**, shown as **0.00%**. The next 90 days are also **0.00%**. The SPX6900 token on Ethereum was created once with 1 billion coins, has no mint function and no owner, and 6.9% of all SPX already sits on the burn address.

## The verdict, in one paragraph

SPX6900 is flat. The framework's 90-day net is **−0.0006%** (displayed **0.00%**), the monitor reads **+0.05%**, and the gap is **0.05 percentage points** — well inside the 0.5-point line, so no warning chip is shown. The monitor's small plus comes from dividing market value by price each day, which wobbles a little even when not one SPX is created. The honest label for SPX is a **fixed-supply meme coin with a slowly growing burn pile**: nothing can add coins, and only outside apps and holders take a few away.

## Sell pressure: where new SPX comes from

Protocol inflation is **0**, and it is zero by design, not by chance. The SPX6900 contract on Ethereum wrote all 1,000,000,000 SPX to the launch wallet in its first transaction. After that, the only code that moves balances is the transfer function, which takes coins from one wallet and gives the same amount to another. The published code matches the code running on-chain, the list of functions it can call contains no mint, and the owner rights were given up, so no one can ever add an SPX. That is why the total supply of SPX6900 reads 1 billion at every block — the number is written into the code itself.

Vesting unlocks are **0**. SPX6900 went straight into a trading pool at launch with no team share, no investor share and no fund share. No unlock tracker lists a schedule for SPX, and the wallet that launched the token holds 0 SPX today. Foundation and unscheduled unlocks are **0** because there is no foundation, no treasury and no team wallet. Long-term locks and bankruptcy releases are **0**: no estate, trustee or time-lock holds SPX for later release.

## Buy pressure: where new SPX goes

There is no programmatic buyback (**0**) because SPX6900 earns nothing: it is a meme coin with no business, no revenue and no treasury. There is no protocol fee burn (**0**) either. The token once charged a launch tax, but that tax is now zero and, with the owner rights given up, it can never be switched back on. There is no foundation buying (**0**) and no staking or lock contract (**0**).

What does move is the dead address, the one place SPX goes to be destroyed. Over the 90 days to Sep 29 2026, **5,722.8 SPX** landed there in 31 transfers, which we read one by one and matched to the change in the dead address's balance to within a fraction of a coin. Almost all of it — **5,720.5 SPX** — came from one launchpad app that pairs new tokens with SPX and burns part of its trading fees in SPX. That app burned **5,574 SPX** in its launch week (Jul 27 to Aug 3 2026) and about **147 SPX** in early September, its last burn on Sep 3 2026. For scale, only **171 SPX** were burned in the nine months before this window. Because these burns follow one app's activity and have no schedule, the next 90 days are booked at **0**. The burn pile now holds **69.01M SPX**, or **6.9%** of all coins ever made — which is why only **930.99M SPX** count as circulating.

## Foundation and overhang

SPX6900 has no team-controlled overhang in the usual sense. The one held-back pile is **62,097 SPX** inside the token contract itself: old launch taxes plus coins that people sent to the contract address by mistake. Only the launch wallet can sell them, and they are already counted as circulating, so a sale would move coins inside the float rather than add new ones. We read this balance from the chain at each rebuild.

The largest single wallet is the bridge contract on Ethereum, holding **109.22M SPX**. Those coins back the SPX copies on Solana (**82.93M**), Base (**26.19M**) and smaller amounts on BNB Chain and Sui. A copy is a claim on a locked coin, so the framework counts every SPX once, on Ethereum. A different Solana token that also calls itself SPX6900 appeared around Sep 20 2026; it is not on the project's own list and is not counted. If the token contract's own balance falls between refreshes, the outflow is checked at the next rebuild — but because it is already circulating, it would still add no new supply.

## How SPX compares to other meme coins

Among meme coins, SPX6900 sits in the strictest supply class: a fixed-supply ERC-20 with no mint and no owner. That puts SPX next to coins like PEPE, which also launched with a fixed supply and renounced control, and far from Dogecoin, which mints about 5 billion new DOGE a year to miners with no cap. For a holder, the difference is simple: Dogecoin's supply grows every minute, while SPX6900's can only shrink.

SPX also differs from meme coins with built-in burns. Shiba Inu leans on community burn portals and app burns that take small amounts off a very large supply; SPX has no burn portal of its own, and its burns come from outside apps. And unlike newer launchpad meme coins, where a creator or team often keeps a share that can be sold later, SPX6900 has no team share at all. The main supply question for SPX is therefore not new coins but where existing coins sit — on exchanges, with a few large holders, or bridged to Solana and Base.

## What to watch in the next 90 days

First, the launchpad app that burns SPX: if its tokens trade again the way they did in late July, burns could restart, and the next rebuild would count them. Second, the Moonshot listing vote for the Solana copy of SPX, pushed on Sep 26 2026 — a listing moves coins between wallets and does not change supply. Third, the bridge contract's **109.22M SPX**: a shift between chains changes where SPX trades, not how many exist. Fourth, the look-alike Solana token named SPX6900: it can confuse buyers but adds nothing to SPX supply. None of these can create a new SPX.

## Summary

SPX6900 (SPX) is a fixed-supply meme coin on Ethereum: 1 billion coins were made at launch, the contract cannot mint more and has no owner, and nothing vests. Over the last 90 days **0 SPX** of new supply met **5,722.8 SPX** of burns, almost all from one launchpad app, for a net of **0.00%**, with the next 90 days also at **0.00%**. The monitor agrees within **0.05 points**. The key risk for SPX is not dilution but concentration: large holders and the bridge contract can move big amounts of coins that already exist, while the supply itself has a hard ceiling that is only ever falling.

---

*MrNasdog Pressure Framework analysis of SPX, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

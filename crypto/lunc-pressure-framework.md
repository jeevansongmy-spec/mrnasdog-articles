---
title:         "LUNC Inflation Analysis · September 2026 · Mixed flows, supply roughly steady"
description:   "Terra Classic mints nothing and burned 5,863.2M LUNC in 90 days, yet reads +0.27%: staked LUNC sits outside the float and 20,849.4M unbonded into it."
canonical_url: "https://mrnasdog.com/research/lunc/inflation"
tags:          ["crypto", "lunc", "terraclassic", "tokenomics"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/lunc/inflation](https://mrnasdog.com/research/lunc/inflation)*

# LUNC Inflation Analysis · September 2026 · Mixed flows, supply roughly steady

Terra Classic creates no new LUNC at all — its issuance settings read zero, and the count of LUNC in existence fell at every one of 91 samples across the last 90 days — and it destroyed **5,863.2M LUNC** over that window through a burn tax and monthly exchange burns. The Pressure Framework still reads Terra Luna Classic at **+0.27%** over the trailing 90 days and **+0.23%** over the next 90, because staked LUNC sits outside the circulating float this page divides by and **20,849.4M LUNC** unbonded into that float. The burn is real. It is outnumbered roughly three and a half to one.

---

## The verdict, in one paragraph

Against a circulating base of **5,531,897M LUNC**, the framework books **20,849.4M LUNC** of sell pressure and **5,863.2M LUNC** of buy pressure over the trailing 90 days — a net of **+0.27%** — and projects **+0.23%** for the next 90 as the higher burn tax carries a full quarter. The inflation monitor reads **+0.27%** for the same window, a gap of **0.002 percentage points**, far inside the framework's 0.5pp tolerance, so LUNC ships with no data-conflict warning. The agreement is worth stating, because the two numbers are built differently: the monitor watches the classified circulating supply move, while the framework measures the burn and the unbonding separately and adds them. The label for Terra Luna Classic is a **deflationary chain with an inflationary float** — the token supply shrinks every day, and the tradable share of it grows anyway.

## Sell pressure: where new LUNC comes from

It does not come from minting. Terra Classic's issuance module reports an inflation rate of zero, annual provisions of zero, and both inflation bounds at zero, and the swap module that once minted LUNC against the failed stablecoin was replaced by an explicitly no-mint version in a 2025 governance vote. Across the window the count of LUNC in existence fell at every sample and rose at none — the strongest available evidence that nothing is being created, since a mint anywhere would appear as an increase. Validators and delegators are paid out of transaction taxes, gas and a pre-funded reward reserve, all coins that already exist. So **Sell #1, protocol inflation, is 0**, watched rather than closed because a vote could switch issuance back on.

**Sell #2, vesting unlocks, is 0**, structurally: Terra Classic has no company, no foundation entity and no team allocation left to release, and no schedule has been voted since the restart. Unlock trackers do publish a Terra vesting calendar, but it belongs to the successor token on a different chain. **Sell #4, long-term locked or bankruptcy, is 0**, and that one was measured rather than assumed: the Terraform Labs estate wallet held **293.2M LUNC** at the start of the window and **293.2M LUNC** at the end, one hundred and one coins apart across 90 days, and the wind-down trust had distributed nothing to creditors as of its most recent quarterly report.

The entire sell side is **Sell #5, staked LUNC returning to the float, at 20,849.4M LUNC**, and it is invisible in the supply figure most Terra Classic coverage quotes. The circulating supply this page divides by excludes staked LUNC — established here by measuring it at both ends of the window, and corroborated by a second independent classifier publishing the same figure — so every coin that unbonds is a coin arriving on the tradable market. Bonded LUNC fell from **915,655.4M** to **894,806.0M** across the 90 days, and the validator set thinned from **99** bonded validators to **87**. The same number comes out two independent ways — the staking pool's own balance, and the sum of every bonded validator's stake — and they agree to the last unit.

## Buy pressure: where new LUNC goes

**Buy #2, the protocol fee burn, is 4,648.4M LUNC**, and it is the mechanism Terra Classic is famous for. Every on-chain transfer pays a tax; a governance vote tripled it from 0.5% to 1.5% on **Aug 2 2026**, pinned to a single block. Four fifths of what the tax collects is destroyed outright and the rest funds the validator reward reserve and the community treasury — a split confirmed to the unit on three separate burn blocks, at the old rate and the new one. Verifying the burn takes care, because Terra Classic's burn address is not a wallet that fills up: it is a chain module that destroys its whole balance in the same block it receives anything, so it reads zero at every height and a build watching it alone reports no burn at all. The count of LUNC in existence is the only readable surface, and it fell **5,863.2M**. Tripling the tax did not triple the burn: the daily pace went from **30.0M** to **75.0M**, so taxed volume fell about a sixth once the tax rose.

**Buy #5, the exchange fee burn, is 1,214.8M LUNC** — the remainder of the destruction, and a separate mechanism with a separate owner. One exchange routes part of its LUNC trading fees to the burn module on the first of each month, and three firings land inside this window, each read out of the block itself: **604.3M** on **Jul 1 2026**, **275.6M** on **Aug 1 2026** and **334.9M** on **Sep 1 2026**, all from one wallet. It is booked apart from the tax burn because it answers to trading volume on a company's books rather than to a chain parameter, and it can stop without a vote. **Buy #1, programmatic buyback, is 0** — Terra Classic runs no programme buying LUNC on the open market. **Buy #3, foundation buy, is 0**, because there is no foundation to do the buying. **Buy #4, new long-term lock, is 0**: staking moved the other way, and that release is booked on the sell side.

## Foundation and overhang

Terra Classic has no foundation, so the overhang is chain-owned, and there are three pots worth watching. The validator reward reserve, which pays stakers in place of a mint, fell from **42,427.0M** to **37,453.8M LUNC**. The community treasury rose from **8,223.1M** to **8,810.3M LUNC** even after two passed votes spent **291.7M** out of it, because the burn tax routes a share back in faster than the votes spend it. The bridge escrow backing wrapped LUNC on other networks holds **78,784.7M LUNC**, and it is a mirror rather than an addition — the escrow is larger than every wrapped copy combined, so nothing is double-counted. None of the three books a number, for the same reason: the classified float already counts them, so money leaving them changes who holds LUNC without changing how much is tradable. The one balance the float leaves out is staked LUNC. If any of these three pots falls between refreshes in a way the float can see, the outflow enters Sell #3 at the next refresh.

## How LUNC compares to other burn-tax chains

Terra Classic belongs to a small class: chains whose issuance is switched off entirely and whose only supply mechanism is destruction. That puts it closer to a fee-burn network like Ethereum after its fee-burning upgrade, or to an exchange token running scheduled buy-and-burn, than to the uncapped continuous-emission layer ones it is usually charted against. The difference from a fee-burn network is where the tax lands: Ethereum burns a base fee tied to block-space demand, while Terra Classic taxes the transfer amount itself, so the LUNC burn scales with value moved rather than with congestion — and, as this window shows, raising the rate can shrink the base it applies to. The difference from an exchange token is ownership: a buy-and-burn is funded by a company's revenue and can be cut when revenue falls, while Terra Classic's tax is a chain parameter only a vote can change. LUNC carries both kinds at once, which is why they are booked as separate rows.

The comparison that actually explains this page is with proof-of-stake chains whose published circulating supply includes staked coins. On those, unbonding is invisible to an inflation reading, because the coins never left the float. Terra Classic is classified the other way, and that single convention is worth more to the number on this page than the burn tax is. A chain that destroys coins every day and still reads inflationary is not a contradiction; it is a reminder that supply pressure is measured against the tradable share, not the total.

## What to watch in the next 90 days

First, the exchange fee burn, which fires on **Oct 1 2026**, **Nov 1 2026** and **Dec 1 2026** at a projected **334.9M LUNC** a firing; it has fallen by nearly half since **Jul 1 2026**, and another step down takes a visible bite out of the buy side. Second, the staking balance: bonded LUNC is the whole sell side, and a quarter in which it stops falling would flip this page deflationary without a single parameter changing. Third, the burn tax itself — the vote that raised it to 1.5% on **Aug 2 2026** can raise or cut it again, and the 2.5-fold burn response to a 3-fold rate rise is the number any future proposal should be judged against. Fourth, the community treasury, the only pot on the chain with a spender rather than a schedule.

## Summary

The MrNasdog Pressure Framework reads Terra Luna Classic at **+0.27%** over the trailing 90 days and **+0.23%** projected forward: mixed flows, supply roughly steady. The structural mechanism is not inflation but unbonding — Terra Classic minted nothing, destroyed **5,863.2M LUNC** through a 1.5% burn tax and three monthly exchange burns, and still lost ground because **20,849.4M LUNC** came out of staking and into a float that never counted it. The key risk is that the burn is the half anyone can change and the unbonding is not: a vote can cut the tax and an exchange can stop burning, but nothing in the protocol slows a staker deciding to leave. The genuine comfort is the ceiling — no new LUNC can appear without a vote to restart issuance, and the count of coins in existence has done nothing but fall.

---

*MrNasdog Pressure Framework analysis of LUNC, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 8 2026.*

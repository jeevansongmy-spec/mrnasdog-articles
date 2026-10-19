---
title:         "SUN Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description:   "SUN is mildly deflationary: no SUN can be minted, and a revenue buyback burned 9.03M SUN in 90 days, −0.05% net, with about 8.41M more due around Oct 25 2026."
canonical_url: "https://mrnasdog.com/research/sun/inflation"
tags:          ["crypto", "sun", "sunswap", "defi"]
published:     true
---
Originally published at [SUN Inflation Analysis · October 2026 · Mixed flows · supply roughly steady](https://mrnasdog.com/research/sun/inflation).

# SUN Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

<!-- main-page -->
This is the long supply read. For the signal, the price drivers and the questions people ask about SUN, see [mrnasdog.com/research/sun](https://mrnasdog.com/research/sun).

SUN is a slowly shrinking token. The SUN contract cannot create a single new coin, so new supply in the last 90 days was **0 SUN**, while the SUN.io buyback burned **9,025,027 SUN** on Jul 25 2026. That leaves the supply down **0.05%** over 90 days, the same **−0.05%** that market data shows, with about **8.41M SUN** more due to burn around Oct 25 2026. The catch is concentration: eight quiet wallets hold **14.92B SUN**, about three quarters of every coin.

## The verdict, in one paragraph

Over the 90 days to Oct 19 2026, SUN's net supply change is **−0.05%**: nothing was added and **9.03M SUN** was burned against **19.22B SUN** in circulation. The market-wide reading for the same 90 days is **−0.05%** as well, a gap of under **0.01 percentage points**, so no warning flag is needed. The next 90 days should look the same, at about **−0.04%**, with one quarterly burn of roughly **8.41M SUN**. SUN is a fixed-supply token with a small, steady revenue burn: deflationary by design, but only just.

## Sell pressure: where new SUN comes from

Protocol inflation is **0**, and it can never be anything else. The SUN token contract on TRON only holds the standard functions for moving balances: there is no mint, no burn, no owner and no upgrade path anywhere in its code. All **19,900,730,000 SUN** were created when the token launched (the 2021 redenomination multiplied the original 19.9M SUN by 1,000), so SUN.io's mining rewards and veSUN rewards are paid out of coins that already exist.

Vesting unlocks are **0**. SUN.io launched without a team allocation, a private sale or a pre-mine. The only schedule ever published, a four-year linear release of the SUN DAO's **47.16%** share set at launch, has run its full course. Every SUN that has not been burned already counts as circulating, so there is no locked bucket left to release.

Foundation and unscheduled unlocks are **0**. Large SUN wallets exist (see the overhang section), but they already sit inside the circulating count, so a transfer from one of them to an exchange moves coins between holders rather than adding new SUN. Long-term locked or bankruptcy supply is also **0**: no estate, trustee or long lock is releasing SUN.

## Buy pressure: where new SUN goes

The programmatic buyback is the only thing removing SUN, and it booked **9,025,027 SUN** in the window. SUN.io feeds it from four places: **0.05%** of every SunSwap V2 trade, one sixth of the fees from the SunSwap V3 TRX/USDT pool (added on May 2 2026), **100%** of SunPump's protocol revenue and **50%** of SunX's net revenue. The revenue is swapped into SUN in a burn wallet, and once a quarter the wallet sends everything to TRON's black hole address. Round 51, covering Apr 25 to Jul 25 2026, burned **9,025,027 SUN** on Jul 25 2026 and brought the all-time total to **678.55M SUN**, about 3.4% of the original supply.

The next round, number 52, is due around **Oct 25 2026**. The burn wallet has already bought **6.06M SUN** since the July burn, and at the pace of the last 90 days the round comes to about **8.41M SUN**. The burns used to happen every four weeks; since round 50 in April 2026 they happen once a quarter, so round 53 (around Jan 25 2027) falls just outside the next 90 days.

The protocol fee burn is **0** as a separate line, because the fee share that reaches SUN is spent through the buyback and is counted there once. A Foundation buy is **0**: apart from the revenue buyback, nothing shows a SUN.io treasury buying SUN. A new long-term lock is **0** as well. Holders can lock SUN for 6 months to 4 years to get veSUN, which carries votes on mining rewards and half of the stablecoin-pool fees, and the lock vault holds **477.4M SUN**. Locked SUN still counts as circulating, so the vault takes nothing out of the float.

## Foundation and overhang

The real story in SUN's supply is who holds it. Eight wallets with no public owner hold **14.92B SUN**, roughly **75%** of every coin ever made: **3.11B**, **2.52B**, **1.79B**, **1.68B**, **1.66B**, **1.50B**, **1.48B** and **1.19B SUN**. Seven of them did not send a single SUN in the last 90 days. The 2.52B wallet paid out **1.2M SUN**, a tiny amount next to its balance. Because all eight already count as circulating, they add nothing to the supply number, but a sale from any of them would hit the market far harder than any burn can offset.

Two smaller pools are watched as well: the burn wallet, which holds **6.06M SUN** waiting for the October burn, and the veSUN lock vault at **477.4M SUN**, whose locks expire on their own dates. Each of these balances is watched on-chain. If any of them falls between checks, the outflow enters foundation sell pressure at the next refresh.

## How SUN compares to other DeFi exchange tokens

SUN copies the Curve playbook on governance: lock the token for up to four years, receive vote-escrowed power, and use it to steer mining rewards. The difference is on supply. CRV pays its liquidity rewards with newly minted CRV, so Curve's supply rises every day; SUN pays its rewards from coins that were created at launch, because its contract cannot mint. On the supply side SUN behaves more like a fixed-cap token with a slow burn than like an emissions-funded DEX token.

Its closest relative is JST, the token of JustLend DAO on the same TRON network. Both route platform revenue into buyback-and-burn rounds. JST's rounds are much larger relative to its supply: TRON DAO reported that 1.71B JST, about **17.29%** of its supply, had been removed by Jul 17 2026, against **3.4%** for SUN after more than four years of burns. SUN's burn is steady but small, worth well under one tenth of a percent of supply each quarter.

Against exchange tokens that burn a fixed share of exchange profit, SUN's buyback depends on on-chain activity: SunSwap trading, SunPump launches and SunX perpetuals. When TRON DeFi is busy the rounds grow (round 50 burned 18.84M SUN over five months); when trading is quiet they shrink. That makes the SUN burn a usage signal more than a price support.

## What to watch in the next 90 days

**Around Oct 25 2026:** the round 52 buyback-and-burn notice. We expect about **8.41M SUN**; anything far below the **6.06M SUN** already sitting in the burn wallet would mean coins were moved out instead of burned.

**The eight large wallets:** any movement from the **14.92B SUN** held in eight quiet wallets, especially transfers to exchanges, matters more than any burn.

**The veSUN vault:** the lock vault holds **477.4M SUN**; a steady drain would show holders choosing not to relock.

**Platform revenue:** SunPump launches and SunX trading volume decide how big round 53 (around Jan 25 2027) will be.

## Summary

SUN is mildly deflationary: its supply fell **0.05%** in the 90 days to Oct 19 2026, as a quarterly revenue buyback burned **9.03M SUN** and nothing new was created. The supply is capped by code at **19.90B SUN**, **678.55M** of it already burned, and the next burn of about **8.41M SUN** is due around Oct 25 2026. The key risk is concentration, not inflation: eight wallets hold about three quarters of all SUN, and a sale from them would outweigh years of burns.

*MrNasdog Pressure Framework analysis of SUN, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 19 2026.*

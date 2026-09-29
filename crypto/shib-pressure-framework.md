---
title: "SHIB Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description: "SHIB supply is roughly steady: no mint and no vesting, and burns removed 4.18B SHIB in 90 days, 0.0007% of 589.24T, so the net reads 0.00% back and forward."
canonical_url: "https://mrnasdog.com/research/shib/inflation"
tags: ["crypto", "shib", "shiba-inu", "memecoin"]
published: true
---

> Originally published at **[mrnasdog.com/research/shib/inflation](https://mrnasdog.com/research/shib/inflation)** by MrNasdog.

Shiba Inu (SHIB) supply is roughly steady and very slightly shrinking: the SHIB token on Ethereum cannot create a single new coin, and holders and apps burned **4.18B SHIB** over the last 90 days. Against **589.24T SHIB** in circulation, that burn is about **0.0007%**, so the net reads **0.00%** over the last 90 days and the next 90 days, while the independent supply monitor reads **−0.09%**. SHIB has no mint, no vesting, no buyback and no team unlock — its supply can only go down, and only by what people choose to burn.

## The verdict, in one paragraph

For the 90-day window ending **Sep 29 2026**, the Pressure Framework reads **SHIB at −0.0007% net**, which shows as **0.00%**: the sell side added **0 SHIB** and the buy side removed **4.18B SHIB** through burns. The independent supply monitor reads **−0.09%** over the same window. The gap between the two is **0.09 percentage points**, well inside the **0.5-point** tolerance, so no data-conflict flag is shown. Looking forward, only the steady part of the burn is projected, about **1.07B SHIB**, which is still **0.00%** of supply. The cite-able label for Shiba Inu is a fixed-supply meme token whose burns are real but far too small to move the float.

## Sell pressure: where new SHIB comes from

Protocol inflation is **0**, and it can never be anything else. SHIB is a plain ERC-20 token on Ethereum, and its runtime code offers only transfer, approve, allowance and burn functions: there is no mint function, no owner, no pause switch and no upgrade path. All **1 quadrillion SHIB** were created at launch in August 2020, and no transfer from the zero address, the mark of a mint, appeared in the window.

Vesting unlocks are **0** because nothing ever vested. At launch half of the supply went into a Uniswap trading pool and half was sent to Vitalik Buterin, with no team tranche, no investor round, no token sale and no unlock calendar. There is nothing left to release.

Foundation and unscheduled unlocks are **0**. The Shiba Inu team has never published a treasury wallet that holds SHIB and discloses no holdings of its own. The original deployer wallet still holds **50.5M SHIB** and an early wallet holds **2.25M SHIB**; neither moved.

Long-term locked or bankruptcy supply is **0**. The **54.9B SHIB** seized by the US government in the FTX case moved to a new wallet on **Jul 15 2026** and has not been sold. Both the old and the new wallet sit inside the circulating count, so the move adds nothing new — though a sale would be real selling.

## Buy pressure: where new SHIB goes

A programmatic buyback is **0**: the Shiba Inu project runs no contract or treasury that buys SHIB off the market. A foundation buy is **0** too, and a new long-term lock is **0** — SHIB staked in the ShibaSwap vault stays inside the circulating count, and the vault actually shrank this window, from **3.54T** to **3.47T SHIB**.

The protocol fee burn books **0** on Ethereum. Shibarium, the Shiba Inu layer-2 network, turns part of its gas fees into SHIB and burns it, and that burn removed about **131.4M SHIB** this window. But it lands on Shibarium's own copy of SHIB, which has been barely backed on Ethereum since the 2025 bridge hack: the Ethereum bridge holds only **90.9M SHIB**, and it did not move. No Ethereum SHIB left the market because of the Shibarium burn.

The whole buy side is holder and app burns: **4.18B SHIB** sent to addresses no one can spend from — two dead addresses, the SHIB token contract itself, and the token's burn function. Every one of those transfers was read on the Ethereum chain and matched to the balances at both ends of the window. One trading app that burns part of its fees sent **3.11B SHIB**, almost all of it between **Jul 25 2026** and **Jul 28 2026**, the biggest burn week in a year. The rest came from about 30 wallets and apps at a steady pace near **360M SHIB a month**. Only that steady pace is carried forward, about **1.07B SHIB** for the next 90 days, because the July burst has no schedule.

## Foundation and overhang

Shiba Inu has almost no team-controlled overhang to watch. The largest single tracked balance is the **54.9B SHIB** held in the US government's FTX-case wallet, which moved on Jul 15 2026 and is checked on-chain every day. The original deployer wallet (**50.5M SHIB**) and an early wallet (**2.25M SHIB**) are dormant and checked on-chain every day. The treasury that funds repayments to users hurt by the 2025 Shibarium bridge hack has no published address, so it is checked by hand every two weeks through official posts. Exchange wallets and the staking vault belong to their depositors and are not team supply. If any of these balances falls between refreshes, the outflow enters the sell side at the next refresh.

## How SHIB compares to other meme tokens

SHIB sits at the far end of the meme-token range: a fixed supply with no issuance at all. Dogecoin, the other big dog-themed coin, is the opposite design — a proof-of-work chain that mints **10,000 DOGE** every block with no cap, so its supply grows every day by design. SHIB, by contrast, can only shrink, because its code has no way to add coins and a burn function to remove them.

Compared with tokens that burn by protocol, SHIB's burn is voluntary. Exchange tokens and fee-burning chains destroy coins automatically out of revenue or gas, often at a pace of several percent a year. SHIB's burns depend on holders and apps choosing to send coins away, and even a record week of **about 2.9B SHIB** is a rounding error on **589.24T**. The Shibarium fee burn was meant to be the protocol engine, but it now burns an unbacked layer-2 copy rather than Ethereum SHIB.

The practical result: SHIB carries none of the unlock or emission risk that newer meme tokens with team and launch allocations carry, and none of the steady dilution of an inflationary coin. Its supply story is settled. Whatever moves the SHIB price comes from demand, not from supply.

## What to watch in the next 90 days

First, the **54.9B SHIB** FTX-case wallet: any sale from it would be real selling into the market, even though it adds no new supply. Second, another app-driven burn burst like the one of **Jul 25 2026**; a repeat would lift the buy side, but it would still round to **0.00%**. Third, the Shibarium reindexing planned to finish in **Q4 2026** and any move to restore the bridge's backing, which is what would let the Shibarium fee burn count again. Fourth, any Doggy DAO governance vote touching supply or the burn — none is scheduled.

## Summary

Shiba Inu (SHIB) is a fixed-supply Ethereum token: it cannot mint, nothing vests and the team holds no disclosed supply, so sell pressure is exactly **0**. Holder and app burns removed **4.18B SHIB** in the 90 days to **Sep 29 2026**, most of it in one late-July burst, which is only **0.0007%** of the **589.24T SHIB** in circulation. The Pressure Framework therefore reads SHIB supply as roughly steady at **0.00%** both back and forward, in line with the monitor's **−0.09%**. The main risk is a sale from the seized FTX-case wallet; the ceiling is structural — SHIB supply can never rise above today's level.

*MrNasdog Pressure Framework analysis of SHIB, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

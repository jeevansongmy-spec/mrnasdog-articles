---
title:         "HYPE Inflation Analysis · September 2026 · Mixed flows, supply roughly steady"
description:   "HYPE supply is roughly steady at +0.05% over 90 days and next: a 1.98M HYPE fee buyback plus burns offset 2.35M of team, staking and foundation supply."
canonical_url: "https://mrnasdog.com/research/hype/inflation"
tags:          ["crypto", "hype", "hyperliquid", "defi"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/hype/inflation](https://mrnasdog.com/research/hype/inflation)*

# HYPE Inflation Analysis · September 2026 · Mixed flows, supply roughly steady

HYPE, the gas and staking coin of the Hyperliquid chain, sits almost exactly at balance. Over the last 90 days Hyperliquid added **2.35M HYPE** to the market — **1.32M** released by the core-contributor vault, **0.79M** of staking rewards and **0.24M** from the Hyper Foundation and community-grants wallets — while the Assistance Fund buyback took **1.98M HYPE** off the market and fee burns destroyed **0.26M**. The MrNasdog Pressure Framework reads HYPE at **+0.05% net** over the last 90 days against a supply-monitor reading of **−0.02%**, and at the same **+0.05%** for the next 90 days. A second Hyperliquid buyback, funded by reserve yield, is due to make its first payment on **Oct 3 2026**; it has not paid yet and is not counted. The HYPE cap is fixed at **1,000M**.

## The verdict, in one paragraph

For the 90-day window ending **Sep 13 2026**, the Pressure Framework books **2,349,942 HYPE** of sell pressure against **2,239,744 HYPE** of buy pressure, a net of **+0.05%** of the **222.45M** circulating HYPE float. The independent supply monitor reads the same window at **−0.02%**, a gap of about **0.06 percentage points**, inside the half-point tolerance, so HYPE ships with **no data-conflict flag** — though the classified HYPE float behind that monitor has barely moved since late May, so the small gap is not proof that the two agree. The forward column also reads **+0.05%**: every row is carried at its measured pace. The new reserve-yield buyback is left at **zero** until it pays, because its size depends on reserve balances and interest rates that no one has published as a fixed amount. The label for Hyperliquid is **self-funded balance**: trading fees now buy back almost exactly what staking and the team put on the market.

## Sell pressure: where new HYPE comes from

Sell #1, protocol inflation, is **0.79M HYPE**. Hyperliquid does not mint new HYPE; stakers are paid out of a **411.60M** reserve that was set aside at launch but never issued. That distinction protects the **1,000M** cap, but it does not change what a holder sees: every staking reward is a HYPE coin that was not in the market yesterday. The reserve paid out about **2.44M HYPE** across the window, a figure that closes three ways — against the vault's own staking rewards, against the reserve's balance, and against the published reward curve, which pays less per coin as more HYPE is staked. Of that, **1.65M** went to the team vault, the Hyper Foundation and the grants wallet; those rewards are counted only when those wallets send HYPE out, below, so booking them here as well would count them twice. What reaches ordinary Hyperliquid stakers is the **0.79M** in this row.

Sell #2, vesting unlocks, is **1.32M HYPE**, and this is the row where the Hyperliquid unlock calendar and the chain disagree most. The core-contributor vault received **238M HYPE** at launch, and its published schedule allows roughly **9.92M HYPE** a month — about **29.75M** across this window. The vault took a small fraction of that. It sent out **452,000 HYPE** on **Jul 7 2026**, **433,024** on **Aug 6 2026** and **433,419** on **Sep 6 2026**, each split across about ten outside wallets, and each close to what the vault earns from staking in a month. The vault still holds **241.25M HYPE**, all of it staked. The framework books what was released, never what was allowed.

Sell #3, foundation and unscheduled unlocks, is **0.24M HYPE** from two Hyperliquid project wallets. The Hyper Foundation wallet, which received **60M** at launch, sent **50,000 HYPE** on **Aug 4 2026** and another **50,000** on **Aug 31 2026**. The community-grants wallet, which received **3M**, sent **143,501 HYPE**, most of it one **140,000** transfer on **Jun 20 2026**. Both wallets already have more HYPE unstaked and waiting — **50,000** and **106,500**. Sell #4, long-term locked or bankruptcy supply, is **zero**: no estate or trustee holds HYPE, and the listed companies keeping HYPE treasuries bought on the open market, so their coins were already in the float.

## Buy pressure: where new HYPE goes

Buy #1, the programmatic Hyperliquid buyback, is **1.98M HYPE**. Almost all trading fees on the Hyperliquid exchange flow to the Assistance Fund, which buys HYPE on the open market around the clock and holds it at a system address that has no private key. Read at both ends of the window, that balance rose from **45.19M** to **47.17M HYPE**, and its full trading record since late August adds up to the balance change to the last coin. It has never sent a single HYPE out. In **December 2025** Hyperliquid validators voted, with **85%** support, to treat that balance as burned. It is not a burn in the strict sense — the coins still count inside Hyperliquid's total supply — but nobody holds a key to them, and moving them would take a change to the chain's own code. They are off the market, which is what the buy side measures.

Buy #2, the protocol fee burn, is **0.26M HYPE**, and it combines two burns that were checked for overlap. On the trading layer, fees paid in HYPE for faster order handling and for launching new spot and perpetual markets are destroyed outright: HYPE total supply fell by **222,250** across the window. On HyperEVM, the smart-contract side of Hyperliquid, gas fees are destroyed as well — **36,688 HYPE**. In a series of paired readings the trading-layer supply fell while the HyperEVM burn balance barely moved, so the two are separate flows and both count. Buy #3, foundation buying, is **zero**: neither project wallet bought HYPE back. Buy #4, new long-term locks, is **zero**: launching a market or a stablecoin on Hyperliquid requires a **500,000 HYPE** bond, but that bond sits in ordinary staking, which is already part of the circulating count.

## Foundation and overhang

The Hyperliquid overhang is large and almost entirely on-chain, which is why every piece of it is re-read at each refresh rather than taken on trust. The biggest is the un-issued reward reserve at **411.60M HYPE**, which drains a little every day into staking rewards. Next is the core-contributor vault at **241.25M HYPE**: its calendar says it could release ten times what it does, and whether it ever starts is the single largest risk on this page. The Hyper Foundation wallet holds about **60.45M HYPE** and the community-grants wallet about **2.97M**, both mostly staked. The Assistance Fund address holds **47.17M HYPE** and has never sent a coin out. Exchange custody wallets and unlabelled large holders are left out — those coins belong to depositors or to no identified group. If any of these balances falls between refreshes and the HYPE does not go to a burn, the outflow enters Sell #3 at the next refresh.

## How HYPE compares to other exchange and perpetuals tokens

Most proof-of-stake chains pay validators with freshly minted coins and hope a fee burn catches up. Hyperliquid inverts the funding: its staking rewards come from a fixed, pre-allocated reserve, so HYPE issuance can never push past the cap, and its trading fees are large enough to buy back roughly as much HYPE as the reserve and the team release. The Hyperliquid exchange collected about **$76M** of fees over the last 30 days against a HYPE market value near **$17.4B** — a ratio that puts HYPE among the fee-heavy tokens rather than the quiet chains.

Against exchange tokens that buy back and burn on a quarterly calendar, the HYPE buyback runs continuously, every day, straight out of trading activity, so its size moves with volume and price rather than with a published sizing rule. Against exchange tokens whose buybacks sit in a company account, the Hyperliquid destination is stronger: the Assistance Fund has no key and no owner who could decide to sell. The trade-off is the supply side. A token whose team allocation is already spent carries no vesting risk; HYPE still carries a **241.25M** vault whose release pace is a choice, not a rule, and a buyback that only matches new supply rather than overwhelming it.

## What to watch in the next 90 days

First, **Oct 3 2026**: the reserve-yield buyback is due to make its first payment to the Assistance Fund, with further payments every 30 days. Its size is not fixed — it depends on the dollar reserves behind USDC on Hyperliquid and on interest rates — so it is counted at zero until it pays; a large first payment would lower the forward reading at the next refresh. Second, the core-contributor vault on **Oct 6**, **Nov 6** and **Dec 6 2026**: a release anywhere near the **9.92M** calendar would swamp every buyback on this page. Third, the **50,000** and **106,500 HYPE** already unstaked in the foundation and grants wallets, which are the next Sell #3 entries once they move. Fourth, Hyperliquid trading volume, which sets the size of both the buyback and the fee burn.

## Summary

The MrNasdog Pressure Framework reads HYPE at **+0.05% net** over the trailing 90 days and **+0.05%** over the next 90, a Hyperliquid supply that is roughly steady. The structural mechanism is a fixed **1,000M** cap with staking paid from a pre-set reserve, offset by a fee-funded Assistance Fund buyback of **1.98M HYPE** into a keyless address and **0.26M HYPE** of fee burns. The key risk is the core-contributor vault: it holds **241.25M HYPE** and releases a small slice of what its calendar allows, and that pace is a decision the team can change. The cap is the ceiling; the vault is the swing factor.

MrNasdog Pressure Framework analysis of HYPE, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 13 2026.

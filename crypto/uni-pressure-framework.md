---
title: "UNI Inflation Analysis · October 2026 · Mixed flows · supply roughly steady"
description: "UNI supply is roughly steady: Uniswap's fee burn destroyed 5.71M UNI in 90 days against a 5.00M UNI treasury growth budget. Net −0.13%, next 90 days +0.15%."
canonical_url: "https://mrnasdog.com/research/uni/inflation"
tags: ["crypto", "uni", "uniswap", "defi"]
published: true
---

Originally published at [https://mrnasdog.com/research/uni/inflation](https://mrnasdog.com/research/uni/inflation) by MrNasdog.

# UNI Inflation Analysis · October 2026 · Mixed flows · supply roughly steady

**UNI supply is roughly flat.** In the 90 days to Oct 1 2026 the Uniswap DAO treasury released **5.00M UNI** as a growth budget, while the Uniswap fee switch destroyed **5.71M UNI** and a multisig sent **113K UNI** back to the treasury, so net supply fell **0.13%**. For the next 90 days we expect another **5.00M UNI** out and about **4.07M UNI** burned, a rise of about **0.15%**; the monitor reads **+0.02%**.

## The verdict, in one paragraph

Over the last 90 days UNI supply changed by **−0.13%** of its **620.28M** circulating coins: **5.00M UNI** came in and **5.82M UNI** went out. The independent monitor reads **+0.02%** for the same window, a gap of **0.15 percentage points**, well inside our 0.5-point tolerance, so no warning chip is shown. For the next 90 days the same growth payout meets a smaller burn in coin terms, because UNI now costs nearly three times what it did in early July, so we project **+0.15%**. In one line: **UNI is a fee-burn token whose burn roughly cancels its treasury budget.**

## Sell pressure: where new UNI comes from

**Protocol inflation: 0.** No UNI was minted. The Uniswap token contract still reports a total of exactly **1,000,000,000 UNI**, the same number it held at launch in 2020, and we confirmed that this number is stored in a live field that a mint would change, not a fixed constant. The DAO does hold a right to mint up to **2% a year**, about 20M UNI, open since Jan 1 2024. It has never used it and no vote to use it exists, so it is a watch item, not a flow.

**Vesting unlocks: 5.00M UNI.** The UNIfication vote of December 2025 set up a growth budget of **20M UNI a year** for Uniswap Labs, paid in **5M UNI** slices each calendar quarter through a vesting contract that pulls coins from the DAO treasury. The July slice left the treasury on **Jul 14 2026**. The treasury is the only pile not counted as circulating, so each slice is new supply for the market. The October slice unlocked on **Oct 1 2026** and can be claimed at any time, so we book **5.00M UNI** again for the next 90 days. The January slice falls on Jan 1 2027, just after that window. The treasury has approved **25M UNI** more for this budget, five slices.

**Foundation and unscheduled unlocks: 0.** Apart from the growth slice, nothing left the DAO treasury in the window. **Long-term locked or bankruptcy: 0.** There is no estate or trustee holding UNI, and the original team and investor vesting finished in 2024.

## Buy pressure: where new UNI goes

**Programmatic buyback: 5.71M UNI.** Since the Uniswap fee switch went live, part of every swap fee on covered pools collects in a vault on each chain. The vault can only be emptied by destroying a fixed lot of UNI, 2,000 or 4,000 coins at a time, so traders buy UNI on the market and send it to the burn address whenever the fees inside are worth more than the lot. Over the 90 days the burn address gained **5,708,001 UNI**, worth about **$30.2M** at each day's price. We counted every one of the 2,445 burn transfers and the total matched the burn address balance to the last coin.

The pace changed inside the window. On **Jul 27 2026** two governance votes switched fees on for Uniswap v4 pools and for Robinhood Chain. Before that the burn bought about **$148K** of UNI a day; after it, about **$404K** a day. Because each burn is set by the dollar value of fees, a higher UNI price means fewer coins per dollar. At about **$8.94** per UNI, the post-change pace gives roughly **4.07M UNI** for the next 90 days.

**Protocol fee burn: 0.** No fee is destroyed directly; the burn always runs through bought UNI, so it lives in the buyback row. **Foundation buy: 113K UNI.** On **Jul 30 2026** a DAO-linked multisig sent **113,138 UNI** back into the treasury, which took those coins out of circulation; it was a one-off, so the next 90 days carry 0. **New long-term lock: 0.** UNI has no staking contract; a staking idea was posted on the forum in June 2026 but never reached a vote.

## Foundation and overhang

The one large overhang is the **Uniswap DAO treasury**, the governance timelock, with **267.25M UNI**. It is exactly the gap between total supply (**887.53M** after burns) and circulating supply, so it is the whole non-circulating pile. **25M UNI** of it is already approved for the growth budget at 5M a quarter; the rest needs a governance vote to move. Inside the circulating float we also track the Labs growth wallet at about **12.0M UNI**, the 2020 airdrop contract at about **12.5M UNI** of unclaimed coins, and the DAO-linked multisig at about **20K UNI**. Selling these would add nothing new to supply, but they show who could sell. We read these balances on the chain at every rebuild. If the treasury's balance falls between refreshes by more than the scheduled slice, the outflow enters Sell #3 at the next refresh.

## How UNI compares to other DEX tokens

Most exchange tokens pay their users with new coins. Emission-based tokens such as **CAKE**, **CRV** and **AERO** mint fresh supply every week to reward liquidity providers and voters, and then try to win it back with burns or long locks. UNI works the other way round: Uniswap mints nothing, pays liquidity providers only from trading fees, and turns a slice of those fees into a **UNI burn**. Its only new supply is a fixed, voted budget from a treasury that already exists.

The closest match is a fee-funded buyback token such as **HYPE**, where trading fees buy the token on the market. The difference is where the coins go. In UNI's design the bought coins are destroyed at the burn address, so they cannot come back, while a buyback into a fund or treasury can be spent again later. The trade-off is that UNI's burn depends on how many pools pay fees and on how busy they are, and it shrinks in coin terms when the price rises.

The other contrast is the cap. UNI has a hard cap of 1B plus a dormant 2% mint right; burns have already cut total supply to 887.53M. Emission tokens have no such ceiling in practice. So for UNI, the main supply question is how fast the DAO spends its treasury, not how fast new coins are printed.

## What to watch in the next 90 days

**Oct 1 2026 — growth slice.** The fourth 5M UNI slice of 2026 unlocked today; the claim moves it from the treasury into circulation.

**Oct 3 2026 — Arc fee vote ends.** A live proposal would switch Uniswap fees on for Arc, Circle's new chain; if it passes, its fees join the burn. We have not booked it yet.

**v4 fees, part two.** The July v4 fee vote was labelled part one of two, so a second batch of v4 fee switches is likely to follow. No date is set; each one would raise the dollar pace of the burn.

**Burn pace against price.** The burn bought about $592K of UNI a day in September. If UNI's price holds near $9, that means fewer coins burned than in early summer; a falling price would burn more coins for the same fees.

**Jan 1 2027 — next slice.** The next 5M UNI growth slice unlocks just after this window and will enter the following quarter's count.

## Summary

UNI is in mixed flows with supply roughly steady: over 90 days the DAO treasury released **5.00M UNI** to Uniswap Labs and the fee-funded burn destroyed **5.71M UNI**, for a net change of **−0.13%**, and we project **+0.15%** for the next 90 days. Nothing is minted and nothing vests besides the 5M-a-quarter growth budget. The key risk is a bigger treasury spend: the treasury still holds **267.25M UNI**, and a vote could also switch on the unused 2% yearly mint. The ceiling is the 1B cap, with total supply already burned down to **887.53M UNI**.

---

*MrNasdog Pressure Framework analysis of UNI, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 1 2026.*

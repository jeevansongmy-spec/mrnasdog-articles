---
title:         "NEXO Inflation Analysis · August 2026 · Mixed flows, supply roughly steady"
description:   "NEXO cannot mint and cannot burn, and its buyback pays into a reserve the tradable count already includes — so it removes nothing. Framework 0.00%, monitor +0.09%."
canonical_url: "https://mrnasdog.com/research/nexo/inflation"
tags:          ["crypto", "nexo", "cefi", "exchange-token"]
published:     true
---

> Originally published at **[mrnasdog.com/research/nexo/inflation](https://mrnasdog.com/research/nexo/inflation)** by MrNasdog.

**TL;DR.** NEXO is the Ethereum token of Nexo, a lending, exchange and card company, and over the 90 days to **Aug 26 2026** the MrNasdog Pressure Framework reads **zero** sell pressure against **zero** buy pressure on a circulating base of **1,000,000,000 NEXO**, for a net of **0.00%**. The NEXO contract carries no mint instruction and no burn instruction in its deployed code, so the 2018 supply of **1,000,000,000 NEXO** is fixed in both directions. The buyback everybody cites cannot change that: it pays into a reserve that the circulating count already includes, and that reserve has held exactly **114,800,950.27 NEXO** since 2023 without receiving a single token. NEXO is **fixed, not deflationary**.

## The verdict, in one paragraph

For the 90-day window ending **Aug 26 2026**, the Pressure Framework reads **NEXO at 0.00% net**: sell pressure of **0**, buy pressure of **0**, on a circulating base of **1,000,000,000 NEXO**. The next 90 days read **0.00%** as well, because there is no mechanism in the NEXO contract that can add a token and none that can remove one. Our supply monitor reads **+0.09%** for the same window, a gap of **0.09 percentage points**, comfortably inside the half-point tolerance, so no monitor-gap flag is raised on this build — and that residual is arithmetic noise rather than issuance, because the monitor infers supply from market value divided by price while the on-chain supply held at **1,000,000,000** to eighteen decimal places at both ends of the window. The right label for NEXO is **a hard-fixed exchange-and-lending token whose buyback recycles float rather than retiring it**.

## Sell pressure: where new NEXO comes from

It does not come from anywhere. Sell #1, protocol inflation, is **0**, and this build did not take that on trust from a tidy round number — a supply that reads exactly **1,000,000,000** is a reason to check harder, not to relax. We pulled the deployed NEXO contract code and searched it for the instructions that would create or destroy tokens. The mint instruction is not present. The burn instruction is not present. Neither is a destroy path or a minter role, and Nexo's own published token source agrees: the supply is written once at deployment and never touched again. Nexo is a company, not a blockchain, so there is also no block reward, no validator subsidy and no staking emission to book.

Sell #2, vesting unlocks, is **0**, because the entire **1B NEXO** was distributed at the 2018 sale and no escrow contract holds a locked tranche today. Sell #3, foundation and unscheduled unlocks, is **0** on measurement rather than on assumption. Nexo's company reserve is four wallets, and this build finally reads them directly: they hold **208,333,332**, **98,437,500**, **33,333,332** and **13,749,996 NEXO**, summing to **353,854,160 NEXO**. That total was identical to nine decimal places at both ends of this window, and identical again at samples running back to **Aug 26 2024**. Two years, not one token moved. Sell #4, long-term locked or bankruptcy, is **0**: Nexo is an operating going concern with no estate, no trustee schedule and no court-ordered distribution.

## Buy pressure: where new NEXO goes

Buy #1, the programmatic buyback, is the row this page exists to settle, and it is **0** for two independent reasons. The first is structural and survives any amount of spending. Take the supply and subtract the tradable count: **1,000,000,000** total minus **1,000,000,000** circulating leaves **nothing** outside the float. Every NEXO in existence is counted as tradable, and that includes the **114,800,950 NEXO** parked in Nexo's Investor Protection Reserve, the published on-chain address that receives every repurchase. Buying tokens into a reserve the count already includes moves them between pockets; it cannot shrink a float that never excluded them. A reserve of **114.8M** simply cannot fit inside a non-circulating bucket of zero.

The second reason is that the buyback did not fire at all. The reserve held **114,800,950.27 NEXO** on the day this window opened and the identical figure on the day it closed, and at every block we sampled in between and back through **Jun 1 2023**. Every buyback programme Nexo itself has published belongs to 2020 to 2023; the last one closed on **Mar 2 2023** after repurchasing **63,244,559.958 NEXO** for **$50,002,838.84**. A claim that a fresh **$50M** programme was approved in December 2025 keeps circulating in secondary coverage, but no Nexo announcement we could fetch supports it and the designated reserve shows no matching inflow.

Buy #2, the protocol fee burn, is **0** and always has been. Nexo's repurchases are frequently described elsewhere as a buyback and burn; the measurement disagrees. We read the dead addresses instead of trusting the phrase, and one holds **10.71 NEXO** while the other holds **nothing**, both unchanged across the window. Destroyed NEXO over 90 days: **zero**. Repurchased NEXO vests for twelve months in the reserve and is then recycled into NEXO-denominated interest payouts, which returns it to the market rather than retiring it. Buy #3, foundation buy, is **0**, with no dated and sized entity purchase disclosed in the window. Buy #4, new long-term lock, is **0**: Nexo's loyalty tiers look like a lock and are not one, because the qualifying NEXO stays in a wallet that keeps earning and stays withdrawable at any moment, and a freely transferable position is not a lock.

## Foundation and overhang

Two team-controlled overhangs are tracked on NEXO, and this build has an on-chain address for both. The first is the company reserve of **353,854,160 NEXO** across four wallets, re-read from chain at every refresh, with no published release schedule. It is worth naming what that figure equals: a rival supply classifier publishes NEXO circulating at **646,145,840**, and one billion minus that is **353,854,160** — the same number to the token. The reserve wallets and the disputed slice are the same thing. The second overhang is the Investor Protection Reserve of **114,800,950 NEXO**, also re-read from chain at every refresh, also unscheduled. Together they are **46.9%** of all NEXO sitting in identified company hands, counted as tradable by the number this framework divides by. Neither has moved. If either balance falls between refreshes, that outflow enters Sell #3 at the next refresh.

## How NEXO compares to other exchange and lending tokens

NEXO belongs to the family of company-issued exchange and platform tokens funded by corporate revenue rather than by protocol fees, and inside that family it sits at the passive extreme. The active model is an exchange token whose contract exposes a working burn instruction and whose operator calls it quarterly, permanently lowering the supply ceiling. NEXO cannot do that even if its board wanted to: the instruction is absent from the deployed code, so no amount of revenue can retire a token. Its repurchases are custody transfers.

The deeper structural split is not burn versus no burn — it is where the buyback pays, and that single fact inverts the reading. A protocol whose buyback delivers into a contract sitting outside the circulating count genuinely removes supply, and the framework books it as real buy pressure. A protocol whose buyback delivers into a treasury the count already includes removes nothing, and the framework books it at zero however large the cheque. NEXO is firmly in the second group, and unusually clearly so, because its non-circulating bucket is not merely small, it is exactly zero. Against a chain with continuous validator issuance NEXO looks far better — it has no issuance to fight — but against a genuinely deflationary token it is simply flat, and flat is the honest label.

## What to watch in the next 90 days

First, the Investor Protection Reserve at **114,800,950 NEXO**: an inflow would confirm a live repurchase programme, and an outflow would be genuine sell pressure entering Sell #3, since vested reserve NEXO is earmarked for interest payouts back to users. Second, the four company reserve wallets holding **353,854,160 NEXO**, static since **Aug 2024** — the largest single supply risk NEXO carries, and the one with no published schedule. Third, any Nexo primary announcement that actually confirms or retires the disputed December 2025 **$50M** buyback claim. Fourth, the token-weighted governance staking module reported live in early 2026: if Nexo publishes a contract address and a locked quantum, that becomes a real Buy #4 for the first time. Fifth, the newly listed venues from **Aug 21 2026** and **Aug 22 2026**, which change where NEXO trades but not how much of it exists.

## Summary

The MrNasdog Pressure Framework reads NEXO at **0.00% net supply change** over the 90 days to **Aug 26 2026** and **0.00%** for the next 90, on a circulating base of **1,000,000,000 NEXO**. The structural mechanism is a 2018 fixed pre-mint whose deployed contract contains no instruction to create or destroy a token, which makes NEXO immune to issuance and equally incapable of shrinking. The key risk is custody rather than issuance: **468,655,111 NEXO**, roughly **46.9%** of everything, sits in identified company wallets that the circulating count already treats as tradable, so any release is invisible to the headline supply figure and immediately real to the market. The ceiling is hard at **1,000,000,000 NEXO** and can never rise; it can never fall either.

---

*MrNasdog Pressure Framework analysis of NEXO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 26 2026.*

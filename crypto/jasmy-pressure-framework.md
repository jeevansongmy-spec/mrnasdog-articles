---
title:         "JASMY Inflation Analysis · July 2026 · Mixed flows · supply roughly steady"
description:   "JasmyCoin nets 0.00% supply change: a hard-capped 50B Ethereum token with no mint and no burn in its code, vesting finished since 2023, and a 555M reserve static for a year."
canonical_url: "https://mrnasdog.com/research/jasmy/inflation"
tags:          ["crypto", "jasmy", "jasmycoin", "ethereum"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/jasmy/inflation](https://mrnasdog.com/research/jasmy/inflation)*

# JASMY Inflation Analysis · July 2026 · Mixed flows · supply roughly steady

JasmyCoin books a clean **0.00%** net supply change across both the trailing and forward 90-day windows, and every one of the eight framework rows measures zero. JASMY is a hard-capped **50,000,000,000** ERC-20 on Ethereum whose deployed token code contains no mint function and no burn function at all, its 2021 launch allocation finished vesting in **2023**, and the single reserve wallet holding the last **555M** JASMY has not moved a coin in twelve months. Our supply monitor reads **+0.07%** over the same window — a gap of **0.07** percentage points, well inside tolerance. With **~49.4B** of the **50B** cap already circulating, JasmyCoin is a fully-distributed, inert-supply token.

## The verdict, in one paragraph

Across the trailing 90 days the JASMY ledger books **0** of sell pressure against **0** of buy pressure on a circulating float of **~49,445M JASMY**, for a net of **0.00%**. The forward read is identical at **0.00%**, because none of the mechanisms that move a token's supply exist here: JasmyCoin cannot issue, cannot burn, has no vesting calendar left and runs no buyback. Our supply monitor reads **+0.07%** over the same window — a gap of **0.07** percentage points, so no data-conflict flag is raised. That fractional reading is not a release; the monitor's own history shows the derived supply pinned at **49.445B** essentially every day since January 2026, and the 90-day-ago anchor simply landed on a downward rounding excursion. The cite-able label for JasmyCoin today is a **fully-distributed fixed-supply token**: the supply question is settled, and everything that happens to the JASMY price from here is demand.

## Sell pressure: where new JASMY comes from

Nowhere — and that is measured, not assumed. Protocol inflation is **0** because JasmyCoin has no protocol emission of any kind. JASMY is not a proof-of-work or proof-of-stake coin with a block subsidy; it is a plain ERC-20 whose entire **50,000,000,000** supply was created once, at genesis, in 2021. We read the token's on-chain total supply at both edges of the window and the two reads came back as the byte-identical value, **50,000,000,000** JASMY exactly. We then read the deployed contract code itself: it carries no minting function, no owner or admin function that could add one, and no pause switch. New JASMY is not merely unissued — it is unissuable in the code that is live today.

Vesting unlocks are **0** because JasmyCoin has run out of schedule. The genesis allocation split the **50B** cap into an ecosystem tranche, a funds-and-institutions tranche, a contributors-and-community tranche and an incentives tranche, and those tranches released through 2022 and **2023**. What remains is arithmetic: **~49.4B** of the **50B** cap — **98.9%** — is already in the market. No dated JASMY unlock appears on the project's own announcement surface or on any unlock calendar for the window. A vesting cliff that does not exist contributes nothing.

Foundation and unscheduled unlocks are **0** as well, and this row is where the JasmyCoin build got sharper this month. The entire non-circulating remainder of JASMY — the difference between the **50,000M** cap and the **49,445M** float — sits in one readable reserve wallet holding **555,000,322** JASMY. We read that wallet's balance at four points spread across a year and got the same number to seven decimal places every time. Not a coin has left it. A reserve that has been static for over a year gives the framework no firing to observe and no pattern to project forward, so the row is zero with the overhang tracked rather than estimated. Finally, long-term locked or bankruptcy supply is **0**: Jasmy Incorporated is an operating Japanese company, and there is no estate, trustee or court-ordered JASMY distribution anywhere in the picture.

## Buy pressure: where new JASMY goes

The buy side of the JasmyCoin ledger is just as empty, and that is the honest half of the story. A programmatic buyback books **0** because Jasmy does not run one. The only buyback-and-burn material that surfaces for JASMY is a third-party post soliciting BNB deposits against bonus tiers — a solicitation scheme, not a Jasmy mechanism — and it corresponds to no on-chain purchase or destruction whatsoever.

Protocol fee burn is **0** for the most fundamental reason available: the JASMY token contract has no burn function in its deployed code, so no JASMY can be destroyed by anyone. The customary dead address has received **315** JASMY across the coin's entire lifetime — a rounding error against **50B**. The obvious question is JasmyChain, the EVM Layer-2 built on Arbitrum Orbit that completed its mainnet migration on **Jan 17 2026** and uses JASMY as its gas currency. Gas paid on JasmyChain is collected by the chain's fee accounts, not burned, and the JASMY circulating on JasmyChain is bridged rather than newly issued — which is exactly why the Ethereum supply read flat through a window that sits six months after the L2 went live. A foundation buy books **0** with no disclosed treasury purchase in the window, and a new long-term lock books **0**: the only lockup Jasmy ever ran was a **100M** JASMY trial that began **May 1 2024** and was never repeated, and bridging to JasmyChain hands back a matching balance on the other side rather than removing float.

## Foundation and overhang

JasmyCoin has exactly one team-controlled overhang worth naming, and it is unusually clean. The reserve wallet holding **555,000,322** JASMY — roughly **1.1%** of the cap — is the whole of the non-circulating supply, and it is read directly on-chain each rebuild rather than inferred from a disclosure. Its balance was identical at **Jul 26 2025**, **Jan 25 2026**, **Apr 25 2026** and **Jul 24 2026**. There is no published calendar governing its release; it is simply still. If that wallet's balance falls between refreshes, the outflow enters the Foundation and unscheduled-unlocks row at the next refresh, and the framework reading changes with it.

Two things deliberately do **not** count as JasmyCoin overhang. The four largest JASMY wallets on Ethereum hold about **14,331M** between them — roughly **28.7%** of all JASMY — and every one of them was funded out of a labelled exchange deposit contract in late 2025. Those are custodial wallets holding customer coins, not project supply, and they were static through the window in any case. Uncoordinated holders and dispersed early investors are likewise treated as ordinary float. The framework watches identified, coordinated supply; on JasmyCoin that comes to one wallet and one number.

## How JASMY compares to other fixed-supply utility tokens

The structural family JasmyCoin belongs to is the fully-distributed, hard-capped ERC-20 — tokens minted once at genesis with no ongoing issuance, where the supply story finishes long before the demand story starts. Against a halving-model chain like Bitcoin, JASMY is stricter in one respect and weaker in another: Bitcoin still issues new coins on a decaying schedule and will keep doing so for another century, whereas JASMY's **50B** is complete today and cannot grow by a single unit. But a mining subsidy also buys a security budget; JASMY's cap buys nothing but certainty.

Against an uncapped continuous-emission Layer-1 — an Ethereum, a Solana, a Cosmos chain paying validators from new issuance — the contrast is sharper. Those chains carry a permanent structural headwind that has to be earned back through fee burn or staking absorption. JasmyCoin carries no headwind at all, which is why its framework reading is **0.00%** rather than a small positive number. The comparison that matters most, though, is against exchange tokens and fee-burning networks that run quarterly buybacks or transaction burns. Those tokens can post negative net supply — genuinely deflationary readings — because revenue is routed back into destroying float. JasmyCoin has no such pipe. Fees on JasmyChain are collected, not burned; there is no revenue-to-token mechanism; and the token code could not burn even if a programme were approved tomorrow, without a new contract. That is the ceiling on JASMY: a fixed, flat supply tops out at neutral. It will never be dragged down by dilution, and it will never be lifted by structural scarcity.

## What to watch in the next 90 days

First, the **555M** reserve wallet. It is the only address that can change the JASMY sell ledger, and any outflow from it is the single most material supply event available to this coin. Second, JasmyChain fee policy: if Jasmy ever routes L2 gas revenue into a buyback or deploys a burn contract, the buy ledger stops being empty by design — the chain went live **Jan 17 2026** and the ecosystem has been expanding since the third-party exchange launch of **Feb 2 2026**. Third, any repeat of the **May 1 2024** exchange lockup programme, which would land in the new long-term lock row. Fourth, Jasmy Incorporated's corporate announcements — the issuer publishes there before it publishes anywhere else, and its last token-relevant post predates this window. Fifth, JANCTION, the affiliated network whose digital-asset infrastructure was announced **Mar 27 2026**: it carries its own token, but any JASMY-denominated incentive attached to it would show up here first.

## Summary

The MrNasdog Pressure Framework reads JasmyCoin at **0.00%** net supply change over both the last and next 90 days, with all eight ledger rows measuring zero. The structural mechanism is a hard cap that is effectively spent: **50,000,000,000** JASMY minted once at genesis, **~49.4B** already circulating, no mint function and no burn function in the deployed Ethereum contract, vesting finished in **2023**, and a lone **555M** reserve wallet that has held the same balance for twelve months. The key risk is not dilution but discretion — that single reserve wallet has no published release schedule, so its stillness is a habit rather than a guarantee. The ceiling is equally clear: with no buyback and no burn pipe, JASMY cannot become deflationary, and a flat supply is the best reading this token can produce. Our supply monitor's **+0.07%** confirms the picture within a rounding error.

---

*MrNasdog Pressure Framework analysis of JASMY, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 25 2026.*

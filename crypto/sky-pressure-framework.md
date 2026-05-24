---
title: "Sky (SKY): The Endgame Token in the Middle of a Migration"
description: "A MrNasdog Pressure Framework read of Sky (SKY, formerly MKR): the Endgame migration is 99.95% complete (1 MKR : 24,000 SKY), USDS stability fees flow into Sky's surplus buffer. Mixed structural conditions while the token's monetary policy stabilizes."
canonical_url: "https://mrnasdog.com/research/sky/full"
tags: ["crypto", "sky", "maker", "defi"]
published: true
---

> Originally published at **[mrnasdog.com/research/sky/full](https://mrnasdog.com/research/sky/full)** by MrNasdog.

This is a **MrNasdog Pressure Framework** analysis of **Sky (SKY)** — the rebrand-and-redenomination of MakerDAO's MKR — on Metric 1 (sell pressure) and Metric 2 (buy pressure). Narrative (Metric 3) is covered separately. The short version: the migration from MKR to SKY is essentially complete (99.95% converted at a 1:24,000 ratio), and the protocol's USDS stability fees create a real but variable buy-side lever — similar in shape to the old MKR burn-and-mint dynamic, with a different surface.

## The setup

In 2024, MakerDAO rebranded to **Sky** and introduced a new token SKY at a fixed **1 MKR : 24,000 SKY** redenomination. The DAI stablecoin was rebranded to **USDS** (existing DAI still works; both circulate). The Endgame plan splits the protocol into SubDAOs (Spark, Stargate, etc.) with their own tokens. Sky governance still uses SKY (or MKR, which is interchangeable via the 1:24,000 upgrade contract).

Live numbers, origin-first from Ethereum mainnet RPC + Sky docs:

- **SKY total supply: 23,462,665,147 SKY** (~23.46B, verified on-chain via `totalSupply()`)
- **Migration status: ~99.95% of MKR converted to SKY** (~478K MKR still un-upgraded — small overhang)
- **Implied SKY at full conversion: ~23.46B** (1:24,000 × original ~977K MKR)
- **USDS issued: ~$5B+ across DAI + USDS** (stability fee–generating debt)
- Sky has no fixed max supply written into the SKY contract — issuance is governed by a "skyMint" mechanism for incentives + redemptions. Net issuance/redemption is governance-controlled.

## The sell ledger

*What the design predictably puts on the market.*

| # | Source | Tag | Value |
|---|---|---|---|
| 1 | Protocol inflation | **Tag B** | Sky SubDAO farming incentives — governance-controlled, currently modest |
| 2 | Vesting unlocks (still-locked allocations on schedule) | — | **~0** — no scheduled team vesting (Maker had none; Sky inherits) |
| 3 | **Team / DAO / identified-group holdings** | **Tag B** | Sky Foundation / SubDAO treasuries — TBD on-chain enumeration |
| 4 | Bankruptcy estate | — | **0** |

**Inflation is *discretionary*, not scheduled.** Unlike NEAR or TAO with hard-coded mint schedules, Sky's `skyMint` is a governance-callable contract used to fund SubDAO farming programs and protocol incentives. Recent issuance has been modest. **Tag B** because the address (governance multisig) is known but the timing is discretionary.

**Vesting: zero.** Maker (Sky's predecessor) was launched without a traditional team vesting schedule — early holders bought MKR in the 2017 sale and through governance. Sky inherits no scheduled vesting.

**Tag B is Sky's governance-controlled treasury + SubDAO multisigs.** Hard to enumerate cleanly without per-SubDAO address mapping. Flagged as TBD here.

**Bankruptcy estate: zero.**

## The buy ledger

*What the design predictably takes off the market.*

| # | Source | Value |
|---|---|---|
| 1 | **Revenue-backed buyback (Sky's "Smart Burn Engine" / surplus buffer)** | **Tag A** — variable, depends on USDS stability fees and surplus level |
| 2 | Burn mechanism | included in #1 (surplus buffer mechanism) |
| 3 | Locked allocations | — context only |
| 4 | Protocol-level demand (governance only) | small |

**This is Sky's structural strength.** USDS borrowers pay a **stability fee** in USDS to the protocol. When the protocol's surplus buffer exceeds a threshold, the excess is used (under Sky's flap auction / smart burn mechanism, the successor to Maker's classic flap) to **buy and remove SKY from circulation**. This is the closest thing in DeFi to a real revenue-backed buyback.

The rate is **variable**: in high-USDS-demand periods (high stability fees + lots of borrowing), the buyback accelerates. In low-demand periods, it slows. Recent volume has been modest but non-zero — meaningfully more than UNI's empty buy ledger, meaningfully less than HYPE's Assistance Fund.

## Net position

- **Sell:** discretionary Sky SubDAO incentives + governance-controlled treasury deployment — variable, modest today
- **Buy:** USDS stability-fee-driven SKY buyback via the surplus buffer — variable, real

**Net structural read: roughly balanced today, with both sides governance-sensitive.** Sky is the closest token in our coverage to a "fundamentally-revenue-linked" governance token — its buy pressure tracks actual stablecoin demand. That's both its strength (real economic linkage) and its variability (revenue swings with rates and demand).

Compared to the rest of our coverage:

- **BNB**: structural deflation from burns → favorable
- **HYPE**: AF buyback > vest → favorable
- **SKY**: revenue-linked buyback, governance-sensitive → **moderately favorable when USDS demand is strong**
- **UNI**: no buyback, no inflation → neutral
- **NEAR / TAO / ONDO**: structural sell > buy → unfavorable

## What to watch

1. **USDS stability fee + outstanding debt levels** — drives buyback rate. Sky publishes these on dashboards (`sky.money`).
2. **Surplus buffer balance** — threshold above which the smart burn engine activates.
3. **Sky governance proposals on SubDAO farming incentives** — affects the discretionary issuance line.
4. **MKR → SKY remaining conversions** — ~478K MKR left; small overhang during the tail end of migration.

---

*MrNasdog Pressure Framework analysis of SKY, Metrics 1 &amp; 2. Data + explanation only. Not financial advice. Numbers as of May 2026.*

*Data note: Total supply read directly from the SKY ERC-20 contract via Ethereum mainnet RPC. Migration math derived from the published 1 MKR : 24,000 SKY ratio. Surplus buffer mechanics per Sky protocol docs (`docs.sky.money`). The legacy MKR contract still exists; both MKR and SKY circulate during the migration tail.*

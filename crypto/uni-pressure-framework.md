---
title: "Uniswap (UNI): A Clean Sell Ledger and a Fee-Switch Decision That Won't Go Away"
description: "A MrNasdog Pressure Framework read of Uniswap (UNI): original 4-year vesting completed Sep 2024, no inflation today (but governance can enable 2%/yr), no buyback, no burn. The DAO Treasury holds 259.6M UNI (~26% of supply). The fee switch — debated for years — is the only structural buy-side lever."
canonical_url: "https://mrnasdog.com/research/uni/full"
tags: ["crypto", "uniswap", "defi", "dex"]
published: true
---

> Originally published at **[mrnasdog.com/research/uni/full](https://mrnasdog.com/research/uni/full)** by MrNasdog.

This is a **MrNasdog Pressure Framework** analysis of **Uniswap (UNI)** on Metric 1 (sell pressure) and Metric 2 (buy pressure). Narrative (Metric 3) is covered separately. The short version: UNI has the cleanest sell ledger of any DeFi token we cover today — original vesting is done, no inflation is active — but the buy ledger is also empty until governance enables the fee switch.

## The setup

UNI is the governance token of Uniswap, the dominant DEX on Ethereum and EVM L2s. ERC-20 (`0x1f98…f984`) with a **fixed 1B genesis supply** at launch in September 2020. The initial allocation: **60% community treasury** (600M UNI), **21.51% team** (215M, 4-year vest), **17.8% investors** (178M, 4-year vest), **0.69% advisors** (7M, 4-year vest). The 4-year vesting cliff completed in **September 2024** — meaning *all original allocations are now fully unlocked*.

The protocol's tokenomics also allow **a perpetual 2% annual inflation** that can be enabled by governance. **It has not been enabled.** The on-chain UNI contract's `mint()` function is callable only by the governance timelock, and no inflation proposal has passed.

Live numbers, origin-first from Ethereum mainnet RPC + Uniswap docs:

- **Total supply: 1,000,000,000 UNI** (fixed today, verified on-chain via `totalSupply()`)
- **Circulating: ~635.7M UNI** (~63.6%, per CoinGecko cross-check)
- **DAO Treasury (Timelock `0x1a9c…35bc`): ~259.6M UNI** (~26% of supply — read directly on-chain)
- **Uniswap Foundation grants treasury: tens of millions of UNI** (separately funded, smaller than the main Treasury)
- Price ~$3.47 → market cap ~$2.20B · FDV ~$3.47B

## The sell ledger

*What the design predictably puts on the market.*

| # | Source | Tag | Value |
|---|---|---|---|
| 1 | Protocol inflation | — | **0** (2%/yr available but not enabled by governance) |
| 2 | Vesting unlocks (still-locked allocations on schedule) | — | **0** (4-year vests completed Sep 2024) |
| 3 | **Team / DAO / identified-group holdings** | **Tag B** | **~259.6M UNI** in Treasury Timelock + Foundation grants |
| 4 | Bankruptcy estate | — | **0** |

**Inflation: zero today.** The 2%/yr perpetual inflation that governance can enable would add ~20M UNI/yr to the sell ledger. This is the single biggest negative catalyst latent in the design — but it has not been triggered in 5+ years and the political appetite has been low. **Watch it, don't price it in.**

**Vesting: zero.** All original 4-year vests (team, investors, advisors) finished in September 2024. There is no scheduled supply releasing into the market today. Original investor unlock pressure is no longer a structural force.

**Tag B is the DAO Treasury.** Per the new framework rule (only identified coordinated entities; both locked + unlocked count, de-dup against #1, #2, #4): the **Uniswap Treasury Timelock holds 259.6M UNI** (read on-chain). The Uniswap Foundation operates a separate grants treasury (tens of millions of UNI). Combined Tag B exposure is ~270–290M UNI — the DAO can deploy this via votes (grants, retroactive funding, market-making programs, etc.). Note: VC holdings that originally vested out are now distributed across many funds and excluded under the framework rule (Pantera-style noise).

**Bankruptcy estate: zero.**

## The buy ledger

*What the design predictably takes off the market.*

| # | Source | Value |
|---|---|---|
| 1 | Revenue-backed buyback | **0** — fee switch debated since 2022, never enabled |
| 2 | Burn mechanism | **0** — no protocol burn |
| 3 | Locked allocations | — context only (UNI staked in governance contracts is functionally liquid via undelegation) |
| 4 | Protocol-level demand (governance only) | **~0** — UNI is needed to vote, not transact |

This is where Uniswap is structurally weakest. The protocol generates ~$1B+ per year in trading fees, all of which go to **LP providers, not UNI holders**. The "fee switch" — the governance lever that would route a portion of LP fees to UNI stakers or to a buyback — has been debated since 2022, voted in temperature checks, never permanently activated. **Today the buy ledger is empty.**

## Net position

Combine the ledgers:

- **Sell, Tag A:** 0
- **Sell, Tag B:** ~270–290M UNI in DAO Treasury + Foundation grants (deployed at governance discretion)
- **Buy, Tag A:** 0

**The structural read is "neutral and waiting for a decision."** UNI has neither the relentless structural sell of an inflationary L1 (NEAR, TAO) nor the cliff schedule of a vesting-heavy token (ONDO). But it also has none of the structural buy that drives BNB or HYPE. Net: today it's quiet on both sides, with the actual price story coming from external demand (DeFi summer-style narratives) and from any DAO Treasury deployment decisions.

Compared to the rest of our coverage:

- **BNB**: supply ↓ from burns → favorable
- **HYPE**: AF buyback > vest → favorable
- **UNI**: clean sell ledger, empty buy ledger → **neutral, lever-dependent**
- **NEAR / TAO**: scheduled supply ↑, weak buy → unfavorable
- **ONDO**: scheduled cliffs, no buy → most unfavorable

## The two levers

UNI is unusual in having **two governance-controlled levers** that would move it in opposite directions:

1. **Fee switch enablement** (positive). Route some portion of trading fees to UNI holders/stakers or to a buyback. Single biggest structural catalyst available. Debated for years; activation odds rise whenever the DAO Treasury balance debate heats up.
2. **2%/yr perpetual inflation enablement** (negative). The protocol's tokenomics ALLOW this; governance can pass it. It has not been activated in 5+ years and there's no concrete proposal on the table — but it's a latent risk.

The framework gives UNI no credit for either today. Both are governance-dependent; until one passes, neither scores.

## What to watch

1. **Any fee-switch proposal that reaches a binding on-chain vote** (not just temp checks). Forum: `gov.uniswap.org`.
2. **Any 2%/yr inflation enablement proposal** — same channel.
3. **Uniswap Treasury Timelock balance changes** — read on-chain at `0x1a9c…35bc`. Large grants or program funding move this number.
4. **Uniswap Foundation grant cadence** — proxy for ecosystem Tag B deployment rate.

---

*MrNasdog Pressure Framework analysis of UNI, Metrics 1 &amp; 2. Data + explanation only. Not financial advice. Numbers as of May 2026.*

*Data note: Total supply + Treasury Timelock balance read directly from on-chain (`totalSupply()` and `balanceOf(0x1a9c…35bc)` on the UNI ERC-20 contract via Ethereum mainnet RPC). Circulating supply cross-checked via CoinGecko. Foundation grants treasury balance noted as separately funded but not address-enumerated in this draft.*

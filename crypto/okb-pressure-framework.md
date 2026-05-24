---
title: "OKB: After the 2025 Reset, a Hard 21M Cap"
description: "A MrNasdog Pressure Framework read of OKB: the 2025 OKX Reset burned ~235M+ OKB, cutting total supply to a hard 21M (BTC-style). No inflation, no vesting. Quarterly buyback-and-burn continues. Tag B opacity = the only structural risk."
canonical_url: "https://mrnasdog.com/research/okb/full"
tags: ["crypto", "okb", "okx", "exchange-token"]
published: true
---

> Originally published at **[mrnasdog.com/research/okb/full](https://mrnasdog.com/research/okb/full)** by MrNasdog.

This is a **MrNasdog Pressure Framework** analysis of **OKB** (OKX's exchange token) on Metric 1 (sell pressure) and Metric 2 (buy pressure). Narrative (Metric 3) is covered separately. The short version: after the 2025 OKX Reset burned ~235M+ OKB, total supply is now a hard **21 million** — BTC-style. Combined with continued buyback-and-burn, OKB has the most aggressive deflationary mechanics of any exchange token we cover.

## The setup

OKB is OKX's exchange token, originally an ERC-20 on Ethereum (`0x7523…2a86c`). Originally issued at ~300M total supply in 2018, OKX ran quarterly buybacks-and-burns for years, then in **2025 executed the "OKB Reset"** — a one-time mass burn that destroyed ~235M+ OKB and reduced **total supply to 21M** with a hard cap going forward. OKB Chain (X Layer) is OKX's L2 EVM chain that uses OKB as gas; the token bridges between Ethereum mainnet and X Layer.

Live numbers, origin-first from Ethereum mainnet RPC + OKX docs:

- **Total supply: ~21M OKB** (per CoinGecko cross-check; hard cap post-Reset)
- Ethereum mainnet contract holds ~429K OKB (the rest lives on X Layer + bridges)
- Price ~$82 → market cap ~$1.73B
- **No protocol inflation** (cap is enforced)
- **No team vesting today** (original 60% to team / advisors / investors vested out years ago)
- **Quarterly buyback-and-burn** funded by OKX exchange revenue

## The sell ledger

*What the design predictably puts on the market.*

| # | Source | Tag | Value |
|---|---|---|---|
| 1 | Protocol inflation | — | **0** (21M hard cap post-Reset) |
| 2 | Vesting unlocks (still-locked allocations on schedule) | — | **0** (original vests completed years ago; the Reset removed the rest) |
| 3 | **Team / DAO / identified-group holdings** — OKX corporate treasury | **Tag B** | not separately disclosed from custodial; **structural opacity** |
| 4 | Bankruptcy estate | — | **0** |

**Inflation: zero.** Hard 21M cap.

**Vesting: zero.** The 2018 distribution: 60% team/foundation (5-year vest), 30% ICO, 10% community. Vesting completed in 2023; the 2025 Reset burned much of the remaining team allocation. Nothing scheduled today.

**Tag B is OKX corporate treasury, with structural opacity** (same shape as BNB). OKX-labeled wallets on Etherscan are primarily exchange custodial — coins belonging to depositors, not OKX's discretion. The framework rule excludes custodial wallets. The actually-discretionary OKX corporate treasury is not separately disclosed in an identified multisig. **Honest read: small Tag B that's not enumerable to ONDO Foundation Safe precision.**

**Bankruptcy estate: zero.**

## The buy ledger

*What the design predictably takes off the market.*

| # | Source | Value |
|---|---|---|
| 1 | **Revenue-backed buyback** — OKX uses exchange revenue to buy OKB on the open market | **Tag A** — quarterly |
| 2 | **Burn mechanism** — purchased OKB sent to burn address | **Tag A** — same flow as #1, paired |
| 3 | Locked allocations | — context only (some OKB locked in X Layer staking; small) |
| 4 | Protocol-level demand (gas on X Layer + OKX fee discount) | **Tag B** — exchange-utility-driven |

**Buyback + burn is the structural strength.** OKX commits to quarterly buyback-and-burn funded by exchange profits. Unlike BNB's Auto-Burn (which destroys from a team pool, not market), OKX's mechanic **does buy on the open market** before burning. This makes it a true Tag-A revenue-backed buyback (rare in our coverage — alongside HYPE's Assistance Fund and SKY's surplus buffer).

The volume depends on OKX revenue + the buyback rate set by management. Historically the equivalent of low single-digit millions of OKB per quarter at recent prices, though the post-Reset 21M cap means each buyback now removes a larger % of supply.

## Net position

- **Sell, Tag A:** 0 (no inflation, no vesting)
- **Sell, Tag B:** small but opaque (OKX corporate treasury not separately disclosed)
- **Buy, Tag A:** quarterly revenue-backed buyback-and-burn (real market buying, variable with exchange revenue)

**Net structural read: favorable, with the same opacity caveat as BNB.** OKB combines BNB's "no scheduled supply" cleanliness with a genuine open-market buyback (which BNB lost when Auto-Burn replaced the pre-2021 mechanic). Against ETH-style structural cleanliness it's even tighter — 21M hard cap is more deflationary than ETH's net-flat trend.

Compared to the rest of our coverage:
- **OKB**: 21M hard cap + quarterly revenue-backed buyback — **most aggressively deflationary exchange token**
- **BNB**: ↓3–6%/yr from burns, Auto-Burn ≠ market buyback — favorable
- **HYPE**: AF buyback > vesting — favorable
- **SKY**: surplus-buffer revenue-linked buyback — moderately favorable
- **ETH**: net flat-to-deflationary, lowest gross inflation — favorable

## The only structural risk

Same as BNB: **opacity**. OKX the company holds OKB outside identified custodial wallets, and the framework cannot fully read this. If a future leak or transparency disclosure reveals a separately-held corporate treasury, that becomes a new Tag B line. Until then, the visible sell ledger is empty.

## What to watch

1. **Quarterly OKB buyback-and-burn announcements** at `okx.com/help-center/okb`.
2. **OKX exchange revenue trend** — drives buyback volume.
3. **X Layer (OKB Chain) gas demand growth** — adds a second protocol-level demand line.
4. **Any OKX transparency disclosure** of separately-held corporate treasury — would add Tag B.

---

*MrNasdog Pressure Framework analysis of OKB, Metrics 1 &amp; 2. Data + explanation only. Not financial advice. Numbers as of May 2026.*

*Data note: 21M total supply per CoinGecko cross-check (matches OKX's post-Reset published cap). Ethereum mainnet contract balance read directly via `eth_call` → `totalSupply()` on the OKB ERC-20 (`0x7523…2a86c`); the mainnet contract holds only ~429K OKB with the bulk on X Layer + bridges. OKX corporate vs. custodial split flagged as a known opacity.*

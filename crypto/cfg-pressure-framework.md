---
title: "Centrifuge (CFG): Substrate-Native RWA Token with PoS Inflation"
description: "A MrNasdog Pressure Framework read of Centrifuge (CFG): the RWA-focused Substrate-based chain's native token, ~578M total supply, validator inflation for PoS security, original ICO/team distributions long since vested. Tag B = Centrifuge Foundation."
canonical_url: "https://mrnasdog.com/research/cfg/full"
tags: ["crypto", "centrifuge", "rwa", "defi"]
published: true
---

> Originally published at **[mrnasdog.com/research/cfg/full](https://mrnasdog.com/research/cfg/full)** by MrNasdog.

This is a **MrNasdog Pressure Framework** analysis of **Centrifuge (CFG)** on Metric 1 (sell pressure) and Metric 2 (buy pressure). Narrative (Metric 3) is covered separately. The short version: CFG is the native token of the Centrifuge Chain (Polkadot ecosystem), an RWA-focused Substrate L1. Modest PoS inflation, no scheduled vesting today, Centrifuge Foundation reserves as Tag B.

## The setup

Centrifuge is the original on-chain RWA platform — tokenizes off-chain credit (invoices, real estate, treasury bills) into DeFi-usable assets. CFG is the native token of **Centrifuge Chain**, a Substrate-based parachain (Polkadot ecosystem). There's also a CFG ERC-20 wrap on Ethereum (`0xc221…d8e312`) for DeFi composability, but the native asset lives on Centrifuge Chain.

Live numbers, origin-first from Centrifuge official docs + chain RPC:

- **Total supply: ~578.4M CFG** (per CoinGecko cross-check)
- **Genesis: ~400M at launch (2021)**; current supply reflects PoS inflation since
- **Inflation: ~3%/yr nominal** (Substrate PoS rewards to nominators + collators)
- Price ~$0.29 → market cap ~$170M (FDV similar; no hard cap, just nominal inflation)
- **Centrifuge Foundation + Tinlake operators** hold reserves for grants + ecosystem
- **Real-world assets backed by CFG-secured pools**: ~$500M+ TVL in tokenized credit + treasuries

## The sell ledger

*What the design predictably puts on the market.*

| # | Source | Tag | Value |
|---|---|---|---|
| 1 | **Protocol inflation** — PoS rewards to nominators/collators | **Tag A** | **~3%/yr nominal**, ~17M CFG/yr |
| 2 | Vesting unlocks (still-locked allocations on schedule) | — | **~0** — 2021 ICO + team vests largely complete |
| 3 | Team / DAO / identified-group holdings | **Tag B** | Centrifuge Foundation + early Tinlake operators — TBD |
| 4 | Bankruptcy estate | — | **0** |

**Inflation is the headline.** Substrate-based chains typically run a 2–10% PoS inflation rate; Centrifuge's recent target is ~3%/yr. At ~578M supply that's ~17M CFG/yr added to the circulating float, paid to nominators and collators.

**Vesting is near zero.** The 2021 distribution (24% community + 14% early backers + 27% team/contributors + 27% community sale + 8% liquidity) had 1–4 year vests; the last cliffs concluded by 2025. Nothing on a hard schedule today.

**Tag B is the Centrifuge Foundation + identified ecosystem operators.** The Foundation holds reserves for grants, the original Tinlake protocol team holdings, and DAO treasury items. Discretionary. Flagged TBD pending Substrate-aware enumeration.

## The buy ledger

*What the design predictably takes off the market.*

| # | Source | Value |
|---|---|---|
| 1 | Revenue-backed buyback | **0** — no buyback contract |
| 2 | Burn mechanism | **0** structural |
| 3 | Locked allocations | — context only (CFG staked for nomination, ~7-day unbond = liquid) |
| 4 | Protocol-level demand (RWA pool fees, governance) | **Tag B small** — variable with RWA activity |

**No structural buyback or burn.** RWA pool fees on Centrifuge generate revenue, but the protocol does not route those fees back to CFG as a buyback. Protocol-level demand exists — CFG is needed for nominator selection and governance — but it's modest relative to the inflation flow.

## Net position

- **Sell, Tag A:** ~17M CFG/yr (3% inflation)
- **Buy, Tag A:** essentially 0 (no buyback, no burn, narrow protocol demand)
- **Net structural dilution:** roughly **~3%/yr** on the predictable Tag A layer

Same shape as NEAR (PoS inflation, no buyback offset) — modest scale of dilution but unfavorable structurally.

Compared to the rest of our coverage:
- **BNB / OKB / ETH**: net deflationary or flat — favorable
- **HYPE / SKY**: revenue-linked buyback — favorable
- **CFG / NEAR**: ~2.5–3%/yr inflation, no buy — unfavorable
- **TAO / SUI / ONDO**: high unfavorable

## What could flip the buy ledger

A protocol revenue routing to CFG buyback would do it — no such mechanism today. The natural buyer for CFG is RWA pool activity; if RWA TVL scales meaningfully and a protocol fee goes to a structural buy, the picture changes.

## What to watch

1. **Centrifuge Chain validator + nominator stake** — drives effective inflation distribution; check via the Centrifuge / Polkadot.js explorer.
2. **RWA pool TVL on Centrifuge** — fees + protocol demand.
3. **Centrifuge Foundation discretionary activity** — Tag B watch.
4. **Any governance proposal on fee-share or buyback** — would move the buy ledger off zero.

---

*MrNasdog Pressure Framework analysis of CFG, Metrics 1 &amp; 2. Data + explanation only. Not financial advice. Numbers as of May 2026.*

*Data note: Total supply cross-checked via CoinGecko. Inflation rate per Centrifuge official tokenomics docs; precise per-epoch reward requires querying the Centrifuge Chain via Polkadot.js or the Substrate RPC. CFG ERC-20 wrap on Ethereum is for DeFi composability; the native asset lives on Centrifuge Chain. Foundation balance + Tag B figures flagged as TBD pending Substrate-aware enumeration.*

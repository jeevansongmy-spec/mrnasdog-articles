---
title: "Sui (SUI): No Inflation, But 60% of Supply Still Unvesting"
description: "A MrNasdog Pressure Framework read of Sui Network (SUI): fixed 10B supply, no protocol inflation, but ~60% of supply is still locked in scheduled vesting through 2030. Heavy unlock pressure ahead. Origin-first from the Sui mainnet RPC."
canonical_url: "https://mrnasdog.com/research/sui/full"
tags: ["crypto", "sui", "layer1", "move"]
published: true
---

> Originally published at **[mrnasdog.com/research/sui/full](https://mrnasdog.com/research/sui/full)** by MrNasdog.

This is a **MrNasdog Pressure Framework** analysis of **Sui Network (SUI)** on Metric 1 (sell pressure) and Metric 2 (buy pressure). Narrative (Metric 3) is covered separately. The short version: SUI has no protocol inflation and a clean fixed-supply design, but **~60% of its total supply is still locked under scheduled vesting through ~2030** — the same structural shape as Ondo, just spread over a smoother glide path.

## The setup

Sui is a layer-1 proof-of-stake smart-contract platform written in Move, built by Mysten Labs and stewarded by the Sui Foundation. Mainnet launched **April 12, 2023** (genesis epoch 0 from the official RPC). Total supply is fixed at **10B SUI**, verified directly from the Sui mainnet RPC (`suix_getTotalSupply`).

Live numbers, origin-first from the Sui mainnet RPC (`fullnode.mainnet.sui.io`):

- **Total supply: 10,000,000,000 SUI** (fixed cap, verified on-chain via `suix_getTotalSupply` returning `10000000000000000000` MIST = 10B SUI)
- **Current epoch: 1137** (~24h epochs from genesis)
- **Total staked: ~7.42B SUI** (~74.2% of total — read from `suix_getLatestSuiSystemState`)
- **Active validators: 128**
- **Circulating supply (CoinGecko cross-check): ~4.005B SUI** (~40.1%)
- **Still-locked (vesting): ~5.99B SUI** (~59.9% of total)
- Price ~$1.065 → market cap ~$4.27B · FDV ~$10.65B

Initial allocation (per Sui Foundation tokenomics docs): Community Reserve, Early Contributors (Mysten Labs + team), Investors, App Testers + Burnt Finance Migration. Most non-community allocations have published vesting schedules with multi-year cliffs and linear vests stretching out toward **~2030**.

## The sell ledger

*What the design predictably puts on the market.*

| # | Source | Tag | Value |
|---|---|---|---|
| 1 | Protocol inflation | — | **0** (fixed 10B cap, no mint function) |
| 2 | **Vesting unlocks (still-locked allocations on schedule)** | **Tag A** | **~5.99B SUI scheduled to release** through ~2030 |
| 3 | **Team / DAO / identified-group holdings** — Mysten Labs + Sui Foundation already-unlocked portions | **Tag B** | TBD on-chain enumeration |
| 4 | Bankruptcy estate | — | **0** |

**Inflation: zero.** Sui's 10B cap is enforced at the protocol level. The RPC confirms `getTotalSupply()` returns exactly 10B. New SUI is never minted on a schedule.

**Vesting is THE structural sell line.** With 5.99B still locked and the vest stretching out toward ~2030, the implied **monthly release is in the range of 50–100M SUI/month** depending on cliff structure — that's a lot. (A precise breakdown requires the published Sui Foundation schedule; this article uses a midpoint estimate.) **At today's circulating ~4.0B, an additional ~5.99B coming over ~4 years means circulating supply will roughly 2.5× before the vest is complete.** Tag A because the schedule is published and trackable.

**Tag B is Mysten Labs + Sui Foundation already-unlocked portions** — coins that have vested out of #2 but haven't moved into broad circulation. Plus discretionary Foundation deployments. De-duped against #2 (anything still on the published vest schedule belongs to #2, not #3).

**Bankruptcy estate: zero.**

## The buy ledger

*What the design predictably takes off the market.*

| # | Source | Value |
|---|---|---|
| 1 | Revenue-backed buyback | **0** — no protocol buyback contract |
| 2 | Burn mechanism | **0** structural — storage fund operates as rebates, not burns |
| 3 | Locked allocations | — context only (~7.42B staked is functionally liquid; ~1 epoch = 24h unstake) |
| 4 | Protocol-level demand (gas) | **Tag A** — real but modest at current activity |

Sui has no structural buyback or burn. The much-discussed **storage fund** is a deflationary-adjacent mechanism, but functionally it's a rebate system for past storage costs, not a burn. Gas demand exists (every Sui transaction requires SUI for gas), but the reference gas price is low (100 MIST = 1e-7 SUI) and on-chain volume produces modest daily demand.

## Net position

- **Sell, Tag A:** ~1.5B+ SUI/year (rough estimate of 5.99B vest over 4 years)
- **Buy, Tag A:** minimal (gas demand only)
- **Net structural dilution to circulating supply: substantial** — circulating will roughly double in the next 24 months under the published vest schedule.

**This is the same structural shape as Ondo and TAO: scheduled supply up, structural buy minimal.** Different mechanics (vesting cliffs vs. cliff days vs. block emission), same direction.

Compared to the rest of our coverage:

- **BNB**: supply ↓ from burns → favorable
- **HYPE**: AF buyback > vest → favorable
- **UNI / SKY**: clean today, lever-dependent → neutral / mixed
- **NEAR**: ~2.5%/yr inflation → unfavorable
- **TAO**: ~27%/yr inflation, halving 10mo → unfavorable now, programmed improvement
- **SUI**: ~38% supply unvesting over 4 years (~9%/yr of total) → **unfavorable**
- **ONDO**: ~17%/yr cliffs → most unfavorable

## What flips the buy ledger

A revenue-funded buyback would need governance to introduce one — none on the roadmap publicly. The natural buyer for SUI is application demand on the chain; if a flagship Sui app (e.g., a stablecoin issuer, a large DeFi protocol, a viral consumer app) generates significant fee volume and the protocol routes some fees to a buyback, the picture changes. **No such mechanism exists today.**

## What to watch

1. **Sui Foundation tokenomics page** — monthly unlock disclosures; track cliff dates.
2. **Mysten Labs + Sui Foundation wallet activity** — large transfers visible on SuiVision / SuiScan.
3. **Storage fund balance over time** — read via RPC; tracks deflationary-adjacent mechanics.
4. **On-chain gas burn (if any reform is introduced)** — would move source #2 of the buy ledger from 0 to non-zero.

---

*MrNasdog Pressure Framework analysis of SUI, Metrics 1 &amp; 2. Data + explanation only. Not financial advice. Numbers as of May 2026.*

*Data note: Total supply (10B) read directly from the Sui mainnet RPC via `suix_getTotalSupply` on `0x2::sui::SUI`. Current epoch + total staked + validator count from `suix_getLatestSuiSystemState`. Genesis date inferred from epoch math (1137 epochs × 24h from epoch start) → ~April 12, 2023. Circulating supply cross-checked via CoinGecko. Vesting schedule details from the Sui Foundation tokenomics page; precise per-month unlock pace requires the published cliff schedule.*

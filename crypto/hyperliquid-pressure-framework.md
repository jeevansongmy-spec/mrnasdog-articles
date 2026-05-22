---
title: "Hyperliquid (HYPE): The Buyback Is Bigger Than the Unlock"
description: "A MrNasdog Pressure Framework read of Hyperliquid's HYPE — the Assistance Fund buys back ~2.95M HYPE per 90 days against ~1.0M of unlock selling, a ~2.95× buy-to-sell ratio. Every number is pulled from Hyperliquid's own API."
canonical_url: "https://mrnasdog.com/research/hype"
tags: ["crypto", "hyperliquid", "defi", "hype"]
published: true
---

> Originally published at **[mrnasdog.com/research/hype](https://mrnasdog.com/research/hype)** by MrNasdog.

This is a **MrNasdog Pressure Framework** analysis of **Hyperliquid (HYPE)** on Metric 1 (sell pressure) and Metric 2 (buy pressure). Narrative (Metric 3) is covered separately. Every number is pulled from Hyperliquid's own API. The short version: the protocol buys back more of its own token than its insiders unlock.

## The setup

HYPE has a **fixed maximum supply of 1 billion** tokens. Of that, ~298.7M is circulating, ~241.4M sits in a locked team/contributor vault, ~44.44M has been absorbed by the Assistance Fund, and ~414.7M is reserved for future emissions. Price is around $58. Three features make HYPE unusually clean to score: no protocol inflation, an on-chain Assistance Fund that buys HYPE with 99% of trading fees, and a discretionary — but stable — contributor unlock.

## Metric 1 — Sell pressure

Sell pressure measures the predictable selling baked into the design. Walking the six sources for HYPE:

**1. Protocol inflation — zero.** HYPE's supply is fixed; nothing is minted on a schedule. This source contributes nothing, and that's verifiable from the supply figures.

**2. Vesting unlocks — Tag A, ~1.0M / 90 days.** The locked vault holds 241.4M HYPE. On paper the contributor allocation authorizes up to ~9.92M/month, but Hyperliquid distributes at **discretion** and has consistently released far less — roughly ~330K/month. Because that smaller figure repeats month after month, it's a **stable pattern**, so we treat it as trackable and predictable (Tag A) and project the recent rate forward: ~1.0M over 90 days. The authorized ceiling is not the number; the actual on-chain release is.

**3. Treasury releases — Tag B, ~60.2M.** The Hyper Foundation treasury sits at the identified address `0xd57e…` and holds ~60.2M HYPE — verified directly from the official API (~60.1M staked + 0.1M spot). We can read it, but its deployment timing is discretionary, so it's Tag B: trackable, unpredictable. It doesn't enter the bars, but it's a real, watchable overhang.

**4. Locked stake unlocks — skipped.** HYPE's unstaking cooldown is 7 days — under the 90-day threshold, so it's short-term noise the framework deliberately ignores.

**5. Bankruptcy estate — zero.** HYPE launched in late 2024; there is no FTX-style estate distributing tokens.

**6. Large concentrated holdings — Tag C, ~238M.** With the Foundation now separated out as Tag B, the remaining float (~238M, which is also what aggregators report as "circulating") is spread across ~237,000 wallets, most unidentified. We can see balances but not owners or intentions, so it's untrackable for sell-timing.

**Metric 1, Tag A total: ~1.0M HYPE of predictable sell pressure over 90 days** — entirely the contributor vault release.

## Metric 2 — Buy pressure

Buy pressure measures the predictable buying baked into the design. HYPE's is unusually strong and unusually clean.

**1. Revenue-backed buyback — Tag A, ~2.95M / 90 days.** Hyperliquid's Assistance Fund receives **99% of all trading fees** in USDC and uses them to buy HYPE on the open market, sending the tokens to an address with no private key — effectively a burn (ratified by a December 2025 validator vote). This is the cleanest Tag A in crypto: a public address, a fixed rule, fully on-chain. Reading its buy fills directly, the fund is buying **~32,723 HYPE per day** — about 2.95M over 90 days — and it now holds ~44.44M HYPE.

**2. Burn mechanisms — Tag A, negligible.** Explicit burns to dead addresses total only ~1,676 HYPE. The real "burn" for HYPE is the Assistance Fund itself.

**3. Locked allocations — context.** ~432.0M HYPE is staked. Staking locks supply rather than buying it, so it doesn't enter the buy bar — but it does mean a large share of supply is illiquid.

**4. Protocol-level demand (gas) — small.** HYPE is the gas token; usage-driven demand is real but minor next to the buyback, and is largely captured in the burn figure.

**Metric 2, Tag A total: ~2.95M HYPE of predictable buy pressure over 90 days** — almost entirely the Assistance Fund.

## The read

On the predictable (Tag A) layer, HYPE takes in **~2.95M HYPE of buying** against **~1.0M of unlock selling** every 90 days — a **2.95× buy-to-sell ratio**, net +1.95M HYPE. The structural consequence is visible in the supply itself: circulating is roughly flat-to-shrinking even as the vault unlocks, because the Assistance Fund removes more than the vault releases. In framework terms, HYPE's structural conditions on the supply side are **favorable** — the protocol is a bigger buyer of its own token than its insiders are sellers.

## Data & confidence

Source: the Hyperliquid info API (`api.hyperliquid.xyz`) — origin-first. **High confidence:** buyback rate (on-chain buy fills), supply, Assistance-Fund and vault balances (read directly). **Medium:** the ~330K/month vesting release (discretionary, but a stable pattern). **Reconstructed:** the 90-days-ago balances — the chain stores only current state, so a daily snapshot is now recording exact history going forward.

## Limitations

Discretionary distribution can change — the foundation could release more or less than its recent pattern. The buyback scales with trading fees, so a volume collapse would shrink it; the projection assumes status quo. And the untrackable float (~298.7M, Tag C) plus any unidentified foundation treasury sit outside the headline number by design — not because they don't matter, but because we won't put a number on what we can't verify.

---

*MrNasdog Pressure Framework analysis of HYPE, Metrics 1 & 2. Data + explanation only. Not financial advice. Numbers as of May 2026. By MrNasdog (Zhiyi Song).*

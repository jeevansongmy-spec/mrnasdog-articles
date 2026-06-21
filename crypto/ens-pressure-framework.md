---
title:         "ENS Inflation Analysis · June 2026 · Supply Roughly Steady"
description:   "Fixed 100M supply, vesting completed Nov 2025, no buyback or burn. Framework reads 0.00% net; monitor +5.33% is expired-vesting reclassification, not new ENS."
canonical_url: "https://mrnasdog.com/research/ens/inflation"
tags:          ["crypto", "ens", "ethereum", "governance"]
published:     true
---

*Originally published at [mrnasdog.com/research/ens/inflation](https://mrnasdog.com/research/ens/inflation)*

Ethereum Name Service has a **fixed 100M ENS supply**, its 4-year vesting schedule completed in November 2025, and it runs no buyback and no burn. The Pressure Framework reads **0.00% net** to market over the next 90 days. The inflation monitor reads **+5.33%** over the trailing window — a 5.33pp gap that is the tail of expired vesting, not new ENS, so a monitor-gap flag ships with the primary kept.

## The verdict, in one paragraph

For the 90-day window beginning June 21 2026, the framework reads **ENS at 0.00% net inflation**: no sell-side mechanism is firing and no buy-side mechanism is removing supply. The inflation monitor reads **+5.33%** over the trailing 90 days, a **5.33pp gap** that triggers a monitor-gap flag. That gap is not new ENS — on-chain totalSupply held at 100,000,000 throughout, and the monitor's circulating denominator simply caught up as the final linear-vesting tranche unlocked into already-allocated buckets. The honest label for ENS in mid-2026 is a **structurally quiet, fully-vested governance token** whose only live supply question is a large but dormant DAO treasury.

## Sell pressure: where new ENS comes from

The short answer for ENS is: nowhere, right now. **Sell #1 protocol inflation is zero** — the ENS ERC-20 has a fixed 100M supply, and the on-chain totalSupply() call returns 100,000,000 exactly. The ENS DAO holds the right to mint up to 2% of supply per year, but that power has never been exercised and is gated behind a governance vote plus a 365-day minimum interval; no mint is scheduled in the window, so it scores 0 with the capacity noted as an overhang.

**Sell #2 vesting unlocks is zero** because the schedule has physically expired. The 4-year linear vesting that began on November 8 2021 — covering both the DAO community treasury and the core-contributor allocation — reached completion in November 2025. There is no remaining cliff to fire. **Sell #3 foundation and unscheduled unlocks is zero** on flow, though it carries the one real overhang ENS has (covered below). **Sell #4 long-term locked or bankruptcy is zero** — there is no bankruptcy estate holding ENS.

## Buy pressure: where new ENS goes

ENS has no active buy-side mechanism, so all four rows are zero. **Buy #1 programmatic buyback is zero** — ENS runs no repurchase programme; the protocol's revenue, earned from .eth registration and renewal fees, is collected in ETH and flows to the DAO treasury and the endowment, never into open-market ENS buys. **Buy #2 protocol fee burn is zero** — there is no EIP-1559-style ENS burn, and no mechanism that destroys ENS supply. **Buy #3 foundation buy is zero** — neither the ENS Foundation nor the DAO accumulates ENS from the market. **Buy #4 new long-term lock is zero** — no staking or lock-up programme for ENS has been announced.

## Foundation and overhang

The one live supply question for ENS is the **DAO treasury overhang**. Of the original 50M ENS allocated to the community treasury, the bulk remains DAO-controlled, with roughly **9.70M ENS** sitting directly in the on-chain governance timelock as of June 21 2026. This is a large balance relative to the ~40.41M circulating, so it is enumerated and watched. Crucially, it is dormant: the ENS DAO funds its operations by selling ETH earned from registration revenue, not by selling ENS, and the endowment manager explicitly holds only ETH and USDC — never the native token. Because no ENS sale from the treasury has been observed, the framework scores this overhang at 0 flow. The trigger is mechanical: if the DAO timelock or treasury ENS balance falls between refreshes, that outflow enters Sell #3 at the next refresh.

## How ENS compares to other fixed-cap governance tokens

ENS belongs to the class of **fixed-cap, fully-vested governance tokens with a treasury-heavy float** — its closest structural analogues are tokens like UNI and, before its buyback era, AAVE. Like UNI, ENS has a hard 100M cap and a DAO that holds an enormous share of supply; unlike post-UNIfication UNI or Aavenomics-era AAVE, ENS routes none of its protocol revenue into ENS burns or buybacks, so it has no deflationary counter-pressure. That makes ENS structurally flatter than buyback tokens — neither inflating nor shrinking.

The distinction that matters against continuous-emission L1s (uncapped chains that mint validator rewards every block) is that ENS cannot dilute holders through issuance: the only path to new ENS is the discretionary 2% governance mint, which has never been used. Against a chain like Solana or a staking-reward token, ENS looks far more supply-disciplined on paper — but it trades that discipline for a concentration risk, since the DAO treasury could in principle distribute or sell ENS if governance ever chose to. The framework reads what is happening, not what could: today, ENS is quiet.

## What to watch in the next 90 days

First, any ENS DAO governance proposal that **distributes, sells, or mints ENS** — the 2% annual mint or a treasury diversification vote would move the reading immediately. Second, the **DAO timelock ENS balance** (~9.70M today); a drop signals a treasury outflow that enters Sell #3. Third, the recurring ENS DAO community update and newsletter for any endowment policy change that touches ENS rather than ETH. Fourth, any first-ever activation of a **buyback or burn** — none is on the table as of June 21 2026, but it would flip the buy side from zero. None of these has a fixed date; they are governance-driven watch lines, not scheduled cliffs.

## Summary

ENS is a fixed-100M, ~40%-circulating governance token whose 4-year vesting completed in November 2025 and which runs no buyback and no burn, leaving the framework at 0.00% net to market. The inflation monitor's +5.33% is the tail of that expired vesting reclassifying already-minted ENS into the circulating count, not new issuance — hence the flag with the primary kept. The structural risk is the large dormant DAO treasury, which has never sold ENS; the structural ceiling is the 100M hard cap plus the unused 2% annual mint. For a governance token, ENS is about as supply-quiet as the framework reads.

---

*MrNasdog Pressure Framework analysis of Ethereum Name Service (ENS), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 21, 2026.*

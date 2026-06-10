---
title: "Sky (SKY) Inflation Analysis: USDS Holder Rewards Run Against the Smart Burn Engine"
description: "A MrNasdog Pressure Framework read of Sky (SKY): USDS holder rewards distribute ~150M SKY / 90D. Smart Burn Engine offset documented but unbooked this read. Framework reads +0.64%, aggregator +0.95%."
canonical_url: "https://mrnasdog.com/research/sky/inflation"
tags: ["crypto", "sky", "stablecoin", "defi"]
published: true
---

> Originally published at **[mrnasdog.com/research/sky/inflation](https://mrnasdog.com/research/sky/inflation)** by MrNasdog.

Sky distributes roughly 150M SKY every 90 days to USDS stablecoin holders as protocol-revenue rewards. The Smart Burn Engine deploys USDS daily to buy and burn SKY, but the in-window burn quantum is not enumerated in this read. Framework reading: **+0.64% net** on a 23.46B effective cap.

## The verdict, in one paragraph

For the 90-day window ending June 10 2026, the framework reads **SKY at +0.64% net inflation** — USDS holder rewards distribution as the sole booked flow, with the Smart Burn Engine offset left unbooked pending an on-chain wallet read. The aggregator monitor reads **+0.95%**, a 0.31-percentage-point gap inside the framework's tolerance. The two readings agree on direction. Sky in mid-2026 is a revenue-driven protocol where the buyback engine and the rewards stream operate on similar magnitudes — both flows are real, but only the rewards stream is enumerated in this conservative read.

## Sell pressure: where new SKY comes from

Sky inherits the Maker governance model with a 23.46B effective cap derived from the 1 MKR : 24,000 SKY migration. Roughly 99% of original MKR has converted to SKY since the August 2024 rebrand; the remaining MKR holders face a 1% per quarter conversion penalty since September 2025 (June 2026 penalty: 3%). The total supply is effectively at the cap.

The active sell flow is the **USDS holder rewards stream** — Sky distributes 600M SKY annually to USDS stablecoin holders as a share of protocol revenue. Over 90 days, that comes to roughly **150M SKY** entering circulation as new minted supply via the DssVestMintable contract. This is Sell #1 in the framework's ledger.

A separate stream — the SKY staking rewards normalised to 838.18M / 180 days under the February 26 2026 executive spell — runs parallel and is a different cohort of stakers receiving SKY. For this conservative read, the framework books only the USDS holder distribution; the staking rewards stream contributes additional minted supply but isn't separately enumerated. Sell #2 (vesting unlocks) is zero — Maker had no traditional team vesting at launch and Sky inherits no scheduled cliff schedule. Sell #3 (Foundation discretion) is zero with the standard SubDAO-multisig opacity caveat — the Sky Foundation and SubDAO custody addresses are not publicly enumerated, so this is a watching item rather than a quantified row. Sell #4 (bankruptcy estate) is zero.

## Buy pressure: the Smart Burn Engine

The **Smart Burn Engine (SBE)** launched in February 2025 and is the structural mechanism on the buy side. The SBE deploys USDS from protocol surplus revenue daily to buy SKY on the open market and burn the purchased tokens. Pre-March 14 2026, the deploy rate ran roughly 300,000 USDS per day; an executive vote ratified on March 14 2026 cut the rate to 37,600 USDS per day for approximately three months to build the Aggregate Backstop Capital toward a $150M target. At roughly $0.07 per SKY, the post-cut rate translates to about 537K SKY burned per day, or roughly 1.5-2B SKY over 90 days when fully enumerated.

This read does not book the SBE flow as Buy #1, however. The framework's anti-fabrication rule requires fresh on-chain enumeration of the SBE wallet outflow within the current window before booking the buyback row, and that on-chain read was not completed this session. Booking the burn at the documented rate without the on-chain confirmation would risk fabricating a number from the protocol's published intent rather than verified reality. The prior refresh (May 30 2026) did book Buy #1 at ~85M SKY for the window, splitting between the pre- and post-cut rate; future refreshes should restore this row.

Buy #2 (protocol fee burn) is zero — SBE is buyback-then-hold, not a transfer-fee burn. Buy #3 (Foundation buy) is zero — SBE is the structural mechanism. Buy #4 (new long-term lock) is zero — the LockStake staking engine unbond is operational, not a long-term lock under the framework's definition.

## Foundation and overhang

Sky Foundation and the SubDAO multisigs (Spark and others) collectively manage protocol parameters and treasury operations, but the per-multisig address registry is not publicly disclosed. The framework treats this as Sell #3 watching opacity with value zero — the same structural shape as BNB and OKB corporate treasury opacity. The largest visible overhang is structural rather than custodial: the 19% of original MKR still unconverted to SKY represents about 11.5M SKY of potential migration inflow at the 1:24,000 ratio, which is immaterial against the 23.27B circulating base.

## How SKY compares to other stablecoin-issuance governance tokens

Among stablecoin-issuance governance tokens, Sky's revenue-first design is the most aggressive at recycling protocol revenue into token-side flows. Maker (legacy MKR) ran a simpler model where stability-fee revenue funded the Surplus Buffer and triggered token buybacks; Sky's structure separates the USDS holder rewards stream from the SBE buyback, with both flows running concurrently. Frax (FXS, now veFXS) runs a similar duality but at lower scale. Compound (COMP) and Aave (AAVE) do not redistribute protocol revenue to token holders structurally; their governance tokens accrue value via fee-switch decisions made via governance.

Sky's framework reading should normalise around neutral once both flows are fully enumerated. The +0.64% reading in this report reflects the conservative under-booking of the SBE burn; the true net reading with SBE booked would land closer to flat or slightly deflationary at current burn pace.

## What to watch in the next 90 days

Three things move the framework reading. First, the **Aggregate Backstop Capital target** — once the $150M backstop target is reached, the SBE deploy rate is expected to scale back up toward the pre-March-14 rate of 300,000 USDS per day, which would materially increase Buy #1 and pull the net reading downward. Second, **USDS supply growth** — the holder rewards stream scales with USDS circulation; meaningful USDS growth means more rewards distribution and therefore higher Sell #1. Third, **governance changes** to the rewards stream rate — the February 26 2026 executive spell normalised it; another spell could adjust it again.

## Summary

SKY is a stablecoin-issuance governance token with two large recurring flows: 600M SKY/year to USDS holders as protocol-revenue rewards, and a revenue-funded buy-and-burn via the Smart Burn Engine. The framework reads +0.64% net for the trailing 90 days, booking only the rewards distribution; the aggregator monitor agrees within tolerance at +0.95%. The SBE burn is real and structurally important but is left unbooked in this read pending a fresh on-chain wallet enumeration. Future refreshes should restore the buyback row and likely flip the net reading toward neutral or mildly deflationary.

---

*MrNasdog Pressure Framework analysis of Sky (SKY), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 10, 2026.*

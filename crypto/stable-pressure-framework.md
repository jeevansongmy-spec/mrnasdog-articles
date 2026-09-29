---
title:         "STABLE Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description:   "STABLE supply is flat: 0.00% net over 90 days and next. All 100B were made at launch, fees are paid in USDT, and the 82B locked STABLE wait until Dec 8 2027."
canonical_url: "https://mrnasdog.com/research/stable/inflation"
tags:          ["crypto", "stable", "layer1", "tokenomics"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/stable/inflation](https://mrnasdog.com/research/stable/inflation)*

# STABLE Inflation Analysis · September 2026 · Mixed flows · supply roughly steady

STABLE supply did not grow in the last 90 days and is not set to grow in the next 90: the MrNasdog Pressure Framework books **0 STABLE** of sell pressure and **0 STABLE** of buy pressure, a net of **0.00%** against **26.75B** circulating STABLE. All **100B** STABLE were created when the Stable mainnet launched on **Dec 8 2025**, and the **82B** still locked cannot start to leave the lock before **Dec 8 2027** under the Universal Lock that Stable published on **Aug 14 2026**.

## The verdict, in one paragraph

The framework reads STABLE at **0.00%** net over the last 90 days and **0.00%** for the next 90 days. The inflation monitor reads **+11.07%** over the same window, a gap of **11.07 percentage points**, far above the 0.5-point line, so the page carries a ⚠ monitor gap chip. The gap has a clear cause: the supply figure the monitor reads kept adding about **889M STABLE** a month on the old release plan, rising from **24.05B** to **26.71B**, while on the Stable chain the team, investor, Foundation and staked validator wallets did not send out a single STABLE. The explanation does not remove the gap, so the chip stays. STABLE today is a fixed-supply token with a large locked overhang and a release calendar that was pushed back by a year.

## Sell pressure: where new STABLE comes from

Protocol inflation (Sell #1) is **0**. Stable issued the whole STABLE supply of **100,000,000,000** in one event at launch, and the total supply read on the Stable chain today is still exactly 100B. Stable validators and their stakers are paid out of gas fees, and gas on Stable is paid in USDT, so staking does not mint new STABLE; the chain's reward pool holds about half of one STABLE. The Stable whitepaper says no further issuance is possible, and the Stable docs say minting the governance token is blocked.

Vesting unlocks (Sell #2) are **0**. The team allocation of **25B STABLE** and the investors and advisors allocation of **25B STABLE** each sit in a single wallet that received its coins in Dec 2025 and has never sent any out. Under the original STABLE tokenomics both allocations had a one-year cliff, so the first team and investor unlock would have landed on **Dec 8 2026**, inside the next 90-day window. The Stable whitepaper version 2.0 replaced those terms with the Universal Lock: one release calendar for all **82B** locked STABLE, with the first floor of **4.1B** starting on **Dec 8 2027** and dripping out over 180 days.

Foundation and unscheduled unlocks (Sell #3) are **0**. Unlock trackers still show the ecosystem allocation releasing about **889M STABLE** a month, but the Foundation's locked wallet has held exactly **21B STABLE** since Dec 2025, and the validator allocation of **11B STABLE** has stayed staked the whole time. Under the Universal Lock, any Foundation tokens counted as unlocked since launch are locked again from **Oct 5 2026**. Long-term locked or bankruptcy supply (Sell #4) is **0**: Stable has no estate, trustee or court schedule releasing STABLE.

## Buy pressure: where new STABLE goes

Programmatic buyback (Buy #1) is **0**. Stable collects its gas fees in USDT into a treasury that validators may share with stakers; whether any of that money will ever be used for STABLE is still undecided, and no buyback has been announced. Protocol fee burn (Buy #2) is **0**: because gas is paid in USDT, using the Stable chain burns no STABLE, and total supply sits at the same 100B it had on launch day.

Foundation buy (Buy #3) is **0**, since no announcement or wallet flow shows the Stable Foundation buying STABLE on the market. New long-term lock (Buy #4) is **0**. About **11.0B STABLE** is staked, nearly all of it the validator allocation delegated in Dec 2025, and it did not grow in the window. The Oct 5 2026 relock looks like a lock on paper, but the coins it covers never left the locked wallets, so it takes nothing off the market.

## Foundation and overhang

The STABLE overhang is large and well defined. Four locked balances hold **82.0B STABLE**: the team wallet at **25B**, the investor wallet at **25B**, the Foundation's locked wallet at **21B** and the staking pool at **11.0B**. On-chain, that leaves about **18.0B STABLE** outside the locks, which matches the 18% the whitepaper says was in circulation from day one. The Foundation's day-one wallet holds **7.54B STABLE**, down from 8.0B after 460M went out in Dec 2025, and it has not moved since; those coins already count as circulating, so spending them would add nothing new.

The one sign of stress in the numbers is the denominator: the circulating count of **26.75B** is about **8.75B** higher than the coins that sit outside the locks, because it follows the old monthly release plan. Every one of these balances is re-read at each rebuild. If any locked wallet's balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How STABLE compares to other stablecoin-payment Layer 1s

STABLE belongs to a new class of Layer 1 chains built for stablecoin payments, where the coin people send is a dollar token and the native token sits in the background for staking and voting. Plasma, which launched in September 2025, pays for USDT transfers with a paymaster but still uses its own XPL token for ordinary gas and for staking. Stable goes further: gas itself is paid in USDT, and validators are paid from those fees, so STABLE has no issuance at all. In supply terms that puts STABLE closer to a fixed-cap token than to the uncapped proof-of-stake chains that inflate every block.

The trade-off is value flow. On chains like Ethereum or BNB Chain, users pay gas in the native coin and part of it is burned, so heavy use shrinks supply. On Stable, heavy use earns USDT for validators and stakers but burns no STABLE. For STABLE, the only supply lever left is the lock: **82%** of all STABLE is still locked, which is a much larger share than most launched Layer 1 tokens carry in their second year. The Universal Lock also adds a price test that most vesting plans lack: a release floor is delayed three months if the 30-day average price is under **$0.025** the day before it starts, up to nine months, with a hard end on Dec 8 2029.

## What to watch in the next 90 days

First, the Universal Lock Effective Date on **Oct 5 2026**, when Foundation tokens counted as unlocked since launch are formally locked again; watch whether the circulating count falls back toward **18B**, which would shrink the denominator but move no coin. Second, **Oct 8 2026**, the date unlock trackers still list for the next monthly release of about **889M STABLE**; under the new whitepaper it should not happen, and any coins leaving the Foundation's locked wallet would be booked. Third, **Dec 8 2026**, the old team and investor cliff date, which no longer releases anything; the team and investor wallets should still read 25B each after it. Fourth, the fee switch: any Stable governance decision to route USDT fees to STABLE stakers or to a buyback would add a buyer. Fifth, the Foundation's day-one wallet of 7.54B, which funds exchange campaigns and partner rewards from coins already in circulation.

## Summary

STABLE, the staking and governance token of the Stable Layer 1, has a fixed supply of 100B that has not changed since launch on Dec 8 2025, and the MrNasdog Pressure Framework reads its net supply change at **0.00%** for both the last and the next 90 days. Gas on Stable is paid in USDT, so there is no STABLE issuance, no burn and no buyback. The key risk is the locked overhang of **82B STABLE**, 82% of all supply, which the Universal Lock now holds back until **Dec 8 2027** and then releases in seven floors through Dec 8 2029. The monitor reads **+11.07%** because its supply figure follows the old monthly release plan, not the wallets, so the gap stays flagged.

*MrNasdog Pressure Framework analysis of STABLE, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

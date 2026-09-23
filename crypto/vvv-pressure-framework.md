---
title:         "VVV Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "VVV supply is growing: +3.19% over 90 days as staking emissions and team vesting outrun Venice's revenue buy-and-burn. Full Pressure Framework ledger."
canonical_url: "https://mrnasdog.com/research/vvv/inflation"
tags:          ["crypto", "vvv", "venice", "ai"]
published:     true
---

Originally published at [VVV Inflation Analysis · September 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/vvv/inflation).

# VVV Inflation Analysis · September 2026 · Supply growing · projected to keep growing

VVV supply is growing and is projected to keep growing. The MrNasdog Pressure Framework reads Venice Token at **+3.19%** over the trailing 90 days and **+3.29%** over the next 90, because new staking emissions and team vesting streams add more VVV than revenue buybacks burn. Sell pressure is **2.02M VVV**, buy pressure is **0.49M VVV**, and the inflation monitor reads **+2.29%**. VVV has no supply cap: Venice has cut the staking emission from 14M a year at launch to 2.5M today and 2M from Oct 1 2026, but the rate is a company setting, not a hard limit.

## The verdict, in one paragraph

Against a circulating base of **48.12M VVV**, the framework books **2.02M VVV** of sell pressure and **0.49M VVV** of buy pressure over the 90 days to Sep 23 2026 — a net of **+3.19%** — and projects **+3.29%** for the next 90 days. The inflation monitor reads **+2.29%** for the same window, a gap of **0.89 percentage points**, which is over the framework's 0.5-point tolerance and ships with a monitor-gap warning on the overview. The gap is explained: the monitor's supply count sat about **0.36M VVV** above the chain until a one-time recount on Aug 17 2026, which alone accounts for **0.77 points**. The label for VVV is **an uncapped staking token whose falling emission is still outrun by vesting**: every cut to the Venice emission helps, but the VVV float keeps growing faster than the Venice buy-and-burn removes it.

## Sell pressure: where new VVV comes from

Sell #1, protocol inflation, is **0.690M VVV**. The VVV contract on Base has exactly one supply function — a mint that only the Venice staking contract can call — and that contract mints new VVV every second to pay stakers. Total VVV in existence rose by **0.728M** across the window. About 5% of every emission goes to the Venice company treasury, which sits outside the float, so **0.690M VVV** reached stakers. The staking emission was cut twice inside the window, and both cuts were read directly off the contract: **4M a year** until Jul 1 2026, **3M** until Sep 1 2026 and **2.5M** since. Venice has announced a further cut to **2M a year on Oct 1 2026**, which is why Sell #1 falls to about **0.478M VVV** in the next 90 days.

Sell #2, vesting unlocks, is the largest row at **1.250M VVV**. Venice team and contributor grants sit in two on-chain vesting contracts and drip out every second across 17 live streams; holders withdrew **1.250M VVV** in the window, and each contract's withdrawals match its balance change exactly. The main team streams finish on Jan 27 2027, a few newer contributor grants run into 2028, about **1.19M VVV** more unlocks in the next 90 days, and **1.89M VVV** is still waiting on live streams. The Series A token grant announced on Jul 1 2026 is locked for one year, so it adds nothing before Jul 2027.

Sell #3, Foundation and unscheduled unlocks, is **0.080M VVV**. The main Venice treasury sends one batch near each month end to an operating wallet that counts as circulating — on Jun 30, Aug 2 and Aug 31 2026 — and the framework carries three more batches forward. A same-day staking round trip out of the treasury went out and came back, so it adds nothing. Sell #4, long-term locked or bankruptcy, is **0**: VVV has no bankruptcy estate, no trustee and no court-ordered distribution.

## Buy pressure: where new VVV goes

Buy #1, programmatic buyback, is **0.127M VVV**, and every unit of it was destroyed. Venice spends part of its revenue buying VVV on the open market. Each subscription — and since Jul 17 2026, each purchase of API credits — buys VVV and sends it straight from the swap to the zero address: **0.060M VVV** across more than 255,000 small burns, running about three times faster once credit burns began. A second Venice wallet buys through the day and burns once a month: **0.023M** on Jul 9, **0.027M** on Aug 7 and **0.017M** on Sep 8 2026. Because the VVV contract has no burn function, its total supply can only rise; the zero-address balance is the real burn record, and it rose by exactly the amount the burn transfers add up to.

Buy #2, protocol fee burn, is **0** — gas on Base is paid in ETH and nothing in the token burns fees. Buy #3, Foundation buy, is **0**: there is no programme that buys VVV and holds it in a company wallet. Buy #4, new long-term lock, is **0** even though staking grew by **1.84M VVV** and DIEM minting locks staked VVV further, because staked VVV already counts as circulating. Buy #5, treasury absorption, is **0.360M VVV**: coins that moved from the market side back into Venice wallets outside the float, led by **0.200M** of Venice's own staked VVV returned to a company wallet on Jul 28 2026. Only its recurring fee-and-swap part, about **0.044M**, is carried forward.

## Foundation and overhang

The Venice overhang is large and fully named. Five company-controlled addresses hold everything counted outside the float, and together they rebuild the circulating figure to within 432 VVV. The main Venice treasury holds **20.77M VVV** and also receives about 5% of every emission. A second company wallet holds **8.63M VVV**, a liquidity wallet that runs Venice's pool positions holds **1.57M VVV**, and the two vesting contracts hold **1.94M VVV**. Venice founder Erik Voorhees has said the company owns more than 30M VVV and chose to raise equity rather than sell treasury tokens.

None of the company wallets has a published release calendar, so their balances are read from the chain at every rebuild. If the treasury, the second wallet or the liquidity wallet falls between refreshes by more than the monthly batch already counted, that outflow enters Sell #3 at the next refresh. The monthly burn wallet is tracked the same way: it holds a working balance between burns, and if that balance ever leaves for anywhere other than the zero address, it enters the sell side instead.

## How VVV compares to other staking-emission tokens

VVV belongs to the uncapped staking-emission class, the same broad shape as proof-of-stake layer-1 tokens that pay validators in new coins. The difference is who sets the rate. On a typical staking chain the emission follows a protocol curve tied to how much is staked. On VVV it is a single number the Venice company writes into the staking contract, and Venice has only ever moved it down — from 14M a year at launch to 2M from Oct 1 2026. That is a stronger downward track record than most staking chains, and a weaker guarantee than a hard cap like Bitcoin's, because the same setting could move back up.

On the buy side, VVV sits closer to revenue-buyback tokens than to fee-burn chains. Where a fee-burn chain destroys part of every transaction fee in protocol code, the Venice buy-and-burn is funded from app revenue — subscriptions and API credits — and executed by the company on the open market. It scales with Venice's business rather than with on-chain activity, and it is real: the burn record matches the burn transfers to the last decimal. At today's rate it removes roughly one VVV for every fifteen that emissions and vesting add.

The last comparison is to freshly launched tokens working through a team vest. For VVV, vesting — not emission — is now the biggest source of new float, and it ends in early 2027. Once the main team streams finish on Jan 27 2027, the Venice sell side shrinks to the staking emission and treasury batches. The gap narrows sharply, though burns at today's pace would still cover only about a quarter of what is left. That is the path to the net deflation Venice says it is aiming for, and it still needs bigger burns or smaller emissions.

## What to watch in the next 90 days

First, the Oct 1 2026 emission cut to 2M VVV a year — confirm the staking contract rate actually steps down. Second, the monthly Venice buyback burns, expected around Oct 8, Nov 7 and Dec 8 2026, and whether the per-subscription and per-credit burns keep their post-Jul 17 pace as the VVV price moves. Third, the team vesting streams, which keep releasing about 1.19M VVV a quarter until Jan 27 2027. Fourth, the month-end treasury batches around Sep 30, Oct 31 and Nov 30 2026, and any larger move out of the **20.77M VVV** main treasury. Fifth, any new Venice tokenomics update that changes the emission, the burn share of revenue or the DIEM supply target.

## Summary

The MrNasdog Pressure Framework reads VVV at **+3.19%** over the trailing 90 days and **+3.29%** projected forward: supply growing, projected to keep growing. The structural driver is team vesting of **1.250M VVV** a quarter plus a staking emission of **0.690M**, against a revenue buy-and-burn of **0.127M** and **0.360M** absorbed back into Venice wallets. The key risk is that VVV has no cap and **30.97M VVV** sits in company wallets with no release schedule. The comfort is direction: Venice keeps cutting the emission, and the largest sell row runs out in January 2027.

MrNasdog Pressure Framework analysis of VVV, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 23 2026.

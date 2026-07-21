---
title:         "GRASS Inflation Analysis · July 2026 · Supply growing · projected to keep growing"
description:   "Grass mints nothing — its whole 1B supply was created at launch. Yet ~51.4M GRASS left its locks in 90 days against zero buyback or burn. Framework reads +8.13% net."
canonical_url: "https://mrnasdog.com/research/grass/inflation"
tags:          ["crypto", "grass", "solana", "depin"]
published:     true
---

*Originally published at [mrnasdog.com/research/grass/inflation](https://mrnasdog.com/research/grass/inflation)*

# GRASS Inflation Analysis · July 2026 · Supply growing · projected to keep growing

Grass (GRASS) is a **Solana DePIN token with a hard 1,000,000,000 cap that was minted in full at launch** — the token contract has never issued a single new GRASS, so every unit of supply growth is a locked bucket opening. Over the 90 days to Jul 21 2026 about **51.4M GRASS** actually left its locks: **14.5M** of network rewards, **17.5M** of realised vesting and **19.4M** of Foundation treasury deployment. Buy pressure is **zero on every row** — no buyback, no burn, no treasury bid. The framework nets that to about **+8.13%** against **632.1M circulating**; our supply monitor reads the same window at **+11.79%**.

## The verdict, in one paragraph

For the window opening Jul 21 2026, the MrNasdog Pressure Framework reads **GRASS at about +8.13% net** supply growth over the next 90 days — roughly **51.4M GRASS** of gross release against **zero** buy pressure. Our supply monitor reads the trailing 90 days at **+11.79%**, a gap of about **3.66 percentage points** that ships a **⚠ monitor-gap chip**. The gap has a specific cause and we walked it: the published unlock calendar for the window totals **94.8M GRASS**, but the lock vaults on Solana only paid out **51.4M**. The calendar counts a token as released the moment it vests on paper; the vault only counts it when it moves. Grass is a **hard-capped DePIN token that is nonetheless steeply dilutive on the active float** — nothing is printed, and yet nothing stands against the unlock either.

## Sell pressure: where new GRASS comes from

Sell #1 — protocol inflation — is **14.5M GRASS** over 90 days, and the mechanism matters more than the number. Grass has **no protocol inflation in the ordinary sense**. The SPL token supply reads **999,993,143** against the **1,000,000,000** cap and has not moved up since the Oct 28 2024 launch; the tiny shortfall is dust burned at launch, not a burn engine. What looks like emission is a transfer: the Foundation vault sends about **4.84M GRASS** a month to the wallet that pays out network rewards to bandwidth providers, and it did so on **Apr 28 2026**, **May 25 2026** and **Jun 23 2026**. Three draws is **14.5M** reaching holders. As a cross-check, the published linear release for the router-reward and future-incentive buckets works out to about **3.68M** a month, or **11.0M** across the window — the same order of magnitude, which is what we need before booking the measured figure.

Sell #2 — vesting unlocks — is **17.5M GRASS**, and this is where the framework parts company with every unlock tracker covering Grass. Investor and contributor GRASS sits inside three readable multisig lock vaults on Solana that release on the 28th of each month. Read at both ends of the window, each vault fell from **21,431,666** to **15,586,666** — a payout of exactly **1,948,333** per vault on **Apr 28 2026**, **May 28 2026** and **Jun 28 2026**. Three vaults, three firings, **17.5M** released. The public vesting calendar for the very same three dates says **76.0M** — early investors at about **19.39M** a month plus contributors at about **5.95M** a month. That is **4.3 times** the flow the vaults produced. Tokens that vest on paper but never leave the lock are not sell pressure yet, so the framework books the realised outflow and carries the undrawn remainder as overhang.

Sell #3 — Foundation and unscheduled unlocks — is **19.4M GRASS**, the largest single row on the page. The Grass Foundation treasury is a multisig vault holding about **264.4M GRASS** with no published release calendar at all. Outside the reward stream it deployed about **6.1M** on **Apr 23 2026** and a single block of **13.3M** on **Jun 10 2026**. Because this is a repeated, dated, on-chain pattern rather than a hypothetical, it earns a real number rather than a zero. Sell #4 — long-term locked or bankruptcy — is **zero**: Grass has no bankruptcy estate, no trustee and no court-ordered distribution, so the row stays empty.

## Buy pressure: where new GRASS goes

Every buy row on the Grass ledger reads **zero**, and that is the single most important fact on this page. Buy #1 — programmatic buyback — is **zero**: Grass earns genuine revenue, roughly **$33M** annualised in stablecoins from AI customers, but none of it is routed into buying GRASS on the open market. On **Jul 7 2026** the Grass Foundation opened a holder vote asking whether a share of protocol revenue should flow back to token holders. That vote is a signal, not a mechanism; nothing is executed on chain, so nothing is booked.

Buy #2 — protocol fee burn — is **zero**. Grass is an application network rather than a base chain: it bills AI customers off chain and destroys no GRASS in the process, so there is no per-transaction burn to offset the unlock. Buy #3 — Foundation buy — is **zero**, and this one is measured rather than assumed: across the whole 90-day window the Foundation vault only sent GRASS out, and not a single token came back in. Buy #4 — new long-term lock — is **zero**: no new lockup contract with an announced size was deployed, and tokens leaving the vesting vaults move to holder wallets, not into a fresh lock. With a sell side of **51.4M** and a buy side of **zero**, the net is simply the gross.

## Foundation and overhang

Three team-controlled overhangs are tracked on GRASS. The first is the **Foundation treasury vault**, a Solana multisig holding about **264.4M GRASS** — roughly **42%** of the circulating float — against no published release calendar; it is read on chain at every rebuild. The second is the **three vesting lock vaults**, which still hold about **46.8M GRASS** undrawn between them and pay out on the 28th of each month. The third is the **vested-but-unclaimed entitlement**: about **58.5M GRASS** that the public calendar treats as already released but which never left a vault during the window. That backlog is the reason the trackers and the framework disagree, and its direction — draining or accumulating — is the single most useful thing to watch next quarter.

The rule is the same for all three. If any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh. Nothing is projected forward on capacity alone: the Foundation could move **264.4M GRASS** tomorrow, but being able to move is not the same as moving, and only observed, dated movement earns a number on this page.

## How GRASS compares to other DePIN networks

Grass sits in the hard-capped, fully pre-minted class of DePIN tokens — the opposite structure to networks like Helium or Filecoin, where the chain itself mints new units as a block reward and supply growth is an ongoing protocol action. On Grass the protocol prints nothing; the token contract has been quiet since launch. That sounds far safer, and in one sense it is: there is a firm ceiling of **1,000,000,000 GRASS** that no vote can raise, and dilution has an end date rather than a tail. But a cap only limits the total. What reaches the market over any given quarter is decided by unlock schedules and treasury discretion, and on that measure Grass is currently more dilutive than most emission-based chains, at about **+8.13%** across 90 days.

Against exchange tokens with quarterly buybacks — the BNB or OKB shape — the contrast is sharper still. Those tokens run a revenue-to-token pipe that removes supply on a schedule, so their ledgers carry a real number on the buy side. Grass has the revenue but not the pipe: about **$33M** annualised flows in and none of it reaches the token. The **Jul 7 2026** revenue-share vote is precisely the mechanism that would move Grass from one class to the other, which is why it is the most consequential open item on the page.

Against fee-burn base chains — the Ethereum or BNB Chain shape — Grass has no equivalent lever at all, because it does not settle transactions and charges its customers off chain. The comparison worth making is with other young, venture-backed, pre-minted DePIN tokens whose first two years are dominated by investor and contributor vesting rather than by any protocol mechanic. In that cohort Grass is unusual only in one respect: its locks are readable, so the difference between the calendar and the actual flow can be measured instead of guessed.

## What to watch in the next 90 days

First, the monthly lock releases on **Jul 28 2026**, **Aug 28 2026** and **Sep 28 2026** — three firings inside the window, about **5.85M GRASS** each at the realised rate against a calendar entitlement near **25.3M**. Second, whether the vested-but-unclaimed backlog of about **58.5M GRASS** starts draining; a catch-up claim would be the one event that closes the monitor gap from the primary side. Third, the Stage 2 network-reward claim window opening **Jul 22 2026** — notable because those rewards are paid in stablecoin rather than in GRASS, so the largest community distribution of the year adds no token supply at all. Fourth, the outcome of the revenue-share vote opened on **Jul 7 2026**: if it becomes an actual buyback or staking sink, the buy side of this ledger stops being zero. Fifth, the early-investor vesting schedule completing around **Oct 28 2026**, which removes the largest recurring unlock from the calendar entirely.

## Summary

The MrNasdog Pressure Framework reads **GRASS at about +8.13% net supply growth** over the next 90 days — **51.4M GRASS** leaving its locks against **zero** buy pressure — versus **+11.79%** on our supply monitor, a **3.66 point** gap that ships with a warning chip. The structural mechanism is unusual: Grass mints nothing and never will, because its entire **1,000,000,000** supply was created at launch and the cap cannot be raised; all supply growth is pre-minted buckets opening on schedule or at Foundation discretion. The key risk is that the buy side is empty on every row while a **264.4M GRASS** treasury with no published calendar sits above a float of **632.1M**. The ceiling is real and the dilution ends, but it has not ended yet, and until the revenue-share vote becomes a live mechanism nothing on this page pushes back against it.

---

*MrNasdog Pressure Framework analysis of GRASS, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 21 2026.*

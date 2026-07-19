---
title: "UNI Inflation Analysis · July 2026 · Mixed Flows, Supply Roughly Steady"
description: "Uniswap's fee switch burned ~4.14M UNI over 90 days against a 5M growth-budget tranche, with no protocol mint ever called. Framework reads +0.14% net."
canonical_url: "https://mrnasdog.com/research/uni/inflation"
tags: ["crypto", "uni", "uniswap", "defi"]
published: true
---

*Originally published at [mrnasdog.com/research/uni/inflation](https://mrnasdog.com/research/uni/inflation)*

# UNI Inflation Analysis · July 2026 · Mixed Flows, Supply Roughly Steady

Uniswap has never minted a single new UNI — the contract's dormant 2% minter has never been called, and total supply still reads its **1B genesis figure**. The only fresh supply is the **20M UNI per year growth budget**, which released one **5M UNI** tranche on **Jul 14 2026**. Against it, the UNIfication fee switch destroyed **~4.14M UNI** over the same 90 days, verified directly on the burn address. Framework reading: **+0.14% net** — Uniswap's float is close to flat, with the direction set by swap volume rather than by a schedule.

## The verdict, in one paragraph

For the 90-day window ending **Jul 19 2026**, the MrNasdog Pressure Framework reads Uniswap at **+0.14% net**: the growth-budget vesting added **5M UNI** to the float while the UNIfication fee-switch burn removed **4.14M UNI**, so the two mechanisms very nearly cancel. The inflation monitor reads **−1.34%** over the same window, a gap of **1.48 percentage points**, which crosses the framework's tolerance and ships a monitor-gap flag. That gap is not a burn the framework missed. The monitor tracks a circulating-supply classification computed as genesis supply minus burned UNI minus the DAO governance treasury balance — so it moves whenever UNI enters or leaves that treasury, whether or not a single token changes hands on a market. Two such custody events landed in this window: a governance vote executed **Jun 1 2026** returned **12.5M** previously-delegated UNI into the treasury, and the **5M** growth-budget tranche left it on **Jul 14 2026**. The framework keeps its net-flow-to-market read. UNI in mid-2026 is best characterised as a **zero-mint governance token with a usage-contingent burn**.

## Sell pressure: where new UNI comes from

Sell #1, protocol inflation, is **zero**. The UNI contract carries a minter that became unlockable in September 2024 and could issue up to 2% of supply per year, but Uniswap governance has never called it. Read directly on-chain this window, UNI's total supply is still exactly **1,000,000,000** — the genesis figure, untouched since 2020. The Pressure Framework counts what actually fires, never what a contract merely permits.

Sell #2, vesting unlocks, is the only non-zero sell row, at **5M UNI**. Uniswap's original four-year vesting — team, investors, advisors, the September 2020 airdrop and liquidity-mining rewards — ran to completion in 2024, and every unlock tracker now lists UNI as fully unlocked with no cliff remaining. What replaced it is the **20M UNI per year growth budget** created by the UNIfication vote, paid in quarterly tranches out of the DAO governance treasury from January 2026. One tranche fired inside this window: exactly **5,000,000 UNI** left the Uniswap governance timelock on **Jul 14 2026**, confirmed by reading the timelock balance before and after. That is already-minted treasury supply moving out of protocol custody, not new issuance.

Sell #3, Foundation and unscheduled unlocks, is **zero**. Uniswap's two identified team-controlled pools both grew rather than sold in the window. Sell #4, long-term locked or bankruptcy, is **zero** — Uniswap has no bankruptcy estate and no trustee distribution schedule of any kind.

## Buy pressure: where new UNI goes

Buy #2, protocol fee burn, is the load-bearing buy row at **4.14M UNI**. The UNIfication fee switch, live since December 2025, collects a share of swap-fee revenue from Uniswap v2, v3 and Unichain into a single vault contract. That accumulated fee value cannot simply be withdrawn: it is released only when a claimant burns UNI through a second contract, which forwards the UNI to the dead address where it can never return. Because the claimant has to acquire the UNI first, the burn is funded by real market demand rather than by a treasury transfer. Reading the burn address directly on-chain, its UNI balance rose from **103.36M** at the start of the window to **107.50M** at the end — a destruction of **4,138,000 UNI**. Sampling the same address at six points across the 90 days shows the balance rising at every step, which confirms a continuous mechanism rather than a single large event.

The remaining buy rows are zero. Buy #1, programmatic buyback, is **zero** because Uniswap operates no protocol-owned wallet that accumulates UNI — fee value routes straight into the burn path, so counting it again would double-count the same flow. Buy #3, Foundation buy, is **zero**; the Uniswap Foundation runs no open-market UNI accumulation programme. Buy #4, new long-term lock, is **zero** — a redesign that would redirect UNIfication value into staking rewards instead of burns is under discussion on the Uniswap governance forum but has not reached a vote.

## Foundation and overhang

Uniswap has two identified team-controlled overhangs. The first and much larger is the **DAO governance timelock**, the on-chain treasury, holding **~267.1M UNI** as of **Jul 19 2026** — the bulk of all non-circulating UNI. It grew in this window: the **Jun 1 2026** vote recalled **12.5M UNI** that had been delegated out to the Foundation and to a group of active delegates back in 2022 and 2023, returning all of it to the timelock. The vote itself records that those tokens were never circulating; they simply moved between two non-market locations. The second overhang is the **growth-budget spending wallet**, which received the **5M** tranche on **Jul 14 2026** and now holds **~14M UNI**. Its history shows roughly **15M UNI** received across three tranches and only about **1M UNI** spent, in February 2026 — a single sporadic firing with no published calendar, which is why the framework projects nothing from it. Both balances are tracked on every refresh: if either the treasury or the budget wallet sees its UNI balance fall between refreshes through a market deploy, that outflow enters Sell #3 at the next refresh.

## How UNI compares to other DEX governance tokens

Most DEX governance tokens are structurally inflationary by design. SushiSwap's SUSHI, PancakeSwap's CAKE and Curve's CRV all fund liquidity mining or staking rewards out of continuous emission, so fresh supply arrives every block regardless of how the protocol is used. Uniswap is the opposite case in mechanism: it has never minted, its four-year vesting is spent, and its only supply addition is a fixed, already-minted treasury budget with a known annual ceiling of 20M UNI. Curve's veCRV design is the nearest structural cousin in that it separates locked holders from the market float, but Curve still emits new CRV continuously while Uniswap does not emit at all.

Against fee-funded burn and buyback models — Aave's AAVE buyback, MakerDAO's MKR smart-burn, or an EIP-1559-style base-fee burn — Uniswap sits closer to the base-fee end of the spectrum than to the buyback end. A quarterly buyback spends a budgeted amount whether or not the protocol was busy. Uniswap's burn is coupled one-for-one to fee claims, so it scales with swap volume and stops when volume stops. That makes UNI's deflation **usage-contingent rather than scheduled**, and it is the single most important thing to understand about UNI inflation: the sell side of the ledger is fixed and known, while the buy side floats with how much people actually trade on Uniswap.

## What to watch in the next 90 days

First, two fee-expansion votes closing **Jul 26 2026** — one activating protocol fees on Uniswap v4 pools across seven chains, the other extending v2 and v3 fee collection to a new chain deployment. Both would widen the revenue base feeding the burn. Second, the next **growth-budget quarterly tranche around Oct 1 2026**, which adds another 5M UNI to the float on the same fixed cadence. Third, **Uniswap swap volume** itself, since the burn rises and falls with fee revenue and is the only variable in this ledger. Fourth, a governance forum proposal opened **Jun 25 2026** that would hard-cap UNI supply by auto-burning any future 2% inflation and redirect UNIfication value into staking — still a request for comment with no vote scheduled, but it would rewrite both sides of this ledger if it advanced. Fifth, any DAO vote to activate the dormant 2% minter or to deploy the ~267.1M treasury to market.

## Summary

Uniswap's UNI is a 1B genesis-supply, fully-unlocked, DAO-governed token whose supply is now close to flat. No protocol mint has ever fired, the original vesting is spent, and the only fresh supply is a 5M-per-quarter treasury growth budget — against which the UNIfication fee switch burned **4.14M UNI** this window, confirmed directly on the burn address. The framework reads **+0.14% net** while the monitor reads **−1.34%**, a **1.48 percentage point** gap driven by circulating-supply reclassification after 12.5M delegated UNI returned to the DAO treasury on Jun 1 2026, not by any flow the framework missed. The key risk is swap volume, because Uniswap's burn is usage-contingent and its supply addition is not; the ceiling is the 1B genesis supply with no mint ever called; and the swing factor is whether governance activates the dormant 2% minter or expands the fee switch further.

---

*MrNasdog Pressure Framework analysis of Uniswap (UNI), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 19, 2026.*

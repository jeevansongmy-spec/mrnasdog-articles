---
title: "UNI Inflation Analysis · August 2026 · Mixed Flows, Supply Roughly Steady"
description: "Uniswap's fee switch burned ~3.93M UNI over 90 days against a 5M growth-budget tranche, with no protocol mint ever called. Framework reads +0.17% net."
canonical_url: "https://mrnasdog.com/research/uni/inflation"
tags: ["crypto", "uni", "uniswap", "defi"]
published: true
---

*Originally published at [mrnasdog.com/research/uni/inflation](https://mrnasdog.com/research/uni/inflation)*

# UNI Inflation Analysis · August 2026 · Mixed Flows, Supply Roughly Steady

Uniswap has never minted a single new UNI — the contract's dormant 2% minter has never been called, and total supply read on-chain still shows its **1,000,000,000** genesis figure. The only fresh supply this window is the **20M UNI per year growth budget**, which released one **5M UNI** tranche on **Jul 14 2026**. Against it, the UNIfication fee-switch burn destroyed **~3.93M UNI** over the same 90 days, verified directly on the burn address. Framework reading: **+0.17% net**, versus a monitor read of **−1.56%** — Uniswap's float is close to flat, with direction set by swap volume rather than by a schedule.

## The verdict, in one paragraph

For the 90-day window ending **Aug 1 2026**, the MrNasdog Pressure Framework reads Uniswap at **+0.17% net**: the growth-budget vesting added **5M UNI** to the float while the UNIfication fee-switch burn removed **3.93M UNI**, so the two mechanisms very nearly cancel. The inflation monitor reads **−1.56%** over the same window, a gap of **1.73 percentage points**, which crosses the framework's tolerance and ships a ⚠ monitor-gap flag. That gap is not a burn the framework missed. The monitor tracks a circulating-supply figure computed as genesis supply minus burned UNI minus the DAO governance treasury balance, so it moves whenever UNI enters or leaves that treasury, whether or not a token changes hands on any market. This window the treasury balance grew by about **7.6M UNI** — roughly **12.6M** in from returned and consolidated grant wallets against the **5M** growth tranche paid out — and that custody shift, not a market sale, is most of the monitor's decline. The framework keeps its net-flow-to-market read. UNI in mid-2026 is best characterised as a **zero-mint governance token with a usage-contingent burn**.

## Sell pressure: where new UNI comes from

Sell #1, protocol inflation, is **zero**. The UNI contract carries a minter that became unlockable in September 2024 and could issue up to 2% of supply per year, but Uniswap governance has never called it. Read directly on-chain at both ends of this window, UNI's total supply is still exactly **1,000,000,000** — the genesis figure, untouched since 2020. The Pressure Framework counts what actually fires, never what a contract merely permits, so the dormant minter contributes nothing.

Sell #2, vesting unlocks, is the only non-zero sell row, at **5M UNI**. Uniswap's original four-year vesting — team, investors, advisors, the September 2020 airdrop and liquidity-mining rewards — ran to completion in 2024, and every unlock tracker now lists UNI as fully unlocked with no cliff remaining. What replaced it is the **20M UNI per year growth budget** created by the UNIfication vote, paid in quarterly tranches out of the DAO governance treasury from January 2026. One tranche fired inside this window: exactly **5,000,000 UNI** left the Uniswap governance timelock on **Jul 14 2026**, confirmed by reading the treasury's transfer logs. That is already-minted treasury supply moving out of protocol custody, not new issuance.

Sell #3, Foundation and unscheduled unlocks, is **zero**. Uniswap's two identified team-controlled pools both grew rather than sold in the window, and neither shows a market deploy. Sell #4, long-term locked or bankruptcy, is **zero** — Uniswap has no bankruptcy estate and no trustee distribution schedule of any kind.

## Buy pressure: where new UNI goes

Buy #2, protocol fee burn, is the load-bearing buy row at **3.93M UNI**. The UNIfication fee switch, live since December 2025, collects a share of swap-fee revenue from Uniswap v2, v3 and Unichain into a single vault contract, TokenJar. That accumulated fee value cannot simply be withdrawn: it is released only when a claimant burns UNI through a second contract, Firepit, which forwards the UNI to the dead address where it can never return. Because the claimant has to acquire the UNI first, the burn is funded by real market demand rather than by a treasury transfer. Reading the burn address directly on-chain, its UNI balance rose from **103.94M** at the start of the window to **107.87M** at the end — a destruction of **3,928,000 UNI**. Sampling the same address across the 90 days shows the balance rising at every step, which confirms a continuous mechanism rather than a single event.

The other three buy rows are **zero**. Buy #1, programmatic buyback, does not exist: Uniswap does not accumulate UNI in a treasury that bids on the market — the fee switch destroys UNI directly, so there is no buyback-and-hold. Buy #3, Foundation buying, is zero because the Uniswap Foundation spends UNI through grants rather than accumulating it. Buy #4, a new long-term lock, is zero — no fresh escrow or multi-year lock was announced in the window, and the growth-budget vesting is supply leaving the treasury, not entering a lock.

## Foundation and overhang

The framework tracks two team-controlled overhangs, and both are surfaced on the overview rather than folded into a sell figure, because neither actually reached the market this window. The first is the **DAO governance treasury**, the on-chain timelock that holds roughly **267.2M UNI** — about 30% of post-burn supply. It is the source of the 20M-per-year growth budget, and it is refreshed on every rebuild by reading its balance directly; this window it grew rather than shrank, taking in about 12.6M UNI from returned grant and delegation wallets against the 5M it paid out. The second is the **growth-budget operating wallet**, which has received the quarterly tranches and still holds around **14M UNI** — most of what it has been sent, largely unspent. If either of these balances falls between refreshes — the treasury deploying beyond the scheduled tranche, or the operating wallet selling into the market — that outflow enters Sell #3 at the next refresh. Until then they are capacity, not cadence, and the framework holds them at zero.

## How UNI compares to other DeFi tokens

Most large DeFi governance tokens sit in one of two camps. The first is the **uncapped-emission** camp — protocols that still mint new tokens to pay liquidity incentives or stakers, so their supply grows structurally regardless of usage. The second is the **fixed-but-inert** camp — tokens like the old UNI, fully unlocked with a hard genesis cap but no mechanism to remove supply, where the float simply sits flat. UNIfication moved UNI into a rarer third category: a **fixed-supply token with a demand-linked burn**. There is no issuance at all, and the only force that removes supply is holders burning UNI to claim swap fees.

That makes UNI structurally closer to an **exchange token with a fee burn** than to a typical DeFi governance token — value accrual scales with trading volume, and the burn strengthens when the venue is busy. The key difference is direction of causation: an exchange buys back and burns from its own revenue, whereas UNI's burn is paid by whoever wants the accumulated fees, so it consumes UNI only when there is real demand for that claim. Against uncapped DeFi peers, UNI cannot inflate; against inert fixed-cap peers, it can actually shrink. Where it lands in any given quarter is decided by two numbers that are close in size — the **5M** scheduled growth release and a burn that has run near **3.9M to 4.1M** — so the token reads as roughly flat, tilting deflationary only when swap volume lifts the burn above the release.

## What to watch in the next 90 days

Four items would move this reading. First, the **next quarterly growth-budget tranche** of about **5M UNI** is due around **Oct 1 2026** and lands inside the next window — the recurring sell input. Second, the **fee-switch burn rate**: it tracks swap volume directly, so a busier quarter pushes the ~3.93M burn above the 5M release and flips the net deflationary, while a quiet one widens the gap the other way. Third, **RFC 26132**, posted **Jun 25 2026**, proposes a synthetic hard cap that would route inflation to burn and add staking distribution — it is only a request for comment today, with no vote scheduled, but an on-chain execution would materially change the ledger. Fourth, any **treasury deployment** beyond the scheduled tranche, or a sale from the ~14M growth-budget operating wallet, would open Sell #3.

## Summary

Uniswap is a **zero-mint governance token with a usage-contingent burn**. No UNI has ever been issued — total supply reads its **1B** genesis figure on-chain — so the only fresh supply is the **5M** quarterly growth-budget tranche, and the only removal is the fee-switch burn, which took **3.93M UNI** to the dead address this window. The two nearly cancel for a net of **+0.17%**, roughly flat. The monitor's **−1.56%** mostly reflects UNI moving into the DAO treasury rather than any market sale, which is why the framework keeps its own read and flags the **1.73-point** gap. The key risk is not inflation but the treasury overhang; the ceiling is the fixed 1B cap that can only ever shrink.

---

*MrNasdog Pressure Framework analysis of UNI, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 1 2026.*

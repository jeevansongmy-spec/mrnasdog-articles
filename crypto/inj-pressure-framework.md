---
title: "INJ Inflation Analysis · July 2026 · Supply growing, projected to keep growing"
description: "A MrNasdog Pressure Framework read of Injective (INJ): ~1.19M/90D of 4.40% staking inflation vs only ~0.15M of buyback-and-burn. Framework +1.04% net; monitor +0.09% (0.95pp gap) — mildly inflationary."
canonical_url: "https://mrnasdog.com/research/inj/inflation"
tags: ["crypto", "inj", "injective", "burn-auction"]
published: true
---

> Originally published at **[mrnasdog.com/research/inj/inflation](https://mrnasdog.com/research/inj/inflation)** by MrNasdog.

Injective mints about **1.19M INJ** over the next 90 days as staking rewards under a **4.40%** yearly inflation rate, while its monthly buyback and weekly burn auction destroy only about **0.15M INJ** in the same window. The burns are real but far below the mint, so the framework reads about **+1.04%** net — mildly inflationary. Our supply monitor reads **+0.09%** over the last 90 days; the gap of **0.95 percentage points** is a supply-proxy artifact in the monitor, so the framework keeps its on-chain read and ships a monitor-gap note.

## The verdict, in one paragraph

For the 90-day window ending July 14 2026, the MrNasdog Pressure Framework reads **INJ at about +1.04% net** on the forward view: about **1.19M INJ** of new staking issuance against roughly **0.15M INJ** removed by the Community BuyBack and the burn auction. Our supply monitor reads the realized last-90-day change at just **+0.09%**, a gap of about **0.95 percentage points**, which is over the half-point tolerance, so a **monitor-gap chip ships**. The deep walk traced the gap to the monitor's market-cap-over-price supply proxy, whose circulating figure is pinned near INJ's **100M** genesis number and does not track the chain's on-chain mint, while Injective's own mint module confirms annual provisions of about **4.84M INJ** a year. INJ is **mildly inflationary on the active float** — the burns brake the mint, but they do not reverse it.

## Sell pressure: where new INJ comes from

Sell #1 — protocol inflation — is the whole sell story, at about **1.19M INJ** over the next 90 days. Injective mints new INJ every block as staking rewards; the on-chain mint module reports inflation at **4.40%** a year, with annual provisions near **4.84M INJ**. The rate is pinned at the top of the band because the staked share of supply, near **50%**, sits below the protocol's **60%** bonded target, and the dynamic mechanism keeps issuance at its ceiling whenever staking runs light. Successive tokenomics upgrades — INJ 3.0 and the 2026 Supply Squeeze — lowered that band to a **2.2%–4.4%** range, but 4.40% is where the live rate sits today, and there is no supply cap to slow it.

Sell #2 — vesting unlocks — is **zero**: every team, seed, private-sale and ecosystem allocation finished unlocking by early 2024, so INJ is fully unlocked and no cliff hits the market. Sell #3 — Foundation and unscheduled unlocks — is also zero as a flow; a small governance-controlled community pool holds about **0.04M INJ**, and foundation and ecosystem balances sit off the freely-traded float, but none has a scheduled release. Sell #4 — long-term locked or bankruptcy — is zero, because no bankruptcy estate or court distribution applies to INJ, and staked INJ merely faces a **21-day** unbonding period rather than a long-term lock.

## Buy pressure: where new INJ goes

Unlike a pure emission chain, INJ has a real buy side — it is simply smaller than the mint. Buy #1 — programmatic buyback — is about **0.13M INJ**: a monthly Community BuyBack routes protocol revenue into repurchasing INJ, and every bought token is **permanently burned** rather than parked in a wallet, across recent rounds of roughly **51K**, **42K** and **39K INJ**. Buy #2 — protocol fee burn — is about **0.02M INJ**: the weekly burn auction pools **60%** of exchange and dApp fees into a basket, auctions it for INJ, and burns the winning bid. Buy #3 — Foundation buy — and Buy #4 — new long-term lock — are both zero, with no discretionary open-market buying or new escrow in the window. Together the buy side removes about **0.15M INJ**, roughly an eighth of the **1.19M** minted — enough to slow dilution, not to end it.

## Foundation and overhang

INJ carries no classic unlock overhang — the token is fully distributed, and the published circulating figure of about **100M** already treats the float as liquid. The balances worth naming are the governance-controlled **community pool**, currently about **0.04M INJ**, and the foundation and ecosystem holdings that sit between the **100M** public circulating figure and the roughly **110M** minted on-chain. None of these has a dated release; the community pool can be deployed only by a passing on-chain vote, and the buyback destination is a burn, so bought INJ never becomes future sell pressure. The framework re-checks the on-chain mint rate, the staked ratio and the monthly burn totals on a roughly bi-weekly walk; if any of these team-controlled balances moves between refreshes, that outflow enters Sell #3 at the next refresh.

## How INJ compares to other buyback-and-burn L1s

INJ belongs to the class of **fee-funded buyback-and-burn tokens** — assets that pair ongoing issuance with a revenue-driven burn, the way some exchange tokens run quarterly buybacks. What separates INJ from a pure-emission chain like an uncapped proof-of-stake L1 with no burn is exactly that buy side: the monthly Community BuyBack and the weekly burn auction genuinely remove INJ. What separates it from a token that has actually gone net-deflationary is scale — at current activity the burns run near **0.57M INJ** a year against a mint of about **4.84M INJ** a year, so the burn offsets roughly an eighth of issuance, not all of it.

That is the honest read the marketing tends to blur: Injective describes a **Supply Squeeze** and a deflationary trajectory, and the mechanisms are real and growing, but on the current numbers INJ is still **mildly inflationary**, not deflationary. For an inflation lens specifically, INJ sits below a no-burn staking chain and above a genuinely deflationary fee-burner: it dilutes, but at a slowing rate that would flip negative only if the burns roughly quadrupled or the mint fell toward the bottom of its **2.2%** band as staking rises past the **60%** target.

## What to watch in the next 90 days

Watch the monthly Community BuyBack rounds — their size scales with protocol revenue, and a sustained jump (the June 2026 round was the largest to date) is the single fastest way the buy side could start to close on the mint. Watch the staked ratio: if it climbs back above the **60%** bonded target, the dynamic band eases inflation below 4.40% toward its **2.2%** floor, directly shrinking Sell #1. Watch the weekly burn auction basket, a live read on exchange and dApp fee revenue. And watch the on-chain mint rate itself, the single number that sets Sell #1 each block.

## Summary

INJ is an uncapped proof-of-stake staking token whose supply grows by continuous emission at a 4.40% yearly rate, pinned at the top of its band because staking runs below the 60% bonded target. Injective mints about 1.19M INJ over the next 90 days, while a monthly buyback and a weekly burn auction destroy only about 0.15M, leaving the framework at about +1.04% net — mildly inflationary. Our supply monitor reads +0.09% realized, a gap of about 0.95 points traced to a supply proxy pinned at the 100M genesis figure, so the framework keeps its on-chain read and flags the gap. The key risk to this reading is the burn side: if the buyback rounds keep scaling and staking rises, INJ's dilution narrows and could one day turn deflationary — but it is not there yet.

---

*MrNasdog Pressure Framework analysis of Injective (INJ), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 14 2026.*

---
title: "CAKE Inflation Analysis · August 2026 · Supply shrinking, projected to keep shrinking"
description: "PancakeSwap burns roughly three times the CAKE it mints: ~2.0M created against ~6.9M destroyed per 90 days. Framework -1.52% net against a monitor -1.5%."
canonical_url: "https://mrnasdog.com/research/cake/inflation"
tags: ["crypto", "cake", "pancakeswap", "defi"]
published: true
---

> Originally published at **[mrnasdog.com/research/cake/inflation](https://mrnasdog.com/research/cake/inflation)** by MrNasdog.

# CAKE Inflation Analysis · August 2026 · Supply shrinking, projected to keep shrinking

PancakeSwap burns far more CAKE than it mints. Over the 90 days to **Aug 4 2026**, farm and pool rewards issued about **2.0M CAKE** — roughly **22,250** a day — while a revenue-funded buyback-and-burn destroyed about **6.9M CAKE**, more than three times as much. On a circulating base of **322M CAKE** the Pressure Framework reads **-1.52%** net, against our supply monitor's stable **-1.5%** for the same window — a gap of about **0.02 percentage points**, so no monitor-gap flag ships. CAKE is a **capped, structurally deflationary exchange token** with no vesting overhang to unlock.

## The verdict, in one paragraph

For the 90-day window ending **Aug 4 2026**, the MrNasdog Pressure Framework reads **CAKE at about -1.52% net**: sell pressure of **2.0M CAKE** against buy pressure of **6.9M CAKE** on a circulating base of **322M CAKE**. Our supply monitor reads a stable **-1.5%** across the clean days of the same window, a gap of about **0.02 percentage points** — well inside the half-point tolerance, so no monitor-gap flag ships with this page. The two agree because the CAKE ledger is closed, not estimated: real supply is defined by the project's own docs as the token's total supply minus the balance sitting in its dead address, and reading both on-chain at each end of the window shows the net effective supply falling from about **345M** to about **340M CAKE** — a drop of **4.91M**, which is exactly the **2.0M** minted minus the **6.9M** burned. CAKE is best labelled **a capped exchange token that is deflationary by structural buyback-and-burn**.

## Sell pressure: where new CAKE comes from

It comes from one place: emission. Sell #1 — protocol inflation — is **2.0M CAKE** over 90 days, minted as farm, syrup-pool and product rewards at about **22,250 CAKE** a day. That rate is the result of successive cuts under PancakeSwap's current tokenomics, down from an original **40,000** a day, and the exchange's own monthly burn reports confirm the pace — roughly **667,000 CAKE** minted a month across April, May and June 2026. The emission is capped in aggregate: total CAKE can never exceed the **400M** hard cap, which the community itself cut from **450M** in a governance proposal opened **Jan 16 2026**. Because emission runs on a governance-set schedule rather than a decay curve or a cliff, the trailing rate is an honest forward predictor.

Every other sell row is zero, and each for a clean reason. Sell #2 — vesting unlocks — is **zero** because CAKE was fair-launched: there was no private sale, no venture allocation and no team vesting, so there is no cliff calendar for anything to unlock from. This is unusual and it matters — most tokens carry a vesting overhang that eventually reaches the market, and CAKE simply does not have one. Sell #3 — Foundation and unscheduled unlocks — is **zero** in value: the project treasury is funded from a slice of the daily emission and spent operationally, but those coins are already counted as new supply the moment they are minted, so booking the treasury's spending again would double-count it. Sell #4 — long-term locked or bankruptcy — is **zero**: CAKE has no estate, no trustee and no court-ordered distribution.

## Buy pressure: where new CAKE goes

CAKE's buy side is a burn, and it is large. Buy #1 — programmatic buyback — is **6.10M CAKE** over 90 days: protocol revenue from spot trading, perpetuals, prediction, lotteries and launchpads is used to buy CAKE on the open market and send it to a dead address that no one can spend from. This is the dominant engine of PancakeSwap's deflation and, by the project's own weekly breakdown, the trading buyback alone accounts for the bulk of it. Buy #2 — protocol fee burn — is **0.80M CAKE**: fees that are already collected in CAKE are burned directly, without a market purchase. Together the two burn about **6.9M CAKE** over the window — more than three times the **2.0M** minted — which is why the capped supply keeps shrinking. PancakeSwap has now recorded net deflation for more than **34** consecutive months.

The other two buy rows are zero. Buy #3 — Foundation buy — is **zero**: there is no discretionary open-market buying outside the automatic revenue buyback that already sits in Buy #1. Buy #4 — new long-term lock — is **zero**: holders can lock CAKE into veCAKE for voting power over where emissions are directed, but that locking is user-initiated and reversible at expiry rather than a protocol escrow, and no new protocol lock was added in the window. Locking removes CAKE from the tradable float, but because it is a holder choice that unwinds on its own schedule, the framework watches it rather than booking it as buy pressure.

## Foundation and overhang

CAKE carries an unusually light overhang for an exchange token. There is no vesting contract, no investor unlock schedule and no bankruptcy estate — the three pools that dominate most ledgers are simply absent here. What remains is the operational treasury, funded from a slice of the daily emission and spent on grants, incentives and operations. Those coins are counted as new supply at the moment of minting, so the treasury is a monitored balance rather than a booked sell row, and it has no published release schedule. The one other off-float pool is user-elected veCAKE locking, which is a holder brake rather than a team overhang.

The rule that governs the treasury is the same one applied everywhere: if its balance falls between refreshes in a way not already captured by emission, the outflow enters Sell #3 at the next refresh. The buyback destination is fully transparent — bought-back CAKE goes to a public dead address whose balance is read on-chain each rebuild, and it stood at about **4,632M CAKE** destroyed over the token's life as of **Aug 4 2026**. Because those coins are burned rather than accumulated, there is no buyback wallet that could later sell back into the market.

## How CAKE compares to other exchange tokens

The right comparison class for CAKE is the exchange and DEX tokens that route revenue back into their own supply — the quarterly-buyback exchange tokens and the fee-driven DEX tokens. What separates them is not price but three mechanism choices: whether the supply is capped, whether new issuance still exists, and whether revenue is used to remove tokens. CAKE sits at the aggressive end of deflation. It is capped at **400M**, it still mints (unlike a token that has finished emitting), and it burns far more than it mints every single week. That combination — live emission fully overwhelmed by a live burn — is rarer than it sounds.

Contrast that with a vote-escrow DEX token that mints continuously and burns nothing, where the float grows every epoch and vote-locking is the only brake — the mirror image of CAKE. Or contrast it with a quarterly-buyback exchange token that buys back and burns in lumpy scheduled events rather than continuously. CAKE's burn is continuous, funded by day-to-day product revenue rather than a treasury decision, and transparent to a public dead address. The honest way to read CAKE is that it converts its trading and product revenue directly into supply reduction, which is why it has printed **34** straight months of shrinking supply. The risk is the reverse of an inflation risk: the burn is only as large as PancakeSwap's revenue, so a deep drop in trading volume would slow the deflation toward neutral.

## What to watch in the next 90 days

First, trading volume. The entire burn is revenue-funded, so the single biggest swing factor is how much CAKE the protocol earns and buys back — a weak quarter shrinks the burn and pushes the net reading toward zero, a strong one deepens it. Second, the weekly burn reports themselves: PancakeSwap publishes a burn every week, and a run of weeks where net deflation slips below about **300,000 CAKE** would be the first sign the trend is cooling. Third, any governance move on emission — the daily mint has been cut repeatedly and voters could cut it again, which would deepen deflation without needing more revenue. Fourth, the **400M** cap: with net effective supply at about **340M** and falling, the cap is a ceiling the token is moving away from, not toward, and any proposal to lower it further would be structurally bullish for scarcity. Fifth, veCAKE lock balances, which change how much CAKE sits off the tradable float.

## Summary

CAKE is one of the clearest deflationary exchange tokens in our catalogue. PancakeSwap mints about **2.0M CAKE** a quarter as farm and pool rewards and destroys about **6.9M** over the same window through a revenue-funded buyback-and-burn, leaving a net **-1.52%** change in the float and a projected **-1.52%** for the next 90 days — the 34th-plus consecutive month of shrinking supply. There is no vesting row at all, because CAKE was fair-launched with no premine and no investor allocation, and the supply is capped at **400M**, cut from **450M** in January 2026. The key risk is not dilution but dependence: the burn is only as large as the protocol's revenue, so a sharp fall in trading activity would slow the deflation rather than reverse it.

---

*MrNasdog Pressure Framework analysis of CAKE, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 4 2026.*

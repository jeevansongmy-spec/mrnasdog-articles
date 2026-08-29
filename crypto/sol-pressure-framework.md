---
title:         "SOL Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description:   "SOL runs +1.28% net new supply over 90 days: 3.67% staking issuance plus 2.29M SOL of realised lockup and estate unlocks, against a burn of only 57.1K SOL."
canonical_url: "https://mrnasdog.com/research/sol/inflation"
tags:          ["crypto", "sol", "solana", "layer1"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/sol/inflation](https://mrnasdog.com/research/sol/inflation)*

# SOL Inflation Analysis · August 2026 · Supply growing, projected to keep growing

Solana has two supply stories running at once, and only one of them is slowing. Staking issuance added **5.27M SOL** over the last 90 days at a rate that decayed from **3.82%** to **3.67%** a year, while the chain's monthly lockup ladders released another **2.29M SOL** that genuinely drained out of escrow. Against that, the only mechanism removing SOL is the base-fee burn, and it destroyed just **57.1K SOL** — under **1%** of what was minted. Net **+1.28%** of circulating supply reached the market over 90 days, against **+1.12%** on the inflation monitor, and there is **no supply cap** anywhere in the design.

## The verdict, in one paragraph

The framework reads Solana at **+1.28%** net supply growth over the trailing 90 days and projects **+1.23%** for the next 90. The inflation monitor independently reads **+1.12%** over the same window, leaving a gap of **0.17** percentage points — comfortably inside tolerance, so no data-conflict chip is raised on the SOL page. Solana is **structurally inflationary on a decaying curve**: the mint shrinks about **15%** every year toward a **1.5%** floor, but the removal side is a rounding error, so the supply line only ever bends, never turns down. The interesting variable is not the mint — that is arithmetic — but whether the vesting escrows keep emptying at the pace the chain calendar sets.

## Sell pressure: where new SOL comes from

Sell #1, protocol inflation, is the largest line at **5.27M SOL**. Solana mints new SOL at every epoch boundary and pays all of it to validators and their delegators — the foundation share of issuance reads zero on the chain. The curve is the one Solana launched with: an **8%** starting rate that tapers **15%** per protocol-year toward a terminal **1.5%**. Read this session, that put the rate at **3.82%** when the window opened and **3.67%** today, falling to about **3.54%** by the end of the next 90 days — which is why the forward figure, **4.96M SOL**, is smaller than the trailing one.

That row is sensitive to something most Solana readings get wrong: how long an epoch actually takes. Measured directly from block times, epochs ran **2.05 days** for most of the window and then stepped down to **1.83 days** at epoch **1020** on **Aug 21 2026**, when the first slot-time reduction went live and Solana moved from 400-millisecond to 350-millisecond slots. Faster slots do not mean faster inflation, because the same upgrade re-scales the protocol's internal year by the inverse ratio — but a build that assumes the nominal 2.5-day epoch, or that counts epochs without noticing the step, gets the issuance figure wrong in both directions at once.

Sell #2, vesting unlocks, is **1.68M SOL** and it is a genuinely realised number rather than a calendar entry. Solana classifies a locked stake account as circulating the moment its lockup timestamp passes, whether or not anyone withdraws — so the schedule and the market can disagree. Reading each account instead of the pool settles it: one tranche lands on the **7th** of every month, a full tranche is **34** stake accounts holding about **635K SOL**, and the June, July and August 2026 tranches released **1.90M SOL** on the calendar while only **220K** is still sitting in those accounts. Roughly **88%** of every tranche walks. A separate escrow vested a **1.38M SOL** cliff on **Aug 1 2026** and has not moved a coin of it, so none of that is booked as sell pressure — it is carried as an overhang instead.

Sell #3, foundation and unscheduled unlocks, is zero for the window. Sell #4, long-term locked or bankruptcy, is **607K SOL**: the bankruptcy estate runs its own ladder on the **11th** of each month at about **202K SOL** a tranche, and every tranche dated up to **Aug 11 2026** now reads zero on the chain, with outside reporting sizing the August release at **201,741 SOL** moved on to a custody account for creditor payouts. That ladder is a different escrow from the vesting programme, so the two rows do not double-count each other.

## Buy pressure: where new SOL goes

Almost nowhere. Buy #2, the protocol fee burn, is the only non-zero buy row on Solana at **57.1K SOL** over 90 days, or roughly **634 SOL** a day. The mechanism has two legs that are easy to conflate. The base fee is a flat **5,000** lamports per signature and exactly half of it is destroyed. Priority fees are not burned at all — since the priority-fee change shipped, **100%** of them go to the block producer. Reading 30 whole blocks this session gives **32,233** signatures and shows the base fee is only **32%** of what users actually pay; the other **68%** is priority payment that never leaves supply. Out-of-protocol validator tips are plain transfers and are not a protocol burn either.

Buy #1, programmatic buyback, is zero because Solana has none: staking rewards are minted fresh, not purchased, and no protocol revenue pool exists to fund an open-market bid. Buy #3, foundation buy, is zero — the Foundation is a net seller of SOL into listed treasury vehicles at a discount, not a buyer of it. Buy #4, new long-term lock, is zero because no new lockup programme was created; about **68%** of supply is staked, but stake unbonds at an epoch boundary and staking is not a lock in the framework's sense. Listed Solana treasury companies hold roughly **11M SOL** and keep adding, but that is market demand rather than a protocol mechanism, so it stays out of the ledger.

## Foundation and overhang

Three team-controlled overhangs sit behind the SOL ledger, and all three are readable on the chain. The largest is **29.3M SOL** held in stake accounts that carry no lockup at all and are kept out of the float purely by classification — capacity with no schedule attached. Second is **19.6M SOL** still under live lockup across **793** accounts, releasing monthly into **2028**, of which **2.63M** is the bankruptcy-estate ladder running through **Sep 2027**. Third is **5.75M SOL** that has already vested and simply never been withdrawn, dominated by that unmoved **1.38M** cliff from **Aug 1 2026**. Worth noting for anyone checking a vesting aggregator: the popular ones report Solana as fully unlocked with no calendar at all, and the chain flatly contradicts them. If any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How SOL compares to other uncapped Layer-1 chains

Solana belongs to the uncapped continuous-emission class, and inside it the design is unusually honest: a fixed disinflation curve nobody can quietly renegotiate, with issuance falling on a published schedule rather than on discretion. Against a hard-cap proof-of-work chain, the contrast is structural — a halving chain steps its issuance down in discrete jumps toward a fixed ceiling, while Solana decays continuously toward a floor it never leaves. That floor is the point: at terminal **1.5%**, Solana keeps minting forever, so its supply line flattens rather than stopping.

Against the fee-burn Layer-1s, Solana looks thin on the removal side. A chain whose burn scales with congestion can flip deflationary in a busy quarter; Solana's burn is pinned to a flat per-signature charge that ignores how much work a transaction actually costs, so it stays near **634 SOL** a day whatever happens to demand — around **1%** of the mint. And against exchange tokens with quarterly buybacks, the difference is that Solana has no revenue-to-token pipe at all: fees route to validators, not to a treasury that buys the coin back.

The last comparison is the escrow one. Many Layer-1s finished vesting years ago; Solana has not. Its monthly ladders still push **1.9M SOL** a quarter into the classified float, and unlike a coin whose unlocked tokens sit in a foundation wallet, the vast majority of Solana's actually walk — **88%** for the vesting programme, **100%** for the estate ladder. That is the half of the SOL supply story a pure issuance model misses entirely.

## What to watch in the next 90 days

First and largest: a **875K SOL** lockup cliff vests on **Aug 30 2026** in a single account belonging to the escrow that has never drawn a coin. It is not booked as a sell, and whether it moves is the single biggest swing factor in the next reading. Second, the monthly vesting tranches land on **Sep 7 2026**, **Oct 7 2026** and **Nov 7 2026** at about **635K SOL** each; the forward row assumes they keep realising at **88%**. Third, the estate ladder fires on **Sep 11 2026**, **Oct 11 2026** and **Nov 11 2026** at about **202K SOL**.

Fourth, and the one that would change the shape of the curve: Solana validators voted on **Aug 28 2026** to double the disinflation rate from **15%** to **30%** a year, which would pull the terminal **1.5%** floor forward to **2029** and cut roughly **18.9M SOL** of future issuance. It passed with **67.00%** of participating stake, a hair over the two-thirds bar. It has **not activated** — the chain still reports the original taper, the proposal carries no feature key and no activation epoch, and implementation is estimated at months of client coordination — so the framework books nothing for it. The companion proposal, which would have replaced the flat signature fee with a resource-based fee burned in full and lifted daily burns roughly fourteenfold, **failed** to reach the same two-thirds bar. Watch for the activation epoch; that is the moment both the Sell #1 and Buy #2 rows would need re-basing.

## Summary

Solana is an uncapped proof-of-stake Layer-1 whose supply grows about **1.3%** a quarter and whose only removal mechanism recovers under **1%** of what it mints. The issuance half is predictable and shrinking — **3.67%** a year today, decaying **15%** annually toward a **1.5%** floor — but the escrow half is the live risk: **19.6M SOL** is still under lockup on a monthly calendar running to **2028**, and the chain shows those tranches genuinely emptying rather than re-locking. The upside case is the **Aug 28 2026** vote to double disinflation, which would materially bend the mint if it ever reaches an activation epoch; the ceiling, for now, is that there is no ceiling at all.

---

*MrNasdog Pressure Framework analysis of SOL, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 29 2026.*

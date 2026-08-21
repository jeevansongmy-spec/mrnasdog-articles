---
title:         "SOL Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description:   "SOL runs +1.36% net new supply over 90 days: 3.69% staking issuance plus 2.29M SOL of realised stake-lockup and estate unlocks, against a burn of only 67.8K SOL."
canonical_url: "https://mrnasdog.com/research/sol/inflation"
tags:          ["crypto", "sol", "solana", "layer1"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/sol/inflation](https://mrnasdog.com/research/sol/inflation)*

# SOL Inflation Analysis · August 2026 · Supply growing, projected to keep growing

Solana (SOL) added **+1.36%** to its tradable supply over the last 90 days and is projected to add **+1.33%** over the next 90. Two engines drive it: staking issuance of **5.72M SOL**, minted on a disinflation curve that has already walked the Solana mint rate from 8% at launch down to **3.69%** a year, and **2.29M SOL** that genuinely left Solana's stake lockup ladders and the FTX bankruptcy estate. The only thing pulling the other way is a base-fee burn of **67.8K SOL** — under 1% of the mint. Solana has no cap and no buyback, so the ceiling on SOL supply is a falling issuance curve, not a fixed number.

## The verdict, in one paragraph

Over the 90 days to **Aug 21 2026**, the Pressure Framework reads Solana at **+1.36%** net new supply — **8.01M SOL** of sell pressure against **67.8K SOL** of buy pressure, on a circulating float of **583.1M SOL**. The independent supply monitor reads **+0.918%** over the same window, a gap of **0.44** percentage points, which sits inside tolerance, so no data conflict is flagged on the SOL overview. The residual is explained on-chain rather than assumed: part of Solana's issuance accrues to stake that is classified as non-circulating, so it is minted but never lands in the float the monitor measures. The cite-able label for SOL today is **structurally inflationary on a falling curve** — Solana's supply growth is real and above 1% a quarter, but every year the mint rate is 15% smaller than the year before.

## Sell pressure: where new SOL comes from

Solana's protocol inflation is the largest line at **5.72M SOL** over 90 days. New SOL is minted every epoch and paid entirely to validators and their delegators — the foundation share of Solana issuance is zero. The curve is the one Solana launched with and it is intact: an 8% starting rate, a 15% taper each year, and a 1.5% terminal floor. Read straight off the chain, the Solana mint rate fell from **3.84%** a year at the start of the window to **3.69%** at the end, and is on track for **3.55%** ninety days from now. Because the observed rate lands exactly on the launch curve, no emission change has activated on Solana.

Vesting unlocks contributed **1.68M SOL**. Solana's remaining vesting sits in on-chain stake accounts with a lockup date, and the ladders release one tranche a month of roughly **634K SOL**. Three tranches came due inside the window, worth **1.90M SOL** in total. Reading those accounts at both ends of the window shows **220K SOL** still sitting untouched, so the realised release was **1.68M SOL** — about 89% of the calendar. This overturns the previous reading of Solana's unlock behaviour, which measured the non-circulating pool in aggregate and concluded the cliffs never reach the market. Per stake account, they plainly do. The one genuine exception is a single **1.38M SOL** cliff that came due **Aug 1 2026** and has not moved.

The bankruptcy line — Solana stake held by the FTX estate — contributed **0.61M SOL**. The estate holds a ladder of monthly stake tranches of about **202K SOL** each. Three came due inside the window and every one of them reads zero today; the **Aug 11 2026** tranche was unstaked and moved to a custody wallet for creditor payouts. The estate still has **2.63M SOL** laddered out to **Sep 11 2027**. The foundation and unscheduled-unlock line is **0** — Solana's reserve stake did not release anything into the market during the window, and enumeration rather than projection is the right treatment for it.

## Buy pressure: where new SOL goes

Solana has exactly one supply sink, and it is small. Half of every base transaction fee is destroyed, which worked out to **67.8K SOL** over the 90 days, or about **754 SOL** a day. Reading whole Solana blocks at both ends of the window confirms the split precisely: the burn equals 2,500 lamports times the number of signatures in the block, and priority fees and validator tips go to the block producer in full rather than being burned. That change was already live before this window opened, so the trailing burn rate is the honest forward estimate.

The other three buy lines are **0**. Solana runs no programmatic buyback — staking rewards are minted fresh, never purchased on the market, so there is no contract bidding for SOL. No foundation open-market buying is disclosed or visible on chain. And there is no new long-term lock with a stated size: listed treasury companies hold roughly **11M SOL** between them and stake most of it, but that is ordinary buying rather than a lock the Solana protocol enforces, so the framework does not book it. Net of everything, the SOL burn offsets about 0.8% of the SOL mint.

## Foundation and overhang

Three team-controlled overhangs are tracked on Solana. The largest is **29.85M SOL** of reserve stake that carries no lockup date at all — nothing on chain restrains it, and only classification holds it out of the float. Second is the vested-but-unmoved remainder, **1.68M SOL** that sat in place after its lock ran out, dominated by that **1.38M SOL** cliff from **Aug 1 2026**. Third is the still-locked schedule: **19.60M SOL** with a future unlock date, of which **2.63M SOL** belongs to the FTX bankruptcy estate and the rest runs out to **Mar 2028**.

All three are read from the Solana stake program directly, refreshed each rebuild. If any of these balances falls between refreshes, the outflow enters the foundation and unscheduled-unlock line at the next refresh rather than being back-filled from a schedule. That is the whole point of measuring the escrow instead of the calendar: on Solana the two numbers disagree, and this window they disagreed by **1.68M SOL**.

## How SOL compares to other uncapped proof-of-stake chains

Solana sits in the same structural family as the other uncapped proof-of-stake Layer-1s, but its curve is unusually specific. Where a halving-model chain like Bitcoin has a hard cap and a step-function subsidy cut, and where a fee-burn chain like Ethereum can swing between net issuance and net burn depending on demand, Solana's SOL issuance is a smooth, pre-committed decay: 15% smaller every year until it reaches 1.5%. Nothing about usage changes it. That makes SOL supply growth more predictable than a burn-dependent chain and less predictable than a capped one — you always know the mint rate, but you never get a ceiling.

The comparison that matters most is fee burn versus mint. Ethereum's burn can and does exceed its issuance in busy periods because the whole base fee is destroyed. On Solana only half of the base fee burns, and the base fee is a flat charge per signature rather than a congestion price, so the burn barely responds to demand — **67.8K SOL** against **5.72M SOL** minted. Solana's validators capture the congestion revenue instead, through priority fees paid to them in full. That is a deliberate design choice favouring validator economics over SOL scarcity, and it is exactly what the current governance package is trying to change.

On the unlock side, Solana looks more like a post-bankruptcy asset than like a typical Layer-1. Most large chains finished investor vesting years ago; Solana still has **19.60M SOL** under lockup, and a meaningful slice of it belongs to a bankruptcy estate that sells on a fixed monthly rhythm rather than on price. The offsetting detail is who buys the locked SOL: treasury companies have been acquiring locked-stake tranches at a discount and holding them, which is why so much of the released supply moves without visibly hitting order books.

## What to watch in the next 90 days

The stake-weighted vote on Solana's faster-disinflation and fee-burn package runs to **Aug 29 2026**; if it passes, the taper doubles from 15% to 30% a year and the SOL base fee is replaced by a resource fee that is burned in full, taking the burn from roughly 650 SOL a day toward 7,500–9,000. That single vote is the biggest available swing in this reading. Second, a **875K SOL** lockup cliff comes due on **Aug 30 2026** — a one-off, larger than any monthly tranche. Third, the monthly vesting tranches land on **Sep 7 2026** and **Oct 7 2026** at roughly 634K SOL each; whether they drain as fast as the last three is the test of this build's central finding. Fourth, the FTX estate tranche on **Sep 11 2026** is worth about 202K SOL and has fired on schedule every month. Finally, watch the **1.38M SOL** that vested **Aug 1 2026** and has still not moved — if it goes, it lands in the ledger the moment it does.

## Summary

The MrNasdog Pressure Framework reads Solana at **+1.36%** net new SOL supply over the last 90 days and **+1.33%** projected over the next 90, against a monitor reading of **+0.918%**. The structural mechanism is a pre-committed disinflation curve that shrinks Solana's mint 15% a year toward a 1.5% floor, paired with a base-fee burn far too small to offset it and no buyback at all. The key risk is the unlock side rather than the mint: **19.60M SOL** remains locked to **Mar 2028** and, contrary to the previous reading, the ladders do empty — about 89% of each vesting tranche and 100% of the FTX estate ladder left the escrow this window. There is no supply cap on SOL; the only ceiling is a curve that gets smaller every year, and a governance vote closing **Aug 29 2026** could make it shrink twice as fast.

---

*MrNasdog Pressure Framework analysis of SOL, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 21 2026.*

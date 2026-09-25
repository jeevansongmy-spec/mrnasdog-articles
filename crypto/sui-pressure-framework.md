---
title: "SUI Inflation Analysis · September 2026 · Supply growing, projected to keep growing"
description: "SUI supply is growing at +1.64% net over 90 days: a staking subsidy and monthly unlocks added 66.99M SUI and nothing is burned. Forward reading +1.53% net."
canonical_url: "https://mrnasdog.com/research/sui/inflation"
tags: ["crypto", "sui", "layer1", "vesting"]
published: true
---

> Originally published at **[mrnasdog.com/research/sui/inflation](https://mrnasdog.com/research/sui/inflation)** by MrNasdog.

# SUI Inflation Analysis · September 2026 · Supply growing, projected to keep growing

SUI, the native coin of the Sui layer-1, was created in full at launch — **10B SUI**, with no mint and no burn — so every change in SUI supply is a release of coins that already exist. Two mechanisms release them: a staking subsidy paid out every day that came to **26.01M SUI** over the last 90 days, and monthly Sui unlocks to early contributors, the community reserve and the Mysten Labs treasury that added **40.98M SUI**. Nothing is removed, so the MrNasdog Pressure Framework reads SUI at **+1.64% net** over the last 90 days against a supply-monitor reading of **+1.67%** — a gap of **0.03 percentage points**, which is agreement, not conflict. With **4.10B SUI** circulating out of 10B, SUI has more than half of its supply still to release.

## The verdict, in one paragraph

For the 90-day window ending **Sep 25 2026**, the Pressure Framework reads **SUI at +1.64% net**: **66.99M SUI** entered circulation through the Sui staking subsidy and the monthly unlocks, and **zero** SUI left it. The independent supply monitor reads the realised 90-day change at **+1.67%**. The gap is **0.03 percentage points**, far inside the framework's half-point tolerance, so SUI ships with **no data-conflict flag**. The forward column reads **+1.53%**, a little softer, because the Sui staking subsidy is cut by 10% on **Oct 14 2026** and each monthly unlock is slightly smaller than the one before. The label for SUI is **structurally inflationary by scheduled release**: a fixed-supply chain whose float grows every day and every month as pre-made coins are unlocked, with no burn to offset them.

## Sell pressure: where new SUI comes from

Sell #1, protocol inflation, is the Sui staking subsidy: **26.01M SUI** over the window. It is not minted. At launch a fund was set aside to top up validator and staker rewards while fees are small, and every Sui epoch — one per day — the protocol pays a fixed amount out of it. The project itself says each payout increases circulating supply, which is why the framework books it. The fund was read from the chain at both ends of the window: it held **260.15M SUI** at the start and **234.13M SUI** at the end, and the fall matches the sum of the 90 payouts to the last fraction of a coin. The amount paid each day steps down 10% every 90 epochs. It paid **313,811 SUI** a day until **Jul 16 2026**, **282,430** since, and drops to **254,187** on **Oct 14 2026**, which is why the next 90 days pay less, about **23.41M SUI**.

Sell #2, vesting unlocks, is **22.77M SUI** — the early-contributor tranches released on the first of each month: about **7.65M SUI** on Jul 1 and Aug 1 and **7.46M SUI** on **Sep 1 2026**. Locked SUI is held by outside custodians rather than in an on-chain lock contract, so there is no escrow to read; the published Sui token schedule is what the market counts, and the circulating figure rose by exactly those steps. Sell #3, foundation and unscheduled unlocks, is **18.21M SUI**: the same monthly unlocks free **4.00M SUI** from the community reserve and **2.07M SUI** from the Mysten Labs treasury, three times in the window. Sell #4, long-term locked or bankruptcy supply, is **zero**: no estate distributes SUI and no long-dated lock is unwinding. A listed company holds a large SUI treasury, but it is a separate firm that bought its coins, and none of its transfer limits end in the next 90 days. Together the four rows add **66.99M SUI**, well inside the **5.90B SUI** that sits outside circulation today.

## Buy pressure: where new SUI goes

Nowhere, and that is the other half of the SUI story. Buy #1, programmatic buyback, is **zero** even though a Sui buyback exists: the Sui Foundation buys SUI every day with yield earned on stablecoin reserves, about **726K SUI** for roughly **$539K** across this window. The foundation does not burn or hold that SUI — it hands the coins back out to apps, validators and partners, and says total supply is unchanged — so the buyback supports price without taking anything off the market.

Buy #2, protocol fee burn, is **zero** because Sui has no burn. Computation fees are paid to validators and stakers, and storage fees go into a storage fund that refunds most of them when data is deleted. A small non-refundable part stays in that fund — about **150K SUI** this window — but the fund is still inside the counted float, so it removes nothing. Both supply surfaces were checked: total SUI supply read exactly 10B at both ends, and the Sui framework code has no mint or burn path left after launch. Buy #3, foundation buying, is **zero** beyond the buyback that is handed back out. Buy #4, new long-term locks, is **zero**: no new SUI lockup with a stated size appeared, and staked SUI stays inside the circulating count.

## Foundation and overhang

The SUI overhang is large and mostly known. The Sui token schedule still has about **686M SUI** to release month by month through May 2030, and a further **5.22B SUI** is allocated with no release dates at all beyond 2030 — together the **5.90B SUI** outside circulation today, most of it in the community reserve the Sui Foundation manages. The staking-subsidy fund, now **234.13M SUI**, is the one piece readable on-chain, so it is re-read from the chain every refresh; the custodial tranches are checked against the published schedule every two weeks. The buyback is watched as well, although by design it holds no pile. If any of these balances falls faster than its published schedule between refreshes, the outflow enters Sell #3 at the next refresh.

## How SUI compares to other proof-of-stake layer-1 chains

SUI sits in the class of proof-of-stake layer-1 chains that created their whole supply at launch and pay validators out of a pre-made fund, rather than minting new coins forever. That makes SUI different from an uncapped proof-of-stake chain, whose staking rewards are freshly minted and whose supply has no cap: SUI supply can never pass 10B, and the Sui staking subsidy shrinks by a tenth every quarter until it runs out. The trade-off is timing. An uncapped chain spreads its dilution evenly over decades; SUI front-loads it, with **59%** of all SUI still outside circulation and a monthly unlock calendar that keeps releasing it.

Against chains that burn part of every fee, SUI has no offset at all. A fee burn lets heavy usage cancel some issuance; Sui routes fees to validators and to the storage fund instead, so busier blocks never slow SUI supply growth. The Sui fee base is also small next to the subsidy — gas fees came to about **223K SUI** over the window, under 1% of the **26.01M SUI** the subsidy paid — and the network cut its reference gas price about five times in April 2026. The buyback is the closest thing to a sink, and it is built to recycle SUI rather than remove it.

## What to watch in the next 90 days

The **Oct 1 2026** Sui unlock is the next dated release, about **13.26M SUI** across early contributors, the community reserve and the Mysten Labs treasury. On **Oct 14 2026** the staking subsidy falls 10%, to about **254,187 SUI** a day, the step that pulls the forward reading down. The **Nov 1 2026** and **Dec 1 2026** unlocks follow at about **13.15M** and **12.97M SUI**. Last, the buyback: it hands its coins back out today, and a switch to burning or holding them would open the first non-zero buy row SUI has had.

## Summary

The MrNasdog Pressure Framework reads SUI at **+1.64% net** over the trailing 90 days and **+1.53%** over the next 90, with a buy side that is zero on every row. The structural mechanism is a fixed **10B SUI** supply released on a schedule — a staking subsidy paid every day that shrinks every quarter plus monthly unlocks — with no burn to offset it, while the Sui Foundation's buyback recycles its coins instead of removing them. The key risk is the size of what is still to come: **5.90B SUI** sits outside circulation, and **5.22B** of it has no published dates. The cap is hard — SUI supply can never pass 10B — but SUI will keep growing toward it for years.

---

*MrNasdog Pressure Framework analysis of SUI, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 25 2026.*

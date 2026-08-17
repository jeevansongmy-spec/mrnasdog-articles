---
title: "CFG Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description: "A MrNasdog Pressure Framework read of Centrifuge (CFG): an immutable contract mints 3% a year, 12.74M CFG reached the market in 90 days for +3.33% net, +2.52% forward, with zero buyback or burn."
canonical_url: "https://mrnasdog.com/research/cfg/inflation"
tags: ["crypto", "cfg", "centrifuge", "rwa"]
published: true
---

> Originally published at **[mrnasdog.com/research/cfg/inflation](https://mrnasdog.com/research/cfg/inflation)** by MrNasdog.

# CFG Inflation Analysis · August 2026 · Supply growing, projected to keep growing

Centrifuge's CFG is an Ethereum-native governance token whose issuance is written into a contract nobody can amend: about **3% a year**, minted weekly, compounding on the whole supply. The Pressure Framework reads **+3.33% net** supply growth over the last 90 days — roughly **12.74M CFG** reaching outside hands against a tradable base of **380.38M** — and projects **+2.52%** forward, with a buy side of effectively **zero**: no buyback, no fee burn, no treasury accumulation. Our monitor reads **−34.33%** for the same window, a gap of about **38 percentage points** that is a counting change rather than a sell, so a ⚠ chip ships.

## The verdict, in one paragraph

For the 90 days to **Aug 17 2026** the framework reads Centrifuge at **+3.33%** net supply growth and projects **+2.52%** for the next 90 days. Our monitor reads **−34.33%**, a gap of about **38 percentage points**, which triggers the ⚠ chip. The deep walk settles it without ambiguity. The monitor's own day-by-day record drops from **577.5M** tracked supply on **Jun 8 2026** to **379.3M** on **Jun 9 2026** — a one-day step of roughly 198M tokens, with no burn of that size anywhere on Ethereum. The chain says the opposite: total CFG supply rose from **632.0M** on **May 19 2026** to **700.3M** on **Aug 17 2026**, read at both ends on three independent archive nodes. What changed was the definition, not the supply — the tracked count was re-based onto Centrifuge's own published released-supply figure of 54.6%, about **380.4M**, and that step ages out of the 90-day window around **Sep 7 2026**. CFG is **structurally inflationary on the active float**: a hard-coded mint with no offsetting sink.

## Sell pressure: where new CFG comes from

**Protocol inflation** is the backbone of the CFG ledger at **8.28M CFG** over the window and about **5.12M** forward. Centrifuge runs a dedicated inflation minter contract on Ethereum whose parameters are immutable — a seven-day period and a per-period rate that compounds to **2.998% a year** on total supply — so the widely quoted "3% inflation" is not a policy Centrifuge chooses each quarter, it is literally compiled into the contract. Two mints landed inside the window, on **Jun 4 2026** and **Aug 3 2026**, and every newly minted CFG is paid into the Centrifuge Treasury first. That treasury is a full pass-through: over the same 90 days it received about 38.3M CFG and paid out about 46.5M, so the mint is booked as reaching the market rather than parked. Two governance threads, on **Jul 28 2026** and **Aug 15 2026**, argue for cutting the rate; neither has been put to a vote, so the emission schedule stands.

**Vesting unlocks** book at **zero**, and the reason is opacity rather than absence. Centrifuge publishes three vesting streams — the team's 12% allocation through **May 2030**, the CP149 incentive tranche of 100M CFG vesting linearly through **Apr 2029**, and an investor remainder running 22 months to **Mar 2028** — but none of them carries a dated cliff calendar with quanta, and the CP149 tranche vests into the Centrifuge Treasury rather than onto the market, which makes it an internal transfer. The one vesting aggregator with a CFG page publishes a visibly broken table, so no second source exists to triangulate against. The framework therefore reads what actually left the project's wallets on-chain instead of a schedule, and that flow is already carried in the inflation and Foundation rows.

**Foundation and unscheduled unlocks** add **4.45M CFG**: the portion of the outflow that came from balances Centrifuge already held rather than from the new mint. Payments were lumpy but never stopped — about 7.82M CFG in June, 1.34M in July and 3.62M in the first 17 days of August, most recently **3.57M on Aug 13 2026**. **Long-term locked or bankruptcy** is **zero**: Centrifuge has no bankruptcy estate, and the one route that could have produced a supply backlog — converting legacy chain CFG and wrapped WCFG into the current token — closed permanently on **Apr 10 2026**, so no further legacy CFG can ever appear.

## Buy pressure: where new CFG goes

The buy side of the Centrifuge ledger is almost entirely empty, and that is the structural point about CFG. **Programmatic buyback** is **zero**: a governance proposal to route protocol revenue toward the token was rejected, the follow-up fee discussion from **Feb 2026** never reached a vote, and no contract anywhere buys CFG. **Protocol fee burn** is **zero**: fees on Centrifuge's tokenized-asset products are paid in the assets themselves and in ETH, and none of them destroy CFG. **Foundation buy** is **zero** — the treasury is funded by minting, so it has no reason to buy on the open market, and no purchase was observed.

**New long-term lock** is also **zero**, despite an eye-catching 33.75M CFG now sitting in a governance proxy contract. That CFG came out of Centrifuge's own reserve rather than the tradable float, so locking it removes nothing from the market, and the contract itself is a permissioned executor with no time lock and no release schedule — it can send the balance out at any moment. It is tracked as overhang, not credited as absorption. The only genuine reduction was **0.08M CFG** burned as the migration helper settled its last claims, ending **Jun 4 2026** — bookkeeping from a finished process, contributing nothing forward.

## Foundation and overhang

Three Centrifuge-controlled pools sit behind the tradable float and are refreshed from the chain on every rebuild. The reserve wallet holds about **128.07M CFG**, roughly a third of the entire tradable supply, and it grew during the window because a post-migration reconciliation mint of **59.81M CFG** landed there on **Jun 4 2026** — supply that was created but never entered the float. The Centrifuge Treasury wallet, the destination of every inflation mint, holds only about **1.69M CFG** because it spends almost everything it receives. The governance proxy holds **33.75M CFG** under a permissioned executor with no lock. None of these has a published release schedule, which is precisely why they are enumerated rather than projected. If any of these balances falls to an outside address between refreshes, the outflow enters the Foundation row at the next refresh.

## How CFG compares to other real-world-asset tokens

The structural class CFG belongs to is governance tokens attached to real-world-asset credit protocols, and the comparison that matters is mechanism, not price. The strongest tokens in that class close the loop: protocol revenue is routed back into the token through a buyback or a burn, so growth in assets under management shows up as demand for the token. Centrifuge has built the revenue side — tokenized Treasury and credit products, with institutional partners arriving through 2026 — but has never connected it to CFG. Fees are earned in the assets and in ETH; nothing flows back.

Against fixed-supply and burn-driven designs the contrast is sharper still. A capped token with a fee burn shrinks its float as usage grows. CFG has no cap at all, and its issuance is the reverse of usage-linked: the inflation minter pays out the same 3% a year whether Centrifuge finances one billion dollars of assets or none. Compared with the chains whose emissions at least buy something — validator security, block production — CFG pays for nothing structural, because after the migration to Ethereum there are no collators to fund and no staking to reward. That is the substance of the complaint raised in the governance forum in **Jul 2026** and again in **Aug 2026**: a governance-only token carrying an emission schedule designed for a chain that no longer exists.

## What to watch in the next 90 days

First, whether either inflation thread — the proposal of **Jul 28 2026** or the follow-up of **Aug 15 2026** — is converted into a formal vote; a rate cut would be the single largest change available to this ledger. Second, the reserve wallet holding **128.07M CFG**, whose drawdown pace sets the Foundation row entirely. Third, the governance proxy holding **33.75M CFG**, which can move without notice and would land in the sell ledger if it did. Fourth, any move to connect protocol fees to CFG, which is the only path to a non-zero buy side. Fifth, around **Sep 7 2026**, the one-day counting step of **Jun 9 2026** rolls out of the trailing 90-day window, at which point our monitor should stop reading a false −34% and converge back toward the framework.

## Summary

The MrNasdog Pressure Framework reads Centrifuge's CFG at **+3.33%** net supply growth over the 90 days to **Aug 17 2026** and projects **+2.52%** forward — structurally inflationary on the active float, with a buy side of effectively zero. The mechanism is unusually clean to describe: an immutable contract mints about **3% a year** into the Centrifuge Treasury, the treasury spends it, and nothing anywhere buys or burns CFG back. The key risk is the overhang rather than the mint — **128.07M CFG** in a reserve wallet and **33.75M** in an unlocked governance proxy together exceed 40% of the tradable float and carry no published release schedule. There is no cap and no ceiling: CFG supply grows indefinitely until governance changes the rate, and as of **Aug 17 2026** no vote to do so has been called.

---

*MrNasdog Pressure Framework analysis of CFG, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 17 2026.*

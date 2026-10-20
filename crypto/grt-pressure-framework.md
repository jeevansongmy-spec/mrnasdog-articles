---
title:         "GRT Inflation Analysis · October 2026 · Supply growing · projected to keep growing"
description:   "GRT is inflationary: 74.66M newly minted GRT plus a 38.75M Foundation unlock against a 63.2K burn give +1.04% over 90 days, about +1.07% next. No cap."
canonical_url: "https://mrnasdog.com/research/grt/inflation"
tags:          ["crypto", "grt", "the-graph", "infrastructure"]
published:     true
---
Originally published at [GRT Inflation Analysis · October 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/grt/inflation).

# GRT Inflation Analysis · October 2026 · Supply growing · projected to keep growing

<!-- main-page -->
➜ Start with the The Graph coin page for the short answer (should you buy GRT?) and its price drivers: [mrnasdog.com/research/grt](https://mrnasdog.com/research/grt)

GRT is inflationary: The Graph added about **1.04%** to the circulating supply in the last 90 days, and the next 90 days project about **1.07%**. Two streams feed it. The protocol mints **120.73 GRT** for every Ethereum block (**74.66M GRT** in 90 days), and the Foundation's vesting lock releases **12.92M GRT** a month (**38.75M** in 90 days). Against that, the protocol burned only **63.2K GRT**, and GRT has no supply cap.

## The verdict, in one paragraph

Our ledger puts GRT at **+1.04%** net over the last 90 days (Jul 21 to Oct 19 2026) and **+1.07%** over the next 90. The inflation monitor reads **+1.31%** for the same 90 days, a gap of **0.27 percentage points**, so the two readings agree and the coin page carries no warning note. The monitor's circulating figure took one step up on Aug 19 2026 and has held flat since; on-chain, new GRT arrived every day of the window. Put simply, GRT is **inflationary by design**: new coins pay the people who run the network, and the burn is too small to matter.

## Sell pressure: where new GRT comes from

Protocol inflation is the biggest source. The Graph mints new GRT on Arbitrum at a fixed **120.73 GRT per Ethereum block**, about **866,000 GRT a day** and roughly 3% of supply a year. In the 90 days to Oct 19 2026 the chain shows **74.66M GRT** minted: **63.34M** paid out as indexing rewards to the indexers and delegators who serve data, **8.18M** sent to the Foundation's new Innovation Allocation, and **3.13M** held back from indexers that missed the new service standard. The minting rate itself did not change in the window; what changed on Sep 1 2026 is where it goes, because GIP-0089 now sends 20% of every block's new GRT (24.146 GRT) to the Foundation. For the next 90 days we project the full rate of about **77.93M GRT**, since the Innovation share is minted every block and indexers have been collecting their rewards closer to the full amount since September.

Vesting unlocks are the second source. The Graph Foundation's allocation sits in an on-chain vesting lock of **1.55B GRT** that opens in 120 equal monthly slices of **12.92M GRT**, from Dec 17 2020 to Dec 17 2030. Three slices left the lock in this window, on Jul 24, Aug 25 and Sep 23 2026, for **38.75M GRT**; each one was passed on to another Foundation wallet within a day. The lock still holds **658.75M GRT**. The next 90 days carry three more slices: the Oct 18 2026 slice, already open and waiting to be claimed, then Nov 17 and Dec 17 2026, another **38.75M GRT**.

Foundation and unscheduled unlocks add **0** on top of that, because the Foundation's other wallets already count as circulating and their new coins are inside the mint figure above. Long-term locks and bankruptcy add **0**: there is no estate or trustee holding GRT, and the early team, investor and Edge & Node allocations finished vesting by Dec 2025.

## Buy pressure: where new GRT goes

GRT has no programmatic buyback, so that row is **0**. A community member asked on the forum on Sep 5 2026 for part of protocol revenue to buy and burn GRT, but there is no formal proposal or vote behind it yet.

The protocol fee burn is real but tiny. A small tax on query payments destroyed **39,432 GRT** in the 90 days, a tax on curation destroyed **23,526 GRT**, and **259 GRT** was sent to dead addresses, for **63.2K GRT** in total. That is less than a tenth of one percent of the new GRT minted over the same days. We project the same burn for the next 90 days; more query traffic moving onto the network since Oct 8 2026 could lift it, but not by enough to change the picture.

Foundation buying is **0**: the Foundation receives and spends GRT, and nothing in the window shows it or any treasury buying. New long-term locks are also **0**. About **1.93B GRT** is staked by indexers and delegators, down from 2.09B at the start of the window, but staked GRT still counts as circulating, so staking takes nothing out of the float.

## Foundation and overhang

The largest team-controlled overhang is the Foundation vesting lock itself: **658.75M GRT** on Oct 19 2026, down from 697.5M on Jul 21 2026, releasing 12.92M every month until Dec 17 2030. It is the only team supply still outside the circulating count, and its monthly slices are already booked in the vesting row. The Foundation's Innovation Allocation received **8.18M GRT** of new coins since Sep 1 2026 and has paid out **6.96M**, leaving **1.22M**. A separate wallet holds **3.13M GRT** of rewards withheld from indexers that missed the service standard, and nothing has left it yet. The Foundation wallet that receives each monthly slice holds only about 150,000 GRT, because the slices pass straight through.

We read these wallets on-chain at every rebuild. If any of their balances falls between rebuilds, the outflow goes into Sell #3 at the next refresh.

## How GRT compares to other data and infrastructure networks

GRT belongs to the group of work tokens that pay the network's operators in newly minted coins. Like Ethereum's validator issuance or Filecoin's block rewards, the new GRT goes to the people who do the work, here the indexers who serve blockchain data, and their delegators. The difference is size and offset: Ethereum burns part of every fee and Filecoin burns network fees, while The Graph's fee burn is a rounding error next to its minting. GRT's net growth is close to its gross growth.

Against oracle and data tokens with a fixed cap, the contrast is sharper. A capped token can only grow its float by releasing coins that already exist; GRT both mints new coins with no cap and still releases a Foundation allocation every month until 2030. The monthly vesting slice is predictable and dated, which makes it easier to plan around than a discretionary treasury sale, but it adds about **0.35%** to the float every quarter on its own.

Inside its own design, GRT's weak spot is that demand for the token comes from staking, delegation and curation, while query fees are paid in small amounts and only a sliver is burned. Until the network's fee income grows by many times, issuance sets the direction of supply.

## What to watch in the next 90 days

The Foundation's monthly slices: the Oct 18 2026 slice is waiting to be claimed, and the next slices open on **Nov 17 2026** and **Dec 17 2026**, each **12.92M GRT**; the one after that falls on Jan 17 2027, just past this window.

GIP-0090, posted on Sep 23 2026, would send 0.1% of each block's new GRT to a community support group for twelve months; it moves coins inside the same 120.73 GRT a block, so it would not change the total.

Query fees and burns after Oct 8 2026, when Subgraph Studio traffic for BNB Smart Chain and Polygon began moving onto the network; more paid queries means a slightly larger tax burn.

Any proposal that changes the 120.73 GRT a block, or that turns the Sep 5 2026 request for revenue-funded burns into a real vote, would move the forward reading more than anything else on this list.

The Innovation Allocation and the reclaimed-rewards wallet, which together hold about **4.35M GRT**; any large payout from them would show up as Foundation spending.

## Summary

GRT, the token of The Graph, is inflationary: supply grew about **1.04%** in the 90 days to Oct 19 2026 and is projected to grow about **1.07%** in the next 90. The growth comes from a fixed mint of **120.73 GRT** per Ethereum block, now split 80% to indexing rewards and 20% to the Foundation, plus a **12.92M GRT** monthly Foundation unlock that runs until Dec 17 2030. The burn from query and curation taxes, **63.2K GRT** in 90 days, removes almost nothing, and nothing buys GRT back. With no supply cap and **658.75M GRT** still in the Foundation lock, the key risk is steady new supply meeting thin fee income.

---

*MrNasDog Pressure Framework analysis of GRT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Oct 19 2026.*

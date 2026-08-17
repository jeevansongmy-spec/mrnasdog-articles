---
title:         "BCH Inflation Analysis · August 2026 · Mixed flows, supply roughly steady"
description:   "Mixed flows, supply roughly steady: Bitcoin Cash mined 40.0K BCH in 90 days with no buyback and no burn. Framework net +0.20%, monitor +0.21%, gap 0.01pp."
canonical_url: "https://mrnasdog.com/research/bch/inflation"
tags:          ["crypto", "bch", "bitcoincash", "proofofwork"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/bch/inflation](https://mrnasdog.com/research/bch/inflation)*

# BCH Inflation Analysis · August 2026 · Mixed flows, supply roughly steady

Bitcoin Cash has the simplest supply story the Pressure Framework tracks: mining is the only thing that creates a BCH, and nothing at all destroys one. Over the last 90 days the Bitcoin Cash chain minted **40.0K BCH** from **12,790** blocks at a **3.125 BCH** subsidy, against zero buyback, zero burn and zero new locked supply — a net **+0.20%** of circulating supply reaching the market, versus **+0.21%** on the inflation monitor. With roughly **96%** of the **21M** hard cap already mined and the next halving not due until around **Apr 2028**, that figure is about as low as a chain that removes nothing can go.

## The verdict, in one paragraph

The framework reads Bitcoin Cash at **+0.20%** net supply growth over the trailing 90 days and projects the same **+0.20%** for the next 90. The inflation monitor independently reads **+0.21%** over the same window, leaving a gap of **0.01** percentage points — far inside tolerance, so no data-conflict chip is raised on the BCH overview. That agreement is expected here, because there is only one supply mechanism to disagree about: the coinbase subsidy. Bitcoin Cash is a **quiet, capped proof-of-work chain** whose entire monetary policy is a fixed halving schedule inherited from Bitcoin and never amended in nine years.

## Sell pressure: where new BCH comes from

There is exactly one source of new BCH, and it is Sell #1, protocol inflation. Miners earned **3.125 BCH** per block for the whole window — the subsidy set by the height-840,000 halving in **Apr 2024** — and the Bitcoin Cash chain produced **12,790** blocks between the two window edges. That is **142.1** blocks a day against the ten-minute target of 144, so the framework books the observed count rather than the nominal one: **40.0K BCH**. Reading the schedule instead of the chain would have claimed 40,500 BCH, about 1.3% too much. Bitcoin Cash shares its hashing algorithm with Bitcoin, so hashrate migrates on relative profitability and the real block pace drifts around the target — which is why the chain read, not the calendar, governs this row.

Every other sell row is zero, and each is zero for a different reason. Sell #2, vesting unlocks, is zero because there is no vesting schedule anywhere in Bitcoin Cash: the chain launched in **Aug 2017** by copying Bitcoin's ledger one-for-one, so there was no premine, no team allocation and no investor tranche to unlock. Sell #3, foundation and unscheduled unlocks, is zero because no foundation or protocol treasury holds BCH at all — the full block reward goes to the miner, and the 2020 proposal to divert part of the coinbase into developer funding was rejected and never activated on this chain. Sell #4, long-term locked or bankruptcy, is zero for the window: the Mt. Gox rehabilitation estate still owes creditors BCH alongside BTC, but no BCH-denominated estate movement was observed between the window edges and the trustee publishes neither an address nor a remaining quantum.

## Buy pressure: where new BCH goes

Nowhere. All four buy rows read zero, and on Bitcoin Cash that is a design decision rather than an oversight. Buy #1, programmatic buyback, is zero because there is nothing to buy back with — Bitcoin Cash keeps no protocol revenue and holds no treasury, so every satoshi of subsidy and fee leaves the protocol the moment a block is found. Buy #2, protocol fee burn, is zero because Bitcoin Cash never destroys a coin: transaction fees are swept into the coinbase output and paid to the miner, exactly as on Bitcoin, with no base-fee burn in the consensus rules.

Buy #3, foundation buy, is zero because there is no foundation balance sheet to do the buying; Bitcoin Cash upgrades move through an open proposal process supported by voluntary donations. Buy #4, new long-term lock, is zero because Bitcoin Cash is pure proof-of-work — there is no staking, no bonding and no lockup contract, so holders have no protocol-level way to take coins off the tradable float. The practical consequence is that the framework's BCH reading can never be negative while the subsidy is still paying. The floor is the halving schedule, not a burn.

## Foundation and overhang

Bitcoin Cash has almost nothing to enumerate here, which is itself the finding. There is no foundation treasury, no labs entity, no DAO treasury, no buyback accumulation wallet and no identified team multisig — a fair-launch fork inherits no cap table. The single tracked overhang is a bankruptcy-estate residual: the **Mt. Gox** rehabilitation estate, whose court-approved plan repays creditors in fiat, BTC and BCH. Public reporting puts the fork-era BCH figure at roughly **143K BCH** with an undisclosed portion already paid out across the **Jul 2024** and **Mar 2025** rounds; the trustee has never published a BCH address or a current balance, so the framework treats the quantum as opaque and books no value.

One nuance matters for reading this overhang correctly: Bitcoin Cash has no non-circulating bucket, so those estate coins are already counted inside circulating supply. A Mt. Gox payout therefore moves float from one holder to another rather than adding new BCH — it can pressure price without touching the inflation reading. The watch line still stands: if the estate's BCH balance falls between refreshes, the outflow enters Sell #4 at the next refresh.

## How BCH compares to other capped proof-of-work chains

Bitcoin Cash belongs to the small class of hard-capped proof-of-work coins whose issuance is a fixed halving curve and whose buy side is empty by construction. Against Bitcoin itself the mechanism is identical — same **21M** cap, same 210,000-block halving interval, same coinbase-to-miner payout — and the two chains halve within months of each other because they share a subsidy schedule and a hashing algorithm. The difference is fee policy at the margin: neither burns fees, but Bitcoin Cash's large blocks and near-zero fee market mean the coinbase is almost entirely subsidy, so its issuance is even more purely a function of block count than Bitcoin's.

The sharper contrast is with the chain that split away from Bitcoin Cash over exactly this question. eCash took the developer-funding path Bitcoin Cash rejected and now diverts a large share of every coinbase to protocol development, ecosystem funding and staking rewards; Bitcoin Cash pays **100%** to the miner. Against uncapped continuous-emission chains — the proof-of-stake layer-1s that mint a percentage of supply every year and then hand it back as staking rewards — Bitcoin Cash's **+0.20%** per quarter is an order of magnitude quieter, and it steps down again rather than resetting. And against exchange tokens with quarterly buybacks, or fee-burning smart-contract chains, Bitcoin Cash simply has no deflationary lever at all: it cannot score at the top of the inflation metric, because a capped-but-flat supply that removes nothing is not a shrinking supply.

## What to watch in the next 90 days

The **Mt. Gox** repayment deadline of **Oct 31 2026** falls inside the window and is the one dated event on the BCH calendar; a large estate distribution would not change the inflation reading but would move float, and any BCH-denominated movement books into Sell #4 at the next refresh. Watch the observed block pace, currently **142.1** a day: because Bitcoin Cash competes for the same hashrate as Bitcoin, a sustained shift toward or away from the chain moves Sell #1 by a few percent without any rule changing. Watch the Bitcoin Cash proposal forum for the 2027 upgrade cycle — the ideas in discussion, including faster blocks and new arithmetic operations, are scripting and block-timing changes rather than issuance changes, but a faster-blocks proposal is the one item that would restate the per-block subsidy even while leaving total issuance intact. And watch the approach to the cap: with roughly **0.92M BCH** left to mine, the next halving around **Apr 2028** will cut the subsidy to **1.5625 BCH** and roughly halve this reading again.

## Summary

The MrNasdog Pressure Framework reads Bitcoin Cash at **+0.20%** net supply growth over the last 90 days and the same over the next 90, matching the inflation monitor's **+0.21%** to within **0.01** percentage points. The mechanism is one line long: **40.0K BCH** of proof-of-work block subsidy, no buyback, no burn, no vesting, no treasury and no staking lock, against a hard **21M** cap that is already about **96%** mined. The key risk is not issuance but distribution — the opaque Mt. Gox estate residual against an **Oct 31 2026** deadline, coins that already sit inside circulating supply and so would pressure price without registering as inflation. The ceiling is the schedule itself: Bitcoin Cash cannot shrink its supply, only slow its growth, and the next step down comes at the **Apr 2028** halving.

---

*MrNasdog Pressure Framework analysis of BCH, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 17 2026.*

---
title:         "XMR Inflation Analysis · August 2026 · Mixed flows · supply roughly steady"
description:   "Monero mined 64,621 blocks in 90 days at a fixed 0.6 XMR reward — 38.8K new coins, +0.21% net, with no buyback, no burn and no unlocks in the ledger."
canonical_url: "https://mrnasdog.com/research/xmr/inflation"
tags:          ["crypto", "xmr", "monero", "privacy"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/xmr/inflation](https://mrnasdog.com/research/xmr/inflation)*

Monero mined **64,621** blocks in the last 90 days, each paying the permanent tail emission of **0.6 XMR** — roughly **38.8K** new XMR, or **+0.21%** of the **18.79M** circulating. Every other row in the Pressure Framework ledger is zero: no vesting unlocks, no foundation allocation, no buyback, no burn. XMR is a fair-launch proof-of-work privacy coin whose supply moves in one direction, very slowly, by protocol rule rather than by anyone's decision.

## The verdict, in one paragraph

For the 90-day window ending **Aug 17 2026**, the MrNasdog Pressure Framework reads Monero at **+0.21% net** — sell pressure of **38.8K XMR** against buy pressure of exactly **zero**. Our supply monitor reads the same window at **+1.93%**, a gap of **1.72 percentage points** that exceeds the framework's tolerance and ships a **monitor-gap chip** on the overview card. The gap is not new coins. At **0.6 XMR** per block Monero can physically mint no more than about **38.8K XMR** in 90 days, yet the monitor booked roughly **356K** — more than nine times what the protocol can produce. The cause is a broken figure in the monitor's own supply history: that history sat pinned near **18.45M XMR**, a placeholder equal to the largest value a 64-bit counter can hold, then jumped to the true supply near **18.77M** in a single day on **May 28 2026**. The 90-day window opens on **May 19 2026**, so that one-day correction still sits inside it and ages out on **Aug 26 2026**. Monero is a **quiet chain with a fixed, permanent, non-discretionary issuance rate**.

## Sell pressure: where new XMR comes from

Sell pressure in Monero has exactly one source, and it is the tail emission. Since the end of May 2022 the block reward has been fixed at **0.6 XMR**, and unlike Bitcoin it never halves and never falls to zero — the tail emission is designed to pay miners forever so the security budget does not depend on transaction fees alone. This build measured the emission rather than assuming it: reading block heights at both ends of the window gives **3,677,179** on **May 19 2026** and **3,741,800** on **Aug 17 2026**, a measured count of **64,621** blocks. That is **718** blocks a day against a two-minute target of 720 — real block spacing drifts with hashrate, and assuming the round number would have overstated issuance. Multiplying the measured count by the fixed reward gives **38.8K** new XMR. Transaction fees are paid to the miner alongside that reward, but fees recycle coins that already exist, so only the **0.6** base counts as new supply.

The other three sell rows are zero, and each is zero for a structural reason. Vesting unlocks are zero because Monero launched openly in April 2014 with no premine, no instamine allocation, no initial coin offering and no team tranche — there is nothing locked, so there is no unlock calendar for any tracker to publish. Foundation and unscheduled unlocks are zero because no premined foundation reserve exists; the only group-controlled pool is the community crowdfunding General Fund, discussed below. Long-term locked or bankruptcy supply is zero because no estate, trustee schedule or court-ordered distribution of XMR exists. In the Pressure Framework's terms, Monero has no discretionary sell pressure at all — nobody can decide to release coins, because nobody is holding any back.

## Buy pressure: where new XMR goes

The Monero buy ledger is empty across all four rows, and this build re-verified each one rather than assuming it. Programmatic buyback is **zero**: Monero keeps no protocol revenue whatsoever — every transaction fee is paid straight to the miner who found the block — so there is no treasury income that could fund open-market buying. Protocol fee burn is **zero**: Monero has no burn mechanism of any kind, so unlike a fee-burning smart-contract chain, no XMR is ever destroyed. Foundation buy is **zero**: the donation-funded General Fund exists to pay contributors in XMR, not to accumulate it. New long-term lock is **zero** because Monero is proof-of-work and has no staking, no bonding, no escrow and no lockup contract that could take coins off the float.

That emptiness is the whole story of the coin's supply profile. There is no mechanism, anywhere in Monero, that removes XMR from circulation. The net figure is therefore identical to the gross emission, and the framework's next-90-day reading of **+0.21%** is simply the tail emission expressed as a percentage of the float. It falls slightly every year on its own, because the numerator is fixed in coins while the denominator keeps growing — roughly **0.84%** a year today, and lower every year after.

## Foundation and overhang

Monero has one identified group-controlled pool and it is unusual: the Community Crowdfunding System General Fund. It is not a premined allocation — it is filled entirely by donations and by money left over from funded proposals, and it pays contributors for approved work. At this walk, four proposals were open on the crowdfunding surface, each seeking between **36** and **120** XMR to pay development work. The General Fund's balance is not published, and because Monero conceals individual balances and amounts by design, it cannot be read from the chain either. It is therefore tracked as an **opaque overhang** at value zero, re-walked on the crowdfunding surface at every rebuild. If a large funded proposal moves and the outflow becomes visible through project disclosure, that outflow enters Sell #3 at the next refresh. Beyond it there is nothing: no foundation treasury of premined XMR, no labs holding, no decentralised-autonomous-organisation treasury, no buyback wallet and no bankruptcy residual. A fair launch leaves no team allocation behind.

## How XMR compares to other privacy and proof-of-work chains

Against Bitcoin, the mechanism difference is the tail. Bitcoin is hard-capped at 21 million with a subsidy that halves roughly every four years and eventually reaches zero, so its issuance rate steps down in jumps and its long-run security budget must come from fees. Monero is uncapped, but its issuance is a flat line: the same **0.6 XMR** per block forever. Uncapped sounds worse and is arithmetically milder — a fixed coin quantum divided by a growing supply produces a rate that falls asymptotically toward zero without ever creating a fee-only security cliff.

Against the other privacy coins, the difference is who gets paid. Zcash is capped and halving like Bitcoin, but a share of its block reward is routed to a development fund, so part of its issuance is a claim held by an organisation rather than by miners. Dash splits its block reward between miners, masternodes and a governance treasury that proposals draw on, so a slice of new supply is spent by vote. Monero routes **100%** of the block reward to whoever mined the block, and funds development from voluntary donations instead. That is why the Pressure Framework's Sell #3 row is zero for Monero and non-zero for treasury-funded peers: there is no protocol-level entity accumulating XMR to spend.

Against fee-burning chains such as Ethereum, Monero has no offsetting buy side at all. A burn chain can turn net-deflationary when activity is high; Monero never can, because its ledger has no burn, no buyback and no lock. Its floor and its ceiling are the same number. That makes Monero the cleanest case in this framework — the reading is arithmetic, not judgment.

## What to watch in the next 90 days

First, the monitor gap should close by itself on **Aug 26 2026**, when the one-day supply correction of **May 28 2026** falls out of the trailing 90-day window; if the gap persists past that date, the upstream feed has a second problem and the next rebuild must re-walk it. Second, the FCMP++ upgrade — full-chain membership proofs — is still in stressnet with no activation height announced; it changes privacy, not issuance, but it is the only hard fork on the horizon and a fork is the only way the tail emission could ever change. Third, watch measured block spacing: this window came in at **718** blocks a day, and a sustained hashrate move would shift issuance by a percent or two either way. Fourth, watch the crowdfunding General Fund for any disclosed large outflow, the only path to a non-zero Sell #3. Fifth, the European Union's privacy-coin restrictions take effect in **July 2027** and further exchange delistings would move where XMR trades — a float-location change, not a supply change, and outside this metric.

## Summary

The MrNasdog Pressure Framework reads Monero at **+0.21%** net supply growth over the last 90 days and the same **+0.21%** projected forward, from **38.8K** newly mined XMR against an entirely empty buy ledger. The structural mechanism is the perpetual tail emission of **0.6 XMR** per block, fixed since May 2022, never halving and set by protocol rather than by any committee. The key risk is not supply at all — issuance is the most predictable number on this page — but access: exchange delistings and the European Union's privacy rules affect where XMR can be traded, not how much of it exists. There is no cap on Monero's supply, and no need for one: because the quantum is fixed in coins while the float grows, the inflation rate falls every single year on its own, and nothing in the protocol can accelerate it.

---

*MrNasdog Pressure Framework analysis of XMR, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 17 2026.*

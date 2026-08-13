---
title:         "DOT Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description:   "Polkadot issues 13.89M DOT per 90 days under its new 2.1B hard cap with every burn switched off — framework reads +0.82% net, monitor +0.47%, gap 0.34pp."
canonical_url: "https://mrnasdog.com/research/dot/inflation"
tags:          ["crypto", "dot", "polkadot", "layer1"]
published:     true
---

> Originally published at **[mrnasdog.com/research/dot/inflation](https://mrnasdog.com/research/dot/inflation)** by MrNasdog.

Polkadot minted about **13.89M DOT** over the last 90 days and is on track for roughly **13.78M** over the next, against **zero** buy-side offset — no buyback, no fee burn, no new lockup. The MrNasdog Pressure Framework reads **+0.82% net** for the trailing window and **+0.81%** forward, while our supply monitor reads **+0.47%**, a gap of **0.34 percentage points** that stays inside tolerance. Polkadot's March 2026 governance reset did two opposite things at once: it wrote a permanent **2.1 billion DOT** hard cap into the protocol and cut issuance **53.6%**, and it switched off every DOT burn the network had.

## The verdict, in one paragraph

Over the last 90 days the MrNasdog Pressure Framework reads Polkadot at **+0.82% net**: about **13.89M DOT** of newly issued supply reaching the market against **0** on the buy side, on a circulating base of **1,697.82M DOT**. Our supply monitor reads the same trailing window at **+0.47%** — a gap of **0.34 percentage points**, inside the framework's tolerance, so this build ships **no monitor-gap chip** and needs no reconciliation walk. Projected forward the framework reads **+0.81%** for the next 90 days. Polkadot is best labelled a **capped chain that still mints, and no longer removes anything** — the dilution is now slow and bounded, but it is entirely one-directional.

## Sell pressure: where new DOT comes from

Sell #1 — protocol inflation — is the whole story on Polkadot, at about **13.89M DOT** realised over the last 90 days and **13.78M DOT** projected for the next. Polkadot is a nominated-proof-of-stake chain, and new DOT is issued every block to pay validators and nominators. What makes DOT unusual is that this rate is not a protocol constant — it is a governance variable, and Polkadot changed it. OpenGov referenda **#1710** and **#1828** shipped runtime **v2.1.0** on **Mar 12 2026** and stepped issuance down on **Mar 14 2026**, cutting annual DOT issuance **53.6%** from roughly **120M** to about **56.88M DOT** a year and writing a permanent hard cap of **2,100,000,000 DOT** into the protocol.

Because that reset landed before this window opened, the figure above is not a model — it is a measurement. Reading Polkadot's total issuance directly on chain at both ends of the window, from **May 15 2026** to **Aug 13 2026**, gives **1,683,928,509 DOT** rising to **1,697,822,137 DOT**: an increase of **13,893,628 DOT** in exactly 90 days, an annual pace of **56.35M DOT**. That sits within **1%** of the published schedule, and the sub-windows inside it decay smoothly rather than stepping, which confirms one Polkadot issuance mechanism ran for the whole period. From here the schedule is biennial: every two years issuance drops a further **13.14%** of the remaining distance to the cap, with the next step due around **Mar 2028**.

The other three sell rows are all **0**. Sell #2, vesting unlocks, is empty because Polkadot has no live unlock calendar at all — the genesis, sale and Web3 Foundation allocations finished vesting years ago, and the chain's own DOT supply figure sits within about **640 DOT** of the circulating figure, so there is no locked bucket left to release. The **402M DOT** of room left under the 2.1B ceiling is not an escrow held by anyone; that DOT does not exist yet and only appears as the issuance schedule mints it. Sell #3, foundation and unscheduled unlocks, is 0 because no team-controlled DOT left its wallets in the window. Sell #4 is 0 because Polkadot is a live project with no bankruptcy estate and no trustee distribution schedule.

## Buy pressure: where new DOT goes

Nowhere — and this is the part of the Polkadot reset that gets least attention. Buy #1, programmatic buyback, is **0**: Polkadot has never deployed a buyback contract and the Web3 Foundation runs no repurchase programme. Buy #2, protocol fee burn, is **0**, and it is a **0** that used to be a real number. Polkadot historically burned a slice of unspent treasury funds at the end of every spend period, and it burned transaction fees and coretime sales revenue as well. Referendum **#1827**, executed alongside the March 2026 upgrade, set that treasury burn to **0%** and redirected fees, coretime revenue and validator slashes into the **Dynamic Allocation Pool** instead of destroying them. Polkadot burns nothing today, so any DOT burn figure quoted from before **Mar 2026** is refuted.

Buy #3, foundation buy, is **0** because the Web3 Foundation discloses no open-market DOT accumulation — its stated position is that it holds years of operating runway without needing to touch its DOT, which is the absence of a buying programme rather than the presence of one. Buy #4, new long-term lock, is **0** because staking on Polkadot is not a lock: staked DOT is already inside the circulating figure, and the same March 2026 package cut the unbonding wait from **28 days** to roughly **24 to 48 hours**, which makes DOT easier to release rather than harder. The result is a ledger with one non-zero line on the sell side and a completely empty buy side.

## Foundation and overhang

Three team-controlled overhangs are tracked on Polkadot. The first is the **OpenGov Treasury**, holding **24.31M DOT** as of **Aug 13 2026** — a governance treasury that can only be spent by a passing OpenGov referendum, fully readable on chain and re-read at every rebuild. The second is the **Dynamic Allocation Pool buffer**, holding **2.62M DOT** on the same date. The DAP is new, and it is the mechanism that replaced burning: reading its live budget map on chain shows **32.2%** of every block's DOT issuance retained in the buffer, **45.2%** paid to stakers and **22.6%** paid as validator incentive. Notably there is no fixed treasury share in that map at all — the old 85/15 stakers-versus-treasury split is gone, and the Polkadot Treasury is now funded by governance decisions out of the DAP.

The third is the **Web3 Foundation reserve**, and it is opaque: the foundation publishes no wallet addresses and no DOT token count, so the position can only be monitored through official disclosure rather than read on chain. No release fired from any of the three inside this window, which is why Sell #3 reads **0**. If any of these overhangs' balances falls between refreshes — the Polkadot Treasury through a passing DOT-denominated spend, the DAP buffer through a governance allocation that reaches the market, or the Web3 Foundation through a disclosed distribution — that outflow enters Sell #3 at the next refresh.

## How DOT compares to other capped proof-of-stake chains

The useful comparison for Polkadot is mechanism, not price, and on mechanism DOT has just moved category. Until March 2026 Polkadot belonged with the uncapped continuous-emission Layer 1s — chains like Cosmos Hub, which mint staking rewards forever against no maximum supply and no burn. DOT has now left that group: the **2.1 billion** ceiling is protocol-encoded, so unlike an uncapped chain there is a terminal DOT number, and unlike an uncapped chain the issuance schedule walks down on a fixed biennial calendar rather than floating on a bonded ratio. In that respect Polkadot now resembles a halving-model chain: a known cap, a known decay, and no discretion in the emission itself.

Where DOT differs sharply from the chains it most invites comparison with is the buy side. Ethereum pairs its staking issuance with a base-fee burn, so heavy usage can push net ETH supply negative; Polkadot deliberately removed that possibility, routing fees and coretime revenue into the Dynamic Allocation Pool rather than destroying them. Exchange tokens with quarterly buybacks and burns run a permanent, mechanical bid against their own float; DOT has no such mechanism and no plans for one. So Polkadot sits in an unusual position: a capped, disinflationary asset whose net supply nevertheless cannot go negative under any level of network activity, because there is no path by which a DOT is destroyed.

The trade Polkadot made is worth naming plainly, because it cuts both ways for DOT holders. Burning is deflationary but wasteful; the DAP keeps the value inside the system and lets governance spend it on security, ecosystem funding or a strategic reserve. That is a better capital-allocation story and a worse scarcity story. Against a halving chain, DOT's cap gives it a comparable long-run ceiling; against a fee-burning chain, DOT gives up the one mechanism that could make its supply shrink.

## What to watch in the next 90 days

First, the **Dynamic Allocation Pool budget map**. It is set by governance and currently retains **32.2%** of DOT issuance in the buffer; any referendum that re-weights it, adds a treasury key, or funds a strategic reserve changes where new DOT lands and is the single item most likely to move this page. Second, the **DAP buffer balance** itself, at **2.62M DOT** today — a large allocation out of it toward market-facing spending would put a real number into Sell #3 for the first time.

Third, the **Polkadot Treasury** at **24.31M DOT**: a DOT-denominated spend passing OpenGov is a direct, dated, on-chain outflow. Fourth, any proposal to **reintroduce a burn** — the March 2026 decision to stop burning DOT was contested in the forum, and a reversal would be the only realistic route to a negative net reading for Polkadot. Fifth, the next scheduled issuance step, due around **Mar 2028**: it is outside this window, but any referendum that pulls it forward or alters the biennial **13.14%** decay would re-base Sell #1 immediately.

## Summary

The MrNasdog Pressure Framework reads Polkadot (DOT) at **+0.82% net** over the last 90 days and **+0.81%** projected forward, against a supply monitor reading of **+0.47%** — a **0.34 percentage point** gap that stays inside tolerance. The structural mechanism is nominated-proof-of-stake issuance measured on chain at **56.35M DOT** a year, minting **13.89M DOT** in the trailing window, now bounded by a protocol-encoded hard cap of **2.1 billion DOT** and stepping down every two years. The key risk is that nothing offsets it: the same March 2026 vote that capped DOT also ended every burn, so Polkadot has no buyback, no fee burn and no lockup, and every newly issued DOT stays in supply. The ceiling is real and only **402M DOT** away, but until it is reached DOT holders are diluted a little over **3%** a year with no mechanism capable of reversing it.

---

*MrNasdog Pressure Framework analysis of DOT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 13 2026.*

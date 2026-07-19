---
title:         "XMR Inflation Analysis · July 2026 · Mixed flows · supply roughly steady"
description:   "Monero mined 64,769 blocks in 90 days at a fixed 0.6 XMR reward — 38.9K new coins, +0.21% net, with no buyback, no burn and no unlocks in the ledger."
canonical_url: "https://mrnasdog.com/research/xmr/inflation"
tags:          ["crypto", "xmr", "monero", "privacy"]
published:     true
---

*Originally published at [https://mrnasdog.com/research/xmr/inflation](https://mrnasdog.com/research/xmr/inflation)*

Monero mined **64,769** blocks in the last 90 days, each paying the permanent tail emission of **0.6 XMR** — about **38.9K** new XMR, or **+0.21%** of the **18.78M** circulating. Every other row in the Pressure Framework ledger is zero: no vesting unlocks, no foundation allocation, no buyback, no burn. XMR is a fair-launch proof-of-work privacy coin whose supply moves in one direction, very slowly, by protocol rule rather than by anyone's decision.

## The verdict, in one paragraph

For the 90-day window ending **Jul 19 2026**, the MrNasdog Pressure Framework reads Monero at **+0.21% net** — sell pressure of **38.9K XMR** against buy pressure of exactly **zero**. Our supply monitor reads the same window at **+1.76%**, a gap of **1.55 percentage points** that exceeds the framework's tolerance and ships a **monitor-gap chip** on the overview card. The gap is not new coins. At **0.6 XMR** per block Monero can physically mint no more than about **38.9K XMR** in 90 days, yet the monitor booked roughly **325K** — over eight times the protocol ceiling. Tracing it day by day, the monitor's upstream supply figure stepped up by about **317K** coins in a single day on **May 29 2026**, a day on which the chain minted roughly **432 XMR**. That is a data-feed correction, not issuance. The chain count is kept as primary. Monero is a **quiet chain with permanent, mechanical, slowly-shrinking inflation**.

## Sell pressure: where new XMR comes from

Sell #1, protocol inflation, is the entire sell ledger, and it is measured rather than assumed. Monero reached **tail emission** at the end of May 2022: once the original mining schedule ran down, the block reward settled at a fixed **0.6 XMR** per block and stays there permanently — the only fixed-rate perpetual block reward among the large-cap coins, and one that never falls to zero. Blocks target roughly two minutes, but real block times drift with hashrate, so this build read the chain directly instead of assuming a rate. Between the block mined on **Apr 20 2026** and the chain tip on **Jul 19 2026**, Monero produced **64,769** blocks — an actual pace of about **719.7** blocks a day rather than the nominal 720. At 0.6 XMR each that is **38.9K XMR** of new supply, or **+0.21%** against circulating supply of **18.78M**. Because the reward is fixed in coins and not as a percentage, the same quantum is minted every quarter forever while the denominator grows — annualised it is roughly **158K XMR**, about **0.84%** a year, and that percentage declines every year without any governance decision.

Sell #2, vesting unlocks, is **zero**, and structurally so. Monero launched in April 2014 as a fair launch with no premine, no instamine allocation, no investor round and no developer tax. Nothing was ever locked, so there is no vesting cliff or unlock calendar that could ever release supply — the row is not merely empty this quarter, it can never fill. Sell #3, foundation and unscheduled unlocks, is likewise **zero**: no reserve of XMR was ever set aside for a foundation or for Monero Research Lab, and development is funded by the Community Crowdfunding System, a donation-based mechanism rather than a token allocation. Sell #4, long-term locked or bankruptcy, is **zero** — there is no bankruptcy estate, no trustee distribution schedule and no court-ordered release of XMR anywhere in view.

## Buy pressure: where new XMR goes

The Monero buy ledger is empty across all four rows, which is unusual and worth stating plainly rather than glossing. Buy #1, programmatic buyback, is **zero** because Monero retains no protocol revenue at all: every transaction fee is paid directly to the miner who found the block, so no treasury accumulates and there is nothing to fund open-market buying. Buy #2, protocol fee burn, is **zero** for the same structural reason — fees are transferred to miners, never destroyed, so Monero has no burn analogue to the fee-burn mechanisms found on smart-contract chains.

Buy #3, foundation buy, is **zero**. The Community Crowdfunding System General Fund exists to pay contributors for approved work, not to accumulate XMR, and no open-market purchasing was observed in the window. Buy #4, new long-term lock, is **zero** because Monero has no staking at all — it is proof-of-work, so there is no bonding contract, no lockup and no mechanism that removes XMR from the tradable float. The practical consequence is that the framework's net number and the gross mining number are the same figure: **38.9K XMR** reaches the market over 90 days and nothing takes any of it back.

## Foundation and overhang

Monero has almost nothing to enumerate here, because a fair launch leaves no team-controlled allocation behind. There is no foundation treasury of premined XMR, no labs entity holding tokens, no DAO treasury and no buyback accumulation wallet. The single identified team-controlled pool is the **Community Crowdfunding System General Fund**, a multisig holding donated XMR plus the residue of proposals that were overfunded or never completed. Its balance is not published, and Monero's privacy design means it cannot be read from the chain either, so the framework tracks it as an **opaque overhang** rather than a measured balance and refreshes it by walking the project's own disclosure surface on each rebuild.

It is worth being precise about what Monero's privacy does and does not hide, because this is routinely stated wrongly. Total issuance is **fully auditable**: coinbase rewards are transparent, block heights are public, and any node can verify the supply from first principles — which is exactly how the **38.9K** figure above was derived. What is private is **individual balances and transaction amounts**, protected by ring signatures and confidential transactions. So the aggregate is verifiable while the General Fund's wallet-level holdings are not. If that overhang's balance falls between refreshes and the outflow becomes visible through project disclosure, it enters Sell #3 at the next refresh.

## How XMR compares to other proof-of-work chains

Monero and the hard-capped proof-of-work chains solve the same security problem with opposite answers. A halving-model chain with a fixed maximum supply cuts its block subsidy on a schedule until issuance approaches zero, betting that transaction fees alone will eventually pay for security. Monero rejected that bet: the tail emission is a deliberate decision that a permanent, predictable **0.6 XMR** per block keeps miners paid regardless of fee-market conditions, and also replaces coins lost to forgotten keys. The trade is explicit — Monero gives up the hard-cap marketing story and accepts a permanent **+0.21%** per quarter, in exchange for a security budget that never depends on fee volatility.

Against uncapped continuous-emission proof-of-stake chains, Monero looks conservative rather than aggressive. Those chains typically issue several percent a year and route it to stakers, which means a large fraction of new supply is immediately re-locked and the headline inflation overstates real float growth. Monero has no such offset and no such distortion: **38.9K XMR** is minted and **38.9K XMR** reaches the open market, mined by whoever ran the hashrate. The number is small but it is honest — there is no staking ratio, no re-lock, and no re-classification that could make the reported figure diverge from the tradable reality.

Against the other privacy coins, Monero's distinguishing feature is that its supply schedule is boring on purpose. Several privacy projects carry founder rewards, development funds taken from the block reward, or premined allocations that create a discretionary overhang the market must price. Monero carries **none** of those, so its Pressure Framework ledger has exactly one live row. For a supply-side reader, that is the whole appeal: there is no schedule to track, no governance vote that could change the mint, and no entity with a stockpile to deploy.

## What to watch in the next 90 days

First, the **FCMP++** upgrade work continuing through 2026 — it replaces ring signatures with full-chain membership proofs and materially changes Monero's privacy and scaling, but it does not touch issuance; watch it for narrative, not for supply. Second, the Monero Research Lab's post-quantum work on Jamtis addresses, which advanced in **May 2026** and would lengthen addresses without altering the block reward. Third, the native **THORChain** XMR swap route, in final testing as of **Jun 24 2026**, which changes where XMR liquidity lives as centralised exchanges continue delisting it — a float-location question, not a supply question.

Fourth, the Community Crowdfunding System proposals portal, the only surface on which the single identified overhang could move; a large funded proposal is the one thing that would put a number into Sell #3. Fifth, and the only item that could genuinely change this page: any consensus proposal to alter the tail emission itself. A GitHub issue arguing the **0.6 XMR** reward is too low has been open since late 2025 and has not been adopted; changing it would require a hard fork with broad consensus, and until one ships the **+0.21%** reading holds by protocol rule.

## Summary

Monero mints **38.9K XMR** per 90 days from a permanent tail emission of **0.6 XMR** across **64,769** observed blocks, and removes none of it — no buyback, no burn, no lock — for a Pressure Framework net of **+0.21%** against **18.78M** circulating. The fair launch means there is no vesting schedule, no foundation allocation and no discretionary overhang beyond an opaque donation-funded General Fund, so the ledger has one live row and seven structural zeros. The key risk is not dilution — it is that the mint is permanent and uncapped, so XMR will never have a scarcity ceiling to point at, only a rate that keeps falling as a percentage. Our supply monitor's **+1.76%** reading for the same window is an upstream data correction dated **May 29 2026**, not issuance; the chain count of **38.9K** is what actually reached the market.

---

*MrNasdog Pressure Framework analysis of XMR, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 19 2026.*

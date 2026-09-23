---
title:         "XTZ Inflation Analysis · September 2026 · Supply growing · projected to keep growing"
description:   "XTZ supply grows 0.74% a quarter: Tezos minted 8.16M XTZ of staking rewards in 90 days while fee burns removed 0.06M. Full Pressure Framework analysis."
canonical_url: "https://mrnasdog.com/research/tezos/inflation"
tags:          ["crypto", "xtz", "tezos", "layer1"]
published:     true
---

Originally published at [XTZ Inflation Analysis · September 2026 · Supply growing · projected to keep growing](https://mrnasdog.com/research/tezos/inflation).

# XTZ Inflation Analysis · September 2026 · Supply growing · projected to keep growing

XTZ supply is growing and is projected to keep growing. Tezos minted **8.158M XTZ** of staking rewards over the last 90 days, while fee burns and forfeited rollup bonds destroyed **0.065M XTZ**, for a net of **+0.74%** against a monitor reading of **+0.73%**. The pace is set by adaptive issuance, a reward rate that falls as more XTZ is staked, and Tezos has no maximum supply.

## The verdict, in one paragraph

Against a circulating base of **1,096.9M XTZ**, the Pressure Framework books **8.163M XTZ** of sell pressure and **0.065M XTZ** of buy pressure over the 90 days to **Sep 23 2026**, a net of **+0.74%**, and projects **+0.74%** for the next 90 days. The inflation monitor reads **+0.73%** for the same window, a gap of **0.005 percentage points**, well inside the 0.5-point tolerance, so no warning ships. The ledger also closes against the chain itself: minted XTZ plus claimed fundraiser coins, minus every destroyed coin, equals the rise in circulating XTZ to the last millionth. Tezos is a steady, uncapped staking chain whose new supply is only lightly offset by burns.

## Sell pressure: where new XTZ comes from

Almost all of it comes from protocol inflation. Tezos pays bakers and stakers in newly minted XTZ, and the chain keeps its own count of every XTZ it has created. That count rose **8.158M XTZ** across the window, about **90.6K XTZ** a day. The rate is not fixed. Under adaptive issuance, Tezos recalculates its yearly reward rate every cycle from the share of XTZ that is staked, paying less as that share rises. The rate read **3.21%** on **Jun 25 2026** and **2.96%** on **Sep 23 2026**, while the staked share climbed from **29.6%** to **31.0%**. The Ushuaia upgrade activated on **Jun 30 2026**, inside the window, but it widened the data layer and left the reward rules and the XTZ supply untouched, so the next 90 days carry the same measured pace.

Vesting unlocks are **0**. The Tezos Foundation and founding-team allocations released monthly over four years and finished on **Sep 17 2022**; no new vesting schedule exists. Foundation and unscheduled unlocks are **0**: the fourteen labelled Tezos Foundation wallets sent out nothing at all during the window, and their coins already count as tradable float in any case. Long-term locked or bankruptcy releases are **0**, because XTZ has no bankruptcy estate, trustee or court-ordered distribution.

One extra row exists because of how Tezos launched. About **20.0M XTZ** from the 2017 fundraiser has never been claimed, and those coins sit outside the circulating count until their owner activates them. One owner did so on **Jul 28 2026**, adding **4,588 XTZ** to the float. Claims happened 11 times in the past year, **82.9K XTZ** in total, so the forward reading carries a quarter of that, about **20.7K XTZ**.

## Buy pressure: where new XTZ goes

Programmatic buyback is **0**. Tezos transaction fees go to bakers, and no treasury or protocol programme buys XTZ on the market. Protocol fee burn is **34.8K XTZ**, from two separate paths read at both window ends. Storage and new-account fees, which Tezos destroys rather than pays out, removed **21.9K XTZ**. The chain's built-in liquidity-baking exchange burned another **12.9K XTZ** by sending its 0.1% trade fee to the null address; every one of those transfers came from that one exchange contract, and their sum matches the null address's balance change exactly.

Foundation buy is **0**: the labelled Tezos Foundation wallets received only **8.54 XTZ** in the whole window. New long-term lock is **0**. Staked XTZ rose from **322.3M** to **339.9M**, but staked coins still count as circulating on Tezos, so staking moves coins within the float and removes nothing from this reading.

The last buy row is an accident rather than a policy. Between **Aug 15 2026** and **Aug 18 2026**, one operator lost six fraud-proof disputes on Etherlink, the Tezos rollup. Each loss cost a **10K XTZ** bond, half paid to the winner and half destroyed, for **30.0K XTZ** burned in all. Nothing schedules another dispute, so the forward reading carries **0** here.

## Foundation and overhang

The largest identified holder that could sell is the Tezos Foundation. Fourteen labelled wallets, four bakers and ten delegators, held **83.4M XTZ** at the end of the window, much of it staked, with zero outgoing transfers across the 90 days. The Foundation's report for the second half of 2025 valued its XTZ at **USD 76M** on **Dec 31 2025**, which suggests part of its XTZ sits outside the labelled set, for example in loans or exchange liquidity. Those coins are already inside the float, so a sale would not add new supply to this reading, but it would still add coins to the market, and the labelled wallets are read at every rebuild.

The second overhang is the **20.0M XTZ** of unclaimed fundraiser coins, which can be claimed at any time with no expiry. There is no buyback wallet and no bankruptcy estate. If the Foundation wallets fall between refreshes by more than their own rewards explain, that outflow is examined at the next refresh; if the unclaimed fundraiser pool falls, that outflow enters the fundraiser row at the next refresh.

## How XTZ compares to other staking chains

XTZ sits in the class of uncapped proof-of-stake chains that mint rewards forever, next to most Cosmos chains. What sets Tezos apart is that its rate is a feedback loop rather than a fixed schedule: when more XTZ is staked, adaptive issuance pays less, and when staking falls, it pays more. That makes the forward number move slowly, and in this window it moved down, from 3.21% to 2.96% a year.

Against a halving-model chain like Bitcoin, XTZ has no hard cap and no dated cut, so its dilution does not fall on a known clock; it falls only as staking rises. Against chains with a large base-fee burn, the Tezos burn is small. Storage fees and the liquidity-baking exchange together destroyed **34.8K XTZ**, well under 1% of the new XTZ minted, so fee burns alone cannot turn Tezos deflationary at today's activity.

Against tokens still working through vesting cliffs, Tezos is simpler: its early allocations finished vesting in 2022, and the only coins entering the float from outside it are occasional fundraiser claims.

## What to watch in the next 90 days

First, the staked share: each rise lowers the reward rate, so a steady climb from **31.0%** would pull the **2.96%** yearly rate lower through **Dec 22 2026**. Second, Tezos governance: a new proposal period opened on **Sep 23 2026** and runs to **Oct 7 2026**, and the next upgrade is expected to switch on native liquid staking, which would likely raise the staked share. Third, further Etherlink disputes, which destroyed **30.0K XTZ** in August. Fourth, the fourteen Tezos Foundation wallets holding **83.4M XTZ**, and any fundraiser claims from the **20.0M XTZ** still unclaimed.

## Summary

The MrNasdog Pressure Framework reads XTZ at **+0.74%** over the last 90 days and **+0.74%** projected forward: supply growing, projected to keep growing. The mechanism is adaptive issuance, which minted **8.158M XTZ** of staking rewards while burns destroyed **0.065M XTZ**. The main risk is that the chain has no maximum supply, so new XTZ keeps arriving every block. The one brake is the rate itself, which falls as more XTZ is staked and read **2.96%** a year on **Sep 23 2026**.

MrNasdog Pressure Framework analysis of XTZ, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 23 2026.

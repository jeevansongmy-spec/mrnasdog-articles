---
title: "ICP Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description: "Mixed flows, supply roughly steady: ICP reads +0.48% over 90 days. The Internet Computer minted 2.80M ICP and burned 117.4K into compute, with no buyback."
canonical_url: "https://mrnasdog.com/research/icp/inflation"
tags: ["crypto", "icp", "internet-computer", "staking"]
published: true
---

> Originally published at **[mrnasdog.com/research/icp/inflation](https://mrnasdog.com/research/icp/inflation)** by MrNasdog.

The Internet Computer is one of the few networks that genuinely destroys its own coin, yet over the 90 days to **Sep 15 2026** it still created far more ICP than it burned. The Pressure Framework reads ICP at **+0.48%** net over the trailing 90 days and **+0.36%** over the next 90: sell pressure of **2.80M ICP** from node operator pay and cashed-out voting rewards, buy pressure of **117.4K ICP** burned into compute, against a supply monitor reading of **+0.39%**. ICP has no supply cap; the only brake on issuance is what the NNS governance system votes to pay.

## The verdict, in one paragraph

Against a circulating base of **556.8M ICP**, the framework books **2.80M ICP** of sell pressure and **117.4K ICP** of buy pressure over the trailing 90 days — a net of **+0.48%** — and projects **+0.36%** for the next 90 days. The inflation monitor reads **+0.39%** for the same window, a gap of **0.09 percentage points**, well inside the framework's 0.5pp tolerance, so the overview ships with no monitor-gap warning. The numbers are unusually well pinned: the ICP ledger's count of coins in existence rose by exactly what was minted minus what was burned, to the smallest unit the coin has. The label for ICP is an **uncapped network with a real burn that currently offsets about 4% of its own issuance**.

## Sell pressure: where new ICP comes from

New ICP comes from two places, and because they run on different clocks the ledger keeps them in separate rows. The larger is Sell #5, node operator rewards, at **1.74M ICP**. The operators who run the Internet Computer's physical machines are paid once a month in newly minted ICP, with pay set in XDR, a basket of world currencies, and converted to ICP at the time of payment. Three payments fell in the window: **668.5K ICP** on **Jul 15 2026**, **541.9K ICP** on **Aug 14 2026** and **525.1K ICP** on **Sep 13 2026**. NNS proposal 142681, executed on **Jul 6 2026**, set a floor of 2 XDR per ICP on that conversion, so while ICP trades below that level the network mints fewer coins than the market price would imply; all three payments in the window were paid under the floor. The step down after July came from the amount owed itself, which fell by about a quarter in XDR terms, in the same month the NNS approved a smaller target network of 612 nodes. The forward projection uses the September amount.

Sell #1, protocol inflation, is the other leg at **1.06M ICP**. NNS voting rewards are not paid in ICP; they accrue as maturity, an internal credit inside each staked neuron, and a coin is minted only when a holder disburses that maturity. Holders disbursed **1.06M ICP** across the window, a little more in each successive month. The Mission 70 reform cut the voting reward pool by roughly a third in April 2026, before this window opened, and the pool held steady throughout it.

Sell #2, vesting unlocks, is **0**. Staked and still-vesting ICP is already counted in the circulating supply, so a neuron dissolving changes who can sell but adds no coin to the float. The remaining 2021 launch allocations did keep unwinding, down about one million ICP over the window, but those coins were inside the float all along. Sell #3, Foundation and unscheduled unlocks, is **0**, with no public evidence of a release in the window. Sell #4, long-term locked or bankruptcy, is **0**: there is no estate or trustee attached to ICP.

## Buy pressure: where new ICP goes

Buy #2, the protocol fee burn, is **117.4K ICP**, and it is real destruction rather than a transfer. When a developer converts ICP into cycles, the fuel that pays for compute and storage on the Internet Computer, the ICP is removed from the ledger entirely; a tiny fee on every transfer is removed the same way. Over the window **117.2K ICP** was burned into cycles and **132 ICP** as transfer fees. There is no dead address to watch: the count of ICP in existence is where the burn shows, and it fell short of the gross mint by exactly this amount.

Buy #1, programmatic buyback, is **0**. No programme buys ICP on the open market. A 2026 plan routes a fifth of revenue from private business subnets into burning ICP, but any such burn passes through the same cycles counter, so it is already inside Buy #2 and is not counted twice. Buy #3, Foundation buy, is **0**: the DFINITY Foundation announced no purchase. Buy #4, new long-term lock, is **0**. ICP staked in governance rose from **289.1M** to **289.6M**, but staked ICP already counts as circulating, so more staking removes nothing from this reading.

## Foundation and overhang

The largest overhang on ICP is not a team wallet. It is **96.1M ICP-equivalent** of uncashed voting-reward maturity, about 17% of supply, which grew by **1.83M** across the window and becomes new ICP the moment holders disburse it. There is no schedule; it converts at the holders' pace, and it is read from the NNS governance canister at every rebuild. Second is the **20.2M ICP** still inside unwinding 2021 launch allocations, supply-neutral under this denominator but spendable as it releases. Third is the Neurons' Fund, the governance-run pool that backs new projects, at **15.3M ICP** staked plus **5.8M** of maturity, deployable only by an NNS vote. Fourth is the DFINITY Foundation itself, whose holdings are not published as an identifiable set of wallets and are tracked through its disclosures. If any of these balances falls between refreshes by more than its schedule explains, that outflow enters Sell #3 at the next refresh.

## How ICP compares to other uncapped proof-of-stake chains

ICP sits in the class of uncapped, continuously issuing proof-of-stake networks, alongside most Cosmos-based chains, where staking rewards are a policy decision rather than a number fixed in code. Two features set it apart. First, a large part of its issuance pays for hardware rather than for staking: node operator rewards were **1.74M** of the **2.80M ICP** minted, a cost that proof-of-work chains carry through block subsidies and most proof-of-stake chains fold into validator rewards. Second, its voting rewards only become coins when claimed, so realised issuance runs well below the headline reward rate.

On the burn side ICP resembles Ethereum more than a typical staking chain: usage destroys the native coin, and the burn scales with demand for compute. The difference is scale. Ethereum's base-fee burn has at times exceeded its issuance; ICP's cycles burn offset about 4% of minting in this window. Against exchange tokens that run scheduled buyback-and-burn programmes, ICP has no discretionary lever at all: the burn is purely mechanical, which makes it honest, and small.

## What to watch in the next 90 days

First, the node operator payments due around **Oct 14 2026** and **Nov 13 2026**, projected at about **525.1K ICP** each; the next one after lands around **Dec 14 2026**, just past the forecast window, and would lift the projection to roughly **+0.45%** if it arrives early. Second, the ICP price against the 2 XDR floor: above it, each payment mints fewer coins; below it, the floor caps the mint. Third, maturity disbursement, which has risen month over month and draws on a **96.1M** reserve. Fourth, the cycles burn, the only buy-side mechanism, where any real growth in compute demand shows up directly. Fifth, NNS governance, where node reward, topology and network economics proposals continue to change the size of the mint.

## Summary

The MrNasdog Pressure Framework reads ICP at **+0.48%** over the trailing 90 days and **+0.36%** projected: mixed flows, supply roughly steady but still growing. The Internet Computer minted **2.80M ICP** for node operators and cashed-out voting rewards and burned **117.4K ICP** into compute, with no buyback. The key risk is the **96.1M ICP-equivalent** of unclaimed maturity, which can turn into new coins at holders' discretion. ICP has no supply cap, so the ceiling on issuance is whatever NNS governance votes to pay.

*MrNasdog Pressure Framework analysis of ICP, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Sep 15 2026.*

---
title: "ICP Inflation Analysis · August 2026 · Mixed last 90D, projected to grow"
description: "MrNasdog Pressure Framework read of Internet Computer (ICP): 2.66M ICP minted in 90 days against a real 0.10M cycles burn. Net +0.46%; monitor +0.76%."
canonical_url: "https://mrnasdog.com/research/icp/inflation"
tags: ["crypto", "icp", "internet-computer", "staking"]
published: true
---

> Originally published at **[mrnasdog.com/research/icp/inflation](https://mrnasdog.com/research/icp/inflation)** by MrNasdog.

The Internet Computer is one of the few networks that genuinely destroys its own coin, and it is still net inflationary. Over the last 90 days the Internet Computer minted **2.66M ICP** and burned **0.10M ICP**, a net **+0.46%** of the **555.37M ICP** circulating supply, against **+0.76%** read by the inflation monitor. The next 90 days project to **+0.53%**. ICP has no supply cap, so nothing in the protocol forces issuance to stop — but a governance vote executed on **Jul 6 2026** now puts a hard floor under the price used to pay node operators, which caps the largest single source of new ICP.

## The verdict, in one paragraph

The MrNasdog Pressure Framework reads the Internet Computer at **+0.46%** net supply growth over the trailing 90 days and **+0.53%** over the coming 90. The inflation monitor reads **+0.76%** for the same trailing window, a gap of **0.30 percentage points** — inside the framework's half-a-point tolerance, so no data-conflict chip is raised. The small difference is what you would expect from a supply figure derived from market capitalisation divided by price rather than read straight off the ledger. The characterisation: **a network with a real burn that is still far too small to matter**. Both taps are open on ICP, which is rarer than it sounds — most uncapped proof-of-stake chains only mint. The Internet Computer mints and destroys, and the destruction currently offsets under **4%** of the issuance.

## Sell pressure: where new ICP comes from

New ICP arrives through two channels and nothing else. The larger one is node-provider rewards: operators who run the physical machines behind the Internet Computer are paid once a month, and that payment mints fresh ICP. Two such payments landed inside the last 90 days, together **1.37M ICP**. The bill itself is denominated in a reserve-currency unit and converted into ICP at settlement, which used to mean a cheaper ICP printed more coins for the same bill. NNS proposal **142681**, executed **Jul 6 2026**, ended that by fixing a minimum conversion rate; ICP has traded below that floor every day since, so the node-provider mint is now capped at roughly **0.58M ICP** a month regardless of how weak the price gets. Three payments fall inside the next 90 days rather than two, which is why the forward node-provider figure rises to **1.75M ICP** even though the per-payment rate is falling.

The second channel is neuron maturity. Staking ICP in an NNS neuron does not pay coins — it accrues maturity, which is a claim, not a token. New ICP exists only at the moment a holder converts that maturity into real ICP by spawning or disbursing it. That conversion minted **1.29M ICP** over the window and is projected flat at **1.29M ICP** for the next, a rate confirmed independently across two non-overlapping 90-day windows. This distinction matters: the headline governance-reward rate is far larger than the minting it actually produces, because most maturity is restaked rather than cashed out.

Every other sell row is zero. Vesting unlocks contribute **0** because the Internet Computer has no unlock calendar that adds supply — genesis seed and early-contributor allocations sit inside eight-year dissolving neurons running to 2029, and staked ICP is already counted in circulating supply, so a neuron completing its schedule converts locked tokens into liquid ones without creating a coin. Foundation and unscheduled unlocks contribute **0** because no tracked team-controlled position released ICP in the window. Long-term locked or bankruptcy contributes **0** because the Internet Computer is a live project with no estate and no trustee distribution.

## Buy pressure: where new ICP goes

The Internet Computer's buy side is a single mechanism, and it is the most interesting thing about ICP tokenomics. Compute on the network is paid for in cycles, and cycles are created by destroying ICP. The coin is not moved to a treasury or handed to validators — it is burned, permanently. That burn removed **0.10M ICP** over the last 90 days and is running at the same pace into the next **0.10M ICP**. Ledger transaction fees are burned too, but they amount to roughly **130 ICP** across the whole quarter — a rounding error beside the cycle burn.

What sets the ICP burn apart from a fee burn on a general-purpose chain is that it tracks compute demand rather than transaction count or fee spikes. It is a usage meter. It is also, at present, tiny: **0.10M ICP** against **2.66M ICP** minted. For the Internet Computer to reach net-zero supply on today's issuance, network compute demand would have to rise by roughly **26 times**. That is the whole deflation thesis in one number.

The remaining buy rows are zero. Programmatic buyback is **0** — the Internet Computer has no buyback contract and the NNS has never authorised open-market repurchase. Foundation buy is **0** — DFINITY discloses no accumulation programme. New long-term lock is **0**, because staking into an NNS neuron removes nothing from supply: staked ICP already sits inside the circulating figure. The window in fact ran the opposite way, with the unvested genesis bucket releasing **8.78M ICP** into liquid float.

## Foundation and overhang

Four team-controlled or protocol-controlled overhangs are tracked on the Internet Computer, and one of them dwarfs the rest. Accrued neuron maturity stands at about **95.66M ICP-equivalent** — an unminted, unscheduled claim on future ICP, refreshed from the NNS every day. It is not owed to any single party, but it is real latent supply, and the pace at which holders choose to convert it is the single largest swing factor in the ledger. The still-unvested genesis bucket holds about **20.24M ICP** and drained **8.78M ICP** into liquid float during the window, running down toward its 2029 finish. The Neurons' Fund holds about **15.26M ICP** staked, deployable only by a passing governance vote. The DFINITY Foundation publishes no single wallet address, so its own position is opaque and monitored through official disclosure on a bi-weekly walk rather than by chain read.

If any of these balances falls between refreshes, the outflow enters the Foundation and unscheduled unlocks row at the next refresh. Nothing did in this window, which is why that row sits at **0** rather than being absent — the framework surfaces what it is watching, not only what fired.

## How ICP compares to other uncapped compute chains

Against uncapped continuous-emission layer ones, the Internet Computer looks unusually restrained. Chains whose only supply force is a staking mint — no burn on the other side — commonly run **3%** to **13%** a year with nothing able to slow them except a governance vote. ICP's **+0.53%** per 90 days annualises near **2.1%**, and it has a second mechanism working against issuance rather than nothing at all. The Internet Computer also differs from those chains in that its staking rewards do not mint on accrual. Maturity is a claim; only conversion mints. A chain that mints staking rewards directly to validators has no such buffer.

Against fee-burn chains, the comparison inverts. A base-fee burn scales with transaction demand and can flip a chain net-deflationary during congestion. The Internet Computer's burn scales with compute purchased, which is far steadier and far smaller — good for predictability, bad for magnitude. ICP will not flip deflationary on a busy week; it would need a durable multi-year rise in canister workload. Against hard-capped proof-of-work chains, the Internet Computer has no halving, no terminal supply and no protocol guarantee that issuance ever ends. What it has instead is a governance body that can and does cut its own issuance — the Jul 6 2026 conversion floor being the most recent example, and the wider Mission 70 reform approved in April 2026 the larger one. That is a weaker guarantee than code, but it is a live one, and the measured supply growth has fallen every quarter since it began.

## What to watch in the next 90 days

The node-provider mint fires monthly and is the largest dated event on the calendar: payments are due around **Aug 14 2026**, **Sep 13 2026** and **Oct 13 2026**, roughly **0.58M ICP** each while the conversion floor binds. The floor itself is the second watch item — it only caps the mint while ICP trades below the level set on **Jul 6 2026**; a strong price rally would lift ICP above it and let node-provider minting expand again, an unusual case where a higher price means more issuance. Third, the cycle burn: a durable step up in compute demand is the only thing that can move the buy side, so watch whether the quarterly burn breaks decisively above **0.10M ICP**. Fourth, the pace of maturity conversion — if holders begin cashing out a larger share of the **95.66M ICP-equivalent** maturity stock, the mint rises without any protocol change at all. Fifth, further Mission 70 steps reaching the NNS vote portal, since each one has so far cut issuance rather than raised it.

## Summary

The MrNasdog Pressure Framework reads the Internet Computer as mildly inflationary and improving: **+0.46%** net supply over the last 90 days, **+0.53%** projected for the next, on **555.37M ICP** circulating with no supply cap. The structural mechanism is two-sided — **2.66M ICP** minted for node operators and governance-reward conversion against a real, permanent **0.10M ICP** burn from compute purchases. The key risk is the **95.66M ICP-equivalent** stock of accrued neuron maturity, an unscheduled claim on future supply that could mint faster than projected if holders choose to convert it. The ceiling is governance rather than code: the Internet Computer has no maximum supply, and its declining issuance rests on NNS decisions such as the **Jul 6 2026** conversion floor, which can be revisited by the same body that set them.

---

*MrNasdog Pressure Framework analysis of ICP, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 14 2026.*

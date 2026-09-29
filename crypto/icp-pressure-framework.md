---
title: "ICP Inflation Analysis · September 2026 · Mixed flows · supply roughly steady"
description: "ICP supply is roughly steady but rising: 2.80M ICP minted for node providers and voting rewards against a 128.8K cycles burn gives +0.48% net in 90 days."
canonical_url: "https://mrnasdog.com/research/icp/inflation"
tags: ["crypto", "icp", "internet-computer", "staking"]
published: true
---

> Originally published at **[mrnasdog.com/research/icp/inflation](https://mrnasdog.com/research/icp/inflation)** by MrNasdog.

The MrNasdog Pressure Framework reads ICP at **+0.48% net** over the last 90 days and **+0.45%** over the next 90: the Internet Computer minted **2.80M ICP** between Jul 1 and Sep 29 2026 and burned **128.8K ICP**, so supply grew by about **2.68M ICP**. The new ICP comes from two protocol payments — **1.74M ICP** to node providers and **1.07M ICP** of voting rewards that neuron holders cashed out — while the only thing that removes ICP is the burn of ICP into cycles, the fuel apps pay for computing. Nothing vests, there is no buyback, and ICP has no supply cap; the burn covers under 5% of what is minted.

## The verdict, in one paragraph

ICP supply grew **+0.48%** in the trailing 90 days (2,804,970 ICP minted, 128,812 ICP burned, against **556.92M ICP** circulating), and the framework projects **+0.45%** for the next 90 days. The monitor reads **+0.34%** for the same window, a gap of **0.14 percentage points** — inside the 0.5-point tolerance, so no monitor-gap warning is shown. Both sides sit under +0.5%, which puts ICP in the mixed band: supply roughly steady, but only because the network is large, not because the burn keeps up. The cite-able label is **mildly inflationary, subsidy-driven, with a small usage burn**.

## Sell pressure: where new ICP comes from

Protocol inflation from voting rewards added **1,069,447 ICP** in the window. ICP holders who lock coins in NNS neurons and vote earn rewards as maturity, and maturity turns into new ICP only when a holder cashes it out. The reward pool has sat near 54,000 ICP a day since the Mission 70 cut took effect in late April 2026, and it paid out about 41,000 ICP a day this window; most of that stays as maturity or is staked back into neurons, and only the cashed-out part enters the market. The ledger count of every mint in the window matches the change in supply to the last unit once burns are added back, and the governance canister's own reward records agree with the split within about 4%.

Node provider rewards added **1,735,523 ICP** in three monthly payments: 668,529 ICP on Jul 15, 541,884 ICP on Aug 14 and 525,110 ICP on Sep 13 2026. The network owes node providers an amount set in XDR and pays it in freshly minted ICP. Two governance decisions changed that bill inside the window: on Jul 6 2026 the NNS set a floor that counts ICP at no less than 2 XDR when paying, and on Jul 31 2026 it adopted a smaller target network of 612 nodes, down from 764. The monthly bill fell by about a fifth after that, so the framework books the next three payments — due around Oct 14, Nov 13 and Dec 14 2026 — at the latest size, **about 1.58M ICP** in total.

Vesting unlocks are **0**: every sale round finished vesting by Jun 11 2025. Foundation and unscheduled unlocks are **0**, and long-term locked or bankruptcy supply is **0** — there is no estate or trustee, and ICP locked in neurons already counts as circulating, so a neuron that dissolves adds nothing new to the float.

## Buy pressure: where new ICP goes

The protocol fee burn removed **128,812 ICP** in 90 days, about 1,431 ICP a day. Almost all of it — 128,673 ICP — was ICP converted into cycles, the unit every Internet Computer app burns to pay for compute and storage; the other 139 ICP were ledger transfer fees, which are destroyed rather than paid to anyone. The burn grew through the window, from about 29,000 ICP in July to about 54,000 ICP in September, as more apps and the new cloud engines drew on the network. No pricing change is scheduled, so the framework holds the trailing rate for the next 90 days.

Programmatic buyback is **0**: no contract or treasury buys ICP on the market. The plan to spend 20% of cloud-engine revenue on buying and burning ICP destroys coins through the same cycles burn, so it is counted once, inside the burn. Foundation buying is **0**, and new long-term locks are **0** — neuron stakes grew by about 846,000 ICP in the window, but staked ICP still counts as circulating, so a larger stake removes nothing from the float.

## Foundation and overhang

The largest overhang on ICP is not a wallet. It is **about 96.45M ICP** of earned but uncashed voting rewards held as neuron maturity, plus **16.94M ICP** of maturity staked back into neurons. None of it is ICP yet; it becomes new supply only when holders cash it out, which is exactly the flow the voting-reward row measures each window. The maturity balance rose by about 1.79M ICP in these 90 days, so the backlog is still growing faster than it is being drawn down.

Three other holdings are tracked, all already inside the circulating count: the genesis bucket of seed and early-contributor neurons (about **20.24M ICP**), the Neurons' Fund (**15.27M ICP** staked plus 5.80M ICP of maturity, which only an NNS vote can commit to new projects), and the DFINITY Foundation's own holdings, which the Foundation does not publish as one figure. Its known governance neuron holds only 10 ICP. If any of these balances falls between refreshes, or if cashed-out maturity jumps well above the trailing rate, the outflow enters the sell side at the next refresh.

## How ICP compares to other uncapped proof-of-stake Layer 1s

ICP pays for security the way most uncapped proof-of-stake chains do — with new coins — but it splits the bill in two. Staking-reward chains such as Ethereum and Polkadot mint rewards straight to validators or stakers; ICP mints both a governance reward to neuron holders and a hardware bill to node providers, and the node bill is priced in XDR, so a falling ICP price means more ICP minted for the same machines. The Jul 6 2026 floor of 2 XDR per ICP caps that effect, which is a design choice few other Layer 1s have.

On the burn side, ICP's reverse-gas model means apps, not users, burn the coin: developers convert ICP into cycles and the cycles pay for compute. That makes the burn a measure of real usage, similar in spirit to Ethereum's base-fee burn, but at today's size it offsets under 5% of minting, against about 1% on Ethereum in its latest window. Chains with a hard cap and halving, like Bitcoin, have no burn to lean on but a schedule that only shrinks; ICP has no cap, so its supply path depends on NNS votes and on how fast usage grows.

The one structural feature with no close match elsewhere is the maturity backlog. Most staking chains pay rewards as liquid coins at once; ICP lets them pile up as maturity that is not yet supply. That keeps the measured inflation lower today than the reward rate suggests, and it leaves about 96.45M ICP that could become supply faster if holders decide to cash out together.

## What to watch in the next 90 days

The next node provider payments are due around **Oct 14 2026**, **Nov 13 2026** and **Dec 14 2026**; each is booked at about 525,110 ICP, and each will be smaller if the 30-day ICP price stays above 2 XDR, because the floor then stops binding. Watch the NNS for any further Mission 70 proposal on voting rewards or node pay — the plan's goal is to cut ICP inflation by at least 70% by the end of 2026, and a new cut would lower the sell side. Watch the cycles burn, which rose each month this window; a burn above about 1,500 ICP a day would lower the forward number. Watch the maturity backlog of about 96.45M ICP: a jump in cash-outs would raise the sell side quickly.

## Summary

ICP is mildly inflationary: the Internet Computer minted 2.80M ICP in the last 90 days — 1.74M ICP for node providers and 1.07M ICP of cashed-out voting rewards — and burned 128.8K ICP for cycles, for a net **+0.48%**, with **+0.45%** projected for the next 90 days. The mechanism is an uncapped subsidy paid in new ICP, trimmed by a usage burn that covers under 5% of it. The key risk is the 96.45M ICP maturity backlog, which can turn into supply whenever holders cash out. ICP has no supply cap; its inflation falls only if the NNS keeps cutting rewards or the cycles burn grows many times larger.

---

*MrNasdog Pressure Framework analysis of ICP, Metric 1 — Inflation. Data + explanation only. Not financial advice. Checked Sep 29 2026.*

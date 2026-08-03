---
title: "AKT Inflation Analysis · August 2026 · Mixed flows, supply roughly steady"
description: "A MrNasdog Pressure Framework read of Akash Network (AKT): a 4% staking mint hands only ~0.88M AKT to the market over 90 days while a usage-linked burn retires ~0.81M. Framework +0.02% net; monitor +0.26%; forward +0.02%."
canonical_url: "https://mrnasdog.com/research/akt/inflation"
tags: ["crypto", "akt", "akash", "depin", "staking"]
published: true
---

> Originally published at **[mrnasdog.com/research/akt/inflation](https://mrnasdog.com/research/akt/inflation)** by MrNasdog.

Akash Network mints AKT at a **4%** annual rate — about **2.9M AKT** over the trailing 90 days — but **70%** of every block reward is diverted to the non-circulating community pool, so only the **0.88M AKT** paid to stakers actually reaches the tradable float. Against that, the Burn-Mint Equilibrium buy-and-burn retired about **0.81M AKT** on real compute usage. The MrNasdog Pressure Framework reads **+0.02%** net supply, essentially flat, and our supply monitor agrees at **+0.26%** — a gap of just **0.24 percentage points**, inside tolerance, so no data-conflict chip ships.

## The verdict, in one paragraph

For the 90-day window opening **Aug 3 2026**, the MrNasdog Pressure Framework reads **AKT at +0.02% net** for both the trailing and forward windows — the staking mint and the Burn-Mint Equilibrium burn very nearly cancel each other out. Our supply monitor reads **+0.26%** for the trailing window, a gap of **0.24 percentage points** that stays inside the framework's 0.5-point tolerance, so no monitor-gap chip appears on the AKT overview. The small residual is diffuse community-pool grant spending reaching the market — a continuous, uncoordinated flow the framework does not book as a discrete release. Worth noting: a prior read of AKT carried a **+11%** monitor figure, but that was a one-time circulating-supply recount of already-minted AKT, and it has now rolled out of the 90-day window, leaving the monitor clean. AKT is best characterised as **a low-inflation Cosmos compute chain whose usage-linked burn holds its tradable supply near flat**.

## Sell pressure: where new AKT comes from

Sell #1 — protocol inflation — is about **0.88M AKT** per 90 days, and the mechanism has a twist that most trackers miss. Akash's mint module runs at a fixed **4%** annual inflation, its hard ceiling, producing roughly **2.9M AKT** of gross new supply over the window. But Akash sets its community tax at **70%**, so 70% of every block reward is routed to the community pool — a governance-controlled treasury that sits outside the circulating supply — and only the remaining **30%**, about **0.88M AKT**, is distributed to stakers and reaches the market. Bonded stake sits near **30%**, far below Akash's **67%** target, which pins inflation at the 4% cap and keeps it from falling.

Sell #2 — vesting unlocks — is **zero**, and permanently so: AKT finished vesting on **Mar 25 2023**, so every investor, team and early-backer allocation is fully unlocked with no cliff or linear release left to come. Sell #3 — foundation and unscheduled unlocks — is also **zero** this window; the community pool holds about **3.71M AKT** and spends on grants and ecosystem work through governance, but that outflow is diffuse rather than a single coordinated release, so it books zero and is monitored. Sell #4 — long-term locked or bankruptcy — is **zero**: no bankruptcy estate or court-ordered distribution touches AKT.

## Buy pressure: where new AKT goes

Buy #1 — programmatic buyback — is about **0.81M AKT**, and it is the structural counterweight to the mint. Akash's Burn-Mint Equilibrium, live since **Mar 23 2026**, ties token demand directly to network usage: every on-chain compute payment market-buys AKT and burns it, issuing a non-transferable settlement credit to providers instead of paying them in freshly moved AKT. The net burn ran from about **5,950 AKT** a day at launch to about **11,105 AKT** a day by late July, retiring roughly **0.81M AKT** over the 90 days to **Aug 3 2026**. Because the burned AKT is destroyed, it needs no offsetting sell-side row.

Buy #2 — protocol fee burn — is **zero** as a separate line: Akash has no EIP-1559-style base-fee burn, and its ordinary transaction fees are paid to stakers rather than destroyed, so the only burn on the network is the Burn-Mint Equilibrium buy-and-burn already counted in Buy #1. Buy #3 — foundation buy — is **zero**: there is no discretionary open-market AKT buying by the foundation or treasury. Buy #4 — new long-term lock — is **zero** as well; no new multi-year AKT lock or escrow contract was announced in the window.

## Foundation and overhang

The one team-controlled overhang on Akash is the community pool, and it is easy to size because the chain publishes it directly: it holds about **3.71M AKT** today. The pool is fed by **70%** of every block reward — roughly **2.0M AKT** flows into it over a 90-day window — and it is drawn down through governance proposals for grants, market-making and ecosystem programs, which is why its balance stays roughly stable rather than compounding. That spending is the mechanism by which most new AKT eventually reaches the market, but it arrives as many small grants to many recipients rather than a single dump, so the framework tracks the pool as an overhang instead of booking a discrete release. The last large draw was a **1M AKT** market-making loan approved **Mar 6 2026**, before this window opened. If the community pool balance falls sharply between refreshes through a single large distribution, that outflow enters Sell #3 at the next refresh.

## How AKT compares to other Cosmos staking chains

AKT belongs to the uncapped-per-year but max-capped Cosmos-SDK staking class — sovereign Layer 1s like Cosmos Hub (ATOM) and Osmosis (OSMO) that mint new tokens continuously to pay stakers on a bonded-ratio curve. Structurally, AKT is on the low-inflation end of that group. Its **4%** mint is modest to begin with, and its unusually high **70%** community tax means most of that mint never touches the tradable float — a sharp contrast to chains that route the large majority of block rewards straight to delegators, where the full emission hits circulating supply.

What genuinely sets AKT apart from most of its Cosmos peers is the Burn-Mint Equilibrium. A typical Cosmos staking chain has no burn at all: its supply only grows, and the sole question is how fast. Akash added a demand-linked destruction mechanism that scales with real compute revenue, so on Akash the buy side is not zero — it is a live burn that currently offsets almost the entire staker-facing mint. That makes AKT behave less like a pure inflation token and more like a fee-burning network whose deflationary force rises and falls with usage, closer in spirit to a chain that burns base fees than to a plain staking L1.

The trade-off is that Akash's burn is only as strong as its compute demand. Base-fee burns on high-throughput chains run on relentless transaction volume; Akash's burn runs on how much GPU and CPU capacity tenants actually rent, which is smaller and more variable. For now the two forces are close to balanced, which is why AKT's tradable supply is near flat — but the balance tilts inflationary the moment usage softens and tilts deflationary if compute demand accelerates.

## What to watch in the next 90 days

Watch the Burn-Mint Equilibrium net burn rate, currently about **11,105 AKT** a day — because it scales with compute spend, a rise in Akash GPU rentals would push the buy side above the mint and flip AKT deflationary, while a fall would leave the mint ahead. Watch the bonded-stake ratio near **30%**: it holds inflation pinned at the 4% cap, and only a large move toward the 67% goal would let the mint ease off. Watch the community pool balance around **3.71M AKT** for any single large governance distribution, which would register as a discrete Sell #3 release. And watch for any governance proposal to change the **4%** inflation cap or the **70%** community tax — either would reset the sell ledger directly.

## Summary

Akash Network is a low-inflation Cosmos compute chain whose tradable supply is close to flat. A **4%** staking mint produces about **2.9M AKT** over 90 days, but its **70%** community tax keeps most of that off the market, leaving only **0.88M AKT** of staker rewards in circulation — and the Burn-Mint Equilibrium buy-and-burn retires about **0.81M AKT** against it. The framework reads **+0.02%** net and our monitor **+0.26%**, a **0.24-point** gap inside tolerance. The key variable is demand: AKT's burn is the first structural force pulling the token out of supply, and whether it grows past the mint depends entirely on how much compute Akash sells.

---

*MrNasdog Pressure Framework analysis of Akash Network (AKT), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 3 2026.*

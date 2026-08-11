---
title:         "GRT Inflation Analysis · August 2026 · The mint is on a chain the supply count never looks at"
description:   "The Graph mints 120.73 GRT per block on its layer 2 and burned only ~57.7K in 90 days. Framework reads +0.63% net; our monitor -0.10% (gap 0.73pp, monitor-gap chip ships)."
canonical_url: "https://mrnasdog.com/research/grt/inflation"
tags:          ["crypto", "grt", "the-graph", "infrastructure"]
published:     true
---

*Originally published at [mrnasdog.com/research/grt/inflation](https://mrnasdog.com/research/grt/inflation)*

# GRT Inflation Analysis · August 2026 · The mint is on a chain the supply count never looks at

The Graph mints **120.73 GRT** every block to pay indexers, and over the 90 days to **Aug 11 2026** that produced **~68.29M** new GRT — all of it created on the Arbitrum layer 2, where The Graph network actually runs. The burn side of the tokenomics, the **1%** curation tax and the **1%** query-fee protocol tax, removed **~57.7K GRT** in the same window: less than **0.1%** of the issuance it is meant to offset. Vesting is finished, there is no buyback, and GRT has **no maximum supply**. The MrNasdog Pressure Framework reads **+0.63% net** per 90 days — about **2.6%** a year — against a supply monitor reading **-0.10%**, a gap of **0.73 percentage points** that ships with a monitor-gap flag. GRT is **a quietly inflationary work token whose inflation is invisible on the chain most people watch**.

## A correction to our own prior reading

This build overturns the previous one. Our earlier pass read GRT as **flat, 0.00% net**, on the reasoning that burns and reclaimed rewards absorbed the entire issuance. That was wrong, for a specific and findable reason: it read a bridge gateway holding a **zero** balance and never looked at the bridge escrow contract holding **2.86B GRT**.

The mechanic is this. Layer-2 token supply *fell* by **7.40M** across the window, which looks like proof nothing was minted. It is not. Net bridge **withdrawals** of **75.63M GRT** — burned on the layer 2, released from escrow on the Ethereum side — more than covered the new issuance and hid it. Netting out the escrow inverts the picture: **68.29M** of genuine new supply was created. Measured burns are **~57.7K GRT**, **0.08%** of the roughly **77.9M** offset the prior build inferred. There was no offset. There was a bridge.

## The verdict, in one paragraph

For the 90-day window ending **Aug 11 2026**, the framework reads **GRT at +0.63% net** — a sell side of **~68.29M GRT** against a buy side of **~57.7K GRT**, on a counted circulating base of **~10.80B**. The forward window reads the same **+0.63%**: the per-block issuance rate is identical at both ends of the window and no dated supply event falls into the next 90 days. Our supply monitor reads **-0.10%** over the same trailing window, a gap of **0.73 percentage points**, over tolerance, so a monitor-gap flag ships. The reason is mechanical rather than a disagreement about facts: the Ethereum GRT contract held at **10,800,262,816.048214** at both ends of the window, to the wei, because reward issuance moved to the layer 2 years ago — while the layer-2 contract minted **~68.29M** new GRT over the same days. Any supply series built on the Ethereum contract alone reports GRT as flat forever. Add both chains and net out the bridge, and real network supply moved from **11,486.92M** to **11,573.66M**.

## Sell pressure: where new GRT comes from

Sell #1, protocol inflation, is **~68.29M GRT** and it is the entire sell side of this ledger. The Graph is an uncapped work token: it launched in **Dec 2020** with **10 billion** GRT and a documented target of roughly **3%** annual issuance to reward indexers for allocating stake to subgraphs. That target is a fixed per-block figure — the rewards manager returned **120.73 GRT** per block at both ends of this window, so the rate did not change mid-window and the forward projection uses the same run rate.

Over the **645,796** Ethereum blocks the window covers, the schedule permitted **~77.97M GRT**. The framework does not ship that ceiling. Reading every mint event on the layer-2 token shows **68,290,627** GRT actually minted, all of it to the subgraph service contract. The **~9.68M** difference is issuance that was never created: rewards are minted only when an indexer collects, and only when it passes the eligibility check governance added to tie rewards to real service quality. That shortfall is *unminted issuance*, not a buy-side offset — it shrinks the sell side rather than adding to the buy side. Realised beats scheduled, so **68.29M** is the number we ship.

Sell #2, vesting unlocks, is **zero**, and this is one of the few large-cap tokens where that is genuinely finished rather than merely paused. The original distribution ran early team and advisors over four years, the core development company over five, and the foundation on a ten-year schedule. Every token-lock manager contract that administered those schedules — on both chains — holds **0 GRT** today and held **0 GRT** at the start of the window, and GRT is publicly reported as fully unlocked with no next unlock date. Sell #3, foundation and unscheduled unlocks, is also **zero**: the foundation and the council treasury both hold GRT, but neither publishes a wallet address, the last disclosed foundation sale was the **2022** strategic round, and no release was observed or announced inside this window. Sell #4, long-term locked or bankruptcy, is **zero** — no estate, trustee schedule or court-ordered distribution touches GRT.

## Buy pressure: where new GRT goes

Buy #2, protocol fee burn, is the only non-zero entry, at **~57.7K GRT**, and its size is the most important finding here. The Graph documents three burns: a **1%** curation tax when a curator signals on a subgraph, a **1%** protocol tax on query fees, and a delegation tax on delegated stake. Read as burn events over the window, curation burned **~13.0K GRT**, query payments burned **~44.7K GRT**, and the staking contract burned under **1 GRT** — because the Horizon upgrade removed the delegation tax that used to be the largest of the three. The project's own tokenomics documentation suggests roughly **1%** of supply is burned annually, about **27M GRT** a quarter; measured, the burn came in at roughly **0.2%** of that. Any claim that GRT is net-neutral because burns cancel the mint does not survive contact with the burn events.

The rest of the buy ledger is empty. Buy #1, programmatic buyback, is **zero**: The Graph has never run a protocol buyback or a treasury repurchase, and no proposal to create one was open in the window — the "GRT buyback and burn" posts circulating on blogging platforms are from impersonation accounts, not the project. Buy #3, foundation buy, is **zero**; the foundation spends its GRT treasury on grants and core development rather than bidding for the token. Buy #4, new long-term lock, is **zero**: indexer and delegator stake sits at **~2.08B GRT** and actually **fell** across the window, from **2,084.5M** to **2,079.5M**, and stake is withdrawable after a thawing period, so it is not the kind of lock that removes float.

## Foundation and overhang

The Graph's overhang picture is unusually clean for a 2020-vintage token. The vesting overhang is **gone** — the four token-lock managers on Ethereum and the three on the layer 2 all read **0 GRT**. What remains is the **foundation treasury** and the **council-controlled community treasury**, which fund grants and core development; neither publishes a wallet address, so both are opaque overhangs walked through official disclosure rather than read from a contract. There is no buyback accumulation wallet to track, because there is no buyback.

The overhang that matters most for GRT is not a wallet at all — it is the **~774M GRT** gap between the **10,799.87M** the market counts as circulating and the **11,573.66M** that actually exists across both chains. That difference is five and a half years of layer-2 reward issuance the Ethereum contract never recorded, and it grows by roughly **68M** every quarter. The standing trigger applies to the wallets we can see: if the foundation or council treasury balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How GRT compares to other uncapped work tokens

GRT belongs to the class of **uncapped service networks that pay their supply-side workers in freshly minted tokens** — the structural family of decentralised storage, compute and bandwidth markets. Within that class the differentiator is whether the demand side burns as fast as the supply side mints. The Graph was designed to work that way, and at high query volume it would. The measurement says demand is not there yet: a **~57.7K** burn against a **~68.29M** mint is a ratio of about **1 to 1,180**.

Against a hard-capped chain like Bitcoin the comparison is structural — a halving schedule guarantees issuance falls, while GRT's **120.73** per block only falls if governance votes it down. Against a proof-of-stake layer 1 running **4%** to **6%** issuance with a base-fee burn, GRT is milder on the headline rate but weaker on the offset, because an L1 burns gas on every transaction whereas The Graph burns only on paid queries and curation. Against an exchange token with a revenue-funded burn, GRT has no equivalent lever at all. GRT today is a **mild, honest, permanent** inflation — small enough not to dominate the price story, structural enough that it never stops on its own.

## What to watch in the next 90 days

First, whether the **issuance allocator** contract is switched on. It is deployed on the layer 2 but holds no GRT and its getters do not respond, so it is not yet wired; once it is, governance can split issuance across destinations, and it is the one piece of machinery that could change the **120.73** per block figure without a hard fork. Second, the pending contract implementations for the subgraph service and the payments escrow, deployed **Jul 23 2026** but not activated — an upgrade landing mid-window would re-base the forward projection. Third, the **rewards-eligibility** mechanism: **~9.68M GRT** of scheduled issuance was never minted this window, and a tighter bar pushes realised issuance further below the schedule. Fourth, query-fee volume, the only variable that can move the burn side off **~57.7K** a quarter. Fifth, any foundation or council treasury disclosure, since both are opaque and only disclosure can reveal a sale.

## Summary

The Graph is an uncapped work token that mints **120.73 GRT** per block on its layer 2 and burned only **~57.7K GRT** in the 90 days to **Aug 11 2026**, giving a Pressure Framework reading of **+0.63% net** per quarter, or roughly **2.6%** a year. The ledger is short: vesting is finished, there is no buyback, no bankruptcy estate and no new lock, so protocol issuance is the whole picture. The key risk is that the offset is usage-driven — the burn scales with paid queries, and at today's volume it cancels less than **0.1%** of the mint. The key caveat is measurement: because the Ethereum contract has been frozen at **10,800,262,816** for over a year, most supply counters show GRT as flat when the network is in fact **11.57B** and growing, so a reader relying on a single-chain figure understates GRT's inflation by the entire amount of it.

---

*MrNasdog Pressure Framework analysis of The Graph (GRT), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 11 2026.*

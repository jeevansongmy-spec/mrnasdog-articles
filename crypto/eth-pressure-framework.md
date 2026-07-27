---
title: "ETH Inflation Analysis · July 2026 · Mixed flows, supply roughly steady"
description: "Ethereum minted ~254K ETH to validators and burned only ~5.2K ETH over 90 days — a net +0.21%. The EIP-1559 burn keeps fading as activity sits on Layer 2."
canonical_url: "https://mrnasdog.com/research/eth/inflation"
tags: ["crypto", "ethereum", "layer1", "eip-1559"]
published: true
---

> Originally published at **[mrnasdog.com/research/eth/inflation](https://mrnasdog.com/research/eth/inflation)** by MrNasdog.

Ethereum minted about **254K ETH** to validators over the last 90 days and destroyed only about **5.2K ETH** through the EIP-1559 base-fee burn, leaving net supply **+0.21%** across the window. Validator issuance is now the whole story: the burn that once cancelled it out has collapsed to roughly **58 ETH a day** because rollup data and everyday activity sit on cheap Layer 2 blob space rather than on mainnet. Ethereum has no hard cap, no vesting schedule and no buyback, so the only two levers that move ETH supply are issuance and the burn — and issuance is winning.

## The verdict, in one paragraph

Over the 90 days to **Jul 27 2026** the MrNasdog Pressure Framework reads ETH at **+0.21%** net supply growth — **254K ETH** of validator issuance against **5.2K ETH** of base-fee burn on a circulating base of **120.68M ETH**. The next 90 days project to **+0.21%** as well: issuance drifts up to about **257K ETH** because the staked pool keeps growing, while the burn is carried forward at the same rate. The inflation monitor reads **-0.02%** over the same window, a gap of **0.22 percentage points** — inside the framework's 0.5pp tolerance, so no data-conflict flag applies. The monitor derives circulating supply from market cap divided by price, which carries enough day-to-day rounding noise on an asset this large to sit anywhere in the near-zero band; the framework reads the chain's own supply, which rose about **249K ETH** net across the window. Both agree on the shape. ETH in July 2026 is **mildly inflationary on a fading burn** — not the "ultrasound money" of 2022, and not a runaway emitter either.

## Sell pressure: where new ETH comes from

Ethereum has exactly one mint. Validator issuance under proof-of-stake produced **254K ETH** over the window, about **2,821 ETH a day**. The rate is not a fixed number: the protocol pays a total base reward each epoch proportional to the square root of the total staked balance, so issuance rises as more ETH is staked but the yield per validator falls. Backing that figure out of the reward curve implies roughly **38.5M ETH** staked across the window, consistent with independent staking data showing the pool climbing from about 35.6M at the start of 2026 toward 40M by mid-year. Because the pool is still growing, the forward projection is slightly higher at **257K ETH** for the next 90 days.

Every other sell row on Ethereum is zero, and zero by design. Vesting unlocks are zero for good: the 2014 crowdsale and both founding endowments finished distributing by 2017, and no vesting contract, cliff or team lock exists on Ethereum today — a genuinely rare position for an asset of this size. Foundation and unscheduled unlocks are zero because Ethereum has no non-circulating bucket at all; every ETH that exists is already counted as circulating, so there is nothing left to unlock into the float. Long-term locked and bankruptcy supply is zero because the large 2022–23 estates settled their ether claims in cash rather than in coin, leaving no ETH distribution schedule running against the market.

## Buy pressure: where new ETH goes

The EIP-1559 base-fee burn is Ethereum's only removal mechanism, and over this window it destroyed just **5.2K ETH** — roughly **58 ETH a day**. Measured across the window's **645,582** blocks, the median base fee was about **0.14 gwei** against a gas limit near **60M**: mainnet gas is effectively at the floor. The reason is the blob market. Since the Fusaka upgrade and the two blob-parameter forks that followed it, Ethereum targets 14 blobs per block and allows up to 21, so rollups post their data for almost nothing and the fee pressure that used to burn thousands of ETH a day never reaches the execution layer. The blob base fee itself sits near its minimum, contributing only a few ETH of burn across the entire window. The decay is still running: the burn averaged about **86 ETH a day** in the first half of the window and about **27 ETH a day** in the last 30 days.

The remaining buy rows are zero. There is no programmatic buyback — Ethereum mints validator rewards rather than purchasing them, and the protocol holds no treasury it could bid with. There is no Foundation buy: the Ethereum Foundation funds itself by selling ETH, not accumulating it. And there is no new long-term lock, because while close to a third of all ETH is staked, withdrawals have been open since 2023 and stakers can exit within days — that is holder-driven yield, not a programme that removes coins from the market.

## Foundation and overhang

The one team-controlled overhang on Ethereum is the Ethereum Foundation treasury, roughly **104K ETH** in total across operating wallets and its staked position. On-chain, the Foundation's main multisig held **7,774 ETH** and its grants wallet **221 ETH** at the last read on **Jul 27 2026**; the balance sits in staked positions and further disclosed addresses. The Foundation has been an active seller under the treasury policy it published in 2025, which sets annual operating spend as a share of treasury value and triggers ETH sales when the fiat buffer falls short: **10,000 ETH** sold over the counter on **May 1 2026**, another **10,000 ETH** the following week, and **3,750 ETH** on **Jul 19 2026**. A further **1,000 ETH** left the main multisig in the four days to Jul 27 2026.

None of that is booked as sell pressure in the ledger, and the reason is structural rather than generous. Because Ethereum has no non-circulating bucket, the Foundation's ETH is already inside the circulating supply the framework divides by — a Foundation sale rotates custody of coins the denominator has already counted, so recording it would put a non-supply quantity into a net-supply equation. The Foundation treasury is therefore tracked as an overhang rather than a row value, and the trigger stands: if the Foundation's balance falls between refreshes, that outflow enters the Foundation row at the next refresh. At roughly 0.09% of supply, the whole treasury is small next to a single quarter of issuance.

## How ETH compares to other proof-of-stake Layer 1 chains

Against the capped, halving-model chains, ETH sits in a different category entirely. A hard-capped proof-of-work coin has a schedule that is knowable years ahead and immune to usage; Ethereum has no cap, and its issuance floats with how much ETH is staked. That makes ETH's supply path a function of validator behaviour rather than of a calendar. The compensation is the burn — capped chains have no removal mechanism at all, whereas Ethereum can in principle run negative. In 2021–23 it did. In 2026 it does not, because the burn depends on demand for mainnet execution and that demand has migrated to Layer 2.

Against other uncapped continuous-emission Layer 1s, ETH is at the quiet end. Chains that mint on a fixed percentage curve typically run supply growth north of 3% a year regardless of activity; Ethereum's **+0.21%** per 90 days annualises to roughly **0.85%**, an order of magnitude milder, and it is partially self-limiting because a growing staked pool raises issuance only with the square root of stake. The structural risk is the mirror image of the structural strength: an emitter whose only offset is fee burn is hostage to where the fees are earned. Ethereum deliberately routed its own transaction volume to rollups, which is good for users and bad for the burn. Chains that keep execution on the base layer — exchange tokens with quarterly buybacks funded by revenue, or Layer 1s that burn a fixed share of every fee — do not have that dependency, because their removal mechanism is tied to revenue rather than to congestion.

## What to watch in the next 90 days

The Glamsterdam upgrade, headlined by EIP-7732 enshrined proposer-builder separation and EIP-7928 block-level access lists, entered its final devnet phase on **Jun 16 2026** and is targeted for mainnet after this window; it changes block production and gas accounting but neither the issuance curve nor the burn rule, so it is a watch line for base-fee demand rather than a ledger event. The third and fourth blob-parameter forks are being held pending telemetry review of the first two — a further blob-capacity increase would push mainnet fees, and the burn, lower still. Total staked ETH is the single most important number for the sell row: every million ETH added to the pool raises annual issuance by roughly 13K ETH. The Ethereum Foundation's next treasury sale, which its policy ties to quarterly buffer checks, would be the next event to move the overhang. And a sustained recovery in mainnet base fees above roughly 1 gwei would be the only realistic path back toward neutral supply.

## Summary

The MrNasdog Pressure Framework reads Ethereum at **+0.21%** net supply growth over the 90 days to **Jul 27 2026** and projects **+0.21%** for the next 90 — mildly inflationary, and steady. The structural mechanism is simple and unusually clean: validator issuance of about **254K ETH** is the only mint, the EIP-1559 base-fee burn of about **5.2K ETH** is the only removal, and there is no vesting, no unlock schedule, no buyback and no bankruptcy estate anywhere in the ledger. The key risk is that the burn keeps shrinking: at **0.14 gwei** median base fees, mainnet is already near the floor, and further Layer 2 scaling pushes it lower. The ceiling on the other side is the square-root issuance curve, which means even a much larger staked pool cannot push ETH supply growth far above **1% a year**.

---

*MrNasdog Pressure Framework analysis of ETH, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Jul 27 2026.*

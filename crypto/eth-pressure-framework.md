---
title: "ETH Inflation Analysis · August 2026 · Mixed flows, supply roughly steady"
description: "Ethereum minted ~261K ETH to validators and burned only ~5.2K ETH over 90 days — a net +0.21%. The EIP-1559 burn keeps fading as activity sits on Layer 2."
canonical_url: "https://mrnasdog.com/research/eth/inflation"
tags: ["crypto", "ethereum", "layer1", "eip-1559"]
published: true
---

> Originally published at **[mrnasdog.com/research/eth/inflation](https://mrnasdog.com/research/eth/inflation)** by MrNasdog.

Ethereum minted about **261K ETH** to validators over the last 90 days and destroyed only about **5.2K ETH** through the EIP-1559 base-fee burn, leaving net supply **+0.21%** across the window. Validator issuance is now the whole story: the burn that once cancelled it out has collapsed to roughly **58 ETH a day** because rollup data and everyday activity sit on cheap Layer 2 blob space rather than on mainnet. Ethereum has no hard cap, no vesting schedule and no buyback, so the only two levers that move ETH supply are issuance and the burn — and issuance is winning.

## The verdict, in one paragraph

Over the 90 days to **Aug 9 2026** the MrNasdog Pressure Framework reads ETH at **+0.21%** net supply growth — **261K ETH** of validator issuance against **5.2K ETH** of base-fee burn on a circulating base of **120.68M ETH**. The next 90 days project to **+0.22%**: issuance drifts up to about **266K ETH** because the staked pool keeps growing, while the burn is carried forward at the same rate. The inflation monitor reads **+0.005%** over the same window, a gap of **0.21 percentage points** — inside the framework's 0.5pp tolerance, so no data-conflict flag applies. The monitor derives circulating supply from market cap divided by price, which carries enough day-to-day rounding noise on an asset this large to sit anywhere in the near-zero band; the framework reads issuance off the staking curve. Both agree Ethereum is close to steady. ETH in August 2026 is **mildly inflationary on a fading burn** — not the "ultrasound money" of 2022, and not a runaway emitter either.

## Sell pressure: where new ETH comes from

Ethereum has exactly one mint. Validator issuance under proof-of-stake produced about **261K ETH** over the window, roughly **2,900 ETH a day**. The rate is not a fixed number: the protocol pays a total base reward each epoch proportional to the square root of the total staked balance, so issuance rises as more ETH is staked but the yield per validator falls. The staked pool is at an all-time high — about **41.4M ETH**, close to **34%** of all ETH, secured by roughly **1.1M validators** — which is exactly why base staking rewards have fallen to around **2.6%**. Because the pool is still growing, the forward projection is slightly higher at **266K ETH** for the next 90 days.

Every other sell row on Ethereum is zero, and zero by design. Vesting unlocks are zero for good: the 2014 crowdsale and both founding endowments finished distributing by 2017, and no vesting contract, cliff or team lock exists on Ethereum today — a genuinely rare position for an asset of this size. Foundation and unscheduled unlocks are zero as a supply row because Ethereum has no non-circulating bucket at all; every ETH that exists is already counted as circulating, so a Foundation sale rotates custody rather than adding coins to the float. Long-term locked and bankruptcy supply is zero because the large 2022–23 estates settled their ether claims in cash rather than in coin.

## Buy pressure: where new ETH goes

The EIP-1559 base-fee burn is Ethereum's only removal mechanism, and over this window it destroyed just **5.2K ETH** — roughly **58 ETH a day**. Mainnet gas is effectively at the floor, and the reason is the blob market. Since the Fusaka upgrade and the two blob-parameter forks that followed it, Ethereum targets far more blob capacity per block, so rollups post their data for almost nothing and the fee pressure that used to burn thousands of ETH a day never reaches the execution layer. The blob base fee itself sits near its minimum, contributing only a few ETH of burn across the entire window. The upshot is blunt: the burn no longer comes close to matching validator issuance, and the "ultrasound money" deflation of 2021–23 is off for as long as activity stays on Layer 2.

The remaining buy rows are zero. There is no programmatic buyback — Ethereum mints validator rewards rather than purchasing them, and the protocol holds no treasury it could bid with. There is no Foundation buy: the Ethereum Foundation funds itself by selling ETH, not accumulating it. And there is no new long-term lock, because while about a third of all ETH is staked, withdrawals have been open since 2023 and stakers can exit within days — that is holder-driven yield, not a programme that removes coins from the market.

## Foundation and overhang

The one team-controlled overhang on Ethereum is the Ethereum Foundation treasury, held across operating wallets and a staked position. The Foundation has been an active seller under the treasury policy it published in 2025, which sets annual operating spend at roughly **15%** of treasury value and triggers ETH sales to fund research, grants and donations: it finalised a **10,000 ETH** over-the-counter sale on **May 1 2026** and sold roughly **20,000 ETH** more across a week of treasury restructuring, alongside smaller conversions to stablecoins earlier in the year. Vitalik Buterin has since signalled the Foundation will sell **less** ETH going forward, prioritising long-term sustainability over the breadth of its spending.

None of that is booked as sell pressure in the ledger, and the reason is structural rather than generous. Because Ethereum has no non-circulating bucket, the Foundation's ETH is already inside the circulating supply the framework divides by — a Foundation sale rotates custody of coins the denominator has already counted, so recording it would put a non-supply quantity into a net-supply equation. The Foundation treasury is therefore tracked as an overhang rather than a row value, and the trigger stands: if the Foundation's balance falls between refreshes, that outflow enters the Foundation row at the next refresh. Even at the pace it has been selling, the whole programme is small next to a single quarter of issuance.

## How ETH compares to other proof-of-stake Layer 1 chains

Against the capped, halving-model chains, ETH sits in a different category entirely. A hard-capped proof-of-work coin has a schedule that is knowable years ahead and immune to usage; Ethereum has no cap, and its issuance floats with how much ETH is staked. That makes ETH's supply path a function of validator behaviour rather than of a calendar. The compensation is the burn — capped chains have no removal mechanism at all, whereas Ethereum can in principle run negative. In 2021–23 it did. In 2026 it does not, because the burn depends on demand for mainnet execution and that demand has migrated to Layer 2.

Against other uncapped continuous-emission Layer 1s, ETH is at the quiet end. Chains that mint on a fixed percentage curve typically run supply growth north of 3% a year regardless of activity; Ethereum's **+0.21%** per 90 days annualises to roughly **0.85%**, an order of magnitude milder, and it is partially self-limiting because a growing staked pool raises issuance only with the square root of stake. The structural risk is the mirror image of the structural strength: an emitter whose only offset is fee burn is hostage to where the fees are earned. Ethereum deliberately routed its own transaction volume to rollups, which is good for users and bad for the burn. Chains that keep execution on the base layer — exchange tokens with quarterly buybacks funded by revenue, or Layer 1s that burn a fixed share of every fee — do not have that dependency.

## What to watch in the next 90 days

The Glamsterdam upgrade, headlined by EIP-7732 enshrined proposer-builder separation and EIP-7928 block-level access lists, is targeted for mainnet around the end of **August 2026**; it changes block production and gas accounting but neither the issuance curve nor the burn rule, so it is a watch line for base-fee demand rather than a ledger event. The next blob-parameter forks are being held pending telemetry review — a further blob-capacity increase would push mainnet fees, and the burn, lower still. Total staked ETH is the single most important number for the sell row: every million ETH added to the pool raises annual issuance by roughly **13K ETH**, and the pool just hit an all-time high near **41.4M**. The Ethereum Foundation's next treasury sale would be the next event to move the overhang. And a sustained recovery in mainnet base fees above roughly **1 gwei** would be the only realistic path back toward neutral supply.

## Summary

The MrNasdog Pressure Framework reads Ethereum at **+0.21%** net supply growth over the 90 days to **Aug 9 2026** and projects **+0.22%** for the next 90 — mildly inflationary, and steady. The structural mechanism is simple and unusually clean: validator issuance of about **261K ETH** is the only mint, the EIP-1559 base-fee burn of about **5.2K ETH** is the only removal, and there is no vesting, no unlock schedule, no buyback and no bankruptcy estate anywhere in the ledger. The key risk is that the burn keeps shrinking: mainnet is already near the floor, and further Layer 2 scaling pushes it lower. The ceiling on the other side is the square-root issuance curve, which means even a much larger staked pool cannot push ETH supply growth far above **1% a year**.

---

*MrNasdog Pressure Framework analysis of ETH, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 9 2026.*

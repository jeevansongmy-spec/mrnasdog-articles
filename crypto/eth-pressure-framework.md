---
title: "ETH Inflation Analysis · July 2026 · The burn stays low, so issuance leads"
description: "The EIP-1559 burn stays low: ~0.252M ETH minted vs only ~0.005M burned over 90 days. Framework reads +0.20% net — mildly inflationary while mainnet gas stays cheap."
canonical_url: "https://mrnasdog.com/research/eth/inflation"
tags: ["crypto", "ethereum", "layer1", "eip-1559"]
published: true
---

> Originally published at **[mrnasdog.com/research/eth/inflation](https://mrnasdog.com/research/eth/inflation)** by MrNasdog.

Ethereum is a proof-of-stake Layer 1 with no supply cap. Proof-of-stake issuance now adds about **0.252M ETH** over 90 days while the EIP-1559 base-fee burn — collapsed since most activity moved to Layer 2 — removes only about **0.005M ETH**. Net is roughly **+0.20%** against the inflation monitor's **−0.0229%**, a gap of **0.22 percentage points** — inside tolerance. ETH is mildly inflationary while mainnet gas stays cheap.

## The verdict, in one paragraph

For the 90-day window ending July 14 2026, the MrNasdog Pressure Framework reads **ETH at +0.20% net**. The independent inflation monitor reads **−0.0229%**, a gap of **0.22 percentage points** — inside the 0.5pp tolerance, so no data-conflict chip is raised, and both readings sit in the same near-zero band. The structural picture is unchanged from spring: Ethereum mints new ETH to pay validators and burns ETH on every block through EIP-1559, but with roughly **39.7M ETH** staked the issuance runs well ahead of a collapsed burn. ETH is a **mildly inflationary supply on the active float** — the burn no longer offsets issuance because the fees that fed it moved to Layer 2.

## Sell pressure: where new ETH comes from

Sell #1 — protocol inflation — is the only live source of new ETH. Proof-of-stake issuance pays validators about **2,800 ETH a day**, or roughly **0.252M ETH** over the 90-day window. Issuance scales with the square root of the total amount staked, and with about **39.7M ETH** staked (near 33% of supply) the mint has settled at this level. This figure is read from the on-chain net supply change plus the base-fee burn, so it reflects what the chain actually issued, not a schedule estimate; the Merge replaced miner block rewards with this far smaller staking reward.

Every other sell row is zero. Sell #2 — vesting unlocks — is zero because Ethereum has no vesting schedule and no locked team allocation dripping into the market; the original 2014 sale and genesis allocations have long since fully circulated. Sell #3 — Foundation and unscheduled unlocks — is zero: the Ethereum Foundation holds a treasury but runs no scheduled release programme, and its operational ETH sales convert already-circulating treasury to stablecoins rather than minting new supply. Sell #4 — long-term locked or bankruptcy — is zero; there is no bankruptcy estate, and the **39.7M ETH** that is staked locks supply rather than adding it.

## Buy pressure: where new ETH goes

Buy #2 — protocol fee burn — used to offset issuance, but it stays collapsed. EIP-1559 burns the base fee of every transaction on every block, permanently destroying that ETH. Over this window the burn runs at only about **0.005M ETH** — roughly 1,750 ETH a month — far below issuance. After the Dencun and Fusaka upgrades moved rollup data to cheap blobs and most user activity migrated to Layer 2, mainnet gas fell to historic lows near 0.2 gwei, so the base fee being burned is tiny. The burn rises again only when mainnet demand returns; until then it cannot keep pace with the mint.

The rest of the buy ledger is zero. Buy #1 — programmatic buyback — is zero because validator rewards are paid from fresh issuance, not from market purchases; there is no treasury buyback. Buy #3 — Foundation buy — is zero; the Foundation runs no accumulation programme. Buy #4 — new long-term lock — is zero as a programmatic line: staking does lock ETH for yield, but it is validator-driven rather than a programme with an announced lock quantum, so it is not booked as a buy-side flow.

## Foundation and overhang

The one tracked overhang is the **Ethereum Foundation treasury**, which holds roughly 0.26% of supply. The Foundation publishes no scheduled release programme; under its treasury policy it sells small amounts of already-circulating ETH to stablecoins to fund research and grants, and stakes the balance. Because these sales move already-circulating treasury rather than mint new ETH, and the quanta are a tiny fraction of supply, the framework books Sell #3 at zero flow and monitors the balance on a roughly bi-weekly web walk. A separate **June 2026** governance proposal would let a stake-weighted majority redirect up to **10%** of validator staking rewards toward ecosystem funding; it is still a research-forum debate, not adopted, and would reallocate rewards rather than change issuance, so it does not touch the ledger. If the Foundation's balance falls between refreshes by an amount large enough to register, the outflow enters Sell #3 at the next refresh.

## How ETH compares to other uncapped Layer 1 chains

Ethereum belongs to the class of **uncapped, continuous-emission Layer 1s**, and it is the only major one that pairs issuance with a structural burn — but right now the burn is dormant. Solana issues continuously and burns only half of a tiny base fee, so its net stays clearly positive; ETH burns the full base fee of every mainnet transaction, which is why its net can collapse toward zero or below when mainnet is busy. Against capped halving chains like Bitcoin, the contrast is sharper still: Bitcoin's emission is fixed and falling on a schedule and there is no burn; ETH has no cap, can swing deflationary in busy periods, but reads mildly inflationary in quiet ones like this window.

The mechanism that makes ETH distinctive is that its supply is **demand-responsive**. More mainnet activity burns more base fee, pushing net supply down exactly when usage is highest; the migration of activity to Layer 2 does the opposite, draining the burn and letting issuance lead. No fixed-schedule chain has this property. For an inflation reading, that means ETH's number is less a property of tokenomics and more a property of where transactions settle — and right now they settle on cheaper rollups, so the EIP-1559 burn has thinned and ETH reads mildly inflationary.

## What to watch in the next 90 days

Watch the burn-versus-issuance balance, which is the entire story. First, mainnet activity: a sustained rise in mainnet transaction and blob demand would lift the burn and pull ETH back toward flat or deflationary, while continued L2 migration keeps issuance ahead. Second, the staking participation rate — now about 33%; if the share of ETH staked climbs further, issuance rises with it. Third, the June 2026 "validator redirected revenue" proposal and the broader capped-issuance reward-curve research — either could reshape validator economics, though neither is scheduled and neither changes gross issuance today. Fourth, the Glamsterdam upgrade, targeted for roughly the end of August 2026, which raises base-layer capacity and enshrines proposer-builder separation but does not alter monetary policy and could keep the burn low if demand does not follow. None of these is a dated ledger event; they are continuous variables the next refresh will re-read.

## Summary

ETH is mildly inflationary. Proof-of-stake issuance of about 0.252M ETH over the window is only weakly offset by an EIP-1559 base-fee burn of about 0.005M ETH, for a framework reading of +0.20% net against the monitor's −0.0229% — agreement within 0.22 percentage points. There is no vesting, no scheduled Foundation release, and no buyback; the only tracked overhang is the unscheduled Foundation treasury. The key variable is where activity settles, because the burn is demand-responsive and has thinned as users moved to Layer 2. Among uncapped Layer 1s, Ethereum is unique in pairing continuous issuance with a full base-fee burn — but that burn only bites when mainnet is busy, and right now it is not.

---

*MrNasdog Pressure Framework analysis of Ethereum (ETH), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 14 2026.*

---
title: "ETH Inflation Analysis · June 2026 · The burn collapsed, so issuance now leads"
description: "The EIP-1559 burn collapsed: ~0.259M ETH minted vs only ~0.006M burned over 90 days. Framework reads +0.21% net — mildly inflationary while mainnet gas stays cheap."
canonical_url: "https://mrnasdog.com/research/eth/inflation"
tags: ["crypto", "ethereum", "layer1", "eip-1559"]
published: true
---

> Originally published at **[mrnasdog.com/research/eth/inflation](https://mrnasdog.com/research/eth/inflation)** by MrNasdog.

Ethereum is a proof-of-stake Layer 1 with no supply cap. Proof-of-stake issuance now adds about **0.259M ETH** over 90 days while the EIP-1559 base-fee burn — collapsed since most activity moved to Layer 2 — removes only about **0.006M ETH**. Net is roughly **+0.21%** against the inflation monitor's **+0.0157%**, a gap of **0.19 percentage points** — inside tolerance. ETH has flipped from flat to mildly inflationary while mainnet gas stays cheap.

## The verdict, in one paragraph

For the 90-day window ending June 24 2026, the MrNasdog Pressure Framework reads **ETH at +0.21% net**. The independent inflation monitor reads **+0.0157%**, a gap of **0.19 percentage points** — inside the 0.5pp tolerance, so no data-conflict chip is raised; both readings agree supply is growing. The structural picture has shifted: Ethereum mints new ETH to pay validators and burns ETH on every block through EIP-1559, but with roughly 40.2M ETH staked the issuance has crept up while the burn has collapsed. ETH is now a **mildly inflationary supply on the active float** — the burn no longer offsets issuance because the fees that fed it moved to Layer 2.

## Sell pressure: where new ETH comes from

Sell #1 — protocol inflation — is the only live source of new ETH, and it is bigger than it was. Proof-of-stake issuance pays validators about **2,870 ETH a day**, or roughly **0.259M ETH** over the 90-day window. Issuance scales with the square root of the total amount staked, and with about **40.2M ETH** staked (near 33% of supply, well above the ~14M level where the protocol issues roughly 1,700 ETH a day) the mint has risen accordingly. This is the single mechanism that creates ETH; the Merge replaced miner block rewards with this far smaller staking reward.

Every other sell row is zero. Sell #2 — vesting unlocks — is zero because Ethereum has no vesting schedule and no locked team allocation dripping into the market; the original 2014 sale and genesis allocations have long since fully circulated. Sell #3 — Foundation and unscheduled unlocks — is zero: the Ethereum Foundation holds a treasury but runs no scheduled release programme, and its operational ETH sales convert already-circulating treasury to stablecoins rather than minting new supply. Sell #4 — long-term locked or bankruptcy — is zero; there is no bankruptcy estate, and the **40.2M ETH** that is staked locks supply rather than adding it.

## Buy pressure: where new ETH goes

Buy #2 — protocol fee burn — used to offset issuance, but it has collapsed. EIP-1559 burns the base fee of every transaction on every block, permanently destroying that ETH. Over this window the burn runs at only about **0.006M ETH** — roughly 2,000 ETH a month — far below issuance. After the Dencun upgrade moved rollup data to cheap blobs and most user activity migrated to Layer 2, mainnet gas fell to historic lows near 0.1 gwei, so the base fee being burned is tiny. The burn rises again only when mainnet demand returns; until then it cannot keep pace with the mint.

The rest of the buy ledger is zero. Buy #1 — programmatic buyback — is zero because validator rewards are paid from fresh issuance, not from market purchases; there is no treasury buyback. Buy #3 — Foundation buy — is zero; the Foundation runs no accumulation programme. Buy #4 — new long-term lock — is zero as a programmatic line: staking does lock ETH for yield, but it is validator-driven rather than a programme with an announced lock quantum, so it is not booked as a buy-side flow.

## Foundation and overhang

The one tracked overhang is the **Ethereum Foundation treasury**, which holds roughly 0.26% of supply. The Foundation publishes no scheduled release programme; under its treasury policy it sells small amounts of already-circulating ETH to stablecoins to fund research and grants — about **5,000 ETH to DAI in April 2026** via a gradual on-chain swap, plus a few thousand more to a treasury buyer in May 2026 — and stakes the balance. Because these sales move already-circulating treasury rather than mint new ETH, and the quanta are a tiny fraction of supply, the framework books Sell #3 at zero flow and monitors the balance on a roughly bi-weekly web walk. If the Foundation's balance falls between refreshes by an amount large enough to register, the outflow enters Sell #3 at the next refresh.

## How ETH compares to other uncapped Layer 1 chains

Ethereum belongs to the class of **uncapped, continuous-emission Layer 1s**, and it is the only major one that pairs issuance with a structural burn — but right now the burn is dormant. Solana issues continuously and burns only half of a tiny base fee, so its net stays clearly positive; ETH burns the full base fee of every mainnet transaction, which is why its net can collapse toward zero or below when mainnet is busy. Against capped halving chains like Bitcoin, the contrast is sharper still: Bitcoin's emission is fixed and falling on a schedule and there is no burn; ETH has no cap, can swing deflationary in busy periods, but reads mildly inflationary in quiet ones like this window.

The mechanism that makes ETH distinctive is that its supply is **demand-responsive**. More mainnet activity burns more base fee, pushing net supply down exactly when usage is highest; the migration of activity to Layer 2 does the opposite, draining the burn and letting issuance lead. No fixed-schedule chain has this property. For an inflation reading, that means ETH's number is less a property of tokenomics and more a property of where transactions settle — and right now they settle on cheaper rollups, so the EIP-1559 burn has thinned and ETH reads mildly inflationary.

## What to watch in the next 90 days

Watch the burn-versus-issuance balance, which is the entire story. First, mainnet activity: a sustained rise in mainnet transaction and blob demand would lift the burn and pull ETH back toward flat or deflationary, while continued L2 migration keeps issuance ahead. Second, the staking participation rate — now about 33% and rising; if the share of ETH staked climbs further, issuance rises with it. Third, any Foundation treasury movement large enough to surface in the monitor would promote Sell #3 from zero to a quantified row. Fourth, any protocol change to the issuance curve or to how blob fees are burned through a future upgrade. None of these is a dated event; they are continuous variables the next refresh will re-read.

## Summary

ETH has flipped from flat to mildly inflationary. Proof-of-stake issuance of about 0.259M ETH over the window is now only weakly offset by an EIP-1559 base-fee burn of about 0.006M ETH, for a framework reading of +0.21% net against the monitor's +0.0157% — agreement within 0.19 percentage points. There is no vesting, no scheduled Foundation release, and no buyback; the only tracked overhang is the unscheduled Foundation treasury. The key variable is where activity settles, because the burn is demand-responsive and has thinned as users moved to Layer 2. Among uncapped Layer 1s, Ethereum is unique in pairing continuous issuance with a full base-fee burn — but that burn only bites when mainnet is busy, and right now it is not.

---

*MrNasdog Pressure Framework analysis of Ethereum (ETH), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 24, 2026.*

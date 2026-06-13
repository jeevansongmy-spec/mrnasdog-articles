---
title: "ETH Inflation Analysis · June 2026 · Issuance and the burn cancel out"
description: "Issuance and the EIP-1559 burn cancel out: ~0.153M ETH minted vs ~0.150M burned over 90 days. Framework reads +0.0025% net — a roughly flat supply."
canonical_url: "https://mrnasdog.com/research/eth/inflation"
tags: ["crypto", "ethereum", "layer1", "eip-1559"]
published: true
---

> Originally published at **[mrnasdog.com/research/eth/inflation](https://mrnasdog.com/research/eth/inflation)** by MrNasdog.

Ethereum is a proof-of-stake Layer 1 with no supply cap, yet its supply barely moves. Proof-of-stake issuance adds about **0.153M ETH** over 90 days and the EIP-1559 base-fee burn removes about **0.150M ETH** — leaving a net of roughly **+0.0025%** against the inflation monitor's **−0.0015%**. The two sides offset, so ETH reads as one of the flattest large-cap assets in coverage.

## The verdict, in one paragraph

For the 90-day window ending June 14 2026, the MrNasdog Pressure Framework reads **ETH at +0.0025% net** for the window. The independent inflation monitor reads **−0.0015%**, a gap of just **0.004 percentage points** — far inside the 0.5pp tolerance, so no data-conflict chip is raised. The structural picture is simple: Ethereum mints new ETH to pay validators and burns ETH on every block through EIP-1559, and at current activity the two flows run roughly level. ETH is a **roughly flat, self-balancing supply** — neither meaningfully inflationary nor deflationary at the moment.

## Sell pressure: where new ETH comes from

Sell #1 — protocol inflation — is the only live source of new ETH. Proof-of-stake issuance pays validators about **1,700 ETH a day**, or roughly **0.153M ETH** over the 90-day window. That rate is about 90% below the old proof-of-work emission; the Merge replaced miner block rewards with a far smaller staking reward sized to the amount of ETH staked (currently about 28M ETH, near 23% of supply). Issuance scales with the square root of total stake, so it rises slowly as more validators join rather than on a fixed schedule.

Every other sell row is zero. Sell #2 — vesting unlocks — is zero because Ethereum has no vesting schedule and no locked team allocation dripping into the market; the original 2014 sale and genesis allocations have long since fully circulated. Sell #3 — Foundation and unscheduled unlocks — is zero: the Ethereum Foundation holds a treasury but runs no scheduled release programme, and no discretionary deployment is booked this window. Sell #4 — long-term locked or bankruptcy — is zero; there is no bankruptcy estate, and the 28M ETH that is staked locks supply rather than adding it.

## Buy pressure: where new ETH goes

Buy #2 — protocol fee burn — is the offsetting force. EIP-1559 burns the base fee of every transaction on every block, permanently destroying that ETH. Over this window the burn runs at about **0.150M ETH**, roughly level with issuance, though it varies with on-chain activity. Since the EIP-7918 blob-fee floor took effect, the burn has stabilised closer to issuance rather than swinging far below it during quiet periods — which is why ETH currently sits near flat rather than mildly inflationary.

The rest of the buy ledger is zero. Buy #1 — programmatic buyback — is zero because validator rewards are paid from fresh issuance, not from market purchases. Buy #3 — Foundation buy — is zero; the Foundation runs no accumulation programme. Buy #4 — new long-term lock — is zero as a programmatic line: staking does lock ETH for yield, but it is validator-driven rather than a programme with an announced lock quantum.

## Foundation and overhang

The one tracked overhang is the **Ethereum Foundation treasury**. The Foundation holds ETH across multiple addresses but publishes no scheduled release programme, so the framework treats the balance as unscheduled and books it at zero flow for the window. It is monitored on a roughly bi-weekly web walk. If the Foundation's balance falls between refreshes — a treasury sale or grant deployment large enough to register — the outflow enters Sell #3 at the next refresh. There is no other team-controlled overhang on a release schedule.

## How ETH compares to other uncapped Layer 1 chains

Ethereum belongs to the class of **uncapped, continuous-emission Layer 1s**, but it is the only major one that pairs issuance with a structural burn. Solana issues continuously and burns only half of a tiny base fee, so its net stays clearly positive; ETH burns the full base fee of every transaction, which is why its net collapses toward zero. Against capped halving chains like Bitcoin, the contrast is sharper still: Bitcoin's emission is fixed and falling on a schedule and there is no burn, so it is always mildly inflationary until the cap; ETH has no cap but can swing deflationary in busy periods because the burn can exceed issuance.

The mechanism that makes ETH distinctive is that its supply is **demand-responsive**. More on-chain activity burns more base fee, pushing net supply down exactly when usage is highest; quiet periods let issuance edge ahead. No fixed-schedule chain has this property. For an inflation reading, that means ETH's number is less a property of tokenomics and more a property of current network usage — and right now usage keeps the burn close enough to issuance to read flat.

## What to watch in the next 90 days

Watch the burn-versus-issuance balance, which is the entire story. First, on-chain activity: a sustained rise in transaction and blob demand would tip ETH net-deflationary, while a quiet stretch would let issuance lead. Second, the staking participation rate — if the share of ETH staked climbs materially, issuance rises with it. Third, any Foundation treasury movement large enough to surface in the monitor would promote Sell #3 from zero to a quantified row. Fourth, any protocol change to the issuance curve or blob-fee mechanics through a future upgrade. None of these is a dated event; they are continuous variables the next refresh will re-read.

## Summary

ETH is a self-balancing, near-flat supply. Proof-of-stake issuance of about 0.153M ETH over the window is offset almost exactly by the EIP-1559 base-fee burn of about 0.150M ETH, for a framework reading of +0.0025% net against the monitor's −0.0015% — agreement within 0.004 percentage points. There is no vesting, no scheduled Foundation release, and no buyback; the only tracked overhang is the unscheduled Foundation treasury. The key variable is on-chain activity, because the burn is demand-responsive and can push ETH either side of zero. Among uncapped Layer 1s, Ethereum is unique in pairing continuous issuance with a full base-fee burn, which is why it reads flatter than any other large-cap emission chain.

---

*MrNasdog Pressure Framework analysis of Ethereum (ETH), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 14, 2026.*

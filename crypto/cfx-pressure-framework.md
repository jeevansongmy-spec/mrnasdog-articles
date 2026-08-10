---
title:         "CFX Inflation Analysis · August 2026 · Two mints, one starved burn"
description:   "Conflux minted 22.4M CFX in 90 days from mining and staking together, and burned 1.4K. MrNasdog Pressure Framework reads +0.43% net against a monitor at +0.74%."
canonical_url: "https://mrnasdog.com/research/cfx/inflation"
tags:          ["crypto", "cfx", "conflux", "layer1"]
published:     true
---

*Originally published at [mrnasdog.com/research/cfx/inflation](https://mrnasdog.com/research/cfx/inflation)*

# CFX Inflation Analysis · August 2026 · Two mints, one starved burn

Conflux minted **22.4M CFX** over the last 90 days from two engines running at once — a proof-of-work block subsidy of **0.401334 CFX** per block and a proof-of-stake reward paid every hour — and destroyed only **1.4K CFX** through its base-fee burn. The framework reads **+0.43% net** on a **5.21B** circulating base, with the same figure projected forward because the mining rate last changed on **Apr 7 2026**, before this window opened. The supply monitor reads **+0.74%**, a **0.31-point** gap that sits inside tolerance. Conflux is an uncapped chain with a fully-released float and no counterweight.

## The verdict, in one paragraph

For the 90-day window from **May 12 2026** to **Aug 10 2026**, the framework reads **Conflux at +0.43% net inflation**: **22.4M CFX** of new issuance against **1.4K CFX** burned. That sell figure is not a model — the chain's own issued-supply counter moved from **5,781.03M** to **5,803.44M** across the window, read directly at both ends on a public node and confirmed at ten evenly spaced points in between. The supply monitor reads **+0.74%**, leaving a gap of **0.31 percentage points**, comfortably inside the half-point tolerance, so no monitor-gap chip ships on the CFX page. Conflux is best labelled a **dual-mint chain with a decorative burn**: two independent issuance streams, one burn that the network is far too quiet to feed, and nothing else on either side of the ledger.

## Sell pressure: where new CFX comes from

Sell #1, protocol inflation, booked **22.4M CFX**, and the interesting part is the split. Conflux runs a Tree-Graph proof-of-work chain and a proof-of-stake chain in the same protocol, and both mint. The mining subsidy is set by the DAO-voted block-reward parameter, currently **0.401334 CFX** per block; sampling six hundred consecutive epochs on chain gives **0.955 CFX** of block reward per epoch after anticone penalties, which across the window's **6.62M** epochs comes to about **6.3M CFX**. The staking side is larger: proof-of-stake rewards run at roughly **7,872 CFX** per staking epoch, and **2,085** of those epochs fell inside the window, for about **16.4M CFX**. Storage-collateral interest, the protocol's third mint, runs on a collateral base of only **3.3M CFX** and contributes a rounding error. The three sum to about **22.8M** against the **22.4M** measured directly — an agreement close enough to confirm the decomposition, with the measured figure the one that ships.

One detail matters for the forward reading. The Conflux block reward is governance-adjustable, and it was halved from **0.802654** to **0.401334 CFX** per block. That change activated on **Apr 7 2026**, five weeks before this window opened, and the parameter reads identically at both window ends and at every interior probe. The trailing rate is therefore the live rate, no re-basing is needed, and the next-90-day column carries **22.4M** unchanged.

Every other sell row is zero. Sell #2, vesting unlocks, is **0** because the genesis release schedule finished in 2024 and the unlock contracts are empty — both the two-year and four-year unlock balances read zero on chain, so there is no cliff left to fire. Sell #3, Foundation and unscheduled unlocks, is **0** with no observed release in the window, though the overhang it tracks is real and is discussed below. Sell #4, long-term locked or bankruptcy, is **0** because no bankruptcy estate or trustee distribution is associated with the asset.

## Buy pressure: where new CFX goes

Buy #2, the protocol fee burn, is the only live buy-side mechanism, and it booked **1.4K CFX**. Conflux burns part of the transaction base fee — the burned share is itself a governance parameter, with the remainder paid to miners — and it also burns a slice of sponsored storage collateral by converting it into storage points. The mechanism works. The volume does not: the chain's cumulative burn counter stands at **32.3K CFX** for the entire life of the mechanism, and it is currently advancing at about **15.5 CFX** per day. Ninety days of that is **1.4K CFX** against a **22.4M** mint. The burn offsets roughly six thousandths of one percent of new issuance, which is why the net and the gross round to the same number.

Buy #1, programmatic buyback, is **0**: there is no buyback contract and no revenue stream pointed at the market, since transaction fees are split between miners and the burn. Buy #3, Foundation buy, is **0** — no accumulation programme has been disclosed and no open-market purchase reported. Buy #4, new long-term lock, is **0**, and this one deserves the reasoning. Proof-of-stake locking grew over the quarter, from **850.4M** to **885.9M CFX**, and Core-Space staking grew from **898.4M** to **935.7M CFX**. Neither is booked as absorption: withdrawal from both is measured in days rather than years, and staked CFX already counts inside the tradable float, so booking it would manufacture roughly **0.25%** of deflation that no holder experienced.

## Foundation and overhang

Conflux's genesis allocation reserved a large ecosystem fund and a smaller foundation holding, and those are the team-controlled overhang this page tracks. Neither publishes a wallet address, so both are opaque — they are tracked through official disclosure and governance records rather than read on chain. Their capacity is real but nothing has moved: a 2025 governance decision authorised placing ecosystem CFX into the treasuries of publicly listed companies under a lock of at least four years, and as of **Aug 10 2026** no such placement has executed anywhere observable. Capacity alone does not make a number.

Two other balances complete the picture. A residual of **16.59M CFX** sits outside the classified float. And **572.96M CFX** rests at the network's null address — that is destroyed supply, not an overhang, and the framework excludes it from both sides of the ledger. If any of these balances falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How CFX compares to other hybrid proof-of-work chains

Conflux belongs to a small family: chains that keep proof-of-work for block production while layering proof-of-stake on top, and that pay both. Against a pure proof-of-work chain with a hard cap — Bitcoin, Litecoin, Ethereum Classic — the structural difference is decisive. Those chains have exactly one mint, and it steps down on a schedule written into the protocol that no vote can touch. Conflux has three mints, no cap, and its largest single lever, the block reward, is a parameter that a governance round can double or halve. That is why a capped chain's inflation is a forecast and Conflux's is a measurement.

Against uncapped continuous-emission proof-of-stake networks, Conflux looks more familiar, but with a twist: its staking reward is the bigger mint. Roughly **16.4M** of the quarter's **22.4M** comes from staking and only **6.3M** from mining, so the chain behaves economically much more like a staking network than the mining branding suggests. The comparison that hurts is with fee-burn chains. Conflux copied the base-fee burn design and even runs a second storage burn beside it — the mechanism is present, correctly implemented and permanently live. On a busy chain that burn can outrun issuance and turn net supply negative. Here throughput is low enough that the burn is a rounding line, so Conflux gets the architecture of a deflationary chain with the arithmetic of an inflationary one.

## What to watch in the next 90 days

First, the **v3.1.0 network hardfork**, activating at epoch **155,140,000**, estimated **Aug 25 2026**. It carries seven improvement proposals covering EVM opcode compatibility and bug fixes, and none of them touches issuance, block reward or burn — so the expected supply impact is nil, and confirming that after activation is the check. Second, the next parameter-voting round. Rounds run every 60 days and the current reward has now survived two of them unchanged since the Apr 7 2026 activation, which places the next boundary near **Oct 4 2026**; a vote to halve or double the block reward would move roughly **3M CFX** a quarter either way. Third, the burn counter: any sustained rise in on-chain activity is the only path by which Buy #2 becomes material, and today it would need to grow by four orders of magnitude. Fourth, the ecosystem-fund authorisation — the first executed treasury placement into a listed company would be a Sell #3 event, and the disclosure would be the trigger. Fifth, the staking balance: a sharp unwind of the **885.9M CFX** currently locked in proof-of-stake would push supply back onto the active float faster than issuance does.

## Summary

Conflux is an uncapped Tree-Graph chain that mints from both proof-of-work and proof-of-stake, and the framework reads it at **+0.43% net** over the last 90 days — **22.4M CFX** issued, measured directly from the chain's own supply counter, against **1.4K CFX** burned. The structural mechanism is a dual mint with a starved burn: the base-fee burn is live and correctly implemented, but network throughput is far too low for it to matter, so almost the entire mint reaches the market. The key risk is governance rather than code — the block reward is a DAO parameter that has already been halved once in 2026 and can move again at any 60-day round, and a large ecosystem fund sits in undisclosed wallets already authorised for treasury deployment. There is no supply cap and no vesting left to expire, so the ceiling on Conflux's supply is whatever its voters decide it should be.

---

*MrNasdog Pressure Framework analysis of CFX, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 10 2026.*

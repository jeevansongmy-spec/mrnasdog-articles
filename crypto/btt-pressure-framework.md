---
title: "BTT Inflation Analysis · August 2026 · Supply flat, projected to stay flat"
description: "A MrNasdog Pressure Framework read of BitTorrent (BTT): the TRON contract has no mint function, so supply is fixed at 990 trillion. Net 0.00% against a supply monitor at +0.04% on a 987.04 trillion tradable base."
canonical_url: "https://mrnasdog.com/research/btt/inflation"
tags: ["crypto", "btt", "bittorrent", "tron"]
published: true
---

> Originally published at **[mrnasdog.com/research/btt/inflation](https://mrnasdog.com/research/btt/inflation)** by MrNasdog.

BitTorrent's BTT is a fixed **990 trillion** token on TRON, and its own contract settles the question of dilution: there is no mint function in the deployed code, so no new BTT can ever be created. Over the 90 days to **Aug 5 2026**, nothing vested, nothing was bought back and nothing was burned, so the MrNasdog Pressure Framework reads **0.00%** net against our supply monitor's **+0.04%** for the same window — a gap of about **0.04 percentage points**, so no monitor-gap flag ships. BTT is a **fixed-supply utility token whose float is essentially static**, with an announced quarterly buyback and burn that has not yet fired.

## The verdict, in one paragraph

For the 90-day window ending **Aug 5 2026**, the framework reads **BTT at 0.00% net**: sell pressure of **zero BTT** against buy pressure of **zero BTT** on a circulating base of about **987 trillion BTT**. Our supply monitor reads **+0.04%** across the same window, oscillating inside a tenth of a percent of noise as market cap and price move around a flat token count — a gap of about **0.04 percentage points**, well inside the half-point tolerance, so no monitor-gap flag ships with this page. The two agree because the ledger is closed rather than estimated: BTT's **990 trillion** supply is fixed on-chain and the verified contract has no mint and no burn function, so there is no mechanism through which the number could move. BTT is best labelled **a fixed-supply token that is static on the float, waiting on a buyback that has not started**.

## Sell pressure: where new BTT comes from

It comes from nowhere, and that is the most important fact about BTT. Sell #1 — protocol inflation — is **zero** because the BTT token contract on TRON exposes only transfer and approval functions; there is no mint in the deployed bytecode and the contract is not a proxy, so no party, not even BitTorrent, can create a single new BTT. The **990 trillion** supply that exists today is the whole supply that will ever exist. This is structural scarcity written into code, not a policy that governance could reverse.

The other sell rows are zero for their own clean reasons. Sell #2 — vesting unlocks — is **zero** because BTT's major distribution finished by 2025 and no unlock event falls inside the window; about **99.7%** of the 990 trillion is already circulating. A small partnership reserve runs on paper to 2028, but those coins sit in their wallets rather than reaching the market, so under the framework's released-beats-scheduled rule they add nothing. Sell #3 — Foundation and unscheduled unlocks — is **zero** in value: about **2.96 trillion BTT**, roughly **0.30%** of supply, remains non-circulating team, partnership and ecosystem reserve, but it has not moved materially and has no published near-term release schedule. Sell #4 — long-term locked or bankruptcy — is **zero**: BTT has no estate, trustee or court-ordered distribution.

## Buy pressure: where new BTT goes

For now, nowhere — but that is about to change on paper. Buy #1 — programmatic buyback — is **zero** today, and it is the row to watch. On **Jul 6 2026** BitTorrent Inc. announced a quarterly buyback and burn funded by **100%** of the revenue from its decentralised services, including BitTorrent Speed and the newly launched BTTInferGrid. The programme buys BTT on the open market and permanently burns it, with the first batch of buybacks running through the third quarter of 2026 and the first burn — together with the amount destroyed, its percentage of supply and the on-chain transaction hash — scheduled for **mid-October 2026**. Because no quantity, rate or wallet has been disclosed in advance, the framework carries the row at **zero** until a real number exists; the destination is a burn, so once it fires it will shrink supply directly.

The remaining buy rows are zero and structurally so. Buy #2 — protocol fee burn — is **zero**: the BTT contract has no burn function and there is no automatic fee burn on transfers, so the only planned burn is the revenue buyback above. Buy #3 — Foundation buy — is **zero**: there is no discretionary open-market buying outside that announced programme. Buy #4 — new long-term lock — is **zero**: no new protocol lock or escrow was added in the window. With every buy row at zero and every sell row at zero, the float simply does not move.

## Foundation and overhang

BTT's overhang is small for a token this old. About **2.96 trillion BTT** — roughly **0.30%** of the 990 trillion max — is still non-circulating, held as team, partnership and ecosystem reserve, with residual partnership vesting scheduled out to 2028. That balance is monitored rather than booked as a sell row, because nothing observable left those wallets in the window and there is no published near-term release. The buyback destination is a burn rather than an accumulation wallet, so there is no bought-back stack that could later be sold back into the market — once tokens are bought, they are destroyed.

The rule that governs the reserve is the same one applied everywhere: if the non-circulating balance falls between refreshes, the outflow enters Sell #3 at the next refresh. Until then, the **0.30%** reserve is the only supply overhang worth tracking, and at the token's scale even a full release would be a small fraction of the **987 trillion** already trading. The larger structural point is that no reserve release can ever be joined by fresh minting, because minting is impossible.

## How BTT compares to other fixed-supply tokens

The right comparison class for BTT is fully distributed, hard-capped tokens whose emission is already finished — not the continuous-emission layer-ones that print new coins every block. What separates tokens in this class is not price but three mechanism choices: whether any supply can still be minted, whether any is still vesting, and whether revenue is used to remove tokens. BTT sits at the inert end of that spectrum: nothing can be minted, essentially nothing is still vesting, and nothing has yet been burned. Its supply behaves like a finished, capped asset whose float is set.

Contrast that with a capped exchange token that mints a trimmed farm emission but burns far more through a live revenue buyback, so its supply shrinks every week — BTT has the same capped ceiling but neither the emission nor, yet, the burn. Or contrast it with a fixed-supply payment coin that will never buy back at all; BTT is one governance-free step ahead of that, because its announced quarterly buyback and burn gives it a path to becoming structurally deflationary the moment the first burn lands. The honest way to read BTT today is as a static, fixed-supply utility token whose inflation risk is zero by construction, and whose only near-term supply catalyst is a buyback whose size is still unknown. The risk is not dilution; it is that the buyback proves small relative to the enormous **987 trillion** float.

## What to watch in the next 90 days

First and above all, the **mid-October 2026** burn report: BitTorrent has committed to publishing the amount of BTT bought back and burned, its percentage of total supply, and the on-chain transaction hash, and that first number will convert Buy #1 from zero into a measurable figure. Second, the revenue behind it — because the buyback is funded entirely by decentralised-service revenue from BitTorrent Speed and BTTInferGrid, the burn will only be as large as those services earn, so any disclosure of service revenue is a direct read on future burn size. Third, the non-circulating reserve: any movement of the roughly **2.96 trillion BTT** team and partnership balance would register as Sell #3 pressure. Fourth, the contract itself, which needs no watching but bears repeating — with no mint function, no governance vote can add to the **990 trillion** cap. Fifth, whether the quarterly schedule holds after the first burn, since a repeatable programme matters far more than a one-off.

## Summary

BTT is one of the most static tokens in our catalogue. Its **990 trillion** supply is fixed on-chain and the deployed contract has no mint and no burn function, so over the 90 days to **Aug 5 2026** nothing was created, nothing vested and nothing was removed — a net **0.00%** change, matching our monitor's **+0.04%** noise to within **0.04 percentage points**. Vesting is essentially complete at **99.7%** circulating, leaving only a **0.30%** reserve overhang that is not moving. The one live catalyst is the quarterly buyback and burn announced **Jul 6 2026**, whose first figures are due in **mid-October 2026**; until then BTT carries zero inflation risk by construction and a still-unsized path to deflation.

---

*MrNasdog Pressure Framework analysis of BTT, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 5 2026.*

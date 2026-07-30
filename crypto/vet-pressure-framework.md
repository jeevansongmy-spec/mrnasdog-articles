---
title: "VET Inflation Analysis · July 2026 · Fixed supply, roughly steady"
description: "VeChain's inflation lives in VTHO, not VET: supply fixed at 85.99B and 100% circulating, no mint, no vesting, no VET burn, no buyback. Framework reads 0.00% (monitor +0.007%)."
canonical_url: "https://mrnasdog.com/research/vet/inflation"
tags: ["crypto", "vet", "vechain", "fixed-supply"]
published: true
---

> Originally published at **[mrnasdog.com/research/vet/inflation](https://mrnasdog.com/research/vet/inflation)** by MrNasdog.

# VET Inflation Analysis · July 2026 · Fixed supply, roughly steady

VeChain is one of the few large chains whose inflation question has a one-word answer: none. **VET** has a fixed supply of **85,985,041,177** coins, no mint function, and circulating already equals total, so nothing is held back to release. The chain does issue and burn tokens constantly — but those are **VTHO**, a separate gas token on its own ledger, and the **100%** gas-fee burn destroys VTHO, never VET. Over the 90 days to **Jul 31 2026** the Pressure Framework reads **0.00M VET** of sell pressure and **0.00M VET** of buy pressure, a net of **0.00%**. Our supply monitor reads the realised change at **+0.0070%** — a gap of **0.007 percentage points**, so no monitor-gap chip ships.

## The verdict, in one paragraph

For the 90-day window ending **Jul 31 2026**, the Pressure Framework reads **VET at 0.00% net**. Sell pressure is **0.00M VET**, buy pressure is **0.00M VET**, against a circulating base of **85,985.04M VET** that is identical to total supply. Our supply monitor reads the realised 90-day change at **+0.0070%**, a gap of **0.007 percentage points** — far inside the framework's half-point tolerance, so no monitor-gap chip appears on the VET overview. The two readings agree because there is genuinely nothing to disagree about: VET has no mint, no VET burn, no vesting and no observed treasury movement, and the monitor's tiny wobble is rounding noise on a market-cap-over-price series sitting on a constant. VET is best characterised as **a fixed-supply coin whose real inflation lives entirely on a second token**.

## Sell pressure: where new VET comes from

The short answer is nowhere. Sell #1, protocol inflation, is **zero** because VET has no mint function — the total supply of VET is fixed and no new VET is ever created. This is the single fact that governs the whole page. VeChainThor runs a dual-token design: VET is the value and staking asset, and VTHO is the gas token that staked VET generates. The network issues VTHO every block and it changed the VTHO issuance model in the Hayabusa upgrade, but not one of those coins is a VET, so none of it belongs in this row.

Sell #2, vesting unlocks, is **zero**. VeChain launched its mainnet in 2018 and every genesis allocation — seed, private sale, public sale and operations — finished unlocking years ago, with the last team cliff clearing in **Aug 2019**. The proof is in the supply figures themselves: circulating supply equals total supply exactly, at **85,985,041,177 VET**, which means there is no locked tranche sitting behind the float waiting for a cliff. Sell #3, Foundation and unscheduled unlocks, is also **zero** for the window. The VeChain Foundation holds VET for grants, partnerships and operations, but because that VET is already inside the circulating count, a Foundation sale moves float, not supply, and no dated release was observed. Sell #4, long-term locked or bankruptcy, is **zero**: there is no VeChain bankruptcy estate, no trustee and no court-ordered distribution.

## Buy pressure: where new VET goes

Buy pressure is **zero** on the VET ledger, and the most important row to explain is the one people assume is large. Buy #2, protocol fee burn, is **zero for VET** even though VeChain burns **100%** of the gas paid on every transaction — because the gas is denominated in VTHO, not VET. The Galactica and Hayabusa upgrades turned VeChain into an aggressively deflationary system, but the deflation happens entirely on the VTHO ledger; it removes VTHO and never destroys a single VET. Counting that burn as a VET buy would be a category error.

The other three buy rows are **zero** as well. Buy #1, programmatic buyback, is zero because VeChain runs none: the only VET buyback it ever announced was a one-off twelve-month plan back in **2019** that lapsed in 2020 and was never replaced, and no wallet is buying VET on the open market today. An expired programme is not an active one. Buy #3, Foundation buy, is zero — no VeChain Foundation open-market VET purchase has been disclosed or is visible on-chain. Buy #4, new long-term lock, is zero, and this one needs the closest look, because VeChain's StarGate staking held roughly **13 billion VET** this window, up from **2.52 billion** at its December 2025 launch. That is a lot of VET pulled into staking, but staking on StarGate is custody, not a lock: after a short maturity — **2 days** at the entry tier — holders can unstake at any time with no cooldown, and the stake positions are freely tradable NFTs. Those coins never leave the tradable float, so no lock is booked.

## Foundation and overhang

VET has only one team-controlled overhang worth naming: the **VeChain Foundation** treasury, the Foundation's own VET held for grants, partnerships and operations. It is followed through VeChain's periodic financial reports rather than a public wallet address, so it is treated as opaque and re-checked on a web walk each rebuild. Crucially, that treasury VET is already counted inside the **85,985.04M VET** circulating figure — total supply and circulating supply are identical, so there is no non-circulating reserve, no unscheduled-unlock pool and no buyback accumulation wallet hiding below the float. A Foundation sale would therefore shift who holds VET, not how much VET exists. There is no DAO treasury distinct from the Foundation and no bankruptcy residual. The large StarGate staking balance is explicitly not an overhang — it is user-owned VET in free-exit custody that stays circulating-classified. If the Foundation treasury balance falls between refreshes, the outflow enters Sell #3 at the next refresh.

## How VET compares to other dual-token and fixed-supply chains

VeChain belongs to a small class of chains that split value and gas into two tokens — the same design pattern as the original Neo and Gas pairing that VeChain descended from. In those systems the coin you buy is deliberately not the coin the network spends, and the inflation you would expect to see on the main asset is exported onto the gas token. That is why VET reads flat while VTHO is where all the monetary action is: dynamic issuance tied to staking, a fifty-percent issuance cut under Hayabusa, and a full base-fee burn. Judging VET by VTHO's mechanics is the most common mistake made about this coin, and it is the mistake this page exists to prevent.

Against ordinary single-token proof-of-stake layer ones, VET looks unusually clean. An uncapped continuous-emission chain mints new coins to pay stakers, so its supply grows every block; VeChain pays stakers in VTHO instead, so VET issuance is zero by design. Against capped-and-halving chains like Bitcoin, VET is stricter still in one sense — there is no ongoing subsidy at all, because distribution finished at genesis — but weaker in another, since VET has no fee burn of its own to make the fixed supply actively shrink. The honest label is fixed-and-flat: nothing is being added, but nothing is being removed either, which is exactly why the framework's inflation score tops out at the middle of the band rather than at the deflationary end. A permanently capped supply is not the same as a shrinking one.

## What to watch in the next 90 days

First, the VeChain Foundation transparency reporting — the treasury is the only VET position that could turn into sell pressure, and a large disclosed sale would be the one event that moves this page off zero on the sell side. Second, any governance proposal that touches VET supply directly; nothing on the published 2026 roadmap does, but the Interstellar full-EVM phase and the AgentSuite rollout are the kind of large changes worth reading for supply language. Third, whether VeChain ever revives a VET buyback — the 2019 programme is long dead, and only a new, funded one would put a real number in the buy column. Fourth, StarGate staking growth: it does not change VET supply, but a very large share of float locked into even free-exit custody thins the tradable market, which matters for how any future Foundation flow lands. There is no dated unlock, burn or cliff to watch, because VET has none.

## Summary

VeChain's VET is a fixed-supply coin: 85,985,041,177 tokens, no mint function, circulating equal to total, and a genesis distribution that finished years ago. The Pressure Framework reads VET at 0.00% net over 90 days, matching our supply monitor to within seven thousandths of a percentage point. The one fact that resolves almost every question about this coin is the dual-token split — VeChain's heavy, 100% gas-fee burn destroys VTHO, a separate token, and never touches VET. The key structural point is that fixed-and-flat is not deflationary: nothing dilutes VET, but nothing shrinks it either, so the only supply-side risk left to monitor is a discretionary sale from the VeChain Foundation treasury that already sits inside the circulating count.

*MrNasdog Pressure Framework analysis of VeChain (VET), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 31 2026.*

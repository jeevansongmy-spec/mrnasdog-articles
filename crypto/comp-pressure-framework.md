---
title:         "COMP Inflation Analysis · June 2026 · Reserve Drains, No New Mint"
description:   "Compound's COMP: fixed 10M cap, vesting ended 2024, Reservoir empty. Only the last ~331.8K reserve COMP drains into circulation — framework reads +0.27% net, monitor agrees."
canonical_url: "https://mrnasdog.com/research/comp/inflation"
tags:          ["crypto", "comp", "compound", "defi"]
published:     true
---

*Originally published at [mrnasdog.com/research/comp/inflation](https://mrnasdog.com/research/comp/inflation)*

# COMP Inflation Analysis · June 2026 · Reserve Drains, No New Mint

Compound's COMP sits on a **fixed 10,000,000 hard cap** with no mint function, vesting that ended in 2024, and an empty distribution Reservoir. The only live supply pressure is the last ~331.8K reserve COMP entering circulation as it is distributed — about **26.5K COMP per 90 days**. Framework reading: **+0.27% net**, with the aggregator monitor reading the same +0.27%. COMP is structurally near the end of its emission curve.

## The verdict, in one paragraph

For the 90-day window ending June 21 2026, the framework reads **COMP at +0.27% net inflation**. There is no buyback and no burn, so the entire reading comes from the sell side: the last fragment of non-circulating COMP draining into circulation at roughly **26.5K COMP per 90 days**. The aggregator monitor reads **+0.27%** over the same window — a **0.00pp gap**, so no warning chip is warranted. The label for COMP is a **maturing fixed-cap governance token**: almost fully distributed, structurally incapable of minting more than 10M, with a small residual reserve drain as its only inflation channel.

## Sell pressure: where new COMP comes from

Only one sell-side row carries any value, and it is small. **Sell #1 protocol inflation** reads **~0.03M COMP per 90 days**. This is not new mint — the COMP ERC-20 has a fixed cap and the contract's **totalSupply()** returns exactly 10,000,000 COMP, verified directly on-chain. It is the last ~331.8K of non-circulating COMP slowly entering the circulating float as Compound distributes it to protocol users. The historical Reservoir contract once dripped 0.5 COMP per Ethereum block (~2,880 COMP/day) to bootstrap usage; that Reservoir is now **empty**, its 4.23M COMP allocation fully spent. What remains is the tail of that distribution working through the system, which the framework measures empirically at **26.5K COMP over 90 days**.

Every other sell row is zero. **Sell #2 vesting unlocks** is zero because the 4-year vesting for founders, team, investors and Compound Labs shareholders **ended in 2024** — there is no remaining cliff. **Sell #3 Foundation and unscheduled unlocks** is zero: the Reservoir is drained and the governance Timelock holds only ~18 COMP, so there is no large treasury to deploy. **Sell #4 long-term locked or bankruptcy** is zero — Compound has no bankruptcy estate and no scheduled long-term-lock cliff.

## Buy pressure: where COMP goes

The buy ledger is empty. **Buy #1 programmatic buyback** is zero — Compound runs no token-repurchase programme; protocol revenue accrues to market reserves and DAO operations, not to buying COMP. **Buy #2 protocol fee burn** is zero, because COMP has no burn mechanism. **Buy #3 Foundation buy** is zero — there is no DAO or Foundation open-market COMP accumulation programme. **Buy #4 new long-term lock** is zero: COMP rewards on Compound III (Comet) are streamed directly to suppliers and borrowers, not locked into a new vehicle. With no offsetting buy pressure, the small reserve drain on the sell side is the entire net reading.

## Foundation and overhang

The team-controlled overhang on COMP is unusually small for a DeFi governance token. The **Compound Reservoir** (0x2775…09e38) — the contract that funded years of COMP distribution — now holds **zero COMP**. The **Comptroller** and the governance **Timelock** hold negligible balances (~18 COMP combined). The remaining ~331.8K non-circulating COMP is the residual that the framework already counts in Sell #1 as it enters circulation. There is no large idle multisig or Foundation safe that could suddenly hit the market. If any identified Compound-controlled wallet's COMP balance falls between refreshes, that outflow enters Sell #3 at the next refresh — but at current balances the capacity for a surprise deploy is structurally minimal.

## How COMP compares to other DeFi governance tokens

COMP belongs to the class of **fixed-cap DeFi governance tokens** alongside AAVE, UNI and MKR — tokens with a hard maximum supply and no protocol mint. Within that class, the differentiator is what each does with revenue. **AAVE** runs a permanent $50M/year buyback, so its net reads slightly deflationary. **UNI** converts swap-fee revenue toward token burn under its fee-switch design. **MKR** has a long history of stability-fee-funded burns. COMP does none of these — it has no buyback and no burn, so its net cannot go negative; the best it can structurally reach is flat once the last reserve COMP finishes entering circulation.

The flip side is that COMP carries almost no dilution risk. Against tokens with multi-year vesting cliffs still ahead, COMP is **96.7% circulating with vesting fully complete**. Its supply curve is essentially finished: the chart is a fixed cap with a thinning tail of reserve distribution, not an unlock schedule with years of cliffs to absorb. For a maturing protocol whose flagship V2 markets have been deprecated in favour of Compound III (Comet), that supply maturity is the structurally cleanest part of the story.

## What to watch in the next 90 days

Three watch lines move the framework reading. First, **Compound III (Comet) reward speeds** — governance can raise or cut the per-market COMP streams, which changes how quickly the residual reserve enters circulation. Second, any **governance proposal to set reward speeds toward zero** — a recurring debate on the Compound forum — which would push the net toward flat. Third, the **final depletion of the reserve**: once the last ~331.8K COMP is fully circulating, the Sell #1 row collapses to zero and COMP becomes a fully-flat fixed-cap asset. No dated cliff or unlock event sits inside the window.

## Summary

COMP is a 10M-cap, ~96.7%-circulating DeFi governance token with vesting finished in 2024 and an empty distribution Reservoir. The framework reads **+0.27% net**, driven entirely by the last reserve COMP draining into circulation at ~26.5K per 90 days; the aggregator monitor confirms +0.27% within 0.00pp. With no buyback and no burn, the structural ceiling is flat, the structural risk is governance changing reward speeds, and the structural floor is the fixed 10M cap that no actor can exceed. COMP is among the most supply-mature governance tokens in the framework's coverage.

---

*MrNasdog Pressure Framework analysis of Compound (COMP), Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 21, 2026.*

---
title:         "LDO Inflation Analysis · July 2026 · Supply shrinking, projected to keep shrinking"
description:   "Lido DAO's LDO is fully vested with no mint or burn — a live DAO buyback removes ~6.4M LDO / 90D. Framework reads −0.76% net; monitor −0.82% (0.06pp gap)."
canonical_url: "https://mrnasdog.com/research/ldo/inflation"
tags:          ["crypto", "ldo", "lido", "staking"]
published:     true
---

*Originally published at [mrnasdog.com/research/ldo/inflation](https://mrnasdog.com/research/ldo/inflation)*

Lido's **LDO** is a fixed 1-billion-cap governance token with no protocol mint and no fee burn, and every vesting cliff finished by 2024 — so the only live supply flow is a DAO-approved buyback that removes **~6.4M LDO** from the market each 90 days into a governance-disabled treasury. The Pressure Framework reads **−0.76% net** over the window; our inflation monitor reads **−0.82%**, a gap of just **0.06 percentage points** — no data-conflict chip. LDO is mildly deflationary by policy rather than by protocol.

## The verdict, in one paragraph

For the 90-day window the framework reads **LDO at −0.76% net**, i.e. supply shrinking. There is no sell pressure at all: the token is fully vested, has no protocol emission and no fee burn, so all four sell rows are zero. The only flow is on the buy side — a **DAO buyback** that has removed roughly **6.4M LDO** from circulation against a base of **~842.8M**. The inflation monitor reads **−0.82%** over the same window; the gap is **0.06 percentage points**, comfortably inside tolerance, so no ⚠ chip ships. Both readings agree because the bought-back LDO leaves the circulating count when it lands in the treasury. LDO is a quiet, structurally deflationary governance token whose only supply lever is a discretionary buyback.

## Sell pressure: where new LDO comes from

Every sell row is zero, and each for a structural reason. **Protocol inflation** is zero because LDO is a fixed 1,000,000,000-supply token that was fully issued at its December 2020 launch — it is a governance token, not a staking-reward token. Lido pays its stakers in **stETH**, not in newly-minted LDO, so no new LDO is ever created. **Vesting unlocks** are zero because the entire distribution has finished vesting: the founder, validator and venture-round allocations unlocked in December 2022, and the final investor tranche unlocked in March 2024, so no cliff falls inside the next 90 days. **Foundation and unscheduled unlocks** are zero as a market flow — the Lido DAO treasury holds roughly **108.2M LDO** on-chain, but it has no published release schedule and no discretionary sale to market was observed in the window. **Long-term locked or bankruptcy** is zero: no bankruptcy estate holds or distributes LDO.

## Buy pressure: where new LDO goes

The buy side carries the whole story. **Programmatic buyback** is booked at **~6.4M LDO**: in April 2026 the Lido DAO approved a one-time buyback of about **10,000 stETH (≈ $20M)** worth of LDO, executed in 1,000-stETH batches with each tranche separately approved and publicly reported, and it has since been supplemented by a revenue-funded dynamic buyback. The DAO treasury's on-chain LDO balance grew by about 6.4M over the 90-day window — LDO bought off the open market and returned to the treasury, where it is governance-disabled while held. **Protocol fee burn** is zero — Lido's protocol fee is taken in staking rewards and split between node operators and the treasury, and none of it buys or burns LDO. **Foundation buy** is zero as a separate line because the treasury buyback is the only accumulation mechanism and it is already counted above. **New long-term lock** is zero — there is no newly-deployed lockup contract with an announced quantum, and the bought-back LDO is not double-counted here.

## Foundation and overhang

One overhang matters: the **Lido DAO treasury**, held in the DAO's Aragon Agent, which carries roughly **108.2M LDO** on-chain. It has no published release schedule, and it is the wallet where the buyback accumulates — those bought-back tokens are governance-disabled while they sit there, so the treasury is both the buyback's destination and the single largest team-controlled claim on the float. It is read directly from chain state each rebuild. If the treasury's LDO balance were to fall between refreshes — a DAO vote to sell or distribute — that outflow would enter Sell #3 at the next refresh. Today it is only growing, which is why the buyback nets to deflation rather than being offset by a treasury sale.

## How LDO compares to other governance tokens with buybacks

LDO's supply mechanics sit at the calm end of the governance-token spectrum. Most DeFi governance tokens are uncapped or still emitting — they mint new supply to incentivise liquidity or reward stakers, so their sell rows are dominated by ongoing emission. LDO does the opposite: it is a fixed 1B-cap token with the mint switched off since launch and vesting fully behind it, so its baseline is flat, and the only active lever pushes supply **down**.

The closest structural analogues are the exchange tokens that run buybacks — BNB, OKB and LEO all use protocol or company revenue to repurchase their token. The key mechanical difference is destination: those programmes typically **burn** the repurchased token, permanently reducing total supply, whereas Lido's buyback is a **buyback-and-hold** — the LDO is removed from the market but parked in the treasury rather than destroyed. That distinction matters for the reading. A burn is irreversible; a hold is a reversible removal, because the DAO could in principle vote those tokens back into circulation. So LDO's deflation is real but softer and more contingent than a burn-model token's: total supply is unchanged at 1B, and only the circulating float has tightened.

Against a continuous-emission Layer 1 or a still-vesting DeFi token, LDO is therefore the quieter asset — no dilution to absorb, and a modest structural tailwind on the float. But unlike a fixed-schedule halving coin, the buyback is discretionary: it depends on the DAO continuing to approve batches and on protocol revenue funding the dynamic programme, not on protocol code. That is why the framework labels LDO deflationary by policy rather than by protocol.

## What to watch in the next 90 days

Three things move the reading. First, the **buyback cadence** — the one-time $20M programme runs in tranche-gated batches, each needing fresh DAO approval and public reporting, so the pace of the next few batches sets the next-90-day number directly. Second, the **dynamic revenue-funded buyback**, which was going live around mid-2026: if it ramps, the ~6.4M/90D run-rate could rise; if protocol revenue softens, it slows. Third, the **treasury balance** — any DAO proposal to deploy or sell treasury LDO would flip the overhang from a growing store into real Sell #3 pressure. All three are governance items, so the Lido research forum and Snapshot votes are the surfaces to watch.

## Summary

LDO is a fully-vested, fixed 1-billion-cap governance token with no protocol mint and no fee burn, so every sell row reads zero, and its only live supply flow is a DAO-approved buyback removing **~6.4M LDO / 90D** into a governance-disabled treasury. The framework reads **−0.76% net** against a monitor reading of **−0.82%** — a 0.06-point gap, no chip — making LDO mildly deflationary by policy rather than protocol. The key risk is that the buyback is discretionary: it can slow or stop by DAO vote, and the ~108.2M-LDO treasury it feeds could one day be deployed back to the market.

---

*MrNasdog Pressure Framework analysis of LDO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated July 7 2026.*

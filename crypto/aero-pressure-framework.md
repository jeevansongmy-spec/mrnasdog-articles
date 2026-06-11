---
title: "AERO Inflation Analysis · June 2026 · Supply growing, projected to keep growing"
description: "A MrNasdog Pressure Framework read of Aerodrome (AERO): weekly gauge emissions ~26M / 90D reaching the float, no buyback or burn. Framework reads +2.73% net; monitor +3.08%. Decaying ve(3,3) inflation on Base."
canonical_url: "https://mrnasdog.com/research/aero/inflation"
tags: ["crypto", "aero", "aerodrome", "base"]
published: true
---

> Originally published at **[mrnasdog.com/research/aero/inflation](https://mrnasdog.com/research/aero/inflation)** by MrNasdog.

Aerodrome, the leading DEX on Base, runs an uncapped ve(3,3) emission: weekly gauge rewards add about **26M AERO** to the float every 90 days, with no buyback or burn to offset them. The Pressure Framework reads **+2.73% net** inflation over the trailing 90 days against a monitor reading of **+3.08%** — steady incentive inflation that decays by design each epoch.

## The verdict, in one paragraph

For the 90-day window the framework reads **AERO at +2.73% net** inflation from weekly gauge emissions reaching the float. The inflation monitor reads **+3.08%** over the same window — a gap of just **0.35 percentage points**, inside the 0.5-point tolerance, so no ⚠ chip is raised. AERO is structurally inflationary on the active float: a vote-escrow incentive token whose emission is the only supply flow, decaying roughly 1% per weekly epoch.

## Sell pressure: where new AERO comes from

New AERO comes from one place: weekly emissions. **Protocol inflation** booked **~26M AERO** for the window — the gauge emissions reaching circulating at the current decaying rate, roughly 10.9% annualized on circulating. The emission curve started at 10M per week, grew 3% weekly for the first 14 epochs, and now steps down ~1% per epoch in cruise; importantly, roughly half of each epoch's total mint lands directly in 4-year vote-locks as the anti-dilution rebase and never reaches the market, which is why the float-reaching figure is ~26M rather than the larger gross. **Vesting unlocks** are zero — genesis allocations distributed at the 2023 launch with no active cliff schedule. **Foundation and unscheduled unlocks** are zero — emissions are the only supply route, with no foundation treasury making discretionary deploys. **Bankruptcy** is zero.

## Buy pressure: where new AERO goes

The buy side is structurally empty. **Programmatic buyback** is zero — Aerodrome routes 100% of protocol fees to veAERO voters as fee-share, not into AERO purchases. **Protocol fee burn** is zero — there is no burn mechanism. **Foundation buy** is zero — no accumulation programme. **New long-term lock** is zero as a booked row: voluntary 4-year vote-locks absorb a large share of supply, but locking is demand-side behaviour by holders, not a protocol-enforced lock with an announced quantum, so the framework monitors it rather than booking it. The fee-share rewards holding AERO but removes nothing from the supply count.

## Foundation and overhang

AERO carries **no foundation treasury overhang** with discretionary deploy — emissions are the only supply route, and they flow through the rule-based weekly schedule rather than a wallet that could surprise the market. There is one governance watch line rather than a wallet one: the Aero Fed phase is active (post-epoch-67), so voters can adjust the emission rate by ±0.01% of supply per epoch. That is a parameter the community controls, not a balance that could leak between refreshes — so the trigger is a governance vote, not a wallet outflow.

The split between gross emission and float-reaching emission deserves one more sentence, because it is the crux of AERO's reading. Each weekly epoch mints a gross amount to the gauges, but the anti-dilution rebase simultaneously mints to existing veAERO lockers in proportion to how much supply is vote-locked — and because a large share of AERO is locked for up to four years, roughly half of each epoch's mint effectively lands back in locks rather than on the market. The framework books the float-reaching portion (~26M / 90D) because that is what actually pressures circulating supply; the rebase half is real issuance but is structurally sequestered. This is why AERO's headline emission rate sounds higher than the +2.73% the framework reports.

## How AERO compares to other emission-driven DEX tokens

AERO is a ve(3,3) DEX token, the model Curve's veCRV pioneered: continuous emissions to liquidity gauges, vote-locking for fee-share and emission direction, and an anti-dilution rebase for lockers. Against Curve, AERO's emission is more aggressively front-loaded but decays on a fixed per-epoch schedule, and 100% of fees flow to voters where Curve splits differently. Against a fee-switch DEX token like Uniswap's UNI — which has a fixed supply and no continuous emission — AERO is structurally inflationary by design: it pays new supply to rent liquidity, where UNI does not emit at all.

The mechanism that defines AERO is the emission-for-liquidity trade: the token inflates to bootstrap and retain the deepest liquidity on Base, and the 4-year vote-locks plus the rebase are the counterweight that keeps a large share of that emission off the market. The framework reads the portion that reaches the float — ~+2.7% per 90 days — and that figure drifts lower each epoch as the curve decays, unless the Aero Fed votes to change it.

## What to watch in the next 90 days

Three things move the reading. First, the **weekly emission decay** — the ~1%-per-epoch step-down means the framework figure drifts gradually lower absent any vote. Second, an **Aero Fed governance vote** — voters can adjust emissions ±0.01% of supply per epoch, the one lever that could raise or lower the trajectory. Third, the **vote-lock rate** — if a larger share of new emission is locked into 4-year veAERO, less reaches the float and the framework reading falls even as gross emission holds.

## Summary

Aerodrome's AERO is an uncapped ve(3,3) DEX token on Base whose only supply flow is weekly gauge emissions — about **26M AERO** reaching the float per 90 days, for a framework reading of **+2.73% net** against a monitor reading of **+3.08%**, a 0.35-point gap with no chip. There is no buyback, no burn, and no foundation overhang; the only counterweights are the decaying emission curve and the 4-year vote-locks. AERO is steadily, deliberately inflationary on the active float, trending lower by design.

---

*MrNasdog Pressure Framework analysis of AERO, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated June 12, 2026.*

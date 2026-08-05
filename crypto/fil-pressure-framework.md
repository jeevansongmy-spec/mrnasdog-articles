---
title:         "FIL Inflation Analysis · August 2026 · Supply growing, projected to keep growing"
description:   "Filecoin added 38.5M FIL in 90 days from mint, vesting and freed collateral, against a 0.64M burn. Framework +4.64% net, monitor +4.71%, projected +3.94% next. Genesis vesting ends Oct 2026."
canonical_url: "https://mrnasdog.com/research/fil/inflation"
tags:          ["crypto", "fil", "filecoin", "storage"]
published:     true
---

> Originally published at **[mrnasdog.com/research/fil/inflation](https://mrnasdog.com/research/fil/inflation)** by MrNasdog.

Filecoin adds supply from three directions at once, and offsets almost none of it. Over the last 90 days a decaying block-reward mint contributed **5.6M FIL**, six-year genesis vesting contributed **16.8M**, and pledge collateral freed as the network consolidated added another **16.1M** — **38.5M FIL** of sell pressure against a fee burn of just **0.64M** and no buyback at all. The framework reads **+4.64% net** against our supply monitor at **+4.71%**, a gap of **0.07 percentage points** that stays well inside tolerance, so no monitor-gap chip ships. FIL is capped at **2 billion**, and the largest of the three taps — the vesting — closes in **October 2026**.

## The verdict, in one paragraph

For the 90-day window ending Aug 5 2026, the Pressure Framework reads **FIL at +4.64% net**. Sell pressure is **38.5M FIL**, buy pressure is **0.64M FIL**, against a circulating base of **815.5M FIL**. Our supply monitor reads the realised change at **+4.71%**, a gap of just **0.07 percentage points** — inside the framework's half-point tolerance, so no monitor-gap chip appears on the FIL overview. That agreement is the confirmation: Filecoin publishes its circulating supply on-chain each epoch as vested plus mined plus reserve-disbursed, minus burnt, minus locked, and reading that model directly at both ends of the window gives a protocol circulating change of about **+37.9M FIL**, which the framework's five sell rows and one buy row reproduce to the token. FIL is best characterised as **structurally inflationary on three independent taps with a negligible burn** — a capped-supply storage chain that is still years from its ceiling.

## Sell pressure: where new FIL comes from

Sell #1, protocol inflation, is **5.6M FIL**. Filecoin mints block rewards on two schedules — a time-based release and a network-performance-based release — that both decay over time, and each reward vests to its storage provider over 180 days. Reading the on-chain minted component at both window ends, only **5.6M FIL** of block reward cleared vesting and reached liquid supply over the 90 days, a strikingly small figure for a chain this size and a direct consequence of how far minting has fallen from its early peak. On its own, the mint would put FIL near **+0.7%**.

Sell #2, vesting unlocks, is **16.8M FIL** and is the largest single source of new supply. The genesis allocations — early SAFT investors, **Protocol Labs** and the **Filecoin Foundation** — vest linearly over six years from the Oct 15 2020 mainnet launch, and that vesting is still running at roughly **187,000 FIL a day**. The six-year schedule completes around **Oct 15 2026**, which falls inside the next-90-day window, so this row is measured at its full trailing rate now but projected to taper as the cliff-end approaches. Sell #3, foundation and unscheduled unlocks, is **zero**: the 300M FIL mining reserve is the one large discretionary overhang, but only about **17.1M** of it has ever been disbursed and that figure did not move over the window. Sell #4, long-term locked or bankruptcy, is **zero** — there is no estate, trustee or court-ordered FIL distribution.

Sell #5 is Filecoin-specific and it is large: **16.1M FIL** of **released pledge collateral**. Storage providers must lock FIL as collateral to prove capacity, and that locked FIL sits outside circulating supply; when providers terminate sectors, the collateral returns to their liquid balances. Over this window protocol-locked FIL fell by about **16.1M**, to roughly **66.5M**, as network storage power consolidated, and that freed collateral is already-minted FIL re-entering the tradable float. It is not new issuance, but it is real supply reaching the market, and it is measured directly as the drop in on-chain locked supply rather than estimated.

## Buy pressure: where new FIL goes

Buy #1, programmatic buyback, is **zero**. Filecoin runs no protocol buyback and no revenue-funded purchase contract; the network's fee income is destroyed rather than recycled into FIL repurchases. Buy #2, protocol fee burn, is **0.64M FIL** — the only non-zero buy row. Filecoin burns FIL through message base fees, the per-sector daily fee introduced in the 2025 **FIP-0100** upgrade, and storage-provider penalties. That burn is real, but at **0.64M** against **38.5M** of new supply it offsets under two percent of the sell side, because on-chain transaction activity is low relative to the size of the token base.

Buy #3, foundation buy, is **zero**: neither Protocol Labs nor the Filecoin Foundation has disclosed an open-market FIL purchase, and no accumulation wallet has been identified. Buy #4, new long-term lock, is **zero** and deserves a note, because pledge collateral is a lock and locking would normally count here. Over this window collateral fell rather than grew — the network released more than it locked — so the net movement appears on the sell side as Sell #5 rather than as a buy-side offset. A return to net storage-power growth would flip that flow and start removing FIL from the float again.

## Foundation and overhang

One large team-controlled overhang is tracked on Filecoin: the **300M FIL mining reserve**, of which only about **17.1M** has ever been disbursed, leaving roughly **283M FIL** undisbursed. That reserve sits outside circulating supply and cannot enter the market without a governance decision — a standing governance discussion has even proposed burning part of it rather than releasing it. The vesting allocations to Protocol Labs and the Filecoin Foundation are already captured in Sell #2 as they release, so they are not double-counted here. Both the reserve and the vesting wallets are re-read on every rebuild, and if the disbursed reserve balance rises between refreshes, that outflow enters Sell #3 at the next refresh.

## How FIL compares to other capped-supply networks

The first comparison is cap versus float. Filecoin has a hard **2 billion** maximum, which superficially resembles a halving-model coin, but the resemblance is thin. A halving chain releases new supply on a fixed schedule and has no vesting overhang; Filecoin's dominant supply force is not its mint at all but its **six-year genesis vesting**, a fixed-term investor-and-team release that a pure mining chain simply does not have. That makes FIL's current inflation a countdown rather than a curve — the vesting ends in **October 2026**, and when it does the single largest tap closes for good.

The second comparison is collateral. Filecoin is unusual among large tokens in that a big slice of its supply is bonded as **pledge collateral** tied to physical storage capacity, so its circulating supply moves with network power in a way most chains never experience. When power grows, FIL is locked and the float shrinks; when power falls, FIL is freed and the float grows. Over this window the network was consolidating, which turned collateral into a **16.1M** source of sell pressure — a mechanism with no analogue on a proof-of-stake chain, where staked tokens stay inside the circulating count.

The third comparison is burn. Fee-burning networks route a share of every transaction fee to destruction, so heavy usage can drive net supply negative. Filecoin does burn fees, and the 2025 per-sector daily fee added a second burn path, but at current activity the total is a **0.64M** rounding error against a **38.5M** sell side. Combined with the absence of any buyback, that leaves FIL firmly in the group of capped assets whose cap is still a distant ceiling rather than a live constraint.

## What to watch in the next 90 days

First and most important, the **Oct 15 2026** vesting completion: the six-year SAFT, Protocol Labs and Foundation schedules end within the window, removing roughly **187,000 FIL a day** of structural sell pressure once they run out. Second, network storage power: the pledge-collateral release in Sell #5 exists only because power is falling, and a stabilisation or recovery would cut that **16.1M** flow or flip it back into a buy-side lock. Third, the block-reward mint, which keeps decaying and will print a little less each window. Fourth, the mining reserve — any governance action that disburses part of the undisbursed **283M FIL**, or the standing proposal to burn it, would be the first thing to put a non-zero number in Sell #3. Fifth, on-chain fee activity, the only lever that could grow the burn into a meaningful offset.

## Summary

Filecoin (FIL) is structurally inflationary on three independent taps with almost nothing on the other side: a decaying block-reward mint added **5.6M FIL** over 90 days, six-year genesis vesting added **16.8M**, and freed pledge collateral added **16.1M**, against a fee burn of **0.64M** and no buyback — a framework reading of **+4.64% net** against a monitor reading of **+4.71%**. The key feature is that the largest tap is temporary: the vesting completes in **October 2026**, after which supply growth should ease sharply toward the mint alone. The key risk is the mirror image of the current tailwind — a further decline in network power keeps freeing collateral, and the 283M-FIL mining reserve remains a governance decision away from the market. FIL is capped at 2 billion, but at 815.5M circulating that ceiling is years off and not the binding constraint today.

---

*MrNasdog Pressure Framework analysis of FIL, Metric 1 — Inflation. Data + explanation only. Not financial advice. Updated Aug 5 2026.*
